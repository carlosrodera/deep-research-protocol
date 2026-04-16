# Related work

Where DRP sits in the deep-research ecosystem, who it competes with, who it complements, and the academic literature it builds on.

---

## 1 · DRP's positioning in one sentence

> DRP is a **human-operated meta-protocol** that orchestrates existing Deep Research agents (ChatGPT DR, Claude DR, Gemini DR, Grok DeepSearch, Perplexity Pro) in parallel and consolidates by consensus. It does not compete with those agents; it uses all of them.

Everyone else builds **another** Deep Research agent. DRP doesn't.

---

## 2 · Comparison matrix — DRP vs. open-source DR agents

| Feature | [LangChain `open_deep_research`](https://github.com/langchain-ai/open_deep_research) | [TIGER `OpenResearcher`](https://github.com/TIGER-AI-Lab/OpenResearcher) | [btahir `open-deep-research`](https://github.com/btahir/open-deep-research) | [nickscamara `open-deep-research`](https://github.com/nickscamara/open-deep-research) | [assafelovic `gptr-mcp`](https://github.com/assafelovic/gptr-mcp) | [langgptai `awesome-deep-research-prompts`](https://github.com/langgptai/awesome-deep-research-prompts) | **DRP (this repo)** |
|---|---|---|---|---|---|---|---|
| Type | DR agent | DR model + agent | DR agent with UI | DR agent | DR over MCP | Prompt collection | **Meta-protocol** |
| Competes with ChatGPT DR? | Yes | Yes | Yes | Yes | Yes | No | **No — uses it** |
| Uses multiple engines in parallel? | ❌ (one-at-a-time provider switch) | ❌ (single model) | ❌ (one-at-a-time) | ❌ | ❌ | ❌ | ✅ **4–5 in parallel** |
| Cross-platform consensus? | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Explicit evidence hierarchy? | ❌ | ❌ | ❌ | ❌ | ❌ | partial | ✅ |
| Hard source quotas (academic/regulatory/industry/counter-example)? | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Confidence scores 0.0–1.0 per finding? | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Anti-echo-chamber prompt variant? | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Machine-readable `_meta` output schema? | ❌ | ❌ | ❌ | ❌ | partial (MCP tool) | ❌ | ✅ |
| Citation-verifier script? | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Install cost | Python + API keys + LangChain | GPU + model | Python + Node + API keys | Python + Firecrawl | Node + MCP host | ∅ | **∅ (paste prompt)** |
| Multilingual? | English-first | English-only | English-first | English-only | English-only | English-first | **EN + ES canonical, open to community localizations** |
| Use-case library | Generic research | Generic | Generic research | Generic | Generic | Generic | **Agent · market report · strategic brief · compliance audit** |
| Dependencies | Heavy (LangGraph, providers) | Heavy (model weights) | Medium (Node, Python) | Medium | Medium | None | **None (stdlib Python for scripts)** |

**Key takeaway:** every row flipping from ❌ to ✅ between the agents and DRP is a feature the user can have *by running DRP on top of whatever agent they already use*, without abandoning their stack.

## 3 · What we explicitly borrow from

DRP is not built in a vacuum. Acknowledged influences:

- **`deep_search_gpt v2.1`** (Carlos Rodera, 2024–2026) — private prompt inside the *GPTs de Emprendedores* community. Source of the scope-builder, strategic-questions, source-quota and confidence-score mechanics.
- **Anthropic's multi-agent deep research architecture** — a lead agent orchestrates parallel sub-agents. DRP's insight: you already have the "sub-agents" — they're called ChatGPT, Claude, Gemini, etc. Run them human-in-the-loop.
- **LangChain `open_deep_research`** — showed that DR workflows are configurable and open-source-viable. DRP stays at a higher abstraction layer.
- **Academic framework on DR evaluation** — three-dimensional evaluation (recall, analysis, presentation) maps onto DRP's quality gates.

## 4 · Academic references

1. [*A Comprehensive Survey of Deep Research: Systems, Methodologies, and Applications*](https://arxiv.org/pdf/2506.12594) — arXiv **2506.12594**, 2026.
   DRP uses this as the canonical source for the citation-hallucination problem statement and the recall/analysis/presentation evaluation axes.
2. [*DeepResearch Bench II: Diagnosing Deep Research Agents*](https://arxiv.org/pdf/2601.08536) — arXiv **2601.08536**, 2026.
   Benchmark targeted by DRP's planned evaluation harness ([`docs/benchmarking.md`](./benchmarking.md)).
3. [*DeepResearchEval: An Automated Framework for Deep Research Task Construction and Agentic Evaluation*](https://arxiv.org/html/2601.09688v1) — arXiv **2601.09688**, 2026.
   Source of the persona-driven, multi-source-evidence task construction method. Will inform DRP's future use-case library.
4. [*Viewpoint: Deep Research Agents — Major Breakthrough or Incremental?*](https://www.jmir.org/2026/1/e88195/PDF) — JMIR, 2026.
   Critical-source read on the DR agent category. DRP takes seriously the "incremental" critique and positions as orthogonal (meta-protocol).
5. [*Towards Knowledgeable Deep Research: Framework and Benchmark*](https://arxiv.org/html/2604.07720) — arXiv **2604.07720**, 2026.
   Framework for structured evaluation dimensions; aligns with DRP Step I quality gates.
6. [*An Open Ended Deep Research Model via Multi-Agent*](https://arxiv.org/pdf/2601.03743) — arXiv **2601.03743**, 2026.
   Context for the multi-agent-orchestration trend.

## 5 · What DRP deliberately does not try to do

Honest scope limits:

- **No autonomous mode.** DRP stays human-in-the-loop. An MCP server is on the roadmap but a fully autonomous DRP runner is out of scope — the cross-platform paste step is what keeps the engines honest.
- **No new DR agent.** We do not host, fine-tune, or retrain anything. We use what exists.
- **No UI.** We ship Markdown. A lightweight UI ("DRP Studio") is on the v2.0 roadmap but is optional.
- **No proprietary retrieval stack.** We do not replace vector DBs, Firecrawl, SearXNG, etc. We assume you (or the DR engine) already have retrieval.

## 6 · Complementary projects to chain with DRP

After producing a DRP brief, these projects are natural downstream consumers:

- **[LangChain `open_deep_research`](https://github.com/langchain-ai/open_deep_research)** — use your DRP brief as a grounding document for agentic extensions.
- **[LlamaIndex](https://github.com/run-llama/llama_index)** / **[Chroma](https://github.com/chroma-core/chroma)** — index the primary sources from your DRP brief into RAG.
- **[Obsidian](https://obsidian.md)** / **[LogSeq](https://logseq.com)** — personal knowledge graph of verified briefs over time. See [`integrations.md`](./integrations.md).
- **[Anki](https://apps.ankiweb.net/)** — turn consolidated findings into spaced-repetition decks for internal training.
- **[Claude Projects](https://claude.ai)** / **[Custom GPTs](https://chat.openai.com/gpts)** — upload the brief + primary sources as KB.

## 7 · How to decide

| If you want to… | Use |
|---|---|
| Run one deep research query fast with minimal setup | ChatGPT DR / Claude DR / Gemini DR / Perplexity Pro |
| Build your own DR agent with custom retrieval | LangChain `open_deep_research` / TIGER `OpenResearcher` |
| Run DR as a tool callable from an agent | `gptr-mcp` (MCP) |
| Collect good single-platform prompts | `awesome-deep-research-prompts` |
| **Run DR across all of the above in parallel and consolidate** | **DRP** |
| Ship a source-verified deliverable for enterprise | **DRP** |
| Build a specialized AI agent with a verified KB | **DRP + `use-cases/agent-building/`** |

## 8 · Honest limitations of DRP's positioning

- If you have 1 engine available, DRP degrades to a rigorous single-engine prompt. Still better than an unstructured prompt — but most of the value is in cross-engine consolidation.
- If a topic is extremely new (≤ 2 weeks old), all 5 engines may share the same thin pool of sources. Cross-validation degrades.
- If a topic has very strong vendor capture (one company dominates the information ecosystem), even 5 engines may all echo the same party line. This is where the **anti-echo prompt** and the **counter-example source quota** earn their keep.

Be honest with your audience about when DRP's marginal value is high vs. low.
