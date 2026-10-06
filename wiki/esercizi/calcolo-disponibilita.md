---
tipo: esercizio
argomento: "calcolo di disponibilità e downtime (MTBF, MTTR, nove)"
difficoltà: bassa
---

# Calcolo della disponibilità e del downtime

## Metodo

> 📄 Fonte: [[02-Availability.pdf#page=6]], [[02-Availability.pdf#page=7]]

1. **Da MTBF e MTTR alla disponibilità:** $A \approx \dfrac{MTBF}{MTBF + MTTR}$ (stesse unità di tempo sopra e sotto).
2. **Dalla disponibilità al downtime:** $\text{downtime} = (1 - A)\cdot T$, con $T$ l'intervallo considerato ($T_{90} = 2160$ h, $T_{anno} = 8760$ h con 365 giorni, come nella tabella della slide).
3. **Dal downtime ammesso alla disponibilità richiesta:** $A = 1 - \dfrac{\text{downtime}}{T}$.
4. **Controllo:** ogni «nove» in più divide il downtime per 10.

## Concetti usati

[[availability]] · [[tattiche-availability]] (le tattiche di recover abbassano l'MTTR)

## Casi svolti

### Caso 1 — Ricostruire la tabella dei «nove»

**Traccia:** [[02-Availability.pdf#page=7]] — verificare i valori della tabella.

Svolgimento completo e tabella in [[availability]] § Tabella dei «nove». **Risultato:** tutte le righe tornano con un anno di 365 giorni, tranne 99,9 % / anno: il valore corretto è $10^{-3} \times 8760\ \text{h} = 8.76\ \text{h}$ = **8 h 45 min 36 s** (la slide riporta 8 h 0 min 46 s).

### Caso 2 — Disponibilità da MTBF e MTTR

> 🧩 Esempio mio per applicare la formula di [[02-Availability.pdf#page=6]] (nessun esercizio numerico nelle slide).

**Dati:** $MTBF = 720\ \text{h}$ (un malfunzionamento al mese), $MTTR = 2\ \text{h}$.

$$
\begin{aligned}
A &= \frac{720\ \text{h}}{720\ \text{h} + 2\ \text{h}} && \text{formula di p. 6} \\
  &= \frac{720}{722} \approx 0.99723 && \text{circa 99,72 \%} \\
\text{downtime}_{anno} &= (1 - 0.99723)\times 8760\ \text{h} \approx 24.3\ \text{h} && \text{circa un giorno all'anno}
\end{aligned}
$$

**Sanity check:** 12 malfunzionamenti all'anno × 2 h di riparazione = 24 h ✔.

**Variante:** con la tattica *redundant spare* il subentro richiede 1 min invece di 2 h: $MTTR = 1/60\ \text{h}$ ⇒ $A = 720/(720 + 0.0167) \approx 0.99998$, downtime annuo $\approx 12 \times 1\ \text{min} = 12\ \text{min}$. Stesso numero di guasti, disponibilità passata da «due nove» a oltre «quattro nove»: si migliora la disponibilità anche **senza** ridurre i guasti, accorciando la riparazione.

### Caso 3 — Dalla misura dello scenario alla disponibilità

> 🧩 Esempio mio sullo scenario di [[02-Availability.pdf#page=9]] (rilevazione ≤ 30 s, ripristino ≤ 60 s).

Se il guasto di un application server interrompe le richieste servite da quell'istanza fino al ripristino, al massimo per $30 + 60 = 90$ s, e capita una volta a settimana:

$$
\text{downtime parziale}_{anno} \le 52 \times 90\ \text{s} = 4680\ \text{s} = 78\ \text{min}
$$

Con due istanze il guasto tocca circa metà delle richieste: l'effetto è compatibile con «completare almeno il 99 % delle richieste» della misura dello scenario. **Ipotesi:** un guasto a settimana; carico diviso a metà tra le istanze; le richieste già in corso sull'istanza guasta vanno perse, non quelle nuove, che vengono reindirizzate.

## Trappole

- Usare unità diverse per MTBF e MTTR.
- Confondere disponibilità (frazione di tempo) e affidabilità (quanto spesso si guasta): due sistemi con la stessa $A$ possono avere guasti rari e lunghi o frequenti e brevi.
- Sbagliare l'anno: la tabella della slide usa 365 giorni.
- Dimenticare che ogni «nove» divide il downtime per 10: serve anche a scovare refusi.

_Aggiornato: 2026-09-30 — ingest 02-Availability.pdf_
