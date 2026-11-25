---
tipo: entità
categoria: stile
famiglia: "layered"
---

# Layered (architettura a strati)

> Pagina iniziata con i cenni della lezione 1 e completata nella Lezione 8 (sezione «Trattazione completa dello stile»; programma: *Layered Style — Virtual Machines and Client-Server*, [[00_IntroduzioneAlCorso_SAD.pdf#page=16]]).

## Contesto e problema

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture.pdf#page=21]]

🧩 Si vuole poter cambiare la piattaforma sottostante (hardware, sistema operativo, tecnologie) senza riscrivere ciò che ci sta sopra: la slide lega la struttura a strati alla **portabilità**, «la capacità di cambiare la macchina virtuale sottostante».

## Soluzione

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture.pdf#page=21]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=22]]

- **Elementi**: strati (*layers*). Uno strato è una **«macchina virtuale» astratta** che fornisce un **insieme coeso di servizi** tramite un'**interfaccia gestita**.
- **Relazione**: *allowed to use* (può usare).
- **Vincolo**: nei sistemi **strettamente stratificati** uno strato può usare **un solo altro strato** (🧩 quello immediatamente sotto).

Tattiche incorporate ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=22]] → [[pattern-architetturali]]): separare le responsabilità; restringere le dipendenze; usare un intermediario (uno strato isola quello sopra dalle tecnologie sottostanti); astrarre i servizi comuni (interfacce definite).

### Come pattern per la modificabilità (Lez. 3)

> 📄 Fonte: [[03-Modifiability.pdf#page=31]], [[03-Modifiability.pdf#page=22]]

- Il pattern divide il sistema in strati che possono essere **sviluppati ed evoluti separatamente** con poca interazione tra le parti: sostiene **portabilità, modificabilità e riuso**.
- Ogni strato è esposto tramite un'**interfaccia pubblica**.
- Gli strati interagiscono secondo una **relazione d'ordine stretta** (o a volte tramite un **layer bridge**).
- La tattica *restrict dependencies* si vede proprio nelle architetture a strati: uno strato può usare solo gli strati inferiori, a volte solo quello immediatamente sotto ([[03-Modifiability.pdf#page=22]] → [[tattiche-modifiability]]).

🧩 Il *layer bridging* è il caso in cui uno strato salta quello sotto e usa direttamente uno strato più in basso (come gli User programs di Unix che chiamano la System call interface senza passare dalle Libraries).

### Layer non è tier (Lez. 4)

> 📄 Fonte: [[3-Architectural Patterns-complete.pdf#page=24]], [[3-Architectural Patterns-complete.pdf#page=34]]

I **layer** sono una **decomposizione logica** delle responsabilità del software; i **tier** sono la **distribuzione fisica o runtime** degli elementi software. Un sistema con 3 layer può stare su 1 tier (il mainframe) o su 3 tier → [[architetture-multi-tier]]. La tabella del three-tier ([[3-Architectural Patterns-complete.pdf#page=34]]) aggiunge altri benefici e limiti degli strati: testabilità con mock o stub, controlli di sicurezza ai confini, ma aggirare gli strati può eludere i controlli.

## Diagramma

![[lez03-mo-p31-layer-pattern.png]]
*Figura di [[03-Modifiability.pdf#page=31]]: cinque strati impilati — Presentation, Application, Business, Persistence, Database — con una freccia verso il basso: «le chiamate tra strati vanno verso il basso».*

![[lez01-intro-p21-layer-structure-unix.png]]
*Figura di [[01-IntroductionOnSoftwareArchitecture.pdf#page=21]]: struttura a strati di Unix System V (dettagli in [[strutture-di-modulo]] § Layer).*

Nella presentazione del corso compare anche una rappresentazione a **cerchi concentrici** (hardware al centro, poi kernel, shell, utilities) ([[00_IntroduzioneAlCorso_SAD.pdf#page=7]]).

## Attributi di qualità

| Attributo | Effetto | Perché | Fonte |
|---|---|---|---|
| Modularità | + | responsabilità separate per strato | [[00_IntroduzioneAlCorso_SAD.pdf#page=8]] |
| Modificabilità | + | dipendenze ristrette: una modifica resta nello strato | [[00_IntroduzioneAlCorso_SAD.pdf#page=8]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=22]] |
| Portabilità | + | si cambia la macchina virtuale sottostante | [[01-IntroductionOnSoftwareArchitecture.pdf#page=21]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=22]] |
| Testabilità | + | 🧩 uno strato si testa sostituendo quello sotto | [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=22]] |
| Riuso | + | strati sviluppati ed evoluti separatamente | [[03-Modifiability.pdf#page=31]] |
| Modificabilità degli strati inferiori | + | il software negli strati inferiori si può cambiare **senza toccare quelli superiori**, purché l'interfaccia non cambi | [[03-Modifiability.pdf#page=31]] |
| Prestazioni (latenza) | − | ogni richiesta attraversa più strati: la stratificazione aggiunge spesso una **penalità di prestazioni** | [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=22]], [[03-Modifiability.pdf#page=31]] |
| Semplicità | − | complessità aggiuntiva | [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=22]] |

> ⚖️ Trade-off: se ci sono **molti casi di layer bridging**, il sistema può non raggiungere gli obiettivi di portabilità e modificabilità che la stratificazione stretta aiuta a ottenere ([[03-Modifiability.pdf#page=31]]).

## Quando usarlo / quando no

Conviene quando contano portabilità e modificabilità più delle prestazioni e si rispetta l'ordine stretto tra strati (Lez. 3); con requisiti di efficienza si può ricorrere a layer aperti, accettando le dipendenze aggiuntive ([[05_Architectural_Styles_Complete.pdf#page=20]], [[05_Architectural_Styles_Complete.pdf#page=24]]).

## Varianti ed esempi

- Unix System V ([[01-IntroductionOnSoftwareArchitecture.pdf#page=21]]) — 🧩 non strettamente stratificato: gli User programs usano sia Libraries sia la System call interface.
- Varianti del programma: *Virtual Machines* e *Client-Server* ([[00_IntroduzioneAlCorso_SAD.pdf#page=16]]) → [[client-server]].

## Trattazione completa dello stile (Lez. 8)

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=17]]–[[05_Architectural_Styles_Complete.pdf#page=29]]

- **Soluzione.** Organizzazione gerarchica, simile a un client–server a più livelli: ogni layer espone un'**API** ai layer superiori, è **server** per i superiori e **client** degli inferiori. Connettori: chiamate di procedura o protocolli di interazione (esempio tipico: i sistemi operativi). Nella variante **virtual machine** i layer sono *opachi* e interagiscono solo con quelli adiacenti ([[05_Architectural_Styles_Complete.pdf#page=17]]).
- **Benefici:** livelli crescenti di astrazione; dipendenze controllate (ogni layer dipende solo da quelli sotto) che facilitano l'evoluzione e limitano la propagazione delle modifiche: un cambiamento in un layer può ripercuotersi solo su quelli superiori; layer riusabili o sostituibili con implementazioni che preservano l'interfaccia; interfacce standardizzate per librerie e framework ([[05_Architectural_Styles_Complete.pdf#page=19]]).
- **Limiti:** attraversare molti layer aggiunge overhead; l'efficienza può motivare il *bypass* di un layer, che introduce dipendenze da considerare nella valutazione della modificabilità ([[05_Architectural_Styles_Complete.pdf#page=20]]).

![[lez08-stili-p18-layered-virtual-machines.png]]
*Tre layer ([[05_Architectural_Styles_Complete.pdf#page=18]]): Program A nel Layer 1 chiama il Layer 2 (Program B e C), che chiamano il Layer 3 (Program D). Le frecce vanno solo verso il layer adiacente inferiore.*

### Layer chiusi e layer aperti

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=21]]–[[05_Architectural_Styles_Complete.pdf#page=25]]

| | **Closed Layers (CLA)** | **Open Layers (OLA)** |
|---|---|---|
| Regola | il layer *i* usa solo il layer *i−1* | il layer *i* può usare qualsiasi layer inferiore |
| Obiettivi | **manutenibilità e portabilità**; ogni layer è una virtual machine VM<sub>i</sub> | **riduzione del tempo di esecuzione, efficienza** |
| Esempio | stack ISO/OSI | OSF/Motif |

![[lez08-stili-p22-closed-layers.png]]
*Closed layers ([[05_Architectural_Styles_Complete.pdf#page=22]]): quattro layer VM1–VM4 con classi (attributi e operazioni); le dipendenze vanno solo al layer immediatamente inferiore, per questo ogni layer è una virtual machine che nasconde quelle sotto.*

![[lez08-stili-p23-osi-closed-layers.png]]
*ISO/OSI ([[05_Architectural_Styles_Complete.pdf#page=23]]): sette layer di rete — Application, Presentation, Session, Transport, Network, DataLink, Physical — con livello di astrazione crescente verso l'alto; ogni layer parla solo con quello adiacente. L'Internet Protocol (IP) definisce, a livello rete, una VM in grado di identificare gli host e trasmettere singoli pacchetti da host a host.*

![[lez08-stili-p24-open-layers.png]]
*Open layers ([[05_Architectural_Styles_Complete.pdf#page=24]]): gli stessi quattro layer, ma alcune dipendenze saltano i layer intermedi (una classe del layer 1 usa direttamente una del layer 4): più efficiente, meno isolamento.*

![[lez08-stili-p25-motif-open-layers.png]]
*OSF/Motif ([[05_Architectural_Styles_Complete.pdf#page=25]]): *Xlib* (disegno di basso livello), *Xt* (gestione dei widget di base), *Motif* (molti widget sofisticati), *Application* (può accedere a ogni layer in modo indipendente — le frecce tratteggiate saltano i layer intermedi).*

🧩 Il compromesso è quello tra [[modifiability]]/portabilità (CLA: poche dipendenze) ed efficienza (OLA: meno attraversamenti).

### Layer e pattern Façade

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=26]], [[05_Architectural_Styles_Complete.pdf#page=27]]

![[lez08-stili-p26-facade-senza.png]]
*Senza façade ([[05_Architectural_Styles_Complete.pdf#page=26]]): un client (AccountManager) coordina Account, Address e CreditCard, chiamando `isValid()` e `save()` su ciascuno.*

![[lez08-stili-p27-facade-con.png]]
*Con una CustomerFacade ([[05_Architectural_Styles_Complete.pdf#page=27]]): il client chiama solo `saveCustomerData()` sulla façade, che coordina gli oggetti del sottosistema. La façade è quindi l'**interfaccia del layer**: nasconde i dettagli e riduce le dipendenze verso gli strati sotto.*

### Esercizio: Lunar Lander a layer

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=28]], [[05_Architectural_Styles_Complete.pdf#page=29]]

![[lez08-stili-p29-layered-lunar-lander.png]]
*Soluzione ([[05_Architectural_Styles_Complete.pdf#page=29]]): Keyboard Input Handler → (input da tastiera) Game Logic and Environment Simulator → (variazione di altitudine) Generic 2D Game Engine → (posizione x, y degli oggetti) Operating System → (dati binari) Hardware Display / Graphics Card. Ogni layer chiama solo quello sotto: è un CLA.*

Confronto con gli altri stili: [[lunar-lander-in-ogni-stile]].

## Connessioni

- [[strutture-di-modulo]]: la *layer structure* è una struttura di modulo.
- [[pattern-architetturali]]: esempio di pattern come insieme di tattiche.
- [[tattiche-architetturali]]: *use an intermediary*.
- [[pattern-modifiability]]: layers come pattern per la modificabilità; *restrict dependencies* in [[tattiche-modifiability]].

## Fonti

- [[introduzione-architettura-software]], [[attributi-di-qualita-e-importanza-architettura]], [[presentazione-corso]], [[quality-attributes-modifiability]]

_Aggiornato: 2026-09-30 — ingest 03-Modifiability.pdf (layer pattern)_
_Aggiornato: 2026-10-01 — ingest 3-Architectural Patterns-complete.pdf_
_Aggiornato: 2026-11-24 — ingest 05_Architectural_Styles_Complete.pdf (Lez. 8)_
