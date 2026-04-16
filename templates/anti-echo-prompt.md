# Anti-echo-chamber prompt (DRP variant)

> Use this variant when the **dominant narrative might be wrong** and consensus is not what you need — you need the strongest counter-case.
>
> Examples: strategic decisions where the market has converged on one story, security claims where vendor docs agree but independent researchers disagree, regulatory interpretations where practitioners have collectively drifted from the letter of the law.

---

## When to use this instead of the canonical consolidation

| Situation | Use |
|---|---|
| You want a verified consensus brief | [`consolidation-prompt.md`](./consolidation-prompt.md) |
| You want to stress-test the consensus | **This prompt** |
| You are entering a market where everyone copies each other | **This prompt** |
| You suspect a vendor/industry echo chamber | **This prompt** |

The two can be chained: run canonical consolidation first, then run anti-echo on top to surface what the consensus is missing.

---

## Prompt

```text
You are a contrarian research analyst with high reasoning effort.

I have [N] parallel Deep Research reports on the same question,
produced by different engines. Every naive consolidation would stress
the consensus. I want the OPPOSITE.

## Rules

1. SURFACE DISAGREEMENT FIRST. Every major finding must be probed for
   counter-evidence before being recorded as "true".
2. For every claim, actively search the reports for the STRONGEST
   contradicting source, even if it is a minority view.
3. Apply a REVERSED evidence hierarchy check: if the consensus is
   overwhelmingly from tier 5–7 (press, community), downgrade its
   confidence even if 4 engines agree. Many-engines-repeating-a-blog
   is still one-blog.
4. Flag any claim where ALL [N] engines cite THE SAME underlying
   source: this is a single point of failure, not consensus.
5. Build a "consensus vulnerability map": rank the top findings by how
   easy they would be to topple with one strong primary source
   disagreeing.

## Output structure (Markdown)

## 1. Executive summary of the contrarian read
≤ 400 words. State where the reports converge, where the convergence
is LOAD-BEARING, and where it is FRAGILE.

## 2. Load-bearing consensus
Findings that survive contrarian stress. Deserve high confidence.
Same table format as the canonical consolidation.

## 3. Fragile consensus
Findings where ≥ 3 engines agreed but ≥ 1 of the following is true:
- They all cite the same underlying source ("echo chamber").
- The supporting tier is 5–7 (press / community).
- A tier 1–3 source contradicts.
- The claim is a forecast or estimate, not a fact.

For each fragile-consensus finding: state why it is fragile + what
would need to be verified against primary source.

## 4. Minority-report findings worth amplifying
Claims surfaced by only 1 engine that a contrarian should investigate
because the consensus may be missing them. Classify as:
- [LIKELY BLIND SPOT — verify]
- [POSSIBLE NOISE — down-rank]

## 5. Single-source-of-failure citations
URLs that underpin multiple claims across multiple engines. If these
were wrong, what breaks? List impact.

## 6. What a steelman of the OPPOSITE position would say
A fair, source-cited argument that a thoughtful dissenter would make
against the overall consensus.

## 7. `_meta` block (YAML)

```yaml
_meta:
  protocol: deep-research-protocol
  version: 3.0
  stage: anti-echo
  run_date: [YYYY-MM-DD]
  engines_count: [N]
  load_bearing_findings: [N]
  fragile_consensus_findings: [N]
  minority_reports_flagged: [N]
  single_source_citations: [N]
  language: [en | es | other]
```

Preserve every URL. Do not truncate.

--- REPORT 1 ---
[paste]

--- REPORT 2 ---
[paste]

--- etc. ---
```

---

## After running

1. Chain into the canonical [`consolidation-prompt.md`](./consolidation-prompt.md) if you haven't already — the contrarian read is meant to CORRECT a consensus brief, not replace it.
2. Manually verify every "fragile consensus" and "single source of failure" entry.
3. For strategic briefs: attach the "steelman of the opposite" section to your deliverable. It signals rigor to senior stakeholders and kills the "yes-man AI" smell.

## Attribution

Part of the **Deep Research Protocol (DRP)** — `github.com/carlosrodera/deep-research-protocol`. MIT © 2026 Carlos Rodera.
