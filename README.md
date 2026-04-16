<!-- omit in toc -->
<h1 align="center">Deep Research Protocol</h1>

<p align="center">
  <strong>Stop asking one AI to do deep research. Ask five. Then consolidate.</strong>
</p>

<p align="center">
  An open, opinionated method for running deep research on <b>ChatGPT, Claude, Gemini, Grok and Perplexity in parallel</b> — then cross-consolidating the five reports into a single, source-verified brief with confidence scores and quality gates.
  <br/>
  <em>It's a meta-protocol, not another deep-research agent.</em>
</p>

<p align="center">
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  <a href="./CHANGELOG.md"><img src="https://img.shields.io/badge/version-v1.0.0-brightgreen.svg" alt="Version"></a>
  <img src="https://img.shields.io/badge/status-production--ready-success.svg" alt="Status">
  <img src="https://img.shields.io/badge/docs-bilingual%20EN%20%7C%20ES-blueviolet.svg" alt="Bilingual">
  <img src="https://img.shields.io/badge/platforms-ChatGPT%20%7C%20Claude%20%7C%20Gemini%20%7C%20Grok%20%7C%20Perplexity-informational" alt="Platforms">
  <a href="https://x.com/carlosrodera_"><img src="https://img.shields.io/badge/follow-%40carlosrodera___-1DA1F2?logo=x" alt="X"></a>
</p>

---

## Table of contents

- [The problem](#the-problem)
- [The fix](#the-fix)
- [How it works](#how-it-works)
- [30-second quickstart](#30-second-quickstart)
- [Install as a Claude Skill](#install-as-a-claude-skill)
- [Use cases](#use-cases)
- [Who is this for](#who-is-this-for)
- [Why this, not another DR agent](#why-this-not-another-dr-agent)
- [Repo layout](#repo-layout)
- [Docs](#docs)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Related work](#related-work)
- [License · Author · Credits](#license--author--credits)

---

## The problem

Every major "deep research" agent — **ChatGPT Deep Research, Gemini Deep Research, Claude Deep Research, Perplexity Pro, Grok DeepSearch** — has the same failure mode:

- **Single-engine bias.** Each system has different training data, different web access, different retrieval heuristics. Ask one, get its slice of reality.
- **Citation hallucination.** A 2026 arXiv survey on deep research systems calls citation accuracy *"a common concern, with multiple instances of hallucinations or erroneous citations, including references to nonexistent articles and incorrect attribution of fictitious articles to real researchers."* ([Huang et al., 2026](https://arxiv.org/pdf/2506.12594))
- **No reproducibility.** Run the same question twice on the same engine, you get two subtly different answers. Run it on another engine, the delta is larger.

Product reports, regulatory briefs, competitive analyses and knowledge bases get shipped on top of that fog.

## The fix

**Run the same scientifically-structured prompt on 5 engines in parallel. Consolidate by consensus.** That's the whole idea.

What happens concretely:

1. You fill one **mega-prompt** with your question, audience, jurisdiction, and a hard methodology (scope builder → strategic questions → evidence hierarchy → source quotas → anti-hallucination rules → quality gates).
2. You launch it **in parallel** on 4–5 Deep Research engines.
3. You run a **consolidation prompt** that cross-references the five reports:
   - **Consensus** (≥ 3 engines agree) → high-confidence core knowledge.
   - **Discrepancies** → surfaced with source attribution and resolved by an explicit evidence hierarchy.
   - **Unique signal** (only one engine) → flagged as "verify or discard".
   - **Gaps** → subtopics no engine covered well; you fill them manually from primary sources.
4. You get one verified brief, with **confidence scores 0.0–1.0 on every key finding**, and a prioritized list of primary sources to download.

The same protocol then feeds any downstream deliverable — a knowledge base, a specialized agent, a market report, a compliance audit, a strategy doc. See [use cases](#use-cases).

## How it works

```
      ┌────────────────────────────────────────────┐
      │         ONE  MEGA-PROMPT  (v3.0)           │
      │  scope · questions · evidence hierarchy ·  │
      │  source quotas · quality gates             │
      └───────┬──────────────────────────────┬─────┘
              │  same prompt in parallel     │
   ┌──────────┼──────────┬──────────┬────────┼──────────┐
   ▼          ▼          ▼          ▼        ▼          ▼
┌──────┐  ┌──────┐   ┌──────┐   ┌──────┐  ┌────────────┐
│ChatGPT│  │Claude│   │Gemini│   │ Grok │  │ Perplexity │
│  DR   │  │  DR  │   │  DR  │   │  DS  │  │     Pro    │
└──┬────┘  └──┬───┘   └──┬───┘   └──┬───┘  └──────┬─────┘
   │          │          │          │             │
   └──────────┴──────────┼──────────┴─────────────┘
                         ▼
              ┌────────────────────────┐
              │  CONSOLIDATION PROMPT  │
              │  consensus · conflict  │
              │  gaps · confidence     │
              └──────────┬─────────────┘
                         ▼
              ┌────────────────────────┐
              │  VERIFIED BRIEF  +     │
              │  primary sources list  │
              └────────────────────────┘
```

Full methodology in [`docs/methodology.md`](./docs/methodology.md).

## 30-second quickstart

```bash
git clone https://github.com/carlosrodera/deep-research-protocol
cd deep-research-protocol
cat research-prompt.md              # the canonical mega-prompt v3.0
```

1. Open [`research-prompt.md`](./research-prompt.md).
2. Fill the **Inputs** block (domain, audience, territory, date, depth).
3. Pick a **domain variant** (A: technical · B: regulatory · C: mixed).
4. Paste `base + domain + platform variant` into each of the 5 engines. Hit go.
5. Save each report to `workspace/research/raw/research-<platform>.md`.
6. Run the **Consolidation Prompt** ([`templates/consolidation-prompt.md`](./templates/consolidation-prompt.md)) on the 5 reports. Output: your verified brief.

Full walk-through: [`docs/quickstart.md`](./docs/quickstart.md).

## Install as a Claude Skill

For Claude Code / Claude.ai users: the entire protocol ships as an installable Skill.

```bash
git clone https://github.com/carlosrodera/deep-research-protocol
ln -s "$(pwd)/deep-research-protocol/skill" ~/.claude/skills/deep-research-protocol
```

Then in Claude Code: `/skills` → `deep-research-protocol` → *"Run the DRP on `<your question>`."* The skill auto-detects your language (EN / ES) and walks you through the entire flow producing versioned artifacts.

## Use cases

DRP is a **research method**, not a product. It works for any deliverable that depends on verified, cross-platform evidence:

| Use case | What you ship | Guide |
|---|---|---|
| **Specialized AI agent** | A Custom GPT / Claude Project / Skill / Gem with a verified KB | [`use-cases/agent-building/`](./use-cases/agent-building/) |
| **Market / competitive report** | A decision-grade market brief with consensus + discrepancies | [`use-cases/market-report/`](./use-cases/market-report/) |
| **Strategic brief** | A board-ready narrative with counter-arguments weighed | [`use-cases/strategic-brief/`](./use-cases/strategic-brief/) |
| **Compliance / regulatory audit** | A jurisdiction-aware compliance map with primary sources | [`use-cases/compliance-audit/`](./use-cases/compliance-audit/) |

Your own use case deserves a folder — [contribute it](./CONTRIBUTING.md).

## Who is this for

- **Consultants, analysts, founders** who ship research-dependent deliverables and can't afford single-engine bias.
- **AI engineers** building specialized agents (RAG + prompt + eval) who need a verified knowledge base, not a folder of PDFs.
- **Compliance, legal and regulatory** teams who need traceable citations.
- **Product / strategy** leaders using AI for competitive research and want cross-platform consensus rather than the output of whichever engine they happen to open.
- **Researchers and educators** teaching evidence-based AI workflows.

If you're looking to "vibe your way through a Custom GPT in an afternoon", this is not for you.

## Why this, not another DR agent

DRP is **not** yet another deep research agent. It is a **human-operated meta-protocol** that runs *on top of* the agents you already have.

| | Deep research agents (LangChain [`open_deep_research`](https://github.com/langchain-ai/open_deep_research), TIGER [`OpenResearcher`](https://github.com/TIGER-AI-Lab/OpenResearcher), btahir [`open-deep-research`](https://github.com/btahir/open-deep-research)) | **Deep Research Protocol (this repo)** |
|---|---|---|
| What it is | An autonomous agent that does research for you | A method you run on top of existing DR agents |
| Competes with | ChatGPT DR, Gemini DR, Perplexity Pro | **Nothing** — it *uses* all of them |
| Bias exposure | Single-engine bias of whichever provider you choose | Cross-platform consensus ≥ 3 engines |
| Hallucination control | Depends on retrieval quality | Evidence hierarchy + confidence scores + source quotas |
| Runtime | Fire-and-forget | Human-in-the-loop orchestration |
| Setup cost | Install agent + API keys + infra | 0. Paste prompt into tabs. |

See full positioning and ecosystem map in [`docs/related-work.md`](./docs/related-work.md).

## Repo layout

```
deep-research-protocol/
├── README.md                   ← hero (you are here)
├── research-prompt.md           ← 🌟 the v3.0 mega-prompt — root-level for discoverability
├── LICENSE                      ← MIT
├── CHANGELOG.md                 ← versioned history
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── .github/
│   ├── ISSUE_TEMPLATE/         ← bug · feature · use-case submission
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── FUNDING.yml
├── docs/
│   ├── quickstart.md            ← step-by-step walk-through
│   ├── methodology.md           ← deep dive into the 5-platform flow
│   ├── evidence-hierarchy.md    ← conflict resolution
│   ├── confidence-scoring.md    ← the 0.0–1.0 rubric
│   ├── platform-variants.md     ← per-engine tuning
│   ├── related-work.md          ← ecosystem + academic refs
│   └── faq.md
├── skill/                       ← installable Claude Skill
│   ├── SKILL.md
│   ├── references/
│   └── assets/
├── use-cases/
│   ├── agent-building/          ← the original 5-phase agent method
│   ├── market-report/
│   ├── strategic-brief/
│   └── compliance-audit/
├── templates/
│   ├── consolidation-prompt.md  ← cross-platform fusion prompt
│   ├── anti-echo-prompt.md      ← contrarian stress-test variant
│   ├── research-prompt.es.md    ← Spanish canonical
│   └── use-case-template.md     ← for community contributions
├── schemas/
│   └── brief.schema.json        ← JSON Schema for the _meta output
├── scripts/
│   └── verify-citations.py       ← catches hallucinated citations
└── examples/
    └── walked-example-scaffold.md
```

## Docs

| Doc | What you'll find |
|---|---|
| [`docs/quickstart.md`](./docs/quickstart.md) | 7-step walk-through from question to verified brief |
| [`docs/methodology.md`](./docs/methodology.md) | The full method: why 5 platforms, why consensus, why confidence scores |
| [`docs/evidence-hierarchy.md`](./docs/evidence-hierarchy.md) | How to resolve source conflicts |
| [`docs/confidence-scoring.md`](./docs/confidence-scoring.md) | The 0.0–1.0 rubric and when to escalate below 0.7 |
| [`docs/platform-variants.md`](./docs/platform-variants.md) | How to tune the prompt per engine |
| [`docs/related-work.md`](./docs/related-work.md) | Academic references, competing repos, positioning |
| [`docs/faq.md`](./docs/faq.md) | "Does it work with only 2 engines? What if I don't have Grok? Etc." |

## Roadmap

- [x] **v1.0 — Research prompt v3.0** canonical release. Multi-platform, multi-domain, consolidation, skill, use-cases.
- [ ] **v1.1 — CLI helper** to scaffold `workspace/`, track runs, diff consolidations over time.
- [ ] **v1.2 — MCP server** exposing DRP as a tool so Claude Code / other MCP clients can auto-launch the multi-platform pass.
- [ ] **v1.3 — Automated evaluation** harness: re-run consolidated briefs against benchmarks ([DeepResearch Bench II](https://arxiv.org/pdf/2601.08536), [DeepResearchEval](https://arxiv.org/html/2601.09688v1)).
- [ ] **v1.4 — Community use-case library** with ≥ 10 contributed walked examples across domains.
- [ ] **v2.0 — DRP Studio**: a lightweight UI to paste reports side-by-side and run consolidation interactively.

Open an issue if you want to lead one of these.

## Contributing

PRs welcome — especially:

- **New use cases** documented against [`templates/use-case-template.md`](./templates/use-case-template.md).
- **Domain variants** for the mega-prompt (biomedical, foreign-jurisdiction legal, hardware, fintech…).
- **Platform variants** for new Deep Research engines as they ship.
- **Walked examples** using the scaffold, with source URLs and confidence scores. *Fabricated examples are rejected.*
- **Reference improvements** and bug fixes.

Read [`CONTRIBUTING.md`](./CONTRIBUTING.md) and [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md) before sending a PR.

## Related work

DRP sits in a crowded space. We owe a direct debt and clear differentiation to:

- **[langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research)** — configurable DR agent.
- **[TIGER-AI-Lab/OpenResearcher](https://github.com/TIGER-AI-Lab/OpenResearcher)** — 30B open DR model.
- **[btahir/open-deep-research](https://github.com/btahir/open-deep-research)** — multi-provider DR UI.
- **[nickscamara/open-deep-research](https://github.com/nickscamara/open-deep-research)** — Firecrawl-based DR agent.
- **[assafelovic/gptr-mcp](https://github.com/assafelovic/gptr-mcp)** — DR via MCP.
- **[langgptai/awesome-deep-research-prompts](https://github.com/langgptai/awesome-deep-research-prompts)** — prompt collection.

Academic references:

1. [*A Comprehensive Survey of Deep Research: Systems, Methodologies, and Applications*](https://arxiv.org/pdf/2506.12594) — arXiv 2506.12594.
2. [*DeepResearch Bench II: Diagnosing Deep Research Agents*](https://arxiv.org/pdf/2601.08536) — arXiv 2601.08536.
3. [*DeepResearchEval: An Automated Framework*](https://arxiv.org/html/2601.09688v1) — arXiv 2601.09688.
4. [*Deep Research Agents: Major Breakthrough or Incremental?*](https://www.jmir.org/2026/1/e88195/PDF) — JMIR 2026.

Full treatment in [`docs/related-work.md`](./docs/related-work.md).

## License · Author · Credits

**License:** MIT © 2026 [Carlos Rodera](https://x.com/carlosrodera_). Fork it, remix it, use it in production, sell it. Attribution appreciated.

**Author:** Carlos Rodera — applied AI consultant. X: [@carlosrodera_](https://x.com/carlosrodera_). Contact: [c@carlosrodera.com](mailto:c@carlosrodera.com).

**Credits:** DRP is synthesized from `deep_search_gpt v2.1` (Carlos Rodera, 2024–2026) and a year of private consulting work inside the *GPTs de Emprendedores* community. Research prompt structure influenced by the 2026 arXiv survey on deep research systems.

---

<p align="center">
  <em>If this saves you time, a ⭐ on the repo and a mention on X or LinkedIn helps other builders find it.</em>
</p>
