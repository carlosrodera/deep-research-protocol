# Deep Research Protocol · Research prompt v3.0 (canonical)

> The canonical multi-platform Deep Research mega-prompt.
> Paste into **ChatGPT Deep Research, Claude Deep Research, Gemini Deep Research, Grok DeepSearch, Perplexity Pro** in parallel (same prompt, per-platform suffix at the very end). Then run [`templates/consolidation-prompt.md`](./templates/consolidation-prompt.md) over the 5 reports.
>
> Spanish version: [`templates/research-prompt.es.md`](./templates/research-prompt.es.md).

---

## How to use

1. **Fill the Inputs block** (`USER_QUERY`, `AUDIENCE`, `TERRITORY`, `CURRENT_DATE`, `DEPTH`, `LANGUAGE_OF_OUTPUT`).
2. **Pick a domain variant** (A: technical / software · B: regulatory / legal · C: mixed) and insert at Step G.
3. **Pick a platform variant** (ChatGPT / Claude / Gemini / Grok / Perplexity) and append at the very end.
4. **Launch in parallel** on 4–5 engines. Minimum viable: 2. Below that, cross-validation adds no value.
5. Save each report as `workspace/research/raw/research-<platform>.md`.
6. Run [`templates/consolidation-prompt.md`](./templates/consolidation-prompt.md) in your strongest model over the 5 reports.
7. Run `python scripts/verify-citations.py workspace/research/consolidated.md` to validate every URL.
8. Output: a verified brief that conforms to [`schemas/brief.schema.json`](./schemas/brief.schema.json).

---

## 1 · Base prompt (paste first)

```text
Act as a senior research analyst. Reasoning effort: HIGH.

Your job is to convert a short user brief into an exhaustive, current,
source-cited and actionable research report that will feed a downstream
deliverable (specialized AI agent, market brief, strategy doc, compliance
map, etc.).

## Inputs (user-filled)

- USER_QUERY: [short natural-language brief of what must be covered]
- AUDIENCE: [who will consume the output — profile, expertise, decisions
  they face]
- TERRITORY / JURISDICTION: [global | country | region — state explicitly]
- CURRENT_DATE: [YYYY-MM-DD — treat anything older than 18 months as
  "possibly stale; verify"]
- DEPTH: [overview | deep]  // default: deep
- LANGUAGE_OF_OUTPUT: [en | es | other]

## Step A · Scope builder (BEFORE any search)

1. Restate the topic with precision: subject, time window, geography,
   disciplines involved.
2. Enumerate 6–10 critical subtopics and one sentence per subtopic
   explaining why it matters for the audience.
3. Declare the optimal depth for each subtopic (overview | deep).

Output this Scope block verbatim at the top of the final report.

## Step B · Strategic questions (BEFORE any search)

- 5–8 core questions covering causes, effects, alternatives, trade-offs.
- 6–12 second-order questions for nuance, non-obvious connections,
  evidence gaps.
- ≥ 2 questions explicitly about biases, limits, and replicability of
  the dominant narrative in the field.

Surface these questions in the report. They are the skeleton of the
investigation.

## Step C · Methodology & evidence hierarchy

Pick one approach: qualitative | quantitative | mixed. Justify briefly.

Declare techniques used: systematic review, comparative analysis,
light meta-analysis, secondary-source interview mining, ethical web
scraping (state yes/no).

Conflict-resolution rule (STRICT ordering, top wins):
  1. Meta-analyses / official bodies / primary legal texts
  2. Peer-reviewed papers
  3. Technical reports, whitepapers, standards bodies
  4. Vendor / first-party official docs
  5. Reputable journalism and industry analysts
  6. General press
  7. Community signals (forums, X/Twitter, Reddit)

If two sources of the same tier disagree, surface BOTH and pick one with
explicit reasoning.

## Step D · Sources policy (HARD QUOTA)

Deliver 8–15 high-quality sources with the following minimum mix:
- ≥ 3 academic / peer-reviewed (or — for technical domains — canonical
  primary specs, RFCs, or vendor reference docs)
- ≥ 2 regulatory / standards / official bodies (or — for pure software —
  release notes + security advisories)
- ≥ 2 industry / market / data reports
- ≥ 1 critical source or counter-example

For each source capture: title, author/org, exact date, URL, one-line
assessment of authority and potential conflict of interest.

## Step E · Web-research rules

- Prefer content ≤ 18 months old. If older, justify why the topic is
  stable enough to rely on it.
- Extract citations with date and author. Direct quotes ≤ 25 words per
  source.
- For numeric claims: state uncertainty range or margin of error. If
  absent from source, mark as "point estimate, no stated uncertainty".
- If data conflicts between sources, present both and conclude with an
  explicit criterion for preferring one.

## Step F · Anti-hallucination protocol (MANDATORY)

- Any claim without a working cited URL → tag `[UNVERIFIED]`.
- Distinguish `[FACT]` (source-backed) from `[INFERENCE]` (your synthesis).
- Assign a confidence score 0.0–1.0 to every KEY finding. Below 0.7
  requires an explicit "why low" line (single source, conflicting
  sources, estimate, forecast…).
- If you genuinely do not find information on a subtopic, say so
  explicitly and mark it as a gap — do not fabricate plausible-sounding
  content.

## Step G · Domain variant

Insert the chosen domain-variant block here (A, B, or C — see below).

## Step H · Output requirements

- Markdown with clear hierarchical headings (##, ###, ####).
- Begin with an **Executive Summary** (≤ 400 words).
- Follow with: Scope block → Strategic questions → Methodology →
  Findings by subtopic → Sources audit → Gaps & open questions →
  Confidence ledger (table: finding · confidence · rationale) →
  Primary-source download list.
- End with the machine-readable `_meta` YAML block below (verbatim field
  names). This block enables downstream automation.
- Do not truncate. If too long, deliver in complete sections.
- Output language: see LANGUAGE_OF_OUTPUT input.

### Machine-readable `_meta` block (end of report)

```yaml
_meta:
  protocol: deep-research-protocol
  version: 3.0
  prompt_hash: [SHA256 of base prompt you used]
  run_date: [YYYY-MM-DD]
  platform: [chatgpt | claude | gemini | grok | perplexity]
  territory: [from USER input]
  language: [from USER input]
  domain_variant: [A | B | C]
  depth: [overview | deep]
  quality_gates:
    clarity: [0-10]
    specificity: [0-1]
    completeness: [0-50]
    structure: [0-40]
    source_quota_met: [true | false]
    anti_hallucination_tagged: [true | false]
    all_numeric_claims_carry_uncertainty: [true | false]
  source_counts:
    primary: [N]
    regulatory_or_security: [N]
    industry: [N]
    counter_example: [N]
  findings_count: [N]
  findings_below_0_7_confidence: [N]
```

## Step I · Quality gates (self-check BEFORE returning)

Pass all or iterate once:
- Clarity ≥ 9.5 / 10
- Specificity ≥ 0.95
- Completeness ≥ 48 / 50 subtopics or strategic questions addressed
- Structure ≥ 36 / 40 (headings, ordering, navigability)
- Source quota met (Step D)
- Anti-hallucination tags applied (Step F)
- Every numeric claim carries uncertainty or a "point-estimate" flag
- `_meta` block complete and valid

If any gate fails: silently iterate once, then deliver. If still failing,
list the failed gates at the top under `## Known limitations of this
report`.

## Step J · Final validation

Walk multi-level: logical → factual → completeness → quality → strategic
alignment with the user's stated decision/audience. If any layer fails,
correct and re-validate before returning.
```

---

## 2 · Domain variants (choose one, insert at Step G)

### Variant A — Technical / software / DevOps

```text
## Domain variant: TECHNICAL / SOFTWARE

Add these dedicated sections to the Findings:

### T1. Project canon
- Canonical repository, current stable version, release cadence, license.
- Official docs structure.
- Authors / maintainers, governance, issue-filing norms, security-
  disclosure policy.
- Rename or major-rewrite history. Legacy config keys and env vars
  still aliased.

### T2. Architecture
- Runtime components, plugin/extension/skill system, adapters/drivers,
  on-disk layout.
- Configuration schema: fields, types, defaults, constraints.
- Supported integrations (LLM providers, storage, messaging, etc.) —
  per integration: auth flow, required env vars, rate limits, quirks.

### T3. Install & first-run
- Supported OSes, minimum requirements.
- Install paths with exact commands (package manager, Docker, source).
- First-run walkthrough to reach a minimal working state.
- Top-10 first-run errors → symptom / cause / fix.

### T4. Security
- Known CVEs and published advisories (link to CVE IDs).
- Permissions / scopes model.
- Hardening checklist (secrets rotation, network exposure, sandboxing,
  signing/verification, audit logging).
- Anti-patterns: what NOT to connect this software to.

### T5. Operations
- Logging paths, verbosity levers, structured-log format.
- Common error messages in GitHub issues / Discord / forums → fix.
- Upgrade / migration procedure between versions. Breaking changes
  timeline.
- Clean uninstall (state wipe, token revocation).

### T6. Ecosystem
- Community hubs (Discord, GitHub Discussions, Reddit, X).
- Notable forks, hosted variants.
- Comparable projects (1-paragraph: when pick this over them).

### T7. Roadmap & recent changes (last 6 months)
- Shipped, announced, deprecated.
```

### Variant B — Regulatory / legal / standards

```text
## Domain variant: REGULATORY / LEGAL / STANDARDS

Add these dedicated sections to the Findings:

### R1. Regulatory framework & canonical sources
- Applicable laws, norms, standards, regulations.
- For each: official name, year, most-recent amendment, official URL
  (BOE, EUR-Lex, Federal Register, iso.org, etc.).
- Any changes in the last 24 months.

### R2. Entities & key concepts
- 15–25 most-relevant institutions, actors, roles.
- Core technical/legal concepts and their operational definitions.
- Native-language terminology ↔ international equivalent.

### R3. Processes & typical workflows
- 5–10 operational processes. Per process: steps, responsible party,
  required documentation, legal deadlines.

### R4. Real-world use cases & FAQs
- 20–30 recurring questions from a typical user. For each a structured
  answer with legal / normative reference.

### R5. Grey zones, controversies, common mistakes
- Divergent interpretations between sources.
- Frequent application errors.
- Penalties, sanctions, typical consequences.

### R6. Updates & trends (last 24 months)
- Recent changes.
- Imminent changes announced.
- Where to follow the domain (bulletins, associations, canonical feeds).
```

### Variant C — Mixed (tech + regulation, e.g. fintech, healthtech, biotech)

```text
## Domain variant: MIXED

Include ALL sections from Variant A AND Variant B.
Cross-reference: for every technical capability, identify the applicable
regulatory constraint and cite both. Flag cases where technical practice
currently violates or strains regulation.
```

---

## 3 · Platform variants (append exactly one at the very end)

### ChatGPT Deep Research (GPT-5)
```text
Use Deep Research with 25–35 searches. Include an appendix listing every
URL consulted, grouped by Finding section. Prioritize official / primary
sources over derivative coverage.
```

### Claude Deep Research (Opus 4.6) — or Claude + web search / MCP
```text
Use the web-search tool. Run ≥ 15 distinct searches across the variant
sections. If a page fails to load, retry with query variants. Prioritize
primary / canonical / first-party sources.
```

### Gemini Deep Research (2.5 Pro)
```text
Activate Deep Research with a plan of ≥ 20 sources. Include Google
Scholar where academic / technical papers exist. Begin with the
Executive Summary (max 400 words).
```

### Grok DeepSearch (Grok 4+)
```text
Activate DeepSearch with live X/Twitter access to detect the last
90 days of discussion, bug reports, and community sentiment. Clearly
separate "academic / official source" from "social-media signal".
Surface any trending security or reliability concerns.
```

### Perplexity Pro
```text
Prioritize official sources (primary repositories, official docs,
gov / standards domains, CVE / NVD). De-prioritize affiliate listicles
and generic explainer posts unless they add unique technical depth.
```

---

## 4 · Checklist

- [ ] ≥ 4 engines launched in parallel (min 2)
- [ ] Territory / jurisdiction stated explicitly in every launch
- [ ] Current date stated explicitly in every launch
- [ ] Reports saved as `workspace/research/raw/research-<platform>.md`
- [ ] [`templates/consolidation-prompt.md`](./templates/consolidation-prompt.md) run, output at `workspace/research/consolidated.md`
- [ ] `python scripts/verify-citations.py workspace/research/consolidated.md` run, all citations resolve
- [ ] Primary sources identified and downloaded to `workspace/research/primary-sources/`
- [ ] ≥ 3 key claims manually verified against primary source
- [ ] `_meta` block complete and valid against [`schemas/brief.schema.json`](./schemas/brief.schema.json)

---

## 5 · Attribution

This prompt is the canonical artifact of the **Deep Research Protocol** (DRP).

- Protocol & synthesis: **Carlos Rodera** — X [@carlosrodera_](https://x.com/carlosrodera_).
- Synthesized from `deep_search_gpt v2.1` (2024–2026) and a year of private consulting work.
- License: MIT. Attribution appreciated.
- Repo: `github.com/carlosrodera/deep-research-protocol`.
