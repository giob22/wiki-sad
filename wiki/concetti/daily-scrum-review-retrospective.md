---
tipo: concetto
importanza_esame: alta
prerequisiti: ["scrum", "sprint-e-sprint-planning"]
fonti_pdf: ["04_Agile_02.pdf#page=55", "04_Agile_02.pdf#page=56", "04_Agile_02.pdf#page=57", "04_Agile_02.pdf#page=58", "04_Agile_02.pdf#page=59", "04_Agile_02.pdf#page=60", "04_Agile_02.pdf#page=61", "04_Agile_02.pdf#page=62", "04_Agile_02.pdf#page=63", "04_Agile_02.pdf#page=64", "04_Agile_02.pdf#page=65"]
termine_inglese: "Daily Scrum, Sprint Review, Sprint Retrospective"
---

# Daily Scrum, Sprint Review e Sprint Retrospective

## Definizione

Tre dei cinque eventi di Scrum ([[sprint-e-sprint-planning]]), ciascuno con uno scopo di ispezione e adattamento diverso:

| Evento | Cosa ispeziona / adatta | Quando | Durata (timebox) | Partecipanti | Fonte |
|---|---|---|---|---|---|
| **Daily Scrum** | **il progresso verso lo Sprint Goal**: si sincronizza il lavoro e si pianificano le prossime 24 ore | **ogni giorno** dello Sprint, **stessa ora**, **stesso luogo** (fisico o virtuale) | **15 minuti** | **Development Team** (nell'infografica: «Developers») | [[04_Agile_02.pdf#page=55]], [[04_Agile_02.pdf#page=56]] |
| **Sprint Review** | **l'Incremento completato**; si adatta il **Product Backlog** | **a fine Sprint, prima della Retrospective** | **al massimo 4 ore** per uno Sprint di un mese | Scrum Team **e stakeholder** | [[04_Agile_02.pdf#page=60]], [[04_Agile_02.pdf#page=61]] |
| **Sprint Retrospective** | **il modo di lavorare** del team; si adatta il **processo** | **a fine Sprint**, dopo la Review | **al massimo 3 ore** per uno Sprint di un mese; proporzionalmente meno per sprint più brevi | Product Owner, Scrum Master, Development Team | [[04_Agile_02.pdf#page=64]] |

> 🧩 Elaborazione mia — durate per sprint di 2 settimane (come nel progetto di corso): assumendo «un mese» = 4 settimane, i massimi diventano **2 ore** per la Review e **1,5 ore** per la Retrospective ($4\,\text{h}\cdot\tfrac{2}{4}$ e $3\,\text{h}\cdot\tfrac{2}{4}$). Le slide dicono solo «proporzionalmente meno».

La Sprint Review **migliora il prodotto**, la Sprint Retrospective **migliora il modo di lavorare del team** ([[04_Agile_02.pdf#page=63]]).

## Spiegazione

### Daily Scrum

> 📄 Fonte: [[04_Agile_02.pdf#page=55]]–[[04_Agile_02.pdf#page=57]]

Nel Daily Scrum il Development Team **sincronizza il proprio lavoro** e **pianifica le attività del giorno** per avvicinarsi allo Sprint Goal. **Non è un resoconto** ma serve a: **verificare il progresso verso lo Sprint Goal; individuare impedimenti; coordinare il lavoro del team; adattare il piano per le prossime 24 ore.**

![[lez07-ag2-p55-daily-scrum.png]]
*Figura di [[04_Agile_02.pdf#page=55]], infografica «Daily Scrum — Inspect progress toward the Sprint Goal and adapt the plan for the next 24 hours». In alto tre «pillole»: **15 minutes**, **every day of the Sprint**, **same time**, **same place, physical or virtual**. Al centro il bersaglio **Sprint Goal** e un gruppo davanti a una lavagna a colonne (To Do / In Progress / Done). Intorno, quattro passi in cerchio: **1 Check progress** (stiamo andando verso lo Sprint Goal?), **2 Identify impediments** (cosa blocca il nostro progresso?), **3 Coordinate work** (come lavoriamo insieme in modo efficace?), **4 Adapt the plan** (cosa faremo nelle prossime 24 ore?). Banda finale: **«A planning conversation, not a status report. Outcome: an actionable plan for the next working day.»***

#### Come è cambiato nel tempo

> 📄 Fonte: [[04_Agile_02.pdf#page=57]]

| | **Ieri** | **Oggi** |
|---|---|---|
| Domande | «Cosa hai fatto ieri? Cosa farai oggi? Quali problemi hai?» | «A che punto siamo rispetto allo Sprint Goal?» · «Cosa dobbiamo fare oggi per avvicinarci all'obiettivo?» · «Ci sono impedimenti che possono rallentare lo Sprint?» |
| Focus | i **task individuali** | l'**esito del team** |

La slide conclude: «il focus passa dai task individuali al risultato del team».

> 🧩 Elaborazione mia — perché cambiare: con le tre domande individuali ognuno racconta il proprio lavoro a turno e il meeting diventa una serie di rapporti; con le domande sull'obiettivo il team ragiona **insieme** su cosa serve al traguardo (per esempio: «due storie sono in test e una è bloccata: chi aiuta?»).

#### La scrum board al centro

> 📄 Fonte: [[04_Agile_02.pdf#page=58]]

![[lez07-ag2-p58-daily-scrum-board.png]]
*Figura di [[04_Agile_02.pdf#page=58]], «Daily Scrum: the scrum board at the center» («Every day, at the same time and place, the team inspects progress and adapts its plan»). Catena in alto: **Sprint Goal** (il fuoco condiviso del team) → **Scrum Board** (rende il lavoro visibile: un *information radiator*) → **Daily Scrum** (si ispeziona la board, si individuano gli impedimenti, si adatta il piano delle 24 ore successive).*

Contenuto dell'infografica:

- **Sprint Goal** dell'esempio: *«Enable users to recover their password securely and easily»*.
- **Scrum board** con quattro colonne e post-it: **To Do** — *MFA*, *Attempt audit log*, *User notifications*; **In Progress** — *Password recovery (reset email)*, *Login*, *Token validation*; **Test** — *Password reset*, *Complex password*; **Done** — *User registration*, *Login*, *Profile update*.
- **Daily Scrum basics**: timebox 15 minuti; partecipanti: sviluppatori; stesso orario e luogo, fisico o virtuale; focus: progresso verso lo Sprint Goal, impedimenti, le prossime 24 ore; «una conversazione di pianificazione, non un resoconto di stato».
- **Using the board during the Daily**: ispezionare la board insieme, **da destra a sinistra** (cioè dalle cose più vicine a «fatto»); individuare impedimenti e colli di bottiglia, come **troppo lavoro in corso**; concordare cosa completare oggi per avanzare verso lo Sprint Goal; adattare il piano per le prossime 24 ore.
- **Guiding questions**: come stiamo progredendo verso lo Sprint Goal? Quali impedimenti bloccano il nostro lavoro? Cosa possiamo fare oggi per spostare il lavoro verso DONE?
- **Example conversation**: Marco — «sto integrando il link di reset ma ho un problema col token»; Sara — «posso aiutarti dopo il Daily»; Luca — «oggi finisco i test del reset della password»; **decisione**: Marco e Sara lavoreranno insieme subito dopo il Daily per risolvere il problema del token.
- **Outcome**: allineamento, collaborazione, piano chiaro per le prossime 24 ore → migliore collaborazione, individuazione precoce dei problemi, più valore consegnato, focus sullo Sprint Goal.

> 🧩 Elaborazione mia — come leggere la board dell'esempio: tre note sono **Done**, **cinque** sono in avanzamento (tre in progress, due in test) e **tre** sono ancora da iniziare. Ispezionando da destra a sinistra si guardano prima *Test* (Password reset e Complex password sono a un passo dal Done: servono a chiudere lo Sprint Goal) e poi *In Progress*, dove «Token validation» è probabilmente la nota bloccata dell'esempio (il token di Marco). Le tre note da iniziare (MFA, audit log, notifiche) non sono necessarie all'obiettivo «recuperare la password»: 🧩 candidate per essere tagliate se il tempo non basta (→ forecast, [[sprint-e-sprint-planning]]).
> ❓ Nella board compare una nota «Login» sia in *In Progress* sia in *Done* (con colori diversi: verde e azzurro); le slide non spiegano il significato dei colori né le due note.

#### Falsi miti sul Daily Scrum

> 📄 Fonte: [[04_Agile_02.pdf#page=59]]

| ❌ Mito | ✅ Realtà |
|---|---|
| È la riunione dello Scrum Master | È la riunione del **Development Team** |
| Serve per fare report | Serve a **pianificare le prossime 24 ore** |
| Ognuno parla del proprio lavoro | Il team **riesamina il flusso di lavoro sulla scrum board** |
| Serve a controllare le persone | **Facilita il coordinamento** per raggiungere lo Sprint Goal |
| I problemi si risolvono durante il Daily | I problemi **si individuano nel Daily** e si affrontano **subito dopo**, coinvolgendo **solo le persone interessate** |

> 🧩 Elaborazione mia — l'ultima riga spiega il timebox di 15 minuti: se si discute ogni problema in plenaria la riunione sfora (come nell'esempio di retrospettiva «il Daily è durato 30 minuti», [[condurre-una-retrospettiva]]); l'esempio della conversazione (Marco e Sara dopo il Daily) è l'applicazione.

### Sprint Review

> 📄 Fonte: [[04_Agile_02.pdf#page=60]], [[04_Agile_02.pdf#page=62]]

La Sprint Review è un **incontro informale**, di **al più quattro ore per uno Sprint di un mese**, in cui **Scrum Team e stakeholder collaborano per ispezionare l'incremento completato** e, se necessario, **adattare il Product Backlog** per cogliere nuove opportunità. In base a quanto realizzato nello Sprint e ai cambiamenti del backlog, i partecipanti **decidono cosa si può fare per ottimizzare il valore del prodotto**. Le decisioni di ottimizzazione dipendono anche da **cambiamenti di mercato**, **possibile uso del prodotto**, **budget e tempo** per gli Sprint successivi. **Esito:** un **Product Backlog rivisto** che definisce il lavoro probabilmente selezionato per il prossimo Sprint.

> 🔑 Definizione chiave — **«La Sprint Review non è una DEMO!»**: è un'occasione per **ispezionare il prodotto, raccogliere feedback e aggiornare il backlog** ([[04_Agile_02.pdf#page=62]]).

![[lez07-ag2-p61-sprint-review.png]]
*Figura di [[04_Agile_02.pdf#page=61]], infografica in due parti. **1 — Sprint Review: what it is** («Inspect the Increment. Get feedback. Adapt the Product Backlog»): cos'è (sessione di lavoro informale in cui Scrum Team e stakeholder ispezionano l'Incremento a fine Sprint e decidono come adattare il Product Backlog per massimizzare il valore); quando e quanto dura (a fine Sprint, prima della Retrospective; fino a 4 ore per Sprint di un mese); chi partecipa (Scrum Team — Developers, Product Owner, Scrum Master — e **stakeholder chiave**: clienti, utenti, management, altre parti interessate). Sequenza «What we do»: **Present the Increment** (gli sviluppatori mostrano cosa è stato fatto) → **Get feedback** (gli stakeholder fanno domande, commentano, suggeriscono miglioramenti, condividono nuove esigenze) → **Discuss & adapt** (si discutono cambiamenti di mercato, budget, tempo disponibile, priorità) → **Update the Product Backlog** (il PO aggiorna e riordina il backlog per cogliere opportunità e massimizzare il valore). **2 — Outcomes & benefits**: esito principale, un backlog **rivisto e ordinato** che informa cosa può essere selezionato per il prossimo Sprint; benefici: allineamento di team e stakeholder, migliore comprensione e trasparenza del prodotto, **decisioni basate sul valore e non solo sull'attività**, valore di prodotto massimizzato. Esempio **«Speed Boat Game»**: ogni funzionalità è un'isola da raggiungere; gli stakeholder hanno un budget limitato (tempo o denaro); insieme decidono quali isole visitare per prime per massimizzare il valore. Banda finale: «La Sprint Review è una conversazione collaborativa per decidere cosa fare dopo, basata sul valore per il cliente e su nuove informazioni — più di una demo di stato.»*

> 🧩 Elaborazione mia — Review e demo: nella Lezione 6 la «iteration demo» era presentata come la dimostrazione del valore e la raccolta di feedback con stakeholder opzionali ([[cerimonie-e-artefatti-agile]]); qui si precisa che la **demo dell'incremento è solo il primo passo** della Review. La Review ha anche un **output**: il backlog aggiornato. Nel gioco della barca (*Speed Boat*), il budget limitato impone di scegliere, e la scelta è proprio la **riprioritizzazione del backlog** che si fa nella Review.

### Sprint Retrospective

> 📄 Fonte: [[04_Agile_02.pdf#page=63]]–[[04_Agile_02.pdf#page=65]]

**Obiettivi** (p. 64): analizzare **come è stato condotto il lavoro** durante lo Sprint; individuare **punti di forza e aree di miglioramento**; **migliorare il processo di sviluppo**; **aumentare la qualità del prodotto** attraverso il miglioramento continuo. **Partecipanti:** PO, SM, Development Team. **Durata:** max 3 ore per uno Sprint di un mese, proporzionalmente meno per sprint più brevi.

Il team riflette su **tre domande** (p. 65):

| # | Domanda | Esempi della slide |
|---|---|---|
| 1 | **Cosa è andato bene?** | collaborazione efficace; stime realistiche; pochi bug; buona comunicazione |
| 2 | **Cosa si potrebbe migliorare?** | troppe user story aperte contemporaneamente; ritardi nei test; Product Backlog poco chiaro; dipendenze tra sviluppatori |
| 3 | **Cosa faremo esattamente nel prossimo Sprint?** | il team definisce **azioni di miglioramento**, ad esempio: limitare il **Work In Progress**; fare code review quotidiane; coinvolgere prima il Product Owner; scrivere i criteri di accettazione durante il Refinement; introdurre la programmazione in coppia per le storie più complesse |

La tabella «osservazione → causa → azione» e l'esercizio sono in [[condurre-una-retrospettiva]]. **Regola:** ogni retrospettiva dovrebbe produrre **al massimo 2–3 azioni** di miglioramento ([[04_Agile_02.pdf#page=67]]).

## Esempi espansi

Le figure di pp. 55, 58, 61 sono spiegate sopra; la tabella di p. 66 e l'esercizio di p. 67 sono in [[condurre-una-retrospettiva]]. Il confronto tra le quattro riunioni è riassunto nella figura di p. 68 inserita in [[sprint-e-sprint-planning]] (quattro riquadri: Daily Scrum, Sprint Planning, Sprint Review, Sprint Retrospective).

## Perché importa

Sono i tre momenti di **ispezione e adattamento** quotidiano (Daily), di **prodotto** (Review) e di **processo** (Retrospective): senza di essi la trasparenza non produrrebbe adattamento ([[scrum]]). Nel progetto di corso la Sprint Review in aula alle date di review e la retrospettiva subito dopo sono richieste; l'esame valuta anche il contributo individuale e il metodo Agile ([[00_IntroduzioneAlCorso_SAD.pdf#page=29]]).

> 🎯 Esame: scopo, partecipanti, durata e output di ciascun evento; i miti sul Daily Scrum; «la Review non è una demo»; differenza Review/Retrospective (prodotto vs processo); le tre domande della retrospettiva e la regola delle 2–3 azioni.

> ⚖️ Trade-off: **Daily breve vs completezza** — 15 minuti non bastano per risolvere i problemi, quindi la discussione tecnica si sposta subito dopo il Daily con chi serve; il prezzo è un'organizzazione più disciplinata.

## Connessioni

- [[sprint-e-sprint-planning]]: Planning e Sprint; figura riassuntiva delle quattro riunioni.
- [[product-backlog-e-sprint-backlog]]: il backlog che esce dalla Review; la DoD che definisce «Done» sulla board.
- [[stima-story-points-velocity-capacity]]: la velocity si misura alla fine dello Sprint.
- [[cerimonie-e-artefatti-agile]]: la versione della Lezione 6 delle quattro cerimonie.
- [[condurre-una-retrospettiva]] *(esercizio)*.

## Fonti

- [[agile-scrum-framework]] — [[04_Agile_02.pdf#page=55]]–[[04_Agile_02.pdf#page=65]], [[04_Agile_02.pdf#page=68]]

_Aggiornato: 2026-10-22 — ingest 04_Agile_02.pdf_
