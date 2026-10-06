---
tipo: fonte
titolo: "Software Architecture — An Introduction (parte 2): Understanding Quality Attributes; Why is Software Architecture important?"
file_raw: "01-IntroductionOnSoftwareArchitecture-2 parte.pdf"
pagine: "1-45"
data_ingest: 2026-09-26
formato: slide-pdf
riferimento_libro: "Bass, Clements, Kazman — Software Architecture in Practice, cap. 1"
argomenti: [attributi di qualità, requisiti funzionali e di qualità, trade-off, scenari di qualità, scenario generale e concreto, valutazione delle prestazioni, analisi d'impatto, tattiche, pattern, Layers, tattiche di prestazioni/disponibilità/sicurezza/modificabilità, motivazioni dell'architettura, linee di prodotto, sistemi aperti, AUTOSAR, ENACTEST]
---

# Attributi di qualità e importanza dell'architettura (parte 2) — 01-IntroductionOnSoftwareArchitecture-2 parte.pdf

## Numerazione pagine ↔ slide

Il PDF riparte da pagina 1, ma la numerazione stampata prosegue la parte 1 con due salti (manca la slide 54 e la slide 87). Alcune slide a sfondo azzurro non riportano il numero: il valore tra parentesi è ricavato dalla regola.

| Pagine PDF | Slide | Regola |
|---|---|---|
| 1–3 | 51–53 | slide = p. + 50 |
| 4–35 | 55–86 | slide = p. + 51 (pp. 14, 16, 18 senza numero stampato: 65, 67, 69) |
| 36–45 | 88–97 | slide = p. + 52 |

## Sommario

Seconda parte della lezione sul capitolo 1 di *Software Architecture in Practice*: sezioni 2 e 3. Un **attributo di qualità** è una proprietà misurabile o verificabile che indica quanto bene il sistema soddisfa gli stakeholder oltre la funzione di base; la funzionalità non determina l'architettura, che si scompone in base alle qualità volute, e requisiti funzionali e di qualità vanno specificati insieme, per responsabilità (esempio: la verifica di ammissibilità con requisiti di prestazioni, disponibilità, sicurezza, modificabilità, testabilità). Gli attributi sono di runtime o di sviluppo e sono in **trade-off**. Tre domande guidano la sezione: come **esprimere** le qualità (**scenari di qualità** in sei parti, Given–When–Then, generali e concreti, con gli scenari di prestazioni e modificabilità dell'Exam Booking System e i metodi di **valutazione**: prestazioni sulle viste C&C, analisi d'impatto e esercizio di modifica per la modificabilità), come **ottenerle** (**tattiche** e **pattern**, con il pattern Layers come insieme di tattiche e le tattiche di prestazioni, disponibilità, sicurezza e modificabilità applicate all'esempio guida). La sezione 3 elenca undici **motivazioni** dell'architettura: abilita/inibisce e permette di prevedere le qualità, comunicazione tra stakeholder, decisioni precoci, vincoli sull'implementazione, influenza sull'organizzazione, sviluppo incrementale, riuso e linee di prodotto, integrazione di elementi indipendenti (ENACTEST, sistemi aperti e AUTOSAR), vocabolario ristretto a soluzioni collaudate, base per la formazione.

## Punti chiave

1. Definizione di QA; i sistemi si riprogettano per le qualità, non per la funzionalità ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=2]]).
2. La funzionalità non determina l'architettura ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=3]]); requisiti funzionali e di qualità insieme, per responsabilità ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=4]]); esempio della verifica di ammissibilità ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=5]]).
3. Due categorie (runtime, sviluppo); trade-off portabilità/prestazioni ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=6]]); tre domande ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=7]]).
4. Scenari: QA osservabili tramite scenari, sei parti ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=8]]); Given–When–Then ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=9]]); definizione delle parti ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=10]]–[[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=12]]); scenario generale di availability ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=13]]).
5. Scenario concreto di prestazioni: 5.000 richieste/min, 95 % entro 2 s, tutte entro 5 s ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=14]]).
6. Valutazione delle prestazioni: cosa, come, su quali viste; il DB a 30 transazioni/s ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=15]]).
7. Scenario concreto di modificabilità: nuova regola in due giorni lavorativi, modifiche limitate ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=16]]); analisi d'impatto sulle viste di modulo ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=17]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=18]]); valutazione empirica ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=19]]).
8. Tattica e pattern: definizioni; i pattern comprendono più tattiche ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=20]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=21]]); il pattern Layers ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=22]]).
9. Tattiche di prestazioni: replicazione, cache, asincronia, con effetti e trade-off ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=23]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=24]]).
10. Tattiche di disponibilità e configurazioni prima/dopo il guasto ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=25]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=26]]).
11. Tattiche di sicurezza: autenticazione, autorizzazione (RBAC), TLS, log ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=27]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=28]]).
12. Tattiche di modificabilità: localize changes, hide information, use an intermediary, defer binding ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=29]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=30]]).
13. Motivazioni dell'architettura §3.1–3.11 ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=31]]–[[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=45]]), con ENACTEST ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=42]]) e AUTOSAR ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=43]]).

Pagine di sola intestazione: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=1]] (sezione 2), [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=20]] (come ottenere le qualità), [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=31]] (sezione 3).

## Concetti introdotti

- [[attributi-di-qualita]]
- [[scenari-di-qualita]]
- [[valutazione-attributi-di-qualita]]
- [[tattiche-architetturali]]
- [[pattern-architetturali]]
- [[importanza-architettura-software]]
- Entità: [[autosar]], [[enactest]], [[layered]]
- Esercizi: [[scenari-di-qualita-concreti]], [[analisi-impatto-modifiche]], [[applicazione-tattiche]]

## Domande aperte

- La slide [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=15]] cita le **viste di concorrenza**, non ancora definite.
- *Schedule Resources* è citata come tattica di prestazioni ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=21]]) ma non spiegata.
- L'elenco delle tattiche di disponibilità termina con «…» ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=25]]): il catalogo completo arriverà con il blocco sulle tattiche del programma.
- Verso dell'interfaccia *TestExecutor* nel diagramma ENACTEST (→ [[enactest]]).
- Refuso: «Asyncronous» per «Asynchronous» ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=24]]).

## Domande da esame

- Cos'è un attributo di qualità? Perché la funzionalità non determina l'architettura?
- Quali sono le sei parti di uno scenario di qualità? Differenza tra scenario generale e concreto. Scrivi uno scenario concreto.
- Come si valutano prestazioni e modificabilità a livello architetturale?
- Cos'è una tattica? Cos'è un pattern? In che relazione sono? Fai l'esempio del pattern Layers.
- Descrivi le tattiche di prestazioni (disponibilità, sicurezza, modificabilità) applicate all'Exam Booking System, con effetti e trade-off.
- Perché l'architettura software è importante? Discuti almeno tre motivazioni.
- Cos'è una linea di prodotto? Cos'è un sistema aperto?

_Aggiornato: 2026-09-26 — ingest_
