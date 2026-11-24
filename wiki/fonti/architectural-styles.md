---
tipo: fonte
titolo: "Architectural Styles"
file_raw: "05_Architectural_Styles_Complete.pdf"
pagine: "1-157"
data_ingest: 2026-11-24
formato: slide-pdf
riferimento_libro: "Taylor, Medvidovic, Dashofy — cap. 4"
argomenti: ["stili architetturali", "layered", "client-server", "data-flow", "shared memory", "interpreter", "implicit invocation", "publish-subscribe", "peer-to-peer", "cloud computing"]
---

# Architectural Styles (Lezione 8)

## Sommario

Le slide (157 pagine, dal capitolo 4 di Taylor, Medvidovic e Dashofy) definiscono lo [[stili-architetturali]] e ne percorrono le famiglie con una griglia costante (componenti e connettori, topologia, invarianti, benefici e limiti, varianti), usando il videogioco Lunar Lander come esempio ricorrente ([[05_Architectural_Styles_Complete.pdf#page=7]]). Dopo gli stili tradizionali e i layered/client–server seguono i data-flow, gli stili a memoria condivisa, interpreter e mobile code (con cenni di cloud computing), l'implicit invocation (publish–subscribe, event-based) e, in appendice, il peer-to-peer. Gli stili orientati ai servizi sono nominati a p. 7 e svolti nella Lezione 10.

## Punti chiave

1. Uno stile è una collezione denominata di decisioni architetturali che vincola e promuove qualità ([[05_Architectural_Styles_Complete.pdf#page=2]]).
2. Ogni stile ha vocabolario, regole di configurazione, semantica e analisi proprie ([[05_Architectural_Styles_Complete.pdf#page=4]]).
3. Main program e subroutine, e object-oriented: gli stili «di linguaggio» ([[05_Architectural_Styles_Complete.pdf#page=8]]–[[05_Architectural_Styles_Complete.pdf#page=15]]).
4. Layered: layer chiusi (manutenibilità, portabilità) vs aperti (efficienza); façade come interfaccia ([[05_Architectural_Styles_Complete.pdf#page=17]]–[[05_Architectural_Styles_Complete.pdf#page=29]]).
5. Client–server: ruoli, tre responsabilità logiche, 2/3/N tier ([[05_Architectural_Styles_Complete.pdf#page=30]]–[[05_Architectural_Styles_Complete.pdf#page=34]]).
6. Data-flow: batch sequential e pipe and filter ([[05_Architectural_Styles_Complete.pdf#page=35]]–[[05_Architectural_Styles_Complete.pdf#page=51]]).
7. Shared data: repository, blackboard, rule-based ([[05_Architectural_Styles_Complete.pdf#page=52]]–[[05_Architectural_Styles_Complete.pdf#page=71]]).
8. Interpreter e mobile code (code on demand, remote evaluation, mobile agent) ([[05_Architectural_Styles_Complete.pdf#page=72]]–[[05_Architectural_Styles_Complete.pdf#page=83]]).
9. Cloud computing: IaaS/PaaS/SaaS, modelli di deployment ([[05_Architectural_Styles_Complete.pdf#page=84]]–[[05_Architectural_Styles_Complete.pdf#page=88]]).
10. Disaccoppiamento (spazio, tempo, sincronizzazione), implicit invocation, publish–subscribe, event-based ([[05_Architectural_Styles_Complete.pdf#page=89]]–[[05_Architectural_Styles_Complete.pdf#page=118]]).
11. Appendice: peer-to-peer centralizzato, decentralizzato, ibrido ([[05_Architectural_Styles_Complete.pdf#page=119]]–[[05_Architectural_Styles_Complete.pdf#page=157]]).

## Concetti introdotti

[[stili-architetturali]] · [[disaccoppiamento-dei-componenti]] · [[cloud-computing]] · [[main-program-e-subroutine]] · [[object-oriented]] · [[layered]] · [[client-server]] · [[batch-sequential]] · [[pipe-and-filter]] · [[repository]] · [[blackboard]] · [[rule-based]] · [[interpreter]] · [[mobile-code]] · [[implicit-invocation]] · [[event-based]] · [[publish-subscribe]] · [[peer-to-peer]] · esercizio [[lunar-lander-in-ogni-stile]]

## Corrispondenza slide → pagine wiki

| Pagine PDF | Argomento | Pagina wiki |
|---|---|---|
| 2–7 | definizione, proprietà, benefici, elenco stili | [[stili-architetturali]] |
| 8–15 | main program, object-oriented | [[main-program-e-subroutine]], [[object-oriented]] |
| 16–29 | layered | [[layered]] |
| 30–34 | client–server | [[client-server]] |
| 35–39 | batch sequential | [[batch-sequential]] |
| 40–51 | pipe and filter | [[pipe-and-filter]] |
| 52–59 | shared data, repository | [[repository]] |
| 60–64 | blackboard | [[blackboard]] |
| 65–71 | rule-based | [[rule-based]] |
| 72–75 | interpreter | [[interpreter]] |
| 76–83 | mobile code | [[mobile-code]] |
| 84–88 | cloud computing | [[cloud-computing]] |
| 89–94 | disaccoppiamento, implicit invocation | [[disaccoppiamento-dei-componenti]], [[implicit-invocation]] |
| 95–106 | publish–subscribe | [[publish-subscribe]] |
| 107–118 | event-based | [[event-based]] |
| 119–157 | peer-to-peer | [[peer-to-peer]] |

## Domande aperte

- Le slide di p. 124 indicano la prima release di Gnutella nel 2003, mentre nello stesso elenco Gnutella è collocato nel 2000: la data è riportata come nella slide; da verificare con la docente.
- Le slide trattano SOA e microservizi solo come voce dell'elenco (p. 7): sono svolti nella Lezione 10.

## Domande da esame

- Definire uno stile architetturale e dire quali proprietà lo caratterizzano.
- Differenza tra layer chiusi e aperti, con un esempio e gli obiettivi di ciascuno.
- Pipe and filter: componenti, connettori, invarianti, attributi di qualità; confronto con batch sequential.
- Differenza tra repository, blackboard (passiva/attiva) e rule-based.
- Le tre varianti di mobile code.
- Le tre forme di disaccoppiamento e il loro costo.
- Pub–sub vs event-based vs implicit invocation.
- P2P centralizzato, decentralizzato e ibrido: pro e contro.

_Aggiornato: 2026-11-24 — ingest 05_Architectural_Styles_Complete.pdf_
