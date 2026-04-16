# 01 · Fundamentos

## Qué es (y qué no es) un agente IA

Un **agente IA especializado** es, en esencia, un LLM (Claude, GPT, Gemini…) al que le hemos dado tres cosas:

1. **Instrucciones** — un prompt de sistema que define su rol, objetivos, límites y estilo.
2. **Base de conocimiento** — documentos o datos a los que puede consultar.
3. **Herramientas** (opcional) — capacidad de ejecutar acciones: búsqueda web, código, APIs, bases de datos.

Un Custom GPT y un Claude Project son versiones de esto que viven dentro de una interfaz de chat. Un sistema agéntico real (Claude Code, OpenCode, un agente con el SDK de Anthropic) añade **loops autónomos**: el modelo decide qué herramienta llamar, ejecuta, evalúa el resultado y continúa hasta cumplir el objetivo.

> **Definición práctica:** un agente es un LLM + contexto + herramientas + criterio de parada.

---

## Cómo "piensa" un LLM (modelo mental mínimo)

Para construir buenos agentes hay que entender cuatro propiedades clave de los LLMs actuales:

### 1. Ventana de contexto = memoria de trabajo
El modelo solo "ve" lo que está dentro de su ventana de contexto en ese momento. Claude Opus 4.6 maneja 1M tokens, Sonnet 4.6 maneja 200K–1M, GPT-5 también en ese rango, Gemini 2.5 hasta 2M. Todo lo que esté fuera del contexto **no existe** para el modelo.

**Consecuencia:** si subes un PDF de 500 páginas a un agente, no lo lee entero cada vez. Busca fragmentos relevantes (RAG) y te devuelve algo que puede ser incorrecto o incompleto si la indexación es mala.

### 2. Los LLMs completan texto, no entienden verdad
Un LLM predice el siguiente token más probable. Eso significa que puede **alucinar** con seguridad absoluta. Nuestra responsabilidad como diseñadores de agentes es:
- Darle fuentes de verdad (base de conocimiento).
- Decirle explícitamente cuándo tiene que consultarlas ("antes de responder sobre X, lee el archivo Y").
- Pedirle que cite o que diga "no lo sé" cuando no haya información.

### 3. Las instrucciones las lee en orden y da prioridad al comienzo y al final
Las primeras y últimas líneas del prompt de sistema pesan más. Por eso el **rol** va al principio y las **reglas críticas** al final.

### 4. El modelo hará lo que le pidas… si se lo pides claro
Las instrucciones vagas producen salidas vagas. "Analiza esto" es peor que "identifica los tres riesgos legales más importantes y cita el artículo de la ley que los respalda".

---

## Agente vs Chatbot vs Asistente vs Automatización

| Término | Qué es | Ejemplo |
|---------|--------|---------|
| Chatbot | Responde preguntas en un dominio acotado | Bot de FAQ de una web |
| Asistente | Chatbot + contexto de usuario + algunas herramientas | ChatGPT, Claude.ai |
| Custom GPT / Project / Skill / Gem | Asistente con instrucciones y conocimiento especializado | GPT "Experto en Ley de Seguridad Privada" |
| Agente | Asistente + loop autónomo + herramientas + criterio de parada | Claude Code, un sistema que lee tu bandeja de entrada y responde emails |
| Sistema agéntico multi-agente | Varios agentes coordinados por un orquestador | Pipeline de investigación → redacción → revisión |

Este repo cubre principalmente **los tres del medio** (Custom GPT, Claude Project/Skill, Gem) y da una puerta de entrada a los dos últimos.

---

## El ciclo de creación: las 5 fases

```
┌────────────────────────────────────────────────────────────────┐
│  FASE 1: INVESTIGACIÓN PROFUNDA (multi-plataforma)             │
│  Entender el dominio, identificar fuentes, leyes, procesos.    │
└────────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────────┐
│  FASE 2: BASE DE CONOCIMIENTO                                  │
│  Estructurar en Markdown/JSON, dividir, indexar.               │
└────────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────────┐
│  FASE 3: PROMPT MAESTRO                                        │
│  Los 11 bloques: rol, misión, audiencia, personalidad,         │
│  proceso, acceso a datos, límites, comandos, formato.          │
└────────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────────┐
│  FASE 4: IMPLEMENTACIÓN (plataforma elegida)                   │
│  Custom GPT / Claude Project / Skill / Gem.                    │
└────────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────────┐
│  FASE 5: PRUEBAS, ITERACIÓN Y MANTENIMIENTO                    │
│  Evaluación, ajuste, actualización de la base de conocimiento. │
└────────────────────────────────────────────────────────────────┘
```

El 70% del tiempo total está en las **fases 1 y 2**. Si las haces bien, el resto es casi mecánico.

---

## Límites reales (para ajustar expectativas)

- **Conocimiento desfasado.** Los modelos tienen un corte de entrenamiento. Si tu dominio cambia rápido (leyes, fiscalidad, productos), la base de conocimiento **debe mantenerse**.
- **Consistencia.** Dos ejecuciones con la misma pregunta pueden dar respuestas distintas. Usa `temperature` baja donde puedas y pide estructura explícita.
- **Privacidad.** No subas datos sensibles de clientes a servicios públicos sin entender la política de retención.
- **Costes.** Los modelos top (Opus 4.6, GPT-5) son ~10× más caros que los rápidos (Haiku 4.5, GPT-5 Mini). En producción a menudo interesa el rápido + un fallback al top para casos difíciles.

---

👉 Siguiente: [02 · Plataformas](02-plataformas.md)
