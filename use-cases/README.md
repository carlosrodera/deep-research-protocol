# Use cases

DRP is a **research method**. Its output — a source-verified, consolidated brief — is the input to many downstream deliverables. Each use case here is a pipeline that takes a DRP brief and transforms it into a specific artifact.

---

## Canonical use cases

| Use case | What you ship | Status |
|---|---|---|
| [`agent-building/`](./agent-building/) | A specialized AI agent (Custom GPT / Claude Project / Claude Skill / Gemini Gem) with a verified knowledge base and an 11-block master prompt | ✅ Production-ready (v1.0) |
| [`market-report/`](./market-report/) | A decision-grade market / competitive intelligence brief | 🟡 Template + pipeline |
| [`strategic-brief/`](./strategic-brief/) | A board-ready strategic narrative with counter-arguments weighed | 🟡 Template + pipeline |
| [`compliance-audit/`](./compliance-audit/) | A jurisdiction-aware compliance map with primary-source citations | 🟡 Template + pipeline |

---

## How to pick one

| If your deliverable is… | Use |
|---|---|
| A system others will interact with conversationally, grounded on verified facts | **agent-building** |
| A narrative for humans to read and act on, describing a market or ecosystem | **market-report** |
| A persuasive document for decision-makers with stakes and trade-offs | **strategic-brief** |
| A compliance / regulatory mapping exercise | **compliance-audit** |
| Something else | See [submit a new use case](../CONTRIBUTING.md) |

---

## Shared inputs

Every use case starts from a DRP brief:

```
workspace/research/consolidated.md
workspace/research/primary-sources/
```

If you don't have these yet, go to [`../docs/quickstart.md`](../docs/quickstart.md) first.

---

## Chain patterns

Use cases can chain:

- **agent-building** → **compliance-audit** — build an agent first, then use it to run compliance audits at scale.
- **market-report** → **strategic-brief** — a market report is often the evidentiary base for a strategic brief.
- **compliance-audit** → **agent-building** — audit findings become the KB of a compliance-specialist agent.

When you chain, maintain the confidence scores through the transformation. Lower confidence does not disappear in a derivative — it carries through and is surfaced in the final deliverable's own confidence ledger.

---

## Contribute a use case

See [`../templates/use-case-template.md`](../templates/use-case-template.md) and [`../CONTRIBUTING.md`](../CONTRIBUTING.md). Real, source-cited submissions only — fabricated examples are rejected.
