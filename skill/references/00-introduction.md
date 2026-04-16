# 00 · Introducción

## Por qué este repositorio

Durante 2023 y 2024 se popularizó el concepto de **"Custom GPTs"**: pequeños agentes dentro de ChatGPT con instrucciones propias y una base de conocimiento. Funcionaron bien, pero tenían limitaciones: contexto reducido, RAG impreciso en documentos largos, difícil compartir, no reutilizables entre conversaciones.

En 2026 el panorama ha cambiado. Tenemos **cuatro formatos principales** para construir un agente especializado:

1. **Custom GPTs (OpenAI)** — sigue vigente, sigue siendo la forma más sencilla de compartir un agente mediante link público o GPT Store.
2. **Claude Projects (Anthropic)** — espacio de trabajo con 200K tokens de contexto, ideal para bases de conocimiento densas.
3. **Claude Skills (Anthropic)** — archivos `.md` portables que añaden capacidades reutilizables a cualquier conversación o proyecto.
4. **Gemini Gems (Google)** — agentes personalizados con integración nativa en Workspace (Gmail, Docs, Drive, Calendar).

Y por encima de todos, los **sistemas agénticos** reales (Claude Code, OpenCode, Cursor, SDK de Claude o OpenAI, Model Context Protocol) que permiten orquestar loops autónomos, herramientas externas y múltiples agentes coordinados.

Este repo te enseña el **método**. El método sirve igual para un Custom GPT que para una Skill de Claude: la parte valiosa es la **investigación + estructuración del conocimiento + prompt maestro**, no la configuración de la UI.

---

## Para quién es esta guía

- **Emprendedores y consultores** que quieren aplicar IA a un dominio concreto (legal, salud, finanzas, marketing, soporte…).
- **Equipos internos** que quieren construir asistentes verticales para procesos específicos de la empresa.
- **Profesionales** que quieren automatizar tareas repetitivas y conservar conocimiento organizacional.
- **Formadores y creadores** que quieren empaquetar su expertise en un agente compartible.

No hace falta saber programar. Sí hace falta **saber de tu dominio**.

---

## La regla de oro (léela dos veces)

> Si tú no sabes hacer la tarea manualmente, tu agente no la va a hacer bien.

Este es el mayor malentendido sobre la IA aplicada. La gente cree que el modelo "sabrá" porque "es muy listo". No. El modelo sabe lenguaje y patrones. El **dominio concreto** (leyes de tu país, normativa de tu sector, procesos de tu empresa) lo pones tú.

Si no sabes cuáles son los pasos correctos de un proceso, no puedes escribir instrucciones que lleven al agente a ejecutarlos bien. Y no puedes evaluar si la salida es correcta.

**Primero aprende tú. Luego enseña al agente.**

---

## Qué NO vas a encontrar aquí

- Hype. Promesas mágicas. "La IA lo hace todo solo".
- Prompts genéricos de 50 palabras que prometen "revolucionar tu negocio".
- Trucos que duran 3 meses hasta que cambia el modelo.

## Qué SÍ vas a encontrar

- Un método de 5 fases probado en consultoría real.
- Plantillas reutilizables de prompts de investigación, prompt maestro y esqueletos de instrucciones.
- Criterios honestos sobre cuándo usar cada plataforma.
- Ejemplos trabajados de principio a fin.
- Criterios de evaluación y mantenimiento.

---

## Siguiente paso

👉 [01 · Fundamentos](01-fundamentos.md) — qué es realmente un agente IA y cómo piensa por dentro.
