# Integrations

Export a verified DRP brief to the tools you actually work in. None of these are required — the Markdown brief at `workspace/research/consolidated.md` is already usable. These are concrete recipes if you want the output to live somewhere else.

Ordered roughly by adoption frequency.

---

## 1 · Claude Project (as a KB)

**Why:** Claude Projects support up to 1M tokens of KB with precise retrieval and a persistent system prompt.

1. Create a new Project on Claude.ai.
2. Upload `workspace/research/consolidated.md` and every file in `workspace/research/primary-sources/`.
3. Project instructions (paste):

   ```
   You are a specialist in <domain>. Every answer MUST cite a filename
   from the project knowledge base. If no file supports a claim, say
   "not in the knowledge base" — never answer from parametric memory.
   Confidence scores from the source brief must be preserved in your
   answers.
   ```

4. Test with 5 realistic queries. Iterate on the instructions.

See [`use-cases/agent-building/`](../use-cases/agent-building/) for the full method.

---

## 2 · Custom GPT (as a KB)

**Why:** public distribution via GPT Store link.

1. Open GPT Builder → Configure.
2. Upload the consolidated brief + primary sources (max 20 files; split the brief if needed — DRP suggests a per-subtopic split with `00-index.md`).
3. Instructions (paste):

   ```
   You are a specialist on <domain>. Before answering, consult the
   named files in your knowledge. Cite the filename and the specific
   section. Preserve confidence scores verbatim. If the knowledge
   base does not cover a question, say so — do not answer from
   training data.
   ```

4. Disable web-browsing if your KB is the canonical source. Otherwise, the GPT will override with parametric memory.

---

## 3 · Notion page

**Why:** team-readable, commentable, diffable via page history.

1. Create a new Notion page.
2. Paste `consolidated.md` — Notion parses Markdown structure.
3. Convert the **Confidence ledger** table to a Notion database with columns: Finding, Confidence, Consensus, Top-tier source. Sort by Confidence.
4. Convert the **Primary-source download list** to a linked-database with Status (Downloaded / Pending / Skipped).
5. Lock the page or move to a read-only section after publish.

---

## 4 · Obsidian vault

**Why:** local-first, long-lived personal knowledge graph, trivially diffable in git.

Suggested folder structure:

```
drp-briefs/
├── <YYYY-MM-DD>-<topic-slug>/
│   ├── brief.md                 ← the consolidated brief
│   ├── _meta.yaml               ← extracted from the brief for portfolio diffing
│   ├── primary-sources/         ← downloaded pdfs / html
│   └── raw/                     ← the 5 parallel reports
└── _portfolio.md                ← dashboard linking to all briefs
```

Tag every brief with `#drp/<domain>` and `#drp/confidence/<high|medium|low>`. Obsidian's graph view now shows your brief portfolio and which domains depend on which primary sources.

---

## 5 · RAG index (Chroma / LlamaIndex / Pinecone)

**Why:** programmatic querying by downstream agents.

Minimum script (adapt to your vector DB):

```python
# pseudo-code — install your RAG stack of choice
from pathlib import Path
import your_vector_db as vdb

brief = Path("workspace/research/consolidated.md").read_text()

# split by heading for chunking (DRP briefs are already structured)
sections = split_by_h2(brief)

for section in sections:
    vdb.upsert(
        id=section.id,
        text=section.text,
        metadata={
            "protocol": "drp",
            "version": "1.0",
            "domain": section.domain,
            "confidence": section.confidence,  # parsed from confidence ledger
            "tier": section.top_source_tier,
        },
    )
```

Also index each file under `primary-sources/` with the same metadata schema. Downstream retrieval can filter by `confidence >= 0.8` or `tier <= 3`.

---

## 6 · Anki deck (for internal training)

**Why:** turn a one-off brief into persistent team knowledge via spaced repetition.

Simple pipeline:

1. Parse the **Confidence ledger** table.
2. For every finding with confidence ≥ 0.8, create a card:
   - **Front:** the question (invert the finding into question form).
   - **Back:** the finding + top source URL + confidence score.
3. Export to Anki via `genanki` or a manual `.csv` import.

Weekly review keeps the team's mental model synced with the most recent DRP pass.

---

## 7 · Google Docs (for non-technical stakeholders)

**Why:** board, exec, legal teams live here.

1. Import `consolidated.md` via Markdown-to-Docs extension or paste into a new doc and let Docs auto-format headings.
2. Delete the `_meta` YAML block (non-technical readers don't need it; keep it in a footnote for auditability).
3. Convert the confidence table to a native Docs table with **conditional formatting** on Confidence column (red < 0.5, yellow 0.5–0.7, green ≥ 0.7).
4. Lock suggesting-mode off. Briefs are artifacts, not drafts.

---

## 8 · Linear / Jira (as a research ticket)

**Why:** operational handoff to engineering / product.

Link the Markdown brief in the ticket body. Expose the `_meta` block as custom fields (Confidence avg, Findings count, Gaps count). Now product can filter the backlog by "research-backed features with confidence ≥ 0.75".

---

## 9 · Confluence (enterprise wiki)

**Why:** the "default" place enterprise wants documents to live.

Use the Markdown-import macro. Translate the confidence ledger to a Confluence table with **status macros** (green/yellow/red) on the Confidence column. Pin the page in the relevant space.

---

## 10 · MCP tool (coming in v1.2)

**Why:** callable from Claude Code, Cursor, or any MCP-compatible client.

Planned: a `drp-mcp` server that exposes:

- `drp.launch(query, engines, domain, territory)` — stage the mega-prompt + track reports.
- `drp.consolidate(report_paths)` — run consolidation.
- `drp.verify_citations(brief_path)` — call `verify-citations.py`.
- `drp.brief_meta(brief_path)` — parse and return the `_meta` block.

Track progress in [`../CHANGELOG.md`](../CHANGELOG.md) and the roadmap.

---

## Writing your own integration

If you build an integration not listed here, submit a PR adding a section above. Every section must:

1. State **why** someone would want this integration (what problem it solves).
2. Include a **minimum viable recipe** (commands or steps that just work).
3. Note any **gotchas** specific to that tool.

Governance in [`../CONTRIBUTING.md`](../CONTRIBUTING.md).
