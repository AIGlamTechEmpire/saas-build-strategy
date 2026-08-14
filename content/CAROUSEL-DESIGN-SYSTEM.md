# Carousel Design System — Founding Creators Studio

Everything in the 15-day calendar is built on this system. Set it up once and
every day after is assembly, not design.

---

## 1. Canvas specs

| Platform | Size | Notes |
|---|---|---|
| **Instagram carousel (primary)** | 1080 × 1350 (4:5) | Takes the most feed height. This is the master. |
| **Facebook carousel** | Same 1080 × 1350 files | Facebook accepts 4:5. Repost the identical images. |
| **TikTok photo/video** | 1080 × 1920 (9:16) | Re-export the master with extra top and bottom padding. |

**Safe area:** keep all text inside a 90px margin on every edge. Instagram
crops the preview and TikTok covers the bottom third with its own UI.

---

## 2. The slide grid

Every carousel uses the same seven-slide architecture. Never pad to hit seven —
if a topic only supports five, ship five.

| Slide | Job | Copy limit |
|---|---|---|
| 1 | **Hook.** Stop the thumb. | 12 words or fewer |
| 2 | **Tension.** Name the gap they feel. | Headline + 1 line |
| 3–5 | **Value.** One single idea each. | Headline + 1–2 lines |
| 6 | **Payoff.** What's possible now. | Headline + 1 line |
| 7 | **CTA.** One action. | Headline + 1 line + handle |

**One idea per slide.** If a slide has two thoughts, it's two slides.

---

## 3. Visual template

**Background.** Vertical gradient, Midnight Indigo `#12082E` at the top through
Royal Violet `#4C1D95` to Aoi Purple `#7C3AED` at the bottom. Add a faint
neon-city silhouette at 8% opacity along the bottom edge so the whole set feels
like it lives in Aoi's world.

**Slide 1.** Aoi at right or left third, full or three-quarter body, with the
hook text stacked in the opposite third. Her hair glow should bleed behind the
text — that's the visual signature.

**Slides 2–6.** Aoi small or absent. These are text slides and the text has to
breathe. When she appears, she's a cut-out at a bottom corner at about 35% of
the slide height, never behind the copy.

**Slide 7.** Aoi returns at full presence, gesturing outward. Founder Gold
`#FBBF24` appears here and only here if the founding rate is mentioned.

**Type scale.** Atkinson Hyperlegible throughout.

| Element | Size | Color |
|---|---|---|
| Hook headline | 96–120px Bold | Studio Cream `#FEF9EE` |
| Slide headline | 64–72px Bold | Studio Cream `#FEF9EE` |
| Emphasis word | same size | Electric Magenta `#D946EF` |
| Body line | 38–44px Regular | Glow Lilac `#E9D5FF` |
| Slide number | 28px Regular | Neon Orchid `#A855F7` |

**Consistent furniture on every slide:**
- Small heart glyph in Electric Magenta at the top left corner
- Slide counter (`03 / 07`) at the bottom right
- "FOUNDING CREATORS" in 24px letterspaced Neon Orchid along the bottom left
- A swipe arrow on slides 1–6, never on 7

---

## 4. Master Claude Design prompt

Paste this once, then swap the copy block per day.

```
Build a 7-slide Instagram carousel at 1080x1350 (4:5) for an anime-themed youth
creative program called Founding Creators: AI Anime Accelerator.

COPY:
[paste the day's slide copy here]

BRAND:
- Background: vertical gradient #12082E to #4C1D95 to #7C3AED, with a faint
  neon city skyline silhouette at 8% opacity along the bottom edge
- Headline text: #FEF9EE, Atkinson Hyperlegible Bold
- Body text: #E9D5FF, Atkinson Hyperlegible Regular
- Emphasis word in headlines: #D946EF
- Accents and dividers: #A855F7
- Gold #FBBF24 ONLY on the final slide, and only when founding tuition is shown
- A small magenta heart glyph top-left of every slide, a slide counter
  bottom-right, and "FOUNDING CREATORS" letterspaced bottom-left

LAYOUT RULES:
- One idea per slide, no exceptions
- Hook slide must read at a glance from arm's length
- 90px safe margin on all edges
- Generous whitespace, identical type scale across all slides
- Slide 1 and slide 7 leave a clear vertical third open on one side for the
  character image to be composited in later
- Slides 2 through 6 are text-led with a clear bottom-corner space for a small
  character cut-out

Don't deliver until it scores 90/100 on hook readability, visual hierarchy,
brand consistency, and scroll-stopping power. Score it, then rewrite until it
clears 90.
```

---

## 5. Compositing Aoi in

Generate Aoi separately using the locked prompt in the character bible, then
place her onto the finished slide. Doing it that way means the text layout never
fights the character render, and one approved render can serve many slides.

1. Generate the pose you need on a plain or simple background.
2. Run the QC checklist from the character bible. Seven for seven.
3. Cut her out, keep a soft violet glow on the edge so she sits in the gradient.
4. Place her in the third the layout left open.
5. Never crop her hair silhouette — the coil halo is her recognition cue.

---

## 6. Accessibility

This is an education brand and the standard should be visible.

- Body text never below 38px on a 1350px-tall canvas.
- Keep contrast at 4.5:1 minimum. Glow Lilac on Midnight Indigo passes. Neon
  Orchid on Royal Violet does not — use it for accents, never body copy.
- Write real alt text on every Instagram slide. The alt text is also where the
  educational line gets to do a second shift.
- Burn captions into every TikTok and Reel. Most of the audience watches muted.

---

## 7. Reusable asset checklist

Build these once and the 15 days assemble fast:

- [ ] Background gradient template, all three sizes
- [ ] Neon skyline silhouette PNG, transparent
- [ ] Heart glyph, magenta and gold versions
- [ ] "FOUNDING CREATORS" footer lockup
- [ ] Slide counter component, 01/07 through 07/07
- [ ] Swipe arrow
- [ ] Cohort 01 badge in Founder Gold
- [ ] 6 approved Aoi renders: hero pose, teaching gesture, arms folded, pointing
      outward, three-quarter turn, seated at a workstation
