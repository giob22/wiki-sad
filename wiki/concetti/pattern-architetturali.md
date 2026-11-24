---
tipo: concetto
importanza_esame: alta
prerequisiti: ["tattiche-architetturali"]
fonti_pdf: ["01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=21", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=22", "01-IntroductionOnSoftwareArchitecture.pdf#page=47", "00_IntroduzioneAlCorso_SAD.pdf#page=16"]
termine_inglese: "architectural pattern"
---

# Pattern architetturali

## Definizione

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=21]] (slide 72), [[01-IntroductionOnSoftwareArchitecture.pdf#page=47]]

> 🔑 Definizione chiave: un **pattern architetturale** descrive un particolare **problema di progetto ricorrente** che si presenta in **contesti di progetto specifici** e presenta una **soluzione architetturale collaudata** (*well-proven*) per quel problema ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=21]]).

Esempio: il pattern architetturale **Layered** ([[layered]]).

Formulazione equivalente della prima parte della lezione: i pattern architetturali sono **composizioni di elementi architetturali** che forniscono **strategie preconfezionate** per risolvere alcuni problemi di un sistema ([[01-IntroductionOnSoftwareArchitecture.pdf#page=47]]).

### La definizione della Lez. 4

> 📄 Fonte: [[3-Architectural Patterns-complete.pdf#page=22]], [[3-Architectural Patterns-complete.pdf#page=23]]

Nella Lez. 4 il pattern architetturale è un **insieme riusabile di decisioni di progetto architetturali** che affronta un **problema di progetto ricorrente**; definisce una **soluzione generale** adattabile a contesti di sviluppo diversi. Si distingue dalla DSSA per l'ambito: la DSSA è un quadro complessivo per una famiglia di sistemi di un dominio, il pattern risolve un problema ricorrente in domini diversi, e più pattern si combinano nella stessa DSSA o architettura → [[progettazione-basata-sul-riuso]], [[dssa]].

Esempi elencati ([[3-Architectural Patterns-complete.pdf#page=23]]): **State-Logic-Display** (three-tiered pattern) → [[state-logic-display]]; **Model-View-Controller**; **Sense-Compute-Control**. Nella lezione successiva (PDF completo) MVC e Sense–Compute–Control sono spiegati per esteso → [[mvc]], [[sense-compute-control]]. Le conclusioni ([[3-Architectural Patterns-complete.pdf#page=96]]) riassumono: si sono analizzate due strategie di progetto basate sul riuso — **DSSA** e **pattern architetturali** (Three-Tier, MVC, Sense–Compute–Control) — e gli **stili architetturali** arriveranno nelle prossime lezioni.

> 🧩 Elaborazione mia — i tre pattern a confronto:
>
> | Pattern | Problema ricorrente | Struttura | Tipo di interazione |
> |---|---|---|---|
> | State-Logic-Display | separare dati, regole e interfaccia distribuendoli su tier | display / logic / state | richiesta–risposta |
> | MVC | presentare e manipolare gli stessi dati in più modi | model / view / controller | eventi utente (o richieste HTTP) |
> | Sense–Compute–Control | controllare un ambiente fisico | sensori / calcolo / attuatori | ciclo continuo |

## Pattern e tattiche

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=21]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=22]] (slide 73)

**I pattern architetturali spesso comprendono più tattiche** di attributi di qualità (es. **Layers** o **Microservices**).

Esempio — il pattern **Layers** incorpora ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=22]]):

| Tattica incorporata | Come la realizza il pattern |
|---|---|
| **Separare le responsabilità** | assegna responsabilità distinte agli strati |
| **Restringere le dipendenze** | controlla quali strati possono comunicare |
| **Usare un intermediario** | uno strato può isolare lo strato superiore dalle tecnologie sottostanti |
| **Astrarre i servizi comuni** | ogni strato espone servizi tramite interfacce definite |

> ⚖️ Trade-off: queste decisioni possono migliorare **modificabilità, testabilità e portabilità**, ma possono introdurre **latenza aggiuntiva** e **complessità** ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=22]]).

> 🧩 Elaborazione mia — tattica vs pattern:
>
> | | Tattica | Pattern |
> |---|---|---|
> | Granularità | una singola decisione di progetto | una soluzione completa (elementi + relazioni + vincoli) |
> | Attributi | mira a **un** attributo di qualità | ne tocca **molti**, con trade-off |
> | Relazione | è un «mattone» | è composto di più tattiche |

## Pattern e stili nel programma

> 📄 Fonte: [[00_IntroduzioneAlCorso_SAD.pdf#page=16]]

Il programma distingue:
- **pattern architetturali**: State-Logic-Display (three-tier), Sense-Compute-Control, MVC;
- **stili architetturali**: monolitico; layered (virtual machine e client-server); data-flow (batch e pipe-and-filter); shared memory (blackboard e rule-based); interpreter (mobile code); implicit invocation (publish-subscribe ed event-based); SOA; microservizi.

La progettazione architetturale si basa sul **riuso dell'esperienza** tramite **DSSA** (*Domain-Specific Software Architectures*), pattern, stili e tattiche ([[00_IntroduzioneAlCorso_SAD.pdf#page=16]]).

La Lez. 4 colloca stili, pattern architetturali, DSSA e design pattern nella figura dell'**ambito di applicabilità**: gli stili incorporano meno conoscenza del dominio dei pattern architetturali ([[3-Architectural Patterns-complete.pdf#page=9]] → [[progettazione-basata-sul-riuso]]). TODO: da espandere — la definizione precisa di **stile** non è ancora stata data: l'outline della Lez. 4 annuncia gli *Architectural Styles* ([[3-Architectural Patterns-complete.pdf#page=2]]) ma il PDF si ferma ai pattern; nelle Lez. 1 e 3 «Layered» è chiamato sia *architecture* sia *pattern*.

## Perché importa

I pattern sono la forma principale di **riuso di soluzioni collaudate**: restringere il vocabolario del progetto a pattern, tattiche ed elementi off-the-shelf rende i progetti più semplici da capire, analizzare e comunicare ([[importanza-architettura-software]] §3.10). Il progetto di corso userà facoltativamente Web App client-server, microservizi, MVC e REST ([[00_IntroduzioneAlCorso_SAD.pdf#page=25]]).

> 🎯 Esame: definizione di pattern; perché un pattern contiene più tattiche; le tattiche del pattern Layers e il loro trade-off.

## Connessioni

- [[tattiche-architetturali]]: i mattoni dei pattern.
- [[layered]], [[microservices]], [[client-server]]: pattern/stili già incontrati.
- [[strutture-e-viste]]: i pattern come strategie preconfezionate nella scelta delle strutture.

## Fonti

- [[attributi-di-qualita-e-importanza-architettura]] — [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=21]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=22]]
- [[introduzione-architettura-software]] — [[01-IntroductionOnSoftwareArchitecture.pdf#page=47]]
- [[presentazione-corso]] — [[00_IntroduzioneAlCorso_SAD.pdf#page=16]]

_Aggiornato: 2026-09-26 — ingest lezione 1_
_Aggiornato: 2026-10-01 — ingest 3-Architectural Patterns-complete.pdf_
_Aggiornato: 2026-10-06 — MVC e Sense–Compute–Control spiegati; conclusioni della lezione_
