---
tipo: entità
categoria: stile
famiglia: "data-flow"
---

# Pipe and filter

## Contesto e problema

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=41]]

Un compito complesso di trasformazione di dati va **scomposto in passi indipendenti**, ognuno con una trasformazione specifica, in modo da poter combinare, riusare e parallelizzare i passi.

## Soluzione

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=42]], [[05_Architectural_Styles_Complete.pdf#page=46]]

- **Componenti — filtri:** programmi che trasformano flussi di dati in ingresso in flussi in uscita. Un filtro può *arricchire* (calcolare o aggiungere informazione), *raffinare* (aggregare o estrarre) o *trasformare* in un'altra rappresentazione. È **attivo** se avvia l'elaborazione come programma o thread separato (ciclo di lettura e scrittura); **passivo** se eseguito su invocazione di un altro componente (*pull*: chiamata di funzione; *push*: chiamata di procedura).
- **Connettori — pipe:** canali per i flussi, realizzati con code, stream, messaggi, file temporanei o simili.
- **Invarianti:** i filtri sono indipendenti e **non condividono stato**; un filtro non sa chi sta a monte o a valle; i filtri possono **girare in concorrenza**, senza attendere che quello a monte abbia finito.
- **Implementazione:** in un processo, le pipe sono code in memoria; in un sistema distribuito, un'infrastruttura di messaggistica (code di messaggi) porta i flussi tra filtri remoti ([[05_Architectural_Styles_Complete.pdf#page=44]]). Un passo lento può avere **più istanze parallele** dello stesso filtro, con attenzione a scritture duplicate e all'ordine ([[05_Architectural_Styles_Complete.pdf#page=45]]).

## Diagramma

![[lez08-stili-p41-pipeline-componenti-riusati.png]]
*Pipeline ([[05_Architectural_Styles_Complete.pdf#page=41]]): i dati della sorgente 1 attraversano Task A, B, C, D e arrivano, trasformati, alla business logic; quelli della sorgente 2 attraversano Task B, E, F. Il Task B è lo stesso componente in due pipeline: «Components reused in different pipelines» — il riuso dei filtri.*

![[lez08-stili-p45-filtri-paralleli.png]]
*Filtri paralleli ([[05_Architectural_Styles_Complete.pdf#page=45]]): i dati da una sorgente si distribuiscono su tre istanze del Task A, passano per Task B e Task C in serie, poi per tre istanze del Task D, fino alla business logic. Le pipe sono i tubi azzurri; lo stadio lento (A, D) è replicato per aumentare il throughput.*

```mermaid
flowchart LR
    A[Filtro A<br/>legge i log] -->|pipe| B[Filtro B<br/>normalizza]
    B -->|pipe| C[Filtro C<br/>tiene gli errori critici]
    C -->|pipe| D[Filtro D<br/>aggrega]
    D -->|pipe| E[Filtro E<br/>salva nel database]
```
*🧩 Ricostruzione dell'esempio di elaborazione di log ([[05_Architectural_Styles_Complete.pdf#page=47]]): ogni scatola è un filtro indipendente, ogni freccia una pipe.*

## Attributi di qualità

| Attributo | Effetto | Perché | Fonte |
|---|---|---|---|
| Prestazioni | + | filtri in parallelo, elaborazione incrementale (non si attende tutto l'input) | [[05_Architectural_Styles_Complete.pdf#page=48]] |
| Scalabilità | + | i filtri costosi si replicano e scalano in modo indipendente | [[05_Architectural_Styles_Complete.pdf#page=48]] |
| Riuso | + | filtri generici servono più catene (es. normalizzazione riusabile per un'altra sorgente) | [[05_Architectural_Styles_Complete.pdf#page=47]], [[05_Architectural_Styles_Complete.pdf#page=48]] |
| Modularità | + | ogni filtro ha una responsabilità distinta | [[05_Architectural_Styles_Complete.pdf#page=48]] |
| Modificabilità e testabilità | + | ogni filtro è disaccoppiato e si cambia/testa in modo indipendente | [[05_Architectural_Styles_Complete.pdf#page=48]] |
| Analizzabilità | + | throughput, latenza e deadlock sono analizzabili | [[05_Architectural_Styles_Complete.pdf#page=49]] |
| Interattività | − | le implementazioni batch ne offrono poca; scomodo per conversazioni complesse | [[05_Architectural_Styles_Complete.pdf#page=50]] |
| Prestazioni (dati complessi) | − | strutture dati complesse richiedono codifica/decodifica costose o formati comuni | [[05_Architectural_Styles_Complete.pdf#page=50]] |

> ⚖️ Trade-off: l'indipendenza dei filtri (che dà riuso e parallelismo) obbliga a un formato comune per i dati sulle pipe.

## Quando usarlo / quando no

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=49]], [[05_Architectural_Styles_Complete.pdf#page=50]]

Sì quando il problema è una catena di trasformazioni di flussi (compilatori, elaborazione di segnali, log); no quando serve interazione complessa o dati strutturati difficili da serializzare.

## Varianti ed esempi

- Shell UNIX: `ls invoices | grep -e August | sort` — tre filtri collegati da due pipe ([[05_Architectural_Styles_Complete.pdf#page=43]]).
- Un compilatore Java: analisi lessicale → parsing → analisi semantica → ottimizzazione ([[05_Architectural_Styles_Complete.pdf#page=43]]).
![[lez08-stili-p51-pipe-filter-lunar-lander.png]]
*Lunar Lander ([[05_Architectural_Styles_Complete.pdf#page=51]]): «Get BurnRate from user» → Stream (in: br) → «Compute new values» → Stream (in: a, f, t, v) → «Display new values to user».*

- Lunar Lander: un filtro chiede il burn rate e lo scrive nello stream; il secondo aggiorna l'ambiente a ogni nuovo valore; il terzo aggiorna il display ([[05_Architectural_Styles_Complete.pdf#page=51]]).

## Connessioni

- [[batch-sequential]]: variante senza concorrenza.
- [[publish-subscribe]]: anche qui la messaggistica fa da connettore, ma con più destinatari.
- [[lunar-lander-in-ogni-stile]]

## Fonti

- [[architectural-styles]]

_Aggiornato: 2026-11-24 — ingest 05_Architectural_Styles_Complete.pdf_
