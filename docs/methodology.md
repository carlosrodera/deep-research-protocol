# Methodology

Why five engines, why consensus, why confidence scores — and why this is a meta-protocol rather than yet another deep research agent.

---

## 1 · The core problem DRP solves

Every major Deep Research engine has the same failure mode:

- **Single-engine bias.** Each system has different training data, different web access, different retrieval heuristics, different safety filters. The same question yields different-shaped answers.
- **Citation hallucination.** [A 2026 arXiv survey](https://arxiv.org/pdf/2506.12594) on deep research systems identifies citation accuracy as "a common concern, with multiple instances of hallucinations or erroneous citations, including references to nonexistent articles and incorrect attribution of fictitious articles to real researchers."
- **No reproducibility.** Same engine, same prompt, different runs → different answers. Different engine → delta multiplies.

DRP attacks all three at the orchestration layer: we can't fix the engines themselves, but we can **cross-validate** their outputs and **require** a rigorous protocol around how they are queried.

## 2 · Why five engines (not one, not ten)

Five is deliberately chosen. Below five you lose robust consensus; above five you hit diminishing returns and severe coordination cost.

| N engines | Consensus robustness | Coordination cost | Net value |
|---|---|---|---|
| 1 | None. Single-engine bias uncorrected. | Minimal. | Low. |
| 2 | Binary — either they agree or they don't. | Low. | Moderate. |
| 3 | Majority-of-three emerges. Usable consensus. | Low. | **Good.** |
| **4–5** | **Stable consensus. Outlier detection. Evidence triangulation.** | **Moderate.** | **Best.** |
| 6+ | Marginal gain. Each engine-in-parallel costs 5–20 min of human attention. | High. | Decreasing. |

**Operational rule:** 4–5 is the sweet spot. Minimum viable: 2 (below that, cross-validation adds no value). If you only have 2 engines available, weight both reports equally and manually verify every claim against a primary source.

## 3 · Why the engines disagree (and how we exploit it)

They disagree on:

- **Freshness.** Different crawl schedules. Perplexity is near-real-time; ChatGPT DR lags.
- **Source mix.** Gemini leans academic (Scholar integration); Grok leans X/social; Perplexity prioritizes official; Claude and ChatGPT are generalists with different training cutoffs.
- **Style.** Claude tends to hedge; GPT-5 tends to commit; Gemini structures longer; Grok injects contemporary signal.
- **Trained biases.** Each RLHF pipeline has different preferences baked in.

Cross-consolidation uses this variance as a feature: **agreement across engines with different biases is stronger evidence than agreement within one engine's ensemble**.

## 4 · The evidence hierarchy

When reports disagree, we do not take a popularity vote. We apply the tier:

1. **Meta-analyses / official bodies / primary legal texts** — gold standard.
2. **Peer-reviewed papers** — high quality, but check funding and publication venue.
3. **Technical reports, whitepapers, standards bodies** — strong for domain technical truth.
4. **Vendor / first-party official docs** — authoritative for their own product.
5. **Reputable journalism and industry analysts** — good for context, weak for precision.
6. **General press** — directional only.
7. **Community signals** (forums, X, Reddit) — leading indicators, not evidence.

A single tier-1 source beats five tier-6 sources that all cite each other. This is the **echo-chamber protection**.

See [`evidence-hierarchy.md`](./evidence-hierarchy.md) for the full conflict-resolution protocol.

## 5 · Source quotas as forcing function

The research prompt Step D enforces a minimum source mix:

- ≥ 3 primary / academic / canonical
- ≥ 2 regulatory / security-authoritative
- ≥ 2 industry / market / data
- ≥ 1 critical / counter-example

Without the quota, engines default to what they find easy. With the quota, they are forced to seek the hard sources — the ones that matter for enterprise decisions.

The **critical / counter-example** requirement is novel: it forces the engine to find at least one source that disagrees with the dominant narrative. This is DRP's single strongest defense against echo-chamber bias, and it is **not** present in any competing deep research system.

## 6 · Confidence scores

Every key finding in a DRP brief carries a confidence score `0.0–1.0`. The rubric:

- **0.9–1.0** — confirmed by ≥ 3 engines AND backed by ≥ 1 tier-1 source AND no contradictions.
- **0.7–0.89** — confirmed by ≥ 2 engines OR backed by 1 tier-1 source. No strong contradictions.
- **0.5–0.69** — one engine OR contradicted by a lower-tier source OR a forecast / estimate. **Must have a "why low" line.**
- **< 0.5** — single source, no cross-validation, or strong contradiction. Treat as hypothesis.

Findings below 0.7 must include an explicit reason (single source, conflicting sources, forecast, estimate, extrapolation from old data, etc.). See [`confidence-scoring.md`](./confidence-scoring.md) for the full rubric and worked examples.

## 7 · Quality gates

Before returning a brief, the engine self-checks against numeric gates (Step I):

- Clarity ≥ 9.5 / 10
- Specificity ≥ 0.95
- Completeness ≥ 48 / 50
- Structure ≥ 36 / 40
- Source quota met
- Anti-hallucination tags applied
- Every numeric claim carries uncertainty

Failing gates trigger a single self-iteration. Gates that still fail are surfaced explicitly at the top of the brief under **Known limitations**. This converts "silent failure" into "visible, triaged limitation" — a massive auditability win.

## 8 · The machine-readable `_meta` block

At the end of every brief, a YAML `_meta` block captures:

- Protocol version, prompt hash, run date, platform(s).
- Territory, language, domain variant, depth.
- Quality-gate scores.
- Source counts per tier.
- Finding counts, low-confidence count, hallucination count.

This block validates against [`schemas/brief.schema.json`](../schemas/brief.schema.json) and enables:

- **Automated QA** — CI can refuse briefs that fail gates.
- **Longitudinal diffing** — track how a brief's metadata evolves over time.
- **Portfolio-level reporting** — "across 40 briefs this quarter, 82% passed source quota, median confidence was 0.78".
- **Downstream consumption** — agents / tools can parse briefs programmatically.

No other open-source DR project emits machine-readable metadata. This is one of DRP's strongest enterprise signals.

## 9 · Why this is a meta-protocol, not an agent

DRP does not compete with ChatGPT Deep Research, Gemini DR, or open-source DR agents like LangChain's `open_deep_research` or TIGER's `OpenResearcher`. It runs **on top of** them.

| Dimension | DR agents (single-engine or built stack) | **DRP (meta-protocol)** |
|---|---|---|
| What it is | An autonomous system that does research | A method you apply on top of existing systems |
| Install | API keys, infra, sometimes GPUs | `git clone` + paste |
| Bias exposure | Single-engine or single-stack | Cross-platform consensus |
| Hallucination defense | Retrieval quality | Evidence hierarchy + confidence scores + quota + verifier script |
| Setup cost | High | Near-zero |
| Who runs it | Autonomous | Human-in-the-loop |
| Output | Research report | Research report **+** auditable metadata |
| Reproducibility | Non-deterministic | Versioned prompt + hash |

DRP treats the existing DR engines as a portfolio of complementary experts. You get to use all of them.

## 10 · When DRP is not the right tool

Be honest about limitations:

- **Quick factual lookups** — if you just need to verify a single fact, one engine with one prompt is fine.
- **Real-time monitoring** — DRP is not a streaming system. For alerts, use a dedicated monitoring stack.
- **Automated pipelines with strict latency** — a full DRP pass is 30–90 min of human-orchestrated work. For sub-minute automation, pick a single-engine DR agent with a programmatic API.
- **Truly proprietary domains** — if your question depends on non-public data (internal docs, private customer data), no public DR engine will help. Use a private RAG system; DRP's methodology can still inform how you structure and verify it.

## 11 · References

1. [*A Comprehensive Survey of Deep Research: Systems, Methodologies, and Applications*](https://arxiv.org/pdf/2506.12594) — arXiv 2506.12594, 2026.
2. [*DeepResearch Bench II: Diagnosing Deep Research Agents*](https://arxiv.org/pdf/2601.08536) — arXiv 2601.08536, 2026.
3. [*DeepResearchEval: An Automated Framework for Deep Research Task Construction and Agentic Evaluation*](https://arxiv.org/html/2601.09688v1) — arXiv 2601.09688, 2026.
4. [*Viewpoint: Deep Research Agents — Major Breakthrough or Incremental?*](https://www.jmir.org/2026/1/e88195/PDF) — JMIR, 2026.
