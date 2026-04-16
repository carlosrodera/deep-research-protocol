# 04 · Fase 2 · Base de conocimiento

El conocimiento recogido en la Fase 1 tiene que transformarse en **archivos que el agente pueda consultar eficientemente**. Esta fase decide si tu agente responderá con precisión quirúrgica o con improvisaciones vagas.

---

## Principios

1. **Markdown y JSON son tus amigos. PDF es tu enemigo.**
   Los modelos procesan texto plano estructurado mejor que PDFs con layout complejo. Convierte siempre.
2. **Divide en archivos temáticos, no uno gigante.**
   Un archivo de 500 páginas obliga al modelo a hacer RAG lossy. Varios archivos de 20-50 páginas con nombres claros permiten al agente **saber exactamente dónde buscar**.
3. **Indexa lo grande.**
   Para cualquier documento >50 páginas, crea un **índice vectorial** en JSON con palabras clave → secciones/páginas.
4. **Nombres de archivo descriptivos.**
   `ley_5_2014_seguridad_privada.md` sí; `documento1.md` no. El modelo lee los nombres y decide.

---

## 2.1 Conversión de formatos

### De PDF a Markdown
- Manual: copiar/pegar y limpiar (funciona con docs cortos).
- Con IA: sube el PDF a Claude o ChatGPT y pide "convierte a Markdown estructurado con jerarquía de títulos y preserva numeración de artículos".
- Con herramientas: [Pandoc](https://pandoc.org/), [Marker](https://github.com/VikParuchuri/marker), [Docling](https://github.com/docling-project/docling).

### De web a Markdown
- [Jina Reader](https://r.jina.ai/) → convierte URL a markdown limpio.
- [Firecrawl](https://www.firecrawl.dev/) → scraping estructurado.
- Copiar/pegar + limpieza manual para páginas cortas.

### De DOCX / HTML
- Pandoc one-liner: `pandoc input.docx -o output.md`.

---

## 2.2 Estructura recomendada de la base de conocimiento

```
/knowledge-base/
├── 00-index.md                       # Índice general legible para humanos
├── 00-index.json                     # Índice vectorial para el agente
├── core/
│   ├── 01-marco-legal.md
│   ├── 02-definiciones.md
│   └── 03-procesos-clave.md
├── normativa/
│   ├── ley_5_2014.md                 # Ley completa en MD
│   ├── reglamento_2417_1994.md
│   └── directiva_eu_2024_xx.md
├── iso/
│   ├── iso_28000_2022.md
│   ├── iso_18788_2015.md
│   └── iso_22301_2019.md
├── casos-practicos/
│   ├── caso-cameras-comercio.md
│   └── caso-vigilancia-eventos.md
└── faq/
    └── preguntas-frecuentes.md
```

**Regla:** un tema = un archivo. Si un archivo supera ~20.000 palabras, divídelo.

---

## 2.3 Índice vectorial (JSON)

Para archivos grandes, crea un índice que mapee **palabras clave → ubicación**. El agente leerá primero el índice, identificará la sección relevante y solo abrirá esa sección.

### Prompt para generarlo

Plantilla completa: [`templates/prompt-indice-vectorial.md`](../templates/prompt-indice-vectorial.md).

Versión rápida:

```text
Tengo un documento Markdown sobre [TEMA] de [N páginas / palabras].

Analiza su contenido y genera un índice JSON con esta estructura:

{
  "document": "nombre_archivo.md",
  "version": "YYYY-MM-DD",
  "sections": [
    {
      "id": "S1",
      "title": "...",
      "keywords": ["palabra1", "palabra2", ...],
      "location": "Título de sección o línea N"
    }
  ],
  "keyword_index": {
    "palabra_clave_1": ["S1", "S4"],
    "palabra_clave_2": ["S2"]
  }
}

Incluye sinónimos y variantes en keywords. El objetivo es que el agente
localice la sección relevante sin leer el documento entero.
```

### Cómo usarlo en las instrucciones del agente

```markdown
## Consulta de base de conocimiento

IMPORTANTE. Antes de responder sobre cualquier tema del dominio:

1. Identifica las palabras clave de la consulta del usuario.
2. Consulta `00-index.json` para encontrar la(s) sección(es) relevante(s).
3. Lee únicamente la(s) sección(es) identificada(s) en su archivo correspondiente.
4. Formula la respuesta citando el archivo y la sección.

Si ninguna palabra clave del índice coincide con la consulta, indícalo
explícitamente en la respuesta: "No tengo información verificada sobre esto
en mi base de conocimiento."
```

---

## 2.4 Documento maestro de normalización

Crea un `00-index.md` legible para humanos que describa qué hay en cada archivo, vigencia, y a qué tipo de preguntas responde.

Ejemplo:

```markdown
# Índice general — Base de conocimiento Agente Legal de Seguridad Privada

Última actualización: 2026-04-10

## Normativa

| Archivo | Cubre | Vigencia | Tipo de consulta |
|---------|-------|----------|------------------|
| `normativa/ley_5_2014.md` | Ley de Seguridad Privada ES | vigente desde 2014, última modificación 2024 | Obligaciones de empresas, personal habilitado |
| `normativa/reglamento_2417_1994.md` | Reglamento desarrollo | vigente | Requisitos técnicos, documentación |

## ISO

| Archivo | Cubre | Tipo de consulta |
|---------|-------|------------------|
| `iso/iso_28000_2022.md` | Gestión de la seguridad en la cadena de suministro | Certificación, auditoría |
```

Este archivo es para **ti**, pero el agente también puede leerlo como mapa general.

---

## 2.5 Metadatos y fecha de vigencia

En cada archivo, cabecera mínima:

```markdown
---
title: Ley 5/2014 de Seguridad Privada
jurisdiction: España
status: vigente
last_update: 2024-06-12
source: https://www.boe.es/eli/es/l/2014/04/04/5/con
retrieved: 2026-04-10
---

# Ley 5/2014...
```

El agente usa esta cabecera para **decir al usuario cuándo se extrajo la información** y alertar si puede estar desactualizada.

---

## 2.6 Checklist de calidad de la base de conocimiento

- [ ] Todos los documentos están en Markdown (o JSON si son datos estructurados).
- [ ] Ningún archivo supera las ~20.000 palabras sin dividir.
- [ ] Nombres de archivo descriptivos y kebab-case.
- [ ] Existe un `00-index.md` humano.
- [ ] Existe un `00-index.json` vectorial si hay archivos grandes.
- [ ] Cada archivo lleva cabecera con fuente, jurisdicción y fecha.
- [ ] Has verificado 3 afirmaciones al azar contra la fuente primaria.
- [ ] El conjunto cabe mentalmente en un mapa de 1 página.

---

## 2.7 Mantenimiento

La base de conocimiento **no es estática**. Define:

- **Frecuencia de revisión:** mensual / trimestral según volatilidad del dominio.
- **Responsable:** quién actualiza y valida.
- **Changelog:** un `CHANGELOG.md` en la carpeta con cambios fechados.

---

## Errores comunes

- ❌ Subir PDFs largos directamente → RAG pobre.
- ❌ Un único archivo de 300 páginas → el agente no sabe dónde mirar.
- ❌ Nombres de archivo genéricos (`doc1.pdf`) → imposible para el modelo decidir.
- ❌ No versionar ni fechar → responderá con información desfasada sin avisar.

---

👉 Siguiente: [05 · Fase 3 · Prompt maestro](05-fase3-prompt-maestro.md)
