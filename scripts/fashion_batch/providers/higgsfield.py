"""Higgsfield client, built on the official `higgsfield-client` SDK
(pip install higgsfield-client -- github.com/higgsfield-ai/higgsfield-client).

Verified by installing the package and reading its source (docs.higgsfield.ai
was unreachable from this environment):
  - SyncClient(api_key=...).subscribe(model, arguments={...}) submits a job and
    blocks until it finishes, returning the JSON result (result["images"][0]["url"]).
  - SyncClient(api_key=...).upload_file(path) uploads a local file and returns a URL.
  - The SDK already retries HTTP 408/429/500/502/503/504 internally (3x, exponential
    backoff -- higgsfield_client/http/retry.py) and raises HiggsfieldClientError once
    retries are exhausted or on any other status code. It does NOT retry a bare
    connection failure (DNS hiccup, dropped connection, read timeout) -- those
    surface immediately as httpx.TransportError -- so that's the one case this
    wrapper adds its own retry for.

BEST-EFFORT AREA: the SDK's README only documents plain text-to-image generation.
There's no public reference for the exact argument name a given Higgsfield model
expects for multiple identity/reference images, so `reference_arg_name` defaults
to "image_urls" (the convention Krea's mirror of the same underlying models
uses). Confirm this against your workspace's model schema and adjust
HIGGSFIELD_MODEL / HIGGSFIELD_REFERENCE_ARG in .env if the 2-prompt dry run's
saved raw_response.json shows it was ignored.

If you're driving this from inside Claude Code rather than as a standalone
script, Higgsfield's Soul Character feature (train once on your 10 photos, then
reuse the returned soul_id across every generation with model="soul_2") is a
better fit for "one identity, many shots" than passing loose reference images
on every call -- see the README for how to do that instead.
"""
from __future__ import annotations

from pathlib import Path

import requests

from .base import GenerationResult, ImageProvider, ProviderError, TransientProviderError

TRANSPORT_ERROR_ATTEMPTS = 4
TRANSPORT_ERROR_BASE_DELAY = 2.0


class HiggsfieldProvider(ImageProvider):
    name = "higgsfield"

    def __init__(
        self,
        hf_key: str | None = None,
        hf_api_key: str | None = None,
        hf_api_secret: str | None = None,
        model: str = "bytedance/seedream/v4/text-to-image",
        reference_arg_name: str = "image_urls",
        extra_arguments: dict | None = None,
    ) -> None:
        try:
            import higgsfield_client
        except ImportError as exc:
            raise ProviderError(
                "The higgsfield-client package is not installed. Run: pip install higgsfield-client"
            ) from exc
        try:
            import httpx
        except ImportError as exc:
            raise ProviderError("httpx is required by higgsfield-client but is not installed.") from exc

        if hf_key:
            combined_key = hf_key
        elif hf_api_key and hf_api_secret:
            combined_key = f"{hf_api_key}:{hf_api_secret}"
        else:
            raise ProviderError(
                "Higgsfield credentials are missing (set HF_KEY, or HF_API_KEY + HF_API_SECRET)."
            )

        self._client = higgsfield_client.SyncClient(api_key=combined_key)
        self._client_error = higgsfield_client.HiggsfieldClientError
        self._transport_error = httpx.TransportError
        self.model = model
        self.reference_arg_name = reference_arg_name
        self.extra_arguments = extra_arguments or {}

    def _with_transport_retry(self, fn, what: str):
        last_error: Exception | None = None
        for attempt in range(1, TRANSPORT_ERROR_ATTEMPTS + 1):
            try:
                return fn()
            except self._client_error as exc:
                # SDK already exhausted its own retries for HTTP-status failures; this is final.
                raise ProviderError(f"Higgsfield {what} failed: {exc}") from exc
            except self._transport_error as exc:
                last_error = exc
                if attempt == TRANSPORT_ERROR_ATTEMPTS:
                    raise TransientProviderError(f"Higgsfield {what} network error: {exc}") from exc
                import time

                time.sleep(TRANSPORT_ERROR_BASE_DELAY * (2 ** (attempt - 1)))
        raise ProviderError(f"Higgsfield {what} failed: {last_error}")

    def upload_reference_images(self, paths: list[Path]) -> list[str]:
        urls = []
        for path in paths:
            url = self._with_transport_retry(
                lambda p=path: self._client.upload_file(p), f"upload of {path.name}"
            )
            urls.append(url)
        return urls

    def generate(self, prompt: str, reference_refs: list[str], aspect_ratio: str) -> GenerationResult:
        arguments = {"prompt": prompt, "aspect_ratio": aspect_ratio}
        if reference_refs:
            arguments[self.reference_arg_name] = reference_refs
        arguments.update(self.extra_arguments)

        result = self._with_transport_retry(
            lambda: self._client.subscribe(self.model, arguments=arguments), "generate"
        )
        images = result.get("images") or []
        if not images:
            raise ProviderError(f"Higgsfield generate returned no images: {result}")
        image_url = images[0].get("url")
        if not image_url:
            raise ProviderError(f"Higgsfield image entry had no url: {images[0]}")

        image_resp = requests.get(image_url, timeout=60)
        image_resp.raise_for_status()
        return GenerationResult(image_bytes=image_resp.content, raw_response=result)
