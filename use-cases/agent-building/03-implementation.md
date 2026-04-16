# 06 · Fase 4 · Implementación por plataforma

Tienes la investigación, la base de conocimiento y el prompt maestro. Ahora toca **montar el agente** en la plataforma elegida.

---

## 6.1 Custom GPT (OpenAI)

### Pasos

1. Ve a [chatgpt.com](https://chatgpt.com) y abre **"Explore GPTs" → "Create"**.
2. Pestaña **"Configure"** (ignora el chat asistente, es más rápido rellenar manual).
3. **Name** — nombre descriptivo, sin emojis innecesarios.
4. **Description** — una frase que diga qué hace y para quién.
5. **Instructions** — pega tu prompt maestro (los 11 bloques).
6. **Conversation starters** — pon los 4 comandos especiales como prompts de ejemplo.
7. **Knowledge** — sube los archivos `.md` y `00-index.json`.
8. **Capabilities** — activa solo las que uses: Web Browsing, DALL·E, Code Interpreter.
9. **Actions** — opcional. Si necesitas llamar a APIs externas, aquí se configura con OpenAPI schema.

### Recomendaciones específicas

- No subas PDFs grandes. Convierte todo a `.md`.
- El `00-index.json` es clave: en las instrucciones, referencia archivos **por nombre exacto**.
- Para probar: pide al GPT que te diga **qué archivos tiene disponibles**. Si no los ve, revisa nombres.
- Publicación: elige *"Only me"* para pruebas, luego *"Anyone with link"* o *"Everyone"*.

---

## 6.2 Claude Project

### Pasos

1. En [claude.ai](https://claude.ai) → **Projects** → **Create Project**.
2. **Name + description.**
3. **Custom instructions** — pega el prompt maestro.
4. **Project knowledge** — arrastra o pega:
   - Archivos `.md` de tu base de conocimiento.
   - `00-index.json`.
   - Cualquier referencia adicional (máx ~90% del límite del proyecto; Claude te avisa).
5. Abre una nueva conversación dentro del proyecto. Todas heredan contexto e instrucciones.

### Recomendaciones específicas

- **Contexto enorme:** puedes subir bases de conocimiento mucho mayores que en un GPT (hasta decenas de miles de palabras efectivas).
- Claude suele **respetar mejor las instrucciones complejas**. Aprovéchalo: procesos de 10 pasos funcionan bien.
- Para bases >200K tokens: usa el modelo Opus 4.6 con 1M tokens.
- Compartir: limitado a tu organización. No hay GPT Store.

---

## 6.3 Claude Skill

### Pasos

1. Crea un archivo `.md` con cabecera YAML:

```markdown
---
name: analista-compliance-seguridad
description: Analista experto en Ley 5/2014 y ISO de seguridad privada en España. Úsalo cuando se consulte normativa, cumplimiento o auditoría del sector.
---

# Instrucciones

[... tu prompt maestro aquí ...]
```

2. En Claude.ai (o Claude Code), ve a **Settings → Skills → Add Skill** y sube el `.md`.
3. La skill se activará automáticamente cuando Claude detecte una consulta que encaje con su `description`, o puedes invocarla explícitamente con `/skill nombre`.

### Recomendaciones específicas

- **La `description` es crítica**: define cuándo Claude cargará la skill. Sé específico con los triggers (temas, palabras clave, contextos).
- Las skills **no llevan base de conocimiento adjunta**. Si la necesitas, combínala con un Project que contenga los documentos.
- Ideal para **procesos reutilizables**: revisión editorial, checklist de seguridad, framework de análisis.
- Versiona en git. Compártelas como archivos.

Plantilla: [`templates/skill-claude.md`](../templates/skill-claude.md).

---

## 6.4 Gemini Gem

### Pasos

1. Ve a [gemini.google.com](https://gemini.google.com) → **Gems** → **New Gem**.
2. **Name + description.**
3. **Instructions** — pega el prompt maestro.
4. **Knowledge** — puedes adjuntar archivos desde Google Drive o subir directamente.
5. Activa extensiones de Workspace (Gmail, Docs, Drive) si el agente debe interactuar con ellos.
6. Guarda y prueba.

### Recomendaciones específicas

- **Fuerza de Gemini:** integración Workspace. Un Gem puede leer tus emails o documentos directamente. Aprovéchalo.
- Contexto enorme (hasta 2M tokens) → útil para codebases o libros enteros.
- Multimodal pesado (vídeo, audio, imagen) mejor que la competencia.

---

## 6.5 Orden de tareas dentro de la implementación

Independientemente de la plataforma:

1. Crea el agente con **prompt maestro y ningún archivo**. Prueba una consulta genérica para ver el tono.
2. Añade **el archivo de índice** (`00-index.json` o `00-index.md`). Prueba: "¿qué documentos tienes disponibles?".
3. Añade **los archivos de la base de conocimiento**. Prueba: "Según `normativa/ley_5_2014.md`, ¿qué dice el artículo 10?".
4. Configura **comandos / starters**. Pruébalos uno a uno.
5. Prueba **5 preguntas reales de usuarios reales** (o simuladas). Ajusta.

---

## 6.6 Checklist de implementación

- [ ] Prompt maestro pegado y por debajo del límite de caracteres.
- [ ] Archivos de base de conocimiento subidos en `.md`/`.json` (no PDF).
- [ ] Nombres de archivo coinciden con los referenciados en el prompt.
- [ ] Índice (`00-index.*`) subido y referenciado.
- [ ] Comandos especiales configurados.
- [ ] Capacidades técnicas (web, código, imagen) activadas o desactivadas según necesidad.
- [ ] Descripción y nombre claros para el usuario final.
- [ ] Privacidad / visibilidad configurada (Solo yo / Con link / Público / Org).

---

👉 Siguiente: [07 · Fase 5 · Pruebas y optimización](07-fase5-pruebas.md)
