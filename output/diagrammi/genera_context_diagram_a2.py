"""Genera il Context Diagram CTX-01 (capitolo A2) come SVG e PNG.

Uso:  py -3.11 genera_context_diagram_a2.py <cartella-di-output>
Produce: ctx-01-context-diagram.svg e ctx-01-context-diagram.png
Linee continue = interazioni applicative; tratteggiate = fuori dal sistema.
"""
import sys
from pathlib import Path

W, H = 1040, 660
out = []


def add(s):
    out.append(s)


def text(x, y, s, size=12, anchor="middle", weight="normal", fill="#0f172a"):
    add(f'<text x="{x}" y="{y}" font-family="Arial" font-size="{size}" '
        f'text-anchor="{anchor}" font-weight="{weight}" fill="{fill}">{s}</text>')


def box(x, y, w, h, title, sub, fill, stroke, dashed=False, sw=2):
    d = ' stroke-dasharray="6 4"' if dashed else ""
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="{sw}"{d}/>')
    text(x + w / 2, y + h / 2 - (6 if sub else -5), title, 14, weight="bold")
    if sub:
        text(x + w / 2, y + h / 2 + 12, sub, 11, fill="#334155")


def head(x, y, direction, color):
    """Punta di freccia piena; direction in 'r','l','u','d'."""
    s = 8
    pts = {"r": [(x, y), (x - s * 1.6, y - s / 1.5), (x - s * 1.6, y + s / 1.5)],
           "l": [(x, y), (x + s * 1.6, y - s / 1.5), (x + s * 1.6, y + s / 1.5)],
           "u": [(x, y), (x - s / 1.5, y + s * 1.6), (x + s / 1.5, y + s * 1.6)],
           "d": [(x, y), (x - s / 1.5, y - s * 1.6), (x + s / 1.5, y - s * 1.6)]}[direction]
    add('<polygon points="' + " ".join(f"{a},{b}" for a, b in pts) + f'" fill="{color}"/>')


def hline(x1, x2, y, label, color="#1d4ed8"):
    """Freccia orizzontale continua con etichetta sopra."""
    direction = "r" if x2 > x1 else "l"
    end = x2 - (1 if direction == "r" else -1) * 12
    add(f'<line x1="{x1}" y1="{y}" x2="{end}" y2="{y}" stroke="{color}" stroke-width="1.8"/>')
    head(x2, y, direction, color)
    text((x1 + x2) / 2, y - 5, label, 11)


def poly(points, color="#475569", start_head=None, end_head=None):
    pts = " ".join(f"{a},{b}" for a, b in points)
    add(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="1.6" '
        f'stroke-dasharray="6 4"/>')
    if end_head:
        head(*points[-1], end_head, color)
    if start_head:
        head(*points[0], start_head, color)


add(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">')
add(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')

# --- attori applicativi (sinistra) ---
AX, AW = 60, 200
box(AX, 140, AW, 100, "Banco", "coordinamento regionale", "#dbeafe", "#1d4ed8")
box(AX, 270, AW, 100, "OPT richiedente", "da smartphone", "#dbeafe", "#1d4ed8")
box(AX, 400, AW, 70, "OPT erogatrice", "stessa organizzazione", "#dbeafe", "#1d4ed8")
box(AX, 500, AW, 100, "Operatore", "interno / esterno", "#dbeafe", "#1d4ed8")

# --- sistema ---
PX, PW = 480, 200
add(f'<rect x="{PX}" y="130" width="{PW}" height="490" rx="14" fill="#fef3c7" '
    f'stroke="#b45309" stroke-width="3.5"/>')
text(PX + PW / 2, 360, "PICUS", 24, weight="bold")
text(PX + PW / 2, 384, "sistema in progetto", 12, fill="#334155")

# --- flussi applicativi ---
L, R = AX + AW, PX
M = (L + R) // 2
hline(L, R, 165, "IF-05 account e catalogo")
hline(L, R, 195, "IF-06 erogatore e appuntamento")
hline(R, L, 225, "IF-07 vista complessiva, schede")
hline(L, R, 295, "IF-01 richiesta di misura")
hline(R, L, 325, "IF-04 stato e appuntamento")
hline(R, L, 355, "IF-08 comunicazioni e allegati")
hline(L, R, 420, "IF-02 misure svolte, dati")
hline(L, R, 450, "IF-03 disponibilità")
hline(R, L, 525, "IF-09 appuntamento da confermare")
hline(L, R, 555, "IF-10 conferma o rifiuto")
hline(L, R, 585, "IF-11 scheda trimestrale")

# --- soggetti fuori dal confine ---
box(700, 20, 260, 80, "Persona o nucleo assistito", "stakeholder, non utente · nessun dato identificativo",
    "#f1f5f9", "#64748b", dashed=True)
box(780, 520, 220, 80, "Portale ministeriale", "sistema esterno", "#f1f5f9", "#64748b", dashed=True)

# --- flussi fuori dal sistema (corridoi esterni) ---
# IF-14: Operatore -> assistito (corridoio piu' esterno)
poly([(AX, 550), (10, 550), (10, 40), (700, 40)], end_head="r")
text(330, 34, "IF-14 erogazione della misura (Operatore → assistito)", 11, fill="#475569")
# IF-12: OPT richiedente <-> assistito
poly([(AX, 305), (25, 305), (25, 60), (700, 60)], start_head=None, end_head="r")
head(AX, 305, "r", "#475569")
text(330, 76, "IF-12 contatto diretto (OPT ↔ assistito)", 11, fill="#475569")
# IF-13: Banco -> portale (inserimento manuale)
poly([(AX, 190), (40, 190), (40, 105), (1020, 105), (1020, 560), (1000, 560)], end_head="l")
text(330, 99, "IF-13 inserimento manuale (Banco → portale)", 11, fill="#475569")

# --- legenda ---
lx, ly = 720, 200
add(f'<rect x="{lx}" y="{ly}" width="290" height="150" rx="8" fill="#ffffff" stroke="#cbd5e1"/>')
text(lx + 12, ly + 24, "Legenda", 13, anchor="start", weight="bold")
add(f'<line x1="{lx + 12}" y1="{ly + 48}" x2="{lx + 62}" y2="{ly + 48}" stroke="#1d4ed8" stroke-width="1.8"/>')
text(lx + 72, ly + 52, "interazione applicativa", 11, anchor="start")
add(f'<line x1="{lx + 12}" y1="{ly + 74}" x2="{lx + 62}" y2="{ly + 74}" stroke="#475569" '
    f'stroke-width="1.6" stroke-dasharray="6 4"/>')
text(lx + 72, ly + 78, "fuori dal sistema (non applicativa)", 11, anchor="start")
add(f'<rect x="{lx + 12}" y="{ly + 92}" width="22" height="14" rx="3" fill="#dbeafe" stroke="#1d4ed8"/>')
text(lx + 72, ly + 103, "utente applicativo", 11, anchor="start")
add(f'<rect x="{lx + 12}" y="{ly + 116}" width="22" height="14" rx="3" fill="#f1f5f9" '
    f'stroke="#64748b" stroke-dasharray="4 3"/>')
text(lx + 72, ly + 127, "soggetto o sistema esterno", 11, anchor="start")

add("</svg>")
svg = "\n".join(out)

dest = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
dest.mkdir(parents=True, exist_ok=True)
(dest / "ctx-01-context-diagram.svg").write_text(svg, encoding="utf-8")

import pymupdf  # noqa: E402

doc = pymupdf.open(str(dest / "ctx-01-context-diagram.svg"))
pix = doc[0].get_pixmap(matrix=pymupdf.Matrix(2, 2))
pix.save(str(dest / "ctx-01-context-diagram.png"))
print("ok", pix.width, pix.height)
