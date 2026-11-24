---
tipo: entità
categoria: stile
famiglia: "data-flow"
---

# Batch sequential

## Contesto e problema

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=37]]

Elaborazioni su grandi volumi di dati, non interattive, che si svolgono per fasi: tipicamente l'elaborazione di transazioni nei sistemi finanziari. È «uno dei primissimi stili architetturali».

## Soluzione

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=37]]

- **Componenti:** programmi separati, eseguiti in un ordine specificato.
- **Connettori:** il passaggio dei dati da un programma al successivo; storicamente potevano essere **persone che spostavano nastri** tra i programmi.
- **Elementi dati:** i **lotti** (*batch*) passati tra i componenti finché l'elaborazione è completa.
- **Vincolo:** ogni programma parte quando il precedente ha finito tutto il suo lotto.

## Diagramma

![[lez08-stili-p38-batch-sequential-finanza.png]]
*Applicazione finanziaria ([[05_Architectural_Styles_Complete.pdf#page=38]]): le «Daily transactions» sono ordinate per numero di conto («Sort by account number», produce «Sorted transactions»); insieme al «Master account tape» alimentano «Process transactions», che produce l'«Updated master tape» (riscritto su nastro per l'uso del giorno dopo, «For tomorrow's use») e da cui «Print summary of accounts» produce il «Print file». I cerchi sono i lotti di dati, i rettangoli i programmi.*

![[lez08-stili-p39-batch-sequential-lunar-lander.png]]
*Lunar Lander in batch sequential ([[05_Architectural_Styles_Complete.pdf#page=39]]): i dati (h, v, t, fuel) attraversano «Get BurnRate from user» → «Compute new h, v, t, fuel» → «Display h, v, t, fuel to user» e rientrano per l'iterazione successiva.*

## Attributi di qualità

| Attributo | Effetto | Perché | Fonte |
|---|---|---|---|
| Interattività / controllo in tempo reale | − | un programma parte solo a lotto precedente completato: «difficilmente una ricetta per una missione lunare di successo» | [[05_Architectural_Styles_Complete.pdf#page=39]] |
| Modularità | + | programmi indipendenti, ciascuno con un compito | [[05_Architectural_Styles_Complete.pdf#page=37]] |

🧩 Il confronto con [[pipe-and-filter]] è istruttivo: lì i filtri lavorano in modo incrementale e concorrente; qui ogni passo attende il lotto completo.

## Quando usarlo / quando no

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=37]], [[05_Architectural_Styles_Complete.pdf#page=39]]

Sì per transazioni finanziarie e lavorazioni in blocco; no per applicazioni interattive o in tempo reale come Lunar Lander.

## Varianti ed esempi

- Elaborazione di transazioni finanziarie (p. 38). Variante moderna: [[pipe-and-filter]].

## Connessioni

- [[pipe-and-filter]]: l'altra variante dei data-flow.
- [[lunar-lander-in-ogni-stile]]

## Fonti

- [[architectural-styles]]

_Aggiornato: 2026-11-24 — ingest 05_Architectural_Styles_Complete.pdf_
