# Changelog

All notable changes to the Deep Research Protocol are documented here. Format: [Keep a Changelog](https://keepachangelog.com/). Versioning: [SemVer](https://semver.org/).

## [1.0.0] — 2026-04-16

### Overview

First public release of the **Deep Research Protocol (DRP)** — an open, opinionated method for running deep research across ChatGPT, Claude, Gemini, Grok, and Perplexity **in parallel**, then cross-consolidating the five reports into a single, source-verified brief.

DRP is not another deep research agent. It is a meta-protocol that runs on top of the agents you already have. It addresses the #1 failure mode of single-engine deep research: citation hallucination and single-platform bias.

### Added

#### Core artifact

- **Research prompt v3.0** ([`research-prompt.md`](./research-prompt.md)) — the canonical multi-platform mega-prompt. Includes:
  - Scope builder (run before search)
  - Strategic questions (cover causes, effects, trade-offs, biases)
  - Evidence hierarchy for conflict resolution
  - Hard source quotas (≥ 3 primary, ≥ 2 regulatory / security-authoritative, ≥ 2 industry, ≥ 1 critical counter-example)
  - Anti-hallucination protocol with `[FACT]` / `[INFERENCE]` / `[UNVERIFIED]` tags
  - Confidence scores 0.0–1.0 on every key finding
  - Quality gates with numeric thresholds and a self-iteration loop
  - Machine-readable `_meta` YAML output block
  - 3 domain variants: A (technical / software), B (regulatory / legal / standards), C (mixed)
  - 5 platform variants: ChatGPT Deep Research, Claude Deep Research, Gemini Deep Research, Grok DeepSearch, Perplexity Pro

#### Differentiating tooling (no other DR repo has these)

- **[`scripts/verify-citations.py`](./scripts/verify-citations.py)** — parses a consolidated brief, extracts every cited URL, verifies resolution + freshness. Flags hallucinated or broken citations.
- **[`schemas/brief.schema.json`](./schemas/brief.schema.json)** — JSON Schema for the consolidated brief output. Enables machine-readable consumption and CI validation.
- **[`templates/consolidation-prompt.md`](./templates/consolidation-prompt.md)** — separated cross-platform consolidation prompt for independent reuse.
- **[`templates/anti-echo-prompt.md`](./templates/anti-echo-prompt.md)** — variant that surfaces disagreement first, for strategic decisions where consensus may be wrong.
- **[`templates/research-prompt.es.md`](./templates/research-prompt.es.md)** — Spanish localization of the mega-prompt.

#### Claude Skill

- **[`skill/SKILL.md`](./skill/SKILL.md)** — installable Claude Skill (name: `deep-research-protocol`), bilingual EN/ES, with progressive disclosure to per-phase references.
- **[`skill/references/`](./skill/references/)** — per-phase playbooks (research, knowledge-base, master-prompt, implementation, testing, platforms, fundamentals).
- **[`skill/assets/templates/`](./skill/assets/templates/)** — skill-internal templates mirroring the root ones.

#### Use cases

- **[`use-cases/agent-building/`](./use-cases/agent-building/)** — the 5-phase method for building specialized AI agents with a verified KB. This is what the first iteration of DRP was originally designed for.
- **[`use-cases/market-report/`](./use-cases/market-report/)** — generating decision-grade market and competitive briefs.
- **[`use-cases/strategic-brief/`](./use-cases/strategic-brief/)** — board-ready strategic narratives with counter-arguments weighed.
- **[`use-cases/compliance-audit/`](./use-cases/compliance-audit/)** — jurisdiction-aware compliance mapping with primary sources.

#### Documentation

- **[`README.md`](./README.md)** — hero, problem, method, quickstart, use cases, related work.
- **[`docs/quickstart.md`](./docs/quickstart.md)** — 7-step walk-through.
- **[`docs/methodology.md`](./docs/methodology.md)** — deep dive into why 5 platforms, why consensus, why confidence scores.
- **[`docs/evidence-hierarchy.md`](./docs/evidence-hierarchy.md)** — conflict-resolution rules.
- **[`docs/confidence-scoring.md`](./docs/confidence-scoring.md)** — 0.0–1.0 rubric.
- **[`docs/platform-variants.md`](./docs/platform-variants.md)** — per-engine tuning guidance.
- **[`docs/integrations.md`](./docs/integrations.md)** — export to Notion, Obsidian, Anki, Claude Project, Custom GPT, RAG indexes.
- **[`docs/benchmarking.md`](./docs/benchmarking.md)** — plan to empirically evaluate DRP vs. single-engine DR against DeepResearch Bench II.
- **[`docs/related-work.md`](./docs/related-work.md)** — ecosystem map + academic references + DRP vs. the rest matrix.
- **[`docs/faq.md`](./docs/faq.md)** — "Does it work with only 2 engines? What if I don't have Grok?"

#### Governance

- [`CONTRIBUTING.md`](./CONTRIBUTING.md), [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md), [`SECURITY.md`](./SECURITY.md).
- `.github/ISSUE_TEMPLATE/` — bug report, feature request, use-case submission.
- `.github/PULL_REQUEST_TEMPLATE.md`, `.github/FUNDING.yml`.

### Notes on genesis

DRP is synthesized from `deep_search_gpt v2.1` (Carlos Rodera, 2024–2026) — a prompt that ran inside the private *GPTs de Emprendedores* community for over a year — and a year of consulting work on specialized-agent builds. A prior, narrower iteration of this work was published as `deep-agent-protocol` and has been [archived](https://github.com/carlosrodera/deep-agent-protocol) in favor of this broader repositioning.
