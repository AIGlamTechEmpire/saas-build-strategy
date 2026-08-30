# Test Prompts (Phase 6)

Use this guide in Phase 6 of the workflow to generate a personalized test prompt for the user to run inside their newly-loaded Claude Project.

## Why we test

The Brain is technically done at Phase 5, but the user has no idea if it actually works until they try it. Phase 6 closes the loop. A 5-minute test surfaces any voice mismatch, missing context, or weak ICP detail before the user walks away thinking the Brain is fine when it's not.

## The principle behind a good test prompt

A good test prompt:

1. **Produces a real piece of work the user could actually use** — not a hypothetical scenario, not a meta-question about their business.
2. **Exercises all six Brain docs** — it should force the AI to pull from Identity, ICP, Offers, Voice, Proof, AND Operating Principles.
3. **Is specific to THIS business** — not "write a sales email" but "write a sales email to [their actual list] inviting them to [their actual current offer] using [their actual proof points]."
4. **Has a clear pass/fail signal** — when the user reads the output, they should be able to instantly tell whether it sounds like them.

## How to generate the test prompt

After Phase 4 drafting is complete, look at what you learned about the business and ask:

**"What is the single piece of work this user creates most often that AI could help with?"**

Common answers by business type:

| Business type | Most common AI-able work |
|---------------|--------------------------|
| Services (coaching, consulting, agencies) | Sales follow-up email after a discovery call |
| Online courses / programs | Marketing email to the list about the next cohort |
| Product / e-commerce | Product description or launch announcement |
| Local services | Reply to a new lead inquiry |
| SaaS | Support reply or feature announcement |
| Content businesses | Social post or newsletter intro |
| Coaching / personal brand | LinkedIn or Twitter/X post in their voice |

Pick the one that matches the user's situation. If you're not sure, default to a sales email — it exercises all six Brain docs reliably.

## The test prompt template

Structure the test prompt with these four elements:

1. **The task** — concrete, specific, with a real verb (write, draft, respond, announce)
2. **The audience** — pulled from their ICP doc
3. **The offer or topic** — pulled from their Offer Stack
4. **One constraint** — something that forces voice precision (length limit, format requirement, banned phrase)

## Example test prompts by business type

### Services business example
For a digital marketing agency serving SMB e-commerce brands:

> *"Draft a follow-up email to a discovery call I just had with the founder of a 7-figure DTC skincare brand. She liked our pitch but said she needs to talk to her business partner. Move the deal forward without being pushy. 150 words max. Sign off as [founder name]."*

This prompt exercises:
- **Company DNA** (positioning of the agency)
- **ICP Profile** (the founder of a 7-figure DTC brand, her psychology)
- **Offer Stack** (whichever service was pitched)
- **Brand Voice** (sign-off, tone)
- **Proof Library** (if AI pulls a relevant case study)
- **Operating Principles** (the "move deal forward without being pushy" approach)

### Course / program business example
For a B2B training program:

> *"Write a marketing email to my list inviting them to the next cohort of [program name]. Use a contrarian opening, name one specific student win as proof, end with a single clear CTA. 200 words. No em-dashes."*

### Product business example
For an outdoor gear e-commerce brand:

> *"Write the product description for our new [product type]. Hook line, three benefit-driven bullets, one specific customer quote as proof, CTA. Match our usual voice — direct, no fluff, no 'transform your adventure' language."*

### Local service business example
For a med spa or wellness practice:

> *"Reply to a new lead inquiry asking about pricing for our [signature service]. Be specific about price, what's included, and the next step. Warm tone. No corporate language. 100 words."*

### SaaS example
For a B2B software company:

> *"Draft a feature announcement email for our new [feature]. Lead with the customer problem it solves (from our ICP doc), describe the feature in plain English, end with how to enable it. 175 words."*

## Evaluation criteria

When the user pastes the output back, evaluate against these criteria:

### Voice check (from `04_Brand_Voice.md`)

- Does it match the 3-4 voice adjectives?
- Does it avoid the banned words list?
- Does it avoid the AI tells (em-dashes, "it's not X it's Y," etc.)?
- Could it sit next to one of the greatest hits samples and feel like the same writer?

### ICP fit check (from `02_ICP_Profile.md`)

- Does it address the actual ICP, not a generic audience?
- Does it use their vocabulary?
- Does it acknowledge their psychology (where they've been burned, what they currently believe)?

### Specificity check

- Does it use real offer names, prices, and details from the Offer Stack?
- Does it pull a specific testimonial or case study from the Proof Library if relevant?
- Does it sound like THIS business, or could it have been written for any business in this category?

## Reporting back to the user

After the user pastes their test output, respond in this structure:

1. **Verdict in one line** — "Brain is live" / "Brain is mostly there with one gap" / "Brain needs tightening in one area"
2. **What's working** — name 2-3 specific things the output got right and trace them back to the Brain doc that made it possible
3. **What's missing (if anything)** — name the specific weakness and trace it to the Brain doc that needs more detail
4. **Offer to revise** — if there's a gap, offer to update the relevant Brain doc immediately and re-test

If the Brain is strong, this whole reply should be short — 4-6 sentences. Don't over-explain. The user should feel confident, not overwhelmed.

If the Brain has gaps, be specific about WHERE in WHICH doc the gap is, so the user understands the system and can refine it themselves later.

## What to do if the user skips Phase 6

Some users will say "I'll test it later." That's fine. Don't push. But tell them:

> *"Run the test prompt this week in your Project. If the output sounds off, the fastest fix is usually in your Brand Voice doc or your ICP doc. Come back if you want a second pass."*

This plants the seed that the Brain is a living thing, not a one-time output.
