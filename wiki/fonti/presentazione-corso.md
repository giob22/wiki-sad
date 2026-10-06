---
tipo: fonte
titolo: "Software Architecture Design (SAD) — Course Presentation"
file_raw: "00_IntroduzioneAlCorso_SAD.pdf"
pagine: "1-37"
data_ingest: 2026-09-26
formato: slide-pdf
riferimento_libro: ""
argomenti: [ruolo dell'architettura, definizione 2003, stili e attributi di qualità, obiettivi formativi, programma, metodi didattici, progetto di corso, esame, calendario, testi]
---

# Presentazione del corso — 00_IntroduzioneAlCorso_SAD.pdf

## Sommario

Slide di presentazione del corso **Software Architecture Design**, LM in Computer Engineering, a.a. 2026/27, **prof. Anna Rita Fasolino** (DIETI-UNINA). Dopo un questionario anonimo d'ingresso, la docente motiva la disciplina: i processi devono consegnare più in fretta sistemi sempre più complessi e di qualità, e questo non è possibile senza curare l'architettura, che permette di ottenere gli **attributi di qualità** richiesti (stili diversi → qualità diverse: layered, web-application, microservizi) e di **organizzare lo sviluppo** iterativo e Agile. Seguono gli **obiettivi** (progettare, documentare, modellare e sviluppare architetture) e i **risultati attesi** secondo i descrittori di Dublino, il **programma** in cinque blocchi (fondamenti, qualità, progettazione con pattern/stili/tattiche, soluzioni architetturali come REST e Docker, processi iterativi e Agile con strumenti di SCM e CI/DevOps), i **metodi didattici** (lezioni, apprendimento per casi e a team), il **progetto software** comune a tutta la classe sviluppato con Scrum in sprint di 2 settimane, le **modalità d'esame** (progetto 50 % + orale 50 %), il **calendario** e i **testi**.

## Punti chiave

1. Docente, corso, a.a. ([[00_IntroduzioneAlCorso_SAD.pdf#page=1]]); sommario ([[00_IntroduzioneAlCorso_SAD.pdf#page=2]]); questionario anonimo d'ingresso, non valutato, per adattare le attività al background della classe ([[00_IntroduzioneAlCorso_SAD.pdf#page=3]]).
2. Perché conta l'architettura: cicli di rilascio più brevi, sistemi più complessi con alte aspettative di qualità ([[00_IntroduzioneAlCorso_SAD.pdf#page=4]], [[00_IntroduzioneAlCorso_SAD.pdf#page=5]]) → [[architettura-software]].
3. Definizione di Bass, Clements, Kazman (2003) ([[00_IntroduzioneAlCorso_SAD.pdf#page=6]]) → [[architettura-software]].
4. Architettura come soluzione: stili, pattern, modelli e tattiche danno qualità diverse — Layered → modularità, modificabilità, portabilità; Web-Application (architettura di riferimento Microsoft) → manutenibilità, scalabilità, sicurezza, prestazioni; Microservizi → agilità, evolvibilità, scalabilità, resilienza ([[00_IntroduzioneAlCorso_SAD.pdf#page=7]]–[[00_IntroduzioneAlCorso_SAD.pdf#page=10]]) → [[layered]], [[microservices]].
5. Un'architettura chiara e documentata sostiene i processi iterativi e Agile ([[00_IntroduzioneAlCorso_SAD.pdf#page=11]]).
6. Obiettivi: conoscenze e competenze per **progettazione**, **documentazione e modellazione**, **sviluppo** di architetture ([[00_IntroduzioneAlCorso_SAD.pdf#page=12]]).
7. Risultati attesi (descrittori di Dublino): conoscere il ruolo dell'architettura nei processi moderni; modelli, stili, pattern e strumenti metodologici; relazione tra progetto architetturale e qualità e implicazioni delle scelte ([[00_IntroduzioneAlCorso_SAD.pdf#page=13]]); saper progettare, documentare e implementare architetture che soddisfino requisiti funzionali e di qualità con processi iterativi, evolutivi e Agile ([[00_IntroduzioneAlCorso_SAD.pdf#page=14]]).
8. Programma — fondamenti e qualità ([[00_IntroduzioneAlCorso_SAD.pdf#page=15]]), progettazione, pattern, stili, soluzioni ([[00_IntroduzioneAlCorso_SAD.pdf#page=16]]), processi iterativi, Agile, SCM, CI, DevOps ([[00_IntroduzioneAlCorso_SAD.pdf#page=17]]) — dettaglio in [[overview]].
9. Metodi didattici: *lecture-based*, *case-based*, *team-based learning* ([[00_IntroduzioneAlCorso_SAD.pdf#page=18]]–[[00_IntroduzioneAlCorso_SAD.pdf#page=22]]) → [[progetto-di-corso]].
10. Progetto comune della classe, sottosistemi a team, dominio con partner esterno, Agile ([[00_IntroduzioneAlCorso_SAD.pdf#page=23]]); tre iterazioni ([[00_IntroduzioneAlCorso_SAD.pdf#page=24]]); tecnologie e stili suggeriti ([[00_IntroduzioneAlCorso_SAD.pdf#page=25]]); sprint di 2 settimane, tutor come Scrum Master ([[00_IntroduzioneAlCorso_SAD.pdf#page=26]]); calendario ([[00_IntroduzioneAlCorso_SAD.pdf#page=27]]) → [[progetto-di-corso]].
11. Valutazione: progetto su GitHub consegnato con pull request una settimana prima; presentazione e discussione all'esame ([[00_IntroduzioneAlCorso_SAD.pdf#page=28]]); progetto 50 % (max 15) + orale 50 % (max 15) ([[00_IntroduzioneAlCorso_SAD.pdf#page=29]]).
12. 6 CFU, 48 ore (30 teoria + 14 pratica + 4 seminari); martedì e giovedì 12:30–14:30, Via Claudio; dal 14 settembre al 18 dicembre 2026, pausa 11–13 novembre ([[00_IntroduzioneAlCorso_SAD.pdf#page=30]]); corso in presenza, Microsoft Team del corso ([[00_IntroduzioneAlCorso_SAD.pdf#page=31]]); seminari specialistici di esperti industriali ([[00_IntroduzioneAlCorso_SAD.pdf#page=32]]); ricevimento su Teams il mercoledì 15–17 ([[00_IntroduzioneAlCorso_SAD.pdf#page=33]]).
13. Testi ([[00_IntroduzioneAlCorso_SAD.pdf#page=34]], [[00_IntroduzioneAlCorso_SAD.pdf#page=35]]) → [[software-architecture-in-practice]]; contatti ([[00_IntroduzioneAlCorso_SAD.pdf#page=36]]); domande ([[00_IntroduzioneAlCorso_SAD.pdf#page=37]]).

## Concetti introdotti

- [[architettura-software]]
- [[attributi-di-qualita]] (nominati)
- [[layered]], [[microservices]] (come esempi)
- [[progetto-di-corso]]

## Domande aperte

- La classificazione degli attributi in «osservabili a runtime, non osservabili a runtime, intrinseci» ([[00_IntroduzioneAlCorso_SAD.pdf#page=15]]) è diversa da quella in due categorie della lezione 1 ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=6]]): verrà chiarita?
- Il dominio del progetto e il partner esterno saranno comunicati all'assegnazione (entro metà ottobre, [[00_IntroduzioneAlCorso_SAD.pdf#page=27]]).

## Domande da esame

- Perché l'architettura software è importante nei processi di sviluppo moderni?
- Che rapporto c'è tra stile architetturale e attributi di qualità? Fai un esempio.
- (Orale) Spiega l'architettura complessiva del progetto e giustifica le scelte di progetto del tuo team ([[00_IntroduzioneAlCorso_SAD.pdf#page=29]]).

_Aggiornato: 2026-09-26 — ingest_
