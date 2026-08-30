# Extraction Guide

Use this guide while scraping the user's website and uploaded materials in Phase 2. Your goal is to harvest as much Brain content as possible BEFORE asking the user anything.

## Special cases

**Multi-business user.** If Phase 1 confirmed the user runs multiple businesses, scope your scraping strictly to the ONE business the Brain is for. If you accidentally land on another of their properties while scraping (e.g., their personal site links to a different venture), do not extract from it. Stay in scope.

**Pre-launch business (no website).** Phase 2 is skipped entirely. Move directly to Phase 3 with the Pre-Launch question set in `interview-bank.md`.

**Thin website.** If the site has only a home page plus contact (no About, no sales page, no blog), still scrape what's there but flag in your confidence map that nearly every Brain doc will need heavy interview support.

## What to fetch and in what order

1. **Home page** — first impressions, value prop, positioning
2. **About page** — founder story, mission, values, team
3. **Sales pages / product pages** — offers, prices, promises, hero stories
4. **Testimonials / case studies / reviews page** — proof
5. **Blog posts, podcast episodes, or YouTube descriptions** — voice samples and POV
6. **Contact / FAQ page** — operating details, response norms

If the user provided URLs outside their main site (e.g., a podcast appearance, a Substack), fetch those too. Outside content is often where the user's TRUE voice shows up.

## What to extract for each Brain document

### For Company DNA (doc 01)

Look for:
- **Business name** — usually in the page title or header
- **Tagline / positioning statement** — main hero text on home page
- **Founder name(s)** — About page
- **Founding story** — About page, sometimes a "Story" or "Our Why" section
- **Mission statement** — often labeled, sometimes in the About page
- **Values** — sometimes listed explicitly with names, sometimes implied through copy
- **What they do (one sentence)** — usually in the home page hero
- **Who they serve (one sentence)** — sometimes in the hero, sometimes on About
- **Differentiation** — look for phrases like "unlike most," "we believe," "the difference is"

Extract direct quotes wherever possible. Direct quotes preserve voice.

### For ICP Profile (doc 02)

Look for:
- **Target audience descriptions** — usually on sales pages (e.g., "for B2B founders running $1M-$10M companies")
- **Pain language** — look for "are you tired of," "if you've ever," "do you struggle with"
- **Desire language** — look for "imagine if," "what if you could," "the dream is"
- **Industry-specific terms** — note vocabulary the user uses for their ICP
- **What the ICP currently believes** — sometimes addressed directly in sales copy
- **Hero customer demographics** — pulled from case studies and testimonials

ICP psychology (deep pain, fears, beliefs) is usually NOT on the website. Plan to ask in Phase 3.

### For Offer Stack (doc 03)

Look for:
- **Every distinct offer** with its name, price, structure, and what's included
- **The promise** — what transformation the offer delivers
- **The audience** — who each offer is for (often different ICPs per offer)
- **Hero customer stories** — pull from testimonial pages and case study pages
- **Common objections addressed** — FAQs and "Is this for you?" sections

If pricing isn't on the website (high-ticket services), mark as `[TO REFINE: pricing structure]` and ask in Phase 3.

### For Brand Voice (doc 04)

This is the MOST important harvest. Pull 5 to 10 distinct writing samples from across the user's content. Look for:
- **Blog post intros** — the opening line of every recent post
- **About page copy** — usually their most polished voice
- **Email signatures or "letter from the founder"** content
- **Social media captions** if visible
- **Sales page openers** — high-energy voice samples

For each sample, note:
- Sentence length (short choppy vs. flowing prose)
- Vocabulary (formal vs. casual, technical vs. plain)
- Rhythm (declarative vs. interrogative, etc.)
- Signature phrases or repeated motifs

Identify what voice tells you about their personality. This becomes the "3 adjectives" section of the Brand Voice doc.

### For Proof Library (doc 05)

Look for:
- **Testimonials** — pull every quote you can find, with attribution
- **Case studies** — full problem/solution/result narratives
- **Numerical proof** — "200+ customers," "$30M generated," etc.
- **Press mentions** — "as featured in" sections
- **Reviews / ratings** — if displayed
- **Awards or recognitions**

For each testimonial, capture:
- The exact quote
- The person's name and role/title
- The transformation they describe
- The objection it kills (e.g., "I was skeptical about cost" kills cost objections)

### For Operating Principles (doc 06)

This is the HARDEST doc to extract from public materials. Most operating principles are internal. Look for:
- **Process or approach pages** — "How we work" sections
- **FAQ entries about timing, deliverables, communication**
- **Hiring pages** — sometimes reveal values about how they treat people
- **Customer service language** — reveals service philosophy

Operating Principles will be ~80% interview-driven. Don't worry if you find very little on the website.

## How to handle uploaded files

### Transcripts (sales calls, podcasts, YouTube videos)

- Scan for the user's voice in unscripted moments. These show the REAL voice better than polished writing.
- Pull 5-10 voice samples from raw speech.
- Note repeated phrases, signature moves, vocabulary patterns.
- If the transcript is a sales call, mine the prospect's words for ICP language.

### Customer surveys

- Pull 5-10 verbatim customer responses for the Proof Library.
- Note recurring pain themes for the ICP doc.
- Look for desire language ("I wish I had...") for the ICP transformation.

### Recent emails (sales emails or newsletter)

- Voice samples.
- Hero stories the user already tells.
- The CTAs they use (these reveal their sales philosophy).

### Old marketing materials, brand decks, pitch decks

- Mission, values, positioning statements they've used before.
- Origin story if the founder included it.

## Synthesizing what you've found

After scraping, build a mental map:

| Brain doc | Confidence (1-5) | Gaps to ask |
|-----------|------------------|-------------|
| Company DNA | 4 | Origin story emotional layer |
| ICP Profile | 2 | Psychology, beliefs, where they've been burned |
| Offer Stack | 5 | Nothing |
| Brand Voice | 4 | Banned words, AI tells they hate |
| Proof Library | 3 | Hero customer story details |
| Operating Principles | 1 | Almost everything |

Use this map to drive Phase 3. Skip clusters where confidence is 4 or 5. Focus questions where confidence is 1, 2, or 3.

## What NOT to do

- **Don't dump everything you scraped into the Brain.** The Brain is curated, not exhaustive. Distill.
- **Don't paraphrase the user's voice into generic language.** Preserve their actual words, especially in the Brand Voice doc.
- **Don't invent content.** If you can't find or extract something and the user hasn't answered it, mark `[TO REFINE]`.
- **Don't include outdated content.** If the user has a 2019 blog post and a 2024 sales page that contradict each other, use the newer one.
