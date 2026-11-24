---
tipo: concetto
importanza_esame: media
prerequisiti: ["stili-architetturali"]
fonti_pdf: ["05_Architectural_Styles_Complete.pdf#page=90"]
termine_inglese: "decoupling (space, time, synchronization)"
---

# Disaccoppiamento dei componenti

## Definizione

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=90]]

Un **intermediario** permette ai componenti di comunicare senza indirizzarsi direttamente. Le slide distinguono tre forme di disaccoppiamento.

## Spiegazione

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=90]], [[05_Architectural_Styles_Complete.pdf#page=91]]

| Forma | Che cosa non serve | Condizione |
|---|---|---|
| **Space / reference decoupling** | i componenti non devono conoscere l'identità l'uno dell'altro | un intermediario fa da tramite |
| **Time decoupling** | i componenti non devono essere disponibili nello stesso momento | i messaggi restano disponibili per la consegna successiva |
| **Synchronization decoupling** | i componenti non devono attendersi durante l'interazione | consegna asincrona |

**Benefici (p. 91):** adattabilità e scalabilità architetturale; lo space decoupling consente a componenti di muoversi, cambiare, essere aggiunti o migrare; il time decoupling tollera componenti che entrano ed escono; il synchronization decoupling riduce il blocco. **Costo:** l'intermediario aggiunge overhead di elaborazione e comunicazione; i componenti dipendono ancora da formati di messaggio condivisi e dal loro significato.

## Esempi espansi

![[lez08-stili-p101-pubsub-disaccoppiamento.png]]
*Le tre forme con un middleware publish/subscribe ([[05_Architectural_Styles_Complete.pdf#page=101]]): space decoupling — P pubblica una volta e il middleware chiama `notify()` verso più S senza che P ne conosca l'identità; time decoupling — P pubblica mentre S è disconnesso (il fulmine indica l'indisponibilità) e la notifica arriva dopo, quando S è di nuovo disponibile; synchronization decoupling — P non attende; S è notificato in modo asincrono.*

## Perché importa

È il vantaggio principale di [[publish-subscribe]], [[event-based]] e dei message broker dei [[microservices]]; il suo prezzo è la minore leggibilità del flusso di controllo ([[implicit-invocation]]).

## Connessioni

- [[publish-subscribe]], [[event-based]], [[implicit-invocation]].
- [[modifiability]]: l'accoppiamento debole è una tattica per la modificabilità ([[tattiche-modifiability]]).

## Fonti

- [[architectural-styles]]; [[05_Architectural_Styles_Complete.pdf#page=90]]–[[05_Architectural_Styles_Complete.pdf#page=91]]

_Aggiornato: 2026-11-24 — ingest 05_Architectural_Styles_Complete.pdf_
