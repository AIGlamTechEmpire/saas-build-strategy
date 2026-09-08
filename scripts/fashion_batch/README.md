# Fashion photo batch generator

Batch-runs the "Authentically You" prompt set (99 lifestyle prompts + 4 studio
plates, see `prompts.json`) against **Krea** or **Higgsfield**, holding one
identity constant across every image via 10 uploaded reference photos.

## 1. Install

```bash
pip install -r ../../requirements.txt
```

(from this folder; or `pip install -r requirements.txt` from the repo root.)

## 2. Get API keys

**Krea** -- create an account at krea.ai, then generate an API key from your
account's API settings (docs at https://docs.krea.ai). Put it in `.env` as
`KREA_API_KEY`.

**Higgsfield** -- get credentials from Higgsfield Cloud (docs at
https://docs.higgsfield.ai/docs). Either a single combined key as `HF_KEY`, or
`HF_API_KEY` + `HF_API_SECRET` separately.

Copy the template and fill it in:

```bash
cp ../../.env.example ../../.env
```

## 3. Add your 10 reference photos

Put exactly 10 photos of the subject in `reference_images/` at the repo root
(see the README in that folder for what makes a good reference set). The
script uploads all 10 once and reuses them for every prompt -- that's what
makes the "IDENTITY LOCK" instructions baked into every prompt actually work.

## 4. Test with 2 prompts first

**Always do this before running the full batch.** It burns 2 generations
instead of 99+, and surfaces a bad API key, wrong folder, or bad model name
immediately instead of on prompt 87:

```bash
python batch_generate.py --provider krea --limit 2
```

Check `output/portrait_001.png` and `.txt`, and `output/manifest.csv`, before
continuing. Swap `--provider krea` for `--provider higgsfield` to test that
path instead.

## 5. Run the full batch

```bash
python batch_generate.py --provider krea
```

Re-running the same command later **skips prompts that already produced an
image** (pass `--overwrite` to force regeneration). That, plus the manifest
being rewritten after every single image, means killing the process partway
through and re-running later picks up where it left off instead of starting
over or losing the record of what already succeeded.

Other useful flags:

| Flag | Default | What it does |
|---|---|---|
| `--set {lifestyle,studio,all}` | `lifestyle` | `lifestyle` = the 99 numbered "Authentically You" prompts, `studio` = the 4 white-cyclorama plates, `all` = both. |
| `--limit N` | none | Only run the first N prompts of the selected set. |
| `--attempts N` | `3` | Retries per prompt on transient errors (timeouts, network blips, HTTP 429/5xx) before that one prompt is logged as failed. |
| `--overwrite` | off | Regenerate images that already exist instead of skipping them. |
| `--output-dir` | `../../output` | Where images, prompt sidecars, `manifest.csv`, and `run.log` are written. |

## What gets saved

For every prompt, e.g. id `042`:

- `output/portrait_042.png` -- the generated image
- `output/portrait_042.txt` -- the exact prompt text used to make it
- a row in `output/manifest.csv` (id, title, status, image/prompt filenames,
  provider, model, timestamps, attempt count, error message if it failed)
- `output/run.log` -- full run log (same content as the console output)

So "which prompt made which image" is always answerable three ways: by
filename pairing, by opening the manifest, or by grepping the log.

## Error handling

A failure on one prompt is caught, logged (to the console, `run.log`, and as
an `error` row in `manifest.csv`), and the batch moves on -- it never stops
the run. Timeouts, connection blips, HTTP 429s, and 5xx responses are retried
automatically with exponential backoff (`--attempts`, `--retry-base-delay`)
before being logged as a failure. Non-retryable errors (bad API key, invalid
prompt, content policy rejection) fail that one prompt immediately without
wasting retries, then move on to the next one.

## Known caveats -- read before you run 99 generations

- **Prompt #100 is missing.** The brief this was built from was titled "One
  Hundred Authentically You Lifestyle Prompts" but only numbered 001-099 were
  actually provided (Set Ten has 9 entries, not 10). `prompts.json` has 99
  lifestyle prompts + 4 studio plates = 103 total. Add #100 to
  `lifestyle_prompts` in `prompts.json` if you have it.
- **Krea's exact request fields were confirmed from a third-party OpenAPI
  mirror** (github.com/api-evangelist/krea-ai), not Krea's own docs site,
  which this environment couldn't reach. The 2-prompt dry run is the real
  check -- if it 400s, open `output/manifest.csv`'s error column, or the
  Krea job's raw response, and adjust `KREA_MODEL` / `KREA_REFERENCE_FIELD`
  in `.env` accordingly.
- **Higgsfield's reference-image argument name is a best-effort default**
  (`image_urls`, same convention Krea uses for the same underlying models).
  Higgsfield's own API docs were also unreachable from here. Confirm the
  argument name for your chosen model and set `HIGGSFIELD_REFERENCE_ARG` /
  `HIGGSFIELD_MODEL` if needed.
- **4:5 aspect ratio and Higgsfield's Soul model don't mix.** Many lifestyle
  prompts ask for `[4:5]`. Krea's `google/nano-banana-pro` (the default)
  supports 4:5 natively. Higgsfield's Soul 2.0 model does not -- its closest
  option is `3:4`.
- **10 reference images is enforced by default.** The script refuses to run
  if `reference_images/` doesn't contain exactly 10 image files (pass
  `--allow-any-reference-count` to override).

## A better option for Higgsfield if you're running this from inside Claude Code

Higgsfield is already connected to this session as a native tool integration
(no API key needed here at all), and it has a purpose-built feature for
exactly this "one identity, many shots" case: **Soul Characters**. You train
a reusable identity model once from 5-20 photos (your 10 fit) and then every
generation just references a `soul_id` instead of re-attaching loose photos
each time -- it's a better mechanistic fit than what this standalone script
does for Higgsfield. Ask me to run the batch that way instead if you'd rather
not manage a separate Higgsfield API key at all.
