---
tipo: concetto
importanza_esame: alta
prerequisiti: ["pattern-architetturali", "attributi-di-qualita"]
fonti_pdf: ["05_Architectural_Styles_Complete.pdf#page=2"]
termine_inglese: "architectural style"
---

# Stili architetturali

## Definizione

> 🔑 Definizione chiave — 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=2]] (da Taylor, Medvidovic e Dashofy, cap. 4)

Uno **stile architetturale** (*architectural style*) è una **collezione denominata di decisioni di progetto architetturale** che (1) si applicano in un particolare contesto di sviluppo, (2) **vincolano** le decisioni architetturali prese per i singoli sistemi di quel contesto, (3) **promuovono qualità desiderabili** nei sistemi risultanti. Gli stili sono **meno specifici del dominio applicativo** dei pattern architetturali e possono servire a vari livelli, «dalle subroutine alla struttura complessiva dell'applicazione».

## Spiegazione

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=2]], [[05_Architectural_Styles_Complete.pdf#page=4]], [[05_Architectural_Styles_Complete.pdf#page=5]], [[05_Architectural_Styles_Complete.pdf#page=6]]

Uno stile è un **modo di restringere lo spazio di progetto**: dice quali tipi di elementi si possono usare, come possono essere collegati e che cosa significa la loro composizione. Proprio perché restringe, offre qualità prevedibili.

**Proprietà di base** (p. 4):

| Proprietà | Che cosa fissa | Esempio |
|---|---|---|
| Vocabolario di elementi di progetto | tipi di componente, connettore ed elemento dati | pipe, filtri, oggetti, server |
| Regole di configurazione | vincoli topologici | ogni componente connesso ad al massimo due altri |
| Interpretazione semantica | il significato di una composizione | un filtro trasforma un flusso in un altro flusso |
| Analisi specifiche dello stile | che cosa si può verificare sui sistemi costruiti con quelle regole | throughput e deadlock in pipe and filter |

**Benefici** (p. 5): riuso del progetto, riuso del codice (si riusano le parti invarianti dello stile), comprensione strutturale (basta il nome — «client–server» — per capire la forma), interoperabilità (convenzioni condivise), analisi specifiche e visualizzazioni specifiche dello stile.

**Dimensioni per analizzare uno stile** (p. 6): vocabolario di componenti e connettori; configurazioni ammesse; modello computazionale sottostante; invarianti; esempi d'uso; benefici e limiti; specializzazioni/varianti. Le pagine entità di questo wiki seguono proprio questa griglia.

> 🧩 Elaborazione mia: le sette domande di p. 6 sono lo schema con cui si «legge» ogni stile all'orale: componenti/connettori → topologia/vincoli → modello computazionale → invarianti → usi → pro/contro → varianti.

## Esempi espansi

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=2]], [[05_Architectural_Styles_Complete.pdf#page=7]]

![[lez08-stili-p3-ambito-degli-stili.png]]
*Mappa di [[05_Architectural_Styles_Complete.pdf#page=3]]: asse «Scope» (livello di programmazione, struttura applicativa con componenti e connettori, struttura di sistema) e asse «Application Domain Knowledge» (da superficiale a profonda); dal basso: design pattern di programma, stili, pattern architetturali, architetture software specifiche di dominio.*

**La mappa di p. 3** colloca gli stili tra i *design pattern di programma* (scope di linguaggio, conoscenza di dominio superficiale) e le *architetture software specifiche di dominio* (scope di sistema, conoscenza profonda). Gli stili stanno a metà: riguardano la struttura applicativa (componenti e connettori) con poca conoscenza del dominio, e i **pattern architetturali** ([[pattern-architetturali]]) li seguono con un po' più di conoscenza di dominio.

**La classificazione di p. 7** raggruppa gli stili in famiglie, ognuna con una pagina nel wiki:

| Famiglia | Stili | Pagine |
|---|---|---|
| Tradizionali / influenzati dal linguaggio | main program e subroutine; object-oriented | [[main-program-e-subroutine]], [[object-oriented]] |
| Layered | layered (virtual machine); client–server | [[layered]], [[client-server]] |
| Data flow | batch sequential; pipe and filter | [[batch-sequential]], [[pipe-and-filter]] |
| Shared memory | repository, blackboard, rule-based | [[repository]], [[blackboard]], [[rule-based]] |
| Interpreter | interpreter; mobile code | [[interpreter]], [[mobile-code]] |
| Implicit invocation | event-based; publish–subscribe; peer-to-peer | [[implicit-invocation]], [[event-based]], [[publish-subscribe]], [[peer-to-peer]] |
| Orientati ai servizi | service-oriented; microservices | [[microservices]] |

Lo stesso gioco, Lunar Lander, viene ridisegnato in quasi ogni stile: vedi [[lunar-lander-in-ogni-stile]].

## Perché importa

> 🎯 Esame: la docente chiede di saper descrivere uno stile con componenti, connettori, topologia, vincoli e attributi di qualità favoriti/penalizzati, e di giustificare la scelta dello stile per un progetto ([[00_IntroduzioneAlCorso_SAD.pdf#page=28]]).

Lo stile è la **prima grande decisione di struttura**: guida quali attributi di qualità si ottengono ([[attributi-di-qualita]]) e quali tattiche ([[tattiche-architetturali]]) si possono applicare. Un pattern architetturale come [[state-logic-display]] o [[mvc]] può essere visto come uno stile più legato al dominio.

## Connessioni

- [[pattern-architetturali]]: pattern e stili differiscono per quanta conoscenza del dominio incorporano.
- [[attributi-di-qualita]]: ogni stile favorisce alcuni attributi e ne penalizza altri.
- [[progettazione-basata-sul-riuso]]: gli stili sono una forma di riuso dell'esperienza.
- [[lunar-lander-in-ogni-stile]]: confronto pratico.

## Fonti

- [[architectural-styles]]; [[05_Architectural_Styles_Complete.pdf#page=2]]–[[05_Architectural_Styles_Complete.pdf#page=7]]

_Aggiornato: 2026-11-24 — ingest 05_Architectural_Styles_Complete.pdf_
