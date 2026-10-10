---
tipo: concetto
importanza_esame: alta
prerequisiti: ["sviluppo-agile"]
fonti_pdf: ["04_Agile_01.pdf#page=22", "04_Agile_01.pdf#page=23", "04_Agile_01.pdf#page=24", "04_Agile_01.pdf#page=25", "04_Agile_01.pdf#page=26", "04_Agile_01.pdf#page=27", "04_Agile_01.pdf#page=28", "04_Agile_01.pdf#page=29", "04_Agile_01.pdf#page=30", "04_Agile_01.pdf#page=31"]
termine_inglese: "Agile ceremonies and artefacts"
---

# Cerimonie e artefatti Agile

## Definizione

> 📄 Fonte: [[04_Agile_01.pdf#page=22]], [[04_Agile_01.pdf#page=28]]

- Le **cerimonie** (*ceremonies*) sono gli incontri ricorrenti che scandiscono ogni iterazione: **planning, daily meeting, demo, retrospettiva**.
- Gli **artefatti** (*artefacts*) sono gli strumenti con cui il team organizza e rende visibile il lavoro: **product backlog, iteration backlog, user story, burndown chart**.

## Le quattro cerimonie

> 📄 Fonte: [[04_Agile_01.pdf#page=23]]–[[04_Agile_01.pdf#page=27]]

| Cerimonia | Scopo (slide) | Partecipanti | Frequenza | Durata | Obiettivo |
|---|---|---|---|---|---|
| **Iteration planning** (in Scrum *sprint planning*) | definire il lavoro e l'obiettivo dell'iterazione; scegliere le attività prioritarie, le storie e i task concreti della prossima iterazione | membri del team, team lead, product owner | all'inizio di ogni iterazione | circa un'ora per ogni settimana di iterazione | preparare il team al successo: PO e team discutono product backlog e iteration backlog e quanto lavoro completare |
| **Daily meeting** (*daily coordination meeting*) | allineamento rapido su avanzamento, ostacoli e prossimi passi | membri del team, team lead, product owner | una volta al giorno, a un orario comodo per il team | circa 15 minuti | incontro leggero e veloce: far sapere al team cosa è stato completato, cosa è in corso e cosa è bloccato |
| **Iteration demo** (*iteration demonstration*) | presentare il valore generato e raccogliere feedback | membri del team, team lead, PO; stakeholder (opzionali) | alla fine dell'iterazione | circa 30–60 minuti | mostrare il lavoro fatto dal team nell'iterazione |
| **Retrospective** (*iteration retrospective*) | riflettere sul processo e decidere azioni di miglioramento | membri del team, team lead, PO | alla fine dell'iterazione | circa 60 minuti | aiutare il team a capire cosa funziona e cosa no |

Fonti per riga: [[04_Agile_01.pdf#page=24]], [[04_Agile_01.pdf#page=25]], [[04_Agile_01.pdf#page=26]], [[04_Agile_01.pdf#page=27]].

![[lez06-ag-p24-iteration-planning-tabella.png]]
![[lez06-ag-p25-daily-meeting.png]]
![[lez06-ag-p26-iteration-demo.png]]
![[lez06-ag-p27-retrospective.png]]
*Figure di [[04_Agile_01.pdf#page=24]]–[[04_Agile_01.pdf#page=27]]: per ogni cerimonia una tabella con partecipanti, frequenza, durata e obiettivo, trascritte sopra.*

> 🧩 Elaborazione mia — **demo e retrospettiva sono due cose diverse**, entrambe a fine iterazione:
> - la **demo** guarda al **prodotto** («abbiamo costruito la cosa giusta?»), con gli stakeholder, e produce feedback sul backlog;
> - la **retrospettiva** guarda al **processo** («abbiamo lavorato bene?»), solo il team, e produce azioni di miglioramento del modo di lavorare. È il principio 12 del Manifesto ([[sviluppo-agile]]).
>
> Esempio di calcolo dalla regola «un'ora per settimana»: con sprint di **2 settimane** (come nel [[progetto-di-corso]]) l'iteration planning dura circa **2 ore**.

## Gli artefatti

> 📄 Fonte: [[04_Agile_01.pdf#page=29]]

| Artefatto | Definizione |
|---|---|
| **Product Backlog** | la lista del lavoro necessario per creare il prodotto; raccoglie tutto il lavoro che arriva al team. Il **product owner lo ordina per priorità**, indicando al team quale lavoro è più importante |
| **Iteration Backlog** | la lista del lavoro da completare in un'iterazione, nell'ordine deciso **dal team** |
| **Burndown Chart** | rappresentazione grafica di quanto velocemente il team procede negli elementi di lavoro; mostra lo sforzo totale per ogni iterazione |
| **User Story** | strumento per descrivere una funzionalità dal punto di vista dell'utente finale: che tipo di utente, cosa vuole e perché; aiuta a creare una descrizione semplificata di un requisito → [[user-stories]] |

![[lez06-ag-p29-artefatti.png]]
*Figura di [[04_Agile_01.pdf#page=29]]: tabella arancione con i quattro artefatti, trascritta sopra.*

### Esempio: product backlog e sprint backlog

> 📄 Fonte: [[04_Agile_01.pdf#page=30]]

![[lez06-ag-p30-product-sprint-backlog.png]]
*Figura di [[04_Agile_01.pdf#page=30]] (in italiano), una lavagna con due colonne. **Product Backlog** — «elenco prioritizzato di tutte le funzionalità desiderate dal cliente»: otto user story numerate per priorità (1 login sicuro, 2 cercare prodotti per nome o categoria, 3 aggiungere prodotti al carrello, 4 pagare con carta di credito, 5 ricevere email di conferma dell'ordine, 6 tracciare l'ordine, 7 salvare prodotti nei preferiti, 8 contattare l'assistenza, …). Una freccia porta allo **Sprint Backlog** — «lavoro selezionato per lo Sprint (obiettivo dello Sprint: Checkout fluido)»: quattro storie (login, carrello, pagamento con carta, email di conferma) e i **task** in cui sono divise (creare form di login, implementare autenticazione JWT, design pagina carrello, API per aggiungere/rimuovere prodotti, integrare gateway di pagamento, gestire esito pagamento, inviare email di conferma, scrivere test automatici). In basso la **Definizione di Fatto (DoD)**: codice sviluppato, test unitari passati, code review completata, documentazione aggiornata, funzionalità demo-ready.*

> 🧩 Elaborazione mia — cosa mostra l'esempio:
> - l'**obiettivo dello sprint** («checkout fluido») guida la scelta: non si prendono semplicemente le prime quattro storie per priorità, ma quelle che insieme realizzano l'obiettivo (la n. 2, ricerca prodotti, resta fuori; entra la n. 5, email di conferma);
> - nello sprint backlog le storie sono **scomposte in task tecnici**, che il team gestisce da sé;
> - la **DoD** vale per tutte le storie: è la lista generale di ciò che rende una storia «fatta» → [[user-stories]] § Quando una storia è completa.

### Burndown chart

> 📄 Fonte: [[04_Agile_01.pdf#page=31]]

- Rappresenta il **lavoro rimanente** (in **Story Point**), che **diminuisce giorno per giorno** fino a **zero alla fine dello Sprint**.
- La **linea tratteggiata** indica il **progresso ideale teorico**; la **linea viola** mostra il **progresso reale** del team.
- **Gestione dei cambiamenti imprevisti:** la **linea blu** in alto evidenzia i **cambiamenti di ambito** (*scope*), mostrando chiaramente se durante il lavoro sono stati aggiunti task non pianificati.

![[lez06-ag-p31-burndown-chart.png]]
*Figura di [[04_Agile_01.pdf#page=31]], infografica «Il grafico burndown Agile — visualizzazione del progresso dello sprint» (in italiano). Al centro il grafico: asse x giorni dello sprint (1–15), asse y Story Point rimanenti (0–80); linea tratteggiata del progresso ideale da 70 a 0; linea viola del progresso reale, a gradini, che risale intorno al giorno 8; linea blu dell'ambito a 70, con un picco al giorno 8 («modifica dell'ambito: aggiunta di Story Point»). Riquadri laterali: **valore del burndown** (identifica ritardi, gestisce le aspettative, mostra il progresso); **dati chiave** (story point di partenza, lavoro completato ogni giorno); **risposta al cambiamento** (mostra l'aggiunta di scope, permette una ri-pianificazione informata); **trasparenza** (condivide lo stato del progetto, allinea gli stakeholder).*

![[grafico-burndown-sprint.svg]]
*🧩 Grafico mio con valori illustrativi costruiti sulla forma della figura di [[04_Agile_01.pdf#page=31]] (script `output/diagrammi/genera_grafici_lez06.py`): sprint di 15 giorni, 70 Story Point iniziali, 7 SP aggiunti al giorno 8.*

> 🧩 Elaborazione mia — come leggerlo:
> - **pendenza della linea ideale**: $70\ \text{SP} / 14\ \text{intervalli} = 5\ \text{SP al giorno}$ (dal giorno 1 al giorno 15 ci sono 14 intervalli);
> - **tratti piatti** (giorni 3→4, 5→6, 10→11): nessuna storia chiusa quel giorno — non vuol dire che nessuno abbia lavorato, ma che il lavoro non è arrivato a «fatto»;
> - **sopra la linea ideale** il team è in ritardo, **sotto** è in anticipo (giorno 7: 38 SP rimanenti contro 40 ideali → leggermente in anticipo);
> - **giorno 8**: l'ambito sale da 70 a 77 SP (linea blu) e il lavoro rimanente **risale** da 38 a 44 nonostante il team abbia lavorato: è il caso «aggiunta di task non pianificati» della slide. Senza la linea blu sembrerebbe che il team sia tornato indietro;
> - chi usa questo grafico durante il **daily meeting** vede subito se l'obiettivo dello sprint è a rischio.

## Perché importa

Sono gli strumenti del metodo Agile usato nel [[progetto-di-corso]]: sprint di 2 settimane con iteration review alla fine di ognuno ([[00_IntroduzioneAlCorso_SAD.pdf#page=26]]). L'esame valuta anche come il team ha applicato il metodo Agile ([[00_IntroduzioneAlCorso_SAD.pdf#page=28]]).

> 🎯 Esame: le quattro cerimonie con scopo, partecipanti, frequenza e durata; differenza demo/retrospettiva; i quattro artefatti; product vs iteration backlog (chi ordina cosa); come si legge un burndown chart.

## Connessioni

- [[sviluppo-agile]]: valori, principi, ruoli.
- [[user-stories]]: l'artefatto che riempie i backlog.
- [[progetto-di-corso]]: sprint e iteration review del progetto.

## Fonti

- [[agile-project-management]] — [[04_Agile_01.pdf#page=22]]–[[04_Agile_01.pdf#page=31]]

_Aggiornato: 2026-10-10 — ingest 04_Agile_01.pdf_
