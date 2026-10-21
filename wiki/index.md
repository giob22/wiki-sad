# Index — Software Architecture Design

## Overview
- [[overview]] — panoramica del corso, programma, copertura
- [[lezioni]] — **percorso di studio** lezione per lezione: un link per pagina, in ordine di slide, con ordine consigliato
- [[avanzamento-studio]] — check-list del programma: da fare (Claude) · studiato · consolidato (tu)
- [[glossario]] — termini inglese ↔ italiano
- [[log]] — registro cronologico delle operazioni sul wiki
- [[CLAUDE]] — regole e procedure del wiki (ingest, query, esercizi, esame, lint)

## Concetti

**Fondamenti** (Lez. 0–1)
- [[architettura-software]] — definizione di Bass, Clements, Kazman; punti fermi; ruolo nel processo (alta)
- [[strutture-e-viste]] — struttura architetturale, tre categorie, relazioni tra strutture, quali scegliere (alta)
- [[strutture-di-modulo]] — moduli, uses/generalizzazione/is-part-of; decomposizione, uses, layer, class, data model; modificabilità (alta)
- [[strutture-componenti-e-connettori]] — componenti, connettori, vista runtime, domande per QA (alta)
- [[strutture-di-allocazione]] — deployment, install, work assignment; «limitato dal componente meno scalabile» (alta)
- [[importanza-architettura-software]] — le 11 motivazioni §3.1–3.11 (alta)
- [[buone-pratiche-architetturali]] — raccomandazioni di processo, regole pratiche (media)

**Qualità** (Lez. 1)
- [[attributi-di-qualita]] — definizione, FR vs QR, runtime vs sviluppo, trade-off (alta)
- [[scenari-di-qualita]] — sei parti, Given–When–Then, generale vs concreto (alta)
- [[valutazione-attributi-di-qualita]] — prestazioni su C&C, analisi d'impatto, esercizio di modifica, DB a 30 tps (alta)
- [[tattiche-architetturali]] — tattiche di prestazioni, disponibilità, sicurezza, modificabilità (alta)
- [[pattern-architetturali]] — definizione, pattern = insieme di tattiche, Layers (alta)

**Attributi di qualità in dettaglio** (Lez. 2–3)
- [[availability]] — failure/fault/error, catena causale, MTBF/MTTR, SLA, «nove», scenari, RTO/RPO (alta)
- [[tattiche-availability]] — detect / recover / prevent, hot/warm/cold spare, tecnologie per gruppo (alta)
- [[modifiability]] — quattro domande, quando/chi, costo e debito tecnico, scalabilità, variabilità, portabilità, location independence, scenari (alta)
- [[tattiche-modifiability]] — increase cohesion, reduce coupling, defer binding per momento di binding (alta)
- [[pattern-modifiability]] — confronto client-server, plug-in, layers, publish-subscribe (alta)

**Processo Agile** (Lez. 6)
- [[sviluppo-agile]] — definizione, Manifesto (valori e principi), iterativo vs waterfall, ruoli (alta)
- [[cerimonie-e-artefatti-agile]] — planning, daily, demo, retrospettiva; backlog e burndown chart (alta)
- [[user-stories]] — tre aspetti, template, epic e task, INVEST, criteri vs DoD (alta)
- [[criteri-di-accettazione-e-bdd]] — criteri di accettazione, BDD, Gherkin Given–When–Then (alta)

**Progettazione e pattern** (Lez. 4)
- [[progettazione-basata-sul-riuso]] — strategie vs metodi, riuso dell'esperienza, tre alternative, ambito di applicabilità (alta)
- [[dssa]] — architetture di riferimento: definizione, esempi (web, TV, AUTOSAR, IoT, cloud), vantaggi e limiti (alta)
- [[linee-di-prodotto-software]] — comunanza vs variabilità, esempi per dominio (media)
- [[architetture-multi-tier]] — tier vs layer, 1/2/3-tier con attributi, middleware, 4-tier, load-balanced cluster (alta)

## Entità
- [[exam-booking-system]] — caso di studio: esempio guida della lezione 1
- [[layered]] — stile/pattern: strati, portabilità, layer bridging (parziale come stile)
- [[client-server]] — pattern: discovery + interazione, benefici e trade-off (parziale come stile)
- [[publish-subscribe]] — pattern: publisher, subscriber, event bus, invocazione implicita
- [[plug-in]] — pattern: nucleo + plug-in, microkernel
- [[circuit-breaker]] — pattern di disponibilità: stop alle chiamate a un servizio che non risponde; Resilience4j
- [[state-logic-display]] — pattern three-tier: display, logic, state
- [[mvc]] — pattern Model–View–Controller: responsabilità, quattro modelli di interazione, Observer, Strategy, Front Controller
- [[spring-mvc]] — framework: Spring Framework (IoC), Spring MVC (DispatcherServlet), Spring Boot
- [[sense-compute-control]] — pattern per il controllo di ambienti fisici: tre/quattro stadi, IoT, Lunar Lander, ADS
- [[microservices]] — stile: servizi indipendenti con propri dati (parziale)
- [[uml]] — linguaggio: notazione delle viste
- [[attribute-driven-design]] — processo: driver → concetti di progetto → strutture
- [[autosar]] — standard: architettura aperta automotive
- [[enactest]] — caso di studio: architettura a componenti di un progetto di ricerca
- [[software-architecture-in-practice]] — libro: testo base e altri testi del corso

## Fonti
- [[presentazione-corso]] — 00_IntroduzioneAlCorso_SAD.pdf, pp. 1–37
- [[introduzione-architettura-software]] — 01-IntroductionOnSoftwareArchitecture.pdf, pp. 1–50
- [[attributi-di-qualita-e-importanza-architettura]] — 01-IntroductionOnSoftwareArchitecture-2 parte.pdf, pp. 1–45 (slide 51–97)
- [[quality-attributes-availability]] — 02-Availability.pdf, pp. 1–23
- [[quality-attributes-modifiability]] — 03-Modifiability.pdf, pp. 1–33 (slide 1–34)
- [[approcci-riuso-progettazione-architettura]] — 04-Architectural Patterns.pdf, pp. 1–37 (slide 1–41)
- [[agile-project-management]] — 04_Agile_01.pdf, pp. 1–60
- [[architectural-patterns-mvc-scc]] — 3-Architectural Patterns-complete.pdf, parte nuova pp. 35–36, 39–96 (slide 38–39, 43–101)
- Programma ufficiale del corso: [[Programma Syllabus]] (raw/)

## Esercizi
- [[scenari-di-qualita-concreti]] — scenari di performance, modifiability e availability; da requisito a scenario (bassa)
- [[calcolo-disponibilita]] — MTBF/MTTR, downtime, tabella dei «nove» (bassa)
- [[analisi-impatto-modifiche]] — sei passi sulla vista dei moduli (bassa)
- [[applicazione-tattiche]] — tattica → dove → effetto → trade-off; dallo scenario alle decisioni; momento di binding (media)
- [[implementare-mvc]] — View con Strategy, ShowExamSessions in Spring MVC, applicazione spese (media)
- [[applicare-sense-compute-control]] — antintrusione, controllo accessi, Lunar Lander con simulazione, ADS (bassa)
- [[valutare-user-stories-invest]] — checklist INVEST, scomposizione di epic (cassiere, PayPal, gestione utenti) (bassa)
- [[da-criteri-di-accettazione-a-bdd]] — dai criteri agli scenari Gherkin (recupero password, login) (bassa)

## Progetto
- [[progetto-di-corso]] — organizzazione, iterazioni, calendario, valutazione; decisioni: nessuna ancora
- [[incontro-stakeholder-ba]] — appunti del primo confronto con lo stakeholder (BA.pdf): cosa è emerso e cosa cambia
- [[domande-al-committente]] — domande da porre al direttore del Banco (Open Questions Log), in ordine di priorità, con ipotesi e documenti da chiedere
- [[a2-stakeholder-e-contesto]] — capitolo A2 (issue S1-01): stakeholder, utenti e sistemi esterni, flussi, Context Diagram CTX-01, ipotesi e domande
- [[mascotte-pinguino]] — animazione fluida della mascotte del team (25 frame → 77 fotogrammi), gesti extra e script per rigenerarla
- [[burndown-github-project]] — burndown dello sprint sul GitHub Project del team, pesato con le taglie; script e workflow
- [[guida-progetto-picus]] — guida completa al progetto d'esame PICUS (presentazione, desiderata del committente, AGENTS.md del team, iterazione preparatoria, ruoli Scrum in 8)

## Esame
_nessun materiale ancora — lancia `prepara esame`_

## Asset
Figure in `raw/assets/`: 2 dalla presentazione (`lez00-intro-pN-*.png`), 24 da 01-IntroductionOnSoftwareArchitecture (`lez01-intro-pN-*.png`), 10 dalla parte 2 (`lez01b-qa-pN-*.png`; N = pagina del PDF, non numero di slide).
Progetto: 1 figura `prog-picus-p12-piano-iterazioni.png` (p. 12 di 00-Presentazione Progetto Picus.pdf).
Lez. 2: 13 figure `lez02-av-pN-*.png`; Lez. 3: 14 figure `lez03-mo-pN-*.png`; Lez. 4: 20 figure `lez04-ap-pN-*.png`; Lez. 5: 32 figure `lez05-ap-pN-*.png` (N = pagina di 3-Architectural Patterns-complete.pdf).
Animazioni SVG e grafico della Lez. 5 in `output/diagrammi/` (script [[genera_animazioni_lez05.py]]): [[anim-mvc-classico.svg]], [[anim-spring-mvc-richiesta.svg]], [[anim-sense-compute-control.svg]], [[grafico-lunar-lander-controllo.svg]].
Lez. 6: 25 figure `lez06-ag-pN-*.png`; animazione [[anim-ciclo-iterazione-agile.svg]] e grafico [[grafico-burndown-sprint.svg]] (script [[genera_grafici_lez06.py]]).
Diagrammi Mermaid ricostruiti (🧩) direttamente nelle pagine: vista dei moduli e versione event-based, vista runtime, deployment iniziale, tattiche di prestazioni e modificabilità, ADD, catena fault→error→failure, stati del circuit breaker, reduce coupling, plug-in, publish-subscribe, sequenza client-server.
