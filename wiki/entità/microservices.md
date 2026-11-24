---
tipo: entità
categoria: stile
famiglia: "service-oriented"
---

# Microservices (microservizi)

> Pagina iniziata con i cenni della lezione 0 e 1; lo stile sarà trattato più avanti (programma: *Service Oriented Style (SOA), Microservices Style*, [[00_IntroduzioneAlCorso_SAD.pdf#page=16]]; testo: Richardson, *Microservices Patterns*, [[00_IntroduzioneAlCorso_SAD.pdf#page=35]]). TODO: da espandere.

## Contesto e problema

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture.pdf#page=3]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=35]]

Costruire un sistema fatto di parti che si possano **sviluppare**, **rilasciare**, **scalare** e che possano **guastarsi** in modo **indipendente**.

## Soluzione

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture.pdf#page=3]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=35]]

- Ogni microservizio ha il proprio **bounded context** e può scalare, essere rilasciato e guastarsi indipendentemente ([[01-IntroductionOnSoftwareArchitecture.pdf#page=3]]).
- Nella **struttura a servizi** le unità sono **servizi** che interoperano tramite **scambio di messaggi**; la struttura aiuta a costruire sistemi di componenti **sviluppabili indipendentemente** ([[01-IntroductionOnSoftwareArchitecture.pdf#page=35]]).

## Diagramma

![[lez01-intro-p35-service-structure.png]]
*Figura di [[01-IntroductionOnSoftwareArchitecture.pdf#page=35]] (la stessa immagine è la «Microservices Architecture» di [[00_IntroduzioneAlCorso_SAD.pdf#page=7]]): client diversi → **API Gateway** → servizi, ciascuno con i propri moduli e il **proprio database**; comunicazione per *remote invocation* e *asynchronous communication*; servizi infrastrutturali comuni (message broker, monitoring, configuration service, service discovery).*

🧩 Il database per servizio è ciò che rende possibile l'indipendenza: nessun servizio legge le tabelle di un altro, quindi ognuno può cambiare il proprio schema e scalare da solo.

## Attributi di qualità

| Attributo | Effetto | Fonte |
|---|---|---|
| Agilità | + | [[00_IntroduzioneAlCorso_SAD.pdf#page=10]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=3]] |
| Evolvibilità | + | [[00_IntroduzioneAlCorso_SAD.pdf#page=10]] |
| Scalabilità | + | [[00_IntroduzioneAlCorso_SAD.pdf#page=10]] |
| Resilienza | + | [[00_IntroduzioneAlCorso_SAD.pdf#page=10]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=3]] |

Penalizzati: TODO — non ancora trattati nelle fonti.

## Quando usarlo / quando no

TODO: da espandere.

## Varianti ed esempi

- È uno degli stili suggeriti per il [[progetto-di-corso]] ([[00_IntroduzioneAlCorso_SAD.pdf#page=25]]); la prima iterazione del progetto prevede la definizione dei *bounded context* ([[00_IntroduzioneAlCorso_SAD.pdf#page=24]]).
- È citato come pattern che comprende più tattiche ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=21]]).

- Nella figura dell'evoluzione dei tier ([[3-Architectural Patterns-complete.pdf#page=27]]) i microservizi corrispondono alla riga «N services»: deployment indipendente, servizi con logica e dati propri, collegati da API o messaggi → [[architetture-multi-tier]].

## Connessioni

- [[strutture-componenti-e-connettori]] § Struttura a servizi.
- [[pattern-architetturali]].
- [[architettura-software]] (esempio nel ruolo dell'architettura).

## Fonti

- [[introduzione-architettura-software]], [[presentazione-corso]]

_Aggiornato: 2026-09-26 — ingest lezione 0 e lezione 1_
_Aggiornato: 2026-10-01 — ingest 3-Architectural Patterns-complete.pdf_
