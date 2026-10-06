---
tipo: fonte
titolo: "Reuse-based approaches for designing a Software Architecture — DSSA, Architectural Patterns and Styles"
file_raw: "04-Architectural Patterns.pdf"
pagine: "1-37"
data_ingest: 2026-10-01
formato: slide-pdf
riferimento_libro: "Taylor, Medvidovic, Dashofy — Software Architecture: Foundations, Theory and Practice, cap. 4"
argomenti: [strategie e metodi di progettazione, riuso dell'esperienza, Attribute-Driven Design, alternative di progetto, ambito di applicabilità, DSSA, architetture di riferimento, AUTOSAR, IoT, cloud NIST, linee di prodotto software, comunanza e variabilità, pattern architetturali, State-Logic-Display, multi-tier, tier vs layer, 1-tier, 2-tier fat client, 3-tier thin client, middleware, 4-tier deployment, load-balanced cluster]
---

# Approcci basati sul riuso per progettare un'architettura — 04-Architectural Patterns.pdf

## Numerazione pagine ↔ slide

| Pagine PDF | Slide | Regola |
|---|---|---|
| 1–20 | 1–20 | slide = p. |
| 21–27 | 22–28 | slide = p. + 1 |
| 28–34 | 30–36 | slide = p. + 2 |
| 35 | 38 | slide = p. + 3 |
| 36–37 | 40–41 | slide = p. + 4 |

Mancano le slide 21, 29, 37 e 39. Le slide 36–37 del PDF (pp. 36–37) hanno il titolo in italiano.

## Sommario

Lezione sul **cap. 4 di Taylor, Medvidovic, Dashofy**: come si progetta un'architettura riusando l'esperienza. Distingue le **strategie** di progettazione (divide-and-conquer, top-down/bottom-up, information hiding, pattern, iterativo e incrementale) dai **metodi** (notazione + processo + linee guida: strutturato, OO, a componenti, a servizi, a modelli), elenca i libri sui metodi e ripropone l'**Attribute-Driven Design**. Le **alternative** di progetto sono tre: partire da zero (soluzioni nuove ma costoso e rischioso), applicare uno stile/pattern generico (riuso ma adattamento), applicare una soluzione specifica del dominio, la **DSSA** (riuso maggiore, se esiste). Una figura colloca design pattern, stili, pattern architetturali e DSSA secondo conoscenza del dominio e ambito. Le **DSSA** (architetture di riferimento) sono insiemi di componenti specializzati, generalizzati e composti in una topologia standard: esempi Microsoft per il web, piattaforma TV, AUTOSAR, IoT, cloud NIST, con un elenco di riferimenti per dominio. Le **linee di prodotto software** riusano sistematicamente ciò che è comune e gestiscono la variabilità pianificata, con esempi in dieci domini. La seconda parte definisce il **pattern architetturale** e lo distingue dalla DSSA, elenca State-Logic-Display, MVC e Sense-Compute-Control, e sviluppa il **three-tiered pattern** nella famiglia **multi-tier**: tier ≠ layer, evoluzione da 1 tier a N servizi, tabelle di benefici e limiti per 1-tier (mainframe), 2-tier (fat client) e 3-tier (thin client), il **middleware** come abilitatore di integrazione e due pattern di deployment della Microsoft Application Architecture Guide (4-tier, load-balanced cluster).

## Punti chiave

1. Titolo e libro di riferimento ([[04-Architectural Patterns.pdf#page=1]]); outline ([[04-Architectural Patterns.pdf#page=2]]); «come si progetta un'architettura?» ([[04-Architectural Patterns.pdf#page=3]]).
2. Strategie vs metodi di progettazione ([[04-Architectural Patterns.pdf#page=4]]); libri sui metodi ([[04-Architectural Patterns.pdf#page=5]]); riuso dell'esperienza ([[04-Architectural Patterns.pdf#page=6]]); ADD ([[04-Architectural Patterns.pdf#page=7]]).
3. Tre alternative di progetto ([[04-Architectural Patterns.pdf#page=8]]); ambito di applicabilità di DSSA, pattern, stili, design pattern ([[04-Architectural Patterns.pdf#page=9]]).
4. DSSA: definizione e tre proprietà dei componenti ([[04-Architectural Patterns.pdf#page=10]]); esempi web Microsoft e TV ([[04-Architectural Patterns.pdf#page=11]], [[04-Architectural Patterns.pdf#page=12]]); vantaggi e limiti ([[04-Architectural Patterns.pdf#page=13]]); otto architetture di riferimento per dominio ([[04-Architectural Patterns.pdf#page=14]]); AUTOSAR, IoT, cloud ([[04-Architectural Patterns.pdf#page=15]]–[[04-Architectural Patterns.pdf#page=17]]).
5. Linee di prodotto: definizione e idea di fondo ([[04-Architectural Patterns.pdf#page=18]]); comunanza vs variabilità ([[04-Architectural Patterns.pdf#page=19]]); esempi in dieci domini ([[04-Architectural Patterns.pdf#page=20]]).
6. Pattern architetturali: sezione ([[04-Architectural Patterns.pdf#page=21]]); definizione e confronto con DSSA ([[04-Architectural Patterns.pdf#page=22]]); tre esempi ([[04-Architectural Patterns.pdf#page=23]]).
7. State-Logic-Display come multi-tier; tier ≠ layer ([[04-Architectural Patterns.pdf#page=24]]); figura e applicazioni ([[04-Architectural Patterns.pdf#page=25]]); two/three/n-tier ([[04-Architectural Patterns.pdf#page=26]]); evoluzione dei tier ([[04-Architectural Patterns.pdf#page=27]]).
8. 1-tier e sua tabella degli attributi ([[04-Architectural Patterns.pdf#page=28]], [[04-Architectural Patterns.pdf#page=29]]); 2-tier fat client e tabella ([[04-Architectural Patterns.pdf#page=30]]–[[04-Architectural Patterns.pdf#page=32]]); 3-tier thin client e tabella ([[04-Architectural Patterns.pdf#page=33]], [[04-Architectural Patterns.pdf#page=34]]).
9. Middleware come abilitatore di integrazione ([[04-Architectural Patterns.pdf#page=35]]); 4-tier deployment per web ([[04-Architectural Patterns.pdf#page=36]]); load-balanced cluster per le prestazioni ([[04-Architectural Patterns.pdf#page=37]]).

## Concetti introdotti

- [[progettazione-basata-sul-riuso]]
- [[dssa]]
- [[linee-di-prodotto-software]]
- [[architetture-multi-tier]]
- Entità: [[state-logic-display]]; aggiornate [[autosar]], [[client-server]], [[layered]], [[microservices]], [[attribute-driven-design]], [[pattern-architetturali]]

## Domande aperte

- L'outline ([[04-Architectural Patterns.pdf#page=2]]) e il titolo annunciano gli **Architectural Styles**, che però non sono nel PDF: arriveranno in una lezione successiva?
- MVC e Sense-Compute-Control sono solo elencati ([[04-Architectural Patterns.pdf#page=23]]).
- La tabella di [[04-Architectural Patterns.pdf#page=20]] è tagliata all'ultima riga (ERP).
- Nel load-balanced cluster ([[04-Architectural Patterns.pdf#page=37]]) load balancer e database sono in copia singola: la slide non discute la loro ridondanza (vedi [[availability]]).

## Domande da esame

- Che differenza c'è tra strategia e metodo di progettazione? Esempi.
- Quali alternative si hanno nel progettare un'architettura? Pro e contro.
- Cos'è una DSSA? Che proprietà hanno i suoi componenti? Esempi, vantaggi e limiti.
- Differenza tra DSSA, pattern architetturale, stile e design pattern.
- Cos'è una linea di prodotto software? Comunanza e variabilità.
- Cos'è un pattern architetturale? Descrivi State-Logic-Display.
- Differenza tra tier e layer.
- Confronta 1-tier, 2-tier e 3-tier rispetto agli attributi di qualità. Fat vs thin client.
- Ruolo e trade-off del middleware.

_Aggiornato: 2026-10-01 — ingest_
