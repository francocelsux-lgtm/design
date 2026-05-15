#!/usr/bin/env python3
"""
Celsux 360 — PDF Generator
Genera PDFs con identidad visual de Celsux 360.
Tipos soportados: presentation, proposal, one_pager, social_mockup

Uso:
    python3 scripts/generate_pdf.py data.json output.pdf
    python3 scripts/generate_pdf.py --demo

Requiere: pip install reportlab pillow
"""

import sys
import json
import os
from datetime import datetime

try:
    from reportlab.lib.pagesizes import letter, A4, landscape
    from reportlab.lib.units import inch, mm
    from reportlab.lib.colors import HexColor, white, black, Color
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table,
        TableStyle, PageBreak, HRFlowable
    )
    from reportlab.graphics.shapes import Drawing, Rect, String, Line
    from reportlab.graphics import renderPDF
    from reportlab.pdfgen import canvas as pdfcanvas
except ImportError:
    print("Error: reportlab requerido. Instalar con: pip install reportlab")
    sys.exit(1)


# ── CELSUX 360 BRAND COLORS ───────────────────────────────────────────────────
C = {
    "red":        HexColor("#E8001D"),
    "red_dark":   HexColor("#B8001A"),
    "black":      HexColor("#0A0A0A"),
    "white":      HexColor("#F5F5F5"),
    "gray":       HexColor("#6B6B6B"),
    "gray_light": HexColor("#D0D0D0"),
}

# ── SLIDE DIMENSIONS (1280×720 landscape, scaled to PDF) ─────────────────────
SLIDE_W = 25.4 * mm * (1280 / 96)   # ≈ approx — use letter landscape
SLIDE_H = 25.4 * mm * (720 / 96)

PAGE_LANDSCAPE = landscape(A4)       # 297 × 210 mm — close to 16:9
PAGE_PORTRAIT  = A4                  # 210 × 297 mm — one-pagers


def make_styles():
    base = getSampleStyleSheet()
    return {
        "display": ParagraphStyle(
            "display",
            fontName="Helvetica-Bold",
            fontSize=48,
            textColor=C["white"],
            leading=50,
            spaceAfter=8,
        ),
        "headline": ParagraphStyle(
            "headline",
            fontName="Helvetica-Bold",
            fontSize=24,
            textColor=C["red"],
            leading=28,
            spaceAfter=6,
        ),
        "headline_dark": ParagraphStyle(
            "headline_dark",
            fontName="Helvetica-Bold",
            fontSize=24,
            textColor=C["black"],
            leading=28,
            spaceAfter=6,
        ),
        "subhead": ParagraphStyle(
            "subhead",
            fontName="Helvetica-Bold",
            fontSize=16,
            textColor=C["white"],
            leading=20,
            spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "body",
            fontName="Helvetica",
            fontSize=10,
            textColor=C["gray"],
            leading=15,
            spaceAfter=4,
        ),
        "body_light": ParagraphStyle(
            "body_light",
            fontName="Helvetica",
            fontSize=10,
            textColor=C["white"],
            leading=15,
            spaceAfter=4,
        ),
        "label": ParagraphStyle(
            "label",
            fontName="Helvetica-Bold",
            fontSize=8,
            textColor=C["red"],
            leading=10,
            spaceAfter=2,
            letterSpacing=2,
        ),
        "eyebrow": ParagraphStyle(
            "eyebrow",
            fontName="Helvetica-Bold",
            fontSize=8,
            textColor=C["red"],
            leading=10,
            spaceAfter=6,
            letterSpacing=2,
        ),
        "stat": ParagraphStyle(
            "stat",
            fontName="Helvetica-Bold",
            fontSize=56,
            textColor=C["red"],
            leading=58,
            spaceAfter=0,
        ),
        "stat_label": ParagraphStyle(
            "stat_label",
            fontName="Helvetica",
            fontSize=11,
            textColor=C["gray"],
            leading=13,
            spaceAfter=0,
        ),
        "footer": ParagraphStyle(
            "footer",
            fontName="Helvetica",
            fontSize=7,
            textColor=C["gray"],
            leading=9,
        ),
    }


# ── CANVAS CALLBACKS (headers / footers / backgrounds) ───────────────────────

def _dark_slide_bg(canv, doc):
    canv.saveState()
    canv.setFillColor(C["black"])
    canv.rect(0, 0, doc.pagesize[0], doc.pagesize[1], fill=1, stroke=0)
    # Red accent bar — top
    canv.setFillColor(C["red"])
    canv.rect(0, doc.pagesize[1] - 4, doc.pagesize[0], 4, fill=1, stroke=0)
    # Footer line
    canv.setFillColor(C["gray"])
    canv.setFont("Helvetica", 7)
    canv.drawString(doc.leftMargin, 14, "www.celsux.com.ar  ×  info@celsux.com.ar  ×  Buenos Aires, Argentina")
    canv.restoreState()


def _light_slide_bg(canv, doc):
    canv.saveState()
    canv.setFillColor(C["white"])
    canv.rect(0, 0, doc.pagesize[0], doc.pagesize[1], fill=1, stroke=0)
    # Red accent bar — left edge
    canv.setFillColor(C["red"])
    canv.rect(0, 0, 4, doc.pagesize[1], fill=1, stroke=0)
    # Footer
    canv.setFillColor(C["gray"])
    canv.setFont("Helvetica", 7)
    canv.drawString(doc.leftMargin + 10, 14, "www.celsux.com.ar  ×  celsux.")
    canv.restoreState()


def _portrait_bg(canv, doc):
    canv.saveState()
    canv.setFillColor(C["white"])
    canv.rect(0, 0, doc.pagesize[0], doc.pagesize[1], fill=1, stroke=0)
    canv.setFillColor(C["red"])
    canv.rect(0, doc.pagesize[1] - 8, doc.pagesize[0], 8, fill=1, stroke=0)
    canv.setFillColor(C["gray"])
    canv.setFont("Helvetica", 7)
    canv.drawString(doc.leftMargin, 14, "www.celsux.com.ar  ×  celsux.")
    canv.restoreState()


# ── BLOCK BUILDERS ────────────────────────────────────────────────────────────

def _red_rule(width=None):
    return HRFlowable(
        width=width or "100%",
        thickness=2,
        color=C["red"],
        spaceAfter=8,
        spaceBefore=4,
    )


def _eyebrow_para(text, styles):
    return Paragraph(f"──── {text.upper()}", styles["eyebrow"])


def _stat_block(value, label, styles):
    return Table(
        [[Paragraph(value, styles["stat"])],
         [Paragraph(label.upper(), styles["stat_label"])]],
        colWidths=["100%"],
        style=TableStyle([
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
        ]),
    )


def _service_row(name, description, styles):
    return Table(
        [[
            Paragraph(name, styles["headline_dark"]),
            Paragraph(description, styles["body"]),
        ]],
        colWidths=["35%", "65%"],
        style=TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ("LINEBELOW", (0, 0), (-1, -1), 0.5, C["gray_light"]),
        ]),
    )


# ── SLIDE GENERATORS ─────────────────────────────────────────────────────────

def slide_cover(data, styles):
    """Slide 01 — Portada (fondo negro)."""
    elements = []
    elements.append(Spacer(1, 0.6 * inch))
    if data.get("eyebrow"):
        elements.append(_eyebrow_para(data["eyebrow"], styles))
    elements.append(Paragraph(data.get("title", "PROPUESTA COMERCIAL"), styles["display"]))
    elements.append(_red_rule())
    if data.get("subtitle"):
        elements.append(Paragraph(data["subtitle"], styles["subhead"]))
    elements.append(Spacer(1, 0.3 * inch))
    meta = []
    if data.get("client"):
        meta.append(f"Cliente: {data['client']}")
    if data.get("date"):
        meta.append(f"Fecha: {data['date']}")
    for m in meta:
        elements.append(Paragraph(m, styles["body_light"]))
    return elements, _dark_slide_bg


def slide_stats(data, styles):
    """Slide — Stats de la empresa (fondo negro)."""
    elements = []
    elements.append(Spacer(1, 0.3 * inch))
    elements.append(_eyebrow_para("Celsux 360 en números", styles))
    elements.append(Spacer(1, 0.15 * inch))

    stats = data.get("stats", [
        {"value": "25+", "label": "años de experiencia"},
        {"value": "3.000+", "label": "eventos producidos"},
        {"value": "360°", "label": "cobertura de servicios"},
    ])

    cols = [_stat_block(s["value"], s["label"], styles) for s in stats]
    col_widths = [f"{100 / len(cols)}%" for _ in cols]

    table = Table([cols], colWidths=col_widths)
    table.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 0.2 * inch))

    clients = data.get("clients", "DirecTV · McDonald's · Adidas · LATAM · GSK · Mercado Libre · BBVA")
    elements.append(Paragraph(clients, styles["body_light"]))
    return elements, _dark_slide_bg


def slide_services(data, styles):
    """Slide — Listado de servicios (fondo blanco)."""
    elements = []
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(_eyebrow_para(data.get("section_label", "Servicios"), styles))
    elements.append(Paragraph(data.get("title", "Lo que hacemos"), styles["headline_dark"]))
    elements.append(_red_rule())
    elements.append(Spacer(1, 0.1 * inch))

    for svc in data.get("services", []):
        elements.append(_service_row(svc["name"], svc.get("description", ""), styles))
    return elements, _light_slide_bg


def slide_text(data, styles):
    """Slide genérico de texto (fondo blanco o negro según 'dark')."""
    dark = data.get("dark", False)
    elements = []
    elements.append(Spacer(1, 0.3 * inch))
    if data.get("eyebrow"):
        elements.append(_eyebrow_para(data["eyebrow"], styles))
    title_style = styles["display"] if dark else styles["headline_dark"]
    elements.append(Paragraph(data.get("title", ""), title_style))
    elements.append(_red_rule())
    body_style = styles["body_light"] if dark else styles["body"]
    for point in data.get("points", []):
        elements.append(Paragraph(f"× {point}", body_style))
        elements.append(Spacer(1, 0.05 * inch))
    if data.get("body"):
        elements.append(Paragraph(data["body"], body_style))
    bg = _dark_slide_bg if dark else _light_slide_bg
    return elements, bg


def slide_contact(data, styles):
    """Slide — Contacto / cierre (fondo negro)."""
    elements = []
    elements.append(Spacer(1, 0.5 * inch))
    elements.append(_eyebrow_para("Próximos pasos", styles))
    elements.append(Paragraph(
        data.get("cta", "Hablemos."),
        styles["display"]
    ))
    elements.append(_red_rule())
    elements.append(Spacer(1, 0.2 * inch))
    contact_items = data.get("contact", [
        "www.celsux.com.ar",
        "info@celsux.com.ar",
        "Buenos Aires, Argentina",
    ])
    for item in contact_items:
        elements.append(Paragraph(item, styles["subhead"]))
    return elements, _dark_slide_bg


# ── SLIDE ROUTER ──────────────────────────────────────────────────────────────

SLIDE_TYPES = {
    "cover":    slide_cover,
    "stats":    slide_stats,
    "services": slide_services,
    "text":     slide_text,
    "contact":  slide_contact,
}


# ── MAIN GENERATOR ────────────────────────────────────────────────────────────

def generate(data: dict, output_path: str) -> str:
    doc_type = data.get("type", "presentation")
    pagesize = PAGE_PORTRAIT if doc_type == "one_pager" else PAGE_LANDSCAPE

    doc = SimpleDocTemplate(
        output_path,
        pagesize=pagesize,
        rightMargin=0.75 * inch,
        leftMargin=0.85 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.4 * inch,
    )

    styles = make_styles()
    story = []

    slides = data.get("slides", [])
    if not slides:
        slides = _default_slides(data)

    for i, slide in enumerate(slides):
        slide_type = slide.get("type", "text")
        builder = SLIDE_TYPES.get(slide_type, slide_text)
        elements, bg_fn = builder(slide, styles)

        # Wrap slide in OnPage callback for background
        from reportlab.platypus import FrameBreak
        from reportlab.platypus.flowables import DocAssign

        story.extend(elements)
        if i < len(slides) - 1:
            story.append(PageBreak())

    # Build with alternating background functions per page
    bg_fns = []
    for slide in slides:
        slide_type = slide.get("type", "text")
        dark = slide.get("dark", slide_type in ("cover", "stats", "contact"))
        bg_fns.append(_dark_slide_bg if dark else _light_slide_bg)

    # Use a custom canvas that applies the right background per page
    class BrandedCanvas(pdfcanvas.Canvas):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._page_index = 0

        def showPage(self):
            super().showPage()
            self._page_index += 1

    def make_canvas(*args, **kwargs):
        return BrandedCanvas(*args, **kwargs)

    # Simpler approach: use onFirstPage / onLaterPages cycling approach
    _bg_cycle = [_dark_slide_bg, _light_slide_bg]
    _page_bg_map = {}
    for i, slide in enumerate(slides):
        slide_type = slide.get("type", "text")
        dark = slide.get("dark", slide_type in ("cover", "stats", "contact"))
        _page_bg_map[i + 1] = _dark_slide_bg if dark else _light_slide_bg

    class PageBgTemplate(SimpleDocTemplate):
        def __init__(self, *a, bg_map=None, **kw):
            super().__init__(*a, **kw)
            self._bg_map = bg_map or {}
            self._cur_page = 0

        def handle_pageBegin(self):
            super().handle_pageBegin()

        def afterPage(self):
            pass

    def on_page(canv, doc):
        page_num = doc.page
        bg_fn = _page_bg_map.get(page_num, _light_slide_bg)
        bg_fn(canv, doc)

    # Rebuild story with on_page callbacks using NextPageTemplate pattern
    doc_final = SimpleDocTemplate(
        output_path,
        pagesize=pagesize,
        rightMargin=0.75 * inch,
        leftMargin=0.85 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.4 * inch,
    )

    story_final = []
    for i, slide in enumerate(slides):
        slide_type = slide.get("type", "text")
        builder = SLIDE_TYPES.get(slide_type, slide_text)
        elements, _ = builder(slide, styles)
        story_final.extend(elements)
        if i < len(slides) - 1:
            story_final.append(PageBreak())

    # Determine first/later page backgrounds from first two slides
    first_bg = _page_bg_map.get(1, _dark_slide_bg)
    later_bg = _page_bg_map.get(2, _light_slide_bg)

    # For multi-page with alternating, use a per-page approach via canvMaker
    _bg_seq = [_page_bg_map.get(i + 1, _light_slide_bg) for i in range(len(slides))]

    class SeqCanvas(pdfcanvas.Canvas):
        _seq = _bg_seq

        def showPage(self):
            idx = self._pageNumber - 1
            if idx < len(self._seq):
                # Draw background before finalizing page
                self.saveState()
                self._seq[idx](self, type("doc", (), {
                    "pagesize": (self._pagesize[0], self._pagesize[1]),
                    "leftMargin": 0.85 * inch,
                })())
                self.restoreState()
            super().showPage()

    # Use simplest reliable approach: single bg function applied per page
    doc_final.build(
        story_final,
        onFirstPage=_page_bg_map.get(1, _dark_slide_bg),
        onLaterPages=_page_bg_map.get(2, _light_slide_bg),
    )

    return output_path


def _default_slides(data):
    """Default slide structure for a commercial proposal."""
    return [
        {
            "type": "cover",
            "title": data.get("title", "PROPUESTA COMERCIAL").upper(),
            "subtitle": data.get("subtitle", "Celsux 360 — All-in-one agency"),
            "client": data.get("client", ""),
            "date": data.get("date", datetime.now().strftime("%B %Y")),
            "eyebrow": "Celsux 360",
        },
        {
            "type": "stats",
            "stats": [
                {"value": "25+", "label": "años de experiencia"},
                {"value": "3.000+", "label": "eventos producidos"},
                {"value": "360°", "label": "cobertura de servicios"},
            ],
        },
        {
            "type": "text",
            "eyebrow": "La propuesta",
            "title": data.get("proposal_title", "Nuestra propuesta"),
            "points": data.get("proposal_points", [
                "Producción integral del evento",
                "Equipo dedicado 24/7",
                "Experiencia con clientes Fortune 500",
            ]),
            "dark": False,
        },
        {
            "type": "services",
            "services": data.get("services", [
                {"name": "Producción", "description": "Coordinación total del evento de principio a fin."},
                {"name": "Ambientación", "description": "Diseño y montaje de escenografía de alto impacto."},
                {"name": "Audiovisual", "description": "Sonido, iluminación y pantallas profesionales."},
            ]),
        },
        {
            "type": "contact",
            "cta": data.get("cta", "Hablemos."),
            "contact": [
                "www.celsux.com.ar",
                "info@celsux.com.ar",
                data.get("contact_name", ""),
            ],
        },
    ]


def demo():
    data = {
        "type": "presentation",
        "title": "PROPUESTA CORPORATIVA",
        "subtitle": "Evento Anual de Premiación",
        "client": "Mercado Libre",
        "date": "Mayo 2026",
        "proposal_points": [
            "Gala de premiación para 500 personas en Palacio Duhau",
            "Producción audiovisual con transmisión en vivo",
            "Ambientación premium con identidad corporativa del cliente",
            "Catering y coordinación logística completa",
        ],
        "services": [
            {"name": "Producción General", "description": "Coordinación integral: venue, proveedores, cronograma y staff."},
            {"name": "Diseño & Ambientación", "description": "Escenografía, branding del evento, materiales impresos."},
            {"name": "Audiovisual", "description": "Pantallas LED, sonido line-array, iluminación de espectáculo."},
            {"name": "Transmisión en Vivo", "description": "Streaming multicanal con switcher profesional y operador dedicado."},
            {"name": "Catering", "description": "Coordinación de menú con proveedor seleccionado por el cliente."},
        ],
        "cta": "Hablemos.",
    }
    out = generate(data, "DEMO-Celsux360.pdf")
    print(f"PDF demo generado: {out}")


if __name__ == "__main__":
    if "--demo" in sys.argv:
        demo()
    elif len(sys.argv) >= 2:
        with open(sys.argv[1]) as f:
            data = json.load(f)
        out = sys.argv[2] if len(sys.argv) >= 3 else "output.pdf"
        generate(data, out)
        print(f"PDF generado: {out}")
    else:
        print("Uso: python3 generate_pdf.py data.json output.pdf")
        print("     python3 generate_pdf.py --demo")
