# Log — Software Architecture Design

Formato entry: `## [YYYY-MM-DD] <operazione> | <dettaglio>`
Filtra ultimi 10: `grep "^## " wiki/log.md | tail -10`

---

## [2026-09-26] setup | Wiki sad inizializzato (struttura, config Obsidian da wiki-asi, 3 PDF copiati in raw/)

## [2026-09-26] ingest | Presentazione del corso (00_IntroduzioneAlCorso_SAD.pdf) | pagine coperte: 1-37
- fonte: [[presentazione-corso]]
- progetto: [[progetto-di-corso]] (metodi didattici, iterazioni, calendario, valutazione)
- overview: programma del corso in 7 blocchi con stato di copertura
- figure: 2 in raw/assets/lez00-intro-pN-*.png

## [2026-09-26] ingest | Software Architecture — An Introduction, parti 1 e 2 (01-IntroductionOnSoftwareArchitecture.pdf, 01-IntroductionOnSoftwareArchitecture-2 parte.pdf) | pagine coperte: 1-50, 1-45
- due PDF uniti in una lezione (Lezione 1) per nome e numerazione continua delle slide — da confermare
- fonti: [[introduzione-architettura-software]], [[attributi-di-qualita-e-importanza-architettura]] (con tabella pagina ↔ slide della parte 2)
- concetti creati (12): architettura-software, strutture-e-viste, strutture-di-modulo, strutture-componenti-e-connettori, strutture-di-allocazione, attributi-di-qualita, scenari-di-qualita, valutazione-attributi-di-qualita, tattiche-architetturali, pattern-architetturali, importanza-architettura-software, buone-pratiche-architetturali
- entità create (9): exam-booking-system, layered, client-server, microservices, uml, attribute-driven-design, autosar, enactest, software-architecture-in-practice
- esercizi creati (3): scenari-di-qualita-concreti, analisi-impatto-modifiche, applicazione-tattiche
- glossario: 54 termini inglese ↔ italiano
- figure: 34 in raw/assets (lez01-intro-pN-*, lez01b-qa-pN-*), tutte incorporate con didascalia; 7 diagrammi Mermaid ricostruiti (🧩)
- elaborazioni espanse: confronto definizioni 2003/2021, λ = 5000/60 ≈ 83.3 req/s contro DB a 30 tps (ρ ≈ 2.8, coda ≈ 3200 richieste, ≈ 107 s per smaltirla), analisi d'impatto passo per passo, requisiti di p.5 riscritti come scenari
- ❓ aperti: verso dell'interfaccia TestExecutor nel diagramma ENACTEST
- refusi segnalati: «Nowasdays» (p.34), «allocatedto» (p.44), «instanciates» (p.49), «Asyncronous» (parte 2 p.24)
- revisione di copertura totale: tutte le 132 pagine citate, tutte le 36 figure usate, nessun link rotto

## [2026-09-26] lint | link orfani e raggiungibilità da lezioni.md
- orfani trovati: CLAUDE.md, index, log → ora linkati da index e overview; 0 orfani, 0 link irrisolti su tutto il vault (PDF e immagini inclusi)
- CLAUDE.md: lezioni.md reso obbligatorio come hub (percorso di lettura con tutte le pagine della lezione); LINT controlla orfani (nessuno ammesso) e pagine non raggiungibili da lezioni.md
- verificato: tutte le pagine di concetti/, entità/, esercizi/, fonti/, progetto/ sono raggiungibili da lezioni.md

## [2026-09-26] riorganizzazione | lezioni.md
- un solo link per pagina in tutto il file; percorso aggregato in ordine di prima comparsa nelle slide, con tutte le pagine PDF coperte
- tolto l'elenco pagina-per-pagina con link ripetuti (la corrispondenza slide → pagina resta nelle pagine fonti/)
- Lezione 1: aggiunto ordine di lettura consigliato (senza link), con il motivo di ogni spostamento
- CLAUDE.md aggiornato con il nuovo formato e il controllo dei link ripetuti nel LINT

## [2026-09-27] setup | check-list avanzamento-studio.md
- creata dal programma ufficiale (00_IntroduzioneAlCorso_SAD.pdf pp. 15–17): 32 argomenti in 7 blocchi (A–G), caselle da fare / studiato / consolidato
- «da fare» spuntato per gli argomenti trattati in Lez. 0–1: A1, A2, B1, B2, B4, C1; B3 (classificazione a tre classi) e gli stili (solo cenni) lasciati da fare
- il file del programma indicato dall'utente non è stato trovato nel vault: usato il programma delle slide
- CLAUDE.md: regola della check-list, passo 14 dell'ingest, controllo nel LINT

## [2026-09-30] ingest | Quality Attributes of an Architecture — Availability (02-Availability.pdf) | pagine coperte: 1-23
- fonte: [[quality-attributes-availability]]
- concetti creati (2): availability, tattiche-availability; entità creata: circuit-breaker
- esercizi: calcolo-disponibilita (nuovo); casi aggiunti: scenari-di-qualita-concreti (caso 4), applicazione-tattiche (caso 5)
- aggiornate: attributi-di-qualita, tattiche-architetturali, exam-booking-system, progetto-di-corso (tabella dei gruppi di p.23, da confermare)
- derivazioni: formula MTBF/MTTR, tabella dei «nove» ricostruita (anno di 365 giorni), significato di RTO/RPO
- refusi/contraddizioni: 99,9 %/anno = 8 h 45 min 36 s (non 8 h 0 min 46 s); schema della server farm riusato accanto allo scenario dell'Exam Booking System (pp. 9, 20); «Tacticts» (p.13)
- figure: 13 in raw/assets/lez02-av-pN-*.png

## [2026-09-30] ingest | Quality Attributes of an Architecture — Modifiability (03-Modifiability.pdf) | pagine coperte: 1-33
- fonte: [[quality-attributes-modifiability]] (con tabella pagina ↔ slide: da p.22 slide = p.+1)
- concetti creati (3): modifiability, tattiche-modifiability, pattern-modifiability; entità create: plug-in, publish-subscribe; aggiornate: client-server (ora pattern, con benefici e trade-off), layered (layer pattern, layer bridging)
- esercizi: casi aggiunti a scenari-di-qualita-concreti (caso 5) e applicazione-tattiche (caso 6)
- annotazioni a mano riportate: p.10 (varianti di modificabilità, esempio SAP), p.17 (MVC e modificabilità dell'interfaccia)
- refusi: «Couple-Time Parameterization», «Ristrict Dependencies» (p.18)
- figure: 14 in raw/assets/lez03-mo-pN-*.png
- glossario: +27 termini (81 totali)
- lezioni.md: Lezioni 2 e 3 con percorso di lettura (un link per pagina) e ordine consigliato
- avanzamento-studio.md: riallineata al programma ufficiale raw/Programma Syllabus.md (nessuna spunta dell'utente da conservare); «da fare» spuntato per A1–A3, B1, B4, B7, B8, B12, C1, C2, E2, E3, E7, F0, F1, F3; plug-in tra gli argomenti aggiunti
- revisione di copertura totale: tutte le 56 pagine citate, tutte le 27 figure usate, 0 orfani, 0 link irrisolti, 0 duplicati in lezioni.md

## [2026-10-01] ingest | Reuse-based approaches for designing a Software Architecture — DSSA, Architectural Patterns and Styles (04-Architectural Patterns.pdf) | pagine coperte: 1-37
- fonte: [[approcci-riuso-progettazione-architettura]] (tabella pagina ↔ slide: mancano le slide 21, 29, 37, 39)
- concetti creati (4): progettazione-basata-sul-riuso, dssa, linee-di-prodotto-software, architetture-multi-tier; entità creata: state-logic-display
- aggiornate: pattern-architetturali (definizione della Lez. 4, esempi), attribute-driven-design, autosar (come DSSA), client-server (2-tier), layered (tier vs layer), microservices (riga «N services»)
- tabelle trascritte: attributi di qualità di 1-tier, 2-tier e 3-tier (pp. 29, 32, 34); esempi di linee di prodotto (p. 20, ultima riga tagliata nella slide)
- nessun esercizio nelle slide
- figure: 20 in raw/assets/lez04-ap-pN-*.png; ADD (p. 7) riusa la figura della Lez. 1
- glossario: +15 termini (96 totali)
- lezioni.md: Lezione 4 con percorso (un link per pagina) e ordine consigliato (multi-tier prima di State-Logic-Display)
- avanzamento-studio.md: «da fare» spuntato per D1 (State-Logic-Display) e Y3 (DSSA); aggiunto X2 (linee di prodotto); nessuna spunta dell'utente toccata
- aperti: gli stili architetturali annunciati nell'outline non sono nel PDF; MVC e Sense-Compute-Control solo elencati
- revisione di copertura totale: tutte le 37 pagine citate, tutte le 20 figure usate, 0 orfani, 0 link irrisolti, 0 duplicati in lezioni.md

## [2026-10-06] ingest | Architectural Patterns, versione completa — parte nuova: middleware, MVC, Spring MVC, Sense–Compute–Control (3-Architectural Patterns-complete.pdf) | pagine coperte: 35-36, 39-96
- confronto automatico con 04-Architectural Patterns.pdf: pp. 1–34 identiche, pp. 37–38 identiche (titoli tradotti), p. 36 = vecchia p. 35 + una nota nuova; ingerite solo le pagine nuove come Lezione 5
- fonte: [[architectural-patterns-mvc-scc]] (tabella «cosa è nuovo» e conversione pagina ↔ slide)
- entità create (3): mvc, spring-mvc, sense-compute-control; esercizi creati (2): implementare-mvc, applicare-sense-compute-control
- aggiornate: architetture-multi-tier (middleware nel three-tier), pattern-architetturali (confronto dei tre pattern, conclusioni), exam-booking-system, progetto-di-corso
- figure: 32 in raw/assets/lez05-ap-pN-*.png
- animazioni e grafici (🧩) in output/diagrammi/ con genera_animazioni_lez05.py: anim-mvc-classico.svg, anim-spring-mvc-richiesta.svg, anim-sense-compute-control.svg (SVG animati SMIL), grafico-lunar-lander-controllo.svg (simulazione del ciclo di controllo, verificata con la soluzione analitica della caduta libera)
- diagrammi Mermaid: relazioni MVC, sequenza MVC classico, tre vs quattro stadi, POST/redirect/GET dell'app spese
- glossario: +20 termini (116 totali)
- lezioni.md: Lezione 5 con percorso (un link per pagina) e ordine consigliato (teoria MVC e Spring prima degli esercizi)
- avanzamento-studio.md: «da fare» spuntato per D2 (Sense–Compute–Control) e D3 (MVC); aggiunto X3 (Spring); nessuna spunta dell'utente toccata
- CLAUDE.md: regola per i PDF aggiornati con lo stesso argomento
- revisione di copertura totale: tutte le 60 pagine nuove citate, tutte le 32 figure usate, 0 orfani, 0 link irrisolti, 0 duplicati in lezioni.md

## [2026-10-06] setup | repository git e regola di commit/push
- repository privato https://github.com/giob22/wiki-sad (primo commit b686f1e)
- CLAUDE.md: ogni modifica alla wiki si chiude con commit e push
