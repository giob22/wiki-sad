---
tipo: concetto
importanza_esame: alta
prerequisiti: ["architettura-software", "strutture-e-viste", "pattern-architetturali"]
fonti_pdf: ["3-Architectural Patterns-complete.pdf#page=3", "3-Architectural Patterns-complete.pdf#page=4", "3-Architectural Patterns-complete.pdf#page=5", "3-Architectural Patterns-complete.pdf#page=6", "3-Architectural Patterns-complete.pdf#page=7", "3-Architectural Patterns-complete.pdf#page=8", "3-Architectural Patterns-complete.pdf#page=9", "3-Architectural Patterns-complete.pdf#page=22"]
termine_inglese: "reuse-based architecture design"
---

# Progettazione architetturale basata sul riuso

## Definizione

> 📄 Fonte: [[3-Architectural Patterns-complete.pdf#page=1]], [[3-Architectural Patterns-complete.pdf#page=3]], [[3-Architectural Patterns-complete.pdf#page=6]]

La lezione segue il **cap. 4 di Taylor, Medvidovic, Dashofy** (*Software Architecture: Foundations, Theory and Practice*). Parte da una domanda: l'architettura è la **struttura a grana grossa** del sistema — un insieme di strutture, di tre tipi principali (C&C, modulari, di allocazione, → [[strutture-e-viste]]) — **ma come si progetta un'architettura?** ([[3-Architectural Patterns-complete.pdf#page=3]]).

La risposta del corso: uno strumento importante della progettazione è il **riuso dell'esperienza** (*reuse of experience*) ([[3-Architectural Patterns-complete.pdf#page=6]]):
- l'esperienza passata va **analizzata e raffinata**;
- è cruciale imparare **sia dai successi sia dai fallimenti** di altri ingegneri;
- fonti: **letteratura** e **conferenze**;
- l'esperienza fornisce l'**insieme iniziale di «possibili alternative di progetto»**.

## Strategie e metodi di progettazione

> 📄 Fonte: [[3-Architectural Patterns-complete.pdf#page=4]], [[3-Architectural Patterns-complete.pdf#page=5]]

| | Strategie di progettazione (*design strategies*) | Metodi di progettazione (*design methods*) |
|---|---|---|
| Cosa sono | un **approccio generale** alla progettazione | più **specifici** delle strategie |
| Cosa forniscono | — | una **notazione** da usare; una **descrizione del processo** da seguire; un insieme di **linee guida** per applicare il metodo |
| Esempi | divide-and-conquer e raffinamento per passi (*stepwise refinement*); strategie top-down vs bottom-up; astrazione dei dati e *information hiding*; uso di pattern e linguaggi di pattern; approccio iterativo e incrementale | progettazione orientata alle funzioni (strutturata, basata sui DFD); orientata agli oggetti; basata su componenti; orientata ai servizi; basata su modelli… |

![[lez04-ap-p5-metodi-di-progettazione.png]]
*Figura di [[3-Architectural Patterns-complete.pdf#page=5]], «Architecture Design Methods»: elenco di libri sui metodi di progettazione architetturale con le copertine — The Unified Software Development Process (Booch, Rumbaugh, Jacobson); A System of Patterns: Pattern-Oriented Software Architecture (Buschmann et al.); Object-Oriented Modeling and Design (Rumbaugh); Design and use of software architectures (Bosch); Software Architecture in Practice (Clements, Bass, Kazman); Applied Software Architecture (Hofmeister et al.); Software Product Lines (Clements, Northrop); Software Architectures: Perspectives on an Emerging Discipline (Shaw); Synthesis-Based Software Architecture Design (Tekinerdogan, Aksit).*

Tra i metodi c'è l'**Attribute-Driven Design** ([[3-Architectural Patterns-complete.pdf#page=7]]), con lo stesso diagramma della Lez. 1 → [[attribute-driven-design]].

## Le alternative da considerare

> 📄 Fonte: [[3-Architectural Patterns-complete.pdf#page=8]]

| Alternativa | Vantaggi | Svantaggi |
|---|---|---|
| **Progettare l'architettura da zero** | possono emergere **soluzioni nuove** | **costosa** (molto lavoro) e **rischiosa** |
| **Applicare una soluzione o strategia generica** (stile/pattern) e adattarla al problema | **riuso**, meno lavoro, meno errori | la soluzione generica può **non adattarsi perfettamente**; può richiedere un **lavoro significativo di adattamento** |
| **Applicare una soluzione specifica del dominio** (DSSA) | **riuso maggiore** | e se una DSSA **non esiste**? |

## DSSA, pattern, stili e design pattern: ambito di applicabilità

> 📄 Fonte: [[3-Architectural Patterns-complete.pdf#page=9]], [[3-Architectural Patterns-complete.pdf#page=22]]

Le forme di riuso viste dal corso sono quattro: **Domain-Specific Software Architectures (DSSA)**, **pattern architetturali**, **stili architetturali**, **design pattern**.

![[lez04-ap-p9-ambito-applicabilita.png]]
*Figura di [[3-Architectural Patterns-complete.pdf#page=9]], «Applicability Scope». Asse verticale: **conoscenza del dominio applicativo** (da *shallow*, scarsa, a *deep*, profonda). Asse orizzontale: **ambito** (*scope*) — dal livello di linguaggio di programmazione, alla struttura dell'applicazione (componenti e connettori), alla struttura del sistema. Dal basso a sinistra all'alto a destra: **(Program) Design patterns** (poca conoscenza del dominio, ambito del codice), **Styles** (ambito ampio, conoscenza del dominio bassa), **Architectural patterns** (più in alto), **Domain-specific s/w archs** (massima conoscenza del dominio e ambito di sistema).*

| Forma di riuso | Conoscenza del dominio incorporata | Ambito | Pagina |
|---|---|---|---|
| Design pattern (di programma) | bassa | livello del linguaggio di programmazione | — (fuori dal corso) |
| Stili architetturali | bassa | struttura dell'applicazione/sistema | [[layered]], [[client-server]], [[publish-subscribe]] |
| Pattern architetturali | media | struttura dell'applicazione (componenti e connettori) | [[pattern-architetturali]], [[state-logic-display]] |
| DSSA | alta | struttura dell'intero sistema in un dominio | [[dssa]] |

🧩 Lettura della figura: più si sale verso le DSSA, più la soluzione riusata è **completa** (copre tutto il sistema) ma **vale solo in un dominio**; scendendo verso i design pattern la soluzione vale ovunque ma copre un pezzo piccolo. È lo stesso trade-off della tabella delle alternative: maggiore riuso contro minore applicabilità.

Differenza tra pattern architetturale e DSSA ([[3-Architectural Patterns-complete.pdf#page=22]]): entrambi catturano **conoscenza architetturale riusabile**, ma con **ambiti diversi**:
- una **DSSA** fornisce un **quadro architetturale complessivo** per una **famiglia di sistemi** in uno **specifico dominio applicativo**;
- un **pattern architetturale** affronta un **problema architetturale ricorrente** e di solito si può applicare **in domini diversi**;
- **più pattern** possono essere **combinati** nella stessa DSSA o architettura di sistema.

## Perché importa

È la risposta del corso alla domanda «come si progetta un'architettura?» e corrisponde al blocco *Progettazione architetturale* del programma: «principi di progettazione architetturale, progettazione basata sul riuso di esperienza, attraverso pattern, stili e tattiche» ([[Programma Syllabus]]). Le tattiche (Lez. 1–3) sono il livello più fine di questo riuso; pattern, stili e DSSA i livelli più ampi.

> 🎯 Esame: strategie vs metodi con esempi; le tre alternative di progetto con pro e contro; differenza tra DSSA, pattern, stili e design pattern (figura dell'ambito di applicabilità).

## Connessioni

- [[dssa]]: la forma di riuso più specifica del dominio.
- [[linee-di-prodotto-software]]: riuso pianificato dentro una famiglia di prodotti.
- [[pattern-architetturali]], [[state-logic-display]]: il pattern come forma di riuso.
- [[attribute-driven-design]]: metodo che seleziona pattern, tattiche, architetture di riferimento e componenti esterni.
- [[importanza-architettura-software]] §3.10: restringere il vocabolario a soluzioni collaudate.

## Fonti

- [[approcci-riuso-progettazione-architettura]] — [[3-Architectural Patterns-complete.pdf#page=1]]–[[3-Architectural Patterns-complete.pdf#page=9]], [[3-Architectural Patterns-complete.pdf#page=22]]

_Aggiornato: 2026-10-01 — ingest 3-Architectural Patterns-complete.pdf_
