# Use case: Agent building

> **Ship a specialized AI agent (Custom GPT, Claude Project, Claude Skill, or Gemini Gem) with a verified knowledge base, an 11-block master prompt, and a tested behavior loop.**

This is the original use case the Deep Research Protocol was designed for. It remains the flagship consumer of a DRP brief.

---

## When to pick this

- You want to ship a domain-specific AI that others will interact with.
- The domain has **enough depth** that a generic LLM answer is inadequate.
- You need **citations** and **traceability** in the agent's answers (enterprise, compliance, regulated domains).
- You are willing to invest 4–8 hours in the first build and an hour/month on maintenance.

If the domain is shallow or changes faster than your maintenance cadence, pick a different use case.

---

## Inputs

- `workspace/research/consolidated.md` — your DRP brief.
- `workspace/research/primary-sources/` — the downloaded tier-1/2 sources.
- A decision on target platform. Read [`../../skill/references/platforms.md`](../../skill/references/platforms.md) if unsure.

---

## Pipeline

```
DRP brief (consolidated.md)
          │
          ▼
┌────────────────────────┐
│ 1. Knowledge base      │  Markdown-first, named files, 00-index.md
│    design              │  primary-sources/ preserved with dates
└──────────┬─────────────┘
           ▼
┌────────────────────────┐
│ 2. Master prompt       │  11 blocks (role, objective, audience, KB
│    (11-block method)   │  protocol, output format, reasoning, guard-
│                        │  rails, escalation, self-check, examples,
│                        │  language policy)
└──────────┬─────────────┘
           ▼
┌────────────────────────┐
│ 3. Platform impl       │  Custom GPT / Claude Project / Skill / Gem
└──────────┬─────────────┘
           ▼
┌────────────────────────┐
│ 4. Test battery        │  ≥ 5 realistic queries; document results;
│    + iteration         │  iterate on prompt + KB
└──────────┬─────────────┘
           ▼
       Shipped agent
       + evaluation.md
       + monthly review
```

---

## Phases

Each phase has a dedicated playbook:

| Phase | Playbook | What you produce |
|---|---|---|
| 1. Knowledge base | [`01-knowledge-base.md`](./01-knowledge-base.md) | `workspace/knowledge-base/` with `00-index.md` + topic files + `primary-sources/` |
| 2. Master prompt | [`02-master-prompt.md`](./02-master-prompt.md) | `workspace/master-prompt.md` |
| 3. Implementation | [`03-implementation.md`](./03-implementation.md) | Deployed agent + `workspace/deployment.md` |
| 4. Testing | [`04-testing.md`](./04-testing.md) | `workspace/evaluation.md` with test results |

These playbooks are inherited from the original Deep Agent Protocol (pre-DRP repositioning) and have been production-tested.

---

## Confidence preservation

The agent's master prompt MUST preserve DRP's confidence scoring. Require the agent to:

1. Cite the named file from the KB with every answer.
2. Preserve the original confidence score where recorded.
3. Refuse to answer from parametric memory when the KB does not cover the question.
4. Escalate findings below 0.7 confidence by flagging them as "provisional, verify with primary source".

This is the difference between a specialist agent and a branded chatbot.

---

## Platform decision

Detailed guide: [`../../skill/references/platforms.md`](../../skill/references/platforms.md). Quick version:

| Need | Platform |
|---|---|
| Share via public link | Custom GPT |
| Large, precise KB (up to 1M tokens) | Claude Project |
| Reusable, version-controlled instruction | Claude Skill |
| Deep Google Workspace integration | Gemini Gem |
| Autonomous tool use | Claude Code + MCPs |

---

## Common failure modes

- **Shallow KB.** You dumped 3 PDFs without splitting or indexing. The agent hallucinates because it cannot find the right slice. Fix: topic-split + `00-index.md`.
- **KB consultation not forced.** Master prompt says "consult knowledge base when useful". The agent ignores. Fix: require named-file lookups unconditionally.
- **No test battery.** You shipped on vibes. Users find the edge cases for you. Fix: 5-query battery before publish, 10-query battery before team rollout.
- **No monthly review.** The agent worked in Q1; in Q3 its cited regulations are obsolete. Fix: calendar reminder + automated `verify-citations.py` re-run.

---

## Example

A full example will be contributed by the community as real agents ship (see [scaffold](../../examples/walked-example-scaffold.md)). We deliberately do **not** ship a fabricated example — see [`CONTRIBUTING.md`](../../CONTRIBUTING.md).
