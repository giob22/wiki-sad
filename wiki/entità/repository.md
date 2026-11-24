---
tipo: entità
categoria: stile
famiglia: "shared memory"
---

# Repository (shared data)

## Contesto e problema

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=53]]

Più agenti devono cooperare sugli stessi dati, ma devono poter essere **aggiunti o rimossi a runtime senza conoscersi**. La soluzione: comunicare attraverso un **repository di dati centralizzato**.

## Soluzione

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=53]], [[05_Architectural_Styles_Complete.pdf#page=55]], [[05_Architectural_Styles_Complete.pdf#page=58]]

- **Componenti:** un repository globale di dati e agenti indipendenti che lo usano. Gli agenti sono indipendenti tra loro; l'archivio è indipendente dagli agenti.
- **Connettori:** chiamate di procedura, accesso diretto alla memoria o operazioni su database (tipicamente **CRUD**: Create, Read, Update, Delete).
- **Topologia:** **stella** centrata sul repository.
- Il repository **gestisce persistenza, vincoli di integrità e accesso concorrente**; gli agenti lo interrogano tramite interfacce di accesso definite. Il **modello dati comune** è una dipendenza architetturale importante.
- Somiglia alle variabili globali, ma offre una distinta organizzazione architetturale ([[05_Architectural_Styles_Complete.pdf#page=53]]).
- Famiglia: le varianti sono *repository*, [[blackboard]] e [[rule-based]] ([[05_Architectural_Styles_Complete.pdf#page=56]]).

## Diagramma

![[lez08-stili-p54-shared-data.png]]
*Architettura shared-data ([[05_Architectural_Styles_Complete.pdf#page=54]]): al centro «Shared Data»; attorno gli agenti (ovali) che vi accedono in lettura e scrittura («Memory Access») ed eseguono «Computation». Forma a stella.*

![[lez08-stili-p57-repository-componenti.png]]
*Diagramma dei componenti ([[05_Architectural_Styles_Complete.pdf#page=57]]): il componente Repository contiene un Request Validator (eseguibile), che usa («use») un Database, ed espone un'interfaccia («instantiate») con un'operazione; il componente Agent la richiede.*

## Attributi di qualità

| Attributo | Effetto | Perché | Fonte |
|---|---|---|---|
| Integrazione dei dati | + | i dati condivisi supportano l'integrazione tra le funzioni applicative | [[05_Architectural_Styles_Complete.pdf#page=59]] |
| Gestibilità centrale (integrità, accessi, backup) | + | vincoli, controllo accessi e backup gestiti in un posto | [[05_Architectural_Styles_Complete.pdf#page=59]] |
| Riuso dei dati | + | nuovi componenti usano i dati esistenti | [[05_Architectural_Styles_Complete.pdf#page=59]] |
| Modificabilità | − | un cambio di schema può richiedere cambi in più componenti | [[05_Architectural_Styles_Complete.pdf#page=59]] |
| Prestazioni | − | accesso concorrente e contesa creano colli di bottiglia | [[05_Architectural_Styles_Complete.pdf#page=59]] |
| Availability | − | un guasto del repository colpisce molte funzioni (single point of failure) | [[05_Architectural_Styles_Complete.pdf#page=59]] |

## Quando usarlo / quando no

🧩 Conviene quando l'integrazione sui dati è l'obiettivo principale e lo schema è stabile; è rischioso quando lo schema cambia spesso o quando disponibilità e prestazioni sono critiche.

## Varianti ed esempi

- [[blackboard]] (controllo guidato dai dati) e [[rule-based]] (base di conoscenza con regole).

## Connessioni

- [[blackboard]], [[rule-based]]: specializzazioni.
- [[availability]], [[modifiability]]: gli attributi penalizzati.

## Fonti

- [[architectural-styles]]

_Aggiornato: 2026-11-24 — ingest 05_Architectural_Styles_Complete.pdf_
