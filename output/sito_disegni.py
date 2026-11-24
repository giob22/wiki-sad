"""Disegni SVG del sito di studio: piccoli (viewBox largo 400), con colori presi dal CSS del sito (tema chiaro/scuro).

Ogni funzione `fig_<chiave>` restituisce (svg, didascalia); `tutte()` le raccoglie per chiave. Un disegno compare sul
sito solo se corso.toml lo assegna a una sezione con una voce [[figure]] (lezione, sezione, disegni = ["<chiave>"]).
Le didascalie iniziano con 🧩: i disegni sono miei, costruiti dalle formule delle slide. Si aggiungono SOLO se
l'utente lo decide (il sito, di default, contiene solo il contenuto dei PDF).

Classi CSS utili (definite in crea_sito.py, si adattano al tema):
  linee   ln (nera) · ax (assi) · gd (griglia tratteggiata) · cv cv2 cv3 cv4 (curve colorate) · dash dash2 · ev (spessa)
  aree    fl fl2 (riempimenti trasparenti) · bx bx1 bx2 (riquadri) · pt (punto)
  testo   tx (normale) · ts (piccolo, grigio) · tb (grassetto) · a1 a2 a3 a4 (colori)
Nel testo `x_i`, `x_{i-1}`, `f^{2}` diventano pedici e apici.
"""
import html
import math

import numpy as np

_n = [0]


def _fmt(s):
    """Testo con pedici e apici: x_i, x_{i-1}, f^{2}."""
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c in "_^" and i + 1 < len(s):
            if s[i + 1] == "{":
                j = s.index("}", i)
                tok, i = s[i + 2:j], j + 1
            else:
                tok, i = s[i + 1], i + 2
            dy = 3 if c == "_" else -4
            out.append(f'<tspan dy="{dy}" font-size="0.72em">{html.escape(tok)}</tspan><tspan dy="{-dy}">​</tspan>')
        else:
            out.append(html.escape(c))
            i += 1
    return "".join(out)


class Svg:
    def __init__(self, w, h, titolo):
        _n[0] += 1
        self.i, self.w, self.h, self.titolo, self.e = _n[0], w, h, titolo, []

    def line(self, x1, y1, x2, y2, c="ln", ar=False, ar0=False):
        m = f' marker-end="url(#a{self.i})"' if ar else ""
        m += f' marker-start="url(#a{self.i})"' if ar0 else ""
        self.e.append(f'<line class="{c}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"{m}/>')

    def poly(self, pts, c="cv", close=False, ar=False):
        d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + (" Z" if close else "")
        m = f' marker-end="url(#a{self.i})"' if ar else ""
        self.e.append(f'<path class="{c}" d="{d}"{m}/>')

    def rect(self, x, y, w, h, c="bx", rx=4):
        self.e.append(f'<rect class="{c}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}"/>')

    def circ(self, x, y, r, c="bx"):
        self.e.append(f'<circle class="{c}" cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}"/>')

    def t(self, x, y, s, c="tx", a="middle"):
        self.e.append(f'<text class="{c}" x="{x:.1f}" y="{y:.1f}" text-anchor="{a}">{_fmt(s)}</text>')

    def t2(self, x, y, righe, c="tx", a="middle", dy=14):
        for k, r in enumerate(righe):
            self.t(x, y + k * dy, r, c, a)

    def mult(self, x, y, r=9):
        self.circ(x, y, r)
        self.line(x - r * .55, y - r * .55, x + r * .55, y + r * .55, "ln")
        self.line(x - r * .55, y + r * .55, x + r * .55, y - r * .55, "ln")

    def somma(self, x, y, r=9, segno=("+", "+")):
        self.circ(x, y, r)
        self.t(x, y + 4, "Σ", "ts")

    def render(self):
        defs = (f'<defs><marker id="a{self.i}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
                f'orient="auto-start-reverse"><path class="mk" d="M0 0L10 5L0 10z"/></marker></defs>')
        return (f'<svg viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{html.escape(self.titolo)}" '
                f'xmlns="http://www.w3.org/2000/svg">{defs}{"".join(self.e)}</svg>')


def lobo(s, cx, y0, hw, h, forma="tri", c="cv", fill="fl"):
    if forma == "tri":
        pts = [(cx - hw, y0), (cx, y0 - h), (cx + hw, y0)]
    elif forma == "ris":      # triangolo asimmetrico: picco a destra
        pts = [(cx - hw, y0), (cx + hw * .8, y0 - h), (cx + hw, y0)]
    else:
        pts = [(cx - hw, y0), (cx - hw, y0 - h), (cx + hw, y0 - h), (cx + hw, y0)]
    if fill:
        s.poly(pts, fill, True)
    s.poly(pts, c)


def asse_f(s, x0, x1, y, etichetta="f", alto=None, cx=None):
    s.line(x0, y, x1, y, "ax", ar=True)
    s.t(x1 + 2, y + 15, etichetta, "ts", "end")
    if alto and cx is not None:
        s.line(cx, y + 3, cx, y - alto, "ax", ar=True)


# --------------------------------------------------------------------------------------------- esempio
# Modello da copiare per i disegni del corso (chiave «esempio»). Non compare sul sito finché corso.toml non lo usa.

def fig_esempio():
    s = Svg(400, 150, "esempio: schema a blocchi")
    s.rect(20, 50, 90, 40, "bx bx1")
    s.t(65, 75, "x(t)", "tx")
    s.rect(155, 50, 90, 40)
    s.t(200, 75, "h(t)", "tx")
    s.rect(290, 50, 90, 40, "bx bx2")
    s.t(335, 75, "y(t)", "tx")
    s.line(110, 70, 155, 70, "ln", ar=True)
    s.line(245, 70, 290, 70, "ln", ar=True)
    s.t(200, 125, "y(t) = x(t) ∗ h(t)", "ts")
    return s.render(), "🧩 Esempio: un sistema LTI con ingresso $x(t)$, risposta impulsiva $h(t)$ e uscita $y(t)=x(t)\ast h(t)$."


def tutte():
    f = {k[4:]: v for k, v in globals().items() if k.startswith("fig_")}
    return {k: fn() for k, fn in f.items()}
