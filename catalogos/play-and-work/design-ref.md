# PLAY & WORK — Catálogo de Eventos Deportivos Corporativos

**Formato:** A4 portrait (210×297mm)
**Páginas:** 9
**Versión:** v3 — 2026-05-15 (Design System v3 aplicado: Anton · Oswald · Open Sans 300 · DM Mono)

## Design System aplicado (v3 canónico)
- **Display:** Anton — UPPERCASE, -0.01em, lh 0.88, mínimo 72px
- **Headline:** Oswald 700 — UPPERCASE, 0.02em tracking
- **Body:** Open Sans 300 — 13–16px, lh 1.65
- **Label:** DM Mono — 9px, 0.20em tracking, UPPERCASE
- **Paleta:** #0A0A0A · #F5F5F5 · #E8001D (máx 3 colores/pieza)
- **Logos:** logo-celsux-white.png (fondos oscuros) · logo-celsux-red.png (fondos claros)

## Correcciones v3 (vs. versión anterior)
- **Tipografía:** DM Sans (retirada) → Open Sans 300. Oswald como display → Anton como display, Oswald como headline.
- **Ghost elements:** × en portada y ? en CTA como elementos gráficos Anton stroke-only (opacity 0.04)
- **Eyebrow pattern:** `──── LABEL` en DM Mono rojo implementado en todas las páginas
- **Sports grid:** 3 columnas × 2 filas (Pádel featured con borde rojo)
- **Marca ×:** Cross accents en cada sport card
- **P2 stat:** Número en rojo (acento) en lugar de negro

## Estructura de páginas
| # | Título | Fondo |
|---|--------|-------|
| 01 | Cover — PLAY & WORK. | Negro |
| 02 | El nuevo wellness corporativo | Blanco |
| 03 | El concepto — Trabajar y jugar | Negro |
| 04 | ¿Qué deporte elige tu equipo? | Blanco |
| 05 | Formatos de evento | Negro |
| 06 | Producción integral | Negro |
| 07 | Cómo trabajamos | Blanco |
| 08 | Trayectoria | Negro |
| 09 | CTA — ¿Comenzamos a crear? | Negro |

## Archivos
- `play-and-work.html` — Fuente editable
- `play-and-work.pdf` — Output final (generado con Puppeteer/Chromium)
- `design-ref.md` — Este archivo

## Exportar PDF
```bash
cd /tmp && node -e "
const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox','--disable-setuid-sandbox','--disable-dev-shm-usage'] });
  const page = await browser.newPage();
  await page.goto('file:///home/user/design/catalogos/play-and-work/play-and-work.html', { waitUntil: 'networkidle0' });
  await page.pdf({ path: '/home/user/design/catalogos/play-and-work/play-and-work.pdf', format: 'A4', printBackground: true, margin: {top:0,right:0,bottom:0,left:0} });
  await browser.close();
})();
"
```
