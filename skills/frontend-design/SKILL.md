---
name: frontend-design
description: >
  Crear interfaces web, componentes y UI de alta calidad visual.
  Usar cuando se pide construir algo web: landing page, componente React,
  HTML/CSS, dashboard, formulario, o cualquier interfaz digital interactiva.
---

# Frontend Design — Instrucciones de Ejecución

## Antes de escribir una línea de código

Definir:
- **Propósito:** ¿Qué problema resuelve esta interfaz?
- **Tono:** Elegir una dirección clara y comprometerse con ella
- **Diferenciador:** ¿Qué hace que esta UI sea memorable?

## Sistema de diseño Celsux (para interfaces de la marca)

Si la interfaz es para Celsux, aplicar:
- Importar `assets/colors_and_type.css` con path relativo — nunca hardcodear colores ni fuentes.
- Colores: Negro `#0A0A0A`, Blanco `#F5F5F5`, Rojo `#E8001D`. Máx 3 por pieza.
- Tipografía (Design System v3 — canónico):
  - Display: **Anton** — UPPERCASE, -0.01em, lh 0.88, mínimo 72px siempre
  - Headline: **Oswald 700** — UPPERCASE, 0.02em tracking
  - Body: **Open Sans 300** — 15–17px, lh 1.65
  - Label: **DM Mono** — 8–10px, 0.20em tracking, UPPERCASE
  - Retiradas (nunca usar): ~~DM Sans~~, ~~Barlow Condensed~~, ~~Cormorant~~, ~~Arial~~, ~~Roboto~~, ~~Inter~~
- Sin bordes redondeados excesivos — 0 en bloques/fotos, 12px cards, 20px paneles, 999px botones.
- Animaciones con propósito — no decorativas.

## Principios de ejecución

**Tipografía:**
- Fuentes con carácter. Evitar Inter, Roboto, Arial como fuente principal.
- Pares: display llamativo + body neutro

**Color:**
- Paleta dominante con acento fuerte
- CSS variables para consistencia total

**Composición:**
- Asimetría intencional. Grillas rotas. Negativos generosos.
- Un elemento por pantalla que "rompa" el orden

**Movimiento:**
- CSS-only cuando sea posible
- Una animación de entrada bien orquestada > diez micro-interacciones

## Output

Código funcional, production-grade.
HTML en un solo archivo cuando sea posible.
React con Tailwind si se pide componente.
Sin comentarios de código innecesarios — el código se explica solo.
