# PRD — PINKY BUSINESS BRAIN Revenue System

**Product:** A four-seat Claude Code subagent architecture that converts one business idea into a complete revenue system — positioning, a priced offer, YouTube angles, a lead magnet, and a follow-up sequence.

**Owner:** PinkyF
**Status:** v1 built and run. Second-pass audit in progress.
**Repository:** `AIGlamTechEmpire/saas-build-strategy`, branch `claude/pinky-business-brain-agents-qdq6ia`

---

## 1. Why this exists

### The problem

Entrepreneurs in this market are not short on AI capability. They are short on **sequence**. They have consumed two to three years of AI content and have nothing billable to show for it, because every build attempt is pointed at a business that was never defined.

AI applied to an undefined business returns undefined output. The operator reads that as *"AI didn't work,"* and buys another tool.

### The thesis

> The money is not in the tools. The money is in the system — and specifically in the **order** the system is built in.

Most people start at content. Content is step three. With no defined buyer and no priced offer underneath it, content converts nothing. Fixing the order fixes the output.

### Why a multi-agent architecture and not one prompt

This is the load-bearing product decision. A single prompt produces a single voice with no capacity for disagreement. Four role-separated agents with a scoring rubric between them produce something structurally different: **one agent can reject another agent's work and force a revision.**

That rejection is not a feature. It is the quality mechanism, the on-camera proof, and the reason this cannot be replicated by pasting a long prompt into a chat window.

---

## 2. Who it is for

### Primary user (operates the system)
PinkyF — creator producing YouTube content that must lead to revenue, not just views.

### Primary audience (receives the output)
Coaches, consultants, creators, service providers, and entrepreneurs doing roughly $2k–$30k/month who already use AI daily and still have no defined ICP, no priced offer, and no repeatable lead motion.

**Sophistication:** intermediate on tools, complete beginner on systems architecture, **trending skeptical**. The skepticism is earned — they have been sold to repeatedly. Every claim must be falsifiable on screen.

### Explicitly not for
Total beginners who have never used an AI tool. Developers looking for a coding agent framework. Anyone wanting a tool comparison or a prompt-engineering lesson.

---

## 3. What gets built

### System architecture

```
                    ┌──────────────────────┐
                    │  business-brief.md   │  ← single source of truth
                    └──────────┬───────────┘
                               │  every seat reads this first
        ┌──────────────────────┼──────────────────────┐
        ▼          ▼           ▼          ▼
   ┌────────┐ ┌────────┐ ┌────────┐ ┌────────────┐
   │ SIGNAL │→│ OFFER  │→│ ANGLE  │→│ CONVERSION │
   └────────┘ └────────┘ └────────┘ └────────────┘
     Kimi     Zahkeily   TingTing    Hezekiah
        └── scored ─┴── scored ─┴──── scored ──┘
            Challenge Pass: one rejection permitted per handoff
                               │
                               ▼
                    ┌──────────────────────┐
                    │  COORDINATOR         │  ← main Claude Code session
                    │  combines + improves │
                    └──────────┬───────────┘
                               ▼
                    outputs/revenue-agent-demo.md
                    outputs/final-video-brief.md
```

### Component inventory

| Path | Type | Purpose |
|---|---|---|
| `business-brief.md` | Input | The defined business asset. Seven fields. Every agent reads it first. Changing this file changes every downstream output. |
| `.claude/agents/market-signal-researcher.md` | Agent (Kimi) | Demand analysis, audience psychology, 7-point opportunity scorecard. **Write-disabled by design.** |
| `.claude/agents/offer-architect.md` | Agent (Zahkeily) | Positioning, priced offer, unique mechanism, value ladder, objection map. |
| `.claude/agents/content-angle-strategist.md` | Agent (TingTing) | Titles, thumbnail text, hook script, sub-15-min retention map, screen-recording beats. |
| `.claude/agents/conversion-system-builder.md` | Agent (Hezekiah) | Lead magnet, in-video CTA, 5-email sequence, sales path, friction check. |
| `runbooks/revenue-agent-runbook.md` | Process | Coordinator rules and run order. |
| `outputs/` | Output | Generated deliverables. |
| `PRD.md` | Spec | This document. |

### Why the researcher cannot write files

`market-signal-researcher` carries `disallowedTools: Write, Edit`. This is deliberate and structural, not a safety afterthought. A research seat that can edit downstream artifacts will quietly reconcile its own findings with the strategy instead of challenging it. **Read-only enforces honest disagreement.** It is the same reason auditors do not keep the books.

---

## 4. How it works

### The Revenue Build Order

Four seats, fixed sequence, no skipping.

| # | Seat | Input | Output | Gate |
|---|---|---|---|---|
| 1 | SIGNAL | `business-brief.md` | Scored opportunity, audience psychology, named risks | Must produce a buyer specific enough to price against |
| 2 | OFFER | Brief + signal | Positioning, priced offer, mechanism, ladder, objections | Must produce a **price** |
| 3 | ANGLE | Brief + signal + offer | Title, hook, retention map, screen beats | Must fit under 15 minutes |
| 4 | CONVERSION | All of the above | Lead magnet, CTA, emails, sales path | Must tie every asset to the offer |

**Hard rule:** do not run Seat 3 until Seat 2 has produced a price. Content built on an unpriced offer is the exact failure mode this system exists to prevent.

### The Challenge Pass

Before output moves downstream, the receiving seat scores it against a rubric (five criteria, 1–5 each) and may reject it **once**, with a written reason.

Observed in the v1 run: the Offer seat rejected the Signal seat's first ICP as *category-level rather than ICP-level*, forcing a revision from "small business owners" to "owner-operators who factor invoices, file IFTA quarterly, run a fuel card, and are behind on categorizing settlement statements."

That delta — vague to priceable — is the product.

### The Override

At least one point per run, the human operator overrules an agent and states the reasoning out loud. In the v1 run the Offer seat recommended $600/month; PinkyF set $450 because the operator is one person in month one with no case studies.

**This is a required step, not an optional one.** A system that appears fully autonomous reads as staged to a skeptical audience. Visible human judgment is what converts the skeptic.

---

## 5. Success criteria

### The system works if

| # | Criterion | How to verify |
|---|---|---|
| 1 | One brief in, five assets out | ICP, priced offer, content angles, lead magnet, follow-up sequence — all present and all consistent with each other |
| 2 | At least one Challenge Pass rejection fires per run | The rejection and revision are both visible in the output |
| 3 | The offer carries a defensible price | Priced against a real deadline, cost, or constraint the buyer already has — not a round number |
| 4 | Output contains at least one detail a single prompt would not reach | v1 benchmark: pricing against the IFTA quarterly filing deadline |
| 5 | Every section connects to attention, leads, revenue, or leverage | No section survives that only describes capability |
| 6 | A full run completes fast enough to film | Under an hour of wall clock, editable to 14 minutes |
| 7 | The output is publishable without a rewrite | Coordinator improves weak agent output rather than pasting it through |

### The system has failed if

- Any single agent produced most of the output. Role separation collapsed.
- Every agent agreed with every other agent. The Challenge Pass never fired.
- The offer is priced at a round number with no defense.
- The final document could have come from one good ChatGPT prompt.
- The video concept ends at "look what it built" with no revenue path attached.

### Business outcomes (targets pending confirmation)

| Metric | Target | Note |
|---|---|---|
| Video → System download rate | To be baselined | CTA is the artifact, not a form — expect above-category |
| System → first-win completion | The critical metric | A downloaded folder that never opens converts nothing |
| Email 1 reply rate | Highest-intent signal in the funnel | Manual replies until volume forces a form |
| System → Install Day | Load-bearing rung | If Install Day doesn't run, the ladder has a hole |
| Install Day → Sprint | Structural trigger | Install Day ends with a price and nothing built; that gap is the offer |

---

## 6. Constraints

**From the brief, non-negotiable:**

- Not a generic AI tools tutorial.
- Not a prompt engineering lesson.
- Must show the connection between AI workflow and revenue.
- Must state that the money is in systems, not tools.
- Beginner-friendly without being basic.

**Added during the v1 build:**

- **No cold-open terminal.** Non-developers leave inside 60 seconds. The tool is the reveal at ~2:10, never frame one.
- **No hypothetical demo business.** One real or disclosed-composite business, carried end to end.
- **No autonomy overclaim.** The Override beat is mandatory.
- **Research is brief-only in v1.** No web access. Every market claim labeled `[EVIDENCE]` or `[INFERENCE]`.
- **No fabricated evidence.** No invented statistics, view counts, or competitor titles presented as verified.

---

## 7. Risks

| Risk | Severity | Mitigation |
|---|---|---|
| **Claude Code install is the biggest funnel leak.** Audience is intermediate on browser AI, not terminals. | Critical | 3-line install block + 60-second video in `START-HERE.md`. Ship a `fallback/` paste-prompt path for people who can't install. |
| The "AI agent team" trope is saturated in its shallow form | High | Differentiate on deliverable quality and the Challenge Pass, not on orchestration |
| Generic LLM output destroys credibility instantly | High | Require one detail per run that a single prompt structurally cannot reach |
| Challenge Pass never fires on a thin brief | High | Agents must also reject on *insufficient input*, naming the missing fields |
| Prices published before confirmation | High | Every figure labeled unconfirmed until sign-off; strip hedges once final |
| Fabricated urgency (early-bird with no workshop date) | High | Set the date before publishing, or cut the deadline entirely |
| Video overruns 15 minutes | Medium | Second-pass audit times the retention map block by block |
| Agent files fail to load after manual creation | Medium | Restart Claude Code; verify with `/agents` |
| System teaches enough that some never buy | Accepted | Crippling the System would contradict the video, and the video is the asset |

---

## 8. Build log

| Version | Date | What happened |
|---|---|---|
| v0 | 2026-08-30 | Repo scaffolded: brief, four agents, runbook, outputs dir |
| v1 | 2026-08-30 | Full four-seat run against `business-brief.md` → `outputs/revenue-agent-demo.md`. Opportunity scored 30/35. Mechanism named (Revenue Build Order + Challenge Pass). Demo business selected (Ledger & Lane). Value ladder drafted. |
| v1.1 | 2026-08-30 | Strategic second pass: Offer and Conversion seats re-score the v1 output on seven criteria and rewrite anything below 4 → `outputs/final-video-brief.md` |

---

## 9. Out of scope for v1

- Web research (no live search; brief-only, inference labeled)
- Building the actual Pinky Brain Revenue System folder as a shippable download
- Landing pages, checkout, or email platform integration
- Recording, editing, or publishing the video
- Any agent that ships, sends, or publishes on the creator's behalf
- Automated ICP validation against real market data

---

## 10. Open decisions

Owned by PinkyF. Not decided by the agent team.

1. **Confirm every price.** $47 / $97 / $1,497 / 2×$799 / $7,497 / $297-mo are all recommendations. Once final, strip the hedging language from the emails — hedged pricing inside a close reads as uncertainty.
2. **Sprint: checkout or application?** $1,497 direct checkout works from cold YouTube. Above that, a human has to talk to them, which means ~$2,997 with an application. **Pick one; do not straddle.**
3. **Real business or disclosed composite?** A real named business beats Ledger & Lane. Without one, use the composite and disclose it on camera.
4. **Is Install Day on the calendar?** If not, the early-bird deadline is fabricated and must be cut.
5. **Reply-volume cutoff.** At what download count does the manual Email 1 reply become a form?
6. **Do the persona names ship in the System?** Kimi / Zahkeily / TingTing / Hezekiah are strong on camera, mildly confusing in a folder opened three days later. Recommendation: keep them, and map each to its seat at the top of the runbook.
