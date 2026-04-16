# Quickstart

From question to verified brief in under 90 minutes.

## 0 · What you need

- Access to **≥ 2** Deep Research engines (ideal: 4–5). Free tiers work for most:
  - **ChatGPT Deep Research** — OpenAI Plus / Pro.
  - **Claude Deep Research** — Anthropic Pro / Team.
  - **Gemini Deep Research** — Google AI Pro.
  - **Grok DeepSearch** — X Premium+.
  - **Perplexity Pro**.
- **Python ≥ 3.10** on your machine (only for `scripts/verify-citations.py`). No pip installs needed.
- A local `workspace/` folder to hold your artifacts.

## 1 · Clone the repo

```bash
git clone https://github.com/carlosrodera/deep-research-protocol
cd deep-research-protocol
mkdir -p workspace/research/{raw,primary-sources}
```

## 2 · Fill the mega-prompt

Open [`research-prompt.md`](../research-prompt.md). Copy the base prompt (section 1). Fill the **Inputs** block:

```text
- USER_QUERY: <what you need to know>
- AUDIENCE: <who will consume the output>
- TERRITORY / JURISDICTION: <global | country | region>
- CURRENT_DATE: <YYYY-MM-DD>
- DEPTH: deep
- LANGUAGE_OF_OUTPUT: en
```

Append one **domain variant** at Step G (A / B / C).

Spanish users: copy from [`templates/research-prompt.es.md`](../templates/research-prompt.es.md).

## 3 · Launch in parallel on 4–5 engines

Open each engine in a separate tab. For each:

1. Paste `base prompt` + `domain variant`.
2. At the very end, paste the **platform variant** from [`research-prompt.md`](../research-prompt.md) section 3.
3. Activate Deep Research / DeepSearch.
4. Hit go.

Each report takes 5–20 min. They run in parallel — start them all, then wait.

## 4 · Save the reports

As each report finishes, save it as Markdown:

```
workspace/research/raw/research-chatgpt.md
workspace/research/raw/research-claude.md
workspace/research/raw/research-gemini.md
workspace/research/raw/research-grok.md
workspace/research/raw/research-perplexity.md
```

## 5 · Run cross-platform consolidation

Open your strongest model (Claude Opus 4.6 or GPT-5 — the one with the biggest context window you can access).

Copy [`templates/consolidation-prompt.md`](../templates/consolidation-prompt.md) and paste all 5 reports into the placeholders. Hit go.

Save the output as `workspace/research/consolidated.md`.

## 6 · Verify citations

```bash
python scripts/verify-citations.py workspace/research/consolidated.md --verbose
```

Any **broken** citation is a hallucination signal. Either fix it (find the real source) or delete the claim. Transient failures (network, 5xx) can be re-checked later.

## 7 · (Optional) Anti-echo pass

If the question is strategic and you suspect a consensus might be wrong:

Copy [`templates/anti-echo-prompt.md`](../templates/anti-echo-prompt.md), paste the 5 raw reports again, and run it. Save as `workspace/research/contrarian.md`. Attach the "steelman of the opposite" section to your final deliverable.

## 8 · Download primary sources

Go through the **prioritized primary-source download list** at the end of `consolidated.md`. Download each to `workspace/research/primary-sources/` with descriptive filenames (`iso_28000_2022.pdf`, not `doc1.pdf`).

## 9 · Feed into a use case

`workspace/research/consolidated.md` is now your verified input. Feed it into one of:

- [`use-cases/agent-building/`](../use-cases/agent-building/) — build a specialized AI agent (the original DRP use case).
- [`use-cases/market-report/`](../use-cases/market-report/) — ship a decision-grade market brief.
- [`use-cases/strategic-brief/`](../use-cases/strategic-brief/) — board-ready narrative.
- [`use-cases/compliance-audit/`](../use-cases/compliance-audit/) — compliance map with primary citations.

Or use one of the patterns in [`docs/integrations.md`](./integrations.md) to export the brief to Notion, Obsidian, Anki, a Claude Project, a Custom GPT, or a RAG index.

## 10 · Schedule maintenance

Knowledge decays. Platforms change defaults. Sources get retracted.

Put a recurring reminder (monthly for fast-moving domains, quarterly for stable) to:

1. Re-run DRP with the same inputs.
2. Diff the new `consolidated.md` against the previous one.
3. Update whatever depends on the brief (agent KB, report, strategy doc).

---

## Stuck?

- [`docs/methodology.md`](./methodology.md) — full explanation of the "why".
- [`docs/faq.md`](./faq.md) — common blockers.
- Open an issue with template **🐛 Bug report** or **✨ Feature request**.
