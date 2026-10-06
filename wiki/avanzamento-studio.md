# Avanzamento dello studio — Software Architecture Design

Check-list degli argomenti del programma, per seguire lo stato di avanzamento.

| Casella | Chi la spunta | Significato |
|---|---|---|
| **da fare** | Claude, a ogni ingest | l'argomento è stato trattato in una lezione ingerita e le pagine del wiki sono pronte da studiare |
| **studiato** | tu | hai letto e capito le pagine dell'argomento |
| **consolidato** | tu | l'hai ripassato e sai esporlo all'orale |

Gli argomenti seguono il **programma ufficiale** del corso → [[Programma Syllabus]] (versione estesa del programma delle slide di presentazione, [[00_IntroduzioneAlCorso_SAD.pdf#page=15]]–[[00_IntroduzioneAlCorso_SAD.pdf#page=17]]). Se la docente cambia il programma durante il corso, gli argomenti nuovi si aggiungono con la nota *(aggiunto: Lez. N)* e quelli tolti si barrano (~~così~~) con la nota *(non trattato)*: le caselle già spuntate non si cancellano. Percorso di lettura lezione per lezione → [[lezioni]]

---

## A. Architetture software: concetti fondamentali

**A1. Definizioni di architettura software** — Lez. 0, Lez. 1 → [[architettura-software]]
- [x] da fare
- [ ] studiato
- [ ] consolidato

**A2. Architettura come insieme di strutture e viste: strutture modulari, dei componenti e connettori, di allocazione** — Lez. 1 → [[strutture-e-viste]], [[strutture-di-modulo]], [[strutture-componenti-e-connettori]], [[strutture-di-allocazione]], [[uml]]
- [x] da fare
- [ ] studiato
- [ ] consolidato

**A3. Ruolo e importanza dell'architettura nei processi di sviluppo software** — Lez. 1 → [[importanza-architettura-software]], [[enactest]], [[autosar]]
- [x] da fare
- [ ] studiato
- [ ] consolidato

## B. Qualità delle architetture software

**B1. Attributi di qualità: definizione, requisiti funzionali e di qualità, trade-off, valutazione** — Lez. 1 → [[attributi-di-qualita]], [[valutazione-attributi-di-qualita]], [[analisi-impatto-modifiche]], [[exam-booking-system]]
- [x] da fare
- [ ] studiato
- [ ] consolidato

### Attributi osservabili a run-time

**B2. Performance** — per ora solo prime tattiche nella Lez. 1 (vedi F0)
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**B3. Security** — per ora solo prime tattiche nella Lez. 1 (vedi F0)
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**B4. Availability** — Lez. 2 → [[availability]], [[calcolo-disponibilita]]
- [x] da fare
- [ ] studiato
- [ ] consolidato

**B5. Functionality**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**B6. Usability**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

### Attributi non osservabili a run-time

**B7. Modifiability** — Lez. 3 → [[modifiability]]
- [x] da fare
- [ ] studiato
- [ ] consolidato

**B8. Portability** — Lez. 3, come variante della modificabilità (nella pagina «modifiability»)
- [x] da fare
- [ ] studiato
- [ ] consolidato

**B9. Reusability**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**B10. Integrability**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**B11. Testability**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

### Specifica e antipattern

**B12. Specificare gli attributi di qualità con gli scenari di qualità (cenni)** — Lez. 1, esempi nelle Lez. 2–3 → [[scenari-di-qualita]], [[scenari-di-qualita-concreti]]
- [x] da fare
- [ ] studiato
- [ ] consolidato

**B13. Architectural anti-patterns**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

## C. Progettazione architetturale

**C1. Principi di progettazione architetturale** — Lez. 1 (raccomandazioni, regole pratiche, ADD) → [[buone-pratiche-architetturali]], [[attribute-driven-design]]
- [x] da fare
- [ ] studiato
- [ ] consolidato

**C2. Progettazione basata sul riuso di esperienza: pattern, stili e tattiche** — Lez. 1, Lez. 4 → [[pattern-architetturali]], [[progettazione-basata-sul-riuso]]
- [x] da fare
- [ ] studiato
- [ ] consolidato

## D. Pattern architetturali

**D1. State-Logic-Display** — Lez. 4, con le architetture 1/2/3-tier e il middleware → [[state-logic-display]], [[architetture-multi-tier]]
- [x] da fare
- [ ] studiato
- [ ] consolidato

**D2. Sense-Compute-Control** — Lez. 5, con IoT, Lunar Lander e ADS → [[sense-compute-control]], [[applicare-sense-compute-control]]
- [x] da fare
- [ ] studiato
- [ ] consolidato

**D3. Model-View-Controller (MVC)** — Lez. 5, con Observer, Strategy, Front Controller → [[mvc]], [[implementare-mvc]]
- [x] da fare
- [ ] studiato
- [ ] consolidato

**D4. Pattern per architetture a microservizi** — cenni nelle Lez. 0–1 alla pagina [[microservices]]
- [ ] da fare
- [ ] studiato
- [ ] consolidato

## E. Stili architetturali

**E1. Stile procedurale e object-oriented**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**E2. Stile a livelli: macchine virtuali** — Lez. 3, come pattern Layers per la modificabilità → [[layered]]
- [x] da fare
- [ ] studiato
- [ ] consolidato

**E3. Stile a livelli: client-server** — Lez. 3, come pattern per la modificabilità; Lez. 4, come architettura 2-tier → [[client-server]]
- [x] da fare
- [ ] studiato
- [ ] consolidato

**E4. Data-flow (batch e pipe-and-filter)**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**E5. A memoria condivisa (blackboard e rule-based)**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**E6. Basato su interprete (codice mobile)**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**E7. Invocazione implicita: publish-subscribe** — Lez. 3, come pattern per la modificabilità → [[publish-subscribe]]
- [x] da fare
- [ ] studiato
- [ ] consolidato

**E8. Invocazione implicita: event-based**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**E9. Stile a oggetti distribuiti**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**E10. Stile Service Oriented (SOA)**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**E11. Stile a microservizi** — cenni nelle Lez. 0–1 (pagina «microservices»)
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**E12. Stile RESTful**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

## F. Tattiche per realizzare gli attributi di qualità

**F0. Tattiche architetturali: definizione, rapporto con i pattern, prime tattiche (prestazioni, disponibilità, sicurezza, modificabilità) sull'esempio guida** — Lez. 1 → [[tattiche-architetturali]], [[applicazione-tattiche]]
- [x] da fare
- [ ] studiato
- [ ] consolidato

**F1. Tattiche per l'availability** (con pattern di ridondanza e circuit breaker) — Lez. 2 → [[tattiche-availability]], [[circuit-breaker]]
- [x] da fare
- [ ] studiato
- [ ] consolidato

**F2. Tattiche per la deployability**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**F3. Tattiche per la modifiability** (con i pattern per la modificabilità) — Lez. 3 → [[tattiche-modifiability]], [[pattern-modifiability]]
- [x] da fare
- [ ] studiato
- [ ] consolidato

**F4. Tattiche per l'energy efficiency**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**F5. Tattiche per la performance**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**F6. Tattiche per la security**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**F7. Tattiche per la safety**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**F8. Tattiche per la testability**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**F9. Tattiche per la usability**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

## G. Soluzioni architetturali

**G1. Accesso alle risorse tramite interfacce; progettazione delle interfacce e stili di interazione**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**G2. Rappresentazione e struttura delle risorse scambiate (XML, JSON, binario)**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**G3. Virtualizzazione e cloud computing**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

## H. Documentare le architetture software

**H1. Stili di documentazione per la vista modulare, dei componenti e connettori e di distribuzione**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**H2. Documentare contesto, comportamento, decisioni di progetto e interfacce dei componenti**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**H3. Cenni allo standard ISO/IEC 42010 (Architecture Description)**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

## I. Sviluppo di architetture con processi iterativi e incrementali

**I1. Sviluppo iterativo e incrementale: differenze rispetto al waterfall**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**I2. Unified Process: fasi di ideazione, elaborazione, costruzione e transizione**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**I3. Discipline e pratiche di UP**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

## J. Sviluppo Agile e gestione Agile dei progetti

> Il modo in cui questi temi si applicano al progetto di gruppo è in [[progetto-di-corso]].

**J1. Principi dello sviluppo Agile, Manifesto Agile e pratiche Agili**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**J2. Test Driven Development (TDD) e refactoring**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**J3. Continuous Integration (CI)**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**J4. Framework Scrum: ruoli, backlog, pratiche**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

## K. Sviluppo iterativo e gestione della configurazione del software

**K1. Gestione delle versioni del software**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**K2. Version control centralizzato e distribuito**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**K3. Processo di build e agile building, continuous integration, DevOps**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**K4. Gestione delle richieste di cambiamento del software**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**K5. Gestione delle release**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

## L. Cenni alle architetture software di nuova generazione

**L1. Sistemi cyber-fisici e Internet of Things**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**L2. Architetture a microservizi e cloud-native**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**L3. Sistemi distribuiti edge–cloud**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**L4. Architetture che integrano componenti di intelligenza artificiale**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**L5. Architetture per sistemi autonomi e adattivi**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**L6. Applicazioni basate su modelli di machine learning e Large Language Model** (esempi: smart city, industria 4.0, automotive, sanità digitale, robotica)
- [ ] da fare
- [ ] studiato
- [ ] consolidato

---

## Argomenti aggiunti durante il corso

**X1. Pattern Plug-in** *(aggiunto: Lez. 3 — pattern per la modificabilità, non presente nel programma)* → [[plug-in]]
- [x] da fare
- [ ] studiato
- [ ] consolidato

**X2. Linee di prodotto software** *(aggiunto: Lez. 4 — non presente nel programma)* → [[linee-di-prodotto-software]]
- [x] da fare
- [ ] studiato
- [ ] consolidato

**X3. Spring Framework, Spring MVC e Spring Boot** *(aggiunto: Lez. 5 — tecnologia, non presente nel programma; utile per il progetto)* → [[spring-mvc]]
- [x] da fare
- [ ] studiato
- [ ] consolidato

## Argomenti del programma delle slide assenti dal programma ufficiale

Il programma delle slide di presentazione ([[00_IntroduzioneAlCorso_SAD.pdf#page=15]]–[[00_IntroduzioneAlCorso_SAD.pdf#page=17]]) cita anche questi argomenti, che nel programma ufficiale non compaiono. Restano qui finché non si capisce se verranno trattati; se no, si barrano.

**Y1. Code smell** (oltre agli antipattern architetturali)
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**Y2. Strumenti di analisi statica e dinamica (SonarQube, CodeScene…)**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**Y3. DSSA (Domain-Specific Software Architectures)** — Lez. 4 (trattata, anche se assente dal programma ufficiale) → [[dssa]]
- [x] da fare
- [ ] studiato
- [ ] consolidato

**Y4. Stile monolitico**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**Y5. Containerizzazione (Docker)** — tecnologia proposta per il progetto
- [ ] da fare
- [ ] studiato
- [ ] consolidato

**Y6. XP (Extreme Programming)**
- [ ] da fare
- [ ] studiato
- [ ] consolidato

_Aggiornato: 2026-09-27 — creata dal programma di 00_IntroduzioneAlCorso_SAD.pdf; «da fare» spuntato per gli argomenti di Lez. 0–1_
_Aggiornato: 2026-09-30 — riallineata al programma ufficiale (raw/Programma Syllabus.md); «da fare» spuntato per gli argomenti delle Lez. 2 (availability) e 3 (modifiability)_
_Aggiornato: 2026-10-01 — «da fare» spuntato per D1 e Y3 (Lez. 4); aggiunto X2 (linee di prodotto)_
_Aggiornato: 2026-10-06 — «da fare» spuntato per D2 (Sense–Compute–Control) e D3 (MVC); aggiunto X3 (Spring)_
