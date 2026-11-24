---
tipo: esercizio
argomento: "Sprint Retrospective: dalle osservazioni alle azioni di miglioramento"
difficoltà: bassa
---

# Condurre una retrospettiva

## Metodo

Quando: alla **fine di ogni Sprint**, dopo la Sprint Review, con PO, Scrum Master e Development Team ([[daily-scrum-review-retrospective]]; [[04_Agile_02.pdf#page=64]]).

1. **Osserva** i fatti dello Sprint (cosa è andato bene, cosa è andato male) con le prime due domande di p. 65.
2. Per ogni problema cerca la **causa** (non fermarti al sintomo).
3. Scegli **un'azione concreta e verificabile** per lo Sprint successivo, che agisca sulla causa.
4. **Limita a 2–3 azioni** in tutto: «provare a migliorare tutto insieme porta quasi sempre a nessun miglioramento; meglio poche azioni chiare e verificabili» ([[04_Agile_02.pdf#page=67]]).

**Concetti usati:** [[daily-scrum-review-retrospective]], [[product-backlog-e-sprint-backlog]] (refinement, criteri di accettazione, DoD), [[stima-story-points-velocity-capacity]] (stime, velocity), [[sprint-e-sprint-planning]] (Sprint Goal), [[user-stories]].

## Casi svolti

### Caso 1 — La tabella «osservazione → causa → azione»

**Traccia:** [[04_Agile_02.pdf#page=66]] — tabella a tre colonne (*Observation*, *Possible cause*, *Action for the next Sprint*) con otto righe, usata come esempio di retrospettiva.

**Svolgimento:** per ogni riga si individua **a che elemento di Scrum** si collega la causa (colonna aggiunta da me 🧩) e **perché l'azione funziona**:

| # | Osservazione | Possibile causa | Azione per il prossimo Sprint | Perché agisce sulla causa 🧩 |
|---|---|---|---|---|
| 1 | Abbiamo iniziato troppe user story contemporaneamente | Troppo **Work in Progress (WIP)** | Limitare a **due** le storie in «In Progress» | un limite al WIP costringe a finire prima di iniziare; più storie chiuse = più velocity ([[stima-story-points-velocity-capacity]]) |
| 2 | I test si sono fatti solo negli ultimi due giorni | Il **tester** è stato coinvolto troppo tardi | Coinvolgere il tester **dall'inizio** di ogni storia | i test diventano parte del lavoro di ogni storia e non un collo di bottiglia finale (DoD: «testata», [[product-backlog-e-sprint-backlog]]) |
| 3 | Alcune user story erano poco chiare | **Criteri di accettazione insufficienti** | **Raffinare di più** il Product Backlog prima dello Sprint Planning | la storia non è «Ready» (chiara, con criteri); si interviene sul refinement |
| 4 | Le nostre stime erano troppo ottimistiche | I **requisiti non erano ben compresi** | Fare **più domande** nel Backlog Refinement e coinvolgere più attivamente il PO | stime fatte su una storia non capita sono sbagliate ([[planning-poker]]: passo «Ask questions») |
| 5 | Il PO aveva disponibilità limitata | **Comunicazione scarsa** | Fissare una **sessione settimanale regolare** di Backlog Refinement | si crea un appuntamento fisso invece di cercare il PO a caso |
| 6 | Abbiamo trovato molti bug durante la demo | **Mancavano code review e test continui** | Introdurre **code review obbligatorie** e **Continuous Integration** | il difetto si trova prima della Review; la CI è citata a p. 11 come pratica tecnica compatibile con Scrum ([[scrum]]) |
| 7 | Il Daily Scrum è durato 30 minuti | Si è **cercato di risolvere i problemi durante la riunione** | Tenere il Daily **entro 15 minuti** e discutere i dettagli tecnici **subito dopo** | rispetta il timebox e i miti sul Daily ([[daily-scrum-review-retrospective]]) |
| 8 | Non abbiamo raggiunto lo Sprint Goal | Abbiamo **preso troppo lavoro** | Pianificare **meno Story Point** per il prossimo Sprint | si calibra la selezione su velocity e capacity ([[sprint-e-sprint-planning]]) |

**Soluzione, con motivazione:** ogni azione della tabella è **specifica, applicabile nello Sprint seguente e verificabile** (un limite numerico, una riunione fissa, una pratica obbligatoria). Nella tabella emergono tre famiglie di cause: **(a) flusso del lavoro** (righe 1, 2), **(b) preparazione del backlog** (righe 3, 4, 5), **(c) qualità e disciplina degli eventi** (righe 6, 7, 8) 🧩. Non è un elenco da applicare tutto insieme: per la regola delle 2–3 azioni, in una vera retrospettiva se ne sceglie una per famiglia, quella con l'impatto maggiore.

### Caso 2 — Retrospettiva su un vostro progetto passato

**Traccia:** [[04_Agile_02.pdf#page=67]] — «Conduct a retrospective on one of your past projects»: *Qual è stato il problema più frustrante che hai incontrato? Quale azione concreta introdurresti per evitare che si ripeta?* Nota: **ogni retrospettiva dovrebbe produrre al massimo 2–3 azioni di miglioramento.**

**Svolgimento:** il PDF non fornisce una soluzione: è un esercizio personale. Il metodo per risponderci:

1. scegli **un** problema (il più frustrante) e scrivilo come **osservazione** misurabile («consegnavamo i test negli ultimi due giorni»);
2. chiediti **«perché?»** fino alla causa su cui puoi agire (come nella colonna *Possible cause*);
3. formula **un'azione per lo sprint successivo**, con numero o data («limite di due storie in corso», «refinement ogni martedì»);
4. controlla che l'azione sia **verificabile** alla retrospettiva successiva.

> 🧩 Elaborazione mia — questo caso va svolto **in modo personale**: l'esame valuta il contributo individuale e la capacità di giustificare le scelte ([[00_IntroduzioneAlCorso_SAD.pdf#page=29]]). Nel progetto di corso la retrospettiva segue ogni review e deve produrre **1–3 azioni** ([[guida-progetto-picus]]); questa tabella è un buon modello per annotarle.

## Trappole

- **Troppe azioni**: più di 2–3 e non se ne attua nessuna (p. 67).
- **Azioni vaghe** («comunicare meglio»): non verificabili; la tabella di p. 66 usa sempre un'azione concreta.
- **Confondere Review e Retrospective**: la Review è sul **prodotto** con gli stakeholder; la Retrospective sul **modo di lavorare**, del solo team ([[04_Agile_02.pdf#page=63]]).
- **Fermarsi al sintomo** («Daily troppo lungo») senza la causa («si risolvevano i problemi in riunione»).

## Fonti

- [[agile-scrum-framework]] — [[04_Agile_02.pdf#page=65]]–[[04_Agile_02.pdf#page=67]]

_Aggiornato: 2026-10-22 — ingest 04_Agile_02.pdf_
