---
tipo: fonte
titolo: "Designing a Software Architecture (ASR e ADD)"
file_raw: "06-ADD-Designing a Software Architecture.pdf"
pagine: "1-41"
data_ingest: 2026-11-24
formato: slide-pdf
riferimento_libro: "Bass, Clements, Kazman — capp. 19–20"
argomenti: ["ASR", "Quality Attribute Workshop", "utility tree", "Attribute-Driven Design", "design concept", "interfacce", "rationale"]
---

# Designing a Software Architecture (Lezione 9)

## Sommario

Le slide (41 pagine) coprono due capitoli del testo base: i **requisiti architetturalmente significativi** (cap. 19: come trovarli con interviste e Quality Attribute Workshop, come prioritizzarli con l'utility tree) e il **metodo ADD** (cap. 20), con i sette passi dalla revisione degli ingressi all'analisi del progetto ([[06-ADD-Designing a Software Architecture.pdf#page=2]], [[06-ADD-Designing a Software Architecture.pdf#page=13]]). La numerazione stampata sulle slide coincide con la pagina del PDF fino a p. 24, poi la numerazione stampata è +1: nel wiki si usa sempre l'indice del PDF.

## Punti chiave

1. Un ASR ha effetto profondo sull'architettura; spesso è un requisito di qualità ([[06-ADD-Designing a Software Architecture.pdf#page=3]]).
2. Gli ASR si ricavano dai requisiti o dagli stakeholder (QAW); senza stakeholder si costruisce un utility tree con coppie (valore, rischio) H/M/L ([[06-ADD-Designing a Software Architecture.pdf#page=4]]–[[06-ADD-Designing a Software Architecture.pdf#page=8]]).
3. ADD procede per round e iterazioni; ogni iterazione ha un obiettivo e segue sette passi ([[06-ADD-Designing a Software Architecture.pdf#page=9]]–[[06-ADD-Designing a Software Architecture.pdf#page=13]]).
4. Gli ingressi (driver) formano un backlog di progettazione ([[06-ADD-Designing a Software Architecture.pdf#page=14]]–[[06-ADD-Designing a Software Architecture.pdf#page=17]]).
5. I design concept (tattiche, pattern, architetture di riferimento, componenti esterni) si scelgono con tabelle pro/contro, eventualmente prototipi ([[06-ADD-Designing a Software Architecture.pdf#page=20]]–[[06-ADD-Designing a Software Architecture.pdf#page=24]]).
6. Istanziare i concept produce strutture (modulo, C&C, allocazione) e interfacce esterne e interne ([[06-ADD-Designing a Software Architecture.pdf#page=25]]–[[06-ADD-Designing a Software Architecture.pdf#page=29]]).
7. Schizzi, decisioni e rationale si registrano; l'avanzamento si traccia con kanban ([[06-ADD-Designing a Software Architecture.pdf#page=30]]–[[06-ADD-Designing a Software Architecture.pdf#page=38]]).
8. Il passo 7 chiude l'iterazione con analisi e revisione dell'obiettivo ([[06-ADD-Designing a Software Architecture.pdf#page=39]]–[[06-ADD-Designing a Software Architecture.pdf#page=41]]).

## Concetti introdotti

[[requisiti-architetturalmente-significativi]] · [[attribute-driven-design]] · [[scenari-di-qualita]] (esempi) · [[strutture-e-viste]] (le tre categorie di strutture)

## Corrispondenza slide → pagine wiki

| Pagine PDF | Argomento | Pagina wiki |
|---|---|---|
| 2–8 | ASR, QAW, utility tree, esempio ospedaliero | [[requisiti-architetturalmente-significativi]] |
| 9–41 | metodo ADD, sette passi, riepilogo | [[attribute-driven-design]] |

## Domande aperte

- Le slide non spiegano come si calcola o si combina il punteggio H/M/L dell'utility tree per ordinare gli scenari; la regola di priorità è un'inferenza (marcata 🧩 nel concetto).

## Domande da esame

- Che cos'è un ASR e come si individua? Che cos'è un utility tree?
- Elencare i sette passi di ADD e dire che cosa produce ciascuno.
- Quali sono i design concept? Come si sceglie tra alternative? Quando conviene un prototipo?
- Che differenza c'è tra interfacce esterne e interne? Perché si registra la rationale?

_Aggiornato: 2026-11-24 — ingest 06-ADD-Designing a Software Architecture.pdf_
