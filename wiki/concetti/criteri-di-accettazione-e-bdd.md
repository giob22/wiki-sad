---
tipo: concetto
importanza_esame: alta
prerequisiti: ["user-stories"]
fonti_pdf: ["04_Agile_01_bis.pdf#page=50", "04_Agile_01_bis.pdf#page=51", "04_Agile_01_bis.pdf#page=52", "04_Agile_01_bis.pdf#page=53", "04_Agile_01_bis.pdf#page=54", "04_Agile_01_bis.pdf#page=55", "04_Agile_01_bis.pdf#page=61"]
termine_inglese: "acceptance criteria, Behavior-Driven Development (BDD)"
---

# Criteri di accettazione e BDD

## Definizione

> 📄 Fonte: [[04_Agile_01_bis.pdf#page=50]], [[04_Agile_01_bis.pdf#page=51]], [[04_Agile_01_bis.pdf#page=55]]

> 🔑 Definizione chiave: i **criteri di accettazione** (*acceptance criteria*) sono le **condizioni specifiche che una singola storia deve soddisfare**: aspetti dettagliati di un requisito ad alto livello, dal punto di vista di uno stakeholder, **unici per ogni user story** ([[04_Agile_01_bis.pdf#page=50]], [[04_Agile_01_bis.pdf#page=51]]).

- Spingono il team a **considerare i dettagli del requisito prima che inizi lo sviluppo**.
- Si integrano naturalmente con un approccio **Behavior-Driven Development (BDD)** o **Acceptance Test-Driven Development (ATDD)**.

Da non confondere con la **Definition of Done**, che vale per tutte le storie → [[user-stories]] § Quando una storia è completa.

> 🔑 Definizione chiave: il **BDD** (*Behavior-Driven Development*) è nato come **evoluzione del TDD** (*Test-Driven Development*). Invece di concentrarsi sui test tecnici, sposta l'attenzione sul **comportamento atteso del sistema dal punto di vista dell'utente finale** ([[04_Agile_01_bis.pdf#page=55]]).

## Spiegazione

### Come funziona il BDD

> 📄 Fonte: [[04_Agile_01_bis.pdf#page=55]]

- **Chi:** i cosiddetti **«Three Amigos»** — business analyst/product owner, sviluppatori, QA/tester — definiscono gli **scenari d'uso prima di scrivere codice**.
- **Sintassi Gherkin:** gli scenari si scrivono in un **linguaggio naturale strutturato** comprensibile a tutti, tecnici e non:
  - **Given** — dato un certo contesto iniziale;
  - **When** — quando avviene un evento o un'azione;
  - **Then** — allora si ottiene un certo risultato.
- **Obiettivo:** creare una **«specifica vivente»** (*living specification*) che serve **sia da documentazione sia da test automatico**.

> 💡 Connessione: è la stessa struttura Given–When–Then degli **scenari di qualità** della Lez. 1 (Given ambiente e artefatto, When sorgente e stimolo, Then risposta misurabile, [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=9]] → [[scenari-di-qualita]]). Gli scenari BDD verificano il **comportamento funzionale**; gli scenari di qualità verificano gli **attributi di qualità**.

## Esempi espansi

### Recupero della password: dalla discussione ai criteri

> 📄 Fonte: [[04_Agile_01_bis.pdf#page=52]]

**Storia:** come cliente, voglio recuperare la mia password così da poter accedere di nuovo al sistema.

| Discussione (domande del team) | → Criterio di accettazione |
|---|---|
| Quanto resta valido il link? | 1. Il link ricevuto via email è valido **30 minuti** |
| Posso riusare un vecchio link? | 2. Ogni link si può usare **una sola volta** |
| C'è una lunghezza minima della password? | 3. La nuova password deve avere **almeno 12 caratteri** |
| Cosa succede se inserisco un'email inesistente? | 4. Se l'email non esiste, viene mostrato un **messaggio generico** |
| Riceverò una notifica? | 🧩 domanda della discussione **senza criterio** corrispondente nella slide |

![[lez06-ag-p52-criteri-recupero-password.png]]
*Figura di [[04_Agile_01_bis.pdf#page=52]]: riquadro verde con le domande della discussione, freccia verso il riquadro blu con i quattro criteri di accettazione.*

> 🧩 Elaborazione mia — il criterio 4 non è un dettaglio d'interfaccia ma di **sicurezza**: un messaggio diverso per «email inesistente» permetterebbe a un attaccante di scoprire quali email sono registrate. È un esempio di come i criteri di accettazione portano dentro la storia anche requisiti di qualità.

### Altri due esempi (in italiano)

> 📄 Fonte: [[04_Agile_01_bis.pdf#page=53]], [[04_Agile_01_bis.pdf#page=54]]

**Esempio 1** — *Come utente registrato voglio effettuare il login tramite email e password, così da accedere alla mia area personale.*

| | Criterio |
|---|---|
| AC1 | Se email e password sono corrette, l'utente accede alla propria area personale |
| AC2 | Se la password è errata, il sistema mostra un messaggio di errore **senza specificare quale credenziale** sia sbagliata |
| AC3 | Se uno dei campi è vuoto, il sistema impedisce l'invio e segnala il campo obbligatorio |
| AC4 | Dopo **5 tentativi** consecutivi falliti, l'account viene bloccato temporaneamente per **15 minuti** |
| AC5 | Se l'utente è disabilitato, il sistema non consente l'accesso |

**Esempio 2** — criteri di accettazione:

| | Criterio |
|---|---|
| AC1 | Inserendo un nome completo o parziale vengono mostrati i prodotti corrispondenti |
| AC2 | La ricerca non distingue tra maiuscole e minuscole |
| AC3 | Se non esistono prodotti corrispondenti, viene mostrato «Nessun prodotto trovato» |
| AC4 | Ogni risultato mostra nome, prezzo e disponibilità del prodotto |
| AC5 | Se il campo di ricerca è vuoto, il sistema invita a inserire un termine di ricerca |

> ⚠️ Contraddizione: a [[04_Agile_01_bis.pdf#page=54]] la user story riportata è **la stessa del login** dell'esempio 1, ma i criteri riguardano la **ricerca di prodotti**. Con ogni probabilità è un errore di copia nella slide: la storia corretta sarebbe del tipo 🧩 «Come cliente voglio cercare prodotti per nome, così da trovare velocemente quello che mi interessa» (la stessa dei Post-it di [[04_Agile_01_bis.pdf#page=37]]).

![[lez06-ag-p53-criteri-login.png]]
![[lez06-ag-p54-criteri-ricerca.png]]
*Figure di [[04_Agile_01_bis.pdf#page=53]] e [[04_Agile_01_bis.pdf#page=54]]: la user story nel riquadro verde a sinistra e la tabella dei criteri AC1–AC5 a destra, trascritte sopra.*

> 🧩 Elaborazione mia — cosa hanno in comune i buoni criteri: ognuno è **verificabile** con un caso preciso (valori concreti: 5 tentativi, 15 minuti, «Nessun prodotto trovato»), copre **anche i casi negativi** (campo vuoto, password errata, utente disabilitato) e non dice **come** implementare (niente tabelle, niente classi).

### Dai criteri agli scenari BDD

> 📄 Fonte: [[04_Agile_01_bis.pdf#page=57]]–[[04_Agile_01_bis.pdf#page=61]]

La traduzione completa dei quattro criteri del recupero password in scenari Given–When–Then, con il file Gherkin, è svolta in [[da-criteri-di-accettazione-a-bdd]].

Cosa insegna l'esercizio ([[04_Agile_01_bis.pdf#page=61]]):
- **non c'è corrispondenza uno-a-uno** tra criteri di accettazione e scenari BDD: **un criterio può richiedere più scenari**;
- il processo va da un **requisito funzionale** a **test eseguibili**;
- i criteri di accettazione fanno da **ponte tra business, sviluppo e qualità del software**.

## Perché importa

I criteri sono la «T» di INVEST: rendono la storia verificabile ([[user-stories]]). Nel progetto di corso servono a decidere quando una storia è finita e a scrivere i test (la valutazione premia documentazione e test, [[00_IntroduzioneAlCorso_SAD.pdf#page=29]]). TDD compare nel programma ([[Programma Syllabus]]) ma qui è solo citato come origine del BDD; TODO: da espandere quando verrà trattato.

> 🎯 Esame: definizione di criteri di accettazione; differenza con la DoD; cos'è il BDD, i «Three Amigos», Given–When–Then; perché un criterio può dare più scenari.

## Connessioni

- [[user-stories]]: i criteri sono il terzo aspetto della storia (i test di accettazione).
- [[da-criteri-di-accettazione-a-bdd]]: esercizio svolto.
- [[scenari-di-qualita]]: stessa struttura Given–When–Then per gli attributi di qualità.

## Fonti

- [[agile-project-management]] — [[04_Agile_01_bis.pdf#page=50]]–[[04_Agile_01_bis.pdf#page=61]]

_Aggiornato: 2026-10-10 — ingest 04_Agile_01_bis.pdf_
