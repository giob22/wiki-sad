---
tipo: fonte
titolo: "Reuse-based approaches for designing a Software Architecture (versione completa) — parte nuova: middleware, MVC, Spring MVC, Sense–Compute–Control"
file_raw: "3-Architectural Patterns-complete.pdf"
pagine: "35-36, 39-96"
data_ingest: 2026-10-06
formato: slide-pdf
riferimento_libro: "Taylor, Medvidovic, Dashofy — Software Architecture: Foundations, Theory and Practice, cap. 4"
argomenti: [middleware nel three-tier, MVC, Observer, Strategy, modelli di interazione MVC, web MVC lato server, UI reattiva lato client, Front Controller, Spring Framework, IoC, Spring MVC, DispatcherServlet, HandlerMapping, ViewResolver, Thymeleaf, Spring Boot, applicazione spese, Sense-Compute-Control, varianti a tre e quattro stadi, IoT, Lunar Lander, ADS]
---

# Pattern architetturali (versione completa) — parte nuova di 3-Architectural Patterns-complete.pdf

## Cosa è nuovo rispetto al PDF precedente

Il file è la **versione completa** di `04-Architectural Patterns.pdf` (Lezione 4). Confronto pagina per pagina:

| Pagine del PDF completo | Rispetto a 04-Architectural Patterns.pdf | Dove è nel wiki |
|---|---|---|
| 1–34 | **identiche** alle pp. 1–34 | Lezione 4 → [[approcci-riuso-progettazione-architettura]] |
| 35 | **nuova**: middleware nell'architettura three-tier | [[architetture-multi-tier]] |
| 36 | = p. 35 (middleware come abilitatore di integrazione) **+ una nota nuova** su n-tier e middleware | [[architetture-multi-tier]] |
| 37–38 | = pp. 36–37 (4-tier, load-balanced cluster), titoli tradotti in inglese | Lezione 4 → [[architetture-multi-tier]] |
| 39–58 | **nuove**: pattern MVC | [[mvc]] |
| 59–82 | **nuove**: Spring MVC, Spring Boot, esempio completo | [[spring-mvc]], [[implementare-mvc]] |
| 83–95 | **nuove**: pattern Sense–Compute–Control | [[sense-compute-control]], [[applicare-sense-compute-control]] |
| 96 | **nuova**: conclusioni | qui sotto e [[pattern-architetturali]] |

Le pagine identiche non sono state ingerite di nuovo: per le pp. 1–34 e 37–38 i link del wiki restano verso `04-Architectural Patterns.pdf`.

## Numerazione pagine ↔ slide (parte nuova)

| Pagine PDF | Slide | Regola |
|---|---|---|
| 35–36 | 38–39 | slide = p. + 3 |
| 37–94 | 41–98 | slide = p. + 4 |
| 95–96 | 100–101 | slide = p. + 5 |

Le slide 77–86 (pp. 73–82, esempio delle spese) e 100 (p. 95, ADS) sono in italiano.

## Sommario

La lezione completa i pattern architetturali. Prima chiarisce il ruolo del **middleware** nel three-tier: strato trasversale che sostiene la comunicazione tra tier e l'integrazione con sistemi esterni; l'n-tier separa le responsabilità, il middleware fornisce i meccanismi per collegarle. Il **Model–View–Controller**, nato con Smalltalk allo Xerox PARC e oggi alla base di molti framework web, separa la logica di dominio dalla presentazione e dall'interazione: lo stesso Model sostiene più View e più Controller. Le responsabilità sono stabili ma le interazioni variano: MVC classico in versione pull o Observer (notify, then pull), web MVC lato server (il Controller passa un View Model alla View) e UI reattiva lato client (il server restituisce dati). Il MVC classico è una composizione dei design pattern **Observer** (Model = Subject, View = Observer) e **Strategy** (View = Context, Controller = Strategy), con un esempio Java prima e dopo Strategy. Nel web lato server si usa il pattern **Front Controller**. Segue un'introduzione a **Spring**: il container IoC dello Spring Framework, Spring MVC con DispatcherServlet, HandlerMapping, Controller annotati, ViewResolver e template Thymeleaf (flusso completo del requisito ShowExamSessions), Spring Boot e la gerarchia dei contesti, con un'applicazione completa per le spese personali. Infine il **Sense–Compute–Control** per il controllo di ambienti esterni: tre fasi, ciclo di controllo, esempio antintrusione, varianti a tre e quattro stadi, un sistema di controllo accessi, l'estensione all'IoT con controllo locale e remoto, gli attributi di qualità, il Lunar Lander e l'architettura dei sistemi di guida autonoma. Le conclusioni annunciano gli stili architetturali.

## Punti chiave

1. Middleware nel three-tier: trasversale, comunicazione tra tier, integrazione esterna ([[3-Architectural Patterns-complete.pdf#page=35]]); n-tier vs middleware ([[3-Architectural Patterns-complete.pdf#page=36]]).
2. MVC: sezione ([[3-Architectural Patterns-complete.pdf#page=39]]); origini e adozione ([[3-Architectural Patterns-complete.pdf#page=40]]); motivazione ([[3-Architectural Patterns-complete.pdf#page=41]]); tre elementi ([[3-Architectural Patterns-complete.pdf#page=42]]); relazioni strutturali ([[3-Architectural Patterns-complete.pdf#page=43]]); interazioni sull'esempio guida ([[3-Architectural Patterns-complete.pdf#page=44]]).
3. Responsabilità stabili, interazioni variabili ([[3-Architectural Patterns-complete.pdf#page=45]]); pull ([[3-Architectural Patterns-complete.pdf#page=46]]); Observer ([[3-Architectural Patterns-complete.pdf#page=47]]); interazione completa ([[3-Architectural Patterns-complete.pdf#page=48]]).
4. Design pattern Observer ([[3-Architectural Patterns-complete.pdf#page=49]]) e Strategy ([[3-Architectural Patterns-complete.pdf#page=50]]); View senza e con Strategy ([[3-Architectural Patterns-complete.pdf#page=51]], [[3-Architectural Patterns-complete.pdf#page=52]]).
5. Altri due modelli di interazione ([[3-Architectural Patterns-complete.pdf#page=53]]): web MVC lato server ([[3-Architectural Patterns-complete.pdf#page=54]]), UI reattiva lato client ([[3-Architectural Patterns-complete.pdf#page=55]]); confronto ([[3-Architectural Patterns-complete.pdf#page=56]]); MVC come famiglia di varianti ([[3-Architectural Patterns-complete.pdf#page=57]]); Front Controller ([[3-Architectural Patterns-complete.pdf#page=58]]).
6. Spring ([[3-Architectural Patterns-complete.pdf#page=59]], [[3-Architectural Patterns-complete.pdf#page=60]]); container IoC ([[3-Architectural Patterns-complete.pdf#page=61]]); Spring MVC ([[3-Architectural Patterns-complete.pdf#page=62]]); DispatcherServlet ([[3-Architectural Patterns-complete.pdf#page=63]]); flusso della richiesta ([[3-Architectural Patterns-complete.pdf#page=64]]); HandlerMapping ([[3-Architectural Patterns-complete.pdf#page=65]]); Controller e Thymeleaf ([[3-Architectural Patterns-complete.pdf#page=66]]); sequenza ShowExamSessions ([[3-Architectural Patterns-complete.pdf#page=67]]); mapping del Front Controller ([[3-Architectural Patterns-complete.pdf#page=68]]).
7. Spring Boot ([[3-Architectural Patterns-complete.pdf#page=69]]); punto di partenza ([[3-Architectural Patterns-complete.pdf#page=70]]); gerarchia dei contesti ([[3-Architectural Patterns-complete.pdf#page=71]]).
8. Esempio Spring MVC — gestione spese ([[3-Architectural Patterns-complete.pdf#page=72]]–[[3-Architectural Patterns-complete.pdf#page=82]]).
9. Sense–Compute–Control: sezione ([[3-Architectural Patterns-complete.pdf#page=83]]); domini e tre fasi ([[3-Architectural Patterns-complete.pdf#page=84]]); architettura e ciclo ([[3-Architectural Patterns-complete.pdf#page=85]]); antintrusione ([[3-Architectural Patterns-complete.pdf#page=86]]); varianti ([[3-Architectural Patterns-complete.pdf#page=87]], [[3-Architectural Patterns-complete.pdf#page=88]]); controllo accessi ([[3-Architectural Patterns-complete.pdf#page=89]]); IoT ([[3-Architectural Patterns-complete.pdf#page=90]]); attributi di qualità ([[3-Architectural Patterns-complete.pdf#page=91]]).
10. Lunar Lander ([[3-Architectural Patterns-complete.pdf#page=92]]–[[3-Architectural Patterns-complete.pdf#page=94]]); ADS ([[3-Architectural Patterns-complete.pdf#page=95]]); conclusioni ([[3-Architectural Patterns-complete.pdf#page=96]]).

## Concetti introdotti

- Entità: [[mvc]], [[spring-mvc]], [[sense-compute-control]]
- Esercizi: [[implementare-mvc]], [[applicare-sense-compute-control]]
- Aggiornati: [[architetture-multi-tier]] (middleware), [[pattern-architetturali]], [[exam-booking-system]], [[progetto-di-corso]]

## Domande aperte

- `CancellationController` è usato nel `main` di [[3-Architectural Patterns-complete.pdf#page=52]] ma la classe non è mostrata.
- L'esempio spese dice che il Controller **valida** l'input ([[3-Architectural Patterns-complete.pdf#page=73]]), ma il codice non contiene validazione.
- La figura ADS ([[3-Architectural Patterns-complete.pdf#page=95]]) non è commentata nelle slide.
- Nella numerazione mancano le slide 40 e 99 (probabilmente slide nascoste).

## Domande da esame

- Cos'è il pattern MVC? Quali responsabilità hanno Model, View e Controller? Perché è stato introdotto?
- Quali modelli di interazione esistono per MVC? Differenza tra MVC classico e web MVC lato server.
- Quali design pattern compongono il MVC classico? Spiega Observer e Strategy nel MVC.
- Cos'è il Front Controller? Come lo realizza Spring MVC?
- Descrivi il flusso di una richiesta in Spring MVC. Che ruolo hanno HandlerMapping e ViewResolver?
- Che differenza c'è tra Spring Framework, Spring MVC e Spring Boot? Cos'è il container IoC?
- Che ruolo ha il middleware in un'architettura n-tier?
- Cos'è il pattern Sense–Compute–Control? In quali domini si usa? Varianti a tre e quattro stadi.
- Come si estende il Sense–Compute–Control all'IoT? Controllo locale vs remoto.
- Applica il Sense–Compute–Control al Lunar Lander.

_Aggiornato: 2026-10-06 — ingest_
