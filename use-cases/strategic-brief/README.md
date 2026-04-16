# Use case: Strategic brief

> **Board-ready strategic narrative with counter-arguments weighed. DRP + anti-echo pass.**

---

## When to pick this

- The decision is **consequential** and **contested** — board-level, capital allocation, organizational pivot, geopolitical move.
- Your audience will **challenge** the brief. "What's the counter-argument?" is a guaranteed question.
- A consensus read alone is insufficient. You need the steelman of the opposite.

---

## Inputs

- `workspace/research/consolidated.md` — from the canonical consolidation.
- `workspace/research/contrarian.md` — from the [`anti-echo prompt`](../../templates/anti-echo-prompt.md). **Required for this use case.**
- Stakeholder map — who signs off, who resists, who enables.

---

## Deliverable shape

```
## One-page summary          (decision framing, recommendation, top risks, confidence)
## Context                   (what changed, why now)
## The evidence              (sub-sections grounded in DRP consolidated findings)
## Load-bearing consensus    (findings that survive contrarian stress)
## Fragile consensus         (findings that look agreed-upon but aren't)
## Steelman of the opposite  (best counter-argument, fully sourced)
## Decision options          (2–4 options with evidence-mapped trade-offs)
## Recommendation            (with explicit contingencies)
## Risks & open questions    (things to re-verify in 30/60/90 days)
## Appendix: confidence ledger + primary sources
```

The **steelman of the opposite** section is what separates a strategic brief from a market report. If you cannot write one, you have not done enough contrarian stress.

---

## Pipeline

1. Run the full DRP for research (consolidation).
2. **Run anti-echo** (chain [`../../templates/anti-echo-prompt.md`](../../templates/anti-echo-prompt.md) on the same 5 reports).
3. Identify **load-bearing** vs **fragile** consensus from the anti-echo output.
4. Write the steelman using only sources from the contrarian pass.
5. Frame decision options so each maps onto a different subset of the evidence. Make the trade-offs explicit.
6. Verify citations.

---

## Specific quality gates

- Every decision option cites specific findings from the consolidated brief with their confidence scores.
- The recommendation is derived from the evidence and acknowledges what would change the recommendation.
- The steelman is long enough to be taken seriously (≥ 1 page, source-backed). A token paragraph signals cowardice.
- Open questions have a review cadence attached (30/60/90 days).

---

## Common failure modes

- **Consensus bias.** Writing the brief entirely from the canonical consolidation without chaining anti-echo. Decision will blind-spot on the consensus's failure modes.
- **Anchoring.** Framing options in a way that the recommendation is obvious. State the recommendation separately and let readers evaluate options on their own.
- **Missing contingencies.** "We should do X" without "we should revisit in 60 days if [signal]".

---

## Example

Contribute a real example via PR.
