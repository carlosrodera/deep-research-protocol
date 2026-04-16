# 09 · Avanzado · MCP y sistemas agénticos

Cuando tu agente necesita **actuar** en el mundo (leer Gmail, consultar una base de datos, ejecutar código, llamar a una API), se te queda corto el Custom GPT o el Project. Aquí entran **MCPs** y **sistemas agénticos**.

---

## Model Context Protocol (MCP)

MCP es un estándar abierto de Anthropic (2024) que define **cómo conectar un LLM a herramientas externas**. Un **servidor MCP** expone funciones; cualquier cliente MCP (Claude Desktop, Claude Code, Cursor, etc.) puede llamarlas.

> Piensa en MCP como "USB-C para agentes IA": conecta una herramienta a cualquier agente compatible.

### Ejemplos de MCPs populares

| MCP | Qué ofrece |
|-----|------------|
| **Brave Search** | Búsqueda web estructurada |
| **Filesystem** | Leer/escribir archivos locales |
| **Git** | Operaciones sobre repos |
| **GitHub** | PRs, issues, workflows |
| **Linear** | Gestión de tickets |
| **Notion** | Lectura/escritura de páginas |
| **Postgres / MySQL / SQLite** | Consultas a BBDD |
| **Slack** | Envío de mensajes, lectura de canales |
| **Gmail / Google Calendar** | Lectura y envío |
| **Puppeteer / Playwright** | Automatización de navegador |
| **Cloudflare Developer Platform** | Workers, D1, KV, R2 |

Catálogo actualizado: [modelcontextprotocol.io](https://modelcontextprotocol.io) y [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers).

### Cómo añadir un MCP a Claude Desktop

Edita `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": { "BRAVE_API_KEY": "tu_api_key" }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/tu/proyectos"]
    }
  }
}
```

Reinicia Claude. Ya puedes decirle "busca con Brave…", "lee el archivo X…", etc.

### Cuándo un MCP vale más que una Action de GPT

- **Privacidad:** MCP corre en tu máquina. No pasa por OpenAI.
- **Potencia:** acceso a tu sistema de archivos, comandos locales, red interna.
- **Versionabilidad:** el servidor MCP es código tuyo.
- **Portabilidad:** la misma herramienta funciona en Claude Desktop, Claude Code, Cursor…

**Contras:** no compartible como un link público. Solo funciona en el equipo/usuario que tiene el MCP instalado.

---

## Claude Code

**Claude Code** es el CLI oficial de Anthropic. Es un agente real: vive en tu terminal, accede al sistema de archivos, ejecuta bash, usa MCPs, puede loopear autónomamente hasta cumplir un objetivo.

### Casos de uso típicos

- Refactorizar código en un repo grande.
- Auditar seguridad de una aplicación.
- Investigar un bug leyendo logs + código.
- Migrar una base de datos.
- Generar y ejecutar scripts de mantenimiento.
- Automatizar workflows repetitivos (escribir informes, procesar archivos).

### Skills dentro de Claude Code

Claude Code soporta Skills igual que Claude.ai. Puedes organizar tus Skills en un repo y Claude las carga cuando toca.

Más info: [claude.ai/code](https://claude.ai/code) · [docs.anthropic.com/en/docs/claude-code](https://docs.anthropic.com/en/docs/claude-code).

---

## OpenCode, Cursor y alternativas

- **[OpenCode](https://opencode.ai/)** — alternativa open source a Claude Code, agnóstico de modelo (soporta Claude, GPT, Gemini, modelos locales).
- **Cursor** — IDE con agentes embebidos. Ideal para desarrollo.
- **Continue.dev** — extensión de VS Code con agentes configurables.
- **Aider** — CLI minimalista para editar código con IA.

Todos soportan MCPs en mayor o menor medida.

---

## Sistemas multi-agente

Para problemas complejos, un solo agente no escala. Patrones habituales:

### 1. Orquestador + especialistas
Un agente "manager" recibe la tarea, la descompone y la reparte entre agentes especializados (investigador, redactor, revisor). Implementable con Claude Agent SDK, LangGraph, CrewAI, AutoGen.

### 2. Pipeline secuencial
`investigación → análisis → redacción → revisión → publicación`. Cada paso es un agente distinto con su prompt maestro.

### 3. Validación cruzada
Dos agentes distintos (ej. Claude + GPT) resuelven el mismo problema. Un tercero compara y consolida.

### 4. Agentes con memoria persistente
Agentes que guardan estado entre ejecuciones en una base de datos o sistema de memoria (archivos, vector store, KV). Útil para asistentes personales o soporte al cliente.

---

## SDK y frameworks

| Framework | Para qué |
|-----------|----------|
| **Anthropic SDK (Python/TS)** | Agentes custom con Claude, tool use, prompt caching |
| **OpenAI SDK + Assistants API** | Agentes custom con GPT, threads, tools |
| **Google GenAI SDK** | Agentes con Gemini |
| **LangGraph** | Grafos de estados para workflows complejos |
| **CrewAI** | Multi-agente con roles y tareas |
| **AutoGen** (Microsoft) | Conversaciones entre agentes |
| **PydanticAI** | Tipado fuerte + structured outputs |

Para empezar: si dominas Python y el caso es claro, usa directamente el SDK de Anthropic u OpenAI. Los frameworks añaden abstracciones útiles solo cuando el sistema crece.

---

## Patrón recomendado para PYMEs

1. **Empieza con Custom GPT o Claude Project.** Valida caso de uso con usuarios reales.
2. **Migra a Claude Code + MCPs** cuando necesites acciones en sistemas internos.
3. **Salta a SDK custom** solo cuando:
   - Lo vas a embeber en un producto propio.
   - Necesitas control fino de latencia o coste.
   - Vas a orquestar varios agentes.

No saltes al SDK por moda. Un GPT bien hecho resuelve el 80% de los casos.

---

## Recursos

- **MCP:** [modelcontextprotocol.io](https://modelcontextprotocol.io)
- **Claude Code:** [docs.anthropic.com/en/docs/claude-code](https://docs.anthropic.com/en/docs/claude-code)
- **Anthropic cookbook:** [github.com/anthropics/anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook)
- **OpenAI cookbook:** [cookbook.openai.com](https://cookbook.openai.com)
- **Awesome MCP:** [github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

---

👉 Siguiente: [10 · Recursos y herramientas](10-recursos.md)
