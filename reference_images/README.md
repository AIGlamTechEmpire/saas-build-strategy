# Reference images

Put exactly **10** reference photos of the subject here before running the batch
script. `batch_generate.py` uploads all 10 once and passes them to every single
generation call, which is how the prompts' "IDENTITY LOCK" / "IDENTITY
REFERENCE PROTOCOL" instructions get honored -- the model reads the face from
these files, not from text.

Guidelines for the 10 photos (matters more than any prompt wording):
- Real, unedited photos of the same person -- no filters, no beauty AI.
- A mix of angles: straight-on, both profiles, a 3/4 view, a couple of
  full-body shots, a couple of close-ups.
- Even, natural lighting. Avoid heavy shadow on one side of the face.
- Recent photos, consistent with the "apparent age and build" the prompts
  ask every plate to hold constant.

Accepted formats: `.jpg`, `.jpeg`, `.png`, `.webp`.

This folder (and its contents) is gitignored on purpose -- these are personal
photos and shouldn't end up in the repo.
