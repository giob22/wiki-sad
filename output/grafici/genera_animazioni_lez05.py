"""Genera le animazioni SVG (SMIL) e il grafico della Lezione 5 (MVC, Spring MVC, Sense-Compute-Control).

Uso:  python genera_animazioni_lez05.py   (solo libreria standard)
Output nella stessa cartella dello script:
  anim-mvc-classico.svg, anim-spring-mvc-richiesta.svg, anim-sense-compute-control.svg,
  grafico-lunar-lander-controllo.svg
Le animazioni girano in loop dentro Obsidian (embed ![[file.svg]]).
"""
from pathlib import Path

OUT = Path(__file__).parent
FONT = "font-family='Segoe UI, Helvetica, Arial, sans-serif'"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def animazione(nome, titolo, w, h, nodi, passi, durata_passo=2.2, note=""):
    """nodi: {id: (x, y, w, h, etichetta, colore)}; passi: [(path_d, testo, colore)].
    Ogni passo: un pallino percorre il path; sotto compare la didascalia del passo."""
    N = len(passi)
    T = N * durata_passo + 1.5          # pausa finale prima di ripartire
    out = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w} {h + 70}' {FONT}>",
           f"<rect width='{w}' height='{h + 70}' fill='#ffffff'/>",
           f"<text x='{w/2}' y='26' text-anchor='middle' font-size='18' font-weight='700' fill='#1f2d3d'>{esc(titolo)}</text>",
           "<defs><marker id='a' viewBox='0 0 10 10' refX='9' refY='5' markerWidth='7' markerHeight='7' orient='auto-start-reverse'>"
           "<path d='M0,0 L10,5 L0,10 z' fill='#8a99a8'/></marker></defs>"]
    # percorsi statici (grigi)
    for d, _, _ in passi:
        out.append(f"<path d='{d}' fill='none' stroke='#c9d3dc' stroke-width='1.6' marker-end='url(#a)'/>")
    # nodi
    for x, y, bw, bh, lab, col in nodi.values():
        out.append(f"<rect x='{x}' y='{y}' width='{bw}' height='{bh}' rx='10' fill='{col}' stroke='#5b6b7b' stroke-width='1.2'/>")
        righe = lab.split("\n")
        for i, r in enumerate(righe):
            yy = y + bh / 2 + (i - (len(righe) - 1) / 2) * 16 + 5
            out.append(f"<text x='{x + bw/2}' y='{yy}' text-anchor='middle' font-size='14' font-weight='{700 if i == 0 else 400}' fill='#1f2d3d'>{esc(r)}</text>")
    # passi animati
    for i, (d, testo, col) in enumerate(passi):
        a, b = i * durata_passo / T, (i + 1) * durata_passo / T
        e = 0.002
        kt = f"0;{a:.4f};{b - e:.4f};1"
        op_kt = f"0;{a:.4f};{a + e:.4f};{b - e:.4f};{b:.4f};1"
        out.append(f"<path d='{d}' fill='none' stroke='{col}' stroke-width='3' opacity='0' marker-end='url(#a)'>"
                   f"<animate attributeName='opacity' dur='{T}s' repeatCount='indefinite' values='0;0;1;1;0.25;0.25' keyTimes='{op_kt}'/></path>")
        out.append(f"<circle r='8' fill='{col}' opacity='0'>"
                   f"<animateMotion dur='{T}s' repeatCount='indefinite' path='{d}' keyPoints='0;0;1;1' keyTimes='{kt}' calcMode='linear'/>"
                   f"<animate attributeName='opacity' dur='{T}s' repeatCount='indefinite' values='0;0;1;1;0;0' keyTimes='{op_kt}'/></circle>")
        out.append(f"<text x='{w/2}' y='{h + 30}' text-anchor='middle' font-size='15' fill='{col}' font-weight='600' opacity='0'>{i + 1}. {esc(testo)}"
                   f"<animate attributeName='opacity' dur='{T}s' repeatCount='indefinite' values='0;0;1;1;0;0' keyTimes='{op_kt}'/></text>")
    if note:
        out.append(f"<text x='{w/2}' y='{h + 58}' text-anchor='middle' font-size='12' fill='#6b7a89'>{esc(note)}</text>")
    out.append("</svg>")
    (OUT / nome).write_text("\n".join(out), encoding="utf-8")


# 1) MVC classico (osservatore) — prenotazione di una sessione d'esame, slide 44 e 48
animazione(
    "anim-mvc-classico.svg", "MVC classico — prenotare una sessione d'esame", 760, 360,
    {"S": (20, 150, 110, 60, "Student", "#e8edf3"),
     "V": (210, 60, 190, 70, "View\nExam Booking UI", "#dbeefb"),
     "C": (210, 240, 190, 70, "Controller\nBooking Controller", "#ece3f7"),
     "M": (530, 140, 200, 90, "Model\nExam Booking Domain", "#e3f3e6")},
    [("M130,165 L208,105", "lo studente seleziona una sessione (evento sulla View)", "#2f6fa8"),
     ("M305,130 L305,238", "la View delega l'input: bookExam(sessionId)  [Strategy]", "#7a4ea8"),
     ("M400,275 L528,205", "il Controller invoca il Model: createBooking(...)", "#7a4ea8"),
     ("M528,160 L402,100", "il Model notifica il cambiamento alle View iscritte  [Observer]", "#3b8a4a"),
     ("M402,115 L528,175", "la View legge lo stato aggiornato dal Model (pull)", "#2f6fa8"),
     ("M208,120 L132,190", "la View mostra il risultato allo studente", "#3b8a4a")],
    note="Il Model non conosce la View concreta: pubblica un evento (notify, then pull)")

# 2) Spring MVC — requisito ShowExamSessions, slide 67
animazione(
    "anim-spring-mvc-richiesta.svg", "Spring MVC — GET /exam-sessions", 900, 400,
    {"B": (20, 40, 130, 56, "Browser", "#e8edf3"),
     "D": (250, 40, 190, 56, "DispatcherServlet\n(Front Controller)", "#dbeefb"),
     "H": (560, 40, 160, 56, "HandlerMapping", "#f2f4f6"),
     "C": (250, 180, 190, 56, "ExamSession\nController", "#ece3f7"),
     "S": (560, 180, 170, 56, "ExamSession\nService", "#e3f3e6"),
     "R": (250, 310, 190, 56, "ViewResolver", "#f2f4f6"),
     "T": (560, 310, 170, 56, "Thymeleaf View", "#fdf0d9")},
    [("M150,68 L248,68", "il browser invia GET /exam-sessions", "#2f6fa8"),
     ("M440,60 L558,60", "il DispatcherServlet chiede l'handler", "#2f6fa8"),
     ("M558,78 L442,78", "HandlerMapping: metodo listAvailableSessions()", "#6b7a89"),
     ("M345,96 L345,178", "il DispatcherServlet invoca il Controller", "#7a4ea8"),
     ("M440,200 L558,200", "il Controller chiama findAvailableSessions()", "#7a4ea8"),
     ("M558,218 L442,218", "il Service restituisce la lista delle sessioni", "#3b8a4a"),
     ("M330,178 L330,98", "il Controller restituisce \"exam-sessions\" + Model", "#7a4ea8"),
     ("M260,96 C200,200 200,250 255,308", "il DispatcherServlet chiede di risolvere \"exam-sessions\"", "#b07a1a"),
     ("M440,350 C500,370 500,370 558,350", "la vista trovata: il template exam-sessions.html", "#b07a1a"),
     ("M645,308 C700,200 520,140 442,90", "il template riceve il Model e genera l'HTML", "#c26a1a"),
     ("M248,82 L152,82", "il DispatcherServlet invia la risposta HTTP", "#3b8a4a")],
    note="Il Controller non genera l'HTML: restituisce un nome logico di vista e i dati")

# 3) Sense-Compute-Control — variante a quattro stadi (slide 88), esempio antintrusione (slide 86)
animazione(
    "anim-sense-compute-control.svg", "Sense–Compute–Control: il ciclo di controllo", 900, 300,
    {"E": (20, 110, 140, 70, "Ambiente\nesterno", "#e8edf3"),
     "S": (200, 40, 140, 60, "Sensing\nsensori di movimento", "#dbeefb"),
     "P": (380, 40, 160, 60, "Context processing\npossibile intrusione?", "#e3f3e6"),
     "L": (580, 40, 140, 60, "Control logic\ndecidere l'azione", "#ece3f7"),
     "A": (740, 160, 140, 60, "Actuation\nallarme / notifica", "#fdf0d9")},
    [("M160,130 L198,80", "l'ambiente produce fenomeni fisici (movimento)", "#6b7a89"),
     ("M340,70 L378,70", "SENSE: i sensori inviano i dati grezzi", "#2f6fa8"),
     ("M540,70 L578,70", "COMPUTE: il contesto stimato (intrusione: sì/no)", "#3b8a4a"),
     ("M720,85 L800,158", "CONTROL: comando agli attuatori", "#7a4ea8"),
     ("M740,200 C500,280 300,260 160,170", "gli attuatori cambiano l'ambiente → il ciclo riparte", "#c26a1a")],
    durata_passo=2.4,
    note="Variante a 4 stadi: l'interpretazione del contesto è separata dalla decisione di controllo")


# 4) Grafico: Lunar Lander con e senza ciclo di controllo (elaborazione mia, slide 92-94)
def simula(controllo, h0=1000.0, v0=-50.0, g=5.32, a_max=16.0, dt=0.05, t_max=120.0):
    """Unità della slide: piedi e secondi. g lunare ≈ 1.62 m/s² ≈ 5.32 ft/s².
    controllo: legge che dalla misura (h, v) calcola la spinta (accelerazione verso l'alto)."""
    h, v, t, fuel = h0, v0, 0.0, 0.0
    T, H, V = [0.0], [h], [v]
    while h > 0 and t < t_max:
        a = controllo(h, v) if controllo else 0.0          # SENSE (h, v) -> COMPUTE (a)
        a = max(0.0, min(a_max, a))                         # CONTROL: limiti del motore
        fuel += a * dt
        v += (a - g) * dt                                   # ambiente: gravità + spinta
        h += v * dt
        t += dt
        T.append(t); H.append(max(h, 0)); V.append(v)
    return T, H, V, fuel


def legge(h, v, g=5.32, k=0.8):
    v_ref = -max(3.0, 0.08 * h)          # scendere più piano man mano che ci si avvicina al suolo
    return g + k * (v_ref - v)           # compensa la gravità + correzione proporzionale


Tc, Hc, Vc, fuel = simula(legge)
Tf, Hf, Vf, _ = simula(None)


def grafico(nome):
    W, H = 900, 420
    pad_l, pad_r, pad_t, pad_b = 60, 20, 50, 90
    pw = (W - pad_l - pad_r - 70) / 2
    ph = H - pad_t - pad_b
    tmax = max(Tc[-1], Tf[-1])
    out = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' {FONT}>",
           f"<rect width='{W}' height='{H}' fill='#fff'/>",
           f"<text x='{W/2}' y='24' text-anchor='middle' font-size='16' font-weight='700' fill='#1f2d3d'>Lunar Lander — discesa con e senza il ciclo Sense–Compute–Control</text>"]

    def pannello(x0, ys_c, ys_f, ymin, ymax, titolo, ylab, soglia=None):
        sx = lambda t: x0 + t / tmax * pw
        sy = lambda y: pad_t + (ymax - y) / (ymax - ymin) * ph
        o = [f"<rect x='{x0}' y='{pad_t}' width='{pw}' height='{ph}' fill='none' stroke='#9aa7b3'/>",
             f"<text x='{x0 + pw/2}' y='{pad_t - 8}' text-anchor='middle' font-size='13' fill='#1f2d3d'>{titolo}</text>",
             f"<text x='{x0 + pw/2}' y='{pad_t + ph + 32}' text-anchor='middle' font-size='12' fill='#55606b'>tempo [s]</text>",
             f"<text x='{x0 - 42}' y='{pad_t + ph/2}' font-size='12' fill='#55606b' transform='rotate(-90 {x0 - 42} {pad_t + ph/2})' text-anchor='middle'>{ylab}</text>"]
        for k in range(6):
            yv = ymin + k * (ymax - ymin) / 5
            o.append(f"<text x='{x0 - 6}' y='{sy(yv) + 4}' text-anchor='end' font-size='10' fill='#55606b'>{yv:.0f}</text>")
            o.append(f"<line x1='{x0}' x2='{x0 + pw}' y1='{sy(yv)}' y2='{sy(yv)}' stroke='#eef1f4'/>")
        for k in range(0, int(tmax) + 1, 20):
            o.append(f"<text x='{sx(k)}' y='{pad_t + ph + 14}' text-anchor='middle' font-size='10' fill='#55606b'>{k}</text>")
        if soglia is not None:
            o.append(f"<line x1='{x0}' x2='{x0 + pw}' y1='{sy(soglia)}' y2='{sy(soglia)}' stroke='#c0392b' stroke-dasharray='5 4'/>")
            o.append(f"<text x='{x0 + pw - 4}' y='{sy(soglia) - 5}' text-anchor='end' font-size='10' fill='#c0392b'>−5 ft/s: soglia per atterrare</text>")
        pts = lambda T, Y: " ".join(f"{sx(t):.1f},{sy(y):.1f}" for t, y in zip(T, Y))
        o.append(f"<polyline points='{pts(Tf, ys_f)}' fill='none' stroke='#9aa7b3' stroke-width='2' stroke-dasharray='6 4'/>")
        o.append(f"<polyline points='{pts(Tc, ys_c)}' fill='none' stroke='#2f6fa8' stroke-width='2.5'/>")
        return o

    out += pannello(pad_l, Hc, Hf, 0, 1000, "quota", "quota [ft]")
    vmin = min(min(Vc), min(Vf))
    out += pannello(pad_l + pw + 70, Vc, Vf, (vmin // 20) * 20, 0, "velocità verticale", "velocità [ft/s]", soglia=-5)
    out.append(f"<line x1='{pad_l}' x2='{pad_l + 30}' y1='{H - 18}' y2='{H - 18}' stroke='#2f6fa8' stroke-width='2.5'/>"
               f"<text x='{pad_l + 36}' y='{H - 14}' font-size='11' fill='#1f2d3d'>con controllo: tocca il suolo a {Vc[-1]:.1f} ft/s dopo {Tc[-1]:.0f} s</text>")
    out.append(f"<line x1='{pad_l + 400}' x2='{pad_l + 430}' y1='{H - 18}' y2='{H - 18}' stroke='#9aa7b3' stroke-width='2' stroke-dasharray='6 4'/>"
               f"<text x='{pad_l + 436}' y='{H - 14}' font-size='11' fill='#1f2d3d'>motore spento: impatto a {Vf[-1]:.0f} ft/s dopo {Tf[-1]:.0f} s</text>")
    out.append("</svg>")
    (OUT / nome).write_text("\n".join(out), encoding="utf-8")


grafico("grafico-lunar-lander-controllo.svg")
print(f"con controllo: t={Tc[-1]:.1f}s v={Vc[-1]:.2f}ft/s  | senza: t={Tf[-1]:.1f}s v={Vf[-1]:.1f}ft/s")
