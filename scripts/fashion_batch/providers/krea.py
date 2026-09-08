"""Krea REST API client.

Verified against Krea's own published OpenAPI spec (the docs.krea.ai site itself
was unreachable from this environment, so this was cross-checked against the
community-maintained mirror at github.com/api-evangelist/krea-ai instead of the
live docs page -- re-confirm against https://docs.krea.ai if any field below
ever 400s, and see the README for how to do that from your dry run's raw output).

Confirmed shape:
  Base URL     https://api.krea.ai
  Auth         Authorization: Bearer <KREA_API_KEY>
  Upload       POST /assets                                  multipart "file" -> {"image_url": ...}
  Generate     POST /generate/image/{provider}/{model}        JSON body -> {"job_id": ..., "status": ...}
  Poll         GET  /jobs/{job_id}                             -> {"status": ..., "result": {"urls": [...]}}

Models that accept multiple reference images via "image_urls" (good fits for the
10-image identity lock this batch needs): google/nano-banana-pro, google/nano-banana-2,
google/nano-banana, openai/gpt-image, openai/gpt-image-2 (max 10 image_urls).
ideogram/ideogram-3 instead uses "character_reference_images" for the same idea.
Pick with KREA_MODEL / KREA_REFERENCE_FIELD in .env -- see README.
"""
from __future__ import annotations

import mimetypes
import time
from pathlib import Path

import requests

from .base import GenerationResult, ImageProvider, ProviderError, TransientProviderError

BASE_URL = "https://api.krea.ai"
TERMINAL_OK = {"completed"}
TERMINAL_FAIL = {"failed", "cancelled"}
IN_PROGRESS = {"backlogged", "queued", "scheduled", "processing", "sampling", "intermediate-complete"}


class KreaProvider(ImageProvider):
    name = "krea"

    def __init__(
        self,
        api_key: str,
        model: str = "google/nano-banana-pro",
        reference_field: str = "image_urls",
        resolution: str | None = "2K",
        extra_params: dict | None = None,
        poll_interval: float = 4.0,
        poll_timeout: float = 420.0,
        http_attempts: int = 4,
        http_base_delay: float = 2.0,
        http_timeout: float = 60.0,
    ) -> None:
        if not api_key:
            raise ProviderError("Krea API key is missing (set KREA_API_KEY).")
        self.api_key = api_key
        self.model = model
        self.reference_field = reference_field
        self.resolution = resolution
        self.extra_params = extra_params or {}
        self.poll_interval = poll_interval
        self.poll_timeout = poll_timeout
        self.http_attempts = http_attempts
        self.http_base_delay = http_base_delay
        self.http_timeout = http_timeout
        self._session = requests.Session()

    def _headers(self) -> dict:
        return {"Authorization": f"Bearer {self.api_key}"}

    def _request(self, method: str, url: str, **kwargs) -> requests.Response:
        last_error: Exception | None = None
        for attempt in range(1, self.http_attempts + 1):
            try:
                resp = self._session.request(
                    method, url, headers=self._headers(), timeout=self.http_timeout, **kwargs
                )
            except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as exc:
                last_error = TransientProviderError(f"{method} {url} network error: {exc}")
            else:
                if resp.status_code == 429 or resp.status_code >= 500:
                    last_error = TransientProviderError(
                        f"{method} {url} returned HTTP {resp.status_code}: {resp.text[:300]}"
                    )
                elif resp.status_code >= 400:
                    raise ProviderError(f"{method} {url} returned HTTP {resp.status_code}: {resp.text[:500]}")
                else:
                    return resp
            if attempt < self.http_attempts:
                time.sleep(self.http_base_delay * (2 ** (attempt - 1)))
        raise last_error  # type: ignore[misc]

    def upload_reference_images(self, paths: list[Path]) -> list[str]:
        urls = []
        for path in paths:
            mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
            with open(path, "rb") as fh:
                resp = self._request(
                    "POST",
                    f"{BASE_URL}/assets",
                    files={"file": (path.name, fh, mime)},
                )
            data = resp.json()
            image_url = data.get("image_url")
            if not image_url:
                raise ProviderError(f"Krea upload of {path} did not return image_url: {data}")
            urls.append(image_url)
        return urls

    def generate(self, prompt: str, reference_refs: list[str], aspect_ratio: str) -> GenerationResult:
        body: dict = {"prompt": prompt}
        if reference_refs:
            body[self.reference_field] = reference_refs
        if aspect_ratio:
            body["aspect_ratio"] = aspect_ratio
        if self.resolution:
            body["resolution"] = self.resolution
        body.update(self.extra_params)

        submit_resp = self._request("POST", f"{BASE_URL}/generate/image/{self.model}", json=body)
        submit_data = submit_resp.json()
        job_id = submit_data.get("job_id")
        if not job_id:
            raise ProviderError(f"Krea generate did not return a job_id: {submit_data}")

        deadline = time.monotonic() + self.poll_timeout
        status = submit_data.get("status", "queued")
        poll_data = submit_data
        while status in IN_PROGRESS:
            if time.monotonic() > deadline:
                raise TransientProviderError(
                    f"Krea job {job_id} did not finish within {self.poll_timeout:.0f}s (last status={status})"
                )
            time.sleep(self.poll_interval)
            poll_resp = self._request("GET", f"{BASE_URL}/jobs/{job_id}")
            poll_data = poll_resp.json()
            status = poll_data.get("status")

        if status in TERMINAL_FAIL:
            raise ProviderError(f"Krea job {job_id} ended with status={status}: {poll_data}")
        if status not in TERMINAL_OK:
            raise ProviderError(f"Krea job {job_id} ended with unrecognized status={status}: {poll_data}")

        urls = (poll_data.get("result") or {}).get("urls") or []
        if not urls:
            raise ProviderError(f"Krea job {job_id} completed but returned no result urls: {poll_data}")

        image_resp = self._request("GET", urls[0])
        return GenerationResult(image_bytes=image_resp.content, raw_response=poll_data)
