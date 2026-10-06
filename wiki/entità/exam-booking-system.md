---
tipo: entità
categoria: caso-di-studio
famiglia: ""
---

# Exam Booking System (esempio guida)

## Cos'è

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture.pdf#page=12]]

Sistema di **prenotazione degli esami** usato come **esempio guida** (*running example*) della lezione 1: un sistema familiare con **problemi architetturali non banali**.

| Aspetto | Contenuto della slide |
|---|---|
| Responsabilità funzionali | gli **studenti** consultano le sessioni d'esame e inviano o cancellano prenotazioni; il sistema **verifica le regole** di prenotazione e **invia notifiche**; i **docenti** vedono le liste dei partecipanti; gli **amministratori** gestiscono sessioni e regole |
| Picco di carico | quando **si aprono le prenotazioni** |
| Evoluzione | le **regole cambiano nel tempo** |
| L'architettura aiuta a ragionare su | modificabilità, prestazioni, disponibilità, sicurezza |

Lo stesso sistema viene esaminato attraverso le viste **di modulo, runtime e di deployment**.

![[lez01-intro-p12-exam-booking-system.png]]
*Figura di [[01-IntroductionOnSoftwareArchitecture.pdf#page=12]]: a sinistra la descrizione del sistema; al centro tre riquadri — Functional responsibilities, Peak load when booking opens, Rules change over time; a destra «Architecture helps us reason about: modifiability, performance, availability, security».*

🧩 I tre riquadri centrali corrispondono ciascuno a un attributo: il picco → prestazioni e scalabilità; le regole che cambiano → modificabilità; i dati degli studenti e i ruoli → sicurezza.

## Come si usa nel corso — mappa dell'esempio

| Tema | Cosa si mostra | Pagina wiki | Fonte |
|---|---|---|---|
| Tre viste | moduli / C&C / allocazione | [[strutture-e-viste]] | [[01-IntroductionOnSoftwareArchitecture.pdf#page=13]] |
| Vista dei moduli (uses) | Booking usa Authentication, Exam Catalog, Eligibility Checking, Notifications | [[strutture-di-modulo]] | [[01-IntroductionOnSoftwareArchitecture.pdf#page=14]] |
| Ragionamento di modificabilità | responsabilità, eventi, modulo Student Records | [[strutture-di-modulo]] | [[01-IntroductionOnSoftwareArchitecture.pdf#page=15]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=16]] |
| Decomposizione UML | package Student-facing Applications, Shared Client Code, Server-side Modules | [[strutture-di-modulo]] | [[01-IntroductionOnSoftwareArchitecture.pdf#page=19]] |
| Vista runtime | Web Client → API → Booking Service → DB + coda → Notification Service | [[strutture-componenti-e-connettori]] | [[01-IntroductionOnSoftwareArchitecture.pdf#page=28]]–[[01-IntroductionOnSoftwareArchitecture.pdf#page=31]] |
| Deployment | configurazione iniziale e scalabile con load balancer | [[strutture-di-allocazione]] | [[01-IntroductionOnSoftwareArchitecture.pdf#page=39]]–[[01-IntroductionOnSoftwareArchitecture.pdf#page=41]] |
| Requisiti di qualità di una responsabilità | verifica di ammissibilità: 500 ms, 2 s, … | [[attributi-di-qualita]] | [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=5]] |
| Scenari concreti | performance (5.000 richieste/min), modifiability (nuova regola) | [[scenari-di-qualita-concreti]] | [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=14]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=16]] |
| Valutazione | DB a 30 transazioni/s; analisi d'impatto | [[valutazione-attributi-di-qualita]], [[analisi-impatto-modifiche]] | [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=15]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=17]] |
| Tattiche | prestazioni, disponibilità, sicurezza, modificabilità | [[tattiche-architetturali]], [[applicazione-tattiche]] | [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=23]]–[[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=30]] |
| Catena fault → error → failure | SIS non disponibile → dati dello studente mancanti → esito di ammissibilità sbagliato | [[availability]] | [[02-Availability.pdf#page=5]] |
| Scenario di disponibilità | un application server non risponde: rilevazione ≤ 30 s, ripristino ≤ 60 s | [[scenari-di-qualita-concreti]] | [[02-Availability.pdf#page=9]] |
| Tattiche e pattern di disponibilità | health check, retry verso il SIS, transazioni, repliche, circuit breaker; RTO/RPO del DB | [[tattiche-availability]], [[circuit-breaker]] | [[02-Availability.pdf#page=15]]–[[02-Availability.pdf#page=23]] |
| Quando e chi modifica | dalla logica di ammissibilità nel codice alle regole aggiornate a runtime | [[modifiability]] | [[03-Modifiability.pdf#page=6]] |
| Costo della modifica | limite di prenotazioni scritto nel codice vs scaling automatico | [[modifiability]] | [[03-Modifiability.pdf#page=8]], [[03-Modifiability.pdf#page=9]] |
| Tattiche di modificabilità | split/redistribute, API di ammissibilità, event bus, adapter SIS A/B, binding con Maven e Spring | [[tattiche-modifiability]] | [[03-Modifiability.pdf#page=19]]–[[03-Modifiability.pdf#page=25]] |
| MVC classico | prenotare una sessione: View, Booking Controller, Model del dominio | [[mvc]] | [[3-Architectural Patterns-complete.pdf#page=44]] |
| Strategy | ExamCalendarView con BrowseController, BookingController, AdministrationController | [[implementare-mvc]] | [[3-Architectural Patterns-complete.pdf#page=51]], [[3-Architectural Patterns-complete.pdf#page=52]] |
| Spring MVC | requisito ShowExamSessions: `GET /exam-sessions` | [[spring-mvc]] | [[3-Architectural Patterns-complete.pdf#page=63]]–[[3-Architectural Patterns-complete.pdf#page=67]] |

## Elementi del sistema (glossario dell'esempio)

| Elemento | Tipo | Ruolo |
|---|---|---|
| Booking | modulo | gestione delle prenotazioni |
| Eligibility Checking | modulo | verifica delle regole di ammissione (prerequisiti) |
| Exam Catalog | modulo | catalogo delle sessioni d'esame |
| Notifications | modulo | notifiche agli studenti |
| Authentication | modulo | autenticazione |
| Administration | modulo | gestione di sessioni e regole |
| Student Records | modulo (aggiunto a p. 16) | API di accesso ai dati degli studenti |
| Booking Service | componente | contiene Booking + Eligibility Checking |
| Notification Service | componente | invia le email |
| Message Queue / Message Broker | componente / nodo | notifica asincrona (AMQP) |
| University SIS | sistema esterno | *Student Information System*, possiede i dati accademici |
| SIS Adapter | componente (tattica) | intermediario verso il SIS |

## Link ai concetti correlati

[[architettura-software]] · [[strutture-e-viste]] · [[attributi-di-qualita]] · [[tattiche-architetturali]]

## Fonti

- [[introduzione-architettura-software]], [[attributi-di-qualita-e-importanza-architettura]]

_Aggiornato: 2026-09-26 — ingest lezione 1_
_Aggiornato: 2026-09-30 — usi dell'esempio nelle Lez. 2 (availability) e 3 (modifiability)_
_Aggiornato: 2026-10-06 — usi dell'esempio nella lezione su MVC e Spring MVC_
