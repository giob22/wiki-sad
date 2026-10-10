---
tipo: esercizio
argomento: "valutare e scomporre user story con i criteri INVEST"
difficoltà: bassa
---

# Valutare e scomporre user story (INVEST)

## Metodo

> 📄 Fonte: [[04_Agile_01.pdf#page=43]], [[04_Agile_01.pdf#page=44]], [[04_Agile_01.pdf#page=46]], [[04_Agile_01.pdf#page=47]]

1. Controlla il **formato**: *Come \<tipo di utente>, voglio \<azione>, così da \<beneficio>*.
2. Applica la **checklist INVEST** della slide 47, rispondendo Sì / In parte / No a ogni domanda e motivando i «no»:

| Criterio | Domanda di verifica |
|---|---|
| I – Independent | la storia si può sviluppare e completare senza forti dipendenze da altre storie? |
| N – Negotiable | lascia spazio a discussione e negoziazione sulla soluzione? |
| V – Valuable | porta un valore riconoscibile a un utente o stakeholder? |
| E – Estimable | il team ha abbastanza informazioni per stimare lo sforzo? |
| S – Small | è abbastanza piccola da completarsi in un solo Sprint? |
| T – Testable | si possono definire criteri di accettazione chiari e verificabili? |

3. Se la storia è un'**epic**, **scomponila** in storie che descrivono **un comportamento ciascuna**, ognuna con il suo beneficio.
4. Ricontrolla le storie nuove con INVEST: la scomposizione **non garantisce** da sola che siano buone ([[04_Agile_01.pdf#page=48]]).

![[lez06-ag-p47-esercizio-invest.png]]
*Figura di [[04_Agile_01.pdf#page=47]]: a sinistra la storia da valutare, a destra la «INVEST – User Story Assessment Checklist» con le istruzioni (valutare con Sì / In parte / No e spiegare ogni criterio non pienamente soddisfatto) e la domanda di riflessione «come migliorare o dividere la storia per soddisfare meglio INVEST?».*

## Concetti usati

[[user-stories]] (INVEST, epic, dimensione) · [[criteri-di-accettazione-e-bdd]] (la T di INVEST)

## Casi svolti

### Caso 1 — La vendita del cassiere

**Traccia:** [[04_Agile_01.pdf#page=41]], [[04_Agile_01.pdf#page=42]]. Svolgimento della slide: «Un cassiere può gestire una vendita per un cliente» è **troppo grande**, cioè un'**epic**, e si scompone in: inserire gli articoli; vedere il totale; pagare in contanti; ottenere lo scontrino. Ogni storia si divide poi in task (API, form, test). Dettagli in [[user-stories]] § Dimensione.

### Caso 2 — Pagare con PayPal

**Traccia:** [[04_Agile_01.pdf#page=45]] — *«Permettere ai clienti di pagare con PayPal»*. Giudizio della slide: **troppo complessa, è un'EPIC**. Meglio queste storie:
1. Come cliente, voglio vedere PayPal tra i metodi di pagamento disponibili.
2. Come cliente, voglio essere reindirizzato a PayPal per autorizzare il pagamento.
3. Come cliente, voglio tornare automaticamente al sito di e-commerce dopo il pagamento.
4. Come cliente, voglio ricevere una conferma quando il pagamento è completato.
5. Come amministratore, voglio registrare l'esito del pagamento PayPal per aggiornare lo stato dell'ordine.

![[lez06-ag-p45-esempio-paypal-epic.png]]
*Figura di [[04_Agile_01.pdf#page=45]]: la storia di partenza nel riquadro verde con la stella rossa «Troppo complessa!! È una EPIC»; sotto, «Better the following stories…», i cinque riquadri colorati con le storie scomposte.*

**Svolgimento (🧩) — valutazione INVEST:**

| Criterio | Storia originale | Storie scomposte |
|---|---|---|
| I | — | in parte: la 2 dipende dalla 1, la 3 e la 4 dalla 2; sono **passi di un flusso**, quindi vanno pianificate in ordine |
| N | sì | sì |
| V | sì, ma vago | sì: ognuna ha un beneficio per il cliente o per l'amministratore |
| E | **no**: «pagare con PayPal» contiene integrazione, redirect, callback, notifiche, stato dell'ordine | sì: ognuna tocca una parte precisa |
| S | **no**: difficilmente sta in uno sprint | sì |
| T | **no**: quando è «finita»? | sì: es. per la 3 «dopo l'autorizzazione il browser torna alla pagina di conferma dell'ordine» |

**Osservazione:** la storia originale non segue nemmeno il template (manca *come \<utente>* e *così da \<beneficio>*); le storie scomposte sì, tranne il beneficio esplicito che manca in 1–4.

### Caso 3 — Gestire gli utenti della piattaforma (esercizio della slide)

**Traccia:** [[04_Agile_01.pdf#page=47]] — *«Come amministratore, voglio gestire gli utenti della piattaforma per controllarne l'accesso e mantenere aggiornati i loro dati.»*

**Svolgimento (🧩) — la checklist compilata:**

| Criterio | Esito | Motivazione |
|---|---|---|
| I – Independent | In parte | «gestire» include creazione, disattivazione e modifica: dentro la storia ci sono più comportamenti legati tra loro |
| N – Negotiable | Sì | non impone una soluzione |
| V – Valuable | Sì | controllo degli accessi e dati aggiornati |
| E – Estimable | **No** | «gestire» è vago: quali operazioni? Ruoli? Ricerca? Non si sa quanto lavoro c'è |
| S – Small | **No** | difficilmente entra in un solo sprint |
| T – Testable | In parte | si può testare solo dopo aver deciso cosa significa «gestire» |

**Soluzione della slide** ([[04_Agile_01.pdf#page=48]]) — dividere in:
- come amministratore, voglio **creare** un nuovo account utente per consentire l'accesso alla piattaforma;
- come amministratore, voglio **disattivare** un account utente per impedire l'accesso a chi non è più autorizzato;
- come amministratore, voglio **modificare** i dati utente per mantenere aggiornate le informazioni.

Le nuove storie sono **più mirate**, ma vanno comunque **discusse e verificate** con INVEST.

> 🧩 Nota: la storia originale ha **due benefici** diversi («controllare l'accesso» e «dati aggiornati»): è un indizio tipico di epic. Nella scomposizione, creare e disattivare servono il primo beneficio, modificare il secondo.

### Caso 4 — Revisione: due storie da Post-it

**Traccia:** [[04_Agile_01.pdf#page=37]], [[04_Agile_01.pdf#page=46]] (attività di *user stories review*).

| Storia | Problema (🧩) | Riscrittura (🧩) |
|---|---|---|
| «Come amministratore voglio gestire gli utenti (creare, modificare, eliminare) così da mantenere aggiornato il sistema» | epic: tre operazioni in una | come nel caso 3 |
| «Come cliente voglio pagare con PayPal così da completare il pagamento in modo sicuro e veloce» | epic, e «sicuro e veloce» non è verificabile così | come nel caso 2; «sicuro e veloce» va trasformato in criteri di accettazione o in uno scenario di qualità ([[scenari-di-qualita]]) |

## Trappole

- Confondere **storia troppo piccola** con buona storia: «lo scontrino mostra l'indirizzo del negozio» è un dettaglio, non una storia ([[04_Agile_01.pdf#page=41]]).
- Scomporre per **strati tecnici** («fare il database», «fare la UI»): le parti perdono valore per l'utente (V). Si scompone per **comportamenti**, poi ogni storia in task tecnici.
- Credere che la scomposizione basti: le storie nuove vanno ricontrollate.
- Dimenticare il **beneficio** («così da…»): senza, il PO non sa prioritizzare.

_Aggiornato: 2026-10-10 — ingest 04_Agile_01.pdf_
