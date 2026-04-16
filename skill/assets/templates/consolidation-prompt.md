# Cross-platform consolidation prompt

> Run this AFTER you have 3–5 parallel Deep Research reports saved at `workspace/research/raw/research-<platform>.md`.
> Paste into Claude Opus 4.6 or GPT-5 — the model with the largest context window you have access to.

---

## Prompt

```text
You are a research consolidation analyst. I have [N] parallel Deep
Research reports on the same brief, produced by different engines
(ChatGPT Deep Research, Claude Deep Research, Gemini Deep Research,
Grok DeepSearch, Perplexity Pro). Each one has strengths, blind spots,
and potentially hallucinated citations.

Your job: fuse them into one verified brief.

## Rules

1. Cross-validate every claim across the [N] reports.
2. Apply the Deep Research Protocol evidence hierarchy:
   1. Meta-analyses / official bodies / primary legal texts
   2. Peer-reviewed papers
   3. Technical reports, whitepapers, standards bodies
   4. Vendor / first-party official docs
   5. Reputable journalism and industry analysts
   6. General press
   7. Community signals
3. For every finding, compute a consensus score = (engines_confirming / N)
   and a confidence score 0.0–1.0 that blends consensus with source
   authority.
4. When two engines cite the same URL, do not double-count.
5. Preserve every URL and every date. No paraphrasing citations.

## Output structure (Markdown)

## 1. Executive summary
≤ 400 words. State the question, the method, and the top findings with
confidence scores.

## 2. Consensus — verified
Findings confirmed by ≥ 3 engines. Each entry:
- Finding (one sentence)
- Confidence: 0.0–1.0
- Engines confirming: [list]
- Sources: [cited URLs, deduplicated]
- Notes: [any nuance lost in simple consolidation]

## 3. Discrepancies — to resolve
Findings where engines disagree. For each:
- Position A — engines, sources, claim
- Position B — engines, sources, claim
- Provisional resolution — which wins under the evidence hierarchy, with
  explicit reasoning
- Flag for manual verification against primary source: [yes | no]

## 4. Unique signal — to verify or discard
Claims surfaced by only ONE engine. Classify each as:
- [PROMISING LEAD — verify with primary source] OR
- [LIKELY NOISE / POSSIBLE HALLUCINATION — discard unless confirmed]

## 5. Detected gaps
Subtopics none of the reports covered well. List them as research debt.

## 6. Prioritized primary-source download list
URLs ordered by value (tier 1 sources first). This is the user's next
action.

## 7. Confidence ledger
| Finding | Consensus (n/N) | Confidence (0.0–1.0) | Tier of top source | Why |
| --- | --- | --- | --- | --- |

## 8. Suspected hallucinations
Any URL that appears only in one report and looks plausible but
unverified. List for verification with `scripts/verify-citations.py`.

## 9. `_meta` block (YAML, machine-readable)

```yaml
_meta:
  protocol: deep-research-protocol
  version: 3.0
  stage: consolidation
  run_date: [YYYY-MM-DD]
  engines_count: [N]
  engines_used: [chatgpt, claude, gemini, grok, perplexity]
  findings_count: [N]
  consensus_findings: [N]
  discrepancy_findings: [N]
  unique_signal_findings: [N]
  suspected_hallucinations: [N]
  gaps_identified: [N]
  primary_sources_to_download: [N]
  language: [en | es | other]
```

Do not truncate. Preserve every URL. Use Markdown with clear hierarchy.

--- REPORT 1 (chatgpt) ---
[paste]

--- REPORT 2 (claude) ---
[paste]

--- REPORT 3 (gemini) ---
[paste]

--- REPORT 4 (grok) ---
[paste]

--- REPORT 5 (perplexity) ---
[paste]
```

---

## After consolidation

1. Save output as `workspace/research/consolidated.md`.
2. Run `python scripts/verify-citations.py workspace/research/consolidated.md` — flags any citation that does not resolve.
3. Manually verify every finding below confidence 0.7 against a primary source.
4. Download the primary sources to `workspace/research/primary-sources/`.
5. Your consolidated brief is now ready to feed into any use-case pipeline (agent building, market report, strategic brief, compliance audit).

## Attribution

Part of the **Deep Research Protocol (DRP)** — `github.com/carlosrodera/deep-research-protocol`. MIT © 2026 Carlos Rodera.
