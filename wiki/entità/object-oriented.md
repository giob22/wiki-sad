---
tipo: entità
categoria: stile
famiglia: "tradizionali e influenzati dal linguaggio"
---

# Stile object-oriented

## Contesto e problema

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=11]], [[05_Architectural_Styles_Complete.pdf#page=12]]

Si vogliono strutture dati complesse e entità del mondo reale modellate come oggetti, proteggendo l'integrità dei dati con l'incapsulamento.

## Soluzione

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=11]]

- **Componenti:** oggetti, che incapsulano dati e operazioni associate.
- **Connettori:** messaggi e invocazioni di metodo; nelle applicazioni distribuite si può usare un middleware come Java RMI.
- **Topologia:** varia; spesso fa largo uso di **gerarchie di ereditarietà**.
- **Invariante:** ogni oggetto è responsabile dell'integrità della propria rappresentazione interna; gli altri oggetti non possono accedervi direttamente.

## Diagramma

![[lez08-stili-p14-oo-lunar-lander-uml.png]]
*Lunar Lander a oggetti in UML ([[05_Architectural_Styles_Complete.pdf#page=14]]): la classe GUI (`getBurnRate()`, `displayStatus(...)`) crea 1..* oggetti Spacecraft (attributi a, f, t, v; operazioni set/get) e usa l'unica Environment Simulation (`calculateStatus(br, s)`).*

![[lez08-stili-p15-oo-vs-call-return.png]]
*Confronto con la versione call–return ([[05_Architectural_Styles_Complete.pdf#page=15]]): a sinistra (OO) un solo oggetto GUI gestisce tutto l'input e l'output e legge/scrive Spacecraft con operazioni *get*/*set* (a, f, t, v); a destra (call–return) le responsabilità di I/O sono distribuite su più moduli.*

![[lez08-stili-p13-oo-lunar-lander.png]]
*Lunar Lander a oggetti ([[05_Architectural_Styles_Complete.pdf#page=13]]): il modulo «GUI – Get/Display Info» chiama tre procedure: `"GET" a, f, t, v` e `"SET" a, f, t, v` verso SpaceCraft, e `"CALCULATE"` (ingresso: br, SpaceCraft; uscita: SpaceCraft) verso Environment Simulation.*

Descrizione dell'esempio ([[05_Architectural_Styles_Complete.pdf#page=13]]): la GUI legge il burn rate e recupera i parametri con *get*, li mostra e li passa alla simulazione; la simulazione calcola il nuovo stato, memorizzato con *set*.

## Attributi di qualità

| Attributo | Effetto | Perché | Fonte |
|---|---|---|---|
| Integrità dei dati | + | l'incapsulamento: i metodi controllano l'accesso allo stato interno | [[05_Architectural_Styles_Complete.pdf#page=12]] |
| Modellabilità del dominio | + | adatto a strutture complesse e a entità reali come oggetti | [[05_Architectural_Styles_Complete.pdf#page=12]] |
| Modificabilità (identità) | − | gli oggetti collaboranti devono conoscere l'identità di chi fornisce i servizi | [[05_Architectural_Styles_Complete.pdf#page=12]] |
| Comprensibilità | − | relazioni statiche e dinamiche complesse | [[05_Architectural_Styles_Complete.pdf#page=12]] |
| Prestazioni | − | molti oggetti interagenti → overhead | [[05_Architectural_Styles_Complete.pdf#page=12]] |

## Quando usarlo / quando no

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=12]]

Utile con strutture dati complesse e domini ricchi di entità. Con molti oggetti servono «ulteriori criteri di strutturazione» (stili e pattern di livello più alto) per gestire la complessità.

## Varianti ed esempi

- Java RMI come connettore distribuito ([[05_Architectural_Styles_Complete.pdf#page=11]]).

## Connessioni

- [[main-program-e-subroutine]]: confronto diretto sullo stesso esempio.
- [[layered]]: criterio di strutturazione aggiuntivo tipico.
- [[lunar-lander-in-ogni-stile]]

## Fonti

- [[architectural-styles]]

_Aggiornato: 2026-11-24 — ingest 05_Architectural_Styles_Complete.pdf_
