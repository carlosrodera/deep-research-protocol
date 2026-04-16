# Plantilla · Generador del prompt maestro del agente

Este prompt se ejecuta sobre **Claude Opus 4.6, GPT-5 o Gemini 2.5 Pro** con pensamiento extendido activado. Le das el consolidado de investigación + estructura de tu base de conocimiento + objetivos, y te devuelve el prompt maestro de 11 bloques listo para pegar en la plataforma elegida.

---

## Cómo usar

1. Completa las secciones `## INFORMACIÓN DEL USUARIO`.
2. Adjunta (o pega) el informe consolidado de la Fase 1 y la estructura de archivos de la Fase 2.
3. Ejecuta en tu modelo preferido con *extended thinking*.
4. El modelo te devuelve el prompt maestro. Refínalo manualmente.

---

## Prompt

```text
# CREADOR DE INSTRUCCIONES PARA AGENTES IA ESPECIALIZADOS

Actúa como un experto en ingeniería de prompts con amplia experiencia
creando Custom GPTs, Claude Projects, Claude Skills y Gemini Gems
en contexto profesional.

## INFORMACIÓN DEL USUARIO

### Objetivo del agente
[1-2 frases describiendo qué problema resuelve y para quién]

### Plataforma de destino
[Custom GPT / Claude Project / Claude Skill / Gemini Gem / Múltiple]

### Perfil de usuario principal
[Quién va a usar el agente: rol, conocimiento previo, contexto de uso]

### Territorio / jurisdicción
[Si aplica: España, LATAM, UE, USA, global, etc.]

### Entregable esperado
[Formato típico de respuesta: resumen, informe, análisis, checklist, código, etc.]

### Investigación y base de conocimiento
[Pega aquí el informe consolidado de la Fase 1]
[Pega aquí la estructura de archivos de la Fase 2, con nombres y contenido resumido]

### Restricciones especiales
[Límites éticos, legales, de alcance. Qué NO debe hacer. A quién debe derivar.]

### Comandos especiales deseados (opcional, máximo 4)
[Si tienes ideas previas de comandos /atajo, lístalos aquí]

## INSTRUCCIONES

Basándote en la información anterior, genera un prompt maestro completo
estructurado en los 11 bloques siguientes. Cada bloque debe ser específico,
accionable y adaptado al dominio y plataforma.

### 1. CONTEXTO Y PROPÓSITO
Qué problema resuelve, valor único.

### 2. MISIÓN PRINCIPAL
Una sola frase directa.

### 3. AUDIENCIA OBJETIVO
Perfiles concretos con necesidades y nivel técnico.

### 4. PERSONALIDAD Y TONO
Tono (formal/neutro/cercano), estilo (conciso/detallado/didáctico), rasgos.

### 5. METAS ESTRATÉGICAS
Qué debe perseguir siempre, más allá de "responder".

### 6. PROCESO DE TRABAJO
Pasos concretos para cada consulta, numerados.

### 7. ACCESO A DATOS (OBLIGATORIO)
Cómo y cuándo consultar la base de conocimiento.
Referencia los archivos por nombre exacto.
Incluye la regla "nunca responder de memoria si el tema está cubierto
en la base de conocimiento".

### 8. LIMITACIONES Y RESTRICCIONES
Qué no hace, cuándo derivar a profesional humano, cuándo declarar
incertidumbre.

### 9. COMANDOS ESPECIALES
Hasta 4 comandos funcionales (no decorativos). Para cada uno: nombre,
qué dispara, ejemplo.

### 10. ESTILO DE RESPUESTA
Longitud por defecto, estructura general, adaptación a nivel del usuario.

### 11. FORMATO DE ENTREGA
Markdown con jerarquía, uso de tablas, citas, enlaces.

## REQUISITOS DE SALIDA

- Longitud total del prompt: entre 4.000 y 7.000 caracteres si va a un
  Custom GPT, hasta 10.000 si va a un Claude Project/Skill.
- Cero promesas de funcionalidad irreal (navegar, generar imágenes…)
  si la plataforma elegida no las soporta.
- Instrucciones claras, imperativas, sin relleno.
- Elimina adverbios vacíos ("profesionalmente", "eficazmente").
- Incluye una sección final con "Reglas críticas" en formato `CRÍTICO: ...`
  para las no negociables.

Genera el prompt maestro en un bloque de código Markdown listo para copiar.
```

---

## Tras recibir el prompt

Revisión manual obligatoria:

- [ ] El bloque 7 (Acceso a datos) referencia nombres de archivo reales.
- [ ] Los comandos del bloque 9 realmente hacen algo distinto entre sí.
- [ ] Las limitaciones del bloque 8 son realistas (no sobreprotectoras).
- [ ] El tono del bloque 4 matchea al usuario real.
- [ ] Todas las promesas son cumplibles por el modelo + plataforma.
- [ ] Longitud dentro del límite de la plataforma.

Iteraciones típicas: 2-4 pasadas antes del prompt definitivo.
