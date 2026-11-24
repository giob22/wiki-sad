---
tipo: concetto
importanza_esame: alta
prerequisiti: ["scrum", "product-backlog-e-sprint-backlog"]
fonti_pdf: ["04_Agile_02.pdf#page=39", "04_Agile_02.pdf#page=40", "04_Agile_02.pdf#page=41", "04_Agile_02.pdf#page=42", "04_Agile_02.pdf#page=44", "04_Agile_02.pdf#page=45", "04_Agile_02.pdf#page=46"]
termine_inglese: "Scrum events, Sprint, Sprint Goal, Sprint Planning"
---

# Eventi Scrum, Sprint, Sprint Goal e Sprint Planning

## Definizione

> 📄 Fonte: [[04_Agile_02.pdf#page=39]]

Scrum usa **eventi prestabiliti** per creare **regolarità** e ridurre al minimo le riunioni non previste da Scrum. **Ogni evento è a tempo fisso** (*time-boxed*): la sua durata **non può essere cambiata una volta iniziato**. **Ogni evento è un'opportunità formale di ispezionare e adattare qualcosa** (→ pilastri in [[scrum]]).

Gli eventi sono cinque: **Sprint, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective**.

![[lez07-ag2-p68-cerimonie-scrum.png]]
*Figura di [[04_Agile_02.pdf#page=68]] («A final overview of Scrum ceremonies»): quattro riquadri colorati attorno a un disco centrale «Scrum Ceremonies» — **Daily Scrum Meeting** (arancio, in piedi davanti a una lavagna a colonne), **Sprint Planning Meeting** (azzurro, tavolo con persone e icone di idee), **Sprint Review Meeting** (rosa, persone davanti a un portatile), **Sprint Retrospective Meeting** (verde, tavolata con post-it). È la sintesi grafica delle quattro riunioni dentro lo Sprint, trattate in [[daily-scrum-review-retrospective]] (Daily, Review, Retrospective) e qui (Planning).*

La slide di p. 39 mostra anche il diagramma **«Scrum Activities»**: una linea chiusa a forma di anello su cui stanno, in sequenza, **1. Sprint Planning → 2. Daily Scrum** (con una freccia che si richiude su se stessa: ripetuto ogni giorno) **→ 3. Sprint Review → 4. Sprint Retrospective** e poi di nuovo il Planning; **fuori dall'anello**, in alto, la casella **5. Product Backlog Refinement**: è un'attività continua, non un evento in sequenza (→ [[product-backlog-e-sprint-backlog]]).

## Spiegazione

### Lo Sprint

> 📄 Fonte: [[04_Agile_02.pdf#page=40]]

- Ogni Sprint ha **un obiettivo da raggiungere**, **un piano flessibile** per arrivarci, il **lavoro svolto** e il **risultato**; comincia **subito dopo la fine** dello Sprint precedente.
- **Uno Sprint troppo lungo** permette che **la definizione di ciò che si sta costruendo cambi**, aumentando **complessità e rischio**.
- Il lavoro da fare (definito nello Sprint Backlog) **non è un obbligo ma una previsione** (*forecast*): **l'unico contenitore fisso nello Sprint è il timebox, non il lavoro pianificato**.

> 🧩 Elaborazione mia — il vincolo si legge così: a **data di fine fissa** (timebox) il **contenuto può variare**. Se il lavoro previsto non basta, non si allunga lo sprint: si riduce lo scopo (e il PO ne decide gli effetti sul backlog). È il motivo per cui la figura di p. 69 dice «sprint end date and team deliverable do not change» e per cui la capacità e la velocity servono a **non promettere troppo** ([[stima-story-points-velocity-capacity]]). La durata «breve» riduce il rischio di cambiare il bersaglio a metà strada.

### Lo Sprint Goal

> 📄 Fonte: [[04_Agile_02.pdf#page=41]]

**Uno Sprint non è una collezione casuale di user story**: è un insieme di storie che **insieme permettono di raggiungere uno specifico obiettivo di business che genera valore**. Lo **Sprint Goal** è l'**obiettivo dello Sprint** e **le storie selezionate devono contribuire a raggiungerlo**.

#### Esempi: quando c'è un obiettivo e quando no

> 📄 Fonte: [[04_Agile_02.pdf#page=42]]

| Selezione per lo Sprint | Obiettivo? |
|---|---|
| Login · PayPal · PDF Report · Dashboard · Translation | **«What is the Goal? Beats me!!»**: non c'è un obiettivo comune; sono cinque funzioni scollegate |
| Cart · Checkout · Payment · Order confirmation | **Obiettivo chiaro: permettere ai clienti di completare un acquisto online** |

> 🧩 Elaborazione mia — la prova pratica: si prova a formulare **una frase** che spieghi perché quelle storie stanno insieme. Nel secondo caso le quattro storie sono i passi di **uno stesso flusso** (dal carrello alla conferma): finché una manca, il cliente non riesce a comprare, quindi il valore si ottiene solo con tutte. Nel primo caso togliere o aggiungere una voce non cambia nulla. È la stessa logica dell'«obiettivo dello sprint: checkout fluido» con cui nella Lezione 6 si sceglievano le quattro storie della lavagna ([[cerimonie-e-artefatti-agile]]). Un obiettivo coerente è anche ciò che permette di decidere cosa **tagliare** se il tempo non basta: si taglia ciò che sposta meno l'obiettivo.

### Sprint Planning

> 📄 Fonte: [[04_Agile_02.pdf#page=44]] (p. 43 è la slide-titolo)

- Lo **Sprint Planning** individua lo **Sprint Goal** e il **lavoro necessario a raggiungerlo**.
- Il lavoro è **scelto dal Product Backlog** e aggiunto allo **Sprint Backlog**.
- Il lavoro è pianificato dall'**intero Scrum Team**.
- L'evento è a tempo fisso e **la durata varia con la lunghezza dello Sprint**.

![[lez07-ag2-p45-sprint-planning.png]]
*Figura di [[04_Agile_02.pdf#page=45]], infografica «Sprint Planning — Define the Sprint Goal and plan the work needed to achieve it». In alto una casella **Sprint Goal** con una freccia verso la fine del processo. Tre riquadri numerati in sequenza: **1 Product Backlog** (il PO presenta gli elementi a priorità più alta, impilati dal più alto al più basso), **2 Discuss & Select** (gli sviluppatori valutano e scelgono le storie, con tre domande: supporta lo Sprint Goal? abbiamo abbastanza capacità? possiamo completarla nello Sprint?), **3 Sprint Backlog** (storie scelte + un piano per consegnarle, cioè i task con caselle da spuntare). In basso i **criteri di selezione**: Sprint Goal, stime delle storie, capacità disponibile, velocity passata (con la nota: «Past velocity informs the forecast; it is not a fixed commitment»); due note: «l'intero Scrum Team collabora» e «a tempo fisso: la durata dipende dalla lunghezza dello Sprint».*

> 📄 Fonte: [[04_Agile_02.pdf#page=46]]

Come si svolge: il **Product Owner presenta gli elementi a priorità più alta** del backlog; il **Development Team valuta le storie** con tre domande — **contribuiscono allo Sprint Goal? Abbiamo capacità sufficiente? Possiamo completarle nello Sprint?** — e **solo allora** alcune diventano parte dello Sprint Backlog. **La selezione si basa sullo Sprint Goal, sulle storie stimate e sulla velocity del team.**

| Criterio | Cosa si controlla 🧩 | Dove si approfondisce |
|---|---|---|
| **Sprint Goal** | le storie devono servire all'obiettivo | questa pagina |
| **Stime delle storie** | solo storie già stimate (per questo servono «Ready») | [[product-backlog-e-sprint-backlog]] |
| **Capacità disponibile** | le persone realmente disponibili nello sprint | [[stima-story-points-velocity-capacity]] |
| **Velocity passata** | quanti SP il team completa in media: **informa la previsione, non è un impegno fisso** | [[stima-story-points-velocity-capacity]] |

> 🧩 Elaborazione mia — esito: lo Sprint Planning produce **due cose**: l'obiettivo (Sprint Goal) e lo Sprint Backlog (storie scelte + task). Nella Lezione 6 la durata indicata per l'iteration planning era di **circa un'ora per ogni settimana** di iterazione ([[cerimonie-e-artefatti-agile]]): per una iterazione di 2 settimane circa 2 ore. Questo PDF non indica durate numeriche per il Planning, solo che varia con lo sprint. L'applicazione è in [[pianificare-uno-sprint]].

## Esempi espansi

Gli esempi (insiemi di storie a p. 42, criteri di selezione a p. 45, tabella degli stati delle storie a p. 33) sono spiegati sopra e nell'esercizio [[pianificare-uno-sprint]].

## Perché importa

Lo Sprint Planning è il punto in cui **backlog, stime, capacità e obiettivo** si incontrano: è dove un team Scrum decide che cosa promettere. Nel progetto di corso c'è un planning all'inizio di ogni iterazione (5/11, 19/11, 3/12) con obiettivo dello sprint e storie selezionate.

> 🎯 Esame: cinque eventi; timebox; «il lavoro è una previsione, il timebox è fisso»; cos'è lo Sprint Goal e perché non basta «un insieme di storie»; chi partecipa al Planning e come si selezionano le storie.

> ⚖️ Trade-off: **sprint lungo vs corto** — più lungo = più lavoro per sprint ma più rischio che il bersaglio cambi (p. 40); più corto = più feedback ma più eventi fissi.

## Connessioni

- [[product-backlog-e-sprint-backlog]]: input (backlog «Ready») e output (Sprint Backlog) del Planning.
- [[stima-story-points-velocity-capacity]]: numeri che guidano la selezione.
- [[daily-scrum-review-retrospective]]: gli altri tre eventi.
- [[cerimonie-e-artefatti-agile]]: versione generale delle cerimonie nella Lezione 6.

## Fonti

- [[agile-scrum-framework]] — [[04_Agile_02.pdf#page=38]]–[[04_Agile_02.pdf#page=46]], [[04_Agile_02.pdf#page=68]]

_Aggiornato: 2026-10-22 — ingest 04_Agile_02.pdf_
