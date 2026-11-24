---
tipo: esercizio
argomento: "Pianificare uno Sprint: obiettivo, storie pronte, velocity e capacity"
difficoltà: media
---

# Pianificare uno Sprint

## Metodo

Quando: all'inizio di ogni Sprint, nello Sprint Planning ([[sprint-e-sprint-planning]]).

1. **Scegli l'obiettivo** (Sprint Goal): una frase di valore per il business che le storie realizzano **insieme** ([[04_Agile_02.pdf#page=41]]).
2. **Prendi dalla testa del Product Backlog** ordinato solo gli elementi **«Ready»** (chiari, piccoli, con criteri di accettazione, stimati, indipendenti, verificabili, [[04_Agile_02.pdf#page=32]]).
3. **Calcola la velocity** come media degli sprint recenti ([[04_Agile_02.pdf#page=52]]); al **primo sprint** usa una stima iniziale ([[04_Agile_02.pdf#page=53]]).
4. **Correggi per la capacity**: giorni-persona disponibili / giorni-persona pieni ([[04_Agile_02.pdf#page=54]]).
5. **Seleziona** le storie che contribuiscono all'obiettivo, entro il carico così ottenuto, non oltre: è una **previsione**, non un impegno fisso ([[04_Agile_02.pdf#page=45]]).
6. **Scomponi in task** (stimabili in ore) per costruire lo Sprint Backlog ([[04_Agile_02.pdf#page=35]]).

**Concetti usati:** [[product-backlog-e-sprint-backlog]], [[stima-story-points-velocity-capacity]], [[sprint-e-sprint-planning]], [[user-stories]].

## Casi svolti

### Caso 1 — Scegliere un obiettivo (le storie dell'e-commerce)

**Traccia:** [[04_Agile_02.pdf#page=42]] — se per lo Sprint ho scelto *Login, PayPal, PDF Report, Dashboard, Translation*, qual è l'obiettivo? E se scelgo *Cart, Checkout, Payment, Order confirmation*?

**Svolgimento:** prova a scrivere **una frase** che spieghi perché le storie stanno insieme.
- Primo insieme: nessuna frase regge («Beats me!»): sono cinque funzioni indipendenti; non c'è un risultato di valore comune e non si sa cosa tagliare se manca tempo.
- Secondo insieme: *«permettere ai clienti di completare un acquisto online»*; le quattro storie sono i passi dello stesso flusso (carrello → checkout → pagamento → conferma).

**Soluzione:** l'obiettivo del secondo insieme è chiaro; il primo non è un Sprint Goal ma una **lista**. Lo Sprint è un insieme di storie che realizzano insieme un obiettivo ([[04_Agile_02.pdf#page=41]]).

### Caso 2 — Chi può entrare nello Sprint (stati delle storie)

**Traccia:** [[04_Agile_02.pdf#page=33]] — prossimo Sprint tra due settimane; sei elementi con uno stato: *Login — Ready; Product search — Ready; Shopping cart — Almost ready; PayPal — Needs further clarification; Wishlist — Too broadly defined; Mobile app — Just an idea.*

**Svolgimento:** il test di p. 32 separa ciò che si può pianificare da ciò che manca di dettaglio.

| Elemento | Stato | Cosa manca (rispetto alle sei domande) 🧩 | Può entrare? |
|---|---|---|---|
| Login | Ready | niente (3 SP, criteri: email, password, errore, blocco dopo 5 tentativi, [[04_Agile_02.pdf#page=31]]) | **sì** |
| Product search | Ready | niente | **sì** |
| Shopping cart | Almost ready | un requisito (probabilmente criteri o stima) | **forse**, se il refinement si chiude prima dello Sprint |
| PayPal | Needs further clarification | non è chiara | no |
| Wishlist | Too broadly defined | non è abbastanza piccola | no (da scomporre) |
| Mobile app | Just an idea | non è nemmeno una storia | no |

**Soluzione:** «solo i primi 2 o 3 saranno candidati» ([[04_Agile_02.pdf#page=33]]): Login e Product search, e Shopping cart se diventa Ready. Il lavoro da fare nelle due settimane che restano è **backlog refinement** sulle altre ([[04_Agile_02.pdf#page=34]]). La slide non dà le stime di Product search e Shopping cart né un obiettivo, quindi la selezione numerica non si può chiudere qui: ❓ dato mancante.

### Caso 3 — Quanto prendere (velocity e capacity)

**Traccia:** velocity dei primi quattro sprint 28, 31, 30, 29 ([[04_Agile_02.pdf#page=52]]); capacity di un team di 7 su 10 giorni con 7 giorni-persona di assenza ([[04_Agile_02.pdf#page=54]]).

**Svolgimento:**

$$
\begin{aligned}
\bar v &= \frac{28+31+30+29}{4} = 29{,}5 \approx 30\ \text{SP} && \text{velocity media} \\
C &= \frac{70-7}{70} = 0{,}9 && \text{capacity al 90 \%} \\
T &= \bar v \cdot C \approx 30 \cdot 0{,}9 = 27\ \text{SP} && \text{carico da selezionare}
\end{aligned}
$$

> 🧩 Elaborazione mia — i due esempi di p. 52 e p. 54 sono indipendenti nelle slide (la capacity «−10 %» non è collegata alla velocity «30»): li ho combinati per mostrare il passaggio logico «velocity → correzione per capacity → carico». La slide di p. 54 lo dice con le parole «per la stima successiva gli SP del backlog si riducono del 10 %».

**Applicazione al backlog di esempio di p. 27** (le cinque righe stimate 5, 2, 3, 8, 8, nell'ordine di priorità; dati di un esempio diverso, usati solo per mostrare i passaggi 🧩):

| Ordine | Elemento | SP | SP cumulati | Entro 27 SP? |
|---|---|---|---|---|
| 1 | Link accounts to profiles | 5 | 5 | sì |
| 2 | Update traceability matrix | 2 | 7 | sì |
| 3 | Transfer money between accounts | 3 | 10 | sì |
| 4 | Refactor Login Class | 8 | 18 | sì |
| 5 | Find locations | 8 | 26 | sì (26 ≤ 27) |

Con un carico di 27 SP entrano tutte e cinque; con un carico di 20 SP si fermerebbe alla riga 4 (18 SP: aggiungere la quinta porterebbe a 26 > 20).

**Soluzione:** il numero **27** (o «circa 27») è una **previsione**, non un impegno. Se alla fine dello Sprint si completano ad esempio 25 SP, la velocity reale diventa un nuovo dato per la media ([[04_Agile_02.pdf#page=45]], [[04_Agile_02.pdf#page=51]]). Le storie non chiuse **non contano** nella velocity.

## Trappole

- **Riempire lo Sprint con storie non «Ready»**: si scopre durante lo Sprint che mancano criteri o stime.
- **Insieme di storie senza obiettivo** (caso 1): impossibile decidere cosa tagliare.
- **Usare la velocity come impegno** invece che come previsione.
- **Ignorare la capacity**: ferie e assenze riducono il carico sostenibile in proporzione ai giorni-persona persi.
- **Contare storie quasi finite nella velocity**: valgono 0 finché non rispettano la DoD ([[04_Agile_02.pdf#page=51]]).

## Fonti

- [[agile-scrum-framework]] — [[04_Agile_02.pdf#page=31]]–[[04_Agile_02.pdf#page=35]], [[04_Agile_02.pdf#page=41]]–[[04_Agile_02.pdf#page=46]], [[04_Agile_02.pdf#page=51]]–[[04_Agile_02.pdf#page=54]]

_Aggiornato: 2026-10-22 — ingest 04_Agile_02.pdf_
