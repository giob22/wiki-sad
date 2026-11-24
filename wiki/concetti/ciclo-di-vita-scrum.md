---
tipo: concetto
importanza_esame: media
prerequisiti: ["scrum"]
fonti_pdf: ["04_Agile_02.pdf#page=20", "04_Agile_02.pdf#page=21", "04_Agile_02.pdf#page=22", "04_Agile_02.pdf#page=23", "04_Agile_02.pdf#page=24"]
termine_inglese: "Scrum project life-cycle, product vision"
---

# Ciclo di vita di un progetto Scrum, product vision e formazione del team

## Definizione

> 📄 Fonte: [[04_Agile_02.pdf#page=21]]

Scrum, in senso stretto, è **solo una successione di Sprint**; il ciclo di vita di un progetto può però essere visto come composto da **tre macro-fasi**:

| Macro-fase | Che cos'è (slide) | Uscite / attività |
|---|---|---|
| **Inception** (avvio) | fase di pianificazione in cui si **stabiliscono gli obiettivi generali** del progetto e si **progetta l'architettura software** | **visione del prodotto, Product Backlog iniziale, team e ambiente di sviluppo** |
| **Construction** (costruzione) | segue l'inception: **una serie di cicli di Sprint**, ciascuno dei quali sviluppa un **incremento di sistema** | un incremento a ogni Sprint |
| **Transition** (chiusura) | **chiude** il progetto, **completa la documentazione** richiesta (comprese le schermate di aiuto e i manuali utente) e **valuta le lezioni apprese** (*lessons learned*) | documentazione finale, lezioni apprese |

## Spiegazione

![[lez07-ag2-p20-ciclo-di-vita-progetto.png]]
*Figura di [[04_Agile_02.pdf#page=20]]. Una freccia curva «Next Release» attraversa otto cerchi a freccia (otto Sprint). Sotto, una barra divisa in tre tratti: **Inception** («Envision and plan», cioè immaginare e pianificare) sul primo cerchio, **Construction** («Incrementally build a consumable solution», costruire per incrementi una soluzione utilizzabile) sui cerchi centrali, **Transition** («Release solution», rilasciare la soluzione) sugli ultimi. Il messaggio: tutti i cerchi sono Sprint, ma non tutti hanno lo stesso scopo; la maggior parte del lavoro è costruzione, con un inizio di preparazione e una fine di rilascio.*

> 🧩 Elaborazione mia — perché le tre fasi sono compatibili con «Scrum = solo Sprint»: la preparazione e la chiusura sono comunque eseguite in iterazioni a durata fissa (nel progetto di corso la prima iterazione è proprio quella *preparatoria* di 3 settimane). Inoltre l'inception comprende **la progettazione dell'architettura**: è il punto in cui questo corso incontra Scrum (→ [[attribute-driven-design]], [[buone-pratiche-architetturali]]).

> 💡 Connessione: il ciclo inception → costruzione → transizione richiama le fasi dell'Unified Process (ideazione, elaborazione, costruzione, transizione) previste dal programma ([[Programma Syllabus]]); la slide non fa il confronto, e UP non è ancora stato ingerito.

### Product Vision

> 📄 Fonte: [[04_Agile_02.pdf#page=22]]

La **visione del prodotto** (*Product Vision*) descrive **lo scopo del prodotto e il valore che intende generare**. Risponde a quattro domande:

1. quale **problema** vogliamo risolvere?
2. per **chi** sviluppiamo il prodotto?
3. quale **valore** offrirà agli utenti?
4. come sapremo se il prodotto ha **successo**?

La visione **resta stabile nel tempo** e **guida tutte le decisioni sul Product Backlog**.

#### Esempio: visione di una piattaforma di e-commerce

> 📄 Fonte: [[04_Agile_02.pdf#page=23]]

| Parte | Contenuto della slide | Risposta alla domanda di p. 22 🧩 |
|---|---|---|
| **Visione** | permettere ai clienti di acquistare prodotti online in modo rapido, sicuro e semplice da qualsiasi dispositivo | quale problema: acquistare online senza attrito |
| **Utenti** | clienti; amministratori del negozio | per chi |
| **Valore** | ridurre il tempo per completare un acquisto; aumentare le vendite online; migliorare l'esperienza del cliente | quale valore e, con le prime due voci misurabili, come misurare il successo |

> 🧩 Elaborazione mia — la slide non risponde esplicitamente alla quarta domanda («come sapremo se ha successo?»): i valori «ridurre il tempo di acquisto» e «aumentare le vendite» sono però **misurabili** e fanno da criterio di successo. Lo stesso e-commerce è l'esempio del Product Backlog nelle pagine seguenti ([[product-backlog-e-sprint-backlog]]): ogni voce del backlog (login, ricerca, carrello, checkout…) si giustifica rispetto a questa visione.

### Inception e formazione del team

> 📄 Fonte: [[04_Agile_02.pdf#page=24]]

Nell'inception si forma il team. Un **Scrum Team deve essere cross-funzionale**: devono essere presenti **tutte le competenze necessarie a produrre un incremento**. La slide elenca i profili (con icone): **Developer, UX, Tester, DBA, DevOps, Security …**. Il team **si auto-organizza** assegnandosi le varie responsabilità.

**Chi fa il Product Owner?** Lo si sceglie tra: il **cliente**; un **Business Analyst**; un **Product Manager**; un **istruttore** (nel vostro laboratorio); un **senior developer con profonda conoscenza del dominio**. Il PO **comprende i bisogni degli stakeholder, decide le priorità, mantiene il Product Backlog e massimizza il valore del prodotto**.

> 🧩 Elaborazione mia — «tutte le competenze necessarie» significa che il team non dipende da altri per completare una storia: un team di soli programmatori non potrebbe portare a «fatto» una storia che richiede test, database e deployment (cfr. la Definition of Done in [[product-backlog-e-sprint-backlog]]). Nel progetto di corso il PO ruota tra i membri del gruppo a ogni iterazione, mentre la slide elenca figure che di solito stanno fuori dal team: la rotazione è una scelta didattica del corso, non una pratica di Scrum.

## Perché importa

Collega Scrum al **ciclo di progetto**: dove si progetta l'architettura (inception), quando si costruisce (sprint) e quando si chiude (transition). La product vision è il «filo» a cui legare le decisioni, utile anche per giustificare all'orale le scelte architetturali ([[progetto-di-corso]]).

> 🎯 Esame: le tre macro-fasi con le uscite dell'inception; le quattro domande della product vision; cross-funzionalità del team; chi può essere PO.

## Connessioni

- [[scrum]]: ruoli e Sprint.
- [[product-backlog-e-sprint-backlog]]: il Product Backlog iniziale è un'uscita dell'inception.
- [[progetto-di-corso]]: l'iterazione 1 del corso è «architectural inception».

## Fonti

- [[agile-scrum-framework]] — [[04_Agile_02.pdf#page=20]]–[[04_Agile_02.pdf#page=24]]

_Aggiornato: 2026-10-22 — ingest 04_Agile_02.pdf_
