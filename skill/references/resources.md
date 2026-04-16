# 10 · Recursos y herramientas (stack 2026)

Catálogo curado de lo que usamos hoy. Se actualiza periódicamente.

---

## Modelos

| Modelo | Fuerte en | Uso recomendado |
|--------|-----------|-----------------|
| **Claude Opus 4.6** (1M tokens) | Razonamiento, código, seguimiento estricto de instrucciones | Agentes complejos, documentos largos |
| **Claude Sonnet 4.6** (200K-1M) | Equilibrio calidad/coste | Volumen en producción |
| **Claude Haiku 4.5** | Velocidad + precio | Clasificación, enriquecimiento, alta frecuencia |
| **GPT-5** / GPT-5.4 | Ecosistema, multimodal, imagen | Consumer, imágenes, Assistants API |
| **Gemini 2.5 Pro** (2M) | Contexto masivo, multimodal pesado | Workspace, vídeo, audio |
| **Grok 4 / Grok DeepSearch** | Información en tiempo real (X), humor | Investigación de actualidad |
| **DeepSeek, Kimi, Qwen** | Open weights competitivos | Self-hosting, privacidad |

---

## Plataformas para construir agentes sin código

| Plataforma | Fortaleza |
|------------|-----------|
| [ChatGPT Custom GPTs](https://chatgpt.com) | Compartir por link + GPT Store |
| [Claude Projects](https://claude.ai) | Contexto enorme + razonamiento |
| [Claude Skills](https://claude.ai) | Reutilización + versionado |
| [Gemini Gems](https://gemini.google.com) | Integración Google Workspace |
| [Poe](https://poe.com) | Multi-modelo en una sola interfaz |

---

## Investigación

| Herramienta | Uso |
|-------------|-----|
| [ChatGPT Deep Research](https://chatgpt.com) | Búsqueda profunda con síntesis larga |
| [Claude + Brave MCP](https://brave.com/search/api/) | Búsqueda estructurada con razonamiento |
| [Gemini Deep Research](https://gemini.google.com) | Investigación académica |
| [Grok DeepSearch](https://grok.com) | Actualidad y redes sociales |
| [Perplexity Pro](https://perplexity.ai) | Citas verificables |
| [Jina Reader](https://r.jina.ai) | URL → Markdown |
| [Firecrawl](https://firecrawl.dev) | Scraping estructurado |

---

## Estructuración de conocimiento

| Herramienta | Uso |
|-------------|-----|
| [Obsidian](https://obsidian.md) | Editor Markdown local con links y grafos |
| [VS Code](https://code.visualstudio.com) + extensiones Markdown | Edición técnica |
| [JSONEditor Online](https://jsoneditoronline.org) | Validar y estructurar JSON |
| [Pandoc](https://pandoc.org) | Conversión entre formatos |
| [Marker](https://github.com/VikParuchuri/marker) | PDF → Markdown de calidad |
| [Docling](https://github.com/docling-project/docling) | PDF/DOCX → Markdown estructurado (IBM) |

---

## Sistemas agénticos (con código)

| Herramienta | Uso |
|-------------|-----|
| [Claude Code](https://claude.ai/code) | CLI oficial Anthropic |
| [OpenCode](https://opencode.ai) | CLI open source multi-modelo |
| [Cursor](https://cursor.sh) | IDE con agentes |
| [Continue.dev](https://continue.dev) | Extensión VS Code |
| [Aider](https://aider.chat) | CLI minimalista |

---

## SDKs y frameworks

| SDK / Framework | Lenguaje | Uso |
|-----------------|----------|-----|
| Anthropic SDK | Python, TS, Go, Java | Agentes custom con Claude |
| OpenAI SDK | Python, TS, múltiples | Agentes custom con GPT |
| Google GenAI SDK | Python, TS, Go | Agentes con Gemini |
| [LangGraph](https://langchain-ai.github.io/langgraph/) | Python, TS | Grafos de estados |
| [CrewAI](https://crewai.com) | Python | Multi-agente por roles |
| [AutoGen](https://microsoft.github.io/autogen/) | Python | Multi-agente conversacional |
| [PydanticAI](https://ai.pydantic.dev) | Python | Structured outputs tipados |

---

## MCP — Servidores destacados

- [Brave Search MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search)
- [Filesystem MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)
- [GitHub MCP](https://github.com/github/github-mcp-server)
- [Notion MCP](https://developers.notion.com/docs/mcp)
- [Linear MCP](https://linear.app/docs/mcp)
- [Slack MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/slack)
- [Cloudflare Developer Platform MCP](https://developers.cloudflare.com/agents/model-context-protocol/)
- Catálogo completo: [github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

---

## Evaluación y observabilidad

| Herramienta | Uso |
|-------------|-----|
| [Langfuse](https://langfuse.com) | Trazas, evals, prompts versionados |
| [Helicone](https://helicone.ai) | Observabilidad LLM |
| [Braintrust](https://braintrustdata.com) | Evals y experimentos |
| [promptfoo](https://promptfoo.dev) | Testing de prompts |

---

## Comunidad y formación

- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [OpenAI Cookbook](https://cookbook.openai.com)
- [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA) — modelos abiertos
- [r/ClaudeAI](https://reddit.com/r/ClaudeAI)
- [Latent Space podcast](https://latent.space) — newsletter técnica
- [AI Engineer](https://ai.engineer) — conferencia

---

## Mantente actualizado

Este campo cambia cada mes. Tres fuentes fiables para estar al día:

- **Blog de Anthropic:** [anthropic.com/news](https://anthropic.com/news)
- **Blog de OpenAI:** [openai.com/blog](https://openai.com/blog)
- **Hacker News** filtrado por tags AI/LLM.

Y la regla práctica: **no migres cada semana**. Cada 3-6 meses reevalúa tu stack y migra solo si el beneficio es claro.
