"""Common interface every image-generation provider implements.

Keeping this tiny on purpose: batch_generate.py only needs "upload my 10
reference images once" and "generate one image for one prompt."
"""
from __future__ import annotations

import dataclasses
import time
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Callable, TypeVar

T = TypeVar("T")


class ProviderError(RuntimeError):
    """Any failure talking to a provider. The batch runner catches this per-prompt so one
    bad prompt (or a dead API key) never takes down the rest of the queue."""


class TransientProviderError(ProviderError):
    """A failure worth retrying automatically: timeouts, connection resets, HTTP 429/5xx."""


@dataclasses.dataclass
class GenerationResult:
    image_bytes: bytes
    raw_response: dict


class ImageProvider(ABC):
    name: str

    @abstractmethod
    def upload_reference_images(self, paths: list[Path]) -> list[str]:
        """Upload the local reference images once and return provider-side handles
        (URLs or ids) to reuse for every prompt in the batch."""

    @abstractmethod
    def generate(self, prompt: str, reference_refs: list[str], aspect_ratio: str) -> GenerationResult:
        """Run one generation synchronously (submits + polls internally if the
        provider is async) and return the finished image bytes."""


def retry_call(
    fn: Callable[[], T],
    *,
    attempts: int,
    base_delay: float,
    what: str,
    log: Callable[[str], None],
) -> T:
    """Retry `fn()` with exponential backoff. Only retries TransientProviderError;
    anything else (bad API key, invalid prompt, etc.) fails immediately since
    retrying it would just waste time and API credits."""
    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            return fn()
        except TransientProviderError as exc:
            last_error = exc
            if attempt == attempts:
                break
            delay = base_delay * (2 ** (attempt - 1))
            log(f"{what}: transient error ({exc}) - retry {attempt}/{attempts - 1} in {delay:.0f}s")
            time.sleep(delay)
    raise last_error  # type: ignore[misc]
