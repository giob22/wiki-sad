---
tipo: concetto
importanza_esame: alta
prerequisiti: []
fonti_pdf: ["00_IntroduzioneAlCorso_SAD.pdf#page=5", "00_IntroduzioneAlCorso_SAD.pdf#page=6", "01-IntroductionOnSoftwareArchitecture.pdf#page=3", "01-IntroductionOnSoftwareArchitecture.pdf#page=4", "01-IntroductionOnSoftwareArchitecture.pdf#page=7"]
termine_inglese: "software architecture"
---

# Architettura software

## Definizione

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture.pdf#page=4]]

Esistono molte definizioni di architettura software (*software architecture*). Il corso adotta quella di **Bass, Clements e Kazman** (*Software Architecture in Practice*, [[software-architecture-in-practice]]):

> 🔑 Definizione chiave: *«L'architettura software di un sistema è l'insieme delle **strutture** necessarie per **ragionare** sul sistema. Queste strutture comprendono **elementi software**, le **relazioni** tra di essi e le **proprietà** di entrambi.»*

Conseguenze dirette della definizione ([[01-IntroductionOnSoftwareArchitecture.pdf#page=4]]):
- un'architettura comprende **più strutture**, ognuna delle quali offre una **prospettiva diversa** sul sistema → [[strutture-e-viste]];
- le definizioni precedenti mettevano l'accento sugli **elementi**, sulla loro **organizzazione** o sulle **motivazioni** (*rationale*) delle decisioni di progetto. Bass, Clements e Kazman mettono invece l'accento sulle **strutture multiple** e sul loro ruolo nel **ragionare sulle proprietà** del sistema.

### La definizione del 2003 (slide di presentazione del corso)

> 📄 Fonte: [[00_IntroduzioneAlCorso_SAD.pdf#page=6]]

Nella presentazione del corso compare la definizione precedente degli stessi autori (2003): *«L'architettura software di un programma o sistema di calcolo è la struttura, o le strutture, del sistema, che comprendono elementi software, le proprietà **esternamente visibili** di tali elementi e le relazioni tra di essi»* [Bass, Clements, Kazman 2003].

> 🧩 Elaborazione mia — confronto tra le due definizioni:
>
> | Aspetto | Definizione 2003 ([[00_IntroduzioneAlCorso_SAD.pdf#page=6]]) | Definizione adottata ([[01-IntroductionOnSoftwareArchitecture.pdf#page=4]]) |
> |---|---|---|
> | Cosa è l'architettura | la struttura o le strutture del sistema | l'**insieme di strutture** necessarie per ragionare sul sistema |
> | Proprietà considerate | solo quelle **esternamente visibili** degli elementi | proprietà di elementi **e** di relazioni |
> | Criterio di scelta | implicito | esplicito: una struttura è architetturale se serve a **ragionare** su attributi importanti per qualche stakeholder ([[01-IntroductionOnSoftwareArchitecture.pdf#page=5]]) |
>
> Il passo avanti della seconda è il criterio di «utilità per il ragionamento»: non tutto ciò che è struttura è architettura.

## Spiegazione

### Punti fermi sull'architettura

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture.pdf#page=7]]

| Affermazione della slide | Spiegazione |
|---|---|
| L'architettura è un'**astrazione** del sistema: seleziona alcuni dettagli e ne sopprime altri | 🧩 Si tengono gli elementi, le relazioni e le proprietà che servono a ragionare sulle qualità; i dettagli interni degli elementi (come è scritto il codice di un modulo) restano fuori. |
| L'architettura è **progettazione** (*design*), ma **non tutta la progettazione è architettura** | 🧩 Sono architetturali le decisioni che toccano le strutture e le loro proprietà. Scegliere l'algoritmo interno di un modulo, che non cambia interfacce né qualità del sistema, è progettazione non architetturale. |
| **Ogni sistema ha un'architettura**, ma può non essere nota a nessuno, per mancanza di **documentazione architetturale** | 🧩 Le strutture esistono comunque nel codice che gira; senza documentazione nessuno può ragionarci sopra, e l'architettura «subita» non è stata progettata. |
| **Non tutte le architetture sono buone** | Da qui l'importanza della **progettazione** e della **valutazione** dell'architettura (→ [[valutazione-attributi-di-qualita]]). |
| L'architettura **include il comportamento** | Il modo in cui gli elementi interagiscono tra loro e con l'ambiente influisce sulle proprietà dell'architettura (es. prestazioni a runtime): quel comportamento va **progettato e documentato** (→ [[strutture-componenti-e-connettori]]). |

### Ruolo nel processo di sviluppo

> 📄 Fonte: [[00_IntroduzioneAlCorso_SAD.pdf#page=5]], [[00_IntroduzioneAlCorso_SAD.pdf#page=6]], [[00_IntroduzioneAlCorso_SAD.pdf#page=11]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=3]]

Due pressioni spiegano perché l'architettura conta oggi ([[00_IntroduzioneAlCorso_SAD.pdf#page=5]]):
1. la domanda di software cresce e i processi devono sostenere **cicli di rilascio sempre più brevi**;
2. servono sistemi **sempre più complessi** con **aspettative di qualità elevate**.

La tesi del corso: **non si può costruire un sistema complesso di alta qualità, e in tempi di consegna brevi, senza curarne l'architettura** ([[00_IntroduzioneAlCorso_SAD.pdf#page=6]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=3]]). L'architettura aiuta in due modi:

1. **Qualità.** Stili, pattern, modelli e tattiche architetturali permettono di ottenere attributi di qualità diversi ([[01-IntroductionOnSoftwareArchitecture.pdf#page=3]], [[00_IntroduzioneAlCorso_SAD.pdf#page=7]] → [[attributi-di-qualita]], [[tattiche-architetturali]]). Esempio della slide: nei **microservizi** ogni servizio ha il proprio *bounded context* e può scalare, essere rilasciato e guastarsi **indipendentemente**, migliorando resilienza e agilità ([[01-IntroductionOnSoftwareArchitecture.pdf#page=3]] → [[microservices]]).
2. **Organizzazione dello sviluppo.** Definire la struttura permette di organizzare meglio il processo di sviluppo ([[01-IntroductionOnSoftwareArchitecture.pdf#page=3]]). I processi moderni sono spesso **iterativi e Agile**, con rilasci rapidi e incrementali; un'architettura chiara, ben progettata e documentata sostiene questo modo di lavorare ([[00_IntroduzioneAlCorso_SAD.pdf#page=11]] → [[importanza-architettura-software]] §3.6–3.7).

![[lez00-intro-p10-stili-e-attributi-qualita.png]]
*Figura di [[00_IntroduzioneAlCorso_SAD.pdf#page=10]] (costruita progressivamente su [[00_IntroduzioneAlCorso_SAD.pdf#page=7]]–[[00_IntroduzioneAlCorso_SAD.pdf#page=10]]): tre architetture affiancate, ognuna con una nuvoletta degli attributi di qualità che favorisce. **Layered Architecture** (cerchi concentrici: hardware, kernel, shell, utilities) → modularità, modificabilità, portabilità. **Web-Application Ms reference Architecture** (architettura di riferimento Microsoft per applicazioni web, a strati verticali) → manutenibilità, scalabilità, sicurezza, prestazioni. **Microservices Architecture** (client, API Gateway, servizi con i propri moduli e database, servizi infrastrutturali comuni) → agilità, evolvibilità, scalabilità, resilienza. Messaggio: la scelta dello stile determina quali qualità si ottengono.*

## Esempi espansi

L'esempio guida di tutta la lezione 1 è l'[[exam-booking-system]]: lo stesso sistema viene guardato con la vista dei moduli, la vista runtime e la vista di deployment ([[01-IntroductionOnSoftwareArchitecture.pdf#page=12]]).

## Perché importa

È il concetto da cui parte il corso: la definizione (strutture + ragionamento) spiega perché si studiano **viste**, **attributi di qualità** e **tattiche**. All'orale la definizione va saputa e commentata.

> 🎯 Esame: enunciare la definizione di Bass, Clements e Kazman, spiegare «insieme di strutture» e «per ragionare», e i punti fermi di [[01-IntroductionOnSoftwareArchitecture.pdf#page=7]] (astrazione; design ≠ architettura; ogni sistema ne ha una; include il comportamento).

## Connessioni

- [[strutture-e-viste]]: la definizione è costruita sul concetto di struttura.
- [[attributi-di-qualita]]: sono le proprietà su cui l'architettura permette di ragionare.
- [[importanza-architettura-software]]: le 11 motivazioni della sezione 3 della lezione.
- [[buone-pratiche-architetturali]]: come si costruisce una buona architettura.

## Fonti

- [[presentazione-corso]] — [[00_IntroduzioneAlCorso_SAD.pdf#page=5]]–[[00_IntroduzioneAlCorso_SAD.pdf#page=11]]
- [[introduzione-architettura-software]] — [[01-IntroductionOnSoftwareArchitecture.pdf#page=3]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=4]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=7]]

_Aggiornato: 2026-09-26 — ingest lezione 0 e lezione 1_
