---
tipo: entità
categoria: stile
famiglia: "layered"
---

# Layered (architettura a strati)

> Pagina iniziata con i cenni della lezione 1; lo stile sarà trattato per esteso più avanti (programma: *Layered Style — Virtual Machines and Client-Server*, [[00_IntroduzioneAlCorso_SAD.pdf#page=16]]). TODO: da espandere.

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

TODO: da espandere quando lo stile sarà trattato per esteso. Indicazione della Lez. 3: conviene quando contano portabilità e modificabilità più delle prestazioni, e se si rispetta l'ordine stretto tra strati.

## Varianti ed esempi

- Unix System V ([[01-IntroductionOnSoftwareArchitecture.pdf#page=21]]) — 🧩 non strettamente stratificato: gli User programs usano sia Libraries sia la System call interface.
- Varianti del programma: *Virtual Machines* e *Client-Server* ([[00_IntroduzioneAlCorso_SAD.pdf#page=16]]) → [[client-server]].

## Connessioni

- [[strutture-di-modulo]]: la *layer structure* è una struttura di modulo.
- [[pattern-architetturali]]: esempio di pattern come insieme di tattiche.
- [[tattiche-architetturali]]: *use an intermediary*.
- [[pattern-modifiability]]: layers come pattern per la modificabilità; *restrict dependencies* in [[tattiche-modifiability]].

## Fonti

- [[introduzione-architettura-software]], [[attributi-di-qualita-e-importanza-architettura]], [[presentazione-corso]], [[quality-attributes-modifiability]]

_Aggiornato: 2026-09-30 — ingest 03-Modifiability.pdf (layer pattern)_
_Aggiornato: 2026-10-01 — ingest 3-Architectural Patterns-complete.pdf_
