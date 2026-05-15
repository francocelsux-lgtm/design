# Scripts — Celsux 360

## generate_pdf.py

Genera PDFs con identidad visual Celsux 360 a partir de un JSON de contenido.

### Requisitos

```bash
pip install reportlab pillow
```

### Uso

```bash
# Desde un archivo JSON
python3 scripts/generate_pdf.py data.json output.pdf

# Demo — genera una propuesta de ejemplo
python3 scripts/generate_pdf.py --demo
```

### Estructura del JSON

```json
{
  "type": "presentation",
  "title": "PROPUESTA CORPORATIVA",
  "subtitle": "Evento Anual de Premiación",
  "client": "Nombre del cliente",
  "date": "Mayo 2026",
  "slides": [
    {
      "type": "cover",
      "title": "PROPUESTA CORPORATIVA",
      "subtitle": "Celsux 360 — All-in-one agency",
      "client": "Mercado Libre",
      "date": "Mayo 2026",
      "eyebrow": "Celsux 360"
    },
    {
      "type": "stats",
      "stats": [
        { "value": "25+", "label": "años de experiencia" },
        { "value": "3.000+", "label": "eventos producidos" }
      ]
    },
    {
      "type": "text",
      "eyebrow": "La propuesta",
      "title": "Nuestra propuesta",
      "points": ["Punto 1", "Punto 2"],
      "dark": false
    },
    {
      "type": "services",
      "section_label": "Servicios",
      "title": "Lo que incluye",
      "services": [
        { "name": "Producción General", "description": "Descripción breve." }
      ]
    },
    {
      "type": "contact",
      "cta": "Hablemos.",
      "contact": ["www.celsux.com.ar", "info@celsux.com.ar"]
    }
  ]
}
```

### Tipos de slide

| Tipo | Fondo | Uso |
|------|-------|-----|
| `cover` | Negro | Portada del deck |
| `stats` | Negro | Números de la empresa (25+ años, 3.000+ eventos) |
| `text` | Blanco / Negro | Slide genérico con puntos o párrafo |
| `services` | Blanco | Listado de servicios con descripción |
| `contact` | Negro | CTA + datos de contacto |

### Tipos de documento

| `type` | Orientación | Uso |
|--------|-------------|-----|
| `presentation` | Landscape A4 | Decks, propuestas |
| `one_pager` | Portrait A4 | Fichas de servicio |
