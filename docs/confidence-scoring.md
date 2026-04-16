# Confidence scoring

The 0.0–1.0 rubric for every key finding in a DRP brief. Required by the mega-prompt Step F.

---

## The rubric

| Score range | Meaning | Typical composition |
|---|---|---|
| **0.90–1.00** | Safe to act on without further verification | ≥ 3 engines confirm · ≥ 1 tier-1 source · no contradiction · numeric claim with stated uncertainty |
| **0.70–0.89** | Safe to cite, worth spot-checking | ≥ 2 engines confirm · ≥ 1 tier-1/2 source · at most a tier-5/6 contradiction |
| **0.50–0.69** | **Must include "why low" line.** Suitable as a hypothesis, not as a decision-grade claim | 1 engine · OR tier-3/4 only · OR forecast/estimate · OR conflicting tier-same sources |
| **0.30–0.49** | Single source, low tier, or strong contradiction. Treat as open question | 1 tier-5+ source only · OR tier-1 contradicts · OR extrapolation from stale data |
| **< 0.30** | Should not appear in a brief unless explicitly flagged as "rumor / unverified signal" | Community signal only · or internally inconsistent · or speculative |

---

## The "why low" requirement

Any finding below 0.7 must include an explicit sentence explaining the downgrade. Acceptable reasons:

- **Single source.** "Only [source X] supports this; no corroboration across engines."
- **Conflicting sources.** "Tier-2 [source Y] disagrees; reconciliation requires primary-source check."
- **Forecast / estimate.** "Projection based on [analyst method]; no realized data yet."
- **Stale data.** "Source is from 2022; domain moves fast, may not hold."
- **Extrapolation.** "Claim derived by extrapolating [metric] across [axis]; assumption untested."
- **New domain.** "Topic emerged < 3 months ago; source pool is thin."

Unacceptable "reasons":

- *"Hard to verify"* — vague. State what specifically prevents verification.
- *"Experts disagree"* — name the experts or the tier of disagreement.
- *"Industry consensus"* — consensus alone is not a reason to downgrade; state what's missing for upgrade.

---

## Scoring procedure (for the engine)

When producing a finding, walk this checklist:

1. **Count confirming engines.** 1 → cap confidence at 0.69. 2 → cap at 0.85. 3+ → no consensus cap.
2. **Identify top-tier source.** Tier 1 → +0.10. Tier 2 → +0.05. Tier 4–5 → 0. Tier 6–7 → −0.10.
3. **Check contradictions.** Tier-1 contradiction → −0.20. Tier-2/3 contradiction → −0.10. Tier 4+ contradiction → −0.05.
4. **Check uncertainty disclosure.** Numeric claim with stated range → +0.05. Point estimate without range → 0.
5. **Check freshness.** ≤ 6 months → +0.05. 6–18 months → 0. 18+ months in fast-moving domain → −0.10.
6. **Clamp to [0.0, 1.0].**

This is a heuristic, not a formula. Use judgment — the numbers exist to force explicit reasoning, not to replace it.

---

## Worked examples

### Example 1 — High-confidence finding

> **Claim:** "CVE-2026-XXXXX is a critical vulnerability in Product P default config (CVSS 9.1)."
>
> - 4 of 5 engines confirmed, all citing the same NVD entry (tier 1).
> - Vendor advisory (tier 4) confirms.
> - No contradictions.
> - Published 2026-03-12.
>
> **Score: 0.96.** Rationale: 4/5 consensus · tier-1 primary source · first-party confirmation · recent.

### Example 2 — Medium-confidence finding

> **Claim:** "Adoption of technique T grew 3× in 2025."
>
> - 3 of 5 engines agreed on the "3×" figure.
> - Source: one analyst report (tier 5) with proprietary methodology.
> - 1 engine cited a competing analyst (tier 5) giving 2×.
>
> **Score: 0.72.** Rationale: 3/5 consensus but all traced to analyst-tier sources. Methodologies are proprietary. Competing analyst gives 2×.

### Example 3 — Low-confidence finding requiring "why low"

> **Claim:** "Competitor X plans to ship feature F in Q3 2026."
>
> - 1 engine found this, citing a Reddit thread (tier 7).
> - No official announcement (tier 4).
> - No other engine confirmed.
>
> **Score: 0.42. Why low: single-engine · tier-7 source only · no first-party confirmation · forward-looking claim about an unannounced product.**

---

## Aggregation into the `_meta` block

At the end of a brief, aggregate:

```yaml
_meta:
  findings_count: 34
  findings_below_0_7_confidence: 7
```

The `findings_below_0_7_confidence` count is itself a portfolio signal:

- **0–5%** of findings below 0.7 → the brief's topic is well-established and well-sourced.
- **5–25%** → normal for a moderately new domain.
- **> 25%** → the topic is genuinely uncertain; this is a signal to the reader, not a failure of the brief.

---

## Common anti-patterns

- **Confidence theatre.** Assigning 0.9 to everything to look authoritative. If 0.9 is your median, your rubric is broken.
- **False precision.** Using 0.87 when 0.85 and 0.90 carry the same operational meaning. Round to nearest 0.05.
- **Confidence without justification.** Especially below 0.7 — the "why low" line is non-negotiable.
- **Upgrading on consensus alone.** Five tier-6 sources don't equal one tier-1.

---

## Integration with downstream use cases

- **Agent building** — preserve confidence scores in the agent's knowledge base. Train the agent to cite confidence scores in answers.
- **Market reports** — use the confidence ledger as a "how sure are we" exec-summary table.
- **Strategic briefs** — highlight findings below 0.7 as "questions a dissenter would ask".
- **Compliance audits** — below-0.7 findings must be footnoted with the specific verification pending.
