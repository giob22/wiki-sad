#!/usr/bin/env python3
"""Animazione fluida della mascotte (pinguino con elmetto e fragola) da una tavola 5x5 di frame.

Uso:  python genera_animazione_pinguino.py <tavola.webp> <cartella-di-output> [--frame]
      (--frame salva anche i 25 frame allineati come PNG trasparenti;
       --solo-estesa genera soltanto la versione estesa;
       --costruzione genera la versione con la casetta e la fragola ferma, con --anteprima solo un foglio di controllo)

Cosa fa
  1. ritaglia i 25 frame dalla tavola (sfondo già trasparente) e li allinea sui piedi;
  2. crea i fotogrammi intermedi con il flusso ottico (DIS), usando UN solo frame deformato per volta,
     per evitare la doppia immagine; il flusso è smussato per non strappare i contorni;
  3. ritmo da animatore: pose tenute sugli impatti, accelerazione sulla martellata, rallentamento sulle pose;
  4. gesti extra ottenuti dalle pose esistenti con squash & stretch, rotazioni e ombra a terra.
Dipendenze: numpy, pillow, opencv-python (headless).
"""
import math
import os
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

SC = int(os.environ.get("PINGUINO_SC", "2"))   # ingrandimento dell'output rispetto ai frame originali
SIGMA = 8         # smussamento del flusso (più alto = deformazioni più morbide)
BASE_MS = 30      # durata di un fotogramma intermedio (circa 33 fps)
GIF_SCALE = 1.5   # dimensione della GIF rispetto ai frame originali (il WebP usa SC)

# ------------------------------------------------------------------ 1. ritaglio e allineamento


def carica_frame(percorso):
    sheet = np.array(Image.open(percorso).convert("RGBA"))
    mask = (sheet[..., 3] > 8).astype(np.uint8)
    d = cv2.dilate(mask, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
    n, lab, st, cen = cv2.connectedComponentsWithStats(d, connectivity=8)
    gruppi = [i for i in range(1, n) if st[i][4] > 3000]
    if len(gruppi) != 25:
        raise SystemExit(f"Trovati {len(gruppi)} frame invece di 25: controlla la tavola")
    per_riga = sorted(gruppi, key=lambda i: cen[i][1])
    ordine = [g for r in range(5) for g in sorted(per_riga[r * 5:(r + 1) * 5], key=lambda i: cen[i][0])]
    frames = []
    for g in ordine:
        x, y, w, h, _ = st[g]
        crop = sheet[y:y + h, x:x + w].copy()
        crop[~(lab[y:y + h, x:x + w] == g)] = 0
        yy, xx = np.nonzero(crop[..., 3] > 8)
        frames.append(crop[yy.min():yy.max() + 1, xx.min():xx.max() + 1])
    return frames


def classi(f):
    r, g, b, a = [f[..., i].astype(int) for i in range(4)]
    op = a > 200
    rosso = op & (r > 170) & (g < 120) & (b < 120)
    foglia = op & (g > r + 20) & (g > b + 10) & (g > 90)
    grigio = op & (np.abs(r - g) < 22) & (np.abs(g - b) < 28) & (r > 105) & (r < 232)
    azzurro = op & (b > r + 50) & (b > 140)
    giallo = op & (r > 200) & (g > 150) & (g < 238) & (b < 125)
    return op, rosso, foglia, grigio, azzurro, giallo


def ancora(f):
    """Punto di appoggio: x = centro della parte bassa del corpo (senza fragola né martello), y = fondo dei piedi."""
    h = f.shape[0]
    op, rosso, foglia, grigio, azzurro, giallo = classi(f)
    peng = op & ~rosso & ~foglia & ~grigio & ~azzurro
    ys, _ = np.nonzero(giallo)
    basso = ys > h * 0.70
    fy = int(ys[basso].max()) if basso.sum() > 30 else h - 12
    fascia = np.zeros_like(peng)
    fascia[max(0, fy - 62):fy + 2, :] = True
    _, px = np.nonzero(peng & fascia)
    return float(px.mean()), fy


def allinea(frames, margine=6):
    ancore = [ancora(f) for f in frames]
    L = max(int(round(a[0])) for a in ancore) + margine
    R = max(f.shape[1] - int(round(a[0])) for f, a in zip(frames, ancore)) + margine
    T = max(a[1] for a in ancore) + margine
    B = max(f.shape[0] - a[1] for f, a in zip(frames, ancore)) + margine
    out = []
    for f, a in zip(frames, ancore):
        cv = np.zeros((T + B, L + R, 4), np.uint8)
        ox, oy = L - int(round(a[0])), T - a[1]
        cv[oy:oy + f.shape[0], ox:ox + f.shape[1]] = f
        out.append(cv)
    return out, (L, T)


# ------------------------------------------------------------------ 2. fotogrammi intermedi


def premult(f, scala=1):
    a = f[..., 3:4].astype(np.float32) / 255.0
    p = np.concatenate([f[..., :3].astype(np.float32) / 255.0 * a, a], axis=2)
    if scala != 1:
        p = cv2.resize(p, None, fx=scala, fy=scala, interpolation=cv2.INTER_LANCZOS4)
        p = np.clip(p, 0, 1)
        p[..., :3] = np.minimum(p[..., :3], p[..., 3:4])
    return p


def a_rgba(p):
    a = np.clip(p[..., 3], 0, 1)
    rgb = np.where(a[..., None] > 1e-3, p[..., :3] / np.maximum(a[..., None], 1e-3), 0)
    return np.dstack([np.clip(rgb, 0, 1) * 255, a * 255]).astype(np.uint8)


def flusso(a, b):
    def grigio(p):
        x = np.clip(p[..., :3] + (1 - p[..., 3:4]) * 0.5, 0, 1)
        return cv2.cvtColor((x * 255).astype(np.uint8), cv2.COLOR_RGB2GRAY)
    d = cv2.DISOpticalFlow_create(cv2.DISOPTICAL_FLOW_PRESET_MEDIUM)
    f = d.calc(grigio(a), grigio(b), None)
    return cv2.GaussianBlur(f, (0, 0), SIGMA)


def deforma(img, fl):
    h, w = img.shape[:2]
    gx, gy = np.meshgrid(np.arange(w, dtype=np.float32), np.arange(h, dtype=np.float32))
    return cv2.remap(img, gx + fl[..., 0], gy + fl[..., 1], cv2.INTER_LINEAR,
                     borderMode=cv2.BORDER_CONSTANT, borderValue=0)


def intermedio(p0, p1, t, f01, f10):
    """Frame a tempo t (0..1) da UN solo frame deformato: fino a metà dal primo, poi dal secondo."""
    if t < 0.5:
        return deforma(p0, -t * f01)
    return deforma(p1, -(1 - t) * f10)


def curva(tipo, u):
    return {"io": u * u * (3 - 2 * u), "in": u * u, "out": 1 - (1 - u) ** 2, "lin": u}[tipo]


# Coppie (frame i -> i+1, numeri da 1): (intermedi, curva). Le altre: 3 intermedi con "io", oppure 2 sulle
# coppie dove il flusso ottico è meno affidabile (deformano al massimo di ~1/4 e non strappano il viso).
COPPIE_DIFFICILI = {(1, 2), (2, 3), (4, 5), (5, 6), (7, 8), (11, 12), (15, 16), (16, 17), (18, 19), (19, 20),
                    (21, 22), (22, 23)}
TOT_COPPIA_MS = 120   # tempo di ogni passaggio tra due pose, qualunque sia il numero di intermedi
REGOLE = {
    (9, 10): (3, "in"), (10, 11): (1, "in"), (13, 14): (3, "in"), (14, 15): (1, "in"),
    (12, 13): (2, "io"), (23, 24): (1, "io"), (24, 25): (1, "io"), (25, 1): (1, "lin"),
}
# pose tenute (millisecondi aggiunti)
TENUTE = {1: 240, 5: 120, 6: 60, 12: 60, 13: 90, 11: 150, 15: 150, 18: 120, 19: 120, 23: 120}


def regola(i, j):
    """(numero di intermedi, curva) per il passaggio dal frame i al frame j (numeri da 1)."""
    return REGOLE.get((i, j), (2 if (i, j) in COPPIE_DIFFICILI else 3, "io"))


def sequenza_fluida(P2, F, tenute=TENUTE):
    """Lista di (frame premoltiplicato, durata ms) per il ciclo completo 1 -> ... -> 25 -> 1."""
    seq = []
    for i in range(25):
        j = (i + 1) % 25
        n, tipo = regola(i + 1, j + 1)
        passo = int(round(TOT_COPPIA_MS / (n + 1)))
        if (i + 1, j + 1) in ((10, 11), (14, 15)):      # gli impatti arrivano in fretta
            passo = 40
        seq.append((P2[i], passo + tenute.get(i + 1, 0)))
        f01, f10 = F[(i, j)]
        for k in range(1, n + 1):
            t = curva(tipo, k / (n + 1))
            seq.append((intermedio(P2[i], P2[j], t, f01, f10), passo))
    return seq


def sequenza_originale(P2, ms=83, tenute=TENUTE):
    return [(P2[i], ms + tenute.get(i + 1, 0)) for i in range(25)]


# ------------------------------------------------------------------ 3. gesti extra


def trasforma(p, perno, sx=1.0, sy=1.0, rot=0.0, dx=0.0, dy=0.0):
    """Scala e ruota attorno al perno (i piedi), poi sposta. p premoltiplicato RGBA float."""
    px, py = perno
    c, s = math.cos(math.radians(rot)), math.sin(math.radians(rot))
    M = np.array([[c * sx, -s * sy, 0], [s * sx, c * sy, 0]], np.float32)
    M[:, 2] = [px - (M[0, 0] * px + M[0, 1] * py) + dx, py - (M[1, 0] * px + M[1, 1] * py) + dy]
    return cv2.warpAffine(p, M, (p.shape[1], p.shape[0]), flags=cv2.INTER_CUBIC,
                          borderMode=cv2.BORDER_CONSTANT, borderValue=0)


def ombra(shape, perno, scala=1.0, alpha=0.28):
    h, w = shape[:2]
    layer = np.zeros((h, w), np.float32)
    cv2.ellipse(layer, (int(perno[0]), int(perno[1] + 3 * SC)), (int(52 * SC * scala), int(8 * SC * scala)),
                0, 0, 360, 1.0, -1, cv2.LINE_AA)
    layer = cv2.GaussianBlur(layer, (0, 0), 2.5 * SC) * alpha
    out = np.zeros((h, w, 4), np.float32)
    out[..., 3] = layer
    return out


def sopra(fg, bg):
    return fg + bg * (1 - fg[..., 3:4])


def amplia(p, sopra_px, lati_px):
    return np.pad(p, ((sopra_px, 0), (lati_px, lati_px), (0, 0)))


def gesto_salto(base, perno, n=40, ms=BASE_MS, altezza_px=70, alpha0=0.30, con_ombra=True):
    """Salto di gioia: schiaccia, stira, vola, atterra con rimbalzo. Usa la posa 23 (occhi felici)."""
    altezza = altezza_px * SC
    out = []
    for k in range(n):
        u = k / (n - 1)
        sx = sy = 1.0
        h = 0.0
        rot = 0.0
        if u < 0.16:                                   # anticipazione: si abbassa
            e = curva("io", u / 0.16)
            sy, sx = 1 - 0.14 * e, 1 + 0.10 * e
        elif u < 0.24:                                 # spinta: si stira
            e = curva("out", (u - 0.16) / 0.08)
            sy, sx = 0.86 + 0.28 * e, 1.10 - 0.18 * e
        elif u < 0.62:                                 # in volo
            a = (u - 0.24) / 0.38
            h = altezza * 4 * a * (1 - a)
            sy, sx = 1.0 + 0.10 * (1 - a) * (1 - a) - 0.04 * a, 1.0 - 0.06 * (1 - a) * (1 - a) + 0.03 * a
            rot = 5 * math.sin(a * math.pi * 2)
        elif u < 0.72:                                 # atterraggio: schiaccia
            e = curva("out", (u - 0.62) / 0.10)
            sy, sx = 1.0 - 0.16 * e, 1.0 + 0.12 * e
        else:                                          # rimbalzo smorzato
            a = (u - 0.72) / 0.28
            osc = math.exp(-4 * a) * math.cos(a * math.pi * 3.2)
            sy, sx = 1.0 - 0.10 * osc, 1.0 + 0.07 * osc
        spr = trasforma(base, perno, sx, sy, rot, 0, -h)
        if con_ombra:
            spr = sopra(spr, ombra(base.shape, perno, 1 - 0.35 * h / altezza, alpha0 * (1 - 0.4 * h / altezza)))
        out.append((spr, ms))
    return out


def gesto_dondolio(base, perno, n=36, ms=40, con_ombra=True):
    out = []
    for k in range(n):
        a = 2 * math.pi * k / n
        spr = trasforma(base, perno, 1 + 0.012 * math.sin(2 * a), 1 - 0.012 * math.sin(2 * a),
                        3.2 * math.sin(a), 2 * SC * math.sin(a), 0)
        out.append((sopra(spr, ombra(base.shape, perno, 1.0, 0.22)) if con_ombra else spr, ms))
    return out


def gesto_respiro(base, perno, n=40, ms=48, con_ombra=True):
    out = []
    for k in range(n):
        a = 2 * math.pi * k / n
        spr = trasforma(base, perno, 1 - 0.010 * math.sin(a), 1 + 0.022 * math.sin(a), 0.6 * math.sin(a), 0, 0)
        out.append((sopra(spr, ombra(base.shape, perno, 1.0, 0.22)) if con_ombra else spr, ms))
    return out


def gesto_si(base, perno, n=40, ms=BASE_MS, con_ombra=True):
    """Annuisce due volte (posa 18: sorride con il martello alla cintura)."""
    out = []
    for k in range(n):
        u = k / n
        a = max(0.0, math.sin(u * 2 * math.pi * 2)) if u < 0.8 else 0.0
        spr = trasforma(base, perno, 1 + 0.030 * a, 1 - 0.055 * a, 0, 0, 0)
        out.append((sopra(spr, ombra(base.shape, perno, 1.0, 0.22)) if con_ombra else spr, ms))
    return out


def gesto_martello(P2, F, perno, giri=3):
    """Martellata ripetuta: 12 -> 13 (alza) -> 14 (cala) -> 15 (impatto, scossa) e ritorno lento."""
    i12, i13, i14, i15 = 11, 12, 13, 14
    percorso = []

    def tratta(a, b, n, tipo, inverso=False):
        f01, f10 = F[(a, b)] if (a, b) in F else (None, None)
        res = []
        for k in range(1, n + 1):
            t = curva(tipo, k / (n + 1))
            res.append(intermedio(P2[a], P2[b], t, f01, f10))
        return res

    f_a = []
    f_a += [(P2[i12], 150)]
    f_a += [(x, BASE_MS) for x in tratta(i12, i13, 3, "io")]
    f_a += [(P2[i13], 170)]                                      # anticipazione: tiene il martello alto
    f_a += [(x, BASE_MS) for x in tratta(i13, i14, 3, "in")]
    f_a += [(P2[i14], BASE_MS)]
    f_a += [(x, BASE_MS) for x in tratta(i14, i15, 1, "in")]
    impatto = [(P2[i15], BASE_MS)]
    # scossa e schiacciamento all'impatto
    scosse = [(1.0, 0.98, -3), (1.0, 0.99, 3), (1.0, 0.995, -2), (1.0, 1.0, 1), (1.0, 1.0, 0)]
    for sx, sy, dx in scosse:
        impatto.append((trasforma(P2[i15], perno, 1 / sy ** 0.5, sy, 0, dx * SC * 0.5, 0), BASE_MS + 10))
    f_a += impatto
    f_a += [(P2[i15], 140)]
    ritorno = [(x, BASE_MS + 14) for x in tratta(i14, i15, 5, "io")][::-1]
    ritorno += [(x, BASE_MS + 14) for x in tratta(i13, i14, 5, "io")][::-1]
    ritorno += [(x, BASE_MS + 10) for x in tratta(i12, i13, 3, "io")][::-1]
    ciclo = f_a + ritorno
    return ciclo * giri


# ------------------------------------------------------------------ 3b. versione estesa (più lunga e più fluida)

TOT_EST = 140        # ms per passare da una posa alla successiva: con 6 intermedi sono 20 ms l'uno (50 fps)
REGOLE_EST = {(9, 10): (4, "in"), (13, 14): (4, "in"), (12, 13): (4, "io"), (10, 11): (2, "in"), (14, 15): (2, "in"),
              (23, 24): (2, "io"), (24, 25): (2, "io"), (25, 1): (2, "lin")}
TENUTE_EST = {5: 180, 6: 90, 12: 90, 13: 140, 19: 160}
OMBRA_ALPHA = 0.22


def regola_est(i, j):
    return REGOLE_EST.get((i, j), (4 if (i, j) in COPPIE_DIFFICILI else 6, "io"))


def lista_intermedi(P, F, a, b, n, tipo):
    f01, f10 = F[(a, b)]
    return [intermedio(P[a], P[b], curva(tipo, k / (n + 1)), f01, f10) for k in range(1, n + 1)]


def percorso(P, F, pose, tenute=TENUTE_EST, salta_primo=False, ultima=True):
    """Pose consecutive (numeri da 1) con i loro intermedi; l'ultima posa è inclusa se ultima=True."""
    out = []
    for k in range(len(pose) - 1):
        i, j = pose[k], pose[k + 1]
        n, tipo = regola_est(i, j)
        passo = int(round(TOT_EST / (n + 1)))
        if (i, j) in ((10, 11), (14, 15)):
            passo = 30
        if not (k == 0 and salta_primo):
            out.append((P[i - 1], passo + tenute.get(i, 0)))
        out += [(x, passo) for x in lista_intermedi(P, F, i - 1, j - 1, n, tipo)]
    if ultima:
        out.append((P[pose[-1] - 1], 30 + tenute.get(pose[-1], 0)))
    return out


def urto(p, perno, tenuta=200):
    """Scossa e schiacciamento all'impatto del martello, poi la posa tenuta."""
    out = []
    for sx, sy, dx in [(1.0, 0.975, -3), (1.0, 0.985, 3), (1.0, 0.992, -2), (1.0, 0.997, 1)]:
        out.append((trasforma(p, perno, 1 / sy ** 0.5, sy, 0, dx * SC * 0.5, 0), 24))
    out.append((p, tenuta))
    return out


def colpo_extra(P, F, perno):
    """Ritorno lento del martello, attesa in alto, nuovo colpo con scossa (pose 15 -> 13 -> 15)."""
    a13, a14, a15 = 12, 13, 14
    r = [(x, 26) for x in lista_intermedi(P, F, a14, a15, 4, "io")[::-1]]
    r += [(P[a14], 26)]
    r += [(x, 26) for x in lista_intermedi(P, F, a13, a14, 4, "io")[::-1]]
    r += [(P[a13], 230)]
    r += [(x, 24) for x in lista_intermedi(P, F, a13, a14, 4, "in")]
    r += [(P[a14], 24)]
    r += [(x, 30) for x in lista_intermedi(P, F, a14, a15, 2, "in")]
    r += urto(P[a15], perno)
    return r


def sequenza_estesa(P, F, perno):
    """Storia completa (circa 12 s): respira, posa la fragola, prende il martello, colpisce quattro volte,
    lo ripone e annuisce, riprende la fragola, salta di gioia, dondola e ricomincia."""
    ob = lambda seg: con_ombra_fissa(seg, perno)
    seq = []
    seq += ob(gesto_respiro(P[0], perno, n=36, ms=33, con_ombra=False))              # 1: respira
    seq += ob(percorso(P, F, list(range(1, 12))))                                      # 1 -> 11: posa e primo colpo
    seq += ob(urto(P[10], perno, 220))
    seq += ob(percorso(P, F, list(range(11, 16)), salta_primo=True))                   # 11 -> 15: secondo colpo
    seq += ob(urto(P[14], perno, 220))
    seq += ob(colpo_extra(P, F, perno) + colpo_extra(P, F, perno))                     # altri due colpi
    seq += ob(percorso(P, F, [15, 16, 17, 18], salta_primo=True))                      # ripone il martello
    seq += ob(gesto_si(P[17], perno, n=44, ms=22, con_ombra=False))                    # annuisce
    seq += ob(percorso(P, F, [18, 19, 20, 21, 22, 23], salta_primo=True))              # riprende la fragola
    seq += gesto_salto(P[22], perno, n=54, ms=22, altezza_px=55, alpha0=OMBRA_ALPHA)   # salto (ombra propria)
    seq += ob(percorso(P, F, [23, 24, 25], salta_primo=True))
    seq += ob(gesto_dondolio(P[24], perno, n=54, ms=26, con_ombra=False))
    n, tipo = regola_est(25, 1)
    seq += ob([(x, 47) for x in lista_intermedi(P, F, 24, 0, n, tipo)])                # torna alla posa 1
    return seq


def con_ombra_fissa(seq, perno):
    """Ombra a terra uguale su tutti i fotogrammi (il salto ha la sua, più chiara in volo)."""
    sh = ombra(seq[0][0].shape, perno, 1.0, OMBRA_ALPHA)
    return [(sopra(p, sh), d) for p, d in seq]


# ------------------------------------------------------------------ 3c. costruzione: fragola ferma e casetta che cresce
#
# Nei frame originali la fragola cambia posizione (fino a 29 px) perché l'allineamento sui piedi non vale mentre
# il pinguino martella: il punto fisso del mondo è la fragola. Quindi nei frame 5-20 si allinea sulla fragola,
# nei frame 6-19 la si separa dal pinguino e la si ridisegna sempre uguale e immobile dietro di lui.

K3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
FASE_MARTELLO = range(5, 19)          # indici 0-based dei frame 6..19: livello del pinguino separato dalla fragola
FASE_ALLINEATA = range(4, 20)         # frame 5..20: allineati sulla fragola
PAD_SX, PAD_DX, PAD_SU, PAD_GIU = 34, 34, 70, 10   # margini della tela (a scala 1)
LARG_CASA = 128


def maschere_fragola(f):
    """(frutto, nucleo, contorno) della fragola in un frame RGBA allineato."""
    r, g, b, a = [f[..., i].astype(int) for i in range(4)]
    op = a > 120
    rosso = op & (r > 170) & (g < 120) & (b < 120)
    foglia = op & (g > r + 20) & (g > b + 10) & (g > 90)
    chiuso = cv2.morphologyEx(rosso.astype(np.uint8), cv2.MORPH_CLOSE,
                              cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
    n, lab, st, _ = cv2.connectedComponentsWithStats(chiuso, connectivity=8)
    frutto = lab == (1 + int(np.argmax(st[1:, 4])))
    nf, labf, stf, _ = cv2.connectedComponentsWithStats(foglia.astype(np.uint8), connectivity=8)
    vicino = cv2.dilate(frutto.astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (41, 41))).astype(bool)
    foglie = np.zeros_like(frutto)
    for i in range(1, nf):
        if stf[i][4] > 25 and (vicino & (labf == i)).any():
            foglie |= labf == i
    nucleo = cv2.morphologyEx((frutto | foglie).astype(np.uint8), cv2.MORPH_CLOSE,
                              cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7)))
    cont, _ = cv2.findContours(nucleo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    pieno = np.zeros(nucleo.shape, np.uint8)
    cv2.drawContours(pieno, cont, -1, 1, -1)
    nucleo = pieno.astype(bool)
    d_t = cv2.distanceTransform((~(a < 30)).astype(np.uint8), cv2.DIST_L2, 3)
    d_s = cv2.distanceTransform((~nucleo).astype(np.uint8), cv2.DIST_L2, 3)
    mx = np.maximum(np.maximum(r, g), b)
    colorato = ((r > 190) & (g > 100) & (g < 215) & (b < 120)) | (np.minimum(np.minimum(r, g), b) > 190) \
        | ((r > 200) & (g > 170) & (b < 120)) | ((b > r + 25) & (b > 45))
    scuro = ((mx < 120) | (a < 220)) & ~colorato
    contorno = (a > 8) & ~nucleo & scuro & (d_s <= 5.2) & (d_t <= 5.2)
    return frutto, nucleo, contorno


def posizione_fragola(frutto):
    """Bordo sinistro e base del frutto: non vengono coperti dal pinguino, che sta a destra."""
    ys, xs = np.nonzero(frutto)
    return float(np.percentile(xs, 2)), float(ys.max())


def pulisci_frammenti(pen, zona):
    """Toglie i resti scuri e staccati del contorno della fragola; scintille e linee azzurre restano."""
    n, lab, st, _ = cv2.connectedComponentsWithStats((pen[..., 3] > 40).astype(np.uint8), connectivity=8)
    zd = cv2.dilate(zona.astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))).astype(bool)
    out = pen.copy()
    for i in range(1, n):
        if st[i][4] < 900:
            comp = lab == i
            if (comp & zd).any() and pen[..., :3][comp].astype(int).max(axis=1).mean() < 130:
                out[comp, 3] = 0
    return out


def separa_fragola(f):
    """(livello del pinguino senza fragola, sprite della fragola)."""
    frutto, nucleo, contorno = maschere_fragola(f)
    m = nucleo | contorno
    pen = f.copy()
    pen[cv2.dilate(m.astype(np.uint8), K3).astype(bool), 3] = 0
    pen = pulisci_frammenti(pen, m)
    spr = f.copy()
    spr[~(m | (cv2.dilate(m.astype(np.uint8), K3).astype(bool) & (f[..., 3] < 255))), 3] = 0
    return pen, spr


def sposta_int(img, dx, dy, shape):
    """Copia img su una tela di forma shape spostata di (dx, dy) pixel interi."""
    out = np.zeros(shape, img.dtype)
    h, w = img.shape[:2]
    H, W = shape[:2]
    x0, y0 = int(round(dx)), int(round(dy))
    sx0, sy0 = max(0, -x0), max(0, -y0)
    dx0, dy0 = max(0, x0), max(0, y0)
    ww, hh = min(w - sx0, W - dx0), min(h - sy0, H - dy0)
    out[dy0:dy0 + hh, dx0:dx0 + ww] = img[sy0:sy0 + hh, sx0:sx0 + ww]
    return out


def sopra_u8(fg, bg):
    """Compone due immagini RGBA uint8 (fg sopra bg) senza premoltiplicare."""
    a = fg[..., 3:4].astype(np.float32) / 255
    b = bg[..., 3:4].astype(np.float32) / 255
    ao = a + b * (1 - a)
    rgb = (fg[..., :3] * a + bg[..., :3] * b * (1 - a)) / np.maximum(ao, 1e-6)
    return np.dstack([rgb, ao * 255]).clip(0, 255).astype(np.uint8)


def prepara_costruzione(frames, ancora_xy):
    """Allinea sulla fragola, separa i livelli e prepara la tela con lo spazio per la casetta.

    Restituisce: tela (H, W), perno (piedi), livelli del pinguino, sprite della fragola, testa del martello."""
    L, T = ancora_xy
    pos = {i: posizione_fragola(maschere_fragola(frames[i])[0]) for i in FASE_ALLINEATA}
    cx0 = float(np.median([pos[i][0] for i in FASE_MARTELLO]))
    by0 = float(np.median([pos[i][1] for i in FASE_MARTELLO]))
    H0, W0 = frames[0].shape[:2]
    H, W = H0 + PAD_SU + PAD_GIU, W0 + PAD_SX + PAD_DX + LARG_CASA + 30
    pen, sprite_src, orig = {}, {}, {}
    for i, f in enumerate(frames):
        if i in FASE_ALLINEATA:
            dx, dy = cx0 - pos[i][0], by0 - pos[i][1]
        else:
            dx = dy = 0
        sh = sposta_int(f, PAD_SX + dx, PAD_SU + dy, (H, W, 4))
        orig[i] = sh
        if i in FASE_MARTELLO:
            pen[i], sprite_src[i] = separa_fragola(sh)
        else:
            pen[i] = sh
    # sprite: dal frame in cui la fragola è meno coperta
    ref = max(FASE_MARTELLO, key=lambda i: int(maschere_fragola(orig[i])[1].sum() + maschere_fragola(orig[i])[2].sum()))
    spr = sprite_src[ref]
    # testa del martello (grigio) nei frame d'impatto: dove la casetta viene colpita
    teste = []
    for i in (10, 14):
        r, g, b, a = [orig[i][..., k].astype(int) for k in range(4)]
        grigio = (a > 200) & (np.abs(r - g) < 22) & (np.abs(g - b) < 28) & (r > 105) & (r < 232)
        ys, xs = np.nonzero(grigio)
        sel = xs > np.percentile(xs, 55)
        teste.append((xs[sel].mean(), ys[sel].mean()))
    testa = (float(np.mean([t[0] for t in teste])), float(np.mean([t[1] for t in teste])))
    return dict(H=H, W=W, perno=(L + PAD_SX, T + PAD_SU), pen=pen, spr=spr, testa=testa, orig=orig)


# ---- disegno della casetta (stesso stile della mascotte: contorno scuro spesso, colori piatti)

COL_CONTORNO = (22, 28, 48, 255)
COL_LEGNO = [(238, 190, 120, 255), (219, 156, 88, 255)]
COL_LEGNO_SCURO = (172, 106, 54, 255)
COL_ROSSO = (226, 56, 66, 255)
COL_ROSSO_SC = (176, 36, 52, 255)
COL_GIALLO = (247, 197, 49, 255)
COL_VETRO = (190, 226, 245, 255)
COL_CHIODO = (120, 128, 142, 255)
COL_PORTA = (150, 92, 46, 255)


def _fx(pts):
    return (np.asarray(pts, np.float64) * SC * 16).astype(np.int32)


def _poligono(img, pts, fill, spessore=3.2):
    cv2.fillPoly(img, [_fx(pts)], fill, cv2.LINE_AA, 4)
    cv2.polylines(img, [_fx(pts)], True, COL_CONTORNO, max(1, int(round(spessore * SC))), cv2.LINE_AA, 4)


def _linea(img, p0, p1, spessore, colore=COL_CONTORNO):
    cv2.line(img, tuple(int(v) for v in _fx(p0)), tuple(int(v) for v in _fx(p1)), colore,
             max(1, int(round(spessore * SC))), cv2.LINE_AA, 4)


def _cerchio(img, c, r, colore, contorno=True):
    centro = tuple(int(v) for v in _fx(c))
    cv2.circle(img, centro, int(r * SC * 16), colore, -1, cv2.LINE_AA, 4)
    if contorno:
        cv2.circle(img, centro, int(r * SC * 16), COL_CONTORNO, max(1, SC), cv2.LINE_AA, 4)


def _arrotondato(x0, y0, x1, y1, r=2.5):
    pts = []
    for cx, cy, a0 in ((x1 - r, y0 + r, -90), (x1 - r, y1 - r, 0), (x0 + r, y1 - r, 90), (x0 + r, y0 + r, 180)):
        for k in range(5):
            a = math.radians(a0 + 22.5 * k)
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def disegna_casetta(H, W, x0, yg):
    """Cinque livelli: 0 base, 1 pali, 2 parete bassa, 3 parete alta con porta e finestra, 4 tetto con bandierina.

    Ogni livello è un'immagine premoltiplicata a scala SC, con il suo punto d'appoggio per l'effetto 'pop'."""
    B, wall, roof = 9, 70, 52
    top = -B - wall

    def vuoto():
        return np.zeros((H * SC, W * SC, 4), np.uint8)

    Z = 1.25

    def pt(u, v):
        return (x0 + u * Z, yg + v * Z)

    def rr(u0, v0, u1, v1, r=2.5):
        return [pt(u, v) for u, v in _arrotondato(u0, v0, u1, v1, r)]

    strati = {}
    im = vuoto()                                                                   # 0: base
    _poligono(im, rr(-4, -B, LARG_CASA + 4, 0), COL_LEGNO_SCURO)
    for u in (14, 56, 98):
        _cerchio(im, pt(u, -B / 2), 1.5, COL_CHIODO)
    strati[0] = (im, pt(LARG_CASA / 2, 0))

    im = vuoto()                                                                   # 1: pali
    for u0 in (6, LARG_CASA - 24):
        _poligono(im, rr(u0, top, u0 + 18, -B), COL_LEGNO[1])
        _poligono(im, rr(u0 + 3, top + 3, u0 + 9, -B - 3, 1.5), COL_LEGNO[0], 1.4)
    strati[1] = (im, pt(LARG_CASA / 2, -B))

    im = vuoto()                                                                   # 2: parete bassa, tre assi
    for k in range(3):
        y1 = -B - k * 12.0
        _poligono(im, rr(10, y1 - 12.0, LARG_CASA - 10, y1, 2.0), COL_LEGNO[k % 2], 2.8)
        _cerchio(im, pt(17, y1 - 6), 1.5, COL_CHIODO)
        _cerchio(im, pt(LARG_CASA - 17, y1 - 6), 1.5, COL_CHIODO)
    strati[2] = (im, pt(LARG_CASA / 2, -B))

    im = vuoto()                                                                   # 3: parete alta, porta, finestra
    for k in range(3):
        y1 = -B - 36 - k * 11.4
        _poligono(im, rr(10, y1 - 11.4, LARG_CASA - 10, y1, 2.0), COL_LEGNO[(k + 1) % 2], 2.8)
        _cerchio(im, pt(17, y1 - 5.7), 1.5, COL_CHIODO)
        _cerchio(im, pt(LARG_CASA - 17, y1 - 5.7), 1.5, COL_CHIODO)
    ux = LARG_CASA * 0.50
    _poligono(im, rr(ux, -B - 46, ux + 28, -B, 3.0), COL_PORTA)
    _cerchio(im, pt(ux + 22, -B - 22), 2.2, COL_GIALLO, contorno=False)
    wx = LARG_CASA * 0.16
    _poligono(im, rr(wx, top + 8, wx + 26, top + 30), COL_VETRO, 3.0)
    _linea(im, pt(wx + 13, top + 8), pt(wx + 13, top + 30), 2.2)
    _linea(im, pt(wx, top + 19), pt(wx + 26, top + 19), 2.2)
    strati[3] = (im, pt(LARG_CASA / 2, -B - 36))

    im = vuoto()                                                                   # 4: tetto rosso e bandierina
    apx, apy = LARG_CASA / 2, top - roof
    _poligono(im, [pt(-12, top), pt(apx, apy), pt(LARG_CASA + 12, top), pt(LARG_CASA + 12, top + 7), pt(-12, top + 7)],
              COL_ROSSO, 3.4)
    _poligono(im, [pt(-6, top + 1), pt(apx - 3, apy + 9), pt(apx + 10, apy + 9), pt(LARG_CASA * 0.74, top + 1)],
              COL_ROSSO_SC, 2.0)
    _linea(im, pt(apx, apy), pt(apx, apy - 22), 3.0)
    _poligono(im, [pt(apx, apy - 22), pt(apx + 20, apy - 16), pt(apx, apy - 10)], COL_GIALLO, 2.6)
    strati[4] = (im, pt(LARG_CASA / 2, top))
    return {k: (img.astype(np.float32) / 255.0, anc) for k, (img, anc) in strati.items()}


def pop(u):
    """Comparsa a rimbalzo: scala da 0,55 a 1 con un leggero superamento. u in 0..1."""
    u = min(max(u, 0.0), 1.0)
    c1 = 1.70158
    f = 1 + (c1 + 1) * (u - 1) ** 3 + c1 * (u - 1) ** 2
    return 0.55 + 0.45 * f


def casa_a_tempo(strati, t_colpi, t, t_fine):
    """Livello premoltiplicato della casetta all'istante t (ms): la base c'è sempre, un livello per ogni colpo."""
    out = strati[0][0].copy()
    sparizione = 1.0 if t <= t_fine - 300 else max(0.0, (t_fine - t) / 300.0)
    for k, t0 in enumerate(t_colpi, 1):
        if t < t0:
            break
        s = pop((t - t0) / 170.0) * (0.35 + 0.65 * sparizione)
        layer = trasforma(strati[k][0], (strati[k][1][0] * SC, strati[k][1][1] * SC), 0.85 + 0.15 * s, s, 0, 0, 0)
        layer = layer * (min(1.0, (t - t0) / 50.0) * sparizione)
        out = layer + out * (1 - layer[..., 3:4])
    return out

# ------------------------------------------------------------------ 3d. sequenza della costruzione

ZOOM_CASA = 1.25
ESTRATTI_COLPO_MS = 170


def parametri_respiro(n):
    out = []
    for k in range(n):
        a = 2 * math.pi * k / n
        out.append((1 - 0.010 * math.sin(a), 1 + 0.022 * math.sin(a), 0.6 * math.sin(a), 0.0, 0.0))
    return out


def parametri_si(n):
    out = []
    for k in range(n):
        u = k / n
        a = max(0.0, math.sin(u * 2 * math.pi * 2)) if u < 0.8 else 0.0
        out.append((1 + 0.030 * a, 1 - 0.055 * a, 0.0, 0.0, 0.0))
    return out


def parametri_dondolio(n):
    out = []
    for k in range(n):
        a = 2 * math.pi * k / n
        out.append((1 + 0.012 * math.sin(2 * a), 1 - 0.012 * math.sin(2 * a), 3.2 * math.sin(a), 2 * SC * math.sin(a), 0.0))
    return out


def parametri_salto(n, altezza_px):
    """(sx, sy, rotazione, dx, dy, quota relativa) per ogni fotogramma del salto di gioia."""
    altezza = altezza_px * SC
    out = []
    for k in range(n):
        u = k / (n - 1)
        sx = sy = 1.0
        h = 0.0
        rot = 0.0
        if u < 0.16:
            e = curva("io", u / 0.16)
            sy, sx = 1 - 0.14 * e, 1 + 0.10 * e
        elif u < 0.24:
            e = curva("out", (u - 0.16) / 0.08)
            sy, sx = 0.86 + 0.28 * e, 1.10 - 0.18 * e
        elif u < 0.62:
            a = (u - 0.24) / 0.38
            h = altezza * 4 * a * (1 - a)
            sy, sx = 1.0 + 0.10 * (1 - a) ** 2 - 0.04 * a, 1.0 - 0.06 * (1 - a) ** 2 + 0.03 * a
            rot = 5 * math.sin(a * math.pi * 2)
        elif u < 0.72:
            e = curva("out", (u - 0.62) / 0.10)
            sy, sx = 1.0 - 0.16 * e, 1.0 + 0.12 * e
        else:
            a = (u - 0.72) / 0.28
            osc = math.exp(-4 * a) * math.cos(a * math.pi * 3.2)
            sy, sx = 1.0 - 0.10 * osc, 1.0 + 0.07 * osc
        out.append((sx, sy, rot, 0.0, -h, h / altezza))
    return out


def costruisci_sequenza(frames, ancora_xy):
    """Elementi della storia con fragola ferma e casetta che cresce. Ogni elemento è un dizionario con
    il livello (calcolato al momento: 'l' è una funzione), la durata, se serve la fragola dietro, ecc."""
    from functools import partial
    ctx = prepara_costruzione(frames, ancora_xy)
    H, W = ctx["H"], ctx["W"]
    perno = (ctx["perno"][0] * SC, ctx["perno"][1] * SC)
    pen1, spr1 = ctx["pen"], ctx["spr"]
    FM = set(FASE_MARTELLO)
    P1 = {i: premult(pen1[i]) for i in range(25)}
    B1 = {i: premult(sopra_u8(pen1[i], spr1)) for i in (5, 18)}
    P2 = {i: premult(pen1[i], SC) for i in range(25)}
    B2 = {i: premult(sopra_u8(pen1[i], spr1), SC) for i in (5, 18)}
    spr2 = premult(spr1, SC)
    flussi_cache = {}

    def coppia(a, b):
        if (a, b) == (4, 5):
            return P1[4], B1[5], P2[4], B2[5]
        if (a, b) == (18, 19):
            return B1[18], P1[19], B2[18], P2[19]
        return P1[a], P1[b], P2[a], P2[b]

    def flussi(a, b):
        if (a, b) not in flussi_cache:
            A1, Bb1, _, _ = coppia(a, b)
            f01, f10 = flusso(A1, Bb1), flusso(Bb1, A1)
            flussi_cache[(a, b)] = tuple(cv2.resize(f, None, fx=SC, fy=SC, interpolation=cv2.INTER_LINEAR) * SC
                                         for f in (f01, f10))
        return flussi_cache[(a, b)]

    def tw(a, b, n, tipo):
        """Intermedi (funzioni da eseguire al momento) tra le pose a e b (0-based)."""
        _, _, A2, Bb2 = coppia(a, b)
        f01, f10 = flussi(a, b)
        return [partial(intermedio, A2, Bb2, curva(tipo, k / (n + 1)), f01, f10) for k in range(1, n + 1)]

    def el(layer, ms, fr, colpo=False, ombra_fissa=True, ombra_salto=None):
        return {"l": layer, "ms": ms, "fr": fr, "colpo": colpo, "of": ombra_fissa, "os": ombra_salto}

    def trasf(base, p):
        return trasforma(base, perno, p[0], p[1], p[2], p[3], p[4])

    def percorso_c(pose, salta_primo=False, ultima=True):
        out = []
        for k in range(len(pose) - 1):
            i, j = pose[k] - 1, pose[k + 1] - 1
            n, tipo = regola_est(pose[k], pose[k + 1])
            passo = 30 if (pose[k], pose[k + 1]) in ((10, 11), (14, 15)) else int(round(TOT_EST / (n + 1)))
            if not (k == 0 and salta_primo):
                out.append(el(P2[i], passo + TENUTE_EST.get(pose[k], 0), i in FM))
            fr = (i in FM and j in FM)
            out += [el(f, passo, fr) for f in tw(i, j, n, tipo)]
        if ultima:
            u = pose[-1] - 1
            out.append(el(P2[u], 30 + TENUTE_EST.get(pose[-1], 0), u in FM))
        return out

    def urto_c(i, tenuta=200):
        out = []
        for k, (sx, sy, dx) in enumerate([(1.0, 0.975, -3), (1.0, 0.985, 3), (1.0, 0.992, -2), (1.0, 0.997, 1)]):
            out.append(el(partial(trasforma, P2[i], perno, 1 / sy ** 0.5, sy, 0, dx * SC * 0.5, 0), 24, True, colpo=(k == 0)))
        out.append(el(P2[i], tenuta, True))
        return out

    def colpo_extra_c():
        a13, a14, a15 = 12, 13, 14
        r = [el(f, 26, True) for f in tw(a14, a15, 4, "io")[::-1]] + [el(P2[a14], 26, True)]
        r += [el(f, 26, True) for f in tw(a13, a14, 4, "io")[::-1]] + [el(P2[a13], 230, True)]
        r += [el(f, 24, True) for f in tw(a13, a14, 4, "in")] + [el(P2[a14], 24, True)]
        r += [el(f, 30, True) for f in tw(a14, a15, 2, "in")]
        return r + urto_c(a15)

    seq = [el(partial(trasf, P2[0], p), 33, False) for p in parametri_respiro(36)]               # 1: respira
    seq += percorso_c(list(range(1, 12)))                                                           # posa la fragola, prende il martello
    seq += urto_c(10, 220)                                                                          # colpo 1
    seq += percorso_c(list(range(11, 16)), salta_primo=True)
    seq += urto_c(14, 220)                                                                          # colpo 2
    seq += colpo_extra_c() + colpo_extra_c()                                                        # colpi 3 e 4
    seq += percorso_c([15, 16, 17, 18], salta_primo=True)
    seq += [el(partial(trasf, P2[17], p), 22, True) for p in parametri_si(44)]                      # annuisce
    seq += percorso_c([18, 19, 20, 21, 22, 23], salta_primo=True)
    for p in parametri_salto(54, 55):                                                               # salto di gioia
        seq.append(el(partial(trasf, P2[22], p), 22, False, ombra_fissa=False,
                      ombra_salto=(1 - 0.35 * p[5], OMBRA_ALPHA * (1 - 0.4 * p[5]))))
    seq += percorso_c([23, 24, 25], salta_primo=True)
    seq += [el(partial(trasf, P2[24], p), 26, False) for p in parametri_dondolio(54)]              # dondola
    n, tipo = regola_est(25, 1)
    seq += [el(f, 47, False) for f in tw(24, 0, n, tipo)]                                           # torna alla posa 1
    return seq, ctx, perno, spr2


def componi_sequenza(seq, ctx, perno, spr2, on_frame):
    """Compone ogni fotogramma (casetta + fragola + ombra + pinguino) e lo passa a on_frame(uint8, ms)."""
    H2, W2 = ctx["H"] * SC, ctx["W"] * SC
    tx, ty = ctx["testa"]
    x0 = tx - 14.0
    yg = ctx["perno"][1] + 3.0
    strati = disegna_casetta(ctx["H"], ctx["W"], x0, yg)
    ombra_f = ombra((H2, W2), perno, 1.0, OMBRA_ALPHA)
    t_colpi, t = [], 0
    for e in seq:
        if e["colpo"]:
            t_colpi.append(t)
        t += e["ms"]
    t_fine = t
    print(f"colpi a: {[round(x) for x in t_colpi]} ms; durata {t_fine / 1000:.2f} s; {len(seq)} fotogrammi")
    t = 0
    for e in seq:
        layer = e["l"]() if callable(e["l"]) else e["l"]
        bg = ombra_f.copy() if e["of"] else np.zeros((H2, W2, 4), np.float32)
        if e["os"] is not None:
            bg = ombra((H2, W2), perno, e["os"][0], e["os"][1])
        if e["fr"]:
            bg = spr2 + bg * (1 - spr2[..., 3:4])
        casa = casa_a_tempo(strati, t_colpi, t, t_fine)
        bg = casa + bg * (1 - casa[..., 3:4])
        fr = layer + bg * (1 - layer[..., 3:4])
        on_frame(a_rgba(fr), e["ms"])
        t += e["ms"]


def esporta_u8(quadri, durate, base, scala_out, qualita=52, qualita_alpha=70, colori=96, gif=True,
               sfondo=(255, 255, 255)):
    """Scrive <base>.webp (trasparente) e <base>.gif (su sfondo) da fotogrammi RGBA uint8, ritagliando i margini."""
    occ = np.zeros(quadri[0].shape[:2], bool)
    for q in quadri:
        occ |= q[..., 3] > 8
    yy, xx = np.nonzero(occ)
    y0, y1, x0, x1 = max(0, yy.min() - 6), yy.max() + 7, max(0, xx.min() - 6), xx.max() + 7
    quadri = [q[y0:y1, x0:x1] for q in quadri]
    durate = [max(20, int(d)) for d in durate]
    webp = [Image.fromarray(q, "RGBA") for q in quadri]
    webp[0].save(f"{base}.webp", save_all=True, append_images=webp[1:], duration=durate, loop=0,
                 quality=qualita, alpha_quality=qualita_alpha, method=5, exact=False)
    if not gif:
        return len(webp), sum(durate)
    fattore = scala_out / SC
    sizes = (max(1, int(round(webp[0].width * fattore))), max(1, int(round(webp[0].height * fattore))))
    piatti = []
    for im in webp:
        fondo = Image.new("RGBA", im.size, sfondo + (255,))
        fondo.alpha_composite(im)
        piatti.append(fondo.convert("RGB").resize(sizes, Image.LANCZOS))
    campione = Image.new("RGB", (sizes[0] * 4, sizes[1] * 2))
    for n, idx in enumerate(np.linspace(0, len(piatti) - 1, 8).astype(int)):
        campione.paste(piatti[idx], ((n % 4) * sizes[0], (n // 4) * sizes[1]))
    pal = campione.quantize(colors=colori, method=Image.MEDIANCUT, dither=Image.NONE)
    gif_q = [p.quantize(palette=pal, dither=Image.NONE) for p in piatti]
    gif_q[0].save(f"{base}.gif", save_all=True, append_images=gif_q[1:], duration=durate, loop=0, disposal=1,
                  optimize=False)
    return len(webp), sum(durate)


def genera_costruzione(tavola, out, anteprima=False):
    frames, ancora_xy = allinea(carica_frame(tavola))
    seq, ctx, perno, spr2 = costruisci_sequenza(frames, ancora_xy)
    quadri, durate = [], []

    def on_frame(q, ms):
        quadri.append(q)
        durate.append(ms)

    componi_sequenza(seq, ctx, perno, spr2, on_frame)
    if anteprima:
        passo, t, acc, tess = 450, 0, 0, []
        for q, d in zip(quadri, durate):
            if acc >= t:
                tess.append(q)
                t += passo
            acc += d
        h, w = tess[0].shape[:2]
        cols = 6
        riga = (len(tess) + cols - 1) // cols
        foglio = Image.new("RGB", (w * cols, h * riga), (70, 74, 90))
        for n, q in enumerate(tess):
            tile = Image.new("RGBA", (w, h), (70, 74, 90, 255))
            tile.alpha_composite(Image.fromarray(q, "RGBA"))
            foglio.paste(tile.convert("RGB"), ((n % cols) * w, (n // cols) * h))
        foglio.save(out / "anteprima-costruzione.png", optimize=True)
        return len(quadri), sum(durate)
    return esporta_u8(quadri, durate, str(out / "pinguino-costruzione"), 1.0)

# ------------------------------------------------------------------ 4. esportazione


def esporta(seq, base, scala_out, sfondo=(255, 255, 255), gif=True, qualita=80, ritaglia=False, colori=128, qualita_alpha=100):
    """Scrive <base>.webp (trasparente, scala SC) e, se gif=True, <base>.gif (su sfondo, scala_out)."""
    if ritaglia:                       # toglie i margini vuoti comuni a tutti i fotogrammi
        occ = np.zeros(seq[0][0].shape[:2], bool)
        for p, _ in seq:
            occ |= p[..., 3] > 0.03
        yy, xx = np.nonzero(occ)
        y0, y1, x0, x1 = max(0, yy.min() - 6), yy.max() + 7, max(0, xx.min() - 6), xx.max() + 7
        seq = [(p[y0:y1, x0:x1], d) for p, d in seq]
    quadri = [a_rgba(p) for p, _ in seq]
    durate = [max(20, int(d)) for _, d in seq]
    webp = [Image.fromarray(q, "RGBA") for q in quadri]
    webp[0].save(f"{base}.webp", save_all=True, append_images=webp[1:], duration=durate, loop=0,
                 quality=qualita, alpha_quality=qualita_alpha, method=5, exact=False)
    if not gif:
        return len(seq), sum(durate)
    fattore = scala_out / SC
    sizes = (max(1, int(round(webp[0].width * fattore))), max(1, int(round(webp[0].height * fattore))))
    piatti = []
    for im in webp:
        fondo = Image.new("RGBA", im.size, sfondo + (255,))
        fondo.alpha_composite(im)
        piatti.append(fondo.convert("RGB").resize(sizes, Image.LANCZOS))
    # palette globale: evita lo sfarfallio dei colori tra un fotogramma e l'altro
    campione = Image.new("RGB", (sizes[0] * 4, sizes[1] * 2))
    for n, idx in enumerate(np.linspace(0, len(piatti) - 1, 8).astype(int)):
        campione.paste(piatti[idx], ((n % 4) * sizes[0], (n // 4) * sizes[1]))
    pal = campione.quantize(colors=colori, method=Image.MEDIANCUT, dither=Image.NONE)
    gif = [p.quantize(palette=pal, dither=Image.NONE) for p in piatti]
    gif[0].save(f"{base}.gif", save_all=True, append_images=gif[1:], duration=durate, loop=0, disposal=1,
                optimize=False)
    return len(seq), sum(durate)


def anteprima(frames, percorso):
    """Foglio 5x5 con i frame allineati (stessa linea del suolo), su fondo neutro."""
    h, w = frames[0].shape[:2]
    foglio = Image.new("RGB", (w * 5, h * 5), (70, 74, 90))
    for i, f in enumerate(frames):
        tile = Image.new("RGBA", (w, h), (70, 74, 90, 255))
        tile.alpha_composite(Image.fromarray(f, "RGBA"))
        foglio.paste(tile.convert("RGB"), ((i % 5) * w, (i // 5) * h))
    foglio.save(percorso, optimize=True)


def main():
    argomenti = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(argomenti) < 2:
        raise SystemExit(__doc__)
    tavola, out = Path(argomenti[0]), Path(argomenti[1])
    (out / "gesti").mkdir(parents=True, exist_ok=True)

    frames, (L, T) = allinea(carica_frame(tavola))
    P1 = [premult(f) for f in frames]
    P2 = [premult(f, SC) for f in frames]
    perno = (L * SC, T * SC)

    anteprima(frames, out / "anteprima-frame-allineati.png")
    if "--frame" in sys.argv:
        (out / "frame").mkdir(exist_ok=True)
        for i in range(25):
            Image.fromarray(a_rgba(P2[i]), "RGBA").save(out / "frame" / f"frame-{i + 1:02d}.png", optimize=True)

    # flussi calcolati sulla risoluzione originale e poi ingranditi
    F = {}
    for i in range(25):
        j = (i + 1) % 25
        f01, f10 = flusso(P1[i], P1[j]), flusso(P1[j], P1[i])
        F[(i, j)] = tuple(cv2.resize(f, None, fx=SC, fy=SC, interpolation=cv2.INTER_LINEAR) * SC for f in (f01, f10))

    if "--costruzione" in sys.argv:
        n, ms = genera_costruzione(tavola, out, anteprima="--anteprima" in sys.argv)
        print(f"costruzione: {n} fotogrammi, {ms / 1000:.2f} s")
        return
    risultati = {}
    # versione estesa: tela più alta per il salto, stesso flusso con il margine aggiunto
    sopra_px, lati = 70 * SC, 40 * SC
    perno_e = (perno[0] + lati, perno[1] + sopra_px)
    P2e = [amplia(p, sopra_px, lati) for p in P2]
    Fe = {k: tuple(np.pad(f, ((sopra_px, 0), (lati, lati), (0, 0))) for f in v) for k, v in F.items()}
    risultati["pinguino-lavoro-estesa"] = esporta(sequenza_estesa(P2e, Fe, perno_e), str(out / "pinguino-lavoro-estesa"),
                                                  1.0, qualita=52, qualita_alpha=70, ritaglia=True, colori=96)
    if "--solo-estesa" in sys.argv:
        for nome, (n, ms) in risultati.items():
            print(f"{nome}: {n} fotogrammi, {ms / 1000:.2f} s")
        return
    risultati["pinguino-lavoro-fluida"] = esporta(sequenza_fluida(P2, F), str(out / "pinguino-lavoro-fluida"), GIF_SCALE)
    risultati["pinguino-lavoro-originale"] = esporta(sequenza_originale(P2), str(out / "pinguino-lavoro-originale"), GIF_SCALE)

    # gesti extra: tela più grande per lasciare spazio al salto
    sopra_px, lati = 90 * SC, 40 * SC
    perno_g = (perno[0] + lati, perno[1] + sopra_px)
    base = {k: amplia(P2[k - 1], sopra_px, lati) for k in (18, 19, 23, 25)}
    risultati["gesti/pinguino-salto-di-gioia"] = esporta(gesto_salto(base[23], perno_g), str(out / "gesti" / "pinguino-salto-di-gioia"), GIF_SCALE, gif=False)
    risultati["gesti/pinguino-dondolio"] = esporta(gesto_dondolio(base[25], perno_g), str(out / "gesti" / "pinguino-dondolio"), GIF_SCALE, gif=False)
    risultati["gesti/pinguino-respiro"] = esporta(gesto_respiro(base[19], perno_g), str(out / "gesti" / "pinguino-respiro"), GIF_SCALE, gif=False)
    risultati["gesti/pinguino-si"] = esporta(gesto_si(base[18], perno_g), str(out / "gesti" / "pinguino-si"), GIF_SCALE, gif=False)
    P2g = [amplia(p, sopra_px, lati) for p in P2]
    Fg = {k: tuple(np.pad(f, ((sopra_px, 0), (lati, lati), (0, 0))) for f in v) for k, v in F.items()}
    risultati["gesti/pinguino-martellata"] = esporta(gesto_martello(P2g, Fg, perno_g), str(out / "gesti" / "pinguino-martellata"), GIF_SCALE, gif=False)
    for nome, (n, ms) in risultati.items():
        print(f"{nome}: {n} fotogrammi, {ms / 1000:.2f} s")


if __name__ == "__main__":
    main()
