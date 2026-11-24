---
tipo: fonte
titolo: "Service-Oriented and Microservice Architectures (parte 1)"
file_raw: "07— Service-Oriented and Microservice Architectures-1 part.pdf"
pagine: "1-47"
data_ingest: 2026-11-24
formato: slide-pdf
riferimento_libro: "Richardson — Microservices Patterns (esempio FTGO)"
argomenti: ["SOA", "servizi", "contratti", "API HTTP", "REST", "SOAP", "OpenAPI", "broker", "API gateway", "ESB", "orchestrazione", "coreografia"]
---

# Service-Oriented and Microservice Architectures — parte 1 (Lezione 10)

## Sommario

La prima parte del materiale su servizi e microservizi (47 pagine, prof.ssa Fasolino) ricostruisce la prospettiva storica (dal client–server ai microservizi), definisce servizio, contratto e SOA, tratta la comunicazione (comandi, query, eventi; sincrona e asincrona; API HTTP, REST, SOAP/WSDL, OpenAPI; evoluzione del contratto), gli intermediari (broker, discovery, API gateway, ESB) e il coordinamento (orchestrazione e coreografia), sempre con l'esempio ricorrente **Food To Go (FTGO)** e con la richiesta di motivare le scelte con scenari, tattiche e trade-off ([[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=7]]). Il titolo dice «1 part»: la parte sui microservizi in senso stretto non è ancora tra le fonti.

## Punti chiave

1. Servizio = componente autonomo con contratto esplicito; accoppiamento debole, astrazione, autonomia, riuso ([[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=9]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=12]]).
2. La SOA non richiede una tecnologia specifica; SOAP, REST, ESB sono scelte di implementazione; SOA e microservizi non si distinguono per la tecnologia ma per confini e deployment ([[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=13]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=17]]).
3. Comandi, query, eventi; sincrono vs asincrono, con i rischi di timeout, duplicati e ordinamento ([[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=18]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=21]]).
4. API HTTP, REST (vincoli), SOAP/WSDL, OpenAPI, evoluzione compatibile/incompatibile e contract test ([[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=22]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=33]]).
5. Intermediari: broker (forwarding, handle), discovery, API gateway, ESB, con i loro costi ([[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=34]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=42]]).
6. Orchestrazione vs coreografia: visibilità, recupero dei guasti, accoppiamento ([[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=43]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=47]]).

## Concetti introdotti

[[servizi-e-soa]] · [[contratti-e-api-di-servizio]] · [[comunicazione-sincrona-e-asincrona]] · [[intermediari-di-servizio]] · [[orchestrazione-e-coreografia]] · [[microservices]] (aggiornato)

## Corrispondenza slide → pagine wiki

| Pagine PDF | Argomento | Pagina wiki |
|---|---|---|
| 2–17 | prospettiva storica, servizio, SOA, FTGO, wrapper legacy, scenario di interoperabilità | [[servizi-e-soa]] |
| 18–19, 22–33 | comandi/query/eventi, API HTTP, REST, SOAP/WSDL, OpenAPI, evoluzione | [[contratti-e-api-di-servizio]] |
| 20–21 | comunicazione sincrona e asincrona | [[comunicazione-sincrona-e-asincrona]] |
| 34–42 | broker, discovery, API gateway, ESB | [[intermediari-di-servizio]] |
| 43–47 | orchestrazione e coreografia | [[orchestrazione-e-coreografia]] |

## Domande aperte

- Il materiale non tratta ancora le proprietà del microservizio (database per servizio, saga, deployment): da integrare quando arriverà la parte 2.
- L'esempio OpenAPI usa la versione 3.1.0; i campi `info` e `paths` sono riportati come nella slide.

## Domande da esame

- Che cos'è un servizio e che cosa contiene un contratto di servizio?
- SOA vs microservizi: che cosa li distingue davvero?
- Sincrono vs asincrono: rischi e contratti; perché un timeout non basta?
- Quali sono i vincoli di REST? Quando un'API è RESTful?
- Cambiamenti compatibili e incompatibili di un'API; ruolo dei contract test.
- API gateway vs ESB; broker forwarding vs handle; service discovery.
- Orchestrazione vs coreografia nel caso del rifiuto del ristorante in FTGO.

_Aggiornato: 2026-11-24 — ingest 07— Service-Oriented and Microservice Architectures-1 part.pdf_
