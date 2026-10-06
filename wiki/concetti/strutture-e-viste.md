---
tipo: concetto
importanza_esame: alta
prerequisiti: ["architettura-software"]
fonti_pdf: ["01-IntroductionOnSoftwareArchitecture.pdf#page=5", "01-IntroductionOnSoftwareArchitecture.pdf#page=6", "01-IntroductionOnSoftwareArchitecture.pdf#page=13", "01-IntroductionOnSoftwareArchitecture.pdf#page=33", "01-IntroductionOnSoftwareArchitecture.pdf#page=36", "01-IntroductionOnSoftwareArchitecture.pdf#page=47"]
termine_inglese: "architectural structures and views"
---

# Strutture e viste architetturali

## Definizione

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture.pdf#page=5]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=6]]

- Una **struttura** (*structure*) è un insieme di elementi software, delle relazioni tra essi e delle loro proprietà ([[architettura-software]]).
- Una **vista** (*view*) è la **rappresentazione** (il modello, la documentazione) di una struttura, rivolta a chi ha bisogno di ragionare su quell'aspetto del sistema ([[01-IntroductionOnSoftwareArchitecture.pdf#page=6]]).

> 🔑 Definizione chiave: *una struttura è **architetturale** se supporta il **ragionamento** sul sistema e sulle sue proprietà. Il ragionamento deve riguardare un **attributo** del sistema **importante per qualche stakeholder*** ([[01-IntroductionOnSoftwareArchitecture.pdf#page=5]]).

Esempi di attributi citati: la **funzionalità** del sistema, la capacità di **continuare a funzionare** di fronte a guasti o attacchi che cercano di abbatterlo, la **facilità/difficoltà di modificarlo**, la **reattività** alle richieste degli utenti ([[01-IntroductionOnSoftwareArchitecture.pdf#page=5]]).

**L'insieme delle strutture non è né fisso né limitato: dipende** dal sistema e da ciò su cui si vuole ragionare ([[01-IntroductionOnSoftwareArchitecture.pdf#page=5]]).

## Le tre categorie di strutture

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture.pdf#page=5]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=13]]

| Categoria | Domanda a cui risponde ([[01-IntroductionOnSoftwareArchitecture.pdf#page=13]]) | Elementi tipici nell'[[exam-booking-system]] | Pagina |
|---|---|---|---|
| **Strutture di modulo** (*module structures*) | Come è organizzato il **codice**? | Booking, Eligibility Checking, Exam Catalog, Notifications | [[strutture-di-modulo]] |
| **Strutture componenti e connettori** (*component-and-connector*, C&C) | Come si **comporta** il sistema **a runtime**? | Web Client, Application API, Database, Message Queue | [[strutture-componenti-e-connettori]] |
| **Strutture di allocazione** (*allocation structures*) | **Dove** viene eseguito il software? | istanze dell'applicazione, database server, nodi cloud, collegamenti di rete | [[strutture-di-allocazione]] |

![[lez01-intro-p13-tre-viste.png]]
*Figura di [[01-IntroductionOnSoftwareArchitecture.pdf#page=13]]: tre colonne, una per categoria, ciascuna con gli elementi dell'Exam Booking System e la domanda a cui risponde. Nota in fondo: «le viste sono collegate, ma **nessuna è una versione più dettagliata di un'altra**».*

> 🧩 Elaborazione mia: la nota «nessuna vista è il dettaglio di un'altra» è il punto concettuale. Le tre viste non sono livelli di zoom dello stesso disegno: mostrano **tipi diversi di elementi** (unità di codice, entità in esecuzione, risorse non software), quindi nessuna si ricava dall'altra.

## L'analogia con il corpo umano

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture.pdf#page=6]]

![[lez01-intro-p6-analogia-corpo-umano.png]]
*Figura di [[01-IntroductionOnSoftwareArchitecture.pdf#page=6]]: quattro sagome umane che mostrano scheletro, muscoli, sistema nervoso e sistema circolatorio.*

Il corpo umano è fatto di **strutture diverse**; ognuna è modellata da una **vista** diversa, di interesse per un **medico specialista** diverso; **tutte descrivono lo stesso corpo**. Allo stesso modo le viste architetturali descrivono lo stesso sistema, ciascuna per uno stakeholder e un tipo di ragionamento (🧩: l'ortopedico guarda lo scheletro come chi valuta la modificabilità guarda i moduli).

## Relazioni tra strutture

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture.pdf#page=33]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=36]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=50]]

Le strutture danno prospettive diverse **ma non sono indipendenti**: gli elementi di una sono legati agli elementi di altre. Un **modulo** di una struttura di decomposizione può manifestarsi come **uno, parte di uno, o più componenti** di una struttura C&C ([[01-IntroductionOnSoftwareArchitecture.pdf#page=36]]).

Le strutture C&C sono **ortogonali** a quelle di modulo ([[01-IntroductionOnSoftwareArchitecture.pdf#page=33]]):
- un'unica unità di codice (modulo) può essere compilata in **un solo servizio replicato migliaia di volte** nell'ambiente di esecuzione;
- oppure **1.000 moduli** possono essere compilati e collegati in **un unico eseguibile** (un solo componente).

Da qui la regola pratica: **non aspettarsi una corrispondenza uno-a-uno tra moduli e componenti** ([[01-IntroductionOnSoftwareArchitecture.pdf#page=50]] → [[buone-pratiche-architetturali]]).

![[lez01-intro-p36-relazione-tra-strutture.png]]
*Figura di [[01-IntroductionOnSoftwareArchitecture.pdf#page=36]]: a sinistra una **vista di decomposizione** (un «System» che contiene due moduli, Client e Server); a destra una **vista client-server** (un server S1 collegato a dieci client C1…C10 con connettori request-reply). Didascalia: la vista di destra si può usare per **analisi delle prestazioni, previsione dei colli di bottiglia e gestione del traffico di rete**, cose estremamente difficili o impossibili con la vista di sinistra.*

> 🧩 Elaborazione mia: il modulo «Client» della vista di sinistra corrisponde a **dieci** componenti a runtime nella vista di destra. Il numero di istanze e di connessioni simultanee — cioè ciò che determina il carico sul server — esiste solo nella vista C&C.

Anche nell'esempio guida: il componente runtime **Booking Service** contiene **due** moduli, Booking ed Eligibility Checking ([[01-IntroductionOnSoftwareArchitecture.pdf#page=28]]).

## Quali strutture scegliere?

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture.pdf#page=47]]

- **Sistemi piccoli**: spesso bastano meno strutture. Es.: non serve documentare la vista di **deployment** di un sistema installato su un solo nodo, né la vista di **concorrenza** se il sistema è un unico processo.
- **Sistemi grandi**: possono servire più viste.
- Criterio: le strutture devono dare **comprensione e leva** sugli **attributi di qualità più importanti** del sistema; si scelgono quelle che contano di più per ottenerli.
- I **pattern architetturali** sono composizioni di elementi architetturali che forniscono **strategie preconfezionate** per risolvere alcuni problemi del sistema (→ [[pattern-architetturali]]).

## Perché importa

Tutto il resto del corso (documentazione, valutazione, stili) presuppone di sapere **quale vista** usare per **quale domanda**: moduli → modificabilità; C&C → prestazioni, disponibilità, sicurezza, scalabilità; allocazione → prestazioni, disponibilità, costi, organizzazione del lavoro.

> 🎯 Esame: le tre categorie con la domanda di ciascuna, il criterio «una struttura è architetturale se…», e perché moduli e componenti non corrispondono uno a uno.

## Connessioni

- [[strutture-di-modulo]], [[strutture-componenti-e-connettori]], [[strutture-di-allocazione]]: le tre categorie in dettaglio.
- [[attributi-di-qualita]]: il criterio di scelta delle strutture.
- [[importanza-architettura-software]] §3.11: le viste come base per formare i nuovi membri del progetto.
- [[attribute-driven-design]]: il progettista produce proprio queste strutture.

## Fonti

- [[introduzione-architettura-software]] — [[01-IntroductionOnSoftwareArchitecture.pdf#page=5]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=6]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=13]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=33]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=36]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=47]]

_Aggiornato: 2026-09-26 — ingest lezione 1_
