# Two Agent Teams, Not One

**The confusion this resolves:** the four agents already built and the business Casandra
actually sells are **two different systems**. They have been treated as one, which is why
the pieces kept not quite fitting.

---

## Team A — THE MARKETING TEAM (already built)

**Runs on:** Casandra's own business
**Job:** turn her business into content, an offer, and a funnel
**Who it serves:** her

| Seat | Agent | Produces |
|---|---|---|
| SIGNAL | Kimi | Is the demand real, and who is the buyer |
| OFFER | Zahkeily | Positioning, priced offer, value ladder |
| ANGLE | TingTing | Title, hook, retention map |
| CONVERSION | Hezekiah | Lead magnet, CTA, email sequence |

**Status:** built, run, audited twice. It produced `outputs/final-video-brief.md`.

**This team markets the business. It is not the business.**

---

## Team B — THE DELIVERY TEAM (not yet built — this is the product)

**Runs on:** a *client's* business
**Job:** find where the client is bleeding, what they need, and what to do in 30 days
**Who it serves:** paying clients

This is the Pinky Business Brain Revenue System. **This is what "AI Agents R With Us"
actually sells.**

### The sequence

| # | Seat | Job | Input | Output |
|---|---|---|---|---|
| 0 | **CONVERSATION** | Human intake. Not an agent. The brand promise is that a person talks to you first. | — | Notes, goals, daily reality |
| 1 | **BRAIN** | Turn the conversation into structured business knowledge | Conversation + website + materials | The 8 Brain docs |
| 2 | **BLEED** | Find and rank where time and money leak | Brain + Opportunity Map | Ranked bleed list, in **dollars** |
| 3 | **FEED** | Is revenue arriving consistently, and from where | Brain + actual numbers | Feed audit, named channels |
| 4 | **NEED** | Work backward from the 12-month goal to the next 30 days | Goal, actual, bleed, feed | The 30-day revenue plan |
| 5 | **SOP** | Write procedures for the top bleeds so the work stops depending on the owner | Top 3 bleeds | Written SOPs |
| 6 | **AUTOMATE** | Take the worst task off the table — often no AI required | SOPs + 4 Stages | Automation spec |
| 7 | **WORKFORCE** | Only now: the AI employee / command center | Everything above | Agent team spec |

### The gate rule

Same discipline as Team A: **a seat cannot run until the seat before it has produced its
file.** No BLEED without a BRAIN. No 30-day plan without a bleed number. No AI without SOPs.

That gating *is* the "AI is the last phase" promise, made structural instead of stated.

---

## What already exists for Team B

Two assets are already in hand, and they are the engine.

### `assets/brain-builder/` — Seat 1, done

Helena Liu Leo's Brain Builder skill. Produces eight documents: Company DNA, ICP Profile,
Offer Stack, Brand Voice, Proof Library, Operating Principles, Archive Setup, and How To
Load Your Brain. Extraction-first — it mines the website before it asks questions.

**This is the BRAIN seat. It does not need rebuilding.**

### `assets/worksheets/AI_Opportunity_Map_Worksheet_v2.xlsx` — Seat 2, most of the way there

This worksheet is already a bleed calculator:

- Task · Department · Frequency · Hours per occurrence
- **Auto-computes total hours per month** (Daily ×22, Weekly ×4.33, Monthly ×1)
- Cost of doing it wrong: Low / Medium / High
- **Auto-computes Priority**: HIGH when ≥8 hrs/month AND risk is not High

It also carries **the 4 Stages of Work Ownership**, which is a gated sequence of exactly the
same shape as the Build Order:

```
DOING  →  DEFINING  →  DESIGNING  →  DELEGATING
(you do it) (you document it) (you spec it for AI) (AI owns it)
```

Each stage is a prerequisite for the next. You cannot delegate what you never defined.

---

## The gap — and it is the most valuable fix available

**The worksheet counts hours. The business is about money. Nothing currently bridges them.**

A client looking at *"13 hours a month"* shrugs. A client looking at *"$5,070 a month"*
signs. Same task, same worksheet, one missing calculation:

```
target hourly value  =  monthly revenue goal  ÷  hours worked per month
bleed in dollars     =  total hrs/month  ×  target hourly value
```

### Worked on Casandra's own numbers

| | Figure |
|---|---|
| 12-month goal | $750,000 |
| Monthly target | $62,500 |
| Hours worked per month (assume) | ~160 |
| **Target hourly value** | **≈ $390/hr** |
| Actual collected, last 3 months | $6,500 |
| Actual monthly | ≈ $2,167 |
| **Actual hourly value** | **≈ $13.50/hr** |

**The gap is not 29× in revenue. It is 29× in what an hour is worth.**

That reframe is the entire pitch, and it is computable for any client from two numbers they
already know: their goal, and their hours. **Add this column to the worksheet and the
diagnostic goes from interesting to unignorable.**

---

## What this means for the video

The video currently demos **Team A** — the marketing team. That is fine and it works.

But the more honest and more differentiated video demos **Team B**, because Team B is the
thing being sold. "Watch me diagnose a real business in 14 minutes and tell them exactly
what to do in the next 30 days" is a stronger promise than "watch me generate an offer."

**Recommendation:** build Team B, run it on Casandra's own business as the POC, and then
decide which team films. Do not decide the video before seeing Team B's output.

---

## Open questions before Team B is built

1. **"The 4 areas we created" — what are they?** This was referenced but never named. Team B
   cannot be built until these four areas are defined, because the 30-day plan outputs
   against them.
2. **Where does the worksheet live at runtime?** Airtable, or a generated `.xlsx` per client?
3. **Does the client see the Brain, or only the output?**
4. **Is the hourly-value bridge computed from real hours worked, or from a standard 160?**
