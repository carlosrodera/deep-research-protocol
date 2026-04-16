# 02 · Plataformas — qué elegir en 2026

Hay cuatro formatos "sin código" principales y dos formatos "con código". Este capítulo te ayuda a elegir el adecuado **antes** de construir.

---

## Los cuatro formatos sin código

### 1. Custom GPTs (OpenAI)
**Qué es:** versión personalizada de ChatGPT con instrucciones propias, archivos de conocimiento y opcionalmente *Actions* (llamadas a APIs externas), Code Interpreter y generación de imágenes con DALL·E.

**Fortalezas:**
- **Máxima facilidad de compartir**: link público, GPT Store, embebible.
- Ecosistema gigantesco y muchas integraciones enterprise.
- Puede **ejecutar código Python**, **navegar web**, **generar imágenes**.
- Límite histórico de instrucciones de ~8.000 caracteres (hoy algo más amplio, pero sigue siendo compacto — obliga a ser conciso).

**Debilidades:**
- RAG sobre ficheros adjuntos **hit-or-miss** en documentos largos (>50 páginas). Mejor si divides.
- No mantiene memoria entre conversaciones del mismo GPT por defecto.
- Requiere plan de pago para crearlos y publicarlos.

**Úsalo cuando:** quieras distribuir un agente a muchos usuarios mediante un link, necesites imágenes o code interpreter, o ya estés en el ecosistema ChatGPT.

---

### 2. Claude Projects (Anthropic)
**Qué es:** espacio de trabajo dentro de Claude.ai donde defines instrucciones y subes archivos. Todas las conversaciones dentro del proyecto heredan contexto e instrucciones.

**Fortalezas:**
- **Ventana de contexto enorme** (200K tokens en Sonnet, 1M en Opus 4.6). Claude **lee los documentos enteros**, no usa RAG lossy.
- Calidad de razonamiento superior en tareas complejas y seguimiento estricto de instrucciones.
- Excelente para legal, análisis de documentos largos, redacción técnica.

**Debilidades:**
- No se puede compartir públicamente como un GPT (solo dentro de tu org/plan).
- Sin code interpreter integrado (hay *analysis tool* pero menos potente que ChatGPT).
- Menos integraciones plug-and-play que OpenAI.

**Úsalo cuando:** la base de conocimiento sea grande, precisión y razonamiento sean críticos, o sea uso interno para tu equipo.

---

### 3. Claude Skills (Anthropic)
**Qué es:** archivo `.md` con instrucciones reutilizables que Claude puede cargar en cualquier conversación o proyecto. Es la evolución del "prompt templado": en vez de pegar el mismo prompt una y otra vez, lo guardas como skill y Claude lo aplica cuando corresponde.

**Fortalezas:**
- **Portable** entre proyectos y conversaciones.
- Son simples archivos de texto → versionables en git, compartibles por email.
- Perfectas para frameworks analíticos, estilos de escritura, procesos que usas repetidamente.

**Debilidades:**
- Compartir no es un link — hay que enviar el archivo y el destinatario subirlo.
- No llevan base de conocimiento adjunta (las añades al proyecto donde uses la skill).

**Úsalo cuando:** tengas un proceso o estilo que quieras aplicar en contextos variados (no solo un dominio), o quieras versionar instrucciones con git.

Plantilla: [`templates/skill-claude.md`](../templates/skill-claude.md).

---

### 4. Gemini Gems (Google)
**Qué es:** agentes personalizados dentro del ecosistema Gemini con acceso nativo a Google Workspace.

**Fortalezas:**
- **Integración profunda con Gmail, Docs, Drive, Calendar, Sheets**.
- Ventana de contexto masiva (hasta 2M tokens en Gemini 2.5 Pro).
- Bueno para multimodal (vídeo, audio, imagen).

**Debilidades:**
- Menos comunidad y plantillas públicas.
- Compartir restringido al ecosistema Google.

**Úsalo cuando:** tu flujo de trabajo gire en torno a Google Workspace o necesites multimodal pesado.

---

## Los formatos "con código" (avanzado)

### 5. Claude Code / OpenCode / Cursor Agents
Agentes que viven en tu terminal o IDE, con acceso al sistema de archivos, bash, git, web, y **cualquier MCP**. Son los más potentes porque pueden **ejecutar acciones reales** en tu máquina o servidor.

Cubiertos en [docs/09-avanzado-mcp.md](09-avanzado-mcp.md).

### 6. SDKs (Anthropic / OpenAI / Google)
Cuando necesitas un agente embebido en tu producto, con lógica propia, herramientas custom y ejecución automatizada. Sales del chat y entras en código.

---

## Tabla de decisión rápida

| Criterio | Custom GPT | Claude Project | Claude Skill | Gemini Gem |
|----------|-----------|----------------|--------------|------------|
| Compartir por link público | ✅ | ❌ | ❌ | ⚠️ (limitado) |
| Base de conocimiento larga (>100 págs) | ⚠️ | ✅✅ | ➖ (no lleva) | ✅ |
| Reutilización entre conversaciones | ❌ | ✅ | ✅✅ | ✅ |
| Ejecución de código / navegación | ✅ | ⚠️ | ❌ | ✅ |
| Generación de imágenes | ✅ (DALL·E) | ❌ | ❌ | ✅ (Imagen) |
| Workspace Google integrado | ❌ | ❌ | ❌ | ✅✅ |
| Razonamiento complejo / legal | ⚠️ | ✅✅ | ✅ | ✅ |
| Versionable en git | ⚠️ | ⚠️ | ✅✅ | ❌ |
| Facilidad para no técnicos | ✅✅ | ✅ | ⚠️ | ✅ |

---

## Patrones híbridos (lo que hacemos en consultoría real)

No elijas solo uno. En proyectos reales combinamos:

- **Claude Project** para el trabajo pesado interno con base de conocimiento grande.
- **Custom GPT** como "versión pública" del mismo agente para clientes o usuarios finales.
- **Claude Skills** para los sub-procesos reutilizables (estilo de redacción, checklist de revisión).
- **Claude Code + MCPs** cuando hay que automatizar de verdad (scraping, integración con BD, envío de emails).

---

## Decisión por caso de uso

- **Asistente de atención al cliente público** → Custom GPT.
- **Analista legal interno con 2.000 páginas de normativa** → Claude Project.
- **Revisor de artículos con tu estilo editorial** → Claude Skill.
- **Asistente que lee tu bandeja de Gmail y propone respuestas** → Gemini Gem o Claude Code + MCP Gmail.
- **Automatizar generación de informes desde Notion/Linear** → Claude Code con MCPs o SDK.

---

👉 Siguiente: [03 · Fase 1 · Investigación profunda](03-fase1-investigacion.md)
