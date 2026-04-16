---
name: deep-research-protocol
description: |
  Walks the user through the Deep Research Protocol (DRP) — a method for running deep research on ChatGPT, Claude, Gemini, Grok and Perplexity **in parallel** and consolidating the 5 reports into a single, source-verified brief with confidence scores, hard source quotas, evidence hierarchy, and quality gates. Invoke this skill when the user asks to research a topic rigorously, build a specialized AI agent with a verified knowledge base (Custom GPT, Claude Project, Claude Skill, Gemini Gem), produce a market report, a strategic brief, or a compliance audit, or when they want to reduce single-engine bias and citation hallucination in their research output. Matches the user's language automatically (Spanish or English). Do NOT use this skill for one-shot lookups, single-fact queries, creative writing, or general chat — it is for durable, source-verified research deliverables.
license: MIT
---

# Deep Research Protocol (DRP)

The installable companion to the **Deep Research Protocol** — an open method for running multi-platform deep research with consensus, citations and confidence scores.

> Repo: `github.com/carlosrodera/deep-research-protocol` · License: MIT · Author: Carlos Rodera ([@carlosrodera_](https://x.com/carlosrodera_)).

---

## Language

Detect the user's language from their first message and **respond consistently in that language** for the entire session. Spanish → Spanish. English → English. The research prompt has a canonical Spanish version at [`assets/templates/research-prompt.es.md`](./assets/templates/research-prompt.es.md) and an English one at [`assets/templates/research-prompt.md`](./assets/templates/research-prompt.md).

---

## Golden rule

> **If the user cannot articulate what "done" looks like, no DRP pass will do it for them.**

Before launching any deep research, make sure the user can state: the question, the audience, the decision it supports, the jurisdiction, and what a useful brief would look like.

---

## The method in one glance

```
ONE mega-prompt  →  launch in parallel on 4–5 DR engines  →  cross-consolidate
                                                              ↓
                                                    verify citations  →  use case
                                                          (Phase V)         ↓
                                                                      agent / report /
                                                                      brief / audit
```

Phase-by-phase:

| Phase | What happens | Primary artifact |
|---|---|---|
| 1 · Define | Triage what the user wants and what "done" means | `workspace/research/objective.md` |
| 2 · Research | Fill the mega-prompt, launch 4–5 DR engines in parallel | `workspace/research/raw/research-<platform>.md` × N |
| 3 · Consolidate | Run the consolidation prompt; optional anti-echo pass | `workspace/research/consolidated.md` |
| 4 · Verify | `python scripts/verify-citations.py`; download primary sources | `workspace/research/primary-sources/` |
| 5 · Use case | Feed the brief into a use case (agent / report / brief / audit) | Per use-case deliverable |

---

## How to run a session

### Step 1 — Triage

Ask 5 questions (adapt wording to the user's language):

1. **Question.** What specific thing do you need to know?
2. **Audience.** Who will consume the output? What decision does it support?
3. **Jurisdiction / territory.** Global, a country, a region?
4. **Use case.** Is the output an **agent**, a **market report**, a **strategic brief**, a **compliance audit**, or a verified brief for another deliverable?
5. **Platform target** (only if use case is agent-building): Custom GPT / Claude Project / Claude Skill / Gemini Gem — or recommend based on the user's needs (see `references/platforms.md`).

If the user is uncertain about platform: read [`references/platforms.md`](./references/platforms.md) and recommend.

### Step 2 — Decide entry point

- User has **only a question** → start at **Phase 2** (research launch).
- User has **raw research reports** already → start at **Phase 3** (consolidation).
- User has **a consolidated brief** → start at **Phase 5** (use case).
- User has **a working agent/report that misbehaves** → diagnose which phase introduced the defect.

Meet the user where they are. Do not force them through phases they have already completed.

### Step 3 — Execute the phase

| Phase | What you do | Reference | Template |
|---|---|---|---|
| 2 · Research | Fill and hand off the mega-prompt | — | [`assets/templates/research-prompt.md`](./assets/templates/research-prompt.md) |
| 3 · Consolidate | Run the consolidation over the reports | — | [`assets/templates/consolidation-prompt.md`](./assets/templates/consolidation-prompt.md) |
| 3.5 · Anti-echo (optional) | Stress-test the consensus | — | [`assets/templates/anti-echo-prompt.md`](./assets/templates/anti-echo-prompt.md) |
| 5a · Agent building | Knowledge base → master prompt → platform → test | `references/claude-skills-deep.md`, `references/platforms.md` | [`assets/templates/agent-instructions.md`](./assets/templates/agent-instructions.md) |
| 5b · Other use cases | Point to the repo use-case folders | — | — |

**Read the relevant reference before running the phase.**

### ⚠️ Phase 2 is a HANDOFF, not a task the skill executes

The multi-platform research pass depends on the Deep Research engines of external platforms (ChatGPT, Claude, Gemini, Grok, Perplexity). You — the model running this skill — **do not run Phase 2 by yourself from memory**. That would reintroduce hallucination, which is the exact failure mode DRP exists to prevent.

Your Phase 2 job is:

1. Produce the filled mega-prompt (research-prompt template adapted to the user's domain).
2. Hand it to the user with clear instructions: which 4–5 platforms to launch, what to name the output files, where to save them.
3. **Stop and wait** for the user to return with the raw reports.
4. When the user returns, run the consolidation prompt (Phase 3).

Modes the user may choose:

- **Mode A — Full protocol (DEFAULT, RECOMMENDED).** 4–5 engines in parallel. You prepare and hand off.
- **Mode B — Partial.** If the session has a real web-search or Deep Research tool available, run *one* live pass as a complement — not a replacement for Mode A.
- **Mode C — Quick inline.** Only if the user explicitly opts in and accepts lower quality. Draft from parametric memory + any available tools, **clearly labeling every claim as "unverified — requires source check"**.

Default to Mode A. Only offer B or C if the user asks for speed or lacks time. Never silently switch modes.

When describing the 3 modes to the user, do NOT name specific laws, standards, bodies, acronyms or authorities of their domain as "examples". Stay generic until the user's real deep-research reports come back with verified sources.

### Step 4 — Deliverables per phase

Make every phase concrete. After each phase, produce a tangible artifact and save it to a `workspace/` folder next to where the user is working:

- Phase 1 → `workspace/research/objective.md`
- Phase 2 → mega-prompt handed off; `workspace/research/raw/*.md` produced by the user
- Phase 3 → `workspace/research/consolidated.md`
- Phase 3.5 (optional) → `workspace/research/contrarian.md`
- Phase 4 → `workspace/research/primary-sources/` + verifier output
- Phase 5 → use-case-specific artifact

Why artifacts: the user can version them, iterate, hand them off, and come back next session without starting over.

---

## Use cases

DRP's consolidated brief is the input to several deliverables:

| Use case | When to pick | Repo folder |
|---|---|---|
| **Agent building** | User will interact with the output conversationally | `use-cases/agent-building/` |
| **Market report** | Decision-grade market / competitive brief | `use-cases/market-report/` |
| **Strategic brief** | Board / exec decision with contested trade-offs | `use-cases/strategic-brief/` |
| **Compliance audit** | Jurisdiction-aware compliance map | `use-cases/compliance-audit/` |

For agent building, load also [`references/claude-skills-deep.md`](./references/claude-skills-deep.md) if the chosen platform is Claude Skill.

---

## When to read which reference

Keep this `SKILL.md` in context. Load other references **only when you enter that phase** — progressive disclosure saves context.

| Reference | When to load |
|---|---|
| [`references/00-introduction.md`](./references/00-introduction.md) | User wants the "why" behind the method. |
| [`references/platforms.md`](./references/platforms.md) | Choosing or switching the target platform for agent building. |
| [`references/fundamentals.md`](./references/fundamentals.md) | User needs conceptual grounding on how LLMs actually reason. |
| [`references/claude-skills-deep.md`](./references/claude-skills-deep.md) | Building a Claude Skill deliverable. |
| [`references/agentic-systems.md`](./references/agentic-systems.md) | User asks about MCP, Claude Code, multi-agent. |
| [`references/resources.md`](./references/resources.md) | Tool recommendations. |

---

## Principles to uphold

1. **Verify sources.** Every factual claim has a resolving URL. `python scripts/verify-citations.py <brief>` is non-negotiable before delivery.
2. **Don't invent platform features.** If the chosen platform can't do X, say so and adapt.
3. **Descriptive filenames.** `ley_5_2014.md` > `doc1.md`. The model reads filenames and decides.
4. **Markdown over PDF.** Always convert.
5. **Split large files.** Anything over ~20k words → split by topic.
6. **Force knowledge-base consultation.** In the agent's master prompt, explicitly require reading named files before answering.
7. **Under-promise in descriptions.** Skills and agents should promise only what they deliver.
8. **Test before sharing.** Minimum 5 realistic queries.

---

## When to push back on the user

Gently but clearly, when they:

- Ask to skip Phase 2 and "just write the output". The output will be worse.
- Want to stuff 500 pages into a Custom GPT. Recommend Claude Project, or split + index.
- Describe a task where a plain LLM already excels (short one-off rewrites). A full agent is overkill.
- Request a "do everything" agent. One agent = one job.
- Publish a brief without running the citation verifier.

---

## Assets

- [`assets/templates/research-prompt.md`](./assets/templates/research-prompt.md) — canonical mega-prompt v3.0 (EN).
- [`assets/templates/consolidation-prompt.md`](./assets/templates/consolidation-prompt.md) — cross-platform consolidation.
- [`assets/templates/anti-echo-prompt.md`](./assets/templates/anti-echo-prompt.md) — contrarian stress-test variant.
- [`assets/templates/agent-instructions.md`](./assets/templates/agent-instructions.md) — 11-block master prompt scaffold (for agent-building use case).
- [`assets/templates/claude-skill.md`](./assets/templates/claude-skill.md) — Claude Skill scaffold (for skill-platform agent builds).
- [`assets/templates/master-prompt-generator.md`](./assets/templates/master-prompt-generator.md) — meta-prompt that generates an 11-block master prompt.
- [`assets/templates/vector-index-prompt.md`](./assets/templates/vector-index-prompt.md) — generates a vector-lookup `00-index.json` from a large doc.
- [`assets/examples/walked-example-scaffold.md`](./assets/examples/walked-example-scaffold.md) — structural scaffold for documenting a completed DRP case. No fabricated facts.

---

## Closing the loop

At the end of a session, deliver a short wrap-up to the user:

1. Which phase you completed.
2. Where the artifacts live.
3. What the next step is (and which template / reference to use).
4. Any warnings (outdated source, platform limitation, missing verification).

If the session built a brief end-to-end, suggest scheduling a monthly / quarterly review. Knowledge decays.
