---
tipo: entità
categoria: framework
famiglia: ""
---

# Spring MVC (con Spring Framework e Spring Boot)

## Cos'è

> 📄 Fonte: [[3-Architectural Patterns-complete.pdf#page=59]], [[3-Architectural Patterns-complete.pdf#page=60]]

**Spring MVC** è un **framework Java** per sviluppare **applicazioni web lato server** secondo l'approccio **Model–View–Controller** ([[3-Architectural Patterns-complete.pdf#page=59]] → [[mvc]], variante «Web MVC lato server»). Si basa sulla **Servlet API** e fa parte dello **Spring Framework** ([[3-Architectural Patterns-complete.pdf#page=60]]):

| Componente | Ruolo |
|---|---|
| **Spring Framework** | fornisce il **container** e le funzionalità di base |
| **Spring MVC** | realizza lo **strato web** |
| **Spring Boot** | semplifica **configurazione, avvio e deployment** dell'applicazione |

![[lez05-ap-p60-spring-framework-mvc-boot.png]]
*Figura di [[3-Architectural Patterns-complete.pdf#page=60]], «Spring Framework, Spring MVC, and Spring Boot» — il Framework fornisce le fondamenta, MVC aggiunge lo strato web, Boot semplifica configurazione ed esecuzione. Tre strati: **Spring Boot** (avvia e configura l'applicazione: starters, auto-configuration, server incorporato, packaging) *configura e avvia* → **Spring MVC** (realizza lo strato web lato server: DispatcherServlet, Controllers, request mapping, view rendering), che *è costruito su e usa* → **Spring Framework** (fondamenta e infrastruttura: IoC container, dependency injection, AOP, transazioni, accesso ai dati). A sinistra l'**Application code** (Controllers, Services, Repositories) entra in Spring MVC; a destra «Typical Web app = Spring Boot + Spring MVC + Framework Core». Nota: **Spring Boot non sostituisce Spring MVC o lo Spring Framework: li configura e li esegue**.*

## Spring Framework: il container IoC

> 📄 Fonte: [[3-Architectural Patterns-complete.pdf#page=61]]

Il cuore dello Spring Framework è il **container IoC** (*Inversion of Control*), rappresentato soprattutto dall'`ApplicationContext`. Il container IoC:
- **crea** gli oggetti dell'applicazione, chiamati **bean**;
- **risolve le loro dipendenze**;
- **collega tra loro** Controller, Service e Repository;
- **gestisce il ciclo di vita** dei componenti;
- offre **funzionalità trasversali** come gestione delle transazioni e della configurazione.

> 🧩 Elaborazione mia: «inversione del controllo» significa che non è il codice applicativo a creare con `new` gli oggetti da cui dipende; li riceve dal container (*dependency injection*). Per questo `ExpenseController` dichiara `@Autowired ExpenseRepository` senza crearlo ([[3-Architectural Patterns-complete.pdf#page=76]]). È la tattica *defer binding* della Lez. 3 ([[tattiche-modifiability]]): quale implementazione usare si decide alla configurazione/avvio, non nel codice del Controller.

## Spring MVC: lo strato web

> 📄 Fonte: [[3-Architectural Patterns-complete.pdf#page=62]]

Spring MVC è un **modulo dello Spring Framework specializzato nella gestione delle richieste HTTP**: traduce le richieste HTTP in chiamate ai componenti applicativi e coordina la risposta HTTP. Fornisce:
- **instradamento** delle richieste (*request routing*);
- **Controller annotati**;
- **binding e validazione** dei dati in input;
- integrazione con i **servizi applicativi**;
- **preparazione dei dati** per la View;
- **risoluzione della vista** e **generazione dell'HTML**.

### Il Front Controller: DispatcherServlet

> 📄 Fonte: [[3-Architectural Patterns-complete.pdf#page=63]], [[3-Architectural Patterns-complete.pdf#page=68]]

Spring MVC realizza il pattern **Front Controller** ([[mvc]] § Front Controller) con il **`DispatcherServlet`**, una servlet fornita da Spring MVC che è l'**unico punto d'ingresso** dello strato web. Il browser **non deve sapere quale classe Java** gestirà la richiesta: conosce solo un URL, ad esempio `GET /exam-sessions`. Il DispatcherServlet riceve la richiesta e **decide quale controller applicativo** deve gestirla.

![[lez05-ap-p63-dispatcherservlet.png]]
*Figura di [[3-Architectural Patterns-complete.pdf#page=63]]: Browser → *all HTTP requests* → **DispatcherServlet (Front Controller)**, che smista verso ExamSessionController, BookingController, StudentController.*

| Elemento del pattern | Spring MVC ([[3-Architectural Patterns-complete.pdf#page=68]]) |
|---|---|
| Front Controller | `DispatcherServlet` |
| Controller applicativo / handler | classe annotata con `@Controller` |
| Mappatura delle richieste | `HandlerMapping` |
| Operazione applicativa | metodo annotato con `@GetMapping` o `@PostMapping` |
| Dati del modello | attributi dell'oggetto `Model` |
| Selezione della vista | `ViewResolver` |
| Vista | template Thymeleaf, JSP, ecc. |

![[lez05-ap-p68-front-controller-spring.png]]
*Figura di [[3-Architectural Patterns-complete.pdf#page=68]]: la tabella originale, trascritta sopra.*

### Flusso di elaborazione di una richiesta

> 📄 Fonte: [[3-Architectural Patterns-complete.pdf#page=64]], [[3-Architectural Patterns-complete.pdf#page=65]], [[3-Architectural Patterns-complete.pdf#page=66]], [[3-Architectural Patterns-complete.pdf#page=67]]

Il **DispatcherServlet coordina** l'instradamento della richiesta, l'invocazione del Controller, la risoluzione della View e la generazione della risposta ([[3-Architectural Patterns-complete.pdf#page=64]]).

![[lez05-ap-p64-spring-mvc-flusso.png]]
*Figura di [[3-Architectural Patterns-complete.pdf#page=64]], «Spring MVC Request Processing Flow»: Browser → *HTTP request* → DispatcherServlet → *route request* → Controller → *invoke* → Application Service → *result* → Controller → *View name + data* → DispatcherServlet → *resolve view name* → ViewResolver → *View* → DispatcherServlet → *render View with data* → HTML View → *HTTP response* → Browser.*

**1. Trovare il metodo giusto** ([[3-Architectural Patterns-complete.pdf#page=65]]): il DispatcherServlet consulta un **`HandlerMapping`**, che conosce le corrispondenze tra **URL e metodi Java**, definite con **annotazioni**.

```java
// 📄 dalla slide 69: l'annotazione dice che il metodo gestisce le GET verso /exam-sessions
@Controller
public class ExamSessionController {
    @GetMapping("/exam-sessions")
    public String listAvailableSessions(Model model) {
        // ...
    }
}
```

**2. Il Controller esegue la logica di coordinamento** ([[3-Architectural Patterns-complete.pdf#page=66]]): invoca il servizio applicativo, inserisce i dati nel `Model`, restituisce il **nome logico della vista**. **Non genera direttamente la pagina HTML.**

```java
// 📄 dalla slide 70
@GetMapping("/exam-sessions")
public String listAvailableSessions(Model model) {
    var sessions = service.findAvailableSessions();   // invoca il servizio applicativo
    model.addAttribute("examSessions", sessions);     // mette i dati nel Model
    return "exam-sessions";                           // nome logico della vista, non un file
}
```

**3. Dalla vista logica al template**: `exam-sessions` non è il nome completo del file ma un **nome logico**; il **`ViewResolver`** lo mappa, ad esempio, sul template `src/main/resources/templates/exam-sessions.html`. Il template **Thymeleaf** genera la vista:

```html
<!-- 📄 dalla slide 70: una riga di tabella per ogni sessione nel Model -->
<tr th:each="session : ${examSessions}">
    <td th:text="${session.examName}"></td>
    <td th:text="${session.date}"></td>
</tr>
```

![[lez05-ap-p66-controller-thymeleaf.png]]
*Figura di [[3-Architectural Patterns-complete.pdf#page=66]]: il codice del Controller, le note su cosa fa e non fa, il percorso del template e il frammento Thymeleaf, trascritti sopra.*

### Flusso completo: requisito ShowExamSessions

> 📄 Fonte: [[3-Architectural Patterns-complete.pdf#page=67]]

![[lez05-ap-p67-sequenza-show-exam-sessions.png]]
*Figura di [[3-Architectural Patterns-complete.pdf#page=67]], diagramma di sequenza con Student, DispatcherServlet, HandlerMapping, ExamSessionController, ExamSessionService, ViewResolver, Thymeleaf View: `GET /exam-sessions` → *Find handler* → (*ExamSessionController method*) → `listAvailableSessions()` → `findAvailableSessions()` → (*List of sessions*) → (`"exam-sessions"` + Model) → *Resolve "exam-sessions"* → (*View template*) → *Render Model* → (*Generated HTML*) → *HTTP response*.*

![[anim-spring-mvc-richiesta.svg]]
*🧩 Animazione mia degli undici passi di [[3-Architectural Patterns-complete.pdf#page=67]] (generata con `output/diagrammi/genera_animazioni_lez05.py`): segui il pallino e la didascalia del passo.*

> 💡 Connessione: il DispatcherServlet è un **intermediario** (tattica *use an intermediary*, [[tattiche-modifiability]]): il browser dipende solo dagli URL, il Controller solo dal nome logico della vista. Si può cambiare la classe che gestisce un URL o il template di una vista senza toccare l'altra parte.

## Spring Boot

> 📄 Fonte: [[3-Architectural Patterns-complete.pdf#page=69]], [[3-Architectural Patterns-complete.pdf#page=70]]

Spring Boot **non sostituisce** lo Spring Framework né Spring MVC: li **configura e avvia** usando **convenzioni** e **auto-configurazione**. Quando ci sono le dipendenze web, Spring Boot può:
- avviare un **servlet container incorporato**, di solito **Tomcat**;
- creare l'`ApplicationContext`;
- abilitare la **scansione dei componenti**;
- registrare il `DispatcherServlet`;
- configurare Spring MVC;
- impostare la risoluzione delle viste;
- creare un **eseguibile dell'applicazione come file JAR**.

```java
// 📄 dalla slide 74: il punto di partenza dell'applicazione
@SpringBootApplication
public class ExamBookingApplication {
    public static void main(String[] args) {
        SpringApplication.run(ExamBookingApplication.class, args);
    }
}
```

L'annotazione `@SpringBootApplication` abilita, in forma semplificata: **configurazione Spring**, **scansione dei componenti**, **auto-configurazione**.

> 💡 Connessione: «un eseguibile JAR con il server incorporato» è un'**unità di deployment** unica — è ciò che rende naturale impacchettarla in un container Docker, la tecnologia proposta per il [[progetto-di-corso]]. Nel deployment della Lez. 1 l'applicazione era invece un `.war` installato in un web container esterno ([[strutture-di-allocazione]]).

## Gerarchia dei contesti

> 📄 Fonte: [[3-Architectural Patterns-complete.pdf#page=71]]

![[lez05-ap-p71-context-hierarchy.png]]
*Figura di [[3-Architectural Patterns-complete.pdf#page=71]], «Context hierarchy in Spring Web MVC»: il **DispatcherServlet** (in attesa di HttpServletRequest) usa un **WebApplicationContext** che contiene i bean web — Controllers, HandlerMapping, ViewResolver, locale resolvers e altri; questo è collegato a un **WebApplicationContext radice** che contiene i bean dello strato intermedio — services, datasources, ecc.*

> 🧩 Elaborazione mia: la slide ha solo la figura. Il contesto «web» del DispatcherServlet vede i bean del contesto radice (servizi, accesso ai dati), non viceversa: è lo stesso vincolo di dipendenza dello stile [[layered]] (lo strato web usa lo strato di servizio, non il contrario).

## Come si usa nel corso

- Esempio completo in Spring MVC (applicazione per le spese personali, slide 76–86) → [[implementare-mvc]] (caso 3).
- Tecnologia suggerita per il progetto: **Java, Spring Boot e altri framework** ([[00_IntroduzioneAlCorso_SAD.pdf#page=25]] → [[progetto-di-corso]]). La Lez. 2 usava già Spring Boot con Resilience4j per le tattiche di disponibilità ([[circuit-breaker]]).

## Link ai concetti correlati

[[mvc]] · [[implementare-mvc]] · [[architetture-multi-tier]] · [[tattiche-modifiability]]

## Fonti

- [[architectural-patterns-mvc-scc]] — [[3-Architectural Patterns-complete.pdf#page=58]]–[[3-Architectural Patterns-complete.pdf#page=71]]

_Aggiornato: 2026-10-06 — ingest 3-Architectural Patterns-complete.pdf (nuova lezione)_
