---
tipo: concetto
importanza_esame: alta
prerequisiti: ["servizi-e-soa", "contratti-e-api-di-servizio"]
fonti_pdf: ["07— Service-Oriented and Microservice Architectures-1 part.pdf#page=35"]
termine_inglese: "intermediaries: broker, service discovery, API gateway, ESB"
---

# Intermediari di servizio: broker, discovery, API gateway, ESB

## Definizione

> 📄 Fonte: [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=35]]

Un **intermediario** si interpone tra client e servizi con alcune responsabilità, che possono stare in componenti diversi: **routing** (dove vanno richieste e messaggi), **trasformazione** (adattare rappresentazione o formato), **gateway** (applicare politiche di accesso e traffico), **discovery** (risolvere gli endpoint disponibili).

## Spiegazione

> 📄 Fonte: [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=36]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=42]]

| Schema | Come funziona | Pro / contro (dalla slide) | Pagina |
|---|---|---|---|
| **Broker forwarding** | il client invia la richiesta al broker, che la inoltra e rilancia la risposta | centralizza routing e controlli di policy; **un hop in più** e dipendenza dal broker | 36 |
| **Broker handle** | il broker restituisce un **handle** (endpoint); poi il client parla direttamente col provider | meno intermediazione nelle chiamate successive; il client deve gestire cambi di endpoint, informazioni obsolete, guasti del provider | 37 |
| **Service discovery** | un **registry** registra servizi ed endpoint; la discovery cerca un'istanza; la selezione può considerare disponibilità e routing | registrazione, informazioni di salute e aggiornamento richiedono supporto operativo | 38 |

![[lez10-soa-p36-broker-forwarding.png]]
![[lez10-soa-p37-broker-handle.png]]
![[lez10-soa-p38-service-discovery.png]]
*I tre schemi ([[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=36]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=38]]): forwarding (serviceRequest → forwardedRequest → serviceReply → forwardedReply, tutto passa dal broker); handle (il broker risponde con un serviceHandle e il requester chiama direttamente il servizio); discovery (queryServices → serviceList → select aService → service handle → serviceRequestWithHandle → serviceReply).*

**API gateway (p. 39):** punto d'ingresso per le API di servizi selezionati; **autenticazione, rate limit, logging, routing**; può **aggregare risposte**; i servizi mantengono regole di business e dati.

**Enterprise Service Bus (p. 40):** **mediazione** tra sistemi aziendali eterogenei (routing, trasformazione, *bridging* di protocolli); supporta l'integrazione con applicazioni e servizi esistenti; la SOA può usare anche altre strutture.

| | API Gateway | ESB |
|---|---|---|
| Scopo | accesso controllato alle API verso i client | integrazione tra applicazioni e servizi eterogenei |
| Funzioni | autenticazione, rate limiting, routing, aggregazione | trasformazione di messaggi, bridging di protocolli, collegamento a sistemi legacy |
| Esempio FTGO (p. 41) | instrada una richiesta d'ordine a Orders | adatta messaggi contabili per un sistema legacy con un altro formato/protocollo |

Si **sovrappongono** (instradare, proteggere, trasformare) e **possono coesistere** (p. 41).

**I costi della mediazione (p. 42):** un intermediario condiviso crea una dipendenza (capacità e recupero da pianificare); le trasformazioni centralizzate nell'ESB semplificano i client ma l'ESB può accumulare logica di integrazione e complicarsi; cambi di policy toccano più client e servizi; occorre bilanciare interoperabilità con latenza, autonomia e complessità operativa.

## Perché importa

È l'applicazione delle tattiche *use an intermediary* e *encapsulation* ([[tattiche-modifiability]]) al livello dei servizi, con il relativo prezzo (hop in più, single point of failure → [[availability]]).

## Connessioni

- [[microservices]]: il gateway e la discovery sono tipici dei microservizi (figura «Microservices Architecture»).
- [[publish-subscribe]]: il message broker è un intermediario.
- [[servizi-e-soa]]: l'ESB come realizzazione della SOA.

## Fonti

- [[service-oriented-and-microservice-architectures]]; [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=34]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=42]]

_Aggiornato: 2026-11-24 — ingest 07— Service-Oriented and Microservice Architectures-1 part.pdf_
