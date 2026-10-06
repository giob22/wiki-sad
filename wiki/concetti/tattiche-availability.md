---
tipo: concetto
importanza_esame: alta
prerequisiti: ["availability", "tattiche-architetturali"]
fonti_pdf: ["02-Availability.pdf#page=13", "02-Availability.pdf#page=14", "02-Availability.pdf#page=15", "02-Availability.pdf#page=16", "02-Availability.pdf#page=17", "02-Availability.pdf#page=18", "02-Availability.pdf#page=19", "02-Availability.pdf#page=23"]
termine_inglese: "availability tactics"
---

# Tattiche e pattern per l'availability

## Definizione

> 📄 Fonte: [[02-Availability.pdf#page=13]]

Le **tattiche di disponibilità** servono a permettere al sistema di **prevenire o sopportare** i guasti, così che il servizio fornito resti **conforme alla specifica**. Le tattiche **impediscono che i guasti diventino malfunzionamenti** o, almeno, **limitano gli effetti** del guasto e **rendono possibile la riparazione**.

![[lez02-av-p13-tattiche-controllo-risposta.png]]
*Figura di [[02-Availability.pdf#page=13]] (in alto a destra): un **Fault** entra nel blocco **Tactics to Control Response**; ne esce «fault masked, prevented, or repair made» (guasto mascherato, prevenuto, o riparazione effettuata).*

🧩 Collegamento con la catena di [[availability]]: le tattiche agiscono sul passaggio **error → failure** (rilevare, contenere, mascherare) e sui tempi di riparazione.

## Albero delle tattiche

> 📄 Fonte: [[02-Availability.pdf#page=14]]

![[lez02-av-p14-albero-tattiche-availability.png]]
*Figura di [[02-Availability.pdf#page=14]] (dal libro di Bass, Clements, Kazman): le tattiche di disponibilità in tre rami.*

| Detect Faults | Recover from Faults — Preparation and Repair | Recover from Faults — Reintroduction | Prevent Faults |
|---|---|---|---|
| Monitor | Redundant Spare | Shadow | Removal from Service |
| Ping/Echo | Rollback | State Resynchronization | Transactions |
| Heartbeat | Exception Handling | Escalating Restart | Predictive Model |
| Timestamp | Software Upgrade | Nonstop Forwarding | Exception Prevention |
| Condition Monitoring | Retry | | Increase Competence Set |
| Sanity Checking | Ignore Faulty Behavior | | |
| Voting | Graceful Degradation | | |
| Exception Detection | Reconfiguration | | |
| Self-Test | | | |

Nota della slide: queste tattiche sono **spesso fornite da un'infrastruttura software**, come un pacchetto **middleware**. Il lavoro dell'architetto può essere **scegliere e valutare** (più che implementare) le tattiche giuste e la **giusta combinazione** di tattiche.

Le slide spiegano solo le tattiche seguenti; le altre del diagramma sono solo elencate (TODO: da espandere se verranno trattate).

## Rilevare i guasti (*Detecting Faults*)

> 📄 Fonte: [[02-Availability.pdf#page=15]]

| Tattica | Cosa fa | Esempio (Exam Booking System) |
|---|---|---|
| **Monitor** | raccoglie indicatori di salute e di risorse | monitorare istanze applicative, connessioni al database, profondità della coda |
| **Ping / Echo** | verifica raggiungibilità e ritardo | il load balancer sonda ogni application server |
| **Heartbeat** | scambio di messaggi di «vita» (*liveness*) | il broker verifica se i consumatori delle notifiche sono vivi (controllando il reset di un *watchdog timer*) |
| **Condition Monitoring** | verifica le condizioni operative di un processo e le ipotesi di progetto | |
| **Voting** | confronta i risultati di componenti ridondanti | varianti: *replication* (previene guasti hardware ma non software) e *functional redundancy* (più componenti che realizzano diversità per progetto) |
| **Exception Detection** | rileva una condizione che altera il flusso normale di esecuzione | |

> 🧩 Elaborazione mia — ping/echo vs heartbeat: nel **ping/echo** è il controllore che interroga («ci sei?») e attende l'eco; nel **heartbeat** è il componente controllato che manda periodicamente un segnale, e il controllore si allarma se il segnale non arriva (il watchdog non viene resettato). Il primo misura anche il ritardo; il secondo costa meno al controllore.
>
> Perché la *replication* nel voting non copre i guasti software: repliche identiche eseguono lo stesso codice, quindi un difetto produce lo stesso risultato sbagliato in tutte e il voto non lo scopre. La *functional redundancy* usa implementazioni diverse, che difficilmente sbagliano allo stesso modo.

## Recuperare dai guasti (*Recovering from Faults*)

> 📄 Fonte: [[02-Availability.pdf#page=16]]

| Tattica | Cosa fa | Esempio |
|---|---|---|
| **Redundant Spare** | un duplicato subentra | un secondo application server riceve le richieste reindirizzate |
| **Retry** | ripete un'operazione dopo un guasto **transitorio** | ripetere una richiesta al SIS andata in timeout, con una politica **limitata** (*bounded*) |
| **Rollback** | riporta dati o computazione a uno **stato noto e corretto** | |
| **Exception Handling** | contiene l'errore e restituisce una **risposta controllata** (terminando…, restituendo codici d'errore o usando classi di eccezione) | |
| **Graceful Degradation** | mantiene le funzioni **più critiche**, abbandonando quelle meno critiche | preservare le prenotazioni ritardando notifiche o report |

🧩 Il retry deve essere **limitato**: se il guasto non è transitorio, ripetere all'infinito accumula richieste in attesa e peggiora la situazione — è il problema che risolve il circuit breaker (sotto).

## Prevenire i guasti (*Preventing Faults*)

> 📄 Fonte: [[02-Availability.pdf#page=17]]

| Tattica | Cosa fa | Esempio |
|---|---|---|
| **Removal from Service** | mette un componente fuori servizio **prima** che guasti latenti (memory leak, frammentazione…) colpiscano il servizio | riavviare un'istanza applicativa **alla volta** per ripulire le perdite di risorse |
| **Transactions** | sfrutta la semantica transazionale per l'alta disponibilità (vedi il protocollo **two-phase commit**, 2PC) | riservare il posto e registrare la prenotazione in **un'unica transazione atomica** |
| **Increase the competence set** | trattare **più condizioni anomale come casi normali** | Eligibility Checking distingue «**non ammissibile**» da «**SIS non disponibile**» |
| … | (l'elenco continua) | |

🧩 Perché «uno alla volta» in removal from service: con istanze replicate dietro al load balancer, togliere un'istanza lascia le altre a servire; toglierle tutte insieme sarebbe un'interruzione. L'esempio della transazione impedisce lo stato intermedio «posto riservato ma prenotazione non registrata» se il sistema cade a metà.

## Pattern di ridondanza

> 📄 Fonte: [[02-Availability.pdf#page=18]]

| Pattern | Come funziona | Failover | Costo | Fonte |
|---|---|---|---|---|
| **Active redundancy** (*hot spare*) | le repliche elaborano **lo stesso input** e mantengono lo **stato sincronizzato** | **veloce** | **alto** (risorse e sincronizzazione) | [[02-Availability.pdf#page=18]] |
| **Passive redundancy** (*warm spare*) | il componente attivo elabora le richieste e **aggiorna periodicamente** uno standby | intermedio | intermedio | [[02-Availability.pdf#page=18]] |
| **Cold spare** | lo standby **parte solo dopo** il guasto | **il più lento** | **il più basso** | [[02-Availability.pdf#page=18]] |

Il cold spare è **poco adatto** a sistemi con requisiti di alta disponibilità.

**Esempio guida:** gli application server replicati dietro al load balancer si comportano come **repliche attive** quando servono entrambi il traffico; un **database di standby** è di solito **warm o hot**, secondo la politica di replicazione e failover.

![[lez02-av-p18-pattern-ridondanza.png]]
*Figura di [[02-Availability.pdf#page=18]] (a destra): in alto un **Active-Active System**, con le richieste dei client inviate a Node 1 (Active) e Node 2 (Active); in basso un **Active-Passive System**, con le richieste a Node 1 (Active) e una freccia tratteggiata «On Failover» verso Node 2 (Passive).*

> 🧩 Elaborazione mia — legame con la formula $A \approx MTBF/(MTBF+MTTR)$ di [[availability]]: i tre pattern differiscono soprattutto per $MTTR$. Hot: il subentro è quasi immediato; warm: serve allineare lo stato dall'ultimo aggiornamento; cold: bisogna avviare lo standby da zero. Più basso l'$MTTR$, più alta la disponibilità, a costo maggiore.

## Pattern Circuit Breaker

> 📄 Fonte: [[02-Availability.pdf#page=19]]

Impedisce chiamate ripetute a un servizio che non risponde; dettagli e codice in [[circuit-breaker]].

## Dalle tattiche alle tecnologie di implementazione

> 📄 Fonte: [[02-Availability.pdf#page=23]]

![[lez02-av-p23-tattiche-tecnologie-gruppi.png]]
*Figura di [[02-Availability.pdf#page=23]] (slide in italiano): tabella con otto righe numerate nella colonna «Gruppo», ciascuna con problema, tattiche o pattern, tecnologie utilizzabili ed esperimento richiesto.*

| Gr. | Problema | Tattiche o pattern | Tecnologie utilizzabili | Esperimento richiesto |
|---|---|---|---|---|
| 1 | University SIS lento o indisponibile | timeout, bounded retry, circuit breaker, fallback | Spring Boot; WebClient o RestClient; Resilience4j TimeLimiter, Retry e CircuitBreaker; WireMock o Toxiproxy per simulare ritardi ed errori | introdurre ritardi e risposte HTTP 5xx; confrontare latenza, tentativi e comportamento con e senza protezione |
| 2 | guasto del database primario | active–passive redundancy, replication, health monitoring, failover | PostgreSQL streaming replication; Patroni; etcd o Consul; HAProxy; Docker Compose | arrestare il primario, osservare promozione dello standby e riconnessione; misurare RTO e possibile perdita di dati |
| 3 | sovraccarico del Booking Service | load balancing, horizontal scaling, health-based routing | più istanze Spring Boot; Docker; NGINX, HAProxy o Traefik; in alternativa Kubernetes Deployment, Service e HPA; k6 o JMeter | generare carico crescente; misurare throughput, tempi di risposta e distribuzione delle richieste |
| 4 | Notification Service indisponibile | asynchronous messaging, queue-based load leveling, store-and-forward | RabbitMQ; Spring AMQP; RabbitTemplate; @RabbitListener; durable queue e dead-letter queue | arrestare il consumer, produrre notifiche e verificare che vengano conservate e poi elaborate |
| 5 | Analytics esaurisce le risorse condivise | bulkhead, resource isolation, concurrency limiting | Resilience4j Bulkhead o ThreadPoolBulkhead; executor Java separati; HikariCP con pool distinti; limiti di risorse Docker o Kubernetes | saturare Analytics e verificare che Booking continui a rispondere |
| 6 | servizio secondario non disponibile | graceful degradation, fallback, cached response | Resilience4j CircuitBreaker; fallback Spring; Caffeine o Redis per dati temporaneamente memorizzati | disabilitare il servizio secondario e verificare che la funzione principale restituisca una risposta ridotta ma corretta |
| 7 | richieste duplicate | idempotency, duplicate detection, transactional uniqueness | Spring Boot; chiave di idempotenza; tabella PostgreSQL per le richieste elaborate; vincoli UNIQUE; eventuale transactional outbox | inviare più volte la stessa richiesta e verificare che si produca un solo effetto persistente |
| 8 | guasti difficili da individuare e diagnosticare | health monitoring, heartbeat, logging, metrics, distributed tracing | Spring Boot Actuator; Micrometer; Prometheus; Grafana; OpenTelemetry; Jaeger o Grafana Tempo | introdurre un guasto e ricostruirne il percorso con health status, metriche, log e trace distribuite |

> ❓ Salto non ricostruito: la colonna «Gruppo» e la colonna «Esperimento richiesto» suggeriscono che ogni riga sia un'**attività assegnata a un gruppo di studenti**, ma la slide non lo dice. Da chiarire a lezione (→ [[progetto-di-corso]]).

> 🧩 Elaborazione mia — alcune voci compaiono qui per la prima volta nel corso e le slide non le definiscono: *bulkhead* (isolare le risorse di un componente perché il suo sovraccarico non trascini gli altri, come i compartimenti stagni di una nave), *idempotency* (ripetere la stessa richiesta produce un solo effetto — utile proprio con il retry e con i messaggi duplicati della coda), *dead-letter queue* (coda dove finiscono i messaggi che non si riescono a elaborare).

## Perché importa

Mostra concretamente la seconda domanda della Lez. 1 (come ottenere una qualità con mezzi architetturali) per un attributo specifico, fino alle tecnologie del progetto (Spring Boot, Docker, RabbitMQ… → [[progetto-di-corso]]). Il programma prevede le tattiche per availability, deployability, modifiability, energy efficiency, performance, security, safety, testability, usability ([[Programma Syllabus]]).

> 🎯 Esame: i tre rami (detect, recover, prevent) con esempi; ping/echo vs heartbeat; hot/warm/cold spare e trade-off; circuit breaker.

## Connessioni

- [[availability]]: definizioni, misure, scenari.
- [[tattiche-architetturali]]: le prime tattiche di disponibilità (health check, redirect, ridondanza) viste nella Lez. 1.
- [[circuit-breaker]]: pattern per le chiamate a servizi inaffidabili.
- [[applicazione-tattiche]]: dallo scenario alle decisioni (caso 5).

## Fonti

- [[quality-attributes-availability]] — [[02-Availability.pdf#page=13]]–[[02-Availability.pdf#page=19]], [[02-Availability.pdf#page=23]]

_Aggiornato: 2026-09-30 — ingest 02-Availability.pdf_
