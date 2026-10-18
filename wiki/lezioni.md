# Lezioni — Software Architecture Design

Percorso di studio lezione per lezione. **Ogni pagina del wiki è linkata una sola volta** in tutto il file, nel punto in cui il suo argomento compare per la prima volta nelle slide: quando la apri, leggila tutta. Accanto a ogni pagina ci sono **tutte** le pagine del PDF che copre (anche quelle che compaiono più avanti).

Regola: 1 PDF = 1 lezione, salvo diversa indicazione. Glossario dei termini inglesi → [[glossario]] · catalogo completo → [[index]] · stato dello studio → [[avanzamento-studio]]

---

## Lezione 0 — Presentazione del corso
**PDF:** [[00_IntroduzioneAlCorso_SAD.pdf]] (pp. 1–37)

### Percorso di lettura (ordine delle slide)

1. [[presentazione-corso]] — pp. 1–37: sommario di tutta la presentazione (docente, obiettivi, risultati attesi, metodi, orario, seminari, ricevimento, contatti).
2. *Perché conta l'architettura, stili e qualità* (pp. 4–11) — si legge nella Lezione 1: pagine «architettura software», «layered», «microservices».
3. [[overview]] — pp. 12, 15–17, 30: obiettivi formativi, **programma** del corso e stato di copertura, dati del corso.
4. [[progetto-di-corso]] — pp. 18–29: metodi didattici, progetto di classe, iterazioni, Scrum, tecnologie, calendario, **valutazione d'esame**.
5. [[guida-progetto-picus]] — **progetto d'esame PICUS**, dai documenti in `wiki/progetto/riferimenti/`: presentazione PICUS pp. 1–29, richieste informali del committente pp. 1–7, AGENTS.md del team §1–10. Cosa fare, calendario delle iterazioni, dominio e desiderata, attività e deliverable dell'iterazione preparatoria, decisioni del team, come lavorare in 8 ruotando i ruoli Scrum.
6. [[a2-stakeholder-e-contesto]] — **attività 1 del progetto** (presentazione PICUS p. 18, richieste §2–3): analisi degli stakeholder, confini del sistema, flussi, Context Diagram, ipotesi e domande aperte.
7. [[burndown-github-project]] — **strumento per il progetto**: burndown dello sprint sul GitHub Project pesato con le taglie dei task (richiama il burndown chart della Lezione 6, pagina «cerimonie e artefatti Agile»).
8. [[software-architecture-in-practice]] — pp. 34–35: testi del corso (è anche il libro della Lezione 1).

Ordine consigliato: quello delle slide.

---

## Lezione 1 — Software Architecture: an Introduction (cap. 1 di Bass, Clements, Kazman)
**PDF:** [[01-IntroductionOnSoftwareArchitecture.pdf]] (pp. 1–50 = slide 1–50) + [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf]] (pp. 1–45 = slide 51–97)
**Riepiloghi della lezione:** [[introduzione-architettura-software]] (parte 1) · [[attributi-di-qualita-e-importanza-architettura]] (parte 2, con la tabella pagina ↔ slide)

> ⚠️ Due PDF uniti in una lezione per nome e numerazione continua delle slide: da confermare. Sotto, «p.» = pagina del PDF; «P1» = prima parte, «P2» = seconda parte.

### Percorso di lettura (ordine delle slide)

**Parte 1 — Cos'è un'architettura software**

1. [[architettura-software]] — P1 pp. 1–4, 7 (e Lez. 0 pp. 4–11): definizioni, punti fermi, ruolo nel processo di sviluppo.
2. [[microservices]] — P1 pp. 3, 35; P2 p. 21 (e Lez. 0 pp. 7, 10): cenni allo stile a microservizi.
3. [[strutture-e-viste]] — P1 pp. 5–6, 13, 33, 36, 47: struttura architetturale, tre categorie, relazioni tra strutture, quali scegliere.
4. [[strutture-di-modulo]] — P1 pp. 8–11, 14–23; P2 p. 18: moduli, ragionamento di modificabilità, decomposizione, uses, layer, class, data model.
5. [[uml]] — P1 pp. 10, 19, 22, 39–40, 44, 46; P2 p. 42: notazione usata nelle figure.
6. [[exam-booking-system]] — P1 p. 12 (esempio guida usato in tutta la lezione): mappa di dove compare.
7. [[layered]] — P1 p. 21; P2 p. 22 (e Lez. 0 pp. 7–8): stile a strati.
8. [[strutture-componenti-e-connettori]] — P1 pp. 24–35: componenti, connettori, vista runtime, domande per attributo.
9. [[client-server]] — P1 pp. 34, 36: stile client-server.
10. [[strutture-di-allocazione]] — P1 pp. 37–46: deployment, install view, work assignment.
11. [[pattern-architetturali]] — P1 p. 47; P2 pp. 21–22 (e Lez. 0 p. 16): definizione, pattern come insieme di tattiche.
12. [[buone-pratiche-architetturali]] — P1 pp. 48, 50: raccomandazioni di processo, regole pratiche.
13. [[attribute-driven-design]] — P1 p. 49: driver → concetti di progetto → strutture.

**Parte 2 — Attributi di qualità e importanza dell'architettura**

14. [[attributi-di-qualita]] — P2 pp. 1–7, 32–33: definizione, requisiti funzionali e di qualità, categorie, trade-off, tre domande.
15. [[scenari-di-qualita-concreti]] *(esercizio)* — P2 pp. 5, 14, 16: scenari di prestazioni e modificabilità, requisiti riscritti come scenari.
16. [[scenari-di-qualita]] — P2 pp. 8–13: sei parti, Given–When–Then, scenario generale e concreto.
17. [[valutazione-attributi-di-qualita]] — P2 pp. 15, 17–19, 34: valutare prestazioni e modificabilità.
18. [[analisi-impatto-modifiche]] *(esercizio)* — P2 pp. 17–18: i sei passi sull'Exam Booking System.
19. [[tattiche-architetturali]] — P2 pp. 20–30: tattiche di prestazioni, disponibilità, sicurezza, modificabilità.
20. [[applicazione-tattiche]] *(esercizio)* — P2 pp. 23–30: tattica → dove → effetto → trade-off.
21. [[importanza-architettura-software]] — P2 pp. 31–45: le undici motivazioni §3.1–3.11.
22. [[enactest]] — P2 p. 42: architettura a componenti di un progetto (§3.9).
23. [[autosar]] — P2 p. 43: sistema aperto a standard (§3.9).

### Ordine di lettura consigliato

L'ordine delle slide ha alcuni salti: esempi usati prima di essere presentati, esercizi prima della teoria, e pagine della parte 1 (pattern, stili, ADD) che si capiscono solo con la teoria della parte 2. Ordine che suggerisco (numeri del percorso sopra):

| # | Pagina | Perché in questa posizione |
|---|---|---|
| 1 | architettura software | punto di partenza |
| 3 | strutture e viste | inquadra le tre categorie di strutture |
| 6 | Exam Booking System | le pagine sulle strutture usano l'esempio fin dall'inizio: meglio conoscerlo prima |
| 4 | strutture di modulo | |
| 8 | strutture componenti e connettori | |
| 10 | strutture di allocazione | |
| 5 | UML | riepilogo della notazione dopo aver visto tutte e tre le viste |
| 14 | attributi di qualità | |
| 16 | scenari di qualità | la teoria prima dell'esercizio (nelle slide l'esempio di p. 5 precede la definizione di p. 8) |
| 15 | scenari di qualità concreti *(esercizio)* | |
| 17 | valutazione degli attributi di qualità | |
| 18 | analisi d'impatto *(esercizio)* | |
| 19 | tattiche architetturali | |
| 20 | applicazione delle tattiche *(esercizio)* | |
| 11 | pattern architetturali | la definizione completa (pattern = insieme di tattiche) è in P2 pp. 21–22 |
| 7 | layered | la pagina usa tattiche e trade-off della parte 2 |
| 9 | client-server | stile descritto con componenti e connettori |
| 2 | microservices | le parti principali (P1 p. 35) richiedono la vista C&C |
| 13 | Attribute-Driven Design | riassume driver, tattiche, pattern e strutture: ha senso dopo averli visti tutti |
| 12 | buone pratiche architetturali | chiusura sul processo |
| 21 | importanza dell'architettura | |
| 22 | ENACTEST | esempio del §3.9 |
| 23 | AUTOSAR | esempio del §3.9 |

I due riepiloghi della lezione (in testa) vanno letti per ultimi, come ripasso: contengono punti chiave, refusi e domande da esame.

_Aggiornato: 2026-09-26 — percorso riorganizzato: un link per pagina, ordine delle slide + ordine consigliato_

---

## Lezione 2 — Quality Attributes of an Architecture: Availability (capp. 4–13 di Bass, Clements, Kazman)
**PDF:** [[02-Availability.pdf]] (pp. 1–23, slide = pagina)
**Riepilogo della lezione:** [[quality-attributes-availability]]

### Percorso di lettura (ordine delle slide)

1. [[availability]] — pp. 3–12, 20–22: definizione, failure/fault/error e catena causale, faultlessness/fault tolerance/recoverability, MTBF/MTTR, SLA, tabella dei «nove» (con il refuso della riga 99,9 %), scenario generale e scenari concreti, dallo scenario alle decisioni (RTO/RPO).
2. [[calcolo-disponibilita]] *(esercizio)* — pp. 6–7, 9: formula MTBF/MTTR, downtime, ricostruzione della tabella dei «nove».
3. *Scenario di disponibilità dell'Exam Booking System* (p. 9) — già linkato nella Lezione 1: rileggi il **caso 4** della pagina «scenari di qualità concreti».
4. [[tattiche-availability]] — pp. 13–19, 23: albero delle tattiche, detect / recover / prevent, pattern di ridondanza hot/warm/cold, tabella tattiche → tecnologie degli otto gruppi.
5. [[circuit-breaker]] — pp. 19, 23: pattern circuit breaker e Resilience4j.
6. *Dallo scenario alle decisioni* (p. 21) — già linkato nella Lezione 1: rileggi il **caso 5** della pagina «applicazione delle tattiche».
7. *Tabella dei gruppi* (p. 23) — pagina «progetto di corso» (linkata nella Lezione 0), sezione «Esperimenti di disponibilità per gruppo».

### Ordine di lettura consigliato

La slide di p. 21 (dallo scenario alle decisioni) usa tattiche spiegate solo alle pp. 13–19, ma sta nella pagina «availability», che nell'ordine delle slide si legge prima delle tattiche.

| # | Pagina | Perché in questa posizione |
|---|---|---|
| 1 | availability — fino alla sezione «Scenari di disponibilità» | definizioni, misure e scenari |
| 2 | calcolo della disponibilità *(esercizio)* | subito dopo la formula e la tabella dei «nove» |
| 3 | scenari di qualità concreti, caso 4 | lo scenario appena visto, svolto in tabella |
| 4 | tattiche per l'availability | |
| 5 | circuit breaker | pattern citato tra le tattiche |
| 1 | availability — sezione «Dallo scenario alle decisioni architetturali» | ora le tattiche sono note |
| 6 | applicazione delle tattiche, caso 5 | le decisioni di p. 21 lette come tattiche |
| 7 | progetto di corso, tabella dei gruppi | collegamento con il progetto |

Il riepilogo della lezione va letto per ultimo, come ripasso.

---

## Lezione 3 — Quality Attributes of an Architecture: Modifiability (capp. 4–13 di Bass, Clements, Kazman)
**PDF:** [[03-Modifiability.pdf]] (pp. 1–33 = slide 1–34; la tabella di conversione è nel riepilogo)
**Riepilogo della lezione:** [[quality-attributes-modifiability]]

### Percorso di lettura (ordine delle slide)

1. [[modifiability]] — pp. 3–17: definizione, quattro domande, quando e chi modifica, costo e debito tecnico, varianti (scalabilità, variabilità, portabilità, indipendenza dalla posizione), scenario generale e concreto (con le annotazioni a mano di pp. 10 e 17).
2. *Scenario concreto sull'interfaccia utente* (p. 17) — già linkato nella Lezione 1: rileggi il **caso 5** della pagina «scenari di qualità concreti».
3. [[tattiche-modifiability]] — pp. 18–25: increase cohesion, reduce coupling (encapsulation, intermediary, abstract common service, restrict dependencies), defer binding per momento di binding.
4. *Scelta del momento di binding* (pp. 6, 25) — già linkato nella Lezione 1: rileggi il **caso 6** della pagina «applicazione delle tattiche».
5. [[pattern-modifiability]] — pp. 26–33: tabella comparativa dei quattro pattern.
6. *Client-server* (pp. 28–29) — pagina «client-server», già linkata nella Lezione 1 e aggiornata: rileggila tutta.
7. [[plug-in]] — p. 30: nucleo + plug-in, microkernel.
8. *Layers* (p. 31, e p. 22 per restrict dependencies) — pagina «layered», già linkata nella Lezione 1 e aggiornata: rileggi le sezioni «Come pattern per la modificabilità» e «Attributi di qualità».
9. [[publish-subscribe]] — pp. 32–33 (e l'event bus di p. 21): publisher, subscriber, event bus, invocazione implicita.

### Ordine di lettura consigliato

La pagina «pattern per la modifiability» è una tabella di confronto dei quattro pattern: si capisce meglio dopo aver letto le pagine dei singoli pattern.

| # | Pagina | Perché in questa posizione |
|---|---|---|
| 1 | modifiability | |
| 2 | scenari di qualità concreti, caso 5 | subito dopo lo scenario di p. 17 |
| 3 | tattiche per la modifiability | |
| 4 | applicazione delle tattiche, caso 6 | subito dopo gli esempi di binding |
| 6 | client-server | primo dei quattro pattern |
| 7 | plug-in | |
| 8 | layered | |
| 9 | publish-subscribe | |
| 5 | pattern per la modifiability | confronto finale, dopo i singoli pattern |

Il riepilogo della lezione va letto per ultimo, come ripasso.

_Aggiornato: 2026-09-30 — aggiunte Lezione 2 (Availability) e Lezione 3 (Modifiability)_

---

## Lezione 4 — Reuse-based approaches for designing a Software Architecture: DSSA, Architectural Patterns and Styles (cap. 4 di Taylor, Medvidovic, Dashofy)
**PDF:** [[04-Architectural Patterns.pdf]] (pp. 1–37 = slide 1–41; tabella di conversione nel riepilogo)
**Riepilogo della lezione:** [[approcci-riuso-progettazione-architettura]]

### Percorso di lettura (ordine delle slide)

1. [[progettazione-basata-sul-riuso]] — pp. 1–9, 22: come si progetta un'architettura, strategie vs metodi, libri sui metodi, riuso dell'esperienza, tre alternative di progetto, ambito di applicabilità di DSSA/pattern/stili/design pattern, pattern vs DSSA.
2. *Attribute-Driven Design* (p. 7) — si legge nella Lezione 1; la pagina «attribute-driven-design» ha un paragrafo nuovo sulla Lez. 4.
3. [[dssa]] — pp. 10–17: definizione di DSSA/architettura di riferimento, esempi (web Microsoft, TV, AUTOSAR, IoT, cloud NIST), vantaggi e limiti, elenco per dominio.
4. *AUTOSAR come architettura di riferimento* (pp. 13–15) — pagina «autosar», già linkata nella Lezione 1: rileggi la sezione «Come architettura di riferimento (Lez. 4)».
5. [[linee-di-prodotto-software]] — pp. 18–20: definizione, comunanza vs variabilità, esempi in dieci domini.
6. *Definizione di pattern architetturale della Lez. 4* (pp. 22–23) — pagina «pattern architetturali», già linkata nella Lezione 1: rileggi la sezione «La definizione della Lez. 4».
7. [[state-logic-display]] — pp. 23–25 (e la tabella di p. 34): il pattern three-tier display/logic/state.
8. [[architetture-multi-tier]] — pp. 24, 26–37: tier vs layer, evoluzione dei tier, 1-tier, 2-tier, 3-tier con tabelle degli attributi, middleware, pattern di deployment 4-tier e load-balanced cluster.
9. *Aggiornamenti alle pagine di stile* — «layered» (sezione «Layer non è tier»), «client-server» (sezione «Come architettura 2-tier»), «microservices» (riga «N services»): già linkate nella Lezione 1.

### Ordine di lettura consigliato

Nelle slide il pattern State-Logic-Display (pp. 23–25) viene prima della spiegazione delle architetture multi-tier (pp. 26–37), ma la sua pagina si appoggia a quella sui multi-tier (definizione di tier, tabella del three-tier).

| # | Pagina | Perché in questa posizione |
|---|---|---|
| 1 | progettazione basata sul riuso | quadro generale della lezione |
| 2 | attribute-driven design (paragrafo Lez. 4) | metodo citato nel quadro |
| 3 | DSSA | |
| 4 | AUTOSAR (sezione Lez. 4) | esempio di DSSA |
| 5 | linee di prodotto software | |
| 6 | pattern architetturali (sezione Lez. 4) | definizione generale di pattern |
| 8 | architetture multi-tier | tier, layer e le tre architetture con le loro tabelle |
| 7 | State-Logic-Display | il pattern three-tier, ora con il contesto completo |
| 9 | layered, client-server, microservices (sezioni nuove) | collegamenti con gli stili già visti |

Il riepilogo della lezione va letto per ultimo, come ripasso.

_Aggiornato: 2026-10-01 — aggiunta Lezione 4 (Architectural Patterns)_

---

## Lezione 5 — Architectural Patterns (versione completa): middleware, MVC, Spring MVC, Sense–Compute–Control (cap. 4 di Taylor, Medvidovic, Dashofy)
**PDF:** [[3-Architectural Patterns-complete.pdf]] — parte nuova: pp. 35–36 e 39–96 (= slide 38–39 e 43–101). Le pp. 1–34 e 37–38 sono identiche al PDF della Lezione 4 e si leggono lì.
**Riepilogo della lezione:** [[architectural-patterns-mvc-scc]] (con la tabella di cosa è nuovo e la conversione pagina ↔ slide)

### Percorso di lettura (ordine delle slide)

1. *Middleware nel three-tier* (pp. 35–36) — pagina «architetture multi-tier», già linkata nella Lezione 4: rileggi la sezione «Middleware nell'architettura three-tier (Lez. 5)».
2. [[mvc]] — pp. 39–58: origini e motivazione, Model/View/Controller, relazioni strutturali, i quattro modelli di interazione (con animazione), Observer e Strategy, confronto delle varianti, Front Controller.
3. [[implementare-mvc]] *(esercizio)* — pp. 51–52, 65–67, 72–82: View con e senza Strategy, ShowExamSessions in Spring MVC, applicazione per le spese.
4. [[spring-mvc]] — pp. 58–71: Spring Framework e IoC, Spring MVC, DispatcherServlet, flusso della richiesta (con animazione), Spring Boot, gerarchia dei contesti.
5. [[sense-compute-control]] — pp. 83–91, 95: domini, tre fasi, ciclo di controllo (con animazione), antintrusione, varianti a tre e quattro stadi, controllo accessi, IoT, attributi di qualità, ADS.
6. [[applicare-sense-compute-control]] *(esercizio)* — pp. 86, 89, 92–95: antintrusione, controllo accessi, Lunar Lander con simulazione e grafico, ADS.
7. *Conclusioni* (p. 96) — pagina «pattern architetturali», già linkata nella Lezione 1: rileggi la sezione «La definizione della Lez. 4», che ora contiene il confronto dei tre pattern.

### Ordine di lettura consigliato

Nelle slide l'esercizio Strategy (pp. 51–52) e il codice Spring (pp. 65–66) arrivano dentro la teoria, e l'esempio completo delle spese (pp. 72–82) usa Spring MVC: conviene leggere la teoria di MVC e di Spring prima degli esercizi.

| #   | Pagina                                             | Perché in questa posizione                       |
| --- | -------------------------------------------------- | ------------------------------------------------ |
| 1   | architetture multi-tier (sezione middleware)       | completa la lezione precedente                   |
| 2   | MVC                                                | teoria del pattern                               |
| 4   | Spring MVC                                         | il framework che realizza il web MVC lato server |
| 3   | implementare MVC *(esercizio)*                     | i tre casi usano sia MVC sia Spring MVC          |
| 5   | Sense–Compute–Control                              |                                                  |
| 6   | applicare Sense–Compute–Control *(esercizio)*      |                                                  |
| 7   | pattern architetturali (confronto dei tre pattern) | chiusura della lezione                           |

Il riepilogo della lezione va letto per ultimo, come ripasso.

_Aggiornato: 2026-10-06 — aggiunta Lezione 5 (parte nuova di 3-Architectural Patterns-complete.pdf)_

---

## Lezione 6 — Agile Project Management
**PDF:** [[04_Agile_01.pdf]] (pp. 1–60, slide = pagina). Il file si chiama «04_…» ma è la sesta lezione ingerita.
**Riepilogo della lezione:** [[agile-project-management]]

### Percorso di lettura (ordine delle slide)

1. [[sviluppo-agile]] — pp. 3–21: i problemi dei progetti, definizione di Agile, quattro valori e dodici principi del Manifesto, come funziona (con animazione del ciclo), sviluppo iterativo ed evolutivo vs waterfall, ruoli e tre responsabilità.
2. [[cerimonie-e-artefatti-agile]] — pp. 22–31: le quattro cerimonie con le tabelle, gli artefatti, la lavagna product/sprint backlog con la DoD, il burndown chart (con grafico commentato).
3. [[user-stories]] — pp. 32–50: definizione e tre aspetti, template, chi le scrive, dimensione, epic e task, INVEST, revisione e stima, criteri di accettazione vs Definition of Done.
4. [[valutare-user-stories-invest]] *(esercizio)* — pp. 41–48: cassiere, PayPal, gestione utenti, revisione dei Post-it.
5. [[criteri-di-accettazione-e-bdd]] — pp. 50–55, 60: criteri di accettazione con esempi (e l'errore di p. 54), BDD, Three Amigos, Gherkin.
6. [[da-criteri-di-accettazione-a-bdd]] *(esercizio)* — pp. 52, 56–60: recupero password in sei scenari Gherkin, scenari per il login.

Ordine consigliato: quello delle slide.

_Aggiornato: 2026-10-10 — aggiunta Lezione 6 (04_Agile_01.pdf)_

