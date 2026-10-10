# Overview — Software Architecture Design

Corso della LM in Ingegneria Informatica (Computer Engineering), UNINA — DIETI, a.a. 2026/27, 6 CFU (30 h teoria + 14 h pratica + 4 h seminari). Docente: **prof. Anna Rita Fasolino**. Lezioni dal 14 settembre al 18 dicembre 2026, martedì e giovedì 12:30–14:30 ([[00_IntroduzioneAlCorso_SAD.pdf#page=1]], [[00_IntroduzioneAlCorso_SAD.pdf#page=30]]). Testo base: Bass, Clements, Kazman, *Software Architecture in Practice*, 4ª ed. ([[software-architecture-in-practice]]).

**Obiettivo:** conoscenze e competenze per **progettare, documentare e modellare, sviluppare** architetture software ([[00_IntroduzioneAlCorso_SAD.pdf#page=12]]).

**Esame:** progetto di gruppo Agile (50 %) + orale (50 %) con giustificazione delle scelte di progetto → [[progetto-di-corso]] ([[00_IntroduzioneAlCorso_SAD.pdf#page=29]]).

Elenco lezioni e percorso di lettura → [[lezioni]] · Stato dello studio → [[avanzamento-studio]] · Catalogo di tutte le pagine → [[index]] · Registro delle operazioni → [[log]]

## Programma

> 📄 Fonte: programma ufficiale [[Programma Syllabus]]; versione breve nelle slide di presentazione [[00_IntroduzioneAlCorso_SAD.pdf#page=15]]–[[00_IntroduzioneAlCorso_SAD.pdf#page=17]]

| Blocco | Argomenti | Pagine wiki | Stato |
|---|---|---|---|
| Concetti fondamentali | definizioni; strutture e viste (modulari, C&C, allocazione); ruolo e importanza dell'architettura | [[architettura-software]], [[strutture-e-viste]], [[strutture-di-modulo]], [[strutture-componenti-e-connettori]], [[strutture-di-allocazione]], [[importanza-architettura-software]] | trattato (Lez. 1) |
| Qualità | attributi osservabili a run-time (performance, security, availability, functionality, usability) e non osservabili (modifiability, portability, reusability, integrability, testability); scenari di qualità (cenni); antipattern architetturali | [[attributi-di-qualita]], [[scenari-di-qualita]], [[valutazione-attributi-di-qualita]], [[availability]], [[modifiability]] | availability (Lez. 2) e modifiability/portability (Lez. 3) trattati; gli altri attributi e gli antipattern da trattare |
| Progettazione | principi; riuso dell'esperienza con pattern, stili e tattiche | [[pattern-architetturali]], [[attribute-driven-design]], [[buone-pratiche-architetturali]], [[progettazione-basata-sul-riuso]], [[dssa]], [[linee-di-prodotto-software]] | trattato (Lez. 1, Lez. 4: strategie e metodi, alternative di progetto, DSSA, linee di prodotto) |
| Pattern architetturali | State-Logic-Display, Sense-Compute-Control, MVC, pattern per microservizi | [[state-logic-display]], [[architetture-multi-tier]], [[mvc]], [[spring-mvc]], [[sense-compute-control]] | State-Logic-Display e multi-tier (Lez. 4); MVC con Spring MVC e Sense–Compute–Control (Lez. 5); pattern per microservizi da trattare |
| Stili architetturali | procedurale e OO; a livelli (macchine virtuali, client-server); data-flow; memoria condivisa; interprete; invocazione implicita (publish-subscribe, event-based); oggetti distribuiti; SOA; microservizi; RESTful | [[layered]], [[client-server]], [[publish-subscribe]], [[microservices]] | layers, client-server e publish-subscribe visti come pattern per la modificabilità (Lez. 3); gli altri da trattare |
| Tattiche | availability, deployability, modifiability, energy efficiency, performance, security, safety, testability, usability | [[tattiche-architetturali]], [[tattiche-availability]], [[tattiche-modifiability]], [[pattern-modifiability]] | availability (Lez. 2) e modifiability (Lez. 3); prime tattiche di performance e security nella Lez. 1 |
| Soluzioni architetturali | interfacce e stili di interazione; XML, JSON, binario; virtualizzazione e cloud | — | da trattare |
| Documentazione | stili di documentazione delle viste; contesto, comportamento, decisioni, interfacce; ISO/IEC 42010 | — | da trattare |
| Processi iterativi e incrementali | iterativo vs waterfall; Unified Process | [[sviluppo-agile]] (sezione sviluppo iterativo) | iterativo vs waterfall trattato (Lez. 6); Unified Process da trattare |
| Agile | principi, manifesto, TDD, refactoring, CI; Scrum | [[cerimonie-e-artefatti-agile]], [[user-stories]], [[criteri-di-accettazione-e-bdd]], [[progetto-di-corso]] | manifesto, principi, ruoli, cerimonie, artefatti, user story, BDD (Lez. 6); TDD, refactoring, CI e stima delle storie da trattare |
| Gestione della configurazione | version control, build, CI, DevOps, change request, release | — | da trattare |
| Architetture di nuova generazione (cenni) | IoT, cloud-native, edge–cloud, IA, sistemi autonomi, ML e LLM | — | da trattare |

## Filo logico finora

L'**architettura** è l'insieme delle strutture necessarie per ragionare sul sistema ([[architettura-software]]). Le strutture sono di tre tipi — moduli, componenti e connettori, allocazione — e ognuna serve a ragionare su qualità diverse ([[strutture-e-viste]]): i moduli sulla modificabilità, la vista runtime su prestazioni, disponibilità, sicurezza, scalabilità, il deployment sulla disponibilità e sui colli di bottiglia dell'intero percorso. Le qualità — non la funzionalità — determinano l'architettura ([[attributi-di-qualita]]). Si **esprimono** con scenari in sei parti ([[scenari-di-qualita]]), si **ottengono** con tattiche e pattern ([[tattiche-architetturali]], [[pattern-architetturali]]), si **valutano** sull'architettura prima che il sistema esista ([[valutazione-attributi-di-qualita]]). Tutto è mostrato su un esempio guida, l'[[exam-booking-system]]. La Lez. 1 chiude con le motivazioni dell'architettura ([[importanza-architettura-software]]) e con le pratiche e il metodo ADD per costruirla ([[buone-pratiche-architetturali]], [[attribute-driven-design]]).

Dalla Lez. 2 si studiano gli attributi uno per uno, sempre con lo schema **definizione → misure → scenario → tattiche → pattern** (capp. 4–13 del libro). La **disponibilità** ([[availability]]) si misura con MTBF/MTTR e si ottiene rilevando, recuperando e prevenendo i guasti, con ridondanza e circuit breaker ([[tattiche-availability]]); la lezione arriva fino alle tecnologie (Spring Boot, Resilience4j, PostgreSQL, RabbitMQ). La **modificabilità** ([[modifiability]]) riduce costo e rischio delle modifiche: si pianifica con quattro domande (cosa, probabilità, quando/chi, costo), si ottiene aumentando la coesione, riducendo l'accoppiamento e posticipando il binding ([[tattiche-modifiability]]), e si incarna in quattro pattern — client-server, plug-in, layers, publish-subscribe ([[pattern-modifiability]]).

La Lez. 4 risponde a «come si progetta un'architettura?»: riusando l'esperienza ([[progettazione-basata-sul-riuso]]). Le forme di riuso vanno dalla più generale alla più specifica del dominio — design pattern, stili, pattern architetturali, **DSSA** o architetture di riferimento ([[dssa]]) — e il riuso pianificato dentro un'azienda prende la forma delle **linee di prodotto** ([[linee-di-prodotto-software]]). Il primo pattern studiato è **State-Logic-Display** ([[state-logic-display]]), un caso delle **architetture multi-tier**, dove i *tier* (distribuzione fisica) vanno distinti dai *layer* (decomposizione logica) e ogni scelta di 1, 2, 3 o n tier ha benefici e limiti precisi sugli attributi di qualità ([[architetture-multi-tier]]).

La Lez. 5 completa i pattern. Il **middleware** collega i tier e i sistemi esterni. Il **Model–View–Controller** ([[mvc]]) separa dati, presentazione e interazione: le responsabilità sono fisse, le interazioni variano (pull, Observer, web lato server, UI reattiva) e il MVC classico combina i design pattern Observer e Strategy. **Spring MVC** ([[spring-mvc]]) realizza il web MVC lato server con un Front Controller, il DispatcherServlet, e Spring Boot ne semplifica l'avvio. Il **Sense–Compute–Control** ([[sense-compute-control]]) struttura i sistemi che controllano un ambiente fisico con un ciclo sensori → calcolo → attuatori, in tre o quattro stadi, fino all'IoT e alla guida autonoma.

La Lez. 6 passa al **processo**: lo sviluppo **Agile** consegna valore per piccoli incrementi in iterazioni brevi, guidato dai valori e principi del Manifesto. Ruoli (Product Owner, Scrum Master, team), **cerimonie** (planning, daily, demo, retrospettiva) e **artefatti** (backlog, burndown) organizzano il lavoro; i requisiti si scrivono come **user story** che rispettano INVEST, completate da **criteri di accettazione** che il **BDD** trasforma in scenari Given–When–Then eseguibili. È il metodo con cui si sviluppa il progetto di corso.

## Argomenti mancanti / da ingerire

- Altri attributi di qualità: performance, security, functionality, usability, reusability, integrability, testability, deployability, energy efficiency, safety — TODO
- Antipattern architetturali — TODO
- Pattern per microservizi e stili architetturali (annunciati nelle conclusioni della Lez. 5 per le prossime lezioni) — TODO
- Soluzioni architetturali (interfacce, REST, formati, cloud) — TODO
- Documentazione delle architetture (*Views and Beyond*, ISO/IEC 42010) — TODO
- UP, Agile, Scrum, TDD, CI, SCM, DevOps — TODO
- Architetture di nuova generazione — TODO
- Stile di allocazione *work assignment*, viste di concorrenza — TODO (solo nominati nella Lez. 1)

## Fonti ingerite

8 — [[presentazione-corso]], [[introduzione-architettura-software]], [[attributi-di-qualita-e-importanza-architettura]], [[quality-attributes-availability]], [[quality-attributes-modifiability]], [[approcci-riuso-progettazione-architettura]], [[architectural-patterns-mvc-scc]], [[agile-project-management]]; programma ufficiale in [[Programma Syllabus]]

_Aggiornato: 2026-09-26 — ingest di 00_IntroduzioneAlCorso_SAD.pdf e delle due parti di 01-IntroductionOnSoftwareArchitecture_
_Aggiornato: 2026-09-30 — ingest di 02-Availability.pdf e 03-Modifiability.pdf; programma allineato a Programma Syllabus.md_
_Aggiornato: 2026-10-01 — ingest di 04-Architectural Patterns.pdf_
_Aggiornato: 2026-10-06 — ingest della parte nuova di 3-Architectural Patterns-complete.pdf_
_Aggiornato: 2026-10-10 — ingest di 04_Agile_01.pdf_
