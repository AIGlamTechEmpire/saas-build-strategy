#!/usr/bin/env python3
"""Batch-generate the fashion content calendar images via Krea or Higgsfield.

ALWAYS test with a couple of prompts before running the full batch:
    python batch_generate.py --provider krea --limit 2

That does two real generations end to end, so a bad API key, a wrong
reference-image folder, or a bad model name shows up immediately instead of
on prompt 87. Once that looks right, drop --limit to run the whole set:
    python batch_generate.py --provider krea

See README.md in this folder for setup (API keys, reference images, etc).
"""
from __future__ import annotations

import argparse
import csv
import dataclasses
import logging
import json
import os
import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

from providers import PROVIDERS, ProviderError  # noqa: E402
from providers.base import retry_call  # noqa: E402

ACCEPTED_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
REQUIRED_REFERENCE_IMAGE_COUNT = 10
MANIFEST_FIELDS = [
    "id", "set", "title", "status", "aspect_ratio", "image_file", "prompt_file",
    "provider", "model", "started_at", "finished_at", "duration_s", "attempts", "error",
]


@dataclasses.dataclass
class ManifestRow:
    id: str
    set: str
    title: str
    status: str
    aspect_ratio: str
    image_file: str = ""
    prompt_file: str = ""
    provider: str = ""
    model: str = ""
    started_at: str = ""
    finished_at: str = ""
    duration_s: str = ""
    attempts: str = ""
    error: str = ""


def load_dotenv_if_present(path: Path) -> None:
    """Tiny KEY=VALUE .env loader so this doesn't need python-dotenv installed.
    Never overrides a variable already set in the real environment."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def build_logger(log_path: Path) -> logging.Logger:
    logger = logging.getLogger("fashion_batch")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s", "%H:%M:%S")
    stream = logging.StreamHandler()
    stream.setFormatter(fmt)
    logger.addHandler(stream)
    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setFormatter(fmt)
    logger.addHandler(file_handler)
    return logger


def load_prompts(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def select_prompts(data: dict, which: str) -> list[dict]:
    studio = [{**p, "set": p.get("set", "Studio Plates")} for p in data["studio_plates"]]
    lifestyle = data["lifestyle_prompts"]
    if which == "studio":
        return studio
    if which == "lifestyle":
        return lifestyle
    if which == "all":
        return studio + lifestyle
    raise ValueError(f"Unknown --set value: {which}")


def find_reference_images(directory: Path) -> list[Path]:
    if not directory.is_dir():
        raise SystemExit(
            f"Reference image folder not found: {directory}\n"
            f"Create it and put your 10 reference photos in it (see README.md)."
        )
    return sorted(
        p for p in directory.iterdir()
        if p.is_file() and p.suffix.lower() in ACCEPTED_IMAGE_EXTENSIONS
    )


def build_provider(args):
    if args.provider == "krea":
        api_key = os.environ.get("KREA_API_KEY")
        if not api_key:
            raise SystemExit("KREA_API_KEY is not set. Add it to .env or export it (see README.md).")
        return PROVIDERS["krea"](
            api_key=api_key,
            model=os.environ.get("KREA_MODEL", "google/nano-banana-pro"),
            reference_field=os.environ.get("KREA_REFERENCE_FIELD", "image_urls"),
            resolution=os.environ.get("KREA_RESOLUTION", "2K") or None,
        )
    if args.provider == "higgsfield":
        return PROVIDERS["higgsfield"](
            hf_key=os.environ.get("HF_KEY"),
            hf_api_key=os.environ.get("HF_API_KEY"),
            hf_api_secret=os.environ.get("HF_API_SECRET"),
            model=os.environ.get("HIGGSFIELD_MODEL", "bytedance/seedream/v4/text-to-image"),
            reference_arg_name=os.environ.get("HIGGSFIELD_REFERENCE_ARG", "image_urls"),
        )
    raise SystemExit(f"Unknown provider: {args.provider}")


def write_manifest(path: Path, rows: dict[str, ManifestRow]) -> None:
    tmp_path = path.with_suffix(".csv.tmp")
    with open(tmp_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=MANIFEST_FIELDS)
        writer.writeheader()
        for row in rows.values():
            writer.writerow(dataclasses.asdict(row))
    tmp_path.replace(path)


def load_manifest(path: Path) -> dict[str, ManifestRow]:
    rows: dict[str, ManifestRow] = {}
    if not path.exists():
        return rows
    with open(path, "r", newline="", encoding="utf-8") as fh:
        for raw in csv.DictReader(fh):
            rows[raw["id"]] = ManifestRow(**{k: raw.get(k, "") or "" for k in MANIFEST_FIELDS})
    return rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--provider", choices=sorted(PROVIDERS), required=True)
    parser.add_argument("--set", choices=["lifestyle", "studio", "all"], default="lifestyle",
                         help="Which prompts to run (default: lifestyle, the 001-099 'Authentically You' set).")
    parser.add_argument("--limit", type=int, default=None,
                         help="Only process the first N prompts. Use --limit 2 to test before running the full batch.")
    parser.add_argument("--prompts-file", type=Path, default=SCRIPT_DIR / "prompts.json")
    parser.add_argument("--reference-dir", type=Path, default=REPO_ROOT / "reference_images")
    parser.add_argument("--output-dir", type=Path, default=REPO_ROOT / "output")
    parser.add_argument("--prefix", default="portrait", help="Output filename prefix (default: portrait -> portrait_001.png).")
    parser.add_argument("--attempts", type=int, default=3,
                         help="Retries per prompt on transient errors (timeouts, network blips, HTTP 429/5xx).")
    parser.add_argument("--retry-base-delay", type=float, default=5.0, help="Seconds before the first retry; doubles each attempt.")
    parser.add_argument("--overwrite", action="store_true", help="Regenerate images that already exist instead of skipping them.")
    parser.add_argument("--allow-any-reference-count", action="store_true",
                         help="Skip the check that exactly 10 reference images are present.")
    parser.add_argument("--env-file", type=Path, default=REPO_ROOT / ".env")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    load_dotenv_if_present(args.env_file)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    logger = build_logger(args.output_dir / "run.log")

    data = load_prompts(args.prompts_file)
    prompts = select_prompts(data, args.set)
    if args.limit is not None:
        prompts = prompts[: args.limit]
    logger.info("Loaded %d prompt(s) from %s (set=%s)", len(prompts), args.prompts_file, args.set)
    if not prompts:
        logger.error("No prompts selected, nothing to do.")
        return 1

    reference_images = find_reference_images(args.reference_dir)
    if not args.allow_any_reference_count and len(reference_images) != REQUIRED_REFERENCE_IMAGE_COUNT:
        raise SystemExit(
            f"Expected exactly {REQUIRED_REFERENCE_IMAGE_COUNT} reference images in {args.reference_dir}, "
            f"found {len(reference_images)}: {[p.name for p in reference_images]}\n"
            f"Fix the folder, or pass --allow-any-reference-count to proceed anyway."
        )
    logger.info("Using %d reference image(s): %s", len(reference_images), ", ".join(p.name for p in reference_images))

    try:
        provider = build_provider(args)
    except ProviderError as exc:
        logger.error("Could not set up provider %r: %s", args.provider, exc)
        return 1

    logger.info("Uploading %d reference image(s) to %s (once, reused for every prompt)...",
                len(reference_images), provider.name)
    try:
        reference_refs = provider.upload_reference_images(reference_images)
    except ProviderError as exc:
        logger.error("Reference image upload failed, aborting before any generation calls: %s", exc)
        return 1
    logger.info("Reference images uploaded.")

    manifest_path = args.output_dir / "manifest.csv"
    manifest = load_manifest(manifest_path)

    succeeded = failed = skipped = 0
    for prompt_entry in prompts:
        pid = prompt_entry["id"]
        title = prompt_entry.get("title", "")
        prompt_set = prompt_entry.get("set", "")
        aspect_ratio = prompt_entry.get("aspect_ratio", "")
        prompt_text = prompt_entry["prompt"]

        base_name = f"{args.prefix}_{pid}"
        image_path = args.output_dir / f"{base_name}.png"
        prompt_path = args.output_dir / f"{base_name}.txt"

        if image_path.exists() and not args.overwrite:
            logger.info("[%s] %s -- already exists, skipping (use --overwrite to regenerate)", pid, title)
            skipped += 1
            continue

        logger.info("[%s] %s -- generating...", pid, title)
        started_at = time.strftime("%Y-%m-%dT%H:%M:%S")
        t0 = time.monotonic()
        row = ManifestRow(
            id=pid, set=prompt_set, title=title, status="error", aspect_ratio=aspect_ratio,
            provider=provider.name, model=getattr(provider, "model", ""), started_at=started_at,
        )
        attempts_used = 0

        def attempt_once():
            nonlocal attempts_used
            attempts_used += 1
            return provider.generate(prompt_text, reference_refs, aspect_ratio)

        try:
            result = retry_call(
                attempt_once,
                attempts=args.attempts,
                base_delay=args.retry_base_delay,
                what=f"[{pid}] {title}",
                log=logger.warning,
            )
            image_path.write_bytes(result.image_bytes)
            prompt_path.write_text(prompt_text, encoding="utf-8")
            row.status = "success"
            row.image_file = image_path.name
            row.prompt_file = prompt_path.name
            succeeded += 1
            logger.info("[%s] %s -- saved %s", pid, title, image_path.name)
        except Exception as exc:  # noqa: BLE001 -- deliberate: one bad prompt must never kill the batch
            row.status = "error"
            row.error = str(exc)[:500]
            failed += 1
            logger.error("[%s] %s -- FAILED after %d attempt(s): %s", pid, title, attempts_used, exc)
        finally:
            row.attempts = str(attempts_used)
            row.finished_at = time.strftime("%Y-%m-%dT%H:%M:%S")
            row.duration_s = f"{time.monotonic() - t0:.1f}"
            manifest[pid] = row
            write_manifest(manifest_path, manifest)  # rewritten after every item so a crash never loses progress

    logger.info(
        "Done. %d succeeded, %d failed, %d skipped (already existed). Manifest: %s",
        succeeded, failed, skipped, manifest_path,
    )
    return 1 if failed and not succeeded else 0


if __name__ == "__main__":
    raise SystemExit(main())
