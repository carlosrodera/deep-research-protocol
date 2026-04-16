# Platform variants

Per-engine tuning for the DRP mega-prompt. Each engine has different strengths; the variant tells the engine how to play to them.

---

## Why variants exist

The base prompt is engine-agnostic. The variants add one short suffix paragraph that:

1. Activates the right feature (Deep Research mode, DeepSearch, web-search tool).
2. Sets a minimum search depth appropriate for the engine.
3. Nudges the engine toward its comparative strength (Perplexity → official sources, Grok → X signal, Gemini → Scholar, ChatGPT → breadth, Claude → rigor).

---

## The five canonical variants

Source of truth: [`../research-prompt.md`](../research-prompt.md), section 3.

### ChatGPT Deep Research (GPT-5)

```text
Use Deep Research with 25–35 searches. Include an appendix listing every
URL consulted, grouped by Finding section. Prioritize official / primary
sources over derivative coverage.
```

Why this suffix:

- 25–35 searches is ChatGPT DR's productive range. Below 15 it skims; above 40 it over-browses without adding depth.
- The URL appendix is ChatGPT DR's native format and enables cross-checking without re-running the search.
- Explicit "official / primary" nudge counteracts its habit of weighting popular SEO results.

### Claude Deep Research (Opus 4.6) — or Claude + web search / MCP

```text
Use the web-search tool. Run ≥ 15 distinct searches across the variant
sections. If a page fails to load, retry with query variants. Prioritize
primary / canonical / first-party sources.
```

Why:

- Claude's web search is more controlled than agent-style DR; asking for ≥ 15 distinct searches counteracts under-browsing.
- Retry-with-variants instruction recovers from transient failures without hallucinating replacement content.
- "Primary / canonical / first-party" is Claude's natural strength — it rigorously cites but can under-browse if not prompted.

### Gemini Deep Research (2.5 Pro)

```text
Activate Deep Research with a plan of ≥ 20 sources. Include Google
Scholar where academic / technical papers exist. Begin with the
Executive Summary (max 400 words).
```

Why:

- Gemini DR works best with an explicit source-count target.
- Scholar integration is its strongest differentiator — always activate it for academic / technical domains.
- The executive summary upfront enables quick triage.

### Grok DeepSearch (Grok 4+)

```text
Activate DeepSearch with live X/Twitter access to detect the last
90 days of discussion, bug reports, and community sentiment. Clearly
separate "academic / official source" from "social-media signal".
Surface any trending security or reliability concerns.
```

Why:

- Grok's unique asset is real-time X access.
- The explicit separation prevents Grok from mixing social signal with official sources (its default weakness).
- "Last 90 days" focuses attention on signal that other engines cannot surface.

### Perplexity Pro

```text
Prioritize official sources (primary repositories, official docs,
gov / standards domains, CVE / NVD). De-prioritize affiliate listicles
and generic explainer posts unless they add unique technical depth.
```

Why:

- Perplexity's strength is fast, source-cited retrieval.
- Its weakness is that free-tier queries get polluted by SEO content; the explicit de-prioritization nudges it toward official tiers.

---

## How to add a new variant (new engine)

When a new Deep Research engine ships (there will be more — DeepSeek Research, Qwen Research, etc.):

1. Read its documentation and identify:
   - The feature activation (mode name, toggle, tool call).
   - Its comparative strength.
   - Its comparative weakness.
2. Draft a 3–5 line suffix with those three levers.
3. Test against the canonical 5 on two different domains. Compare output structure and source mix.
4. Open a PR adding the variant to [`../research-prompt.md`](../research-prompt.md) and this doc.

Template:

```text
Activate <feature mode> with <minimum depth parameter>. Prioritize
<source type that plays to strength>. Distinguish <signal that this
engine uniquely offers> from <weaker default signal>.
```

---

## Variant anti-patterns

- **Rewriting the base prompt.** The variant is a suffix. If you're rewriting Step A–J to fit an engine, you're off-protocol.
- **Over-constraining.** "Use exactly 50 searches at exactly these domains" — engines silently ignore and the output quality drops. Keep variants short and directional.
- **Adding engine-specific content requirements.** The base prompt's Step G domain variant does that. Platform variants only touch *how* the engine searches, not *what* it searches for.

---

## Degraded-mode advice

If you only have access to 2–3 engines:

- Prefer **Perplexity + Claude + ChatGPT** for maximum complementarity (official / rigor / breadth).
- Drop Grok if your domain is not social-signal-sensitive.
- Drop Gemini if your domain has no academic corpus.

Still run the consolidation prompt. Even 2-engine consolidation catches ~60% of single-engine-only bias.
