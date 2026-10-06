---
tipo: fonte
titolo: "Quality Attributes of an Architecture — Availability"
file_raw: "02-Availability.pdf"
pagine: "1-23"
data_ingest: 2026-09-30
formato: slide-pdf
riferimento_libro: "Bass, Clements, Kazman — Software Architecture in Practice, capp. 4-13"
argomenti: [availability, failure, fault, error, catena fault-error-failure, faultlessness, fault tolerance, recoverability, MTBF, MTTR, SLA, tabella dei nove, scenario generale di availability, scenari concreti, tattiche detect/recover/prevent, active/passive redundancy, cold spare, circuit breaker, RTO, RPO, tecnologie di implementazione]
---

# Availability — 02-Availability.pdf

Numerazione: pagina del PDF = numero stampato sulla slide. Alcune slide sono in italiano (p. 23).

## Sommario

Prima lezione della serie «Quality Attributes of an Architecture» (capp. 4–13 di Bass, Clements, Kazman), che per ogni attributo dà definizioni, scenari, tattiche e pattern. La **disponibilità** è il grado in cui il sistema è operativo e accessibile quando serve; riguarda la capacità di impedire che i guasti diventino malfunzionamenti, continuare nonostante i guasti e ripristinare il servizio. Si distinguono **failure** (esterno, osservabile), **fault** (causa) ed **error** (stato interno scorretto), legati dalla catena fault → activation → error → propagation → failure, interrotta se l'errore è rilevato, contenuto o mascherato; la disponibilità dipende da faultlessness, fault tolerance e recoverability. Si misura come $MTBF/(MTBF+MTTR)$ e si garantisce con uno **SLA**; la tabella dei «nove» traduce le percentuali in downtime. Seguono lo scenario generale di disponibilità (tre slide) e due scenari concreti (server farm, Exam Booking System con rilevazione ≤ 30 s e ripristino ≤ 60 s). Le **tattiche** sono organizzate in detect, recover (preparation and repair, reintroduction) e prevent; le slide spiegano monitor, ping/echo, heartbeat, condition monitoring, voting, exception detection; redundant spare, retry, rollback, exception handling, graceful degradation; removal from service, transactions, increase competence set. Si presentano i **pattern di ridondanza** (hot, warm, cold spare) e il **circuit breaker** con Resilience4j. La lezione chiude passando dallo scenario alle decisioni architetturali (con RTO/RPO per il database), con la figura della configurazione prima/dopo il guasto e con una tabella di otto gruppi che associa a ogni problema tattiche, tecnologie ed esperimento richiesto.

## Punti chiave

1. Titolo della serie e capitoli del libro ([[02-Availability.pdf#page=1]]); sezione Availability ([[02-Availability.pdf#page=2]]).
2. Definizione di availability e tre capacità; obiettivo sull'interruzione cumulativa ([[02-Availability.pdf#page=3]]).
3. Failure, fault, error; faultlessness, fault tolerance, recoverability ([[02-Availability.pdf#page=4]]); catena causale con esempio del Booking System ([[02-Availability.pdf#page=5]]).
4. Misura come probabilità; $A \approx MTBF/(MTBF+MTTR)$; SLA e penali ([[02-Availability.pdf#page=6]]); tabella dei «nove» su 90 giorni e un anno ([[02-Availability.pdf#page=7]]).
5. Scenario concreto della server farm ([[02-Availability.pdf#page=8]]); scenario dell'Exam Booking System ([[02-Availability.pdf#page=9]], ripetuto a [[02-Availability.pdf#page=20]]).
6. Scenario generale di disponibilità in tre parti ([[02-Availability.pdf#page=10]]–[[02-Availability.pdf#page=12]]).
7. Failure vs fault; scopo delle tattiche ([[02-Availability.pdf#page=13]]); albero delle tattiche, ruolo del middleware e dell'architetto ([[02-Availability.pdf#page=14]]).
8. Detecting faults ([[02-Availability.pdf#page=15]]); recovering from faults ([[02-Availability.pdf#page=16]]); preventing faults ([[02-Availability.pdf#page=17]]).
9. Pattern di ridondanza hot/warm/cold e applicazione all'esempio guida ([[02-Availability.pdf#page=18]]); circuit breaker con Resilience4j ([[02-Availability.pdf#page=19]]).
10. Dallo scenario alle decisioni: tre guasti, rilevazione, risposta, misura (RTO ≤ 5 min, RPO ≤ 1 min) ([[02-Availability.pdf#page=21]]); configurazioni prima e dopo il guasto ([[02-Availability.pdf#page=22]]).
11. Dalle tattiche alle tecnologie: tabella di otto gruppi ([[02-Availability.pdf#page=23]]).

## Concetti introdotti

- [[availability]]
- [[tattiche-availability]]
- Entità: [[circuit-breaker]]
- Esercizi: [[calcolo-disponibilita]]; casi aggiunti a [[scenari-di-qualita-concreti]] e [[applicazione-tattiche]]

## Domande aperte

- La tabella di [[02-Availability.pdf#page=23]] con la colonna «Gruppo» ed «Esperimento richiesto» è un'assegnazione ai gruppi del progetto? (→ [[progetto-di-corso]])
- Nell'albero di [[02-Availability.pdf#page=14]] ci sono tattiche solo nominate: timestamp, sanity checking, self-test, software upgrade, ignore faulty behavior, reconfiguration, shadow, state resynchronization, escalating restart, nonstop forwarding, predictive model, exception prevention.
- Refusi: «Tacticts» ([[02-Availability.pdf#page=13]]); nella tabella di [[02-Availability.pdf#page=7]] il downtime annuo a 99,9 % è 8 h 45 min 36 s, non «8 hr, 0 min, 46 sec» (derivazione in [[availability]]); lo schema accanto allo scenario dell'Exam Booking System ([[02-Availability.pdf#page=9]], [[02-Availability.pdf#page=20]]) riporta i valori della server farm.

## Domande da esame

- Definisci la disponibilità. Che differenza c'è tra failure, fault ed error? Descrivi la catena causale.
- Da cosa dipende la disponibilità (faultlessness, fault tolerance, recoverability)?
- Come si misura la disponibilità? Cos'è uno SLA? Quanto downtime annuo corrisponde a 99,99 %?
- Scrivi uno scenario di disponibilità per l'Exam Booking System.
- Descrivi le tattiche per rilevare, recuperare e prevenire i guasti. Differenza tra ping/echo e heartbeat.
- Confronta hot, warm e cold spare.
- Cos'è il pattern circuit breaker e quale problema risolve?
- Cosa sono RTO e RPO?

_Aggiornato: 2026-09-30 — ingest_
