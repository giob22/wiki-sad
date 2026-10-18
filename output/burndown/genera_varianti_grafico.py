"""Quattro varianti grafiche del burndown, su dati SIMULATI (quelli di burndown.py --demo).

Uso:  py -3.11 genera_varianti_grafico.py <cartella-di-output>
Produce varianti/A-stile-docente, B-dashboard, C-scuro, D-task (SVG e PNG).
Serve solo per scegliere il design: nessun collegamento con GitHub.
"""
import sys
from datetime import datetime, timedelta
from pathlib import Path

import pymupdf

sys.path.insert(0, str(Path(__file__).parent))
import burndown as b  # noqa: E402

UTC = b.UTC
NOW = datetime(2026, 10, 30, 12, tzinfo=UTC)
ITEMS = b.demo_items()
TITLE, START, DAYS = b.pick_iteration(ITEMS, "", NOW.date())
MINE, BASE, ROWS = b.compute(ITEMS, TITLE, START, DAYS, NOW)
T0 = datetime.combine(START, datetime.min.time(), UTC)
X_NOW = (NOW - T0).total_seconds() / 86400
SCOPE_NOW, DONE_NOW, REM_NOW = ROWS[-1][1], ROWS[-1][2], ROWS[-1][3]
IDEAL_NOW = BASE * (1 - X_NOW / DAYS)
VELOCITY = DONE_NOW / X_NOW                      # punti completati al giorno
LEFT = DAYS - X_NOW
FORECAST_END = max(0.0, REM_NOW - VELOCITY * LEFT)
BEHIND = REM_NOW - IDEAL_NOW


def day(d):
    return START + timedelta(days=d)


def events():
    """Eventi (giorno, delta, titolo, punti): +punti se aggiunto a sprint iniziato, -punti se Done."""
    ev = []
    for i in MINE:
        xc = (i["created"] - T0).total_seconds() / 86400
        if xc > 0:
            ev.append((xc, +i["points"], i["title"], i["points"]))
        if i["done_at"] and i["done_at"] <= NOW:
            ev.append(((i["done_at"] - T0).total_seconds() / 86400, -i["points"], i["title"], i["points"]))
    return sorted(ev)


def step_points():
    pts, cur = [(0.0, ROWS[0][3])], ROWS[0][3]
    for x, d, _, _ in events():
        pts += [(x, cur), (x, cur + d)]
        cur += d
    pts.append((X_NOW, cur))
    return pts


def scope_steps():
    pts, cur = [(0.0, ROWS[0][1])], ROWS[0][1]
    for x, d, _, _ in events():
        if d > 0:
            pts += [(x, cur), (x, cur + d)]
            cur += d
    pts.append((DAYS, cur))
    return pts


def nice_step(ymax):
    for s in (1, 2, 5, 10, 20, 50):
        if ymax / s <= 8:
            return s


class Svg:
    def __init__(self, w, h, bg):
        self.w, self.h = w, h
        self.o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
                  f'font-family="Arial">', f'<rect width="{w}" height="{h}" fill="{bg}"/>']

    def add(self, s):
        self.o.append(s)

    def text(self, x, y, s, size=12, anchor="middle", color="#0f172a", weight="normal", extra=""):
        self.o.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" fill="{color}" '
                      f'font-weight="{weight}" {extra}>{s}</text>')

    def line(self, x1, y1, x2, y2, color, w=1.5, dash=""):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" '
                      f'stroke-width="{w}"{d}/>')

    def poly(self, pts, fill, op=1.0, stroke="none", w=1.5, dash="", closed=True):
        tag = "polygon" if closed else "polyline"
        d = f' stroke-dasharray="{dash}"' if dash else ""
        f = fill if closed else "none"
        self.o.append(f'<{tag} points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) +
                      f'" fill="{f}" fill-opacity="{op}" stroke="{stroke}" stroke-width="{w}" '
                      f'stroke-linejoin="round"{d}/>')

    def rect(self, x, y, w, h, fill, rx=8, stroke="none", sw=1, op=1.0):
        self.o.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" '
                      f'fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}"/>')

    def circle(self, x, y, r, fill, stroke="none", sw=1):
        self.o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" '
                      f'stroke-width="{sw}"/>')

    def save(self, folder, name):
        self.o.append("</svg>")
        folder.mkdir(parents=True, exist_ok=True)
        svg = folder / f"{name}.svg"
        svg.write_text("\n".join(self.o), encoding="utf-8")
        doc = pymupdf.open(str(svg))
        doc[0].get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5)).save(str(folder / f"{name}.png"))


class Plot:
    """Area del grafico con scale lineari x (giorni) e y (punti)."""
    def __init__(self, x0, y0, w, h, ymax):
        self.x0, self.y0, self.w, self.h, self.ymax = x0, y0, w, h, ymax

    def X(self, d):
        return self.x0 + self.w * d / DAYS

    def Y(self, v):
        return self.y0 + self.h * (1 - v / self.ymax)

    def P(self, pts):
        return [(self.X(x), self.Y(y)) for x, y in pts]


def shade_between(svg, pl, xs, ys_act, behind="#f9a8d4", ahead="#93c5fd", op=0.45):
    ideal = lambda x: BASE * (1 - x / DAYS)
    for i in range(len(xs) - 1):
        x0, x1, a0, a1 = xs[i], xs[i + 1], ys_act[i], ys_act[i + 1]
        d0, d1 = a0 - ideal(x0), a1 - ideal(x1)
        if d0 * d1 >= 0:
            col = behind if (d0 + d1) > 0 else ahead
            svg.poly(pl.P([(x0, a0), (x1, a1), (x1, ideal(x1)), (x0, ideal(x0))]), col, op)
        else:
            t = d0 / (d0 - d1)
            xc = x0 + t * (x1 - x0)
            yc = ideal(xc)
            svg.poly(pl.P([(x0, a0), (xc, yc), (x0, ideal(x0))]), behind if d0 > 0 else ahead, op)
            svg.poly(pl.P([(xc, yc), (x1, a1), (x1, ideal(x1))]), behind if d1 > 0 else ahead, op)


def grid(svg, pl, ymax, color, label_color, day_labels="date", every=1, size=10, show_days=True):
    st = nice_step(ymax)
    for v in range(0, int(ymax) + 1, st):
        svg.line(pl.x0, pl.Y(v), pl.x0 + pl.w, pl.Y(v), color, 1)
        svg.text(pl.x0 - 8, pl.Y(v) + 4, str(v), size + 1, "end", label_color)
    for d in range(0, DAYS + 1, every):
        svg.line(pl.X(d), pl.y0, pl.X(d), pl.y0 + pl.h, color, 1)
        lab = f"{d + 1}" if day_labels == "num" else f"{day(d):%d/%m}"
        if not show_days or (day_labels == "num" and d == DAYS):
            continue
        svg.text(pl.X(d + (0.5 if day_labels == "num" else 0)), pl.y0 + pl.h + 16, lab, size, "middle", label_color)


# ---------------------------------------------------------------- A: stile docente
def variante_a():
    s = Svg(960, 560, "#fbf5e6")
    s.text(480, 40, "IL GRAFICO BURNDOWN: AVANZAMENTO DELLO SPRINT", 22, color="#1f2937", weight="bold")
    s.text(480, 62, f"{TITLE} · {START:%d/%m} → {day(DAYS):%d/%m/%Y} · punti rimanenti (dati simulati)", 13, color="#6b7280")
    s.rect(40, 80, 880, 440, "#ffffff", 14, "#d6c9a8", 2)
    ymax = (max(SCOPE_NOW, BASE) // 5 + 2) * 5
    pl = Plot(110, 125, 780, 330, ymax)
    grid(s, pl, ymax, "#e5e7eb", "#4b5563", "num", every=1, size=10)
    xs = [r[0] for r in ROWS]
    acts = [r[3] for r in ROWS]
    shade_between(s, pl, xs, acts)
    s.poly(pl.P([(0, BASE), (DAYS, 0)]), "none", stroke="#374151", w=2.2, dash="2 4", closed=False)
    s.poly(pl.P(scope_steps()), "none", stroke="#1f6fa8", w=2.8, closed=False)
    s.poly(pl.P(list(zip(xs, acts))), "none", stroke="#8e1b6f", w=3, closed=False)
    for x, a in zip(xs, acts):
        s.circle(pl.X(x), pl.Y(a), 3.5, "#8e1b6f")
    ch = [e for e in events() if e[1] > 0]
    if ch:
        xc, dp = ch[0][0], sum(e[1] for e in ch)
        cx, cy = pl.X(xc), pl.Y(ROWS[0][1] + ch[0][1])
        s.line(cx, cy, cx + 60, cy - 36, "#1f2937", 1.2)
        s.rect(cx + 60, cy - 66, 190, 40, "#fff7d6", 6, "#d6c9a8")
        s.text(cx + 155, cy - 50, "AMBITO MODIFICATO", 11, color="#1f2937", weight="bold")
        s.text(cx + 155, cy - 35, f"aggiunti {dp:g} punti a sprint iniziato", 10, color="#374151")
    s.text(500, 500, "GIORNI DELLO SPRINT", 12, color="#374151", weight="bold")
    s.text(52, 280, "PUNTI RIMANENTI", 12, color="#374151", weight="bold", extra='transform="rotate(-90 52 280)"')
    ly = 98
    for x, col, dash, txt in ((110, "#374151", "2 4", "ideale"), (205, "#8e1b6f", "", "reale"),
                              (285, "#1f6fa8", "", "ambito (scope)")):
        s.line(x, ly, x + 34, ly, col, 3, dash)
        s.text(x + 42, ly + 4, txt, 12, "start", "#1f2937")
    s.rect(440, ly - 7, 22, 14, "#f9a8d4", 3, op=0.7)
    s.text(468, ly + 4, "in ritardo sull'ideale", 12, "start", "#1f2937")
    s.rect(640, ly - 7, 22, 14, "#93c5fd", 3, op=0.7)
    s.text(668, ly + 4, "in anticipo sull'ideale", 12, "start", "#1f2937")
    return s


# ---------------------------------------------------------------- B: dashboard
def variante_b():
    s = Svg(960, 600, "#f3f4f6")
    s.text(40, 42, f"Burndown · {TITLE}", 22, "start", "#111827", "bold")
    s.text(40, 62, f"{START:%d/%m/%Y} → {day(DAYS):%d/%m/%Y} · aggiornato al {NOW:%d/%m %H:%M} (dati simulati)", 12,
           "start", "#6b7280")
    ritardo = BEHIND > 0.5
    cards = [("RIMANENTI", f"{REM_NOW:g}", "punti", "#1d4ed8"),
             ("COMPLETATI", f"{DONE_NOW:g} / {SCOPE_NOW:g}", f"{DONE_NOW / SCOPE_NOW:.0%} del lavoro", "#047857"),
             ("GIORNI RIMASTI", f"{LEFT:.1f}", f"su {DAYS}", "#6d28d9"),
             ("STATO", "In ritardo" if ritardo else "In linea",
              f"{abs(BEHIND):.1f} punti {'sopra' if ritardo else 'sotto'} la linea ideale",
              "#b91c1c" if ritardo else "#047857")]
    for k, (t, v, sub, col) in enumerate(cards):
        x = 40 + k * 224
        s.rect(x, 82, 208, 92, "#ffffff", 12, "#e5e7eb")
        s.rect(x, 82, 6, 92, col, 3)
        s.text(x + 20, 106, t, 11, "start", "#6b7280", "bold")
        s.text(x + 20, 142, v, 28 if len(v) < 9 else 22, "start", col, "bold")
        s.text(x + 20, 162, sub, 11, "start", "#6b7280")
    s.rect(40, 192, 880, 380, "#ffffff", 12, "#e5e7eb")
    ymax = (max(SCOPE_NOW, BASE) // 5 + 2) * 5
    pl = Plot(100, 220, 790, 280, ymax)
    grid(s, pl, ymax, "#f1f5f9", "#6b7280", "date", every=3)
    xs, acts = [r[0] for r in ROWS], [r[3] for r in ROWS]
    area = [(xs[0], 0)] + list(zip(xs, acts)) + [(xs[-1], 0)]
    s.poly(pl.P(area), "#2563eb", 0.12)
    s.poly(pl.P([(0, BASE), (DAYS, 0)]), "none", stroke="#9ca3af", w=2, dash="7 5", closed=False)
    s.poly(pl.P([(X_NOW, REM_NOW), (DAYS, FORECAST_END)]), "none", stroke="#ea580c", w=2.2, dash="3 4", closed=False)
    s.poly(pl.P(list(zip(xs, acts))), "none", stroke="#2563eb", w=3, closed=False)
    for x, a in zip(xs, acts):
        s.circle(pl.X(x), pl.Y(a), 3.2, "#ffffff", "#2563eb", 2)
    s.line(pl.X(X_NOW), pl.y0, pl.X(X_NOW), pl.y0 + pl.h, "#ef4444", 1.3, "4 3")
    s.rect(pl.X(X_NOW) - 24, pl.y0 - 4, 48, 18, "#ef4444", 9)
    s.text(pl.X(X_NOW), pl.y0 + 9, "OGGI", 10, color="#ffffff", weight="bold")
    s.circle(pl.X(DAYS), pl.Y(FORECAST_END), 5, "#ea580c")
    px, py = pl.X(DAYS), pl.y0 + 32
    s.line(px, py + 26, px, pl.Y(FORECAST_END) - 6, "#ea580c", 1.2, "3 3")
    s.rect(px - 250, py, 250, 26, "#fff7ed", 13, "#ea580c", 1.2)
    s.text(px - 125, py + 17, f"Previsione: {FORECAST_END:.0f} punti non completati a fine sprint", 11, color="#c2410c",
           weight="bold")
    ly = 540
    for x, col, dash, txt in ((100, "#2563eb", "", "punti rimanenti"), (260, "#9ca3af", "7 5", "ideale"),
                              (360, "#ea580c", "3 4", f"previsione al ritmo attuale ({VELOCITY:.1f} punti/giorno)")):
        s.line(x, ly, x + 30, ly, col, 3, dash)
        s.text(x + 38, ly + 4, txt, 12, "start", "#374151")
    return s


# ---------------------------------------------------------------- C: scuro
def variante_c():
    s = Svg(960, 540, "#0b1220")
    s.text(40, 46, "BURNDOWN", 12, "start", "#38bdf8", "bold")
    s.text(40, 76, TITLE, 26, "start", "#f8fafc", "bold")
    s.text(40, 98, f"{START:%d %b} → {day(DAYS):%d %b %Y} · dati simulati", 12, "start", "#94a3b8")
    s.text(920, 62, f"{REM_NOW:g}", 46, "end", "#38bdf8", "bold")
    s.text(920, 84, "punti rimanenti", 12, "end", "#94a3b8")
    s.text(920, 102, f"{DONE_NOW / SCOPE_NOW:.0%} completato", 12, "end", "#4ade80", "bold")
    ymax = (max(SCOPE_NOW, BASE) // 5 + 2) * 5
    pl = Plot(80, 130, 840, 330, ymax)
    grid(s, pl, ymax, "#1e293b", "#94a3b8", "date", every=3)
    xs, acts = [r[0] for r in ROWS], [r[3] for r in ROWS]
    s.poly(pl.P([(xs[0], 0)] + list(zip(xs, acts)) + [(xs[-1], 0)]), "#38bdf8", 0.16)
    s.poly(pl.P(scope_steps()), "none", stroke="#fbbf24", w=1.6, dash="5 4", closed=False)
    s.poly(pl.P([(0, BASE), (DAYS, 0)]), "none", stroke="#64748b", w=2, dash="8 6", closed=False)
    s.poly(pl.P(list(zip(xs, acts))), "none", stroke="#38bdf8", w=3.6, closed=False)
    s.circle(pl.X(xs[-1]), pl.Y(acts[-1]), 7, "#0b1220", "#38bdf8", 3)
    for e in events():
        if e[1] > 0:
            s.text(pl.X(e[0]), pl.Y(SCOPE_NOW) - 8, f"+{e[1]:g}", 11, color="#fbbf24", weight="bold")
    ly = 500
    for x, col, dash, txt in ((80, "#38bdf8", "", "rimanenti"), (200, "#64748b", "8 6", "ideale"),
                              (300, "#fbbf24", "5 4", "scope (totale assegnato)")):
        s.line(x, ly, x + 30, ly, col, 3, dash)
        s.text(x + 38, ly + 4, txt, 12, "start", "#cbd5e1")
    return s


# ---------------------------------------------------------------- D: task e ritmo
def variante_d():
    s = Svg(960, 640, "#ffffff")
    s.text(40, 40, f"Burndown · {TITLE}", 21, "start", "#111827", "bold")
    s.text(40, 60, "ogni gradino è un task chiuso: la discesa dipende dai suoi punti (dati simulati)", 12, "start", "#6b7280")
    ymax = (max(SCOPE_NOW, BASE) // 5 + 2) * 5
    pl = Plot(80, 90, 840, 330, ymax)
    grid(s, pl, ymax, "#eef2f7", "#6b7280", "date", every=3, show_days=False)
    s.poly(pl.P([(0, BASE), (DAYS, 0)]), "none", stroke="#9ca3af", w=2, dash="7 5", closed=False)
    s.poly(pl.P(step_points()), "none", stroke="#1d4ed8", w=3, closed=False)
    palette = {1: "#86efac", 2: "#5eead4", 3: "#7dd3fc", 5: "#a5b4fc", 8: "#d8b4fe"}
    stroke = {1: "#16a34a", 2: "#0d9488", 3: "#0284c7", 5: "#4f46e5", 8: "#9333ea"}
    cur = ROWS[0][3]
    placed = []
    for k, (x, d, name, p) in enumerate(events()):
        y_before, cur = cur, cur + d
        pw = int(p)
        cx, cy = pl.X(x), pl.Y((y_before + cur) / 2)
        while any(abs(cx - ox) < 70 and abs(cy - oy) < 23 for ox, oy in placed):
            cy += 24                       # sposta in basso se si sovrappone a un'altra etichetta
        placed.append((cx, cy))
        col = palette.get(pw, "#e5e7eb") if d < 0 else "#fde68a"
        sc = stroke.get(pw, "#6b7280") if d < 0 else "#d97706"
        s.rect(cx + 6, cy - 10, 62, 20, col, 10, sc, 1.2)
        s.text(cx + 37, cy + 4, f"{name} {'−' if d < 0 else '+'}{p:g}", 10, color="#111827", weight="bold")
    s.circle(pl.X(X_NOW), pl.Y(cur), 5, "#1d4ed8")
    # barre: punti completati per giorno
    by = 450
    bh = 90
    s.text(80, by - 6, "Punti completati al giorno", 12, "start", "#374151", "bold")
    perday = {}
    for x, d, _, p in events():
        if d < 0:
            perday[int(x)] = perday.get(int(x), 0) + p
    mx = max(perday.values())
    for dd in range(0, DAYS):
        v = perday.get(dd, 0)
        bw = pl.w / DAYS - 4
        h = bh * v / mx
        s.rect(pl.X(dd) + 2, by + bh - h, bw, max(h, 0.0001), "#93c5fd" if v else "#f1f5f9", 3)
        if v:
            s.text(pl.X(dd) + 2 + bw / 2, by + bh - h - 4, f"{v:g}", 10, color="#1e3a8a", weight="bold")
    s.line(pl.x0, by + bh, pl.x0 + pl.w, by + bh, "#9ca3af", 1)
    for dd in range(0, DAYS + 1, 3):
        s.text(pl.X(dd), by + bh + 16, f"{day(dd):%d/%m}", 10, color="#6b7280")
    # legenda taglie
    lx, ly = 80, 600
    s.text(lx, ly + 4, "Punti del task:", 11, "start", "#374151", "bold")
    for k, pw in enumerate((1, 2, 3, 5, 8)):
        x = lx + 110 + k * 70
        s.rect(x, ly - 8, 34, 18, palette[pw], 9, stroke[pw], 1.2)
        s.text(x + 17, ly + 5, str(pw), 10, color="#111827", weight="bold")
    s.rect(lx + 480, ly - 8, 34, 18, "#fde68a", 9, "#d97706", 1.2)
    s.text(lx + 522, ly + 5, "aggiunto a sprint iniziato", 11, "start", "#374151")
    return s


if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "varianti")
    for name, fn in (("A-stile-docente", variante_a), ("B-dashboard", variante_b),
                     ("C-scuro", variante_c), ("D-task-e-ritmo", variante_d)):
        fn().save(out, name)
        print("ok", name)
