# Assets

## Action needed: save the reference image here

The canonical Aoi Freeman reference image was shared in chat but not as a file
on disk, so it could not be committed automatically. **Save it here before
generating anything:**

```
content/assets/aoi-freeman-ref-01.png
```

Everything downstream depends on it. The character bible describes her design in
enough detail to regenerate her from text alone, but text drifts. Image-to-image
or character-reference generation from this file is what actually keeps her the
same person across fifteen days of posts.

## Naming convention

```
aoi-freeman-ref-01.png          canonical reference, never overwrite
aoi-<pose>-<YYYY-MM-DD>.png     approved renders
day-<NN>-slide-<N>.png          finished carousel slides
day-<NN>-tiktok.mp4             finished vertical video
```

## Approved render library

Build these six and most of the calendar can be assembled without new
generations:

- [ ] `aoi-hero` — full body, standing, rooftop
- [ ] `aoi-teaching` — mid-gesture, explaining
- [ ] `aoi-arms-folded` — direct address, level expression
- [ ] `aoi-pointing-out` — gesturing toward the city
- [ ] `aoi-three-quarter` — turning toward camera
- [ ] `aoi-workstation` — seated at a glowing studio desk, interior

Every one passes the seven-point QC checklist in
`../AOI-FREEMAN-CHARACTER-BIBLE.md` before it goes in this folder. A render that
lands in here is treated as canon by everything after it, so nothing off-model
gets saved.
