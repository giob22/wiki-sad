---
tipo: concetto
importanza_esame: alta
prerequisiti: ["tattiche-modifiability", "pattern-architetturali"]
fonti_pdf: ["03-Modifiability.pdf#page=26", "03-Modifiability.pdf#page=27"]
termine_inglese: "patterns for modifiability"
---

# Pattern per la modifiability

## Definizione

> 📄 Fonte: [[03-Modifiability.pdf#page=27]]

I pattern per la modificabilità **dividono il sistema in moduli** in modo che i moduli possano essere **sviluppati ed evoluti separatamente**, con **poca interazione** tra loro, sostenendo così **portabilità, modificabilità e riuso**.

La lezione ne presenta quattro:

| Pattern | Idea | Tattiche che incorpora (🧩) | Beneficio principale | Trade-off | Pagina |
|---|---|---|---|---|---|
| **Client-Server** | un server offre servizi a molti client distribuiti; scoperta + interazione | encapsulation (il client vede solo il protocollo), discovery | basso accoppiamento server–client, nessun accoppiamento tra client, evoluzione indipendente | prestazioni (rete), sicurezza e integrità sulla rete | [[client-server]] |
| **Plug-in** | un nucleo di funzionalità + varianti che si aggiungono tramite un insieme fisso di interfacce | abstract common service, defer binding (build time o dopo) | estendere il prodotto in modo controllato; plug-in di produttori diversi, evoluzione indipendente dal nucleo | vulnerabilità di sicurezza e minacce alla privacy | [[plug-in]] |
| **Layers** | strati con interfaccia pubblica e ordine stretto di uso | restrict dependencies, encapsulation | modificare gli strati inferiori senza toccare quelli superiori | penalità di prestazioni; il *layer bridging* compromette portabilità e modificabilità | [[layered]] |
| **Publish-Subscribe** | componenti che comunicano con messaggi asincroni tramite un bus di eventi | use an intermediary | publisher e subscriber indipendenti; aggiungere subscriber non cambia il publisher | latenza, ordine di invocazione non deterministico, testabilità | [[publish-subscribe]] |

Fonti per riga: client-server [[03-Modifiability.pdf#page=28]]–[[03-Modifiability.pdf#page=29]]; plug-in [[03-Modifiability.pdf#page=30]]; layers [[03-Modifiability.pdf#page=31]]; publish-subscribe [[03-Modifiability.pdf#page=32]]–[[03-Modifiability.pdf#page=33]].

## Spiegazione

> 🧩 Elaborazione mia: la Lez. 1 ha definito il pattern come insieme di tattiche ([[pattern-architetturali]], con l'esempio Layers). Qui la stessa idea è applicata a un solo attributo: ogni pattern realizza una o più tattiche di [[tattiche-modifiability]] e paga un prezzo su un altro attributo (quasi sempre le prestazioni). Tre dei quattro pattern — client-server, layers, publish-subscribe — sono anche **stili** del programma ([[Programma Syllabus]]: stile a livelli con client-server; invocazione implicita con publish-subscribe).

## Esempi espansi

Ogni pattern è spiegato nella sua pagina, con figure e tabella degli attributi di qualità. Esempio collegato all'Exam Booking System: il publish-subscribe è l'**event bus** con l'evento `ReservationConfirmed` di [[03-Modifiability.pdf#page=21]] (tattica *use an intermediary*, [[tattiche-modifiability]]).

## Perché importa

Tra i pattern citati, **client-server** e **publish-subscribe** sono proposti per il progetto di corso (web app client-server, microservizi, [[progetto-di-corso]]), e il programma prevede i pattern per microservizi ([[Programma Syllabus]]).

> 🎯 Esame: per ciascuno dei quattro pattern — elementi, come favorisce la modificabilità, trade-off.

## Connessioni

- [[tattiche-modifiability]]: le tattiche che i pattern incorporano.
- [[pattern-architetturali]]: definizione generale di pattern.
- [[modifiability]]: l'attributo favorito.

## Fonti

- [[quality-attributes-modifiability]] — [[03-Modifiability.pdf#page=26]]–[[03-Modifiability.pdf#page=33]]

_Aggiornato: 2026-09-30 — ingest 03-Modifiability.pdf_
