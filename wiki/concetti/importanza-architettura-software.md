---
tipo: concetto
importanza_esame: alta
prerequisiti: ["architettura-software", "attributi-di-qualita"]
fonti_pdf: ["01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=31", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=32", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=34", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=35", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=36", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=37", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=38", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=39", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=40", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=41", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=43", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=44", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=45"]
termine_inglese: "why is software architecture important"
---

# Perché l'architettura software è importante

## Definizione

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=31]] (slide 82)

La terza sezione della lezione 1 elenca le motivazioni per cui l'architettura conta. **Ce ne sono decine**; la lezione ne esamina undici (§3.1–3.11, numerazione delle slide).

| § | Motivazione | Idea in una riga |
|---|---|---|
| 3.1 | Abilita o inibisce gli attributi di qualità | le qualità dipendono dalle scelte architetturali |
| 3.2 | Permette di prevedere le qualità | si valutano le qualità sul modello, prima del sistema |
| 3.3 | Comunicazione tra stakeholder | astrazione comune per capirsi e negoziare |
| 3.4 | Decisioni di progetto precoci | le prime decisioni sono le più difficili da cambiare |
| 3.5 | Vincoli sull'implementazione | l'implementazione deve rispettare l'architettura |
| 3.6 | Influenza la struttura organizzativa | la decomposizione diventa la divisione del lavoro |
| 3.7 | Abilita lo sviluppo incrementale | scheletro eseguibile, poi funzionalità |
| 3.8 | Modello trasferibile e riusabile | linee di prodotto |
| 3.9 | Incorporare elementi sviluppati indipendentemente | composizione, sistemi aperti |
| 3.10 | Restringe il vocabolario delle alternative | usare soluzioni collaudate |
| 3.11 | Base per la formazione | le viste introducono i nuovi membri al sistema |

## Spiegazione

### 3.1 — Abilita o inibisce gli attributi di qualità

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=32]] (slide 83), [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=33]] (slide 84)

Tabella completa (prestazioni, modificabilità, sicurezza, scalabilità, riusabilità) in [[attributi-di-qualita]] § L'architettura abilita o inibisce le qualità. Conclusione della slide: il progetto architetturale è importante, ma anche le decisioni di **progetto di dettaglio e implementazione** influenzano la qualità finale.

### 3.2 — Permette di prevedere gli attributi di qualità

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=34]] (slide 85)

Si possono fare previsioni di qualità **basandosi solo sulla valutazione dell'architettura**: se certe decisioni portano a certe qualità, verificando che quelle decisioni siano state prese si può prevedere con fiducia che le qualità ci saranno → [[valutazione-attributi-di-qualita]].

### 3.3 — Comunicazione tra stakeholder

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=35]] (slide 86)

L'architettura è un'**astrazione comune** del sistema che gli stakeholder usano come base per: **creare comprensione reciproca**, **negoziare**, **formare consenso**, **comunicare** tra loro.

### 3.4 — Decisioni di progetto precoci

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=36]] (slide 88)

Un'architettura si può vedere come un **insieme di decisioni precoci**. Cambiarle provoca un **effetto a catena** (*ripple effect*): anche le decisioni prese dopo, che dipendono da quelle, vanno cambiate. Esempi di decisioni precoci:
- il sistema girerà su **un processore** o sarà **distribuito** su più processori?
- il software sarà **a strati**? Se sì, quanti strati e cosa farà ciascuno?
- i componenti comunicheranno in modo **sincrono o asincrono**? Interagiranno trasferendo **controllo**, **dati** o entrambi?
- le informazioni che fluiscono nel sistema saranno **cifrate**?
- quale **sistema operativo** useremo?
- quale **protocollo di comunicazione** sceglieremo?

🧩 Tutte e sei le domande hanno già avuto risposta nell'[[exam-booking-system]]: distribuito (p. 40), comunicazione asincrona per le notifiche (p. 28), TLS (tattiche di sicurezza), protocolli HTTPS/REST, JDBC, AMQP (p. 40).

### 3.5 — Vincoli sull'implementazione

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=37]] (slide 89)

L'implementazione deve **conformarsi** alle decisioni prescritte dall'architettura:
- deve avere **gli elementi** prescritti;
- gli elementi devono **interagire** nel modo prescritto;
- ogni elemento deve **soddisfare la propria responsabilità** verso gli altri come prescritto.

Ognuna di queste prescrizioni è un **vincolo per chi implementa**.

### 3.6 — Influenza la struttura organizzativa

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=38]] (slide 90)

La **decomposizione** del sistema ([[strutture-di-modulo]]) è di solito la base della **work-breakdown structure**, che determina:
- le unità di **pianificazione, schedulazione e budget**;
- i **canali di comunicazione tra team**;
- il **controllo di configurazione** e l'organizzazione del **file system**;
- i piani e le procedure di **integrazione e test**;
- come è organizzata l'intranet del progetto e dove sono collocati i team.

I team **comunicano tra loro in termini di specifiche delle interfacce** dei propri elementi.

🧩 È ciò che accade nel [[progetto-di-corso]]: il sistema è diviso in sottosistemi autonomi assegnati ai team, che si coordinano su architettura comune e contratti d'integrazione ([[00_IntroduzioneAlCorso_SAD.pdf#page=23]], [[00_IntroduzioneAlCorso_SAD.pdf#page=29]]).

### 3.7 — Abilita lo sviluppo incrementale

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=39]] (slide 91)

- Il **primo incremento** può essere un **sistema scheletro** (*skeletal system*): c'è almeno parte dell'**infrastruttura**, ma manca gran parte della funzionalità applicativa. L'infrastruttura riguarda: come gli elementi si **inizializzano**, **comunicano**, **condividono dati**, **accedono alle risorse**, **segnalano errori**, **registrano l'attività**, ecc.
- Negli incrementi successivi si progetta e costruisce **un po' di infrastruttura** a supporto di **un po' di funzionalità end-to-end**, e si ripete fino alla fine.
- Così il sistema è **eseguibile presto** nel ciclo di vita e i **problemi di prestazioni** (e altri) si scoprono presto.

→ anche [[buone-pratiche-architetturali]] (architettura adatta all'implementazione incrementale).

### 3.8 — Modello trasferibile e riusabile

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=40]] (slide 92)

- Riusare un'architettura offre opportunità per sistemi con **requisiti simili**.
- Quando le decisioni architetturali si riusano su più sistemi, si trasferiscono anche **tutte le conseguenze** delle decisioni precoci.
- Una **linea di prodotto** (*product line* o *family*) è un insieme di sistemi costruiti con lo **stesso insieme di asset condivisi**: componenti software, documenti dei requisiti, casi di test, ecc.
- L'architettura definisce **cosa è fisso** per tutti i membri della linea di prodotto e **cosa è variabile**.

### 3.9 — Incorporare elementi sviluppati indipendentemente

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=41]] (slide 93), [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=42]] (slide 94), [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=43]] (slide 95)

Lo sviluppo basato sull'architettura spesso consiste nel **comporre o assemblare elementi** sviluppati separatamente, anche indipendentemente. L'architettura definisce:
- i **componenti** che possono essere incorporati;
- come **interagiscono** con l'ambiente;
- come **ricevono e cedono il controllo**;
- quali **dati consumano e producono**;
- come **accedono ai dati** e quali **protocolli** usano per comunicare e condividere risorse.

**Vantaggi**: minor *time to market*, maggiore affidabilità, costo più basso, flessibilità.

Esempio della docente: l'architettura del progetto **ENACTEST** ([[enactest]]).

**Sistemi aperti** ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=43]]): un **sistema aperto** definisce un insieme di **standard per gli elementi software** — come si comportano, come interagiscono con altri elementi, come condividono dati, ecc. Lo scopo è permettere a **molti fornitori diversi** di produrre elementi. I sistemi aperti sono resi possibili da un'architettura che definisce elementi e interazioni. Esempio: l'architettura a standard aperto **AUTOSAR** ([[autosar]]).

### 3.10 — Restringe il vocabolario delle alternative di progetto

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=44]] (slide 96)

Nel progettare è importante **restringere il vocabolario** a **soluzioni collaudate**: **pattern**, **tattiche** o **elementi off-the-shelf**. Benefici:
- maggiore **riuso**;
- progetti più **regolari e semplici**, più facili da **capire e comunicare**, con risultati **più prevedibili**;
- **analisi più facile** e con maggiore fiducia;
- **tempi di selezione** più brevi;
- maggiore **interoperabilità**.

→ [[pattern-architetturali]], [[tattiche-architetturali]]

### 3.11 — Base per la formazione

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=45]] (slide 97)

L'architettura è la **prima introduzione al sistema** per i nuovi membri del progetto:
- **viste di modulo** per mostrare la struttura del progetto;
- **viste C&C** per spiegare come il sistema dovrebbe funzionare e svolgere il suo compito;
- **viste di allocazione** per mostrare dove si colloca la parte assegnata al nuovo membro nell'ambiente di sviluppo o di deployment.

→ [[strutture-e-viste]]

## Perché importa

È la classica domanda d'apertura dell'orale («perché serve l'architettura?»). La risposta forte lega le motivazioni ai concetti: qualità (3.1–3.2), persone e organizzazione (3.3, 3.6, 3.11), processo (3.4, 3.5, 3.7), riuso (3.8–3.10).

> 🎯 Esame: saper elencare e argomentare almeno le motivazioni principali con un esempio ciascuna (l'Exam Booking System fornisce esempi per 3.1, 3.4, 3.6, 3.7).

## Connessioni

- [[architettura-software]]: definizione e ruolo nel processo.
- [[attributi-di-qualita]], [[valutazione-attributi-di-qualita]]: §3.1 e §3.2.
- [[strutture-e-viste]]: §3.11.
- [[buone-pratiche-architetturali]]: raccomandazioni di processo.
- [[autosar]], [[enactest]]: esempi del §3.9.

## Fonti

- [[attributi-di-qualita-e-importanza-architettura]] — [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=31]]–[[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=45]]

_Aggiornato: 2026-09-26 — ingest lezione 1_
