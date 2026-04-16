# Use case: Market report

> **Ship a decision-grade market or competitive-intelligence brief from a DRP consolidated brief.**

---

## When to pick this

- You need to brief a product / exec / investment decision on a market, a technology, a vertical.
- Your audience is reading to **decide**, not to explore.
- The domain is moving fast enough that parametric-memory reports would be stale on arrival.

---

## Inputs

- `workspace/research/consolidated.md`
- `workspace/research/primary-sources/`
- Audience profile: size, role, decision window.

---

## Deliverable shape

```
## Executive summary          (≤ 300 words, 3 bullets + top-3 confidence-≥0.85 claims)
## Market definition          (scope, boundaries, what's explicitly out)
## Key players                (with quantified positions where available)
## Forces & dynamics          (tech, regulatory, capital, talent)
## Points of consensus        (high-confidence findings, cited)
## Points of disagreement     (where the sources diverge + what it means for the decision)
## Recommendation             (what the audience should do, given the evidence)
## Confidence ledger          (table: finding · confidence · source tier)
## Appendix: primary sources
```

The confidence ledger is **required**. This is the differentiator from a generic market report.

---

## Pipeline

1. **Filter the DRP brief.** Keep findings with confidence ≥ 0.7 by default. Lower-confidence findings go to an "open questions" section, not the main body.
2. **Group by force or player.** The DRP brief is organized by research question; the report is organized by market axis. This is a deliberate re-organization.
3. **Quantify or drop.** Every claim about market size, share, growth, adoption must carry uncertainty. Remove claims that cannot be sourced to a quantified tier-1/2/3 source.
4. **Write the recommendation last.** Derive from the evidence in the preceding sections, not from intuition.
5. **Verify citations.** `python scripts/verify-citations.py market-report.md` — no broken URLs reach the audience.

---

## Specific quality gates

Beyond the canonical DRP Step I gates:

- Every market-size / share / growth figure has a source, a date, a methodology note.
- Every competitor claim cites a first-party or independent-analyst source. No "Wikipedia says".
- Forward-looking claims (forecasts, TAM projections) carry confidence ≤ 0.7 by default unless backed by multiple independent analysts.
- "Consensus" on forward-looking claims requires explicit framing as consensus-of-analysts, not fact.

---

## Common failure modes

- **Confidence laundering.** Taking a confidence-0.6 finding from the DRP brief and restating it without the hedge in the report. Preserve hedges verbatim.
- **Analyst amplification.** 5 analyst reports saying 30% CAGR traced back to 1 primary study. Mark as single-source under its tier.
- **Competitor editorializing.** Characterizing a competitor's position based on marketing copy without naming the source. Always name the source.

---

## Example

Contribute a real, source-cited example via PR. Template: [`../../templates/use-case-template.md`](../../templates/use-case-template.md).
