---
tipo: concetto
importanza_esame: alta
prerequisiti: []
fonti_pdf: ["04_Agile_01.pdf#page=3", "04_Agile_01.pdf#page=5", "04_Agile_01.pdf#page=6", "04_Agile_01.pdf#page=9", "04_Agile_01.pdf#page=10", "04_Agile_01.pdf#page=13", "04_Agile_01.pdf#page=16", "04_Agile_01.pdf#page=17", "04_Agile_01.pdf#page=18", "04_Agile_01.pdf#page=19", "04_Agile_01.pdf#page=20", "04_Agile_01.pdf#page=21"]
termine_inglese: "Agile development, Agile Manifesto"
---

# Sviluppo Agile

## Definizione

> 📄 Fonte: [[04_Agile_01.pdf#page=5]]

> 🔑 Definizione chiave: **Agile** è un **approccio iterativo** alla **gestione dei progetti** e allo **sviluppo dei prodotti** che permette ai team di:
> - **consegnare valore più in fretta**;
> - **ricevere feedback continuo**;
> - **ridurre il rischio di grandi errori** dovuti a una **pianificazione rigida**;
> - **adattarsi al cambiamento**.

L'idea centrale è **evitare il modello «big bang»** (un unico rilascio finale) e lavorare invece per **piccoli incrementi di valore**.

### Il problema da cui si parte

> 📄 Fonte: [[04_Agile_01.pdf#page=3]], [[04_Agile_01.pdf#page=4]]

La lezione si apre con un sondaggio sui problemi incontrati nei progetti passati: requisiti **poco chiari o cambiati** durante il progetto; stakeholder **assenti** e problemi di **comunicazione**; **stime dei tempi** non fatte o non rispettate; **problemi e ritardi imprevisti**; **poca chiarezza sull'avanzamento** del progetto. «Ecco perché oggi parliamo di Agile.»

🧩 Ogni problema del sondaggio ha una risposta Agile che si vedrà nella lezione: requisiti che cambiano → iterazioni brevi e backlog riordinabile; stakeholder assenti → demo a fine iterazione; stime sbagliate → storie piccole stimate dal team; avanzamento poco chiaro → burndown chart e daily meeting ([[cerimonie-e-artefatti-agile]]).

## Il Manifesto Agile

### I quattro valori

> 📄 Fonte: [[04_Agile_01.pdf#page=6]], [[04_Agile_01.pdf#page=7]], [[04_Agile_01.pdf#page=8]]

*«Stiamo scoprendo modi migliori di sviluppare software facendolo e aiutando altri a farlo. Grazie a questo lavoro siamo arrivati a dare valore a:»*

| Diamo più valore a… | …che a |
|---|---|
| **individui e interazioni** | processi e strumenti |
| **software funzionante** | documentazione esaustiva |
| **collaborazione con il cliente** | negoziazione dei contratti |
| **rispondere al cambiamento** | seguire un piano |

*«Cioè, pur riconoscendo valore alle voci a destra, diamo più valore alle voci a sinistra.»*

![[lez06-ag-p6-valori-manifesto.png]]
*Figura di [[04_Agile_01.pdf#page=6]]: il testo originale dei quattro valori del Manifesto, in inglese.*

![[lez06-ag-p7-valori-manifesto-infografica.png]]
*Figura di [[04_Agile_01.pdf#page=7]], «Manifesto per lo sviluppo agile di software — i quattro valori cardine» (in italiano): quattro colonne, ognuna con in alto il valore preferito e in basso quello che passa in secondo piano. **Individui e interazioni** (teamwork, comunicazione, fiducia) sopra **processi e strumenti**; **software funzionante** (qualità, test, rilasci rapidi, feedback) sopra **documentazione esaustiva**; **collaborazione col cliente** (visione condivisa, valore) sopra **negoziazione dei contratti** (avvocati, «red tape»); **risposta al cambiamento** (adattabilità, lessons learned, evoluzione) sopra **seguire un piano** (piano fisso, roadmap rigida). In fondo i firmatari: Beck, Beedle, van Bennekum, Cockburn, Cunningham, Fowler, Grenning, Highsmith, Hunt, Jeffries, Kern, Marick, Martin, Mellor, Schwaber, Sutherland, Thomas.*

> 🧩 Elaborazione mia: la frase finale è il punto che si sbaglia più spesso. Il Manifesto **non** dice «niente documentazione» o «niente piano»: dice che, quando sono in conflitto, vince la voce a sinistra.

Domanda di riflessione della slide ([[04_Agile_01.pdf#page=8]]): *quale dei quattro valori, se applicato fin dall'inizio, avrebbe migliorato di più i tuoi progetti?*

### I dodici principi

> 📄 Fonte: [[04_Agile_01.pdf#page=9]], [[04_Agile_01.pdf#page=10]], [[04_Agile_01.pdf#page=11]]

| # | Principio | 🧩 Collegamento |
|---|---|---|
| 1 | La massima priorità è **soddisfare il cliente** con **consegne anticipate e continue** di software di valore | incrementi di valore |
| 2 | **Accogliere i cambiamenti dei requisiti**, anche a sviluppo avanzato: i processi Agile sfruttano il cambiamento a vantaggio competitivo del cliente | backlog riordinabile |
| 3 | **Consegnare spesso software funzionante**, da un paio di settimane a un paio di mesi, preferendo i tempi più brevi | iterazioni brevi (nel progetto di corso: 2 settimane) |
| 4 | Persone del business e sviluppatori devono **lavorare insieme ogni giorno** per tutto il progetto | Product Owner nel team |
| 5 | Costruire i progetti attorno a **persone motivate**; dare loro ambiente e supporto e **fidarsi** di loro | team auto-organizzato |
| 6 | Il metodo più efficiente ed efficace per trasmettere informazioni al e nel team è la **conversazione faccia a faccia** | daily meeting; la «conversazione» delle user story |
| 7 | Il **software funzionante** è la **misura principale del progresso** | demo a fine iterazione |
| 8 | I processi Agile promuovono uno **sviluppo sostenibile**: sponsor, sviluppatori e utenti devono poter mantenere un **ritmo costante** indefinitamente | stime realistiche |
| 9 | L'**attenzione continua all'eccellenza tecnica e al buon design** aumenta l'agilità | 💡 qui entra l'architettura |
| 10 | La **semplicità** — l'arte di **massimizzare il lavoro non fatto** — è essenziale | storie piccole, niente funzioni non richieste |
| 11 | Le **migliori architetture, requisiti e design** emergono da **team auto-organizzati** | 💡 architettura che evolve |
| 12 | A intervalli regolari il team **riflette su come diventare più efficace**, poi regola e adatta il proprio comportamento | retrospettiva |

In sintesi ([[04_Agile_01.pdf#page=11]]): **consegna continua di valore, collaborazione, semplicità, miglioramento continuo**.

![[lez06-ag-p9-principi-1.png]]
![[lez06-ag-p10-principi-2.png]]
*Figure di [[04_Agile_01.pdf#page=9]] e [[04_Agile_01.pdf#page=10]]: i dodici principi in riquadri colorati (sei per slide), trascritti nella tabella sopra.*

> 💡 Connessione: i principi 9 e 11 legano Agile al corso. L'architettura non si progetta tutta all'inizio («big design up front») ma **emerge ed evolve** per iterazioni; serve però **eccellenza tecnica e buon design** perché il sistema resti modificabile iterazione dopo iterazione ([[modifiability]]). È la motivazione §3.7 della Lez. 1: l'architettura abilita lo sviluppo incrementale, a partire da un sistema scheletro ([[importanza-architettura-software]]).

La slide [[04_Agile_01.pdf#page=12]] propone un «agility check» in aula (senza contenuto scritto).

## Come funziona

> 📄 Fonte: [[04_Agile_01.pdf#page=13]], [[04_Agile_01.pdf#page=14]], [[04_Agile_01.pdf#page=15]]

Il flusso è **Backlog → Priorità → Iterazione → Feedback → Miglioramento** ([[04_Agile_01.pdf#page=13]]).

**Agile divide il progetto in iterazioni** ([[04_Agile_01.pdf#page=14]]):
1. **Fare una lista** — con il cliente, la lista delle funzionalità che vorrebbe: diventa la lista delle cose da fare del progetto.
2. **Dimensionare** — stimare le attività **le une relativamente alle altre** e fare un'ipotesi su quanto durerà ciascuna.
3. **Stabilire le priorità** — chiedere al cliente di ordinare la lista, così si sviluppa prima ciò che conta di più.
4. **Iniziare a lavorare.**

![[lez06-ag-p14-progetto-in-iterazioni.png]]
*Figura di [[04_Agile_01.pdf#page=14]]: i quattro passi su riquadri neri con icone (lista, compasso, bersaglio, spunta).*

**Pianificazione dell'iterazione** ([[04_Agile_01.pdf#page=15]]): **selezione delle attività prioritarie** e **definizione dell'obiettivo dell'iterazione**.

![[lez06-ag-p15-iteration-planning.png]]
*Figura di [[04_Agile_01.pdf#page=15]]: a sinistra il blocco **Work** (Minimum Business Increments e Release Roadmap) — ① entra nel **Product Backlog**, alimentato anche dal **Business Backlog** (criteri, priorità, dimensionamento, sequenza). ② **Iteration Planning** sceglie «la giusta quantità di lavoro» che diventa ③ l'**Iteration Backlog** dentro il ciclo dell'**Iteration** (con il **Coordination Meeting**, la riunione giornaliera). A fine iterazione: **Demo**, **Retrospective** e **Iteration Review**, la cui freccia torna al Product Backlog.*

![[anim-ciclo-iterazione-agile.svg]]
*🧩 Animazione mia del ciclo di [[04_Agile_01.pdf#page=13]] e [[04_Agile_01.pdf#page=15]] (generata con `output/diagrammi/genera_grafici_lez06.py`): backlog ordinato → planning → lavoro con daily meeting → software funzionante → demo → retrospettiva e feedback che tornano nel backlog. Le singole cerimonie sono in [[cerimonie-e-artefatti-agile]].*

## Sviluppo iterativo ed evolutivo

> 📄 Fonte: [[04_Agile_01.pdf#page=16]], [[04_Agile_01.pdf#page=17]], [[04_Agile_01.pdf#page=18]]

- Lo sviluppo iterativo è organizzato come una **serie di mini-progetti brevi e di durata fissa** (es. tre settimane) chiamati **iterazioni**.
- **Ogni iterazione produce un sistema eseguibile, testato e integrato**, anche se parziale.
- Ogni iterazione comprende **analisi dei requisiti, progettazione, implementazione e test**.
- Il sistema **cresce e si raffina** a ogni iterazione grazie a **feedback e adattamento ciclici**.
- Per questo si parla di **sviluppo iterativo e incrementale**; è anche **evolutivo**, grazie a feedback e adattamento.

![[lez06-ag-p17-waterfall-vs-iterativo.png]]
*Figura di [[04_Agile_01.pdf#page=17]], «Waterfall vs. iterative». **«Not like this…»** (barrato): si consegnano una ruota (1), un asse con due ruote (2), un'auto senza carrozzeria (3) e infine l'auto (4); il cliente è scontento fino all'ultimo. **«Like this!»**: si consegnano uno skateboard (1), un monopattino (2), una bicicletta (3), una moto (4), un'auto (5); il cliente è sempre più soddisfatto.*

> 🧩 Elaborazione mia — cosa vuole dire la vignetta: nel primo caso ogni consegna è un **pezzo** che da solo non serve (si vede valore solo alla fine, «big bang»). Nel secondo ogni consegna è un **prodotto usabile**, più semplice, che risolve già il problema (spostarsi) e permette di raccogliere feedback. Attenzione: la vignetta mostra consegne *usabili*, non necessariamente che l'auto si costruisca riusando lo skateboard.

![[lez06-ag-p18-sviluppo-iterativo-evolutivo.png]]
*Figura di [[04_Agile_01.pdf#page=18]]: due iterazioni consecutive, ciascuna con Requirements → Design → Implementation & Test & Integration & More Design → Final Integration & System Test, della durata di **4 settimane (per esempio)**. Note: le iterazioni hanno **durata fissa** (*timeboxed*); il **feedback dell'iterazione N** porta a raffinare e adattare requisiti e design dell'iterazione **N+1**; **il sistema cresce in modo incrementale**.*

| | Waterfall | Iterativo ed evolutivo |
|---|---|---|
| Fasi | requisiti → progetto → implementazione → test, una volta sola | tutte le fasi dentro ogni iterazione |
| Consegna | una sola alla fine («big bang») | un sistema eseguibile, testato e integrato a ogni iterazione |
| Cambiamenti dei requisiti | costosi, scoperti tardi | accolti a ogni iterazione grazie al feedback |
| Rischio | emerge alla fine | emerge presto (si integra e si testa subito) |

Tabella 🧩 costruita sulle slide 16–18; il confronto tra modelli di processo (waterfall, Unified Process) è nel programma ([[Programma Syllabus]]) e non è ancora stato trattato in dettaglio. TODO: da espandere.

## Ruoli

> 📄 Fonte: [[04_Agile_01.pdf#page=19]], [[04_Agile_01.pdf#page=20]], [[04_Agile_01.pdf#page=21]]

**Agile non definisce ruoli specifici: li definiscono i framework** — Scrum, Kanban, Extreme Programming (XP), Disciplined Agile (DA), SAFe, LeSS ([[04_Agile_01.pdf#page=19]]).

Stessi obiettivi, nomi diversi ([[04_Agile_01.pdf#page=20]]):

| Responsabilità | Scrum | Disciplined Agile | XP | SAFe |
|---|---|---|---|---|
| Definisce il valore | Product Owner | Product Owner | Customer | Product Manager / Product Owner |
| Facilita il team | Scrum Master | Team Lead | Coach | Scrum Master |
| Costruisce il prodotto | Developers | Team Members | Programmers | Agile Team |
| Definisce l'architettura | Team | Architecture Owner | Team | System Architect |
| Fornisce feedback | Stakeholder | Stakeholder | Customer | Business Owner |

![[lez06-ag-p20-ruoli-agile.png]]
*Figura di [[04_Agile_01.pdf#page=20]]: la tabella originale, trascritta sopra.*

> 💡 Connessione: in Scrum e XP l'architettura è responsabilità **del team**, mentre Disciplined Agile e SAFe hanno un ruolo dedicato (Architecture Owner, System Architect). La Lez. 1 raccomandava un architetto o un piccolo gruppo di architetti per l'integrità concettuale ([[buone-pratiche-architetturali]]): i framework Agile più «grandi» recuperano proprio questo ruolo.

Le **tre responsabilità fondamentali** ([[04_Agile_01.pdf#page=21]]):

| Ruolo | Cosa fa | Motto |
|---|---|---|
| **Product Owner** | visione del prodotto, priorità, valore | «sviluppare il prodotto giusto» |
| **Scrum Master** | facilita il team, rimuove gli ostacoli, promuove Agile | «aiutare il team a lavorare bene» |
| **Development Team** | progetta, scrive il codice, testa, consegna | «costruire il prodotto nel modo giusto» |

![[lez06-ag-p21-tre-responsabilita.png]]
*Figura di [[04_Agile_01.pdf#page=21]]: tre frecce (arancione, rossa, viola) con i ruoli e, sotto, le loro attività e i motti, trascritti sopra.*

## Perché importa

È il blocco del programma su sviluppo Agile e gestione Agile dei progetti ([[Programma Syllabus]]) e il modo in cui si lavora nel **progetto di corso**: sprint di 2 settimane, iteration review, un tutor come Scrum Master ([[progetto-di-corso]]). Il progetto è metà del voto ed è sviluppato con metodo Agile.

> 🎯 Esame: definizione di Agile; i quattro valori con la frase finale; alcuni principi (soprattutto 3, 7, 9, 11, 12); iterativo vs waterfall; ruoli e tre responsabilità.

## Connessioni

- [[cerimonie-e-artefatti-agile]]: cerimonie (planning, daily, demo, retrospettiva) e artefatti (backlog, burndown).
- [[user-stories]]: come si scrivono i requisiti in Agile.
- [[progetto-di-corso]]: Agile applicato al progetto.
- [[scrum]] e [[gestione-progetto-plan-driven-vs-agile]]: il framework Scrum completo e perché serve una gestione di progetto (Lez. 7).
- [[importanza-architettura-software]]: §3.7, l'architettura abilita lo sviluppo incrementale.

## Fonti

- [[agile-project-management]] — [[04_Agile_01.pdf#page=1]]–[[04_Agile_01.pdf#page=21]]

_Aggiornato: 2026-10-10 — ingest 04_Agile_01.pdf_
_Aggiornato: 2026-10-22 — rinvio alla Lezione 7 (Scrum)_
