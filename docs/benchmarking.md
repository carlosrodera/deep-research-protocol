# Benchmarking plan

DRP is a method. To back its claims with data, we need empirical evaluation against established DR benchmarks. This is the plan — contributions welcome.

> Status: **design stage (v1.0).** Initial results target v1.3. This doc describes the methodology.

---

## Why benchmark

DRP's core claim is that cross-platform consensus + evidence hierarchy + confidence scores + source quotas produce **better** briefs than any single engine alone. "Better" has to mean something measurable. Without benchmarks, DRP is an argument; with them, it's a finding.

The DR literature already has benchmarks — we adopt them rather than invent our own.

---

## Benchmarks in scope

### 1 · DeepResearch Bench II (arXiv 2601.08536)

Dimensions: **information recall, analysis, presentation** — each with 0-1 normalized scores.

Fit for DRP: directly compatible. We run DRP (consolidated output) on the benchmark tasks and compare against single-engine baselines on the same tasks.

### 2 · DeepResearchEval (arXiv 2601.09688)

A persona-driven, two-stage task construction framework. Emits research tasks anchored in realistic user profiles.

Fit for DRP: particularly good for use-case validation (agent building, market report, compliance audit) — DeepResearchEval tasks are persona-realistic, which DRP's use-case library deliberately targets.

### 3 · BrowseComp-Plus (the OpenResearcher benchmark)

Fit: more narrowly retrieval-oriented. Optional baseline; may show DRP's **retrieval**-only pass (without consolidation) lags specialized retrieval-tuned models like OpenResearcher. That's fine — DRP's claim is about **downstream brief quality**, not raw retrieval.

---

## Experimental design

### Baselines

For each benchmark task, measure:

1. **S1 — Single-engine ChatGPT DR** (most common baseline).
2. **S2 — Single-engine Claude DR**.
3. **S3 — Single-engine Gemini DR**.
4. **S4 — Single-engine Perplexity Pro**.
5. **S5 — Single-engine Grok DeepSearch**.

### DRP conditions

6. **DRP-2** — DRP with 2 engines consolidated (lowest viable).
7. **DRP-3** — 3 engines consolidated.
8. **DRP-5** — full 5-engine consolidation (canonical).
9. **DRP-5+AE** — DRP-5 with anti-echo pass chained.

### Primary metrics (from DeepResearch Bench II)

- **Recall** (0-1): fraction of ground-truth facts surfaced.
- **Analysis** (0-1): quality of synthesis, comparison, trade-off articulation.
- **Presentation** (0-1): structure, clarity, navigability.

### DRP-specific metrics

- **Citation resolution rate**: fraction of cited URLs that resolve (measured by `verify-citations.py`). Targets ≥ 95% for DRP-5; single-engine baselines measured for comparison.
- **Hallucination count**: citations that look plausible but fail resolution (tier < 4xx) OR cite a real URL that does not contain the claim.
- **Source tier distribution**: mean tier of top-cited source per finding.
- **Confidence calibration**: for findings the engine rated ≥ 0.7, what fraction are actually correct against benchmark ground truth? (Overconfidence signal.)

### Human-evaluated metric

- **Actionability** (1-5 Likert): independent graders rate whether the brief enables a concrete decision.

---

## Hypotheses (pre-registered)

H1. DRP-5 citation resolution rate ≥ single-engine best by ≥ 10 pp.
H2. DRP-5 hallucination count ≤ 50% of the worst-performing single-engine baseline.
H3. DRP-5 recall > single-engine best by ≥ 5 pp on multi-topic tasks.
H4. DRP-5 mean source tier ≤ 2.5 vs single-engine ≥ 3.5 (lower = better tier).
H5. DRP-5+AE reduces false consensus on contrarian tasks by ≥ 30% vs DRP-5.
H6. Confidence calibration improves monotonically with engine count (S1 < DRP-2 < DRP-3 < DRP-5).

---

## Cost

Rough budget for running the full evaluation once:

| Component | Cost |
|---|---|
| 30 benchmark tasks × 9 conditions × ≤ $2/DR run | ~$540 |
| 2 graders × 30 tasks × 30 min × $40/h | ~$1200 |
| Consolidation compute (Claude Opus 4.6 / GPT-5) | ~$80 |
| **Total per eval cycle** | **~$1,800** |

Modest. Sponsorable. If you have budget, we welcome partial underwriting in exchange for named credit in the eval publication.

---

## Reproducibility

All materials:

- Tasks, prompts, reports (per engine, per condition) committed to a public `benchmarks/` folder (when this work lands).
- `_meta` blocks from every run captured for portfolio-level analysis.
- Grader rubrics and raw scores published.
- Scripts for aggregation (`scripts/bench-aggregate.py`) — planned.

If a result does not hold, we publish it. The point of benchmarking is honest signal.

---

## Call for collaborators

If you want to lead or contribute to this:

- **Eval engineer** — design eval harness, run conditions, aggregate metrics.
- **Grader pool** — 2–4 domain experts per benchmark run.
- **Infra sponsor** — API credits across 5 providers.
- **Academic partner** — venue for publication (workshop / tech report / arXiv).

Open an issue with the tag `benchmark` or DM [@carlosrodera_](https://x.com/carlosrodera_).
