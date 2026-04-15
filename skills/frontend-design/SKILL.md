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
- Colores: Negro `#0A0A0A`, Blanco `#F5F5F5`, Rojo `#E8001D`
- Tipografía display: condensed bold
- Sin bordes redondeados excesivos — geometría limpia y angular
- Animaciones con propósito — no decorativas

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
