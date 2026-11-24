---
tipo: entità
categoria: stile
famiglia: "service-oriented"
---

# Microservices (microservizi)

> Pagina iniziata con i cenni della lezione 0 e 1; lo stile è inquadrato nella Lezione 10 rispetto alla SOA (programma: *Service Oriented Style (SOA), Microservices Style*, [[00_IntroduzioneAlCorso_SAD.pdf#page=16]]; testo: Richardson, *Microservices Patterns*, [[00_IntroduzioneAlCorso_SAD.pdf#page=35]]). La parte dedicata ai microservizi in senso stretto non è ancora tra le fonti.

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

Penalizzati: le fonti (Lez. 10, parte 1) non li elencano ancora; la slide di p. 6 e p. 42 segnalano però il costo di più confini di servizio: interazioni frequenti e bassa latenza favoriscono il tenere insieme le responsabilità, e un intermediario condiviso (gateway, ESB) aggiunge dipendenza e complessità operativa ([[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=6]], [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=42]]).

## Quando usarlo / quando no

Quando i confini coesi e il deployment indipendente contano più della latenza e della semplicità operativa (Lez. 10, p. 6); da completare con la parte sui microservizi in senso stretto, non ancora tra le fonti.

## Varianti ed esempi

- È uno degli stili suggeriti per il [[progetto-di-corso]] ([[00_IntroduzioneAlCorso_SAD.pdf#page=25]]); la prima iterazione del progetto prevede la definizione dei *bounded context* ([[00_IntroduzioneAlCorso_SAD.pdf#page=24]]).
- È citato come pattern che comprende più tattiche ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=21]]).

- Nella figura dell'evoluzione dei tier ([[3-Architectural Patterns-complete.pdf#page=27]]) i microservizi corrispondono alla riga «N services»: deployment indipendente, servizi con logica e dati propri, collegati da API o messaggi → [[architetture-multi-tier]].

## Microservizi e SOA (Lez. 10)

> 📄 Fonte: [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=6]], [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=15]]

- I microservizi **mantengono l'idea** della SOA — capacità di business esposte con contratti espliciti, dettagli nascosti — e ne cambiano l'enfasi: **confini di business coesi, deployment indipendente, proprietà decentralizzata dei dati** (articolo di Lewis e Fowler, 2014).
- La SOA enfatizza l'esposizione e l'integrazione di capacità; i microservizi enfatizzano confini coesi e deployment indipendente. Entrambi possono usare orchestrazione, coreografia e protocolli diversi: **SOAP, REST o un ESB da soli non bastano a distinguerli**.
- **Scelta dei confini:** un sistema può combinare un progetto interno a strati o modulare con integrazione basata su servizi; il deployment indipendente favorisce la separazione, le interazioni frequenti e la bassa latenza favoriscono il tenere insieme responsabilità correlate.
- Ingredienti che li realizzano: [[contratti-e-api-di-servizio]], [[comunicazione-sincrona-e-asincrona]], [[intermediari-di-servizio]] (API gateway, discovery, message broker), [[orchestrazione-e-coreografia]]. Esempio guida: Food To Go (FTGO), da Richardson, *Microservices Patterns*.

> ⚖️ Trade-off: la slide di p. 7 chiede di dichiarare, per ogni scelta di confine, scenario di qualità, tattica, costo ed evidenze ([[servizi-e-soa]]).

## Connessioni

- [[strutture-componenti-e-connettori]] § Struttura a servizi.
- [[servizi-e-soa]]: servizio, contratto, SOA; [[event-based]] e [[publish-subscribe]]: la coreografia di eventi.
- [[pattern-architetturali]].
- [[architettura-software]] (esempio nel ruolo dell'architettura).

## Fonti

- [[introduzione-architettura-software]], [[presentazione-corso]], [[service-oriented-and-microservice-architectures]]

_Aggiornato: 2026-09-26 — ingest lezione 0 e lezione 1_
_Aggiornato: 2026-10-01 — ingest 3-Architectural Patterns-complete.pdf_
_Aggiornato: 2026-11-24 — ingest 07— Service-Oriented and Microservice Architectures-1 part.pdf (Lez. 10)_
