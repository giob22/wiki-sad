"""Genera l'animazione e il grafico della Lezione 6 (Agile Project Management).

Uso:  python genera_grafici_lez06.py   (solo libreria standard)
Output nella stessa cartella:
  anim-ciclo-iterazione-agile.svg  — il ciclo backlog → planning → iterazione → demo → retrospettiva (slide 13–15, 23–27)
  grafico-burndown-sprint.svg      — burndown di uno sprint di 15 giorni con cambio di ambito (slide 31)
"""
from pathlib import Path

OUT = Path(__file__).parent
FONT = "font-family='Segoe UI, Helvetica, Arial, sans-serif'"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def animazione(nome, titolo, w, h, nodi, passi, durata_passo=2.4, note=""):
    """Stesso schema delle animazioni della Lez. 5: un pallino percorre ogni passo, con didascalia."""
    N = len(passi)
    T = N * durata_passo + 1.5
    out = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w} {h + 70}' {FONT}>",
           f"<rect width='{w}' height='{h + 70}' fill='#ffffff'/>",
           f"<text x='{w/2}' y='26' text-anchor='middle' font-size='18' font-weight='700' fill='#1f2d3d'>{esc(titolo)}</text>",
           "<defs><marker id='a' viewBox='0 0 10 10' refX='9' refY='5' markerWidth='7' markerHeight='7' orient='auto-start-reverse'>"
           "<path d='M0,0 L10,5 L0,10 z' fill='#8a99a8'/></marker></defs>"]
    for d, _, _ in passi:
        out.append(f"<path d='{d}' fill='none' stroke='#c9d3dc' stroke-width='1.6' marker-end='url(#a)'/>")
    for x, y, bw, bh, lab, col in nodi.values():
        out.append(f"<rect x='{x}' y='{y}' width='{bw}' height='{bh}' rx='10' fill='{col}' stroke='#5b6b7b' stroke-width='1.2'/>")
        righe = lab.split("\n")
        for i, r in enumerate(righe):
            yy = y + bh / 2 + (i - (len(righe) - 1) / 2) * 16 + 5
            out.append(f"<text x='{x + bw/2}' y='{yy}' text-anchor='middle' font-size='13' font-weight='{700 if i == 0 else 400}' fill='#1f2d3d'>{esc(r)}</text>")
    for i, (d, testo, col) in enumerate(passi):
        a, b, e = i * durata_passo / T, (i + 1) * durata_passo / T, 0.002
        kt = f"0;{a:.4f};{b - e:.4f};1"
        op = f"0;{a:.4f};{a + e:.4f};{b - e:.4f};{b:.4f};1"
        out.append(f"<path d='{d}' fill='none' stroke='{col}' stroke-width='3' opacity='0' marker-end='url(#a)'>"
                   f"<animate attributeName='opacity' dur='{T}s' repeatCount='indefinite' values='0;0;1;1;0.25;0.25' keyTimes='{op}'/></path>")
        out.append(f"<circle r='8' fill='{col}' opacity='0'>"
                   f"<animateMotion dur='{T}s' repeatCount='indefinite' path='{d}' keyPoints='0;0;1;1' keyTimes='{kt}' calcMode='linear'/>"
                   f"<animate attributeName='opacity' dur='{T}s' repeatCount='indefinite' values='0;0;1;1;0;0' keyTimes='{op}'/></circle>")
        out.append(f"<text x='{w/2}' y='{h + 30}' text-anchor='middle' font-size='15' fill='{col}' font-weight='600' opacity='0'>{i + 1}. {esc(testo)}"
                   f"<animate attributeName='opacity' dur='{T}s' repeatCount='indefinite' values='0;0;1;1;0;0' keyTimes='{op}'/></text>")
    if note:
        out.append(f"<text x='{w/2}' y='{h + 58}' text-anchor='middle' font-size='12' fill='#6b7a89'>{esc(note)}</text>")
    out.append("</svg>")
    (OUT / nome).write_text("\n".join(out), encoding="utf-8")


animazione(
    "anim-ciclo-iterazione-agile.svg", "Il ciclo di un'iterazione Agile", 900, 330,
    {"PB": (20, 120, 150, 60, "Product Backlog\nordinato per priorità", "#fdf0d9"),
     "IP": (220, 120, 150, 60, "Iteration Planning\nobiettivo + storie", "#dbeefb"),
     "IB": (420, 50, 150, 60, "Iteration Backlog\nstorie → task", "#e3f3e6"),
     "DM": (620, 50, 150, 60, "Daily meeting\n15 min ogni giorno", "#ece3f7"),
     "DE": (620, 210, 150, 60, "Iteration Demo\nincremento + feedback", "#e3f3e6"),
     "RE": (420, 210, 150, 60, "Retrospective\nmigliorare il processo", "#f2f4f6")},
    [("M170,150 L218,150", "il PO ordina il Product Backlog per priorità (valore)", "#b07a1a"),
     ("M370,140 L418,90", "Iteration Planning: si scelgono le storie e l'obiettivo", "#2f6fa8"),
     ("M570,80 L618,80", "il team lavora; ogni giorno il daily meeting allinea il lavoro", "#7a4ea8"),
     ("M695,110 L695,208", "fine iterazione: software funzionante, integrato e testato", "#3b8a4a"),
     ("M618,240 L572,240", "Demo agli stakeholder: si raccoglie il feedback", "#3b8a4a"),
     ("M420,250 C250,320 100,280 95,182", "Retrospettiva + feedback aggiornano il backlog → nuova iterazione", "#c26a1a")],
    note="Backlog → Priority → Iteration → Feedback → Improvement (slide 13): niente «big bang», piccoli incrementi di valore")


def burndown(nome):
    """Burndown di uno sprint di 15 giorni con 70 Story Point e aggiunta di 7 SP al giorno 8.
    Valori illustrativi, costruiti sulla forma della figura di slide 31."""
    giorni = list(range(1, 16))
    ambito = [70] * 7 + [77] * 8                     # linea blu: ambito dello sprint (con la modifica)
    reale = [70, 62, 55, 55, 50, 50, 38, 44, 38, 30, 30, 21, 13, 5, 0]   # linea viola: lavoro rimanente
    ideale = [70 - 70 * (g - 1) / 14 for g in giorni]   # linea tratteggiata: da 70 a 0 in 14 intervalli
    W, H, l, r, t, b = 900, 430, 70, 230, 50, 60
    pw, ph = W - l - r, H - t - b
    sx = lambda g: l + (g - 1) / 14 * pw
    sy = lambda v: t + (85 - v) / 85 * ph
    o = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' {FONT}>",
         f"<rect width='{W}' height='{H}' fill='#fff'/>",
         f"<text x='{l + pw/2}' y='26' text-anchor='middle' font-size='16' font-weight='700' fill='#1f2d3d'>Burndown chart di uno sprint di 15 giorni</text>",
         f"<rect x='{l}' y='{t}' width='{pw}' height='{ph}' fill='none' stroke='#9aa7b3'/>"]
    for v in range(0, 81, 10):
        o.append(f"<line x1='{l}' x2='{l + pw}' y1='{sy(v)}' y2='{sy(v)}' stroke='#eef1f4'/>"
                 f"<text x='{l - 8}' y='{sy(v) + 4}' text-anchor='end' font-size='11' fill='#55606b'>{v}</text>")
    for g in giorni:
        o.append(f"<text x='{sx(g)}' y='{t + ph + 16}' text-anchor='middle' font-size='11' fill='#55606b'>{g}</text>")
    o.append(f"<text x='{l + pw/2}' y='{H - 14}' text-anchor='middle' font-size='12' fill='#55606b'>giorno dello sprint</text>")
    o.append(f"<text x='{l - 45}' y='{t + ph/2}' font-size='12' fill='#55606b' text-anchor='middle' transform='rotate(-90 {l - 45} {t + ph/2})'>Story Point rimanenti</text>")
    pts = lambda ys: " ".join(f"{sx(g):.1f},{sy(v):.1f}" for g, v in zip(giorni, ys))
    o.append(f"<polyline points='{pts(ambito)}' fill='none' stroke='#2f6fa8' stroke-width='2.5'/>")
    o.append(f"<polyline points='{pts(ideale)}' fill='none' stroke='#6b7a89' stroke-width='2' stroke-dasharray='6 5'/>")
    o.append(f"<polyline points='{pts(reale)}' fill='none' stroke='#8e2c8a' stroke-width='3'/>")
    for g, v in zip(giorni, reale):
        o.append(f"<circle cx='{sx(g):.1f}' cy='{sy(v):.1f}' r='3.5' fill='#8e2c8a'/>")
    # annotazioni
    o.append(f"<text x='{sx(8) + 6}' y='{sy(77) - 8}' font-size='11' fill='#2f6fa8'>giorno 8: +7 SP aggiunti all'ambito</text>")
    o.append(f"<text x='{sx(8) + 6}' y='{sy(44) - 10}' font-size='11' fill='#8e2c8a'>il lavoro rimanente risale</text>")
    o.append(f"<text x='{sx(4)}' y='{sy(55) - 10}' font-size='11' fill='#8e2c8a' text-anchor='middle'>piatto: nessuna storia chiusa</text>")
    lx = l + pw + 15
    for i, (col, dash, txt) in enumerate([("#6b7a89", "6 5", "progresso ideale"), ("#8e2c8a", "", "progresso reale"), ("#2f6fa8", "", "ambito dello sprint")]):
        y = t + 20 + i * 24
        o.append(f"<line x1='{lx}' x2='{lx + 28}' y1='{y}' y2='{y}' stroke='{col}' stroke-width='3' stroke-dasharray='{dash}'/>"
                 f"<text x='{lx + 34}' y='{y + 4}' font-size='12' fill='#1f2d3d'>{txt}</text>")
    o.append(f"<text x='{lx}' y='{t + 110}' font-size='11' fill='#55606b'>sopra la linea ideale = in ritardo</text>")
    o.append(f"<text x='{lx}' y='{t + 126}' font-size='11' fill='#55606b'>sotto la linea ideale = in anticipo</text>")
    o.append("</svg>")
    (OUT / nome).write_text("\n".join(o), encoding="utf-8")


burndown("grafico-burndown-sprint.svg")
print("ok")
