# Software Architecture Design — corso completo

Testo unico di studio del corso (LM Ingegneria Informatica, UNINA, DIETI, prof.ssa Anna Rita Fasolino). Contiene **tutta e sola la teoria**, cioè solo ciò che sta nei PDF delle lezioni, nell'ordine delle slide: definizioni, elenchi, tabelle, esempi, diagrammi e codice. Non c'è la presentazione del corso (Lezione 0) né il progetto di corso. Le spiegazioni estese, gli esempi espansi, i grafici aggiuntivi e gli esercizi stanno nelle pagine concetto ed esercizio, richiamate in fondo a ogni lezione («Approfondimenti nel wiki»).

**Come leggerlo.** Il riferimento al PDF compare solo nel titolo di ogni sezione (`p. N` apre la pagina). Il sito di studio si genera da questo file con `python output/crea_sito.py`; il controllo di integrità con `python output/controlla_corso.py`.

## Indice

| # | Lezione | PDF sorgente |
|---|---|---|
| 1 | [[#Lezione 1 — Introduzione all'architettura software\|Introduzione all'architettura software]] | 01-IntroductionOnSoftwareArchitecture.pdf, 01-IntroductionOnSoftwareArchitecture-2 parte.pdf |
| 2 | [[#Lezione 2 — Attributi di qualità: disponibilità\|Attributi di qualità: disponibilità]] | 02-Availability.pdf |
| 3 | [[#Lezione 3 — Attributi di qualità: modificabilità\|Attributi di qualità: modificabilità]] | 03-Modifiability.pdf |
| 4 | [[#Lezione 4 — Progettazione basata sul riuso: DSSA, pattern e architetture multi-tier\|Progettazione basata sul riuso: DSSA, pattern e architetture multi-tier]] | 3-Architectural Patterns-complete.pdf |
| 5 | [[#Lezione 5 — Pattern architetturali: MVC, Spring MVC e Sense-Compute-Control\|Pattern architetturali: MVC, Spring MVC e Sense-Compute-Control]] | 3-Architectural Patterns-complete.pdf |
| 6 | [[#Lezione 6 — Agile Project Management (Parte 1)\|Agile Project Management (Parte 1)]] | 04_Agile_01_bis.pdf |
| 7 | [[#Lezione 7 — Agile Project Management (Parte 2): il framework Scrum\|Agile Project Management (Parte 2): il framework Scrum]] | 04_Agile_02.pdf |
| 8 | [[#Lezione 8 — Stili architetturali\|Stili architetturali]] | 05_Architectural_Styles_Complete.pdf |
| 9 | [[#Lezione 9 — Il processo di progettazione architetturale: ASR e il metodo ADD\|Il processo di progettazione architetturale: ASR e il metodo ADD]] | 06-ADD-Designing a Software Architecture.pdf |
| 10 | [[#Lezione 10 — Architetture orientate ai servizi e a microservizi (parte 1)\|Architetture orientate ai servizi e a microservizi (parte 1)]] | 07— Service-Oriented and Microservice Architectures-1 part.pdf |

## Lezione 1 — Introduzione all'architettura software

*Fonte: 01-IntroductionOnSoftwareArchitecture.pdf (50 pagine) e 01-IntroductionOnSoftwareArchitecture-2 parte.pdf (45 pagine, numerazione stampata dalla slide 51 alla 97). Cap. 1 di Bass, Clements, Kazman, «Software Architecture in Practice». Esempio guida: l'Exam Booking System.*

### Panoramica · [[01-IntroductionOnSoftwareArchitecture.pdf#page=2|p. 2]]–[[01-IntroductionOnSoftwareArchitecture.pdf#page=3|3]]

Tre parti: **1. Che cos'è un'architettura software · 2. Capire gli attributi di qualità · 3. Perché l'architettura è importante.**

**Ruolo dell'architettura nei processi di sviluppo**
- È impossibile costruire un sistema complesso di alta qualità, in tempi di consegna brevi, senza curare la progettazione dell'architettura.
- Stili, pattern, modelli e tattiche architetturali permettono di ottenere attributi di qualità diversi.
- Esempio, le architetture a **microservizi**: ogni microservizio ha il proprio *bounded context* e può scalare, essere rilasciato e guastarsi in modo indipendente, migliorando resilienza e agilità.
- Definire la struttura dell'architettura permette di organizzare meglio il processo di sviluppo.

### 1. Che cos'è un'architettura software

#### Definizione di Bass, Clements e Kazman · [[01-IntroductionOnSoftwareArchitecture.pdf#page=4|p. 4]]

- Esistono moltissime definizioni di architettura software.
- Definizione di **Bass, Clements e Kazman**: *l'architettura software di un sistema è l'**insieme delle strutture necessarie per ragionare sul sistema**. Queste strutture comprendono **elementi software, relazioni tra di essi e proprietà di entrambi**.*
- Un'architettura comprende **più strutture**, ciascuna con una prospettiva diversa sul sistema.
- Le definizioni precedenti mettevano in evidenza gli elementi architetturali, la loro organizzazione o le motivazioni delle decisioni di progetto; Bass, Clements e Kazman mettono in evidenza **le strutture multiple** e il loro ruolo nel **ragionare sulle proprietà del sistema**.

#### Tre categorie di strutture · [[01-IntroductionOnSoftwareArchitecture.pdf#page=5|p. 5]]

- Le tre categorie: **strutture componenti-e-connettori (C&C)**, **strutture di modulo**, **strutture di allocazione**.
- Una struttura è **architetturale** se permette di ragionare sul sistema e sulle sue proprietà: il ragionamento riguarda un attributo importante per qualche stakeholder (funzionalità, capacità di continuare a funzionare a fronte di guasti o attacchi, facilità di modifica, reattività alle richieste degli utenti…).
- L'insieme delle strutture **non è né fisso né limitato**: dipende.

#### Strutture e viste: l'analogia del corpo umano · [[01-IntroductionOnSoftwareArchitecture.pdf#page=6|p. 6]]

- Il corpo umano è fatto di strutture diverse; ognuna si può modellare con una **vista** diversa, di interesse per un medico specialista diverso. Tutte le viste descrivono il corpo umano.

![[lez01-intro-p6-analogia-corpo-umano.png]]
*Quattro sagome umane: scheletro, muscoli, sistema nervoso, sistema circolatorio. Ogni sagoma è una struttura diversa dello stesso corpo.*

#### Punti chiave sull'architettura · [[01-IntroductionOnSoftwareArchitecture.pdf#page=7|p. 7]]

- Un'architettura è un'**astrazione** di un sistema: seleziona alcuni dettagli e ne sopprime altri.
- L'architettura è progettazione, ma **non ogni progettazione è architettura**.
- **Ogni sistema ha un'architettura**, ma può non essere nota a nessuno (per mancanza di documentazione architetturale).
- Non tutte le architetture sono buone: importanza della **progettazione** e della **valutazione** dell'architettura.
- L'architettura **include il comportamento**: il modo in cui gli elementi interagiscono tra loro e con l'ambiente influisce sulle proprietà (per esempio le prestazioni a runtime); importanza di progettare e documentare questo comportamento.

### Strutture di modulo

#### Che cosa sono · [[01-IntroductionOnSoftwareArchitecture.pdf#page=8|p. 8]]–[[01-IntroductionOnSoftwareArchitecture.pdf#page=9|9]]

- Suddividono il sistema in **unità di implementazione, i moduli**: insiemi di unità di codice o di dati da costruire o riusare, a cui sono assegnate **responsabilità funzionali**.
- I moduli possono essere classi, package, strati o altre unità di implementazione.
- Relazioni tra moduli: **uses**, **generalizzazione**, **«is part of»**.
- I moduli rappresentano un modo **statico** di considerare il sistema.

#### Moduli e relazioni in UML · [[01-IntroductionOnSoftwareArchitecture.pdf#page=10|p. 10]]

![[lez01-intro-p10-uml-moduli-relazioni.png]]
*A sinistra moduli in UML (package, classe, classe con attributi e operazioni, classe astratta, classe con interfaccia fornita a «lecca-lecca», interfaccia); a destra le relazioni UML (is-part-of, uses, generalizzazione).*

#### Domande a cui rispondono · [[01-IntroductionOnSoftwareArchitecture.pdf#page=11|p. 11]]

- Qual è la **responsabilità funzionale primaria** di ogni modulo?
- Quali altri elementi software un modulo **può** usare? Quali **usa e da cui dipende davvero**?
- Quali moduli sono legati da **generalizzazione/specializzazione** (ereditarietà)?
- Le strutture di modulo servono anche a valutare l'**impatto** di una modifica alle responsabilità assegnate a ciascun modulo: sono lo **strumento principale per ragionare sulla modificabilità**.

#### Esempio guida: Exam Booking System · [[01-IntroductionOnSoftwareArchitecture.pdf#page=12|p. 12]]

- Sistema familiare con problemi architetturali non banali. Gli studenti consultano le sessioni d'esame e inviano o annullano prenotazioni; il sistema controlla le regole di prenotazione e invia notifiche; i docenti vedono gli elenchi dei partecipanti; gli amministratori gestiscono sessioni e regole.
- Tre caratteristiche: **responsabilità funzionali**, **picco di carico all'apertura delle prenotazioni**, **regole che cambiano nel tempo**.
- L'architettura aiuta a ragionare su **modificabilità, prestazioni, disponibilità, sicurezza**. Lo stesso sistema sarà esaminato con la vista di moduli, di runtime e di deployment.

![[lez01-intro-p12-exam-booking-system.png]]
*Descrizione del sistema, le tre caratteristiche e le quattro qualità su cui l'architettura permette di ragionare.*

#### Tre viste dello stesso sistema · [[01-IntroductionOnSoftwareArchitecture.pdf#page=13|p. 13]]

| Struttura | Elementi nell'Exam Booking System | Domanda |
|---|---|---|
| **Modulo** | Booking, Eligibility Checking, Exam Catalog, Notifications | come è organizzato il codice? |
| **Componenti e connettori** | Web Client, Application API, Database, Message Queue | come si comporta il sistema a runtime? |
| **Allocazione** | istanze applicative, database server, nodi cloud, collegamenti di rete | dove viene eseguito il software? |

Le viste sono collegate, ma **nessuna è una versione più dettagliata di un'altra**.

![[lez01-intro-p13-tre-viste.png]]
*Le tre colonne con gli elementi dell'esempio e la domanda cui risponde ciascuna.*

#### Vista dei moduli dell'Exam Booking System · [[01-IntroductionOnSoftwareArchitecture.pdf#page=14|p. 14]]–[[01-IntroductionOnSoftwareArchitecture.pdf#page=16|16]]

![[lez01-intro-p14-vista-moduli-exam-booking.png]]
*Le frecce rappresentano la relazione **uses**. Booking usa Authentication, Exam Catalog, Eligibility Checking e Notifications; Administration usa Exam Catalog.* Una modifica a una regola di ammissione dovrebbe riguardare principalmente Eligibility Checking, non Booking.

La vista dei moduli permette di ragionare sulla **modificabilità**:
- Se cambia la regola sui prerequisiti, quali moduli vanno modificati? Una **corretta assegnazione delle responsabilità** a moduli separati localizza il cambiamento e riduce il rischio di effetti indiretti.
- Booking può dipendere direttamente da Notifications? Usare **meccanismi di invocazione indiretta** (per esempio la pubblicazione di eventi) riduce l'accoppiamento tra moduli e semplifica modificabilità e disponibilità, anche se aggiunge complessità.
- Come evitare che ogni modulo interroghi direttamente il database degli studenti? Introducendo un modulo che espone API di accesso ai dati degli studenti si riducono le dipendenze eccessive e si semplificano le modifiche future.

![[lez01-intro-p16-moduli-event-based.png]]
*Struttura dei moduli con notifica a eventi: Booking e Notifications condividono un contratto di eventi («Booking Events») ma non dipendono direttamente l'uno dall'altro; compare il nuovo modulo Student Records, usato da Eligibility Checking.*

#### Strutture di modulo utili

##### Decomposizione (decomposition) · [[01-IntroductionOnSoftwareArchitecture.pdf#page=17|p. 17]]–[[01-IntroductionOnSoftwareArchitecture.pdf#page=19|19]]
- Mostra come i moduli sono decomposti ricorsivamente in moduli più piccoli, fino a quando sono abbastanza piccoli da essere compresi facilmente.
- È un **punto di partenza comune per la progettazione**, spesso base dell'organizzazione del progetto: struttura della documentazione, piani di integrazione e di test.

![[lez01-intro-p18-decomposition-structure.png]]
*Package UML annidati del sistema ATIA-M: moduli «Windows apps» (con codice comune per thick client e due applicazioni Windows), moduli web lato server, moduli Java lato server.*

![[lez01-intro-p19-uml-decomposition-exam-booking.png]]
*Decomposizione dell'Exam Booking System: i package annidati rappresentano la relazione is-part-of (Student-facing Applications, Shared Client Code, Server-side Modules con Booking Management, Eligibility Checking, Notifications). Mostra solo la decomposizione; le dipendenze richiedono una vista uses separata.*

##### Uses · [[01-IntroductionOnSoftwareArchitecture.pdf#page=20|p. 20]]
- I moduli sono legati dalla relazione «use»: un modulo ne usa un altro se la **correttezza del primo richiede la presenza e il corretto funzionamento del secondo**.
- Può servire a valutare il **debito sociale** (*social debt*): la quantità di comunicazione tra i team.

![[lez01-intro-p20-uses-structure.png]]
*Package legati da frecce «use»; sono evidenziati i moduli che devono essere presenti in un incremento se è presente `admin.client` (admin.client, admin.core, util, dao).*

##### Strati (layer) · [[01-IntroductionOnSoftwareArchitecture.pdf#page=21|p. 21]]
- I moduli sono chiamati **strati**. Uno strato è una «**macchina virtuale**» astratta che fornisce un insieme coeso di servizi tramite un'interfaccia gestita.
- Nei sistemi strettamente a strati, uno strato può usare **un solo altro strato**.
- Conferisce **portabilità**: la capacità di cambiare la macchina virtuale sottostante.

![[lez01-intro-p21-layer-structure-unix.png]]
*Struttura a strati di Unix System V: programmi utente e librerie (livello utente); interfaccia di system call, file subsystem, process control, buffering, driver di dispositivo a caratteri e a blocchi, hardware control (livello kernel). Le frecce significano «può usare».*

##### Classi (class) · [[01-IntroductionOnSoftwareArchitecture.pdf#page=22|p. 22]]
- I moduli sono **classi**, legate dalle relazioni «inherits-from» o «is-an-instance-of». Supporta il ragionamento su insiemi di comportamenti simili e differenze parametrizzate. È la struttura tipica di un progetto orientato agli oggetti.

![[lez01-intro-p22-class-structure.png]]
*Struttura di generalizzazione da uno strumento per architetti: la classe `Fact` eredita da `java.util.Observable`; otto classi `…VO` ereditano da `Fact`.*

##### Modello dei dati (data model) · [[01-IntroductionOnSoftwareArchitecture.pdf#page=23|p. 23]]
- Descrive la struttura statica dell'informazione in termini di entità e relazioni.

![[lez01-intro-p23-data-model.png]]
*Tre entità (PurchaseOrder, OrderItem, CatalogItem) con chiavi e tipi; le linee a «zampa di gallina» indicano che a un ordine corrispondono 0 o più voci, ognuna legata a esattamente un articolo di catalogo.*

### Strutture componenti-e-connettori (C&C)

#### Che cosa sono · [[01-IntroductionOnSoftwareArchitecture.pdf#page=24|p. 24]]–[[01-IntroductionOnSoftwareArchitecture.pdf#page=26|26]]

- Mostrano come gli elementi **interagiscono a runtime** per svolgere le funzioni del sistema.
- **Componenti**: le unità principali di calcolo (servizi, peer, client, server, filtri o altri elementi di runtime).
- **Connettori**: i veicoli di comunicazione tra componenti (call-return, operatori di sincronizzazione di processi, pipe, ecc.).

![[lez01-intro-p26-esempio-cc-view.png]]
*Vista C&C di un sistema bancario: più istanze di «Client Teller 1» collegate da un connettore publish-subscribe e da un connettore client-server request/reply con failover automatico verso due server (Main e Backup); entrambi accedono all'Account Database, al quale accede anche un'applicazione amministrativa.*

#### Domande a cui rispondono · [[01-IntroductionOnSoftwareArchitecture.pdf#page=27|p. 27]]

- Quali sono i principali componenti in esecuzione e come interagiscono a runtime?
- Quali sono i principali archivi di dati condivisi? Quali parti del sistema sono replicate?
- Come avanzano i dati nel sistema? Quali parti possono funzionare in parallelo?
- La struttura del sistema può cambiare mentre il sistema è in esecuzione e come?
- Le strutture C&C sono fondamentali per studiare le **proprietà di runtime**: prestazioni, sicurezza, disponibilità e altro.

#### Vista runtime di una prenotazione d'esame · [[01-IntroductionOnSoftwareArchitecture.pdf#page=28|p. 28]]–[[01-IntroductionOnSoftwareArchitecture.pdf#page=31|31]]

![[lez01-intro-p28-runtime-view-exam-booking.png]]
*Student Web Client → Application API → Booking Service; il Booking Service scrive nel Booking Database e nella Message Queue; la coda consegna al Notification Service (notifica asincrona). Il Booking Service è un componente runtime che contiene i moduli Booking ed Eligibility Checking.* La notifica asincrona riduce la latenza della prenotazione ma richiede una gestione esplicita dei guasti.

La vista runtime permette di ragionare su **prestazioni e resilienza**: si può seguire il flusso di una singola richiesta.
1. Lo studente invia la prenotazione. 2. Il Booking Service verifica i vincoli. 3. Il sistema registra la prenotazione. 4. La conferma è messa in coda. 5. Il Notification Service invia l'e-mail.

**Primo trade-off:** la notifica asincrona migliora tempo di risposta e resilienza, ma introduce **consistenza finale** e aumenta la complessità della gestione degli errori.

Domande che la vista C&C permette di porre, per attributo:

| Attributo | Domande |
|---|---|
| **Prestazioni** | quante comunicazioni servono per completare una prenotazione? quali chiamate sono sincrone? dove si può formare una coda? quale componente può diventare collo di bottiglia? |
| **Disponibilità e resilienza** | cosa succede se il Notification Service non risponde? la coda conserva i messaggi durante un guasto? e se il database non è disponibile? ci sono componenti critici non replicati? |
| **Sicurezza** | quali dati passano nei connettori? quali comunicazioni vanno cifrate? quale componente autentica lo studente? chi può accedere al database o pubblicare eventi? |
| **Scalabilità** | quali componenti si possono replicare? le istanze condividono lo stato? il database regge più richieste? la coda permette di distribuire il lavoro tra più consumatori? |

#### Esempi di strutture C&C · [[01-IntroductionOnSoftwareArchitecture.pdf#page=32|p. 32]]–[[01-IntroductionOnSoftwareArchitecture.pdf#page=36|36]]

**Le strutture C&C mostrano una vista di runtime**
- I moduli sono stati compilati in forme eseguibili (componenti); i connettori indicano esplicitamente come i componenti interagiscono (call/return, request/response, pub/sub…).
- Le strutture C&C sono **ortogonali** alle strutture di modulo: un'unità di codice può essere compilata in un unico servizio replicato migliaia di volte; oppure 1.000 moduli possono essere compilati e collegati in un unico eseguibile (componente).

**Esempio: architettura client-server di un sistema bancario ATM degli anni '90**
- Tre tipi di componenti: processi server, processi client ATM, componenti applicativi Windows; i connettori sono **socket TCP**; oggi si usano connettori basati su HTTP.

![[lez01-intro-p34-cc-atm-client-server.png]]
*Tre server (Bank transaction authorizer, ATM monitoring server, ATM reconfiguration server) collegati a tre client; ogni linea è un connettore socket TCP con porte client e server.*

**Struttura a servizi (service structure)**
- Le unità sono **servizi** che interoperano scambiandosi messaggi; la struttura aiuta a progettare un sistema di componenti sviluppabili in modo indipendente.

![[lez01-intro-p35-service-structure.png]]
*Client (app mobile, altro dispositivo, browser) → API Gateway → cinque servizi, ognuno con i propri moduli e il proprio database; invocazione remota e comunicazione asincrona; a destra servizi infrastrutturali comuni (message broker, monitoring, configuration service, service discovery).*

**Relazione tra le strutture**
- Le strutture danno prospettive diverse ma **non sono indipendenti**: elementi di una struttura sono collegati a elementi di altre. Un modulo di una struttura di decomposizione può manifestarsi come uno, parte di uno o più componenti in una struttura C&C.

![[lez01-intro-p36-relazione-tra-strutture.png]]
*A sinistra una vista di decomposizione (System con Client e Server), a destra una vista client-server (un server S1 e dieci client). La vista di destra serve per analisi delle prestazioni, previsione dei colli di bottiglia e gestione del traffico di rete: cose estremamente difficili o impossibili con la vista di sinistra.*

### Strutture di allocazione

#### Che cosa sono · [[01-IntroductionOnSoftwareArchitecture.pdf#page=37|p. 37]]–[[01-IntroductionOnSoftwareArchitecture.pdf#page=38|38]]

- Stabiliscono la **corrispondenza tra le strutture software e le strutture non software** del sistema (organizzazione, ambienti di sviluppo, test ed esecuzione).
- Tre domande (e corrispondenze): su quali **nodi di esecuzione** gira ogni elemento software? In quali **directory o file** è memorizzato ogni elemento durante sviluppo, test e build? Quale **team di sviluppo** è responsabile di ogni elemento?

![[lez01-intro-p38-allocation-structures.png]]
*Al centro gli elementi software dalle viste di modulo o C&C, collegati alla piattaforma di calcolo (deployment style), all'ambiente di produzione (install style) e all'organizzazione dello sviluppo (work assignment style).*

#### Vista di deployment dell'Exam Booking System · [[01-IntroductionOnSoftwareArchitecture.pdf#page=39|p. 39]]–[[01-IntroductionOnSoftwareArchitecture.pdf#page=41|41]]

![[lez01-intro-p39-deployment-iniziale.png]]
*Configurazione iniziale: un solo nodo applicativo regge un carico limitato. Student Device (browser) → HTTPS → Application Server (Web Container con `exam-booking-app.war`) → JDBC/TCP → Database Server (DBMS, `booking-db`); → HTTPS/REST → University SIS Server (`student-records-api`).* L'artefatto applicativo è distribuito una sola volta; il Student Information System possiede i dati accademici.

![[lez01-intro-p40-deployment-scalabile.png]]
*Configurazione scalabile per i picchi di iscrizione: le istanze applicative sono replicate dietro un Load Balancer; compare un Message Broker (AMQP, `notification-queue`).* La replica elimina il server applicativo come singolo punto di guasto; l'infrastruttura condivisa richiede comunque protezione.

La vista di deployment permette di ragionare su **disponibilità e scalabilità**:
- Replicare il server applicativo migliora disponibilità e scalabilità. **Elimina ogni collo di bottiglia? No**: rimuove i limiti di capacità e disponibilità solo al livello applicativo; database, load balancer, session store, message broker e servizi esterni possono restare colli di bottiglia o singoli punti di guasto.
- Conclusione più importante: **la qualità dell'intero sistema dipende dall'intero percorso seguito da una richiesta**. Il sistema è limitato dal componente meno scalabile e può diventare indisponibile per il componente critico meno protetto.

#### Stili di allocazione · [[01-IntroductionOnSoftwareArchitecture.pdf#page=42|p. 42]]–[[01-IntroductionOnSoftwareArchitecture.pdf#page=46|46]]

- Tre stili: **deployment**, **install**, **work assignment**.
- Le viste di deployment sono utili per analizzare **prestazioni, disponibilità, affidabilità e sicurezza**. I tester le usano per capire le dipendenze di runtime, gli integratori per pianificare integrazione e test di integrazione; possono sostenere la **stima dei costi** per scegliere l'hardware.

**Struttura di deployment**
- Mostra come il software è assegnato a elementi hardware di elaborazione e comunicazione. Elementi: elementi software (di solito un processo di una struttura C&C), entità hardware (processori), percorsi di comunicazione. Relazioni: «allocated to» o «deploy» (su quali unità fisiche risiedono gli elementi software) e «migrates-to» se l'allocazione è dinamica.

![[lez01-intro-p44-deployment-structure.png]]
*Vista UML: PC utente Internet, PC Admin Windows, application server Windows con ambiente di esecuzione WebSphere, database server Linux; percorsi «internet» e «intranet» con molteplicità; gli artifact `app-client.jar` e `EnterpriseWebApp.ear` sono distribuiti su nodi diversi.*

**Install view**
- Descrive come il sistema installato è organizzato come struttura di **file e cartelle** e come gli elementi software vi corrispondono. Due tipi di elementi: un componente C&C e un **elemento di configurazione** (file o directory). Due relazioni: **allocated-to** (un componente è allocato a un elemento di configurazione) e **containment** (un elemento di configurazione è contenuto in un altro).

![[lez01-intro-p45-install-view-informale.png]]
*Notazione informale: l'archivio `DukesBankApp.ear` contiene i jar EJB (account, customer, tx) e `web-client.war`; separato `app-client.jar`.*

- Con notazione UML: lo stereotipo `«artifact»` indica un file di qualsiasi tipo; `«manifest»` indica che un componente, una classe o altro artifact è dentro un dato artifact.

![[lez01-intro-p46-install-view-uml.png]]
*Lo stesso contenuto in UML: l'artifact `DukesBankApp.ear` è legato da «manifest» agli artifact jar/war e ai componenti contenuti.*

#### Quali strutture scegliere · [[01-IntroductionOnSoftwareArchitecture.pdf#page=47|p. 47]]

- Nei sistemi **piccoli** si usano spesso meno strutture: non serve documentare il deployment di un sistema su un solo nodo, né la vista di concorrenza se il sistema ha un solo processo. Nei sistemi **grandi** possono servire più viste.
- Le strutture disponibili devono dare intuizioni e leva sugli **attributi di qualità più importanti** del sistema: si scelgono quelle che hanno il ruolo migliore per ottenere quegli attributi.
- I **pattern architetturali** sono composizioni di elementi architetturali che offrono strategie preconfezionate per risolvere problemi comuni di un sistema.

#### Raccomandazioni di processo per buone architetture · [[01-IntroductionOnSoftwareArchitecture.pdf#page=48|p. 48]]

- L'architettura dovrebbe essere il prodotto di **un solo architetto o di un piccolo gruppo** (integrità concettuale e coerenza tecnica), con un forte legame con il team di sviluppo.
- Si basa su una **lista prioritaria di requisiti di attributi di qualità ben specificati**.
- È **documentata** con viste che rispondono alle preoccupazioni dei vari stakeholder; è **valutata** per la capacità di ottenere gli attributi di qualità importanti.
- Si presta all'**implementazione incrementale**: creazione di un sistema «scheletrico», con percorsi di comunicazione esercitati e inizialmente funzionalità minima.

#### Attribute-Driven Design · [[01-IntroductionOnSoftwareArchitecture.pdf#page=49|p. 49]]

![[lez01-intro-p49-attribute-driven-design.png]]
*L'architetto raccoglie i driver architetturali (scopo del progetto, funzionalità primaria, attributi di qualità, vincoli, preoccupazioni architetturali), seleziona e istanzia i concetti di progetto (architetture di riferimento, elementi sviluppati esternamente, …) e produce decisioni di progetto candidate e strutture.*

#### Regole pratiche per buone strutture · [[01-IntroductionOnSoftwareArchitecture.pdf#page=50|p. 50]]

1. L'architettura deve avere **moduli ben definiti** con responsabilità funzionali assegnate secondo i principi di **information hiding** e **separazione delle responsabilità**.
2. Applicare **pattern e tattiche architetturali noti** per ogni attributo di qualità.
3. L'architettura **non deve mai dipendere da una particolare versione** di un prodotto o strumento commerciale.
4. Non aspettarsi una **corrispondenza uno-a-uno tra moduli e componenti**.
5. L'architettura deve avere **pochi e semplici schemi di interazione** tra componenti.
6. …

### 2. Capire gli attributi di qualità

#### Che cos'è un attributo di qualità · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=1|p. 1]]–[[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=2|2]]

- Un **attributo di qualità** (*quality attribute*, QA) è una **proprietà misurabile o verificabile** di un sistema, usata per indicare **quanto bene il sistema soddisfa le esigenze degli stakeholder oltre alla funzione di base**.
- La funzionalità è importante, ma gli attributi di qualità possono essere **ancora più importanti**: molti sistemi vanno riprogettati non per la funzionalità ma perché sono difficili da mantenere, portare o scalare, sono troppo lenti o sono stati compromessi da hacker.

#### Requisiti funzionali e requisiti di qualità · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=3|p. 3]]–[[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=5|5]]

- **Funzionalità** = capacità del sistema di fare il lavoro per cui è stato pensato. Ma **la funzionalità non determina l'architettura**: si decompone l'architettura in moduli e si assegnano le responsabilità in base alla qualità che si vuole ottenere. Si progettano architetture modulari, a strati, a servizi, peer-based… per ottenere caratteristiche di qualità diverse; altrimenti si potrebbe progettare un unico modulo monolitico.
- Requisiti funzionali e di qualità **non vanno definiti separatamente**: domande come «quali vincoli temporali ha questo insieme di responsabilità?», «quali modifiche sono previste?», «quale classe di utenti può eseguirle?» hanno senso e sono azionabili. Se la funzione del software è controllare il comportamento di un motore, come si implementa correttamente senza considerare il comportamento temporale? Meglio parlare di **responsabilità** del software e specificare per ognuna le caratteristiche di qualità richieste.

**Esempio — responsabilità «Verificare se uno studente può prenotare un esame»** (p. 5)

| Attributo | Requisito |
|---|---|
| Prestazioni | il risultato di idoneità è restituito entro 500 ms con carico normale |
| Disponibilità | se il SIS dell'università non è disponibile, il sistema restituisce una risposta controllata entro 2 secondi |
| Sicurezza | solo studenti autenticati e applicazioni amministrative autorizzate possono richiedere l'informazione |
| Modificabilità | una nuova regola di prerequisito si introduce modificando solo Eligibility Checking e i suoi test |
| Testabilità | Eligibility Checking è verificabile senza connettersi al SIS di produzione |

#### Due categorie di attributi e trade-off · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=6|p. 6]]

- Attributi che descrivono una **proprietà del sistema a runtime**: disponibilità, prestazioni, usabilità.
- Attributi che descrivono una **proprietà dello sviluppo** del sistema: modificabilità, testabilità, deployability.
- **Trade-off tra attributi:** il raggiungimento di un attributo ha effetto (positivo o negativo) su un altro. Per ottenere la **portabilità** si isolano le dipendenze del sistema, il che introduce overhead nell'esecuzione e impatta le prestazioni.

#### Tre domande importanti · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=7|p. 7]]

1. Come **esprimere** le qualità che vogliamo che l'architettura abbia?
2. Come **ottenere** quelle qualità con mezzi architetturali?
3. Come **determinare le decisioni di progetto** da prendere rispetto a quelle qualità?

#### 1. Specificare i requisiti di qualità: gli scenari · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=8|p. 8]]–[[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=14|14]]

- Gli attributi di qualità diventano **osservabili tramite scenari**. Un attributo di qualità non ha significato in isolamento: diventa osservabile quando il sistema risponde a un evento rilevante in condizioni specificate, e la risposta attesa deve essere **misurabile**. Esempio: la sicurezza si dimostra quando, di fronte a uno specifico tipo di attacco, il sistema lo sopporta senza perdere dati o funzionalità; la modificabilità, quando a fronte di un tipo di richiesta di modifica lo sforzo resta entro limiti ragionevoli.
- Gli **scenari di qualità hanno sei parti**; nella forma Given–When–Then: *dati un ambiente e un artefatto, quando una sorgente genera uno stimolo, allora il sistema produce una risposta misurabile.*

| Parte | Significato |
|---|---|
| **Stimolo** (stimulus) | evento che arriva al sistema o al progetto (evento, attacco, richiesta utente…) |
| **Sorgente dello stimolo** (source) | entità (umana, un sistema informatico, altro attore) che ha generato lo stimolo |
| **Risposta** (response) | attività che avviene come risultato dello stimolo: sono le responsabilità che il sistema (qualità di runtime) o gli sviluppatori (qualità di sviluppo) devono svolgere; è ciò che l'architetto si impegna a soddisfare |
| **Misura della risposta** (response measure) | usata per misurare la risposta e verificare lo scenario (per le prestazioni latenza o throughput; per la modificabilità il lavoro o il tempo per realizzare, testare e rilasciare la modifica) |
| **Ambiente** (environment) | circostanze in cui si svolge lo scenario: sistema in esecuzione (stato normale o anomalo) o non in esecuzione (sviluppo, test, aggiornamento dei dati, ricarica) |
| **Artefatto** (artifact) | bersaglio dello stimolo: il sistema o il progetto, una collezione di sistemi, l'intero sistema o una o più sue parti (un guasto o una richiesta di modifica può riguardare solo una piccola parte; la modifica dell'interfaccia utente può avere tempi più rapidi di quella del middleware) |

![[lez01b-qa-p9-parti-scenario.png]]
*Le sei parti dello scenario e il loro collegamento.*

- Uno **scenario generale** è indipendente dal sistema e vale per qualunque sistema; uno **scenario concreto** è specifico del sistema considerato. Esempio di scenario generale di disponibilità (p. 13):

![[lez01b-qa-p13-scenario-generale-availability.png]]
*Scenario generale di disponibilità, con le sei parti compilate in modo indipendente dal sistema.*

**Scenario concreto di prestazioni (Exam Booking)** · p. 14

| Parte | Valore |
|---|---|
| Sorgente | studenti |
| Stimolo | 5.000 richieste di prenotazione arrivano in un minuto |
| Ambiente | apertura delle iscrizioni |
| Artefatto | sottosistema di prenotazione |
| Risposta | validare e registrare ogni prenotazione ammissibile |
| Misura della risposta | il 95 % completato entro 2 secondi e tutte le richieste entro 5 secondi |

La misura della risposta rende il requisito verificabile e supporta la valutazione architetturale.

#### Come valutare le prestazioni · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=15|p. 15]]

- In progettazione, per ogni elemento si valutano: tempo di elaborazione; numero di richieste gestibili; numero e costo delle comunicazioni; accessi al database; contesa sulle risorse; lunghezza delle code; possibilità di elaborazione parallela.
- Approcci: **modelli di prestazioni, modelli a code, simulazioni, prototipi architetturali, benchmark dei componenti critici, analisi dei colli di bottiglia**.
- Esempio: replicare il server applicativo può non bastare se il database riesce a completare solo **30 transazioni al secondo**.
- Le prestazioni si valutano soprattutto con le **viste C&C**, integrate dalle viste di deployment e concorrenza quando allocazione delle risorse ed esecuzione parallela influiscono.

#### Scenario concreto di modificabilità · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=16|p. 16]]–[[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=19|19]]

**Introdurre una nuova regola di prerequisito**

| Elemento | Given–When–Then | Scenario concreto |
|---|---|---|
| Sorgente | When | amministrazione dell'università |
| Stimolo | When | richiede una nuova regola di prerequisito |
| Ambiente | Given | sistema in sviluppo; test automatici disponibili |
| Artefatto | Given | modulo Eligibility Checking e la sua suite di test |
| Risposta | Then | gli sviluppatori implementano, testano e rilasciano la nuova regola |
| Misura della risposta | Then | completato in due giorni lavorativi; modifiche limitate a Eligibility Checking, configurazione e test correlati |

Lo scenario rende la modificabilità verificabile vincolando sia lo sforzo sia l'ambito della modifica.

**Valutazione a livello architetturale della modificabilità** (p. 17): si applica una **analisi dell'impatto della modifica** sulle viste di modulo: si identifica lo stimolo di modifica; si individua il modulo responsabile; si tracciano le dipendenze da altri elementi; si determinano gli artefatti interessati; si stima lo sforzo; si valutano gli effetti su test e deployment.

**Vista di moduli dell'Exam Booking System** (p. 18): le frecce rappresentano la relazione uses (Authentication, Exam Catalog, Booking, Eligibility Checking, Notifications, Administration); una modifica a una regola di ammissione dovrebbe riguardare principalmente Eligibility Checking, non Booking.

**Valutazione empirica della modificabilità** (p. 19): quando esiste il sistema o un prototipo si può condurre un **esercizio di modifica**: la modifica è assegnata a uno o più sviluppatori; si registra il tempo dall'inizio al completamento; si contano gli artefatti modificati; si eseguono i test; si verifica che non siano state introdotte regressioni.

#### 2. Ottenere le qualità: tattiche e pattern · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=20|p. 20]]–[[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=22|22]]

- Una **tattica** è una decisione di progetto che influenza il raggiungimento di una risposta di un attributo di qualità. Esempi: *Schedule Resources* è una tattica di prestazioni; *Use an Intermediary* è una tattica di modificabilità.
- Un **pattern architetturale** descrive un problema di progetto ricorrente che si presenta in contesti specifici e presenta una soluzione architetturale ben collaudata. Esempio: il pattern a strati. I pattern architetturali spesso comprendono **più tattiche** (per esempio Layers o Microservices).
- **Esempio: il pattern Layers** può incorporare più tattiche: separare le responsabilità assegnandole a strati distinti; restringere le dipendenze controllando quali strati comunicano; usare un intermediario (uno strato può isolare lo strato superiore dalle tecnologie sottostanti); astrarre i servizi comuni (ogni strato espone servizi tramite interfacce definite). Queste decisioni possono migliorare **modificabilità, testabilità e portabilità**, ma possono introdurre **latenza e complessità** aggiuntive.

#### Tattiche di prestazioni per l'esempio · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=23|p. 23]]–[[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=24|24]]

| Tattica | Come | Effetto | Trade-off |
|---|---|---|---|
| **Replicare le risorse** | più istanze del server applicativo, richieste distribuite da un load balancer | aumenta le richieste servite contemporaneamente | richiede gestione delle sessioni, sincronizzazione e controllo degli accessi concorrenti ai dati |
| **Introdurre una cache** (per il calendario degli esami) | | riduce latenza e carico sul database | i dati in cache possono essere obsoleti |
| **Elaborare i compiti in modo asincrono** | registrare subito la prenotazione e delegare l'invio della conferma a una coda: Booking → Message Queue → Notification | riduce il tempo di risposta percepito dallo studente | le notifiche possono essere ritardate; messaggi persi o duplicati vanno gestiti |

![[lez01b-qa-p24-tattiche-performance.png]]
*Vista C&C con le tre tattiche: replicare le risorse, introdurre una cache, task asincroni.*

#### Tattiche di disponibilità · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=25|p. 25]]–[[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=26|26]]

- **Rilevare i guasti**: il load balancer esegue controlli periodici (health check) sulle istanze applicative.
- **Reindirizzare le richieste**: se un'istanza non risponde, il load balancer la toglie temporaneamente dal pool e instrada il traffico alle altre.
- **Introdurre ridondanza**: replicare server applicativi, database o message broker.

![[lez01b-qa-p26-availability-prima-dopo-guasto.png]]
*Due configurazioni, prima (BEFORE) e dopo (AFTER) un guasto del server.*

#### Tattiche di sicurezza · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=27|p. 27]]–[[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=28|28]]

| Tattica | Come | Effetto |
|---|---|---|
| **Autenticare gli utenti** | verificare l'identità dello studente con il sistema di autenticazione dell'università | impedisce l'accesso anonimo alle funzioni di prenotazione |
| **Autorizzare le operazioni** | controlli basati sui ruoli: gli studenti gestiscono solo le proprie prenotazioni; i docenti vedono l'elenco degli iscritti alle loro sessioni; gli amministratori configurano sessioni e regole | limita le azioni permesse a ciascun utente |
| **Proteggere i dati in trasmissione** | TLS tra browser, server applicativo e sistemi esterni | protegge riservatezza e integrità dei dati trasmessi |
| **Registrare gli eventi rilevanti** (log) | chi ha creato o annullato una prenotazione e quando | consente audit e rilevazione di comportamenti anomali; **trade-off:** i log vanno protetti perché possono contenere dati personali |

![[lez01b-qa-p28-tattiche-security.png]]
*Dove si applicano le tattiche: ① TLS tra browser e server applicativo; ② l'applicazione delega l'identificazione al sistema di autenticazione dell'università; ③ RBAC (Role Based Access Control) verifica ruolo, risorsa e operazione richiesta; ④ gli eventi rilevanti vanno in un audit log protetto; ⑤ TLS anche per le comunicazioni con i sistemi esterni.*

#### Tattiche di modificabilità · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=29|p. 29]]–[[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=30|30]]

| Tattica | Dove | Effetto |
|---|---|---|
| **Localizzare le modifiche** | le regole di ammissione stanno in Eligibility Checking | una modifica ai prerequisiti non deve riguardare Booking |
| **Nascondere le informazioni** | gli altri moduli accedono ai dati degli studenti tramite Student Records | formato, provenienza e metodi di accesso restano nascosti |
| **Usare un intermediario** | l'adapter SIS media l'accesso al sistema informativo dell'università | sostituire o modificare l'API del SIS riguarda soprattutto l'adapter |
| **Posticipare il binding** | le regole sono caricate da configurazione a runtime | alcune variazioni si introducono senza modificare e ricompilare l'applicazione |

### 3. Perché l'architettura software è importante · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=31|p. 31]]

Ci sono decine di motivazioni; se ne esaminano alcune.

#### 3.1 L'architettura inibisce o abilita gli attributi di qualità · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=32|p. 32]]–[[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=33|33]]

- **Alte prestazioni** → gestire il comportamento temporale degli elementi, l'uso di risorse condivise, la frequenza e il volume delle comunicazioni tra elementi.
- **Modificabilità** → assegnare le responsabilità agli elementi e limitare le loro interazioni, in modo che una modifica riguardi pochi moduli.
- **Alta sicurezza** → gestire e proteggere le comunicazioni tra elementi; controllare quali elementi possono accedere a quali informazioni; possono servire elementi specializzati anti-intrusione.
- **Scalabilità delle prestazioni** → localizzare l'uso di risorse per facilitare l'introduzione di sostituzioni a maggiore capacità; evitare di fissare nel codice ipotesi o limiti sulle risorse.
- **Riuso degli elementi** → limitare l'accoppiamento tra elementi, così che un elemento estratto non porti con sé troppi legami con il suo ambiente attuale.
- La progettazione architetturale è importante, ma anche le decisioni di progettazione e implementazione influiscono sulla qualità finale.

#### 3.2 L'architettura permette di prevedere gli attributi di qualità · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=34|p. 34]]

- Si possono fare **previsioni di qualità** su un sistema in base alla sola valutazione della sua architettura. Se si sa che certi tipi di decisioni architetturali portano a certi attributi, si possono prendere quelle decisioni e aspettarsi gli attributi associati; esaminando un'architettura si può stabilire se quelle decisioni sono state prese e prevedere con fiducia le qualità.

#### 3.3 Comunicazione tra stakeholder · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=35|p. 35]]

- L'architettura è un'**astrazione comune** del sistema che gli stakeholder usano come base per creare comprensione reciproca, negoziare, formare consenso e comunicare tra loro.

#### 3.4 Decisioni di progetto precoci · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=36|p. 36]]

- Un'architettura è anche un **insieme di decisioni precoci**; cambiarle causa un effetto a catena sulle decisioni da cambiare di conseguenza.
- Esempi: il sistema girerà su un processore o sarà distribuito? il software sarà a strati (quanti, con quali compiti)? i componenti comunicano in modo sincrono o asincrono? interagiscono trasferendo controllo, dati o entrambi? le informazioni saranno cifrate? quale sistema operativo? quale protocollo di comunicazione?

#### 3.5 Vincoli sull'implementazione · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=37|p. 37]]

- L'implementazione deve conformarsi alle decisioni dell'architettura: avere l'insieme di elementi prescritto; gli elementi devono interagire nel modo prescritto; ogni elemento deve assolvere la propria responsabilità verso gli altri. Ognuna di queste prescrizioni è un **vincolo per l'implementatore**.

#### 3.6 Influenza sulla struttura organizzativa · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=38|p. 38]]

- La **decomposizione** del sistema è di solito la base della *work breakdown structure*, che determina: unità di pianificazione, schedulazione e budget; canali di comunicazione tra team; controllo di configurazione e organizzazione del file system; piani e procedure di integrazione e test; organizzazione della intranet di progetto e collocazione dei team. I team comunicano tra loro in termini di specifiche di interfaccia dei loro elementi.

#### 3.7 Abilitare lo sviluppo incrementale · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=39|p. 39]]

- L'architettura può essere la base dello sviluppo incrementale. Il primo incremento può essere un **sistema scheletrico** con parte dell'infrastruttura ma poca funzionalità applicativa (come gli elementi si inizializzano, comunicano, condividono dati, accedono alle risorse, segnalano errori, registrano attività). Negli incrementi successivi si progetta e costruisce un po' di infrastruttura per supportare un po' di funzionalità end-to-end, e si ripete fino alla fine.
- Il sistema è eseguibile presto nel ciclo di vita; i problemi di prestazioni (e altri) emergono presto.

#### 3.8 Modello trasferibile e riusabile · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=40|p. 40]]

- Il riuso di architetture offre opportunità per sistemi con requisiti simili; quando le decisioni sono riusate in più sistemi, si trasferiscono anche tutte le conseguenze delle decisioni precoci.
- Una **linea di prodotto** o famiglia è un insieme di sistemi costruiti con lo stesso insieme di risorse condivise (componenti software, documenti dei requisiti, casi di test…). L'architettura definisce cosa è fisso per tutti i membri e cosa varia.

#### 3.9 Incorporare elementi sviluppati in modo indipendente · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=41|p. 41]]–[[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=43|43]]

- Lo sviluppo basato sull'architettura si concentra spesso sul comporre elementi sviluppati separatamente. L'architettura definisce: i componenti incorporabili nel sistema; come interagiscono con l'ambiente; come ricevono e cedono il controllo; quali dati consumano e producono; come accedono ai dati; quali protocolli usano per comunicare e condividere risorse.
- Vantaggi: **minor time to market, maggiore affidabilità, costo inferiore, flessibilità**.
- Esempio: l'architettura del progetto **ENACTEST** (p. 42).

![[lez01b-qa-p42-enactest.png]]
*Architettura del progetto ENACTEST (esempio di architettura a componenti).*

- **Sistemi aperti e architetture a standard aperti.** Un **sistema aperto** definisce un insieme di standard per gli elementi software: come si comportano, interagiscono, condividono dati. Lo scopo è consentire a **molti fornitori diversi** di produrre elementi. I sistemi aperti sono abilitati da un'architettura che definisce elementi e interazioni. Esempio: lo standard architetturale aperto **AUTOSAR** (p. 43).

![[lez01b-qa-p43-autosar.png]]
*Architettura aperta AUTOSAR.*

#### 3.10 Restringere il vocabolario delle alternative di progetto · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=44|p. 44]]

- Progettando un'architettura è importante **restringere il vocabolario di progetto a soluzioni collaudate**: pattern, tattiche o elementi off-the-shelf.
- Benefici: maggior riuso; progetti più regolari e semplici, più facili da capire e comunicare, con esiti più prevedibili; analisi più facile e con più fiducia; tempo di selezione più breve; maggiore interoperabilità.

#### 3.11 Una base per la formazione · [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=45|p. 45]]

- L'architettura può essere la prima introduzione al sistema per i nuovi membri del progetto: **viste di modulo** per mostrare la struttura del progetto; **viste C&C** per spiegare come il sistema dovrebbe funzionare e svolgere il suo compito; **viste di allocazione** per mostrare dove la parte assegnata si colloca nell'ambiente di sviluppo o di deployment.

*Approfondimenti nel wiki: [[architettura-software]], [[strutture-e-viste]], [[strutture-di-modulo]], [[strutture-componenti-e-connettori]], [[strutture-di-allocazione]], [[uml]], [[exam-booking-system]], [[attributi-di-qualita]], [[scenari-di-qualita]], [[valutazione-attributi-di-qualita]], [[tattiche-architetturali]], [[importanza-architettura-software]], [[buone-pratiche-architetturali]], [[attribute-driven-design]], [[layered]], [[client-server]], [[microservices]], [[enactest]], [[autosar]]*

## Lezione 2 — Attributi di qualità: disponibilità

*Fonte: 02-Availability.pdf (23 pagine). Cap. 4–13 di Bass, Clements, Kazman, «Software Architecture in Practice»: definizione, scenari per specificare, tattiche e pattern; esempio guida: l'Exam Booking System.*

### Definizioni · [[02-Availability.pdf#page=3|p. 3]]–[[02-Availability.pdf#page=4|4]]

- **Disponibilità** (*availability*) = grado in cui un sistema è **operativo e accessibile quando serve**. Riguarda anche la capacità del sistema di: **prevenire** che i guasti causino malfunzionamenti osservabili dall'esterno; **continuare a fornire il servizio** nonostante alcuni guasti; **recuperare e ripristinare** il servizio dopo un malfunzionamento.
- Obiettivo: assicurare che l'**interruzione cumulativa del servizio non superi un valore accettabile in un intervallo di tempo specificato**.
- **Failure** (malfunzionamento): comportamento scorretto del sistema, osservabile dall'esterno.
- **Fault** (guasto): la causa interna (o esterna) di un failure, per esempio un difetto software o il crash di un server.
- **Error** (errore): stato interno scorretto del sistema, causato da un fault.
- La disponibilità dipende soprattutto da: **assenza di guasti** (ridurre guasti e malfunzionamenti), **tolleranza ai guasti** (continuare a operare nonostante i guasti), **recuperabilità** (ripristinare servizio e dati dopo un malfunzionamento).

### Catena fault → error → failure · [[02-Availability.pdf#page=5|p. 5]]

![[lez02-av-p5-catena-fault-error-failure.png]]
*Schema: Fault → (attivazione) → Error → (propagazione) → Failure; se l'errore è rilevato, contenuto o mascherato non c'è nessun malfunzionamento osservabile. Esempio del Booking System: fault «University SIS non disponibile» → error «i dati dello studente non sono disponibili nell'Exam Booking System» → (se non rilevato né gestito) failure «la richiesta di ammissibilità restituisce un risultato scorretto o nessuno».*

### Misure tipiche della disponibilità · [[02-Availability.pdf#page=6|p. 6]]

- La disponibilità si può misurare come **probabilità** che il sistema fornisca i servizi specificati entro i limiti richiesti in un intervallo di tempo.
- Espressione nota: $\text{Availability} \approx \dfrac{MTBF}{MTBF + MTTR}$, con **MTBF** = *Mean Time Between Failures* (tempo medio tra i guasti) e **MTTR** = *Mean Time to Repair* (tempo medio di riparazione).
- La disponibilità attesa di un sistema o servizio si esprime spesso come **SLA** (*Service Level Agreement*), che specifica il livello di disponibilità garantito e, di solito, le penali per il fornitore in caso di violazione.

### Esempio di requisiti di disponibilità · [[02-Availability.pdf#page=7|p. 7]]

Percentuale di tempo in cui il sistema è disponibile rispetto al tempo in cui è in servizio, con il downtime corrispondente:

| Disponibilità | Downtime su 90 giorni | Downtime su un anno |
|---|---|---|
| 99,0 % | 21 h 36 min | 3 giorni 15,6 h |
| 99,9 % | 2 h 10 min | 8 h 0 min 46 s (sulla slide) |
| 99,99 % | 12 min 58 s | 52 min 34 s |
| 99,999 % | 1 min 18 s | 5 min 15 s |
| 99,9999 % | 8 s | 32 s |

> ⚠️ Refuso della slide: 0,1 % di un anno di 8.760 h dà $8{,}76\ \text{h} = 8\ \text{h}\ 45\ \text{min}\ 36\ \text{s}$, non 8 h 0 min 46 s.

### Scenario di disponibilità · [[02-Availability.pdf#page=8|p. 8]]–[[02-Availability.pdf#page=9|9]]

- Esempio: un server di una server farm si guasta durante il funzionamento normale, e il sistema informa l'operatore e continua a operare **senza downtime**.
- **Scenario per l'Exam Booking System**: durante un periodo di prenotazione, un application server smette di rispondere; il load balancer rileva il guasto, toglie l'istanza dal pool e reindirizza le nuove richieste. **Misura:** rilevazione entro 30 s, ripristino entro 60 s, almeno il 99 % delle richieste completate, nessuna prenotazione confermata persa.

![[lez02-av-p9-scenario-exam-booking.png]]
*Scenario dell'Exam Booking System (riquadro) accanto allo schema della server farm.*

### Scenari generali di disponibilità · [[02-Availability.pdf#page=10|p. 10]]–[[02-Availability.pdf#page=12|12]]

Tabelle del libro, a tre colonne (parte dello scenario, descrizione, valori possibili): sorgente, stimolo, artefatto, ambiente (p. 10); risposta (p. 11); misura della risposta (p. 12).

![[lez02-av-p10-scenario-generale-1.png]]
![[lez02-av-p11-scenario-generale-2.png]]
![[lez02-av-p12-scenario-generale-3.png]]

### Tattiche di disponibilità · [[02-Availability.pdf#page=13|p. 13]]–[[02-Availability.pdf#page=14|14]]

- Un failure si verifica quando il sistema non fornisce più un servizio coerente con la specifica e ciò è osservabile dagli attori. Un fault (o una combinazione di fault) ha il potenziale per causarlo.
- Le **tattiche di disponibilità** servono a far sì che il sistema **prevenga o sopporti i guasti** in modo che il servizio resti conforme alla specifica: evitano che i guasti diventino malfunzionamenti, o almeno ne limitano gli effetti e rendono possibile la riparazione.
- Spesso sono fornite da un'infrastruttura software (per esempio un middleware); il lavoro dell'architetto può essere **scegliere e valutare** (non implementare) le tattiche giuste e la loro combinazione.

![[lez02-av-p14-albero-tattiche-availability.png]]
*Albero delle tattiche (dal libro): rilevare i guasti (monitor, ping/echo, heartbeat, timestamp, condition monitoring, sanity checking, voting, exception detection, self-test); recuperare dai guasti, preparazione e riparazione (redundant spare, rollback, exception handling, software upgrade, retry, ignore faulty behavior, graceful degradation, reconfiguration) e reintroduzione (shadow, state resynchronization, escalating restart, nonstop forwarding); prevenire i guasti (removal from service, transactions, predictive model, exception prevention, increase competence set).*

### Rilevare i guasti · [[02-Availability.pdf#page=15|p. 15]]

| Tattica | Significato | Esempio |
|---|---|---|
| **Monitor** | raccogliere indicatori di stato e di risorse | monitorare istanze applicative, connessioni al database, lunghezza della coda |
| **Ping / Echo** | verificare raggiungibilità e ritardo | il load balancer interroga ogni application server |
| **Heartbeat** | scambiarsi messaggi di vita | il broker controlla se i consumer di notifiche sono vivi (reset di un watchdog timer) |
| **Condition monitoring** | verificare le condizioni operative di un processo e le ipotesi di progetto | |
| **Voting** | confrontare i risultati di componenti ridondanti | |
| **Replication** | previene i guasti hardware, non quelli software | |
| **Functional redundancy** | più componenti che implementano la stessa funzione con diversità per progetto | |
| **Exception detection** | rilevare una condizione che altera il normale flusso di esecuzione | |

### Recuperare dai guasti · [[02-Availability.pdf#page=16|p. 16]]

| Tattica | Significato | Esempio |
|---|---|---|
| **Redundant spare** | un duplicato subentra | un secondo application server riceve le richieste reindirizzate |
| **Retry** | ripetere un'operazione dopo un guasto transitorio | ripetere con politica limitata una richiesta al SIS andata in timeout |
| **Rollback** | riportare dati o calcolo a uno stato corretto noto | |
| **Exception handling** | contenere l'errore e restituire una risposta controllata (crash, codici di errore o classi di eccezione) | |
| **Graceful degradation** | mantenere le funzioni più critiche, abbandonando le meno critiche | preservare la prenotazione ritardando notifiche o report |

### Prevenire i guasti · [[02-Availability.pdf#page=17|p. 17]]

- **Removal from service**: mettere un componente offline prima che guasti latenti (memory leak, frammentazione…) incidano sui servizi. Esempio: riavviare un'istanza applicativa alla volta per liberare le risorse.
- **Transactions**: sfruttare la semantica transazionale per l'alta disponibilità (protocollo *two-phase commit*). Esempio: riservare un posto e registrare la prenotazione in un'unica transazione atomica.
- **Increase the competence set**: trattare più condizioni anomale come casi normali. Esempio: Eligibility Checking distingue «non idoneo» da «SIS non disponibile».

### Pattern di ridondanza · [[02-Availability.pdf#page=18|p. 18]]

| Pattern | Descrizione | Costo / tempo di recupero |
|---|---|---|
| **Redundancy attiva (hot spare)** | le repliche elaborano lo stesso input e mantengono lo stato sincronizzato | failover rapido; costi di risorse e sincronizzazione alti |
| **Redundancy passiva (warm spare)** | il componente attivo elabora le richieste e aggiorna periodicamente uno standby | bilancia tempo di recupero e costo |
| **Cold spare** | lo standby parte solo dopo il guasto | costa meno ma ha il tempo di recupero più lungo (poco adatto a requisiti di alta disponibilità) |

- Nell'esempio, i server applicativi replicati dietro il load balancer si comportano come repliche attive quando servono entrambi traffico; un database standby è di solito warm o hot, a seconda della replica e della politica di failover.

![[lez02-av-p18-pattern-ridondanza.png]]
*In alto un sistema Active-Active (richieste a Node 1 e Node 2, entrambi attivi); in basso un sistema Active-Passive (richieste a Node 1, con failover verso Node 2 passivo).*

### Circuit Breaker · [[02-Availability.pdf#page=19|p. 19]]

- Il **circuit breaker** impedisce chiamate ripetute a un servizio che non risponde: dopo un numero definito di guasti o timeout **apre il circuito**, così le richieste successive falliscono subito o ricevono una risposta di ripiego (*fallback*).
- Evita l'esaurimento delle risorse e i guasti a cascata, lasciando al servizio guasto il tempo di riprendersi.
- In Java Spring Boot si può usare la libreria **Resilience4j**, aggiungendo la dipendenza Maven e proteggendo la chiamata con l'API specifica:

```xml
<dependency>
  <groupId>org.springframework.cloud</groupId>
  <artifactId>spring-cloud-starter-circuitbreaker-resilience4j</artifactId>
</dependency>
```

### Dallo scenario alle decisioni architetturali · [[02-Availability.pdf#page=20|p. 20]]–[[02-Availability.pdf#page=22|22]]

Lo scenario di p. 20 è quello dell'Exam Booking System (p. 9). Tabella di p. 21:

| Guasto / disturbo | Rilevazione | Risposta architetturale | Misura della risposta |
|---|---|---|---|
| Un application server smette di rispondere | health check del load balancer | rimuovere l'istanza e reindirizzare le richieste | rilevazione ≤ 30 s; ripristino ≤ 60 s |
| SIS dell'università non disponibile | timeout e probe falliti | retry limitato; fallire in modo sicuro; riportare l'idoneità come non disponibile | nessuna decisione errata sull'idoneità |
| Il database primario si guasta | replica e monitoraggio del database (cluster monitoring) | promuovere il database standby; riconnettere le istanze applicative allo standby promosso | **RTO ≤ 5 min; RPO ≤ 1 min** |

**RTO** = *Recovery Time Objective*; **RPO** = *Recovery Point Objective*. Domanda di discussione: quali **singoli punti di guasto** restano dopo aver replicato gli application server?

![[lez02-av-p22-configurazioni-prima-dopo-guasto.png]]
*Prima del guasto: due application server con health check, DB primario replicato su standby, due message broker replicati. Dopo: l'Application Server 1 è FAILED, rimosso dal pool, e le richieste vanno al 2.*

### Dalle tattiche alle tecnologie · [[02-Availability.pdf#page=23|p. 23]]

| Problema | Tattiche o pattern | Tecnologie utilizzabili |
|---|---|---|
| SIS lento o indisponibile | timeout, bounded retry, circuit breaker, fallback | Spring Boot; WebClient o RestClient; Resilience4j TimeLimiter, Retry, CircuitBreaker; WireMock o Toxiproxy per simulare ritardi ed errori |
| Guasto del database primario | active–passive redundancy, replication, health monitoring, failover | PostgreSQL streaming replication; Patroni; etcd o Consul; HAProxy; Docker Compose |
| Sovraccarico del Booking Service | load balancing, horizontal scaling, health-based routing | più istanze Spring Boot; Docker; NGINX, HAProxy o Traefik; in alternativa Kubernetes (Deployment, Service, HPA); k6 o JMeter |
| Notification Service indisponibile | messaggistica asincrona, queue-based load leveling, store-and-forward | RabbitMQ; Spring AMQP; RabbitTemplate; @RabbitListener; durable queue e dead-letter queue |
| Analytics esaurisce le risorse condivise | bulkhead, isolamento delle risorse, limite di concorrenza | Resilience4j Bulkhead o ThreadPoolBulkhead; executor Java separati; HikariCP con pool distinti; limiti di risorse Docker o Kubernetes |
| Servizio secondario non disponibile | graceful degradation, fallback, cached response | Resilience4j CircuitBreaker; fallback Spring; Caffeine o Redis |
| Richieste duplicate | idempotenza, duplicate detection, unicità transazionale | Spring Boot; chiave di idempotenza; tabella PostgreSQL per le richieste elaborate; vincoli UNIQUE; eventuale transactional outbox |
| Guasti difficili da individuare e diagnosticare | health monitoring, heartbeat, logging, metriche, distributed tracing | Spring Boot Actuator; Micrometer; Prometheus; Grafana; OpenTelemetry; Jaeger o Grafana Tempo |

*La slide assegna una riga a ciascun gruppo del corso, con un esperimento da svolgere (non riportato qui).*

*Approfondimenti nel wiki: [[availability]], [[tattiche-availability]], [[circuit-breaker]]*

## Lezione 3 — Attributi di qualità: modificabilità

*Fonte: 03-Modifiability.pdf (33 pagine). Cap. 4–13 di Bass, Clements, Kazman, «Software Architecture in Practice»; esempio guida: l'Exam Booking System.*

### I cambiamenti nei sistemi software · [[03-Modifiability.pdf#page=3|p. 3]]

- **La maggior parte dei costi di un sistema software si genera dopo il rilascio.**
- I cambiamenti avvengono per: aggiungere nuove funzionalità, modificare o ritirare le vecchie; correggere difetti, rafforzare la sicurezza, migliorare le prestazioni; migliorare l'esperienza dell'utente; adottare nuove tecnologie, piattaforme, protocolli, standard; far lavorare insieme sistemi mai progettati per farlo.
- La **modificabilità** riguarda il cambiamento; l'interesse è **ridurre costo e rischio** delle modifiche.

### Quattro domande per pianificare la modificabilità · [[03-Modifiability.pdf#page=4|p. 4]]–[[03-Modifiability.pdf#page=6|6]]

1. **Cosa può cambiare?** funzioni del sistema, piattaforma, ambiente, qualità, capacità.
2. **Qual è la probabilità del cambiamento?** quali cambiamenti sono probabili e quindi quali saranno supportati e quali no.
3. **Quando viene fatto il cambiamento e chi lo fa?** *Quando*: nell'implementazione (modificando il codice sorgente); in compilazione (switch di compilazione); nel build (scelta delle librerie); nella configurazione (impostazione di parametri); a esecuzione (parametri, plug-in, allocazione all'hardware…). *Chi*: uno sviluppatore, un utente finale, un amministratore di sistema o il sistema stesso (se è in grado di imparare ad adattarsi).
4. **Qual è il costo del cambiamento?** (vedi sotto).

**Esempio del Booking System — quando si modifica e chi lo fa** (p. 6)

| Fase | Cosa cambia | Esempio |
|---|---|---|
| **Implementazione** | codice sorgente | uno sviluppatore cambia la logica che verifica se uno studente può prenotare un esame |
| **Compilazione** | una scelta fissata alla compilazione | un'opzione di compilazione (switch) abilita una versione di una funzione; cambiarla richiede ricompilazione |
| **Build** | i componenti inclusi nell'applicazione | il team sceglie quale libreria connettore SIS includere; cambiarla richiede un nuovo build |
| **Configurazione** | valori impostati prima dell'avvio | un amministratore imposta l'endpoint del SIS o un limite di prenotazioni in un file di configurazione |
| **Esecuzione** | valori o componenti cambiati mentre l'applicazione gira | un amministratore aggiorna una regola di prenotazione da un'interfaccia di gestione, o il sistema stesso carica un plug-in supportato |

### Qual è il costo del cambiamento · [[03-Modifiability.pdf#page=7|p. 7]]–[[03-Modifiability.pdf#page=9|9]]

Due tipi di costo: **il costo di introdurre i meccanismi** che rendono il sistema più modificabile e **il costo di fare la modifica usando i meccanismi**. Se il codice è modificato spesso, senza introdurre un meccanismo architetturale e accumulando modifiche una sopra l'altra, si genera in genere un **debito tecnico** consistente.

- **Nessuna previsione per un cambiamento futuro** → il costo iniziale è zero. Quando il cambiamento viene richiesto si modifica il codice e si rivalida il sistema (il costo si paga in quel momento). Esempio: se il numero massimo di prenotazioni di Booking è fissato nel codice, alzare il limite richiede modifica del codice, test e un nuovo deployment.
- All'estremo opposto, un sistema può **rilevare cambiamenti nell'ambiente e adattarsi automaticamente**: ogni adattamento non richiede modifiche manuali, ma progettare, realizzare e collaudare quella capacità può costare molto. Esempio: Booking rileva un aumento delle richieste e regola automaticamente il numero di istanze; non serve uno sviluppatore, ma il meccanismo di monitoraggio e scalatura va costruito e collaudato prima.

![[lez03-mo-p8-quando-si-paga-il-costo.png]]
*Due linee temporali: senza previsione il costo si paga quando arriva il cambiamento; con adattamento automatico il costo si paga in anticipo.*

### Sapori specifici di modificabilità · [[03-Modifiability.pdf#page=10|p. 10]]–[[03-Modifiability.pdf#page=14|14]]

Oltre ai cambiamenti dei requisiti funzionali, un sistema può dover accomodare cambiamenti di carico di lavoro, varianti di prodotto, piattaforme di esecuzione o posizione dei servizi: **scalabilità, variabilità, portabilità, indipendenza dalla posizione**.

![[lez03-mo-p10-varianti-modificabilita.png]]
*Quattro riquadri: Scalability, Variability, Portability, Location Independence.*

- **Scalabilità** (*scalability*): capacità di accomodare un carico crescente **aggiungendo risorse**. **Scalatura orizzontale** (*scale out*): aggiungere istanze (per esempio un altro server in un cluster). **Scalatura verticale** (*scale up*): aumentare le risorse di una istanza (CPU, memoria). In cloud, la capacità di aggiungere o togliere risorse al variare della domanda si chiama **elasticità**. Esempio: Booking aggiunge istanze applicative per gestire un picco di prenotazioni.
- **Variabilità** (*variability*): capacità di produrre **varianti pianificate** di un sistema da software e artefatti condivisi. È centrale in una **linea di prodotto software**: una famiglia di prodotti con un nucleo comune ma funzionalità selezionate diverse. Esempio: una linea di prodotto Booking ha un nucleo di prenotazione comune; ogni università sceglie le proprie regole di idoneità e opzioni di notifica per creare la propria variante.
- **Portabilità** (*portability*): facilità di adattare il software a una piattaforma diversa. Migliora quando le dipendenze dalla piattaforma sono minimizzate o **isolate dietro interfacce chiare**; scrivere il software per una macchina virtuale come la JVM riduce la dipendenza dal sistema operativo. Esempio: Booking genera ricevute; usando le API di file indipendenti dalla piattaforma di Java e un percorso di archiviazione configurabile può passare da Linux a Windows senza cambiare la logica di prenotazione.
- **Indipendenza dalla posizione** (*location independence*): permette a componenti distribuiti di comunicare **senza conoscere in anticipo l'indirizzo fisico** l'uno dell'altro. Un client usa un **nome logico** di servizio e scopre l'indirizzo corrente a runtime; un servizio può spostarsi su un altro server con poco o nessun cambiamento per i client. Richiede **indirezione** tra identità logica e posizione fisica, fornita da DNS, service discovery o un intermediario come un load balancer. Esempio: Booking chiama il SIS tramite un nome di servizio; se il SIS cambia server, un registry o il DNS risolve il nome nel nuovo indirizzo.

### Scenario generale di modificabilità · [[03-Modifiability.pdf#page=15|p. 15]]–[[03-Modifiability.pdf#page=17|17]]

![[lez03-mo-p15-scenario-generale-1.png]]
![[lez03-mo-p16-scenario-generale-2.png]]
*Tabella dello scenario generale (parte, descrizione, valori possibili), dal libro.*

**Scenario concreto d'esempio:** uno sviluppatore vuole cambiare l'interfaccia utente; la modifica sarà fatta nel codice **in fase di progettazione**, richiederà **meno di tre ore** per essere fatta e collaudata e **non ci saranno effetti collaterali**.

![[lez03-mo-p17-scenario-concreto-ui.png]]
*Le sei parti dello scenario compilate per il caso dell'interfaccia utente.*

### Tattiche per la modificabilità · [[03-Modifiability.pdf#page=18|p. 18]]

![[lez03-mo-p18-albero-tattiche-modifiability.png]]
*Albero delle tattiche (dal libro): aumentare la coesione, ridurre l'accoppiamento, posticipare il binding.*

### Aumentare la coesione · [[03-Modifiability.pdf#page=19|p. 19]]

- **Split module**: dividere un modulo con responsabilità non correlate in moduli con scopi chiari e coesi. Esempio: separare i controlli di idoneità dall'invio delle notifiche se oggi sono entrambi in BookingService.
- **Redistribute responsibilities**: riunire responsabilità correlate che sono sparse tra più moduli. Esempio: se le regole di idoneità sono in parte nell'interfaccia utente, in parte in BookingService, in parte nel connettore SIS, spostarle in un componente dedicato.
- **Obiettivo:** raggruppare le responsabilità in modo che un cambiamento probabile riguardi **il minor numero possibile di moduli**.

![[lez03-mo-p19-increase-cohesion.png]]
*A sinistra: BookingService (eligibility checks + send notifications) diviso in EligibilityRules e NotificationService. A destra: la logica di idoneità sparsa in UI, BookingService e SIS Adapter riunita in un solo modulo EligibilityRules.*

### Ridurre l'accoppiamento · [[03-Modifiability.pdf#page=20|p. 20]]–[[03-Modifiability.pdf#page=22|22]]

L'**accoppiamento** (*coupling*) è il grado in cui un modulo dipende da un altro; un accoppiamento forte può far propagare una modifica tra moduli.
- **Encapsulation**: esporre un'interfaccia e nascondere l'implementazione interna.
- **Use an intermediary**: far interagire i componenti tramite un mediatore senza che si conoscano; intermediari come un bus publish–subscribe, un repository di dati condiviso o la service discovery dinamica eliminano la necessità che una parte conosca l'identità dell'altra.
- **Abstract common service**: mettere servizi simili dietro un'interfaccia condivisa, in modo che le implementazioni possano cambiare indipendentemente se l'interfaccia resta stabile.
- **Restrict dependencies**: limitare con quali moduli un modulo interagisce o da cui dipende: restringendo la **visibilità** di un modulo (se gli sviluppatori non vedono un'interfaccia non possono usarla) e restringendo l'accesso ai soli moduli **autorizzati**. Si vede nelle architetture a strati (uno strato può usare solo gli strati inferiori, a volte solo il successivo) e nei wrapper (le entità esterne vedono, e quindi dipendono, solo dal wrapper e non dalla funzionalità interna).

![[lez03-mo-p21-reduce-coupling-tre-tattiche.png]]
*Tre tattiche: encapsulation (BookingService → Eligibility API → rule engine nascosto); use an intermediary (BookingService → event bus con l'evento `ReservationConfirmed` → Notification); abstract common service (BookingService → interfaccia comune StudentRecords con implementazioni alternative).*

### Posticipare il binding · [[03-Modifiability.pdf#page=23|p. 23]]–[[03-Modifiability.pdf#page=25|25]]

- Il **binding** è la scelta di un valore, componente o servizio. **Posticipare la scelta** permette alcune modifiche senza cambiare il codice sorgente. Se i binding sono definiti direttamente nel codice in fase di progetto vanno cambiati a mano; altrimenti si possono cambiare automaticamente. Quindi conviene definire i binding il più tardi possibile nel ciclo di vita.
- Tattiche per legare **a compilazione o build**: component replacement (in uno script di build o makefile), compile-time parameterization. A **deploy o configurazione**: configuration-time binding, resource files. A **runtime**: discovery, interpret parameters, shared repositories, polymorphism.

| Momento di binding | Tattica | Tecnologia d'esempio | Esempio nel Booking |
|---|---|---|---|
| Build | Component replacement | Maven build profiles | scegliere il connettore SIS dell'Università A o B al build |
| Compilazione / build | Compile-time parameterization | generazione di sorgenti durante un build Maven | generare una classe con un valore fissato prima della compilazione; cambiarlo richiede ricompilazione |
| Deploy / configurazione | Configuration-time binding | Spring Boot externalized configuration | impostare l'endpoint SIS con una variabile d'ambiente al deploy |
| Deploy / configurazione | Resource files | `application.yml` o `.properties` esterno | impostare in un file il numero massimo di prenotazioni |
| Runtime | Discovery | Spring Cloud DiscoveryClient e service registry | trovare un'istanza SIS disponibile dal nome logico del servizio |
| Runtime | Interpret parameters | logica applicativa che legge parametri della richiesta | scegliere una regola di idoneità in base al tipo di esame della richiesta |
| Runtime | Shared repositories | tabella di database condivisa | leggere dal database le regole di prenotazione attive |
| Runtime | Polymorphism | interfacce Java e implementazioni alternative | scegliere un'implementazione di `EligibilityPolicy` per l'università o l'esame pertinente |

### Pattern per la modificabilità · [[03-Modifiability.pdf#page=26|p. 26]]–[[03-Modifiability.pdf#page=27|27]]

- I pattern per la modificabilità dividono il sistema in moduli che si possono sviluppare ed evolvere separatamente con poca interazione, supportando **portabilità, modificabilità e riuso**: **Client-Server, Plug-in, Layers, Publish-Subscribe**.

### Pattern Client-Server · [[03-Modifiability.pdf#page=28|p. 28]]–[[03-Modifiability.pdf#page=29|29]]

- Un **server** fornisce servizi **contemporaneamente a più client distribuiti**. L'interazione segue la sequenza **Discovery e Interaction**: la comunicazione è avviata da un client, che usa un servizio di discovery per determinare la posizione del server; il server risponde secondo un protocollo concordato. Poi il client invia richieste e il server le elabora e risponde.

![[lez03-mo-p28-client-server.png]]
*Due client collegati via Internet a un server.*

**Benefici e trade-off**
- La connessione tra server e client è stabilita **dinamicamente**; il server non ha conoscenza a priori dei client (**basso accoppiamento** server–client) e non c'è accoppiamento tra i client.
- Il numero di client può scalare facilmente, limitato solo dalla capacità del server; anche la funzionalità del server può scalare se la capacità è superata.
- Client e server possono evolvere indipendentemente; servizi comuni sono condivisi tra più client; l'interazione con l'utente è isolata nel client.
- *Trade-off:* i messaggi possono essere ritardati dalla congestione di rete, degradando (o rendendo imprevedibili) le **prestazioni**; per i client che comunicano via una rete condivisa servono provvedimenti speciali per la **sicurezza** (soprattutto riservatezza) e l'integrità.

### Pattern Plug-in · [[03-Modifiability.pdf#page=30|p. 30]]

- Due tipi di elementi: elementi che forniscono un **nucleo di funzionalità** e **varianti specializzate (plug-in)** che aggiungono funzionalità al nucleo tramite un insieme fisso di interfacce. Nucleo e plug-in sono legati insieme in genere a build time o dopo.
- Esempio: il nucleo può essere un sistema operativo minimale (il **microkernel**, che fornisce memoria, IPC e gestione dei thread); i plug-in forniscono la funzionalità reale (driver di dispositivo, gestione dei task, gestione delle richieste di I/O).
- **Benefici:** un meccanismo controllato per estendere un prodotto base; possono essere sviluppati da produttori diversi ed evolvere indipendentemente dal microkernel. **Rischio:** possono essere introdotte vulnerabilità di sicurezza e minacce alla privacy.

### Pattern Layers · [[03-Modifiability.pdf#page=31|p. 31]]

- Divide il sistema in **strati** sviluppabili ed evolvibili separatamente con poca interazione, a supporto di portabilità, modificabilità e riuso. Ogni strato è esposto tramite un'interfaccia pubblica; gli strati interagiscono secondo una **relazione di ordinamento stretta** (o talvolta tramite un *layer bridge*).
- **Benefici:** il software degli strati inferiori può cambiare (finché l'interfaccia non cambia) senza influire sugli strati superiori.
- **Trade-off:** lo stratificazione aggiunge spesso una **penalità di prestazioni**; se si verificano molti *layer bridging* il sistema può non raggiungere gli obiettivi di portabilità e modificabilità che lo strato rigoroso favorisce.

![[lez03-mo-p31-layer-pattern.png]]
*Cinque strati — Presentation, Application, Business, Persistence, Database — con le chiamate tra strati verso il basso.*

### Pattern Publish-Subscribe · [[03-Modifiability.pdf#page=32|p. 32]]–[[03-Modifiability.pdf#page=33|33]]

- Pattern in cui i componenti comunicano tramite **messaggi asincroni** (eventi, topic). Tre tipi di elementi: **Publisher** (invia/pubblica messaggi), **Subscriber** (si iscrive e poi riceve messaggi), **Event Bus** (gestisce le sottoscrizioni e l'inoltro dei messaggi, parte dell'infrastruttura di runtime). I publisher non conoscono i subscriber; i subscriber conoscono solo i tipi di messaggio.
- Si basa sull'**invocazione implicita**: il componente che pubblica non invoca direttamente nessun altro; a runtime, quando un messaggio è pubblicato, il bus notifica tutti gli elementi registrati per quell'evento o topic. Ne risulta un **accoppiamento debole** tra publisher e subscriber.
- **Benefici:** publisher e subscriber sono indipendenti; aggiungere o cambiare subscriber richiede solo la registrazione a un evento e non cambia il publisher; il comportamento del sistema si cambia facilmente cambiando l'evento o il topic pubblicato e quindi i subscriber che lo riceveranno.
- **Trade-off:** **latenza**; **non determinismo** nell'ordine di invocazione dei metodi; **testabilità**: un cambiamento nei componenti associati agli eventi può avere un impatto ampio su comportamento e qualità del servizio.

*Approfondimenti nel wiki: [[modifiability]], [[tattiche-modifiability]], [[pattern-modifiability]], [[client-server]], [[plug-in]], [[layered]], [[publish-subscribe]], [[linee-di-prodotto-software]]*

## Lezione 4 — Progettazione basata sul riuso: DSSA, pattern e architetture multi-tier

*Fonte: 3-Architectural Patterns-complete.pdf (pp. 1–38 di 96). Cap. 4 di Taylor, Medvidovic, Dashofy, «Software Architecture: Foundations, Theory and Practice». La lezione era in origine un PDF più corto (04-Architectural Patterns), poi esteso dalla docente.*

### Progettare un'architettura: metodi e strategie · [[3-Architectural Patterns-complete.pdf#page=2|p. 2]]–[[3-Architectural Patterns-complete.pdf#page=5|5]]

- Contenuti: metodi di progettazione architetturale; riuso dell'esperienza di progetto; Domain-Specific Software Architectures (DSSA); pattern architetturali; stili architetturali.
- L'architettura rappresenta la **struttura a grana grossa** del sistema: un insieme di strutture, di tre tipi principali (C&C, modulare, allocazione). Ma **come si progetta un'architettura?**
- **Strategie di progettazione** (*design strategies*): approccio generale al progetto: divide-et-impera e raffinamento per passi; top-down vs bottom-up; astrazione dei dati e information hiding; uso di pattern e linguaggi di pattern; approccio iterativo e incrementale.
- **Metodi di progettazione** (*design methods*): più specifici delle strategie; forniscono una notazione, una descrizione del processo da seguire, linee guida per applicare il metodo. Esempi: progettazione funzionale (strutturata, basata su DFD), orientata agli oggetti, basata sui componenti, orientata ai servizi, basata su modelli…

![[lez04-ap-p5-metodi-di-progettazione.png]]
*Elenco di libri sui metodi di progettazione architetturale: The Unified Software Development Process, A System of Patterns (Buschmann et al.), Object-Oriented Modeling and Design (Rumbaugh), Design and use of software architectures (Bosch), ecc.*

### Il riuso dell'esperienza · [[3-Architectural Patterns-complete.pdf#page=6|p. 6]]–[[3-Architectural Patterns-complete.pdf#page=9|9]]

- Un importante strumento di progetto è il **riuso dell'esperienza**: l'esperienza passata va analizzata e raffinata; è cruciale imparare sia dai successi sia dagli insuccessi degli altri ingegneri (letteratura, conferenze). L'esperienza può fornire l'insieme iniziale di «possibili alternative di progetto».
- **Attribute-Driven Design** (p. 7): il metodo di progetto guidato dagli attributi di qualità (vedi Lezione 1).
- **Alternative da considerare** (p. 8):
  - progettare l'architettura **da zero**: possono emergere soluzioni nuove, ma è costoso (laborioso) e rischioso;
  - applicare una **soluzione o strategia generica** (stile o pattern) e adattarla al problema: riuso, meno lavoro, meno errori; ma la soluzione generica può non adattarsi perfettamente e richiedere molto rifacimento;
  - applicare una **soluzione specifica del dominio (DSSA)**: più riuso; ma cosa succede se non esiste una DSSA?
- **DSSA, pattern, stili e design pattern** si distinguono per **ambito di applicabilità** (p. 9).

![[lez04-ap-p9-ambito-applicabilita.png]]
*Asse verticale: conoscenza del dominio applicativo (da superficiale a profonda); asse orizzontale: ambito (livello di linguaggio di programmazione, struttura dell'applicazione, struttura del sistema). Dal basso a sinistra all'alto a destra: design pattern, stili, pattern architetturali, DSSA.*

### Domain-Specific Software Architecture (DSSA) · [[3-Architectural Patterns-complete.pdf#page=10|p. 10]]–[[3-Architectural Patterns-complete.pdf#page=14|14]]

- Una **DSSA** è un'architettura software raccomandata per i sistemi di un **dominio specifico** (detta anche **architettura di riferimento**). Esempi di domini: compilatori per linguaggi di programmazione, elettronica di consumo, avionica, sistemi di e-commerce/negozi web, videogiochi…
- Una DSSA è un insieme di componenti software che sono: **specializzati** per un tipo di compito (nel dominio); **generalizzati**, così da poter essere usati efficacemente nel dominio; **composti in una struttura (topologia) standardizzata** efficace per costruire buone architetture.

![[lez04-ap-p11-architettura-riferimento-web-microsoft.png]]
*Esempio: architettura di riferimento per applicazioni web (Microsoft Application Architecture Guide): browser lato client; lato server strati Presentation, Business e Data, con una colonna trasversale (cross-cutting).*

![[lez04-ap-p12-architettura-riferimento-tv.png]]
*Altro esempio: architettura di riferimento per una piattaforma TV (diagramma a componenti `CTvPlatform`: front-end, back-end, driver del sintonizzatore e altri).*

- **Vantaggi:** le DSSA massimizzano il **riuso di conoscenza e sviluppi precedenti** nella creazione di nuove architetture. **Limiti:** possono essere usate solo per costruire nuove applicazioni **dello stesso dominio**.
- **Esempi di architetture di riferimento per dominio** (p. 14): Automotive: AUTOSAR; IoT: ISO/IEC 30141; Industry 4.0: RAMI 4.0; IoT industriale: IIRA; Smart Grid: SGAM; Cloud Computing: NIST Cloud Computing Reference Architecture; Telecomunicazioni: TM Forum ODA; Sanità: openEHR. Le architetture di riferimento forniscono strutture riusabili, punti di vista, responsabilità e interfacce per una famiglia di sistemi in un dominio; **devono essere specializzate** in base ai requisiti del sistema e agli scenari di qualità.

### Esempi di architetture di riferimento · [[3-Architectural Patterns-complete.pdf#page=15|p. 15]]–[[3-Architectural Patterns-complete.pdf#page=17|17]]

![[lez04-ap-p15-autosar.png]]
*AUTOSAR, piattaforme e architetture software standardizzate per i sistemi elettronici automotive: Application Layer, AUTOSAR Runtime Environment (RTE), Basic Software a strati (Services, ECU Abstraction, Microcontroller Abstraction).*

![[lez04-ap-p16-architettura-riferimento-iot.png]]
*Architettura di riferimento IoT: a sinistra il modello per domini (User, Operations & Management, Application & Service, Access & Communication, Sensing & Controlling, Physical Entity); a destra la vista a livelli.*

![[lez04-ap-p17-cloud-computing-reference-model.png]]
*Modello concettuale di riferimento NIST per il cloud: attori Cloud Consumer, Cloud Auditor, Cloud Provider (con Service Orchestration SaaS/PaaS/IaaS), Cloud Broker, Cloud Carrier.*

### Software Product Line · [[3-Architectural Patterns-complete.pdf#page=18|p. 18]]–[[3-Architectural Patterns-complete.pdf#page=20|20]]

- Una **linea di prodotto software** (*Software Product Line*, SPL) è una famiglia di prodotti software-intensive collegati che: rispondono alle esigenze di uno specifico segmento di mercato o missione; **condividono un insieme gestito di funzionalità comuni**; **differiscono per variazioni esplicitamente pianificate**; sono sviluppati da un **insieme comune di risorse di base riusabili** (*core assets*).
- Idea di fondo: **sviluppare per il riuso, poi derivare i prodotti tramite configurazione.**
- Una SPL **riusa sistematicamente ciò che è comune e gestisce esplicitamente ciò che è variabile**:

| Comunanza: risorse di base condivise | Variabilità: differenze pianificate |
|---|---|
| architettura della linea di prodotto | funzionalità opzionali o alternative |
| componenti e servizi riusabili | implementazioni alternative dei componenti |
| requisiti comuni | requisiti specifici del prodotto |
| test e ambienti di test condivisi | test specifici del prodotto |
| strumenti comuni di build e deployment | opzioni di configurazione e deployment |

![[lez04-ap-p18-linee-di-prodotto.png]]
*Tre cerchi «Common», ciascuno con due cerchietti A e B: Product A = Common + A; Product B = Common + B.*

**Esempi di linee di prodotto in vari domini** (p. 20)

| Dominio | Linea di prodotto | Elementi comuni | Variabilità pianificata |
|---|---|---|---|
| Automotive | sistemi di infotainment | navigazione, interfaccia utente, connettività | display, comandi vocali, servizi online, lingue |
| Avionica | software per una famiglia di aerei | controllo di volo, diagnostica, comunicazioni | sensori, configurazioni dei motori, varianti di velivolo |
| Smart TV | famiglia di modelli di televisori | sistema operativo, streaming, aggiornamenti | schermo, sintonizzatore, impianto audio, applicazioni, mercato di destinazione |
| Smartphone | famiglia di dispositivi dello stesso produttore | sistema operativo, sicurezza, servizi cloud | fotocamere, display, sensori, memoria |
| Stampanti | famiglia di stampanti multifunzione | gestione della stampa, driver, diagnostica | scanner, stampa a colori, duplex, velocità |
| Dispositivi medici | famiglia di monitor per pazienti | acquisizione dati, allarmi, visualizzazione | segni vitali, sensori, interfacce, contesti clinici |
| IoT industriale | famiglia di sistemi di monitoraggio | raccolta dati, comunicazione, gestione dei dispositivi | sensori, protocolli, frequenza di campionamento, analytics |
| E-commerce | piattaforma per diversi negozi online | catalogo, carrello, ordini, autenticazione | pagamenti, valute, promozioni, branding, spedizioni |
| Home banking | soluzioni bancarie configurabili | conti, transazioni, autenticazione, auditing | prodotti finanziari, normative nazionali, regole di autorizzazione |
| Sistemi ERP | suite per organizzazioni diverse | utenti, contabilità, reportistica, «master da…» (testo troncato nella slide) | (cella vuota nella slide) |

![[lez04-ap-p20-esempi-linee-di-prodotto.png]]
*La tabella originale con tutti gli esempi.*

### Pattern architetturali · [[3-Architectural Patterns-complete.pdf#page=21|p. 21]]–[[3-Architectural Patterns-complete.pdf#page=23|23]]

- Un **pattern architetturale** è un insieme riusabile di decisioni di progetto architetturale che affronta un problema ricorrente; definisce una soluzione generale adattabile a contesti diversi.
- Pattern e DSSA catturano entrambi conoscenza architetturale riusabile, ma con **ambiti diversi**: una **DSSA** fornisce un quadro architetturale complessivo per una famiglia di sistemi di un dominio applicativo; un **pattern architetturale** affronta un problema architetturale ricorrente e di solito si applica in domini diversi; **più pattern** possono essere combinati nella stessa DSSA o architettura.
- Esempi: **State-Logic-Display** (o pattern a tre livelli, *three-tiered*), **Model-View-Controller**, **Sense-Compute-Control**.

### State-Logic-Display e architetture multi-tier · [[3-Architectural Patterns-complete.pdf#page=24|p. 24]]–[[3-Architectural Patterns-complete.pdf#page=27|27]]

- **State-Logic-Display (three-tiered)** è un tipo particolare di **architettura multi-tier**. Un'architettura multi-tier **partiziona il sistema in unità separatamente distribuibili ed eseguibili, i tier**. Ogni tier fornisce un insieme di servizi correlati e comunica con gli altri tramite interfacce esplicite. I tier possono essere eseguiti: su macchine o nodi virtuali diversi; in processi o container diversi; oltre confini di rete o organizzativi.
- **Non confondere tier e layer**: i **layer** rappresentano una **decomposizione logica** delle responsabilità del software; i **tier** rappresentano la **distribuzione fisica o di runtime** degli elementi software.
- **Esempi di applicazioni:** applicazioni aziendali, giochi multigiocatore, applicazioni web. Logiche di business possibili: sistema assicurativo, logica di gioco, sistema di calcolo delle tasse.

![[lez04-ap-p25-state-logic-display.png]]
*Tre riquadri impilati: Display (interfaccia utente), Business Logic, State (database); fra Display e Business Logic «Sends data; Requests services» verso il basso e «Returns values for display» verso l'alto; fra Business Logic e State «Requests values be retrieved or stored» e il ritorno dei valori.*

- **Multi-tier — esempi tipici** (p. 26): **two-tier** (client e database server); **three-tier** (client, application server e database server); **n-tier** (tier aggiuntivi per integrazione, messaggistica, caching o servizi esterni).

![[lez04-ap-p27-evoluzione-tier.png]]
*«From Centralised Deployment to Distributed Services» (p. 27): le stesse responsabilità logiche — presentazione, logica applicativa, integrazione, dati — assegnate a un numero crescente di unità installabili in modo indipendente, dal sistema centralizzato (one tier) ai servizi distribuiti.*

### Architettura a un livello (1-tier) · [[3-Architectural Patterns-complete.pdf#page=28|p. 28]]–[[3-Architectural Patterns-complete.pdf#page=29|29]]

- Presentazione, logica applicativa e gestione delle risorse sono **distribuite ed eseguite su un unico sistema centralizzato**. Gli utenti o i programmi esterni accedono tramite **terminali stupidi** (*dumb terminals*) gestiti dal sistema informativo centrale: i terminali forniscono input e output, mentre calcolo e gestione dei dati sono fatti dal sistema centrale. È tipica dei sistemi **mainframe**.
- L'assenza di tier separati non implica assenza di modularità logica: significa che tutti gli elementi software stanno nello stesso ambiente di esecuzione.

![[lez04-ap-p28-one-tier.png]]
*Due terminali utente (input/output) collegati a un Centralised Information System con tre strati: Presentation, Application Logic, Resource Management.*

**E gli attributi di qualità?** (p. 29)

| Attributo | Potenziali benefici | Potenziali limiti |
|---|---|---|
| Prestazioni | la comunicazione locale tra componenti evita l'overhead di rete | il sistema centrale può diventare un collo di bottiglia di calcolo e I/O |
| Disponibilità | meno componenti distribuiti e collegamenti semplificano la gestione dei guasti | il sistema centrale può essere un singolo punto di guasto |
| Scalabilità | le risorse centralizzate si possono potenziare in verticale | difficile la scalatura orizzontale e la scalatura indipendente delle funzioni |
| Sicurezza | dati e controllo di accesso gestiti centralmente | un attacco riuscito al sistema centrale può compromettere l'intero sistema |
| Modificabilità | il deployment centralizzato può semplificare il rilascio | l'accoppiamento stretto può aumentare l'impatto dei cambiamenti e impedire il deployment indipendente |
| Deployability | va gestito un solo ambiente di esecuzione | anche piccoli cambiamenti possono richiedere il rideployment dell'intera applicazione |
| Testabilità | l'intero sistema è collaudabile in un solo ambiente | i componenti possono essere difficili da isolare e collaudare indipendentemente |
| Interoperabilità | non serve integrazione tra tier distribuiti interni | l'integrazione con sistemi esterni o moderni può richiedere adattatori specializzati |

### Architettura a due livelli (2-tier): Client/Server · [[3-Architectural Patterns-complete.pdf#page=30|p. 30]]–[[3-Architectural Patterns-complete.pdf#page=32|32]]

- **Fat client:** presentazione e parte della logica applicativa passano dal sistema centrale al **client**. Il client invoca direttamente i servizi offerti da un server di risorse o di database.
- Client e server sono **unità di esecuzione separate**, possibilmente su macchine diverse. La loro interazione richiede una **API remota o un protocollo di comunicazione esplicito**, che definisce operazioni, dati scambiati, errori e regole di interazione: stabilisce un **contratto esplicito** attraverso il confine client–server e nasconde l'implementazione interna del server.

![[lez04-ap-p31-two-tier.png]]
*Two-Tier Client–Server: il Client Tier (fat client) esegue Presentation e Application Logic, installate su ogni client; il Server Tier gestisce le risorse condivise.*

| Attributo | Benefici | Limiti |
|---|---|---|
| Prestazioni | l'esecuzione locale di presentazione e logica dà interazione reattiva e riduce il carico del server | molte chiamate remote o accesso diretto al database possono creare colli di bottiglia di rete e database |
| Scalabilità | le risorse del client contribuiscono alla capacità di elaborazione | un server o database condiviso può limitare la scalabilità al crescere dei client |
| Disponibilità | i client possono continuare alcune operazioni locali durante disconnessioni temporanee | il server condiviso resta un potenziale singolo punto di guasto |
| Modificabilità | la logica di presentazione evolve indipendentemente dal server se l'API è stabile | cambiare le regole di business può richiedere di aggiornare ogni client |
| Deployability | le modifiche lato server si distribuiscono centralmente | installare, configurare e aggiornare molti fat client è costoso |
| Sicurezza | il server può centralizzare autenticazione e accesso alle risorse | il codice client non è del tutto affidabile; l'accesso diretto al database aumenta la superficie di attacco |
| Interoperabilità | un'API esplicita permette a client di tipi diversi di accedere ai servizi | i client possono dipendere fortemente da una specifica API, protocollo o schema di database |
| Manutenibilità | le responsabilità sono divise tra client e server | la logica di business può essere duplicata o diventare incoerente tra versioni diverse dei client |

### Architettura a tre livelli (3-tier) · [[3-Architectural Patterns-complete.pdf#page=33|p. 33]]–[[3-Architectural Patterns-complete.pdf#page=34|34]]

- L'**interfaccia utente** gira su un desktop o workstation e fornisce una GUI standard (**thin client**). La **logica di business** è fatta di uno o più moduli su un **application server** (o, in alcune configurazioni, su una workstation). Un **RDBMS**, su un database server o mainframe, fornisce memorizzazione, elaborazione delle query, gestione delle transazioni e controllo della concorrenza.
- È una delle specializzazioni più usate del modello **n-tier**.

![[lez04-ap-p33-three-tier.png]]
*Three-Tier Client–Server: Client Tier (browser/app mobile, thin client) → HTTPS API → Application Tier (application server con la logica applicativa, installata centralmente) → SQL/JDBC → Data Tier (database).*

| Attributo | Benefici | Limiti |
|---|---|---|
| Modificabilità | i cambiamenti si localizzano in uno strato | i cambiamenti possono propagarsi se le interfacce tra strati sono instabili |
| Manutenibilità | la chiara separazione delle responsabilità semplifica la comprensione | troppi strati possono introdurre complessità inutile |
| Testabilità | gli strati si testano indipendentemente con mock o stub | le interazioni end-to-end richiedono comunque test di integrazione |
| Riusabilità | servizi di business e di persistenza possono supportare interfacce diverse | i componenti possono restare accoppiati a ipotesi specifiche dello strato |
| Sicurezza | controlli di accesso applicabili a confini ben definiti | saltare gli strati può aggirare i controlli di sicurezza |
| Prestazioni | gli strati permettono ottimizzazioni come il caching | le richieste che attraversano più strati introducono overhead |
| Deployability | gli strati possono essere assegnati a tier di deployment diversi | gli strati logici non sono necessariamente distribuibili in modo indipendente |
| Scalabilità | i singoli tier si possono replicare se gli strati sono distribuiti separatamente | un data tier condiviso può restare un collo di bottiglia |

### Middleware · [[3-Architectural Patterns-complete.pdf#page=35|p. 35]]–[[3-Architectural Patterns-complete.pdf#page=36|36]]

- Il **middleware** è uno **strato infrastrutturale trasversale** (*cross-cutting*) che supporta le interazioni tra i diversi tier; verso i **sistemi esterni** può realizzare adattamento, trasformazione dei dati, mediazione di protocollo e instradamento.

![[lez05-ap-p35-middleware-three-tier.png]]
*Dentro la «Three-tier application»: Presentation Tier → Communication Middleware (chiamate remote, serializzazione, sicurezza) → Business Tier → Data and Integration Middleware (adapter, mediazione di protocollo, trasformazione dei dati) → sistemi esterni e dati.*

- **Il middleware come abilitatore di integrazione:** un'interfaccia comune per accedere a sistemi diversi; adapter e wrapper che nascondono i dettagli specifici dei sistemi; mediazione di protocollo tra tecnologie diverse; trasformazione dei dati tra formati diversi; instradamento e orchestrazione delle richieste.
- **Beneficio:** i client non devono conoscere l'architettura interna o la tecnologia dei sistemi integrati. **Trade-off:** il middleware introduce complessità aggiuntiva, latenza e un potenziale singolo punto di guasto.
- **N-tier definisce come si separano le responsabilità applicative; il middleware fornisce i meccanismi di comunicazione e integrazione necessari per collegare i tier e i sistemi esterni.**

### Pattern di deployment · [[3-Architectural Patterns-complete.pdf#page=37|p. 37]]–[[3-Architectural Patterns-complete.pdf#page=38|38]]

![[lez04-ap-p36-four-tier-deployment.png]]
*Il pattern di deployment a 4 tier (per applicazioni web), dalla Microsoft Application Architecture Guide: Client Tier → Web Tier (web server) → Business Logic Tier (app server) → Database Tier.*

![[lez04-ap-p37-load-balanced-cluster.png]]
*Altro pattern di deployment per garantire le prestazioni, il «Load-Balanced Cluster»: Client → firewall opzionale → Load Balancer → Application Tier con più istanze replicate di AppServer → firewall opzionale → Data Tier.*

*Approfondimenti nel wiki: [[progettazione-basata-sul-riuso]], [[dssa]], [[linee-di-prodotto-software]], [[pattern-architetturali]], [[state-logic-display]], [[architetture-multi-tier]], [[attribute-driven-design]], [[autosar]]*

## Lezione 5 — Pattern architetturali: MVC, Spring MVC e Sense-Compute-Control

*Fonte: 3-Architectural Patterns-complete.pdf (pp. 39–96 di 96). Cap. 4 di Taylor, Medvidovic, Dashofy, «Software Architecture: Foundations, Theory and Practice».*

### Model-View-Controller: origini e motivazione · [[3-Architectural Patterns-complete.pdf#page=39|p. 39]]–[[3-Architectural Patterns-complete.pdf#page=41|41]]

- Un esempio classico di pattern architetturale è il **Model-View-Controller** (MVC). Introdotto con **Smalltalk** allo Xerox PARC alla fine degli anni '70; si può considerare una **composizione di pattern che collaborano**. Oggi è molto adottato nei framework web come Spring MVC, ASP.NET Core MVC, Ruby on Rails, Apache Struts.
- **Obiettivo principale:** separare la **logica di dominio** dalla **presentazione e dall'interazione con l'utente**.
- **Motivazione:** gli stessi dati applicativi possono richiedere più presentazioni. MVC nasce dall'esigenza di mostrare e manipolare gli stessi dati con diverse rappresentazioni grafiche: lo stesso Model può supportare più View senza incorporare logica di presentazione nei componenti di gestione dei dati.

![[lez05-ap-p41-mvc-motivazione.png]]
*Un unico Model («Numerical data») collegato a tre View: un grafico a torta, un grafico ad aree, un istogramma 3D. Gli stessi numeri, tre presentazioni.*

### Il pattern MVC · [[3-Architectural Patterns-complete.pdf#page=42|p. 42]]–[[3-Architectural Patterns-complete.pdf#page=44|44]]

- Separa l'applicazione in tre elementi che cooperano: **Model** (gestisce dati applicativi, stato e logica di dominio), **View** (presenta il model all'utente), **Controller** (interpreta l'input utente e coordina model e view).
- Separare presentazione e stato riduce l'impatto dei cambiamenti dell'interfaccia sul comportamento di base. MVC è un pattern architetturale classico per applicazioni interattive.
- **Relazioni strutturali del MVC classico:** più Controller possono operare sullo stesso Model e più View possono presentarlo; i Controller avviano operazioni sul Model; le View si iscrivono ai cambiamenti del Model e aggiornano la presentazione quando vengono notificate; un solo Model può supportare più Controller e più View.

![[lez05-ap-p43-mvc-relazioni-strutturali.png]]
*Relazioni strutturali: Controller (ruolo initiator, molteplicità *) → Model (repository, 1); View (subscriber, *) ← Model (notifier).*

![[lez05-ap-p44-mvc-interazioni-classico.png]]
*Interazioni tra moduli nel MVC classico, sull'esempio della prenotazione di una sessione d'esame: lo studente seleziona una sessione sulla View; la View passa al Controller la richiesta; il Controller invoca il Model; il Model notifica la View, che aggiorna la visualizzazione.*

### Tre responsabilità, interazioni diverse · [[3-Architectural Patterns-complete.pdf#page=45|p. 45]]

- **Model** = stato applicativo e comportamento di dominio; **View** = presentazione delle informazioni; **Controller** = interpretazione delle azioni dell'utente.
- MVC **non prescrive un unico flusso di interazione**: dipende dal tipo di applicazione, dall'ambiente di esecuzione, dal modello di comunicazione, dall'implementazione o dal framework. **Le responsabilità restano stabili, le interazioni possono variare.**

### 1. MVC classico: la View tira dal Model (pull) · [[3-Architectural Patterns-complete.pdf#page=46|p. 46]]

La View inoltra le azioni dell'utente al Controller; il Controller le interpreta e aggiorna il Model; la View interroga direttamente il Model per i dati da mostrare (*pull*). Si usa quando la View sa da sola quando aggiornarsi.

![[lez05-ap-p46-mvc-pull.png]]
*User → View → user event → Controller → update → Model; la View invia anche query state al Model, che risponde con i dati.*

### 2. MVC classico: interazione basata su Observer · [[3-Architectural Patterns-complete.pdf#page=47|p. 47]]

La View si iscrive ai cambiamenti del Model; il Controller aggiorna il Model; il Model **notifica** le View registrate; ogni View **recupera** lo stato aggiornato dal Model: **notifica, poi pull**. Qui entra il design pattern **Observer**: Model = Subject; View = Observer.

![[lez05-ap-p47-mvc-observer.png]]
*Come la precedente, con in più la freccia change notification dal Model alla View.*

### Un'interazione completa del MVC classico · [[3-Architectural Patterns-complete.pdf#page=48|p. 48]]

View → Controller: **Strategy**; Model → View: **Observer**; View → Model: pull dello stato aggiornato.

![[lez05-ap-p48-mvc-sequenza-completa.png]]
*Sequenza: User perform action → View; View delega l'input → Controller; Controller esegue l'operazione → Model; Model notifica il cambio di stato → View; View interroga lo stato aggiornato → Model; Model restituisce i dati → View; View aggiorna la visualizzazione → User.*

### MVC e design pattern: Observer e Strategy · [[3-Architectural Patterns-complete.pdf#page=49|p. 49]]–[[3-Architectural Patterns-complete.pdf#page=52|52]]

- **Observer** gestisce l'interazione tra Model e View: le View si iscrivono al Model e sono notificate quando il suo stato cambia. Le **View** sono gli *Observer*, i **Model** i *Subject*.
- **Strategy** permette di cambiare il comportamento di interazione associato a una View: la View delega la gestione dell'input a un Controller, e Controller diversi possono dare strategie di interazione diverse.

![[lez05-ap-p49-observer.png]]
*Observer: l'interfaccia Subject (attach, detach, notify) aggrega più Observer (update); ConcreteSubject ha lo stato (getState, setState); ConcreteObserver implementa update.*

![[lez05-ap-p50-strategy.png]]
*Strategy: la View (contesto, con un controller e `handleUserAction`) delega a un'interfaccia Controller (`processAction`), realizzata da controller concreti (per esempio per lo studente e per l'amministratore).*

**Una View in Java senza Strategy** (p. 51): ogni nuovo comportamento di interazione richiede di modificare la View.

```java
void onExamSelected(ExamSession exam) {
    if (mode == BROWSE) { showDetails(exam); }
    else if (mode == BOOKING) { bookingService.book(exam); }
    else if (mode == ADMINISTRATION) { openEditForm(exam); }
}
```

**Lo stesso esempio con il design pattern Strategy** (p. 52): la View conosce solo l'interfaccia del controller; il `main` decide quali controller associare alla view.

```java
interface Controller { void processAction(UserAction action); }
class BrowseController implements Controller {
    public void processAction(UserAction action) { /* Show exam details */ }
}
class BookingController implements Controller {
    public void processAction(UserAction action) { /* Request an exam booking */ }
}
class AdministrationController implements Controller {
    public void processAction(UserAction action) { /* Modify the exam session */ }
}
class ExamCalendarView {
    private Controller controller;
    void onUserAction(UserAction action) { controller.processAction(action); }
}

public static void main(String[] args) {
    ExamService examService = new ExamService();
    Controller controller = new BookingController(examService);
    Controller cancellationController = new CancellationController(examService);
    ExamCalendarView view = new ExamCalendarView();
    view.setController(controller);
    view.show();
    // After an event…
    view.setController(cancellationController);
    view.show();
}
```

### Due ulteriori modelli di interazione MVC · [[3-Architectural Patterns-complete.pdf#page=53|p. 53]]–[[3-Architectural Patterns-complete.pdf#page=57|57]]

**3. Web MVC lato server: il Controller fornisce la View** (p. 54)
- Il browser invia una richiesta HTTP al Controller; il Controller invoca il Domain Model o i servizi applicativi; prepara i dati necessari alla presentazione; sceglie una View e le passa un **View Model**; la View produce la risposta HTML. La View di norma riceve i dati dal Controller e **non osserva direttamente** il Domain Model.

![[lez05-ap-p54-server-side-web-mvc.png]]
*Browser → HTTP request → Controller → operation/query → Domain Model → result → Controller → View Model → View → HTML response → Browser.*

**4. Applicazione web lato client: UI reattiva** (p. 55)
- Il server espone dati e operazioni tramite un'API; il browser mantiene uno **stato locale lato client**; i componenti UI **reagiscono ai cambiamenti di stato**; la comunicazione con il server è asincrona. I framework possono usare architetture **ispirate a MVC** più che MVC rigoroso: componenti, MVVM, Flux, Redux, architetture reattive. Il server restituisce i dati, il client si occupa di rendering e aggiornamento della UI.

![[lez05-ap-p55-client-side-reactive.png]]
*Server → JSON data → Client State → state change → Client UI → user event → Client Logic → HTTP API → Server.*

**Confronto dei modelli di interazione** (p. 56)

| Variante | Chi fornisce i dati alla View? | Come si aggiorna la View? | Contesto tipico |
|---|---|---|---|
| Classic MVC — Pull | la View interroga il Model | refresh esplicito | GUI desktop |
| Classic MVC — Observer | la View interroga il Model dopo la notifica | notifica di cambiamento del Model | GUI interattive |
| Web MVC lato server | il Controller passa un View Model | nuovo ciclo HTTP richiesta–risposta | Spring MVC, ASP.NET MVC, Struts |
| UI reattiva lato client | lo stato client riceve i dati dal server | aggiornamento reattivo dello stato | single-page application |

**Riepilogo: MVC è una famiglia di varianti** (p. 57)

| Classic MVC | Web MVC lato server |
|---|---|
| interazione continua all'interno dell'applicazione | cicli HTTP richiesta–risposta |
| la View può osservare il Model | la View normalmente non osserva il Domain Model |
| la View può interrogare il Model | il Controller fornisce i dati alla View |
| il Controller gestisce eventi della UI | il Controller gestisce richieste HTTP |
| la View è un componente UI persistente | la View è generata per una risposta |

### Il pattern Front Controller · [[3-Architectural Patterns-complete.pdf#page=58|p. 58]]

- Nel Web MVC lato server, un **unico punto di ingresso** riceve tutte le richieste HTTP e le smista al Controller applicativo appropriato; il risultato è usato per generare la risposta tramite una View.

![[lez05-ap-p58-front-controller.png]]
*Dentro il servlet engine (per esempio Tomcat): la richiesta in arrivo va al Front controller, che la delega al Controller; il Controller la gestisce e crea il model; il Front controller delega la generazione della risposta al View template passandogli il model; il template genera la risposta.*

### Spring MVC e Spring Boot

### Panoramica · [[3-Architectural Patterns-complete.pdf#page=59|p. 59]]–[[3-Architectural Patterns-complete.pdf#page=62|62]]

**Spring MVC** è un framework Java per sviluppare applicazioni web lato server secondo l'approccio Model–View–Controller. Si basa sulla **Servlet API** e fa parte dello **Spring Framework**.
- **Spring Framework** fornisce il container e le funzionalità di base; **Spring MVC** realizza lo strato web; **Spring Boot** semplifica configurazione, avvio e deployment.

![[lez05-ap-p60-spring-framework-mvc-boot.png]]
*Tre strati: Spring Boot (starter, auto-configuration, server incorporato, packaging) configura e avvia → Spring MVC (strato web) → Spring Framework (fondamenta).*

- **Spring Framework** gestisce i componenti applicativi e le loro dipendenze. Il cuore è il **container IoC**, rappresentato principalmente da `ApplicationContext`. Il container IoC: **crea gli oggetti applicativi, detti bean**; risolve le loro dipendenze; collega Controller, Service e Repository; gestisce il ciclo di vita dei componenti; offre funzionalità trasversali come gestione di transazioni e configurazione.
- **Spring MVC** è il modulo specializzato nella **gestione delle richieste HTTP**: traduce le richieste HTTP in chiamate a componenti applicativi e coordina la risposta. Offre: instradamento delle richieste (*request routing*); Controller annotati; binding e validazione dei dati di input; integrazione con i servizi applicativi; preparazione dei dati per la View; *view resolution* e rendering HTML.

### Il DispatcherServlet · [[3-Architectural Patterns-complete.pdf#page=63|p. 63]]–[[3-Architectural Patterns-complete.pdf#page=64|64]]

- Spring MVC realizza il Front Controller con il **DispatcherServlet**: un servlet fornito da Spring MVC che rappresenta l'**unico punto d'ingresso dello strato web**. Il browser non deve sapere quale classe Java gestirà la richiesta: conosce solo un URL, per esempio `GET /exam-sessions`. Il DispatcherServlet riceve la richiesta e stabilisce quale controller applicativo la gestirà.

![[lez05-ap-p63-dispatcherservlet.png]]
*Il browser invia tutte le richieste HTTP al DispatcherServlet (Front Controller), che smista verso ExamSessionController, BookingController, StudentController.*

- **Flusso di elaborazione di una richiesta**: il DispatcherServlet coordina instradamento della richiesta, invocazione del Controller, risoluzione della View e rendering della risposta.

![[lez05-ap-p64-spring-mvc-flusso.png]]
*Browser → HTTP request → DispatcherServlet → route request → Controller → invoke → Application Service → result → Controller → view name + data → DispatcherServlet → resolve view name → ViewResolver → View → render View with data → HTML view → HTTP response → Browser.*

### HandlerMapping, Controller e View · [[3-Architectural Patterns-complete.pdf#page=65|p. 65]]–[[3-Architectural Patterns-complete.pdf#page=68|68]]

- Il DispatcherServlet consulta un **HandlerMapping**, che conosce le corrispondenze tra URL e metodi Java (definite con annotazioni). L'annotazione `@GetMapping("/exam-sessions")` indica che il metodo deve gestire le richieste GET dirette a `/exam-sessions`.

```java
@Controller
public class ExamSessionController {
    @GetMapping("/exam-sessions")
    public String listAvailableSessions(Model model) {
        // ...
    }
}
```

- **Il Controller esegue la logica di coordinamento**: invoca il servizio applicativo; inserisce i dati nel Model; restituisce il **nome logico** della View; **non genera direttamente la pagina HTML**. `exam-sessions` non è il nome completo di un file: è un nome logico di vista, che il **ViewResolver** associa, per esempio, al template `src/main/resources/templates/exam-sessions.html`.

```java
@GetMapping("/exam-sessions")
public String listAvailableSessions(Model model) {
    var sessions = service.findAvailableSessions();
    model.addAttribute("examSessions", sessions);
    return "exam-sessions";
}
```

```html
<!-- Template Thymeleaf che genera la View -->
<tr th:each="session : ${examSessions}">
  <td th:text="${session.examName}"></td>
  <td th:text="${session.date}"></td>
</tr>
```

![[lez05-ap-p67-sequenza-show-exam-sessions.png]]
*Flusso completo per il requisito ShowExamSessions: `GET /exam-sessions` → il DispatcherServlet trova l'handler con HandlerMapping → invoca `listAvailableSessions()` → il servizio restituisce `findAvailableSessions()` → il controller ritorna "exam-sessions" + Model → il ViewResolver risolve il nome → la View Thymeleaf produce la pagina.*

**Corrispondenza tra Front Controller e Spring MVC** (p. 68)

| Elemento del pattern | Spring MVC |
|---|---|
| Front Controller | `DispatcherServlet` |
| Application Controller / Handler | classe annotata con `@Controller` |
| Request mapping | `HandlerMapping` |
| Application operation | metodo annotato con `@GetMapping` o `@PostMapping` |
| Model data | attributi dell'oggetto `Model` |
| View selection | `ViewResolver` |
| View template | Thymeleaf, JSP ecc. |

### Spring Boot · [[3-Architectural Patterns-complete.pdf#page=69|p. 69]]–[[3-Architectural Patterns-complete.pdf#page=71|71]]

- **Spring Boot non sostituisce Spring Framework né Spring MVC:** li configura e avvia con convenzioni e **auto-configuration**. In presenza di dipendenze web, Spring Boot può: avviare un container servlet incorporato (di solito Tomcat); creare l'`ApplicationContext`; abilitare il component scanning; registrare il `DispatcherServlet`; configurare Spring MVC; impostare la view resolution; creare un eseguibile come file JAR.

```java
@SpringBootApplication
public class ExamBookingApplication {
    public static void main(String[] args) {
        SpringApplication.run(ExamBookingApplication.class, args);
    }
}
```

`@SpringBootApplication` abilita, in forma semplificata: configurazione Spring, component scanning, auto-configuration.

![[lez05-ap-p71-context-hierarchy.png]]
*Gerarchia dei contesti in Spring Web MVC: il DispatcherServlet usa un WebApplicationContext con i bean web (Controller, HandlerMapping, ViewResolver…), collegato a un WebApplicationContext radice con i bean dello strato intermedio (service, datasource…).*

### Un esempio in Spring MVC: gestione delle spese personali · [[3-Architectural Patterns-complete.pdf#page=72|p. 72]]–[[3-Architectural Patterns-complete.pdf#page=82|82]]

- Applicazione per la gestione delle spese personali. **Model**: gestisce i dati delle spese (importo, data, categoria), le salva e le recupera da un database. **View**: mostra la lista delle spese e permette di aggiungerne di nuove. **Controller**: quando l'utente inserisce una nuova spesa riceve l'input, lo valida, invia i dati al modello per salvarli e aggiorna la vista.

**Classe Model** (`Expense.java`, getter e setter omessi)

```java
package com.example.expensemanager.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.time.LocalDate;

@Entity
public class Expense {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String category;
    private double amount;
    private LocalDate date;

    public Expense() {}
    public Expense(String category, double amount, LocalDate date) {
        this.category = category; this.amount = amount; this.date = date;
    }
    // getter e setter di id, category, amount, date
}
```

**Repository** (`ExpenseRepository.java`, per interagire con il database H2)

```java
@Repository
public interface ExpenseRepository extends JpaRepository<Expense, Long> { }
```

**Controller** (`ExpenseController.java`)

```java
@Controller
public class ExpenseController {
    @Autowired
    private ExpenseRepository expenseRepository;

    @GetMapping("/")
    public String viewExpenses(Model model) {
        List<Expense> expenses = expenseRepository.findAll();
        model.addAttribute("expenses", expenses);
        model.addAttribute("expense", new Expense());
        return "expenses";
    }

    @PostMapping("/addExpense")
    public String addExpense(@ModelAttribute("expense") Expense expense) {
        expense.setDate(LocalDate.now());       // imposta la data corrente
        expenseRepository.save(expense);
        return "redirect:/";
    }
}
```

**View** (`src/main/resources/templates/expenses.html`, con Thymeleaf come motore di template)

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head><title>Gestione Spese</title></head>
<body>
  <h1>Lista Spese</h1>
  <table>
    <thead><tr><th>ID</th><th>Categoria</th><th>Importo</th><th>Data</th></tr></thead>
    <tbody>
      <tr th:each="expense : ${expenses}">
        <td th:text="${expense.id}"></td>
        <td th:text="${expense.category}"></td>
        <td th:text="${expense.amount}"></td>
        <td th:text="${expense.date}"></td>
      </tr>
    </tbody>
  </table>
  <h2>Aggiungi una nuova spesa</h2>
  <form th:action="@{/addExpense}" th:object="${expense}" method="post">
    <label>Categoria:</label> <input type="text" th:field="*{category}" /><br>
    <label>Importo:</label> <input type="number" th:field="*{amount}" /><br>
    <button type="submit">Aggiungi Spesa</button>
  </form>
</body>
</html>
```

![[lez05-ap-p80-view-generata.png]]
*Una possibile View generata: «Lista Spese», tabella con tre righe di esempio (Trasporti, Alimentari, Libri) e sotto il form «Aggiungi una nuova spesa» (Categoria, Importo, pulsante «Aggiungi Spesa»).*

**Configurazione del database** (`src/main/resources/application.properties`, database H2)

```properties
# H2 Database configuration
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=password
spring.jpa.hibernate.ddl-auto=update
spring.h2.console.enabled=true
```

**Applicazione principale** (`ExpenseManagerApplication.java`): una volta completata l'implementazione si esegue l'applicazione da terminale o IDE (IntelliJ, Eclipse) e si va su `http://localhost:8080/` per vedere la lista delle spese e aggiungerne di nuove.

```java
@SpringBootApplication
public class ExpenseManagerApplication {
    public static void main(String[] args) {
        SpringApplication.run(ExpenseManagerApplication.class, args);
    }
}
```

### Il pattern Sense-Compute-Control

### Il pattern · [[3-Architectural Patterns-complete.pdf#page=83|p. 83]]–[[3-Architectural Patterns-complete.pdf#page=86|86]]

- Il pattern **Sense–Compute–Control** supporta applicazioni che **interagiscono con un ambiente esterno e lo controllano**; è comune in telecomunicazioni, domotica e building automation, robotica, avionica, sistemi industriali ed embedded.
- L'interazione segue tre stadi: **Sense** — i sensori raccolgono dati dall'ambiente esterno; **Compute** — i componenti di elaborazione del contesto aggregano e interpretano i dati dei sensori per determinare la situazione attuale; **Control** — i componenti di controllo decidono quali azioni compiere e inviano i comandi agli **attuatori**.
- **Obiettivo:** strutturare le applicazioni di controllo embedded.

![[lez05-ap-p85-scc-architettura.png]]
*Architettura Sense–Compute–Control: la fascia SENSE (sensori 1–4) converge sul blocco COMPUTE «Compute and Control», da cui partono frecce verso la fascia CONTROL (attuatori A, B, C); riquadro «Control loop»: leggi i sensori, calcola le uscite, invia i comandi agli attuatori, ripeti.*

- **Esempio: applicazione di sicurezza domestica (Home Inclusion Detection):** *sense* — rileva movimento con sensori di movimento; *compute* — stabilisce se i dati indicano una possibile intrusione; *control* — agisce sull'ambiente attivando un allarme o inviando una notifica.

![[lez05-ap-p86-scc-home-security.png]]
*Ambiente esterno → fenomeni fisici → sensori → dati grezzi → elaborazione del contesto → contesto interpretato → logica di controllo → comando → attuatori → cambiano l'ambiente.*

### Varianti a tre e a quattro stadi · [[3-Architectural Patterns-complete.pdf#page=87|p. 87]]–[[3-Architectural Patterns-complete.pdf#page=89|89]]

- **Variante a tre stadi:** *Sense* acquisisce i dati dall'ambiente; *Compute* combina interpretazione del contesto e decisione; *Control* invia i comandi agli attuatori. Adatta quando elaborazione e logica di controllo sono relativamente semplici.
- **Variante a quattro stadi:** separa l'**interpretazione del contesto** dalle **decisioni di controllo**; i componenti di elaborazione del contesto possono servire politiche di controllo diverse. Adatta a sistemi complessi, riusabili o distribuiti.
- La variante a tre stadi mette in risalto il ciclo di controllo; quella a quattro stadi migliora **modificabilità e riuso** separando interpretazione del contesto e decisione.

![[lez05-ap-p88-scc-tre-quattro-stadi.png]]
*Tre stadi (Sense → Compute → Control) a confronto con quattro (Sensing → Context Processing → Control Logic → Actuation).*

![[lez05-ap-p89-scc-access-control.png]]
*Variante a quattro stadi: sistema di controllo accessi e rilevamento intrusioni. Fasce separate da linee tratteggiate: entità (camera, rilevatore di movimento, serratura, database delle autorizzazioni, identificatore), contesto, controllo e attuatori.*

### Dal Sense-Compute-Control all'IoT · [[3-Architectural Patterns-complete.pdf#page=90|p. 90]]–[[3-Architectural Patterns-complete.pdf#page=91|91]]

- L'**IoT** estende il ciclo Sense–Compute–Control **distribuendo** rilevazione, calcolo e attuazione tra dispositivi connessi, **nodi edge** e **servizi cloud**.
- **Controllo locale:** sensori → logica di controllo locale all'edge → attuatori; permette risposte rapide e funzionamento anche senza connessione al cloud.
- **Controllo remoto/centrale:** sensori → edge → cloud → logica di controllo remota → edge → attuatori; permette decisioni basate su dati aggregati, regole centralizzate e analisi più complesse.

![[lez05-ap-p90-scc-iot.png]]
*Architettura IoT e ciclo SCC: ambiente fisico osservato dai sensori (dispositivi connessi, SENSE) → telemetria ed eventi → edge/gateway (filtraggio, aggregazione, decisioni locali; COMPUTE, con logica di controllo locale) → piattaforma IoT/cloud (memorizzazione, analytics, gestione dei dispositivi) → applicazioni.*

- **Attributi di qualità:** la separazione di sensing, elaborazione del contesto, controllo e attuazione migliora **modificabilità, testabilità e riuso**; le implementazioni distribuite (IoT) introducono problemi di **latenza, disponibilità, safety e sicurezza**.

### Esempio: Lunar Lander · [[3-Architectural Patterns-complete.pdf#page=92|p. 92]]–[[3-Architectural Patterns-complete.pdf#page=94|94]]

- **Lunar Lander (LL)** è un semplice videogioco sviluppato alla fine degli anni '60. **Obiettivo:** far atterrare in sicurezza una navicella sulla superficie lunare.
- **Meccanica base:** il giocatore controlla la navicella durante la discesa; la manetta controlla la spinta del motore e quindi la velocità di discesa; il carburante disponibile è limitato; quota e velocità iniziali sono predefinite; si vince atterrando con velocità verticale inferiore a **5 piedi al secondo**, con o senza carburante residuo. **Versioni avanzate:** un joystick per controllare movimento orizzontale, orientamento e spinta del motore.

**LL con il pattern Sense-Compute-Control** (p. 93)

| Fase | Lunar Lander |
|---|---|
| Sense | leggere quota, velocità, orientamento e carburante residuo |
| Compute | determinare la spinta necessaria e la correzione di assetto |
| Control | attivare il motore e i propulsori di manovra |
| Ambiente | la gravità lunare cambia posizione e velocità della navicella |

![[lez05-ap-p94-scc-lunar-lander.png]]
*Architettura SCC del Lunar Lander: ambiente lunare e dinamica della navicella → stato fisico → sensing (altimetro, giroscopio, velocità verticale, livello di carburante) → misure → Flight Control Computer (stima dello stato, logica di controllo), che riceve anche i comandi del pilota → attuatori.*

### L'architettura dei sistemi di guida autonoma (ADS) · [[3-Architectural Patterns-complete.pdf#page=95|p. 95]]

![[lez05-ap-p95-ads.png]]
*Architettura tipica di un sistema di guida autonoma: Sensing (GPS/IMU, camera, LiDAR, radar) → Perception (localizzazione, rilevamento) → Planning (previsione, pianificazione) → Control (algoritmi e funzioni di controllo).*

### Conclusioni · [[3-Architectural Patterns-complete.pdf#page=96|p. 96]]

- Sono state analizzate **due strategie di progettazione basate sul riuso**: le **DSSA** e i **pattern architetturali** (Three-Tier, MVC, Sense Compute Control). Nelle prossime lezioni si introdurranno gli **stili architetturali**.

*Approfondimenti nel wiki: [[mvc]], [[spring-mvc]], [[sense-compute-control]], [[applicare-sense-compute-control]], [[implementare-mvc]]*

## Lezione 6 — Agile Project Management (Parte 1)

*Fonte: 04_Agile_01_bis.pdf (81 pagine, «Agile Project Management (Part 1)», prof.ssa Anna Rita Fasolino). Agenda: che cos'è Agile; Manifesto Agile; come funziona Agile; cerimonie; artefatti; user story; Definition of Done; Iteration Demo; Information Radiator.*

### Che cos'è Agile · [[04_Agile_01_bis.pdf#page=3|p. 3]]–[[04_Agile_01_bis.pdf#page=5|5]]

- **Sondaggio** sui progetti passati: requisiti poco chiari o cambiati durante il progetto? stakeholder disponibili o assenti, problemi di comunicazione? stime dei tempi di sviluppo: sono state fatte e rispettate? problemi o ritardi imprevisti? mancava chiarezza sull'avanzamento del progetto? Da qui: *parliamo di Agile*.
- **Agile** è un **approccio iterativo** alla gestione dei progetti e allo sviluppo dei prodotti che permette ai team di: **consegnare valore più velocemente**; **ricevere feedback continuo**; **ridurre il rischio di grandi errori dovuti a una pianificazione rigida**; **adattarsi al cambiamento**.
- Idea di fondo: evitare il modello «big bang» (un unico rilascio finale) e lavorare per **piccoli incrementi di valore**.

### Il Manifesto Agile: i quattro valori · [[04_Agile_01_bis.pdf#page=6|p. 6]]–[[04_Agile_01_bis.pdf#page=8|8]]

![[lez06-ag-p6-valori-manifesto.png]]
*I quattro valori del Manifesto Agile: individui e interazioni più che processi e strumenti; software funzionante più che documentazione esaustiva; collaborazione col cliente più che negoziazione dei contratti; rispondere al cambiamento più che seguire un piano.*

![[lez06-ag-p7-valori-manifesto-infografica.png]]
*Infografica in italiano: ogni valore con ciò che passa in secondo piano.*

Domanda in aula: quale dei quattro valori, se applicato fin dall'inizio, avrebbe più migliorato i vostri progetti?

### I dodici principi · [[04_Agile_01_bis.pdf#page=9|p. 9]]–[[04_Agile_01_bis.pdf#page=11|11]]

1. La massima priorità è **soddisfare il cliente** con **consegne tempestive e continue** di software di valore.
2. **Accogliere i cambiamenti dei requisiti**, anche a sviluppo avanzato; i processi agili sfruttano il cambiamento a vantaggio competitivo del cliente.
3. **Consegnare software funzionante frequentemente**, da un paio di settimane a un paio di mesi, preferendo la scala più breve.
4. Committenti e sviluppatori devono **lavorare insieme quotidianamente** per tutta la durata del progetto.
5. Costruire i progetti attorno a **individui motivati**: dare loro ambiente e supporto necessari e fidarsi che portino a termine il lavoro.
6. Il metodo più efficiente ed efficace di comunicare informazioni **dentro e verso un team** è la **conversazione faccia a faccia**.
7. **Il software funzionante è la principale misura di avanzamento.**
8. I processi agili promuovono lo **sviluppo sostenibile**: sponsor, sviluppatori e utenti devono poter mantenere **un ritmo costante** indefinitamente.
9. La continua attenzione all'**eccellenza tecnica** e alla buona progettazione aumenta l'agilità.
10. **Semplicità**: l'arte di massimizzare la quantità di lavoro non svolto è essenziale.
11. Le migliori architetture, requisiti e progetti emergono da **team auto-organizzati**.
12. A intervalli regolari il team **riflette su come diventare più efficace**, poi regola e adatta il proprio comportamento.

**I principi in breve** (p. 11): *continuous delivery of value* (consegna continua di valore), *collaboration* (collaborazione), *simplicity* (semplicità), *continuous improvement* (miglioramento continuo).

L'attività di p. 12 è un **«agility check»** in aula (la slide non ha contenuto scritto).

### Come funziona Agile · [[04_Agile_01_bis.pdf#page=13|p. 13]]–[[04_Agile_01_bis.pdf#page=15|15]]

- Ciclo: **Backlog → Priorità → Iterazione → Feedback → Miglioramento.**
- **Agile suddivide il progetto in iterazioni** (p. 14), in quattro passi: **Make a list** (fai una lista: con il cliente si elencano le funzionalità che vorrebbe; diventa la lista delle cose da fare del progetto); **Size things up** (stima le attività, una rispetto all'altra, e indovina quanto tempo servirà per ciascuna); **Set some priorities** (chiedi al cliente di dare una priorità alla lista, così si lavora prima sulle cose più importanti); **Start working**.
- **Pianificazione dell'iterazione** (p. 15): **selezione delle attività prioritarie e definizione dell'obiettivo dell'iterazione.**

![[lez06-ag-p14-progetto-in-iterazioni.png]]
*I quattro passi su riquadri neri con icone (lista, compasso, bersaglio, spunta).*

### Sviluppo iterativo ed evolutivo · [[04_Agile_01_bis.pdf#page=16|p. 16]]–[[04_Agile_01_bis.pdf#page=18|18]]

- Lo sviluppo iterativo è organizzato come una serie di **mini-progetti brevi a durata fissa** (per esempio tre settimane), le **iterazioni**. Ogni iterazione produce un **sistema eseguibile, testato e integrato**, anche se solo parziale, e comprende analisi dei requisiti, progettazione, implementazione e test.
- Il sistema **cresce e si raffina a ogni iterazione** tramite feedback e adattamento ciclici: per questo si chiama sviluppo **iterativo e incrementale**, ed è anche **evolutivo** grazie a feedback e adattamento.

![[lez06-ag-p17-waterfall-vs-iterativo.png]]
*«Waterfall vs iterative». Non così: si consegnano una ruota, poi un asse con due ruote, poi un'auto senza carrozzeria, infine l'auto; il cliente è scontento fino all'ultimo. Così: uno skateboard, un monopattino, una bicicletta, una moto, un'auto; il cliente è sempre più soddisfatto.*

![[lez06-ag-p18-sviluppo-iterativo-evolutivo.png]]
*Due iterazioni consecutive, ciascuna con Requirements → Design → Implementation & Test & Integration → System Test, di 4 settimane (per esempio); il feedback dell'iterazione N raffina requisiti e design della N+1.*

### Ruoli in Agile · [[04_Agile_01_bis.pdf#page=19|p. 19]]–[[04_Agile_01_bis.pdf#page=21|21]]

- **Agile non definisce ruoli specifici: li definiscono i framework**: Scrum, Kanban, Extreme Programming (XP), Disciplined Agile (DA), SAFe, LeSS.
- **Stesse responsabilità, nomi diversi** (p. 20):

| Responsabilità | Scrum | Disciplined Agile | XP | SAFe |
|---|---|---|---|---|
| Definisce il valore | Product Owner | Product Owner | Customer | Product Manager / Product Owner |
| Facilita il team | Scrum Master | Team Lead | Coach | Scrum Master |
| Costruisce il prodotto | Developers | Team Members | Programmers | Agile Team |
| Definisce l'architettura | Team | Architecture Owner | Team | System Architect |
| Fornisce feedback | Stakeholder | Stakeholder | Customer | Business Owner |

- **Tre responsabilità fondamentali** (p. 21): **Product Owner** — visione del prodotto, priorità, valore: «sviluppare il prodotto giusto» (*Developing the Right Product*); **Scrum Master** — facilita il team, rimuove gli ostacoli, promuove Agile: «aiutare il team a lavorare bene»; **Development Team** — progetta, scrive il codice, testa, consegna: «costruire il prodotto nel modo giusto».

### Le quattro cerimonie · [[04_Agile_01_bis.pdf#page=22|p. 22]]–[[04_Agile_01_bis.pdf#page=27|27]]

Planning, daily meeting, demo, retrospective: **iteration planning**, **daily coordination meeting**, **iteration demonstration**, **iteration retrospective**.

| Cerimonia | Scopo | Partecipanti | Frequenza | Durata |
|---|---|---|---|---|
| **Iteration planning** (detta anche «sprint planning») | definire il lavoro e l'obiettivo dell'iterazione; le attività da prioritizzare, le storie e i task concreti della prossima iterazione | membri del team, team lead, product owner | all'inizio di ogni iterazione | circa un'ora per ogni settimana di iterazione |
| **Daily meeting** | allineamento rapido su avanzamento, ostacoli, prossimi passi | membri del team, team lead, product owner | una volta al giorno | circa 15 minuti |
| **Iteration demo** | presentazione del valore generato e raccolta di feedback | membri del team, team lead, PO; stakeholder (opzionali) | alla fine dell'iterazione | circa 30–60 minuti |
| **Retrospective** | riflessione sul processo e azioni di miglioramento | membri del team, team lead, PO | alla fine dell'iterazione | circa 60 minuti |

![[lez06-ag-p24-iteration-planning-tabella.png]]
![[lez06-ag-p25-daily-meeting.png]]
![[lez06-ag-p26-iteration-demo.png]]
![[lez06-ag-p27-retrospective.png]]
*Le tabelle delle slide per ogni cerimonia (partecipanti, frequenza, durata, obiettivo).*

### Artefatti Agile · [[04_Agile_01_bis.pdf#page=28|p. 28]]–[[04_Agile_01_bis.pdf#page=31|31]]

Product backlog, iteration backlog, user story, burndown chart.

| Artefatto | Definizione |
|---|---|
| **Product Backlog** | la lista del lavoro necessario per creare il prodotto; raccoglie tutto il lavoro che arriva al team; il product owner lo ordina per priorità |
| **Iteration Backlog** | la lista del lavoro da completare in un'iterazione, nell'ordine deciso dal team |
| **Burndown Chart** | rappresentazione grafica di quanto velocemente il team procede negli elementi di lavoro; mostra lo sforzo totale per ogni iterazione |
| **User Story** | strumento per descrivere una funzionalità dal punto di vista dell'utente finale: che tipo di utente, cosa vuole e perché |

![[lez06-ag-p30-product-sprint-backlog.png]]
*Lavagna con il Product Backlog (otto user story ordinate per priorità: login sicuro, ricerca prodotti, carrello, pagamento con carta, e-mail di conferma, tracciamento ordine, preferiti, assistenza) e lo Sprint Backlog (obiettivo: checkout fluido; quattro storie con i task relativi), più la Definizione di Fatto (codice sviluppato, test unitari passati, code review, documentazione aggiornata, funzionalità demo-ready).*

**Burndown chart** (p. 31): rappresenta il **lavoro rimanente** (in Story Point), che **diminuisce giorno per giorno fino a zero alla fine dello Sprint**. La **linea tratteggiata** indica il progresso ideale teorico; la **linea viola** il progresso reale del team. **Gestione dei cambiamenti imprevisti:** la **linea blu** in alto evidenzia i **cambiamenti di ambito**, mostrando se durante il lavoro sono stati aggiunti task non pianificati.

![[lez06-ag-p31-burndown-chart.png]]
*Infografica «Il grafico burndown Agile»: story point rimanenti sui giorni dello sprint, progresso ideale, progresso reale e linea dell'ambito, con un picco quando si aggiunge lavoro.*

### User story · [[04_Agile_01_bis.pdf#page=32|p. 32]]–[[04_Agile_01_bis.pdf#page=37|37]]

- Formato: **As a \<user>, I want \<capability>, so that \<benefit>.**
- Una **user story** è un modo di rappresentare una funzionalità o un requisito di valore per un utente o cliente. Comprende **tre aspetti**: una **descrizione scritta** della storia (di alto livello, semplice e breve); una **conversazione** sulla storia per capirne i dettagli; un insieme di **test di accettazione** per stabilire quando la storia è completa.
- **Esempio** (p. 34): descrizione: *un cassiere può inserire gli articoli acquistati dal cliente.* La discussione tra i membri del team chiarisce i dettagli (per esempio gli articoli si inseriscono con un codice e si possono inserire più articoli della stessa categoria). Dalla discussione escono i **test di accettazione**: test con un singolo articolo; con più articoli distinti; con più articoli di cui alcuni della stessa categoria; con un gran numero di articoli.
- **Card** (p. 35): di solito si scrivono su **piccoli cartoncini** (per esempio Post-it); il cartoncino dev'essere piccolo per **evitare troppi dettagli**; i test di accettazione si possono elencare **sul retro**.
- **Template** (p. 36): *As a \<type of user>, I want \<to perform some task>, so that I can \<achieve some goal/benefit/value>.*

![[lez06-ag-p37-esempi-user-story.png]]
*Sei Post-it in italiano di esempi di user story (cercare prodotti, aggiungere al carrello, salvare nei preferiti, reimpostare la password, gestire gli utenti, pagare con PayPal).*

### Chi scrive le user story? · [[04_Agile_01_bis.pdf#page=38|p. 38]]–[[04_Agile_01_bis.pdf#page=39|39]]

- Domanda: «Le user story sono scritte solo dal product owner?» **No.** Il PO è responsabile solo di **aggiungerle al Backlog**, ma **chiunque può scriverle** (di solito sono sviluppate e raffinate in modo collaborativo da tutto il team).

### Dimensione delle storie · [[04_Agile_01_bis.pdf#page=40|p. 40]]–[[04_Agile_01_bis.pdf#page=42|42]]

- In sviluppo Agile è utile avere storie che un programmatore (o una coppia) possa **implementare e verificare entro uno Sprint**: dimensione adatta alla pianificazione iterativa. Una storia può essere sviluppata in **un giorno** o in **un'iterazione di due settimane**.
- **Esempi di dimensione** (p. 41): 1) *Un cassiere può gestire una vendita per un cliente* — **troppo grande**. 2) *Un cassiere può aggiungere a un ordine gli articoli acquistati dal cliente* — **dimensione giusta**. 3) *La ricevuta mostra l'indirizzo del negozio* — **troppo piccola**.
- **Dividere e combinare le storie** (p. 42): una storia troppo grande si chiama **Epic**, e si può dividere in più user story. Esempio: «il cassiere può gestire la vendita al cliente» è un'Epic, divisa in: un cassiere può inserire gli articoli acquistati; un cassiere può vedere il totale della vendita; un cliente può pagare una vendita in contanti; un cliente può ottenere la ricevuta. Una **user story** si può dividere in **task** (creare un'API, creare un form, scrivere test…).

![[lez06-ag-p42-epic-storie-task.png]]
*Epic → user story → task.*

### Le proprietà INVEST · [[04_Agile_01_bis.pdf#page=43|p. 43]]–[[04_Agile_01_bis.pdf#page=45|45]]

**INVEST** = *Independent, Negotiable, Valuable, Estimable, Small, Testable.*

| Proprietà | Significato |
|---|---|
| **Independent** | evitare dipendenze tra storie, per non avere problemi di stima, prioritizzazione e pianificazione |
| **Negotiable** | i dettagli si negoziano durante la discussione, quindi una storia non deve essere troppo dettagliata |
| **Valuable** | per utenti e acquirenti: le storie devono avere valore per gli utenti, a volte anche per gli acquirenti, non solo per gli sviluppatori |
| **Estimable** | il team di sviluppo deve poter stimare il lavoro necessario per ogni storia |
| **Small** | dimensione tale da permettere lo sviluppo in un tempo che va da mezza giornata a, al massimo, due settimane |
| **Verifiable (Testable)** | scritte in modo da poter verificare se sono state sviluppate e completate con successo |

**Esempio PayPal** (p. 45): «Permettere ai clienti di pagare con PayPal» è **troppo complessa: è un'Epic**. Meglio queste storie: *come cliente voglio vedere PayPal tra i metodi di pagamento disponibili; voglio essere reindirizzato a PayPal per autorizzare il pagamento; voglio tornare automaticamente al sito e-commerce dopo il pagamento; voglio ricevere una conferma quando il pagamento è completato; come amministratore voglio registrare l'esito del pagamento PayPal per aggiornare lo stato dell'ordine.*

![[lez06-ag-p45-esempio-paypal-epic.png]]
*L'Epic PayPal e le cinque storie in cui si divide.*

### Revisione delle storie e stima · [[04_Agile_01_bis.pdf#page=46|p. 46]]–[[04_Agile_01_bis.pdf#page=49|49]]

- **User stories review**: attività per controllare la qualità delle user story (o dei requisiti) già definite: sono scritte bene? rispettano i criteri INVEST? come si possono riscrivere?
- **Esercizio** (p. 47): la storia *«As an administrator, I want to manage the platform's users in order to control access and keep their data up to date»* va valutata con la checklist INVEST (per ogni criterio: Yes / Partially / No, con una breve spiegazione se non pienamente soddisfatto), poi: come migliorarla o dividerla?
- **Una possibile soluzione** (p. 48): dividerla in *creare un nuovo account utente per consentire l'accesso alla piattaforma; disattivare un account per impedire l'accesso a utenti non più autorizzati; modificare i dati dell'utente per mantenerli aggiornati.* Le nuove storie sono più focalizzate, ma vanno comunque discusse e verificate rispetto a INVEST.
- **Stima delle user story** (p. 49): le stime sono ipotesi basate sulle informazioni disponibili; argomento della lezione successiva (Lezione 7).

![[lez06-ag-p47-esercizio-invest.png]]
*La tabella della checklist INVEST (criterio, domanda, risultato).*

### Criteri di accettazione e Definition of Done · [[04_Agile_01_bis.pdf#page=50|p. 50]]–[[04_Agile_01_bis.pdf#page=52|52]]

- **Quando una storia è completa?** I **criteri di accettazione** (*acceptance criteria*) sono aspetti dettagliati di un requisito di alto livello dal punto di vista di uno stakeholder, **unici per ogni storia**; la **Definition of Done** è una checklist di ciò che rende «fatta» una storia, **in generale per tutte le storie**.
- I criteri di accettazione spingono il team a considerare i dettagli del requisito **prima di cominciare lo sviluppo**; sono condizioni specifiche che una singola storia deve soddisfare; si integrano con un approccio **BDD** (Behavior-Driven Development) o **ATDD** (Acceptance Test-Driven Development).
- **Esempio** (p. 52): *«As a customer, I want to recover my password so that I can access the system again.»* Discussione: quanto resta valido il link? posso riusare un vecchio link? cosa succede se inserisco un indirizzo e-mail inesistente? riceverò una notifica? c'è una lunghezza minima della password? Criteri di accettazione: 1. il link ricevuto via e-mail è valido 30 minuti; 2. ogni link si può usare una sola volta; 3. la nuova password deve contenere almeno 12 caratteri; 4. se l'indirizzo e-mail non esiste, si mostra un messaggio generico.

![[lez06-ag-p52-criteri-recupero-password.png]]
*Il caso del recupero password con discussione e criteri.*

### Altri esempi di criteri di accettazione · [[04_Agile_01_bis.pdf#page=53|p. 53]]–[[04_Agile_01_bis.pdf#page=54|54]]

**Esempio 1 — login.** Storia: *as a registered user, I want to log in using my email and password to access my personal area.*

| Criterio | Testo |
|---|---|
| AC1 | se e-mail e password sono corrette, l'utente accede alla propria area personale |
| AC2 | se la password è errata, il sistema mostra un messaggio di errore senza specificare quale credenziale è sbagliata |
| AC3 | se uno dei campi è vuoto, il sistema impedisce l'invio della richiesta e evidenzia il campo obbligatorio |
| AC4 | dopo 5 tentativi falliti consecutivi, l'account è bloccato temporaneamente per 15 minuti |
| AC5 | se l'utente è disabilitato, il sistema non consente l'accesso |

**Esempio 2 — ricerca prodotti.** Storia: *as a registered user, I want to search for a product so that I can place an order.*

| Criterio | Testo |
|---|---|
| AC1 | inserendo un nome completo o parziale, si mostrano i prodotti corrispondenti |
| AC2 | la ricerca non distingue maiuscole e minuscole |
| AC3 | se non esistono prodotti corrispondenti si mostra il messaggio «No products found» |
| AC4 | ogni risultato mostra nome, prezzo e disponibilità del prodotto |
| AC5 | se il campo di ricerca è vuoto, il sistema mostra un messaggio che invita a inserire un termine di ricerca |

### BDD, Gherkin e dai criteri ai test · [[04_Agile_01_bis.pdf#page=55|p. 55]]–[[04_Agile_01_bis.pdf#page=61|61]]

- **BDD** (*Behavior-Driven Development*) nasce come evoluzione del **TDD** (Test-Driven Development): invece di concentrarsi sui test tecnici, sposta l'attenzione sul **comportamento atteso del sistema dal punto di vista dell'utente finale**. Coinvolge i cosiddetti **«Three Amigos»** (Business Analyst/Product Owner, sviluppatori, QA/tester) nel definire gli scenari d'uso **prima di scrivere codice**.
- **Sintassi Gherkin** (p. 56): gli scenari sono scritti in un linguaggio naturale strutturato, comprensibile a tutti (tecnici e non), nel formato **Given** (dato un contesto iniziale) · **When** (quando avviene un evento o azione) · **Then** (allora si ottiene un risultato). Obiettivo: creare una **«specifica vivente»** (*living specification*) che sia insieme documentazione e test automatico.

**Dai criteri di accettazione ai test BDD** (recupero password, pp. 57–60)

| Criterio | Scenario | Given / When / Then |
|---|---|---|
| 1 — validità del link di 30 minuti | positivo: link usato entro i 30 minuti | *Given* un utente ha ricevuto il link di reset 20 minuti fa · *When* lo apre · *Then* il sistema permette di inserire una nuova password |
| 1 | negativo: link usato dopo la scadenza | *Given* un utente ha ricevuto il link 35 minuti fa · *When* lo apre · *Then* il sistema lo informa che il link è scaduto *And* gli chiede di richiederne uno nuovo |
| 2 — ogni link una sola volta | riuso di un link già usato | *Given* un utente ha già usato il link · *When* tenta di usarlo una seconda volta · *Then* il sistema rifiuta la richiesta *And* mostra un messaggio che il link non è più valido |
| 3 — password di almeno 12 caratteri | scenario 1: password valida | *Given* un utente ha aperto un link valido · *When* inserisce una password di almeno 12 caratteri · *Then* il sistema aggiorna la password *And* conferma l'operazione |
| 3 | scenario 2: password troppo corta | *Given* un utente ha aperto un link valido · *When* inserisce una password di 8 caratteri · *Then* il sistema la rifiuta *And* lo informa che la lunghezza minima è 12 |
| 4 — e-mail inesistente: messaggio generico | richiesta con e-mail non registrata | *Given* l'e-mail «utente@example.com» non è nel sistema · *When* si richiede il recupero della password · *Then* il sistema mostra un messaggio generico *And* non rivela se l'indirizzo sia registrato |

**Cosa abbiamo scoperto?** (p. 61) Non c'è una corrispondenza uno-a-uno tra criteri di accettazione e scenari BDD: **un solo criterio può richiedere più scenari**; il processo va da un requisito funzionale a test eseguibili; i criteri di accettazione fanno da **ponte tra business, sviluppo e qualità del software**.

### Definition of Done · [[04_Agile_01_bis.pdf#page=62|p. 62]]–[[04_Agile_01_bis.pdf#page=67|67]]

- Domanda: **quando una user story si può considerare completa?** Quando si è finito di scrivere il codice? O…?
- **Definition of Done**: ✅ tutti i criteri di accettazione sono soddisfatti; ✅ il codice è stato rivisto (*code review*); ✅ tutti i test unitari sono passati; ✅ i test di integrazione sono passati; ✅ nessun bug critico è aperto; ✅ la documentazione tecnica è aggiornata; ✅ la funzionalità è stata distribuita nell'ambiente di test; ✅ il Product Owner ha verificato la user story. **Solo a questo punto la storia può passare a Done.**

**Una DoD realistica, da prospettive diverse** (p. 64)

| Prospettiva | Condizioni |
|---|---|
| **Coding** | codice completato; standard di codifica rispettati; code review effettuata |
| **Quality** | test unitari passati; test di integrazione passati; nessun bug bloccante |
| **Documentation** | documentazione tecnica aggiornata; API documentate |
| **Deploy** | build completata con successo; deployment nell'ambiente di test |
| **Business** | criteri di accettazione soddisfatti; il Product Owner approva la user story |

- **Prova a scrivere la tua DoD** (p. 65). **Esempio** (p. 66): codice sviluppato; test eseguiti; code review; documentazione aggiornata; deployment nell'ambiente di test; approvazione del Product Owner.
- **Quando si usa la DoD** (p. 67): guida il team durante tutto lo Sprint. Prima di spostare un elemento in Done il team verifica i suoi criteri di accettazione e tutte le condizioni applicabili della DoD. **Alla Sprint Review è considerato parte dell'Incremento solo il lavoro completato che soddisfa la DoD.** Nella **Sprint Retrospective** il team può rivedere e rafforzare la DoD. **Il lavoro che non soddisfa la DoD non è Done e torna al Product Backlog.**

### Iteration Demo · [[04_Agile_01_bis.pdf#page=68|p. 68]]–[[04_Agile_01_bis.pdf#page=74|74]]

- **Il flusso:** verifica della DoD → demo → feedback → rilascio oppure ritorno al backlog (p. 68).
- **Obiettivi della demo** (p. 69): dimostrare l'incremento ottenuto; verificare che le user story soddisfino i criteri di accettazione; raccogliere suggerimenti e osservazioni; determinare le priorità per il Product Backlog; valutare se il prodotto è pronto per il rilascio.
- **Scopo specifico** (p. 70): **non dimostrare il lavoro del team, ma verificare il valore prodotto e raccogliere feedback**. È un momento di discussione tra team e stakeholder per capire se ciò che è stato sviluppato risponde davvero alle esigenze degli utenti e del business. **Partecipanti:** Product Owner, Scrum Master, Development Team, stakeholder clienti, utenti rappresentativi, sponsor (se opportuno).
- **Come funziona** (p. 71): per esempio in un progetto e-commerce si può mostrare: ricerca prodotti; aggiunta al carrello; pagamento con PayPal; conferma dell'ordine. **Si presentano solo le user story completate**, cioè quelle che soddisfano sia i criteri di accettazione sia la DoD. Il team mostra **software funzionante, non slide o documenti**; ogni funzionalità è dimostrata dal vivo.

![[lez06-ag-p72-agenda-demo.png]]
*Una possibile agenda della demo (esempio «Sprint Review — PayPal Checkout»): 1 Introduzione (5 minuti: il PO ricorda lo Sprint Goal, «permettere ai clienti di completare l'acquisto tramite PayPal»); 2 Dimostrazione (20–40 minuti: login, aggiunta di un prodotto, checkout, pagamento PayPal, conferma dell'ordine); 3 Feedback degli stakeholder; 4 Aggiornamento del backlog (nuove user story, modifica di quelle esistenti, cambio di priorità); il tutto informa il lavoro futuro.*

![[lez06-ag-p73-flusso-complessivo.png]]
*Il flusso complessivo: Product Backlog → Iteration Planning → Iterazione (con Iteration Backlog e Coordination Meeting) → Iteration Review (Demo) → Retrospective; «Product feedback» riporta dalla review al Product Backlog e «Process improvements» dalla retrospettiva alla pianificazione.*

- Domanda in aula (p. 74): il vostro team fa demo? Sì o no? Se sì, come sono condotte?

### Information radiator · [[04_Agile_01_bis.pdf#page=75|p. 75]]–[[04_Agile_01_bis.pdf#page=80|80]]

- In Agile l'obiettivo è che lo **stato del progetto sia visibile a colpo d'occhio**. Gli **information radiator** sono strumenti visivi che rendono **trasparente** lo stato del lavoro: «irradiano» informazioni, così chiunque passi vicino alla lavagna o apra il dashboard capisce subito come procede il progetto.
- **Scrum Board** (p. 77): serve a gestire il lavoro di uno Sprint.
- **Kanban Board** (p. 78): rappresenta invece l'**intero flusso di lavoro**. Kanban introduce i **limiti di Work-in-Progress (WIP)**: un numero massimo di task aperti, per evitare di iniziare molte cose senza finirle; l'obiettivo è ottimizzare il flusso.

![[lez06-ag-p77-scrum-board.png]]
*Scrum Board dello Sprint 4: obiettivo dello sprint, colonne To Do / In Progress (max 3) / Testing / Done con i post-it delle user story e i punti, definizione di Done, legenda dei colori, progresso dello sprint (36 %), note (daily scrum, sprint review e planning successivi).*

![[lez06-ag-p78-kanban-board.png]]
*Kanban Board: Backlog, To Do (max 5), In Progress (max 3), In Review (max 2), Done; legenda dei tipi di lavoro e flusso: Backlog → To Do → In Progress → In Review → Done, con le regole sul WIP («visualizzare il lavoro, limitare il WIP, massimizzare il flusso»).*

**Quando usarli** (p. 79)

| Strumento | Quando | Esempio tipico |
|---|---|---|
| **Scrum Board** | il lavoro si può pianificare; il team lavora a Sprint; c'è un Product Owner; si sviluppano nuove funzionalità | sviluppo di una nuova applicazione |
| **Kanban Board** | arrivano continuamente nuove richieste; è difficile pianificare gli Sprint; le priorità cambiano ogni giorno | Service Desk, DevOps Team, Application Support, Incident Management, manutenzione correttiva |

- **Burndown chart** (p. 80): il grafico rende visibile l'avanzamento e supporta la discussione su ostacoli e adattamenti.

![[lez06-ag-p80-burndown-infografica.png]]
*«The Agile Burndown Chart — visualizing sprint progress»: grafico degli story point rimanenti sui giorni dello sprint con la linea ideale e quella reale; riquadri laterali: valore del burndown (individuare i ritardi, gestire le aspettative, mostrare l'avanzamento), dati chiave (story point iniziali, lavoro completato ogni giorno), «inspect and adapt» (individuare scostamenti dal piano, discutere ostacoli e prossimi passi), trasparenza (condividere lo stato, allineare gli stakeholder).*

### Conclusioni · [[04_Agile_01_bis.pdf#page=81|p. 81]]

- Agile favorisce **adattabilità, collaborazione e miglioramento continuo**.

*Approfondimenti nel wiki: [[sviluppo-agile]], [[cerimonie-e-artefatti-agile]], [[user-stories]], [[criteri-di-accettazione-e-bdd]]*

## Lezione 7 — Agile Project Management (Parte 2): il framework Scrum

*Fonte: 04_Agile_02.pdf (70 pagine, «Agile Project Management (Part 2)», prof.ssa Anna Rita Fasolino). Agenda: dalla gestione tradizionale a Scrum; il framework Scrum; Product Backlog e Sprint Planning; Story Point, velocity e capacity; eventi Scrum; workshop (valutazione Agile e pianificazione del primo Sprint).*

### Premessa sulla gestione di progetto · [[04_Agile_02.pdf#page=3|p. 3]]–[[04_Agile_02.pdf#page=7|7]]

**Gestione di progetto tradizionale** (p. 4): il lavoro è pianificato nel dettaglio all'inizio del progetto; il **piano è lo strumento principale di controllo**.

**Quando funziona bene** (p. 5): l'approccio guidato dal piano è molto efficace quando i **requisiti sono stabili**, la **tecnologia è consolidata**, il **prodotto è ben definito**, i **cambiamenti sono limitati** (costruire un ponte, un edificio, installare un impianto industriale). Ma se i requisiti cambiano continuamente, il cliente scopre nuovi bisogni, la tecnologia evolve durante il progetto, gli utenti vedono il software e cambiano idea, restare fedeli a un piano dettagliato definito mesi prima diventa difficile.

**Gestione Agile** (p. 6): richiede un approccio diverso, adattato allo sviluppo incrementale e alle pratiche dei metodi Agile.

**Plan-driven vs Agile** (p. 7)

| Plan-driven | Agile |
|---|---|
| piano dettagliato | visione del prodotto (*Product Vision*) |
| esecuzione del piano | Sprint |
| monitoraggio delle deviazioni dal piano | feedback |
| | adattamento continuo |

### Gestione di progetto e buone pratiche di sviluppo · [[04_Agile_02.pdf#page=8|p. 8]]–[[04_Agile_02.pdf#page=10|10]]

- In molti progetti la gestione non è presa sul serio: l'attenzione è sulle buone pratiche di sviluppo (design pattern, stili architetturali, principi di progettazione, *clean code*). Ma **senza una gestione strutturata è facile perdere visibilità** su stato reale del lavoro, priorità e lavoro rimanente.
- **Agile non sostituisce le competenze tecniche**: fornisce un quadro per organizzare il lavoro, rendere trasparente l'avanzamento e adattarsi al cambiamento.
- **Analizzare i vostri progetti passati** (p. 9): avete applicato design pattern, architettura software, principi SOLID, *clean code*, Git, testing. Ma: sapevate esattamente quanto lavoro restava? quali funzionalità erano le più importanti? c'era una lista condivisa dei compiti da completare? sapevate cosa si poteva rilasciare oggi? tutti avevano la stessa visione dello stato del progetto? Se avete risposto spesso «non sempre», **mancava un framework di gestione del progetto**.

### Scrum · [[04_Agile_02.pdf#page=11|p. 11]]–[[04_Agile_02.pdf#page=14|14]]

- **Scrum** è un framework Agile per gestire lo sviluppo di **prodotti complessi**, introdotto nei primi anni '90 da **Ken Schwaber e Jeff Sutherland**. Si basa su un approccio **iterativo e incrementale** e organizza il lavoro in **Sprint, ruoli, eventi e artefatti**. **Non prescrive come sviluppare il software**: dà una struttura dentro cui i team adottano le pratiche tecniche più adatte (per esempio TDD, Pair Programming, Continuous Integration).
- **Dalla Scrum Guide** di Schwaber e Sutherland (p. 12): Scrum si fonda sulla teoria del **controllo empirico del processo** (**empirismo**): la conoscenza viene dall'esperienza e le decisioni si basano su ciò che è noto. Usa un metodo iterativo e un approccio incrementale per ottimizzare la prevedibilità e controllare il rischio.
- **I tre pilastri** (p. 13): **trasparenza** del processo; **ispezione frequente** del prodotto in costruzione; **adattamento** del processo o del prodotto, se necessario.
- **Elementi del framework** (p. 14): lo **Scrum Team** e: **ruoli**, **eventi**, **artefatti**, **regole** che legano insieme eventi, ruoli e artefatti governandone relazioni e interazioni.

### Lo Scrum Team e i ruoli · [[04_Agile_02.pdf#page=15|p. 15]]–[[04_Agile_02.pdf#page=18|18]]

- Lo Scrum Team comprende tre ruoli: **Product Owner** (definisce le funzionalità del prodotto e le loro priorità); **Development Team** (team auto-organizzato e molto autonomo, non più di 7–8 persone); **Scrum Master** (aiuta il gruppo a imparare e applicare Scrum). **Massimo 10 persone in totale**, inclusi PO e Scrum Master.
- **Product Owner**: responsabile di **massimizzare il valore del prodotto** e del lavoro del Development Team.
- **Scrum Master**: responsabile di **promuovere e supportare Scrum**, aiutando tutti a comprendere teoria, pratiche, regole e valori di Scrum.
- **Development Team**: **numero limitato (7–8) di professionisti** che lavorano per consegnare un Incremento di prodotto finito e potenzialmente rilasciabile.

![[lez07-ag2-p16-po-responsabilita.png]]
*Il Product Owner: decide cosa deve essere fatto (funzionalità, priorità, quando rilasciare); ha un'ampia conoscenza dei bisogni degli utenti finali; sa gestire gli stakeholder; ha un'idea dei processi di sviluppo software e sa comunicare la propria visione al team; il suo scopo principale è produrre valore per l'utente finale e per l'azienda.*

![[lez07-ag2-p17-scrum-master.png]]
*Lo Scrum Master: aiuta gli stakeholder a comprendere i valori di Scrum; guida l'adozione di Scrum nell'organizzazione; facilita gli eventi Scrum come richiesto e necessario (verso il Product Owner); fa da coach Scrum al Dev Team.*

![[lez07-ag2-p18-development-team.png]]
*Il Development Team: cross-funzionale, con tutte le competenze necessarie per creare un Incremento; auto-organizzato; ogni membro allocato al 100 % sul progetto; Scrum non riconosce titoli ai membri; le competenze specialistiche non tolgono che la responsabilità sia del team nel suo complesso; dà indicazioni e suggerimenti al Product Owner per migliorare il prodotto.*

### Gli Sprint · [[04_Agile_02.pdf#page=19|p. 19]]

- Il cuore di Scrum è lo **Sprint**: periodo a durata fissa (*time-boxed*), di norma **un mese o meno**, in cui si crea un incremento di prodotto **utilizzabile e potenzialmente rilasciabile**.
- Gli Sprint hanno **durata costante** per tutto il progetto. Alla fine di uno Sprint, **il successivo comincia subito**.

### Il ciclo di vita di un progetto Scrum · [[04_Agile_02.pdf#page=20|p. 20]]–[[04_Agile_02.pdf#page=21|21]]

Anche se Scrum è basato solo su una successione di Sprint, il ciclo di vita si può vedere in **tre macro-fasi**:
- **Inception** (avvio): fase di pianificazione in cui si stabiliscono gli obiettivi generali del progetto e si progetta l'architettura software. **Uscite:** visione del prodotto, Product Backlog iniziale, team e ambiente di sviluppo.
- **Construction**: l'inception è seguita da una serie di cicli di Sprint, ciascuno dei quali sviluppa un incremento di sistema.
- **Transition** (chiusura): conclude il progetto, completa la documentazione richiesta (schermate di aiuto e manuali utente compresi) e valuta le lezioni apprese.

![[lez07-ag2-p20-ciclo-di-vita-progetto.png]]
*Otto Sprint verso la «Next Release»; sotto, Inception («Envision and plan»), Construction («Incrementally build a consumable solution»), Transition («Release solution»).*

### Product Vision · [[04_Agile_02.pdf#page=22|p. 22]]–[[04_Agile_02.pdf#page=23|23]]

- La **Product Vision** descrive lo scopo del prodotto e il valore che intende generare. Risponde a: quale problema vogliamo risolvere? per chi sviluppiamo il prodotto? quale valore offrirà agli utenti? come sapremo se il prodotto ha successo? **Resta stabile nel tempo** e guida tutte le decisioni sul Product Backlog.
- **Esempio — piattaforma e-commerce:** *Visione:* permettere ai clienti di acquistare prodotti online in modo rapido, sicuro e semplice da qualsiasi dispositivo. *Utenti:* clienti; amministratori del negozio. *Valore:* ridurre il tempo per completare un acquisto; aumentare le vendite online; migliorare l'esperienza del cliente.

### Inception e formazione del team · [[04_Agile_02.pdf#page=24|p. 24]]

- Uno Scrum Team deve essere **cross-funzionale**: devono essere presenti tutte le competenze necessarie a produrre un incremento (Developer, UX, Tester, DBA, DevOps, Security…). Il team si **auto-organizza**, assegnandosi le varie responsabilità.
- **Chi sarà il PO?** Si sceglie tra: il cliente; un Business Analyst; un Product Manager; un istruttore (nel vostro laboratorio); un senior developer con profonda conoscenza del dominio. Il PO capisce i bisogni degli stakeholder, decide le priorità, mantiene il Product Backlog e massimizza il valore del prodotto.

### Gli artefatti Scrum · [[04_Agile_02.pdf#page=25|p. 25]]–[[04_Agile_02.pdf#page=28|28]]

- **Product Backlog**: lista ordinata degli elementi necessari per completare il prodotto; l'ordine stabilisce la priorità. **Sprint Backlog**: piano di sviluppo dettagliato di ogni Sprint; insieme di elementi (task da completare per costruire il prodotto). **Potentially Shippable Product Increment**: tutto ciò che è prodotto durante uno Sprint; in alcuni casi coincide con lo Sprint Backlog.

![[lez07-ag2-p25-artefatti-scrum.png]]
*Product Backlog → Sprint Backlog → ciclo di 2–4 settimane (con ciclo da 24 ore) → Potentially shippable Product Increment.*

- **Product Backlog e Sprint Backlog** (p. 26): il PO definisce nel Product Backlog le funzionalità da costruire (lista prioritaria). Contiene **user story, bug, miglioramenti, debito tecnico e spike**, tutti prioritizzati dal PO. Mentre il lavoro procede, il backlog è aggiornato e raffinato. All'inizio di ogni Sprint il team seleziona un insieme di elementi da sviluppare in quell'iterazione e crea lo Sprint Backlog (i task da eseguire per raggiungere lo Sprint Goal).
- **Un esempio di backlog** (p. 27, «una specie di lista TODO»): ogni attività ha una stima di impegno e in Scrum si stima di norma in story point.

| Ordine | ID | Elemento | Tipo | Stato | Stima |
|---|---|---|---|---|---|
| 1 | 121 | As an Administrator, I want to link accounts to profiles, so that customers can access new accounts | Requirement | Not Started | 5 |
| 2 | 113 | Update requirements traceability matrix | Overhead | Not Started | 2 |
| 3 | 403 | As a Customer, I want to transfer money between my active accounts, so that I can adjust each account's balance | Improvement | Not Started | 3 |
| 4 | 97 | Refactor Login Class | Maintenance | Not Started | 8 |
| 5 | 68 | As a Site Visitor, I want to find locations, so that I can use bank services | Requirement | Not Started | 8 |

![[lez07-ag2-p28-product-e-sprint-backlog.png]]
*Dal Product Backlog (work item 1…n) allo Sprint Backlog (i primi work item, ciascuno scomposto in task) e all'incremento di prodotto.*

### Un backlog che evolve · [[04_Agile_02.pdf#page=29|p. 29]]–[[04_Agile_02.pdf#page=31|31]]

- La prima bozza del backlog definisce solo i requisiti inizialmente noti e meglio compresi. Il Product Backlog **evolve** durante gli Sprint, come il prodotto e l'ambiente in cui sarà usato. Il **Backlog Refinement** è l'atto di aggiungere **dettaglio, stime e ordine** agli elementi del Product Backlog; è un processo continuo in cui PO e Development Team collaborano sui dettagli.
- **Esempio — backlog iniziale di un e-commerce** (p. 30): 1 Login; 2 Product search; 3 Shopping cart; 4 PayPal checkout; 5 Wishlist; 6 Product reviews; 7 Mobile app; 8 AI-powered product recommendations. Gli elementi iniziali sono meno vaghi dei successivi (si veda il 7) e dovranno essere raffinati prima del prossimo Sprint.
- **Raffinare la user story «Login»** (p. 31): da *«As a user, I want to log in.»* a *«As a registered user, I want to authenticate using my email and password to access my personal area.»* Si aggiungono i **criteri di accettazione** (e-mail obbligatoria; password obbligatoria; messaggio di errore; blocco dopo 5 tentativi); poi il team la **stima: 3 Story Point**. **Ora è pronta.** Intanto la storia «Mobile App» resta semplicemente *«Create a mobile app»*: nessuno perde tempo a discuterne, perché probabilmente non sarà sviluppata prima di sei mesi.

### Quando una user story è pronta (Ready) · [[04_Agile_02.pdf#page=32|p. 32]]–[[04_Agile_02.pdf#page=34|34]]

- Esempio: *«As a customer, I want to recover my password.»* È pronta? Domande: è chiara? è abbastanza piccola? ha criteri di accettazione? è stimata? è indipendente? è verificabile? **Se la risposta è sì… allora è READY.**
- **Prossimo Sprint tra due settimane** (p. 33): solo i primi 2 o 3 elementi saranno candidati allo Sprint.

| Elemento | Stato |
|---|---|
| Login | Ready |
| Product search | Ready |
| Shopping cart | Almost ready |
| PayPal | Needs further clarification |
| Wishlist | Too broadly defined |
| Mobile app | Just an idea |

- **Il flusso complessivo** (p. 34): *Product Backlog → Backlog Refinement (chiarimento, scomposizione, stima…) → elementi del Product Backlog «Ready» → Sprint Planning → Sprint Backlog.* Il Backlog Refinement **prepara** il lavoro; lo Sprint Planning **seleziona** il lavoro.

### Sprint Backlog con task dettagliati · [[04_Agile_02.pdf#page=35|p. 35]]–[[04_Agile_02.pdf#page=37|37]]

- **Lo Sprint è pianificato in Story Point; l'esecuzione quotidiana può essere organizzata tramite task**, che possono essere stimati in ore (esempio: foglio di calcolo con obiettivo «Completare User Account», storie *«As a user I want to login so that I can access the user area»* (3 SP) con i task Create login form UI, Create login form controller, Create login business logic, Implement "remember me" check, Write Selenium test case, Manual test on device; e *«As a user I want to logout so that I can browse the website anonymously»* (1 SP) con i task Create logout business logic, Check if logout button is present on UI, Manual test on device; per ogni task ore pianificate e ore rimanenti giorno per giorno su due settimane).

![[lez07-ag2-p35-sprint-backlog-task.png]]
*Il foglio dello Sprint Backlog con ID, storia/task, story point, commenti, ore pianificate e ore rimanenti per giorno.*

- **Potentially Shippable Product Increment** (p. 36): l'insieme delle funzionalità completate in uno Sprint che soddisfano la **Definition of Done** e che potrebbero essere rilasciate agli utenti, anche se si decide di non farlo. Devono: soddisfare i criteri di accettazione; essere testate; essere integrate; essere distribuite nell'ambiente previsto.

### Gli eventi Scrum · [[04_Agile_02.pdf#page=38|p. 38]]–[[04_Agile_02.pdf#page=40|40]]

- Scrum usa **eventi prestabiliti** per creare regolarità e ridurre le riunioni non definite da Scrum. **Ogni evento è a tempo fisso (*time-boxed*)**: la durata non si può cambiare una volta iniziato. Ogni evento è un'opportunità formale di **ispezionare e adattare** qualcosa. Gli eventi sono: **Sprint, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective** (p. 39).
- Diagramma «Scrum Activities»: 1. Sprint Planning → 2. Daily Scrum (ripetuto) → 3. Sprint Review → 4. Sprint Retrospective; fuori dall'anello, 5. Product Backlog Refinement.
- **Sprint** (p. 40): ogni Sprint ha un obiettivo da raggiungere, un piano flessibile per raggiungerlo, il lavoro svolto e il risultato, e comincia subito dopo la fine dello Sprint precedente. Uno Sprint troppo lungo permette che la definizione di ciò che si costruisce cambi, aumentando complessità e rischi. **Il lavoro da svolgere (definito nello Sprint Backlog) non è obbligatorio, ma è una previsione**: l'unico contenitore dello Sprint è il timebox, non il lavoro pianificato.

### Sprint Goal · [[04_Agile_02.pdf#page=41|p. 41]]–[[04_Agile_02.pdf#page=42|42]]

- **Uno Sprint non è una collezione casuale di user story**: è un insieme di storie che, insieme, permettono di raggiungere uno specifico obiettivo di business che genera valore. Lo **Sprint Goal** è l'obiettivo dello Sprint e le storie selezionate devono contribuire a raggiungerlo.
- **Esempi** (p. 42): se per lo Sprint ho scelto *Login, PayPal, PDF Report, Dashboard, Translation*, qual è l'obiettivo? «Beats me!!» Se scelgo *Cart, Checkout, Payment, Order confirmation*, l'obiettivo è chiaro: **permettere ai clienti di completare un acquisto online**.

### Sprint Planning · [[04_Agile_02.pdf#page=43|p. 43]]–[[04_Agile_02.pdf#page=46|46]]

- Lo Sprint Planning individua lo **Sprint Goal** e il lavoro necessario per raggiungerlo. Il lavoro è selezionato dal Product Backlog e aggiunto allo Sprint Backlog; è pianificato dall'**intero Scrum Team**; l'evento è a tempo fisso e la durata varia con la lunghezza dello Sprint.
- Il **PO presenta gli elementi a priorità più alta** del Product Backlog; il **Development Team valuta le user story**: contribuiscono allo Sprint Goal? abbiamo capacità sufficiente? possiamo completarle nello Sprint? **Solo allora** alcune storie sono selezionate e diventano parte dello Sprint Backlog. La selezione si basa sullo **Sprint Goal**, sulle **storie stimate** e sulla **velocity** del team.

![[lez07-ag2-p45-sprint-planning.png]]
*Sprint Planning: 1 Product Backlog (il PO presenta gli elementi più prioritari) → 2 Discuss & Select (gli sviluppatori valutano e scelgono: supporta lo Sprint Goal? abbiamo capacità? possiamo completarla nello Sprint?) → 3 Sprint Backlog (storie scelte + piano di task); criteri di selezione: Sprint Goal, stime delle storie, capacità disponibile, velocity passata («informa la previsione, non è un impegno fisso»); l'intero Scrum Team collabora; a tempo fisso.*

### Stimare le user story · [[04_Agile_02.pdf#page=47|p. 47]]–[[04_Agile_02.pdf#page=50|50]]

- **Quando e da chi** (p. 47): la stima avviene durante il **Backlog Refinement** ed è fatta dal **Development Team**, perché sono gli sviluppatori a capire complessità tecnica, rischi, dipendenze e lavoro coinvolto. Il Product Owner può chiarire il requisito ma **non assegna gli Story Point**.
- **Come si stima** (p. 48): non si stima il tempo; si stima la **dimensione relativa** della user story. Gli **Story Point** rappresentano una combinazione di **complessità, quantità di lavoro, rischio, incertezza**. Il metodo più usato è il **Planning Poker**.
- **Planning Poker** (p. 49): tecnica di stima agile basata su discussione e consenso; tutti stimano in modo indipendente, poi si discute per arrivare a un consenso. **Perché usarlo:** coinvolgimento del team, stime più accurate, rende evidente l'incertezza, consenso e impegno. **Quando:** durante il Backlog Refinement, prima dello Sprint Planning, per stimare storie o lavoro tecnico di dimensione comparabile. **La scala:** carte 1, 2, 3, 5, 8, 13, 21, ? (valori che crescono in modo non lineare; dimensione relativa, non tempo; «?» = «non lo so»/«troppo incerto»). **I passi:** 1 presenta (il PO presenta la storia); 2 fai domande (il team chiarisce i dubbi); 3 stima in privato (ognuno sceglie segretamente una carta); 4 scopri (tutti scoprono la carta insieme); 5 discuti (differenze e ragioni); 6 ristima (se serve, nuova carta in privato); 7 raggiungi il consenso (si ripete fino al consenso). Obiettivo: una comprensione e una stima condivise, non una media. **Esempio:** storia *«As a user, I want to recover my password so that I can access the system again»*; Anna, Luca, Marco, Sara scelgono 3, 5, 3, 8; si discute (perché 8? perché 3? quali rischi?); dopo la ristima si arriva a **5** («Consensus reached!»). **Consigli:** stimare storie di dimensione comparabile; evitare l'ancoraggio sulle prime stime; incoraggiare tutti a spiegare le proprie stime; usare la scala in modo coerente nel tempo; accettare «I don't know» quando l'incertezza è alta.

![[lez07-ag2-p49-planning-poker.png]]
*L'infografica «Planning Poker — Estimate together, estimate better» con i nove riquadri.*

- **Perché Fibonacci, invece del tempo** (p. 50): *perché si stima la complessità, non il tempo.* (1) Confrontare è più facile che misurare: «chi è più grande tra topo, cane, elefante?» è facile, «quanto pesa un elefante?» no. (2) Si usa un riferimento (il topo = 1 punto) e si stima in modo relativo. (3) La **sequenza di Fibonacci** 1, 2, 3, 5, 8, 13, 21… cresce in modo non lineare, con intervalli sempre più ampi che riflettono l'incertezza crescente con la complessità. (4) Esempio con gli animali: topo 1, gatto 2, cane 3, cavallo 8, elefante 21. (5) Esempio con user story: Change the logo 1; Password recovery 3; Product search 5; Shopping cart 8; PayPal payment 13 («perché non 11? la precisione artificiale non aiuta»). (6) Perché non una scala 1–10: «7 o 8?», «9 o 10?» sono distinzioni inutili; con Fibonacci PayPal payment = 8 e un nuovo motore di ricerca = 13. **Messaggio chiave:** Fibonacci non rende le stime più precise; ci aiuta ad accettare che la precisione diminuisce al crescere della complessità.

![[lez07-ag2-p50-perche-fibonacci.png]]
*L'infografica «Why do we use Fibonacci?» con i sei riquadri.*

### Velocity e capacity · [[04_Agile_02.pdf#page=51|p. 51]]–[[04_Agile_02.pdf#page=54|54]]

- **Velocity** (p. 51): numero di Story Point che un team completa durante uno Sprint. Contano solo le storie **completate**: quelle che soddisfano la Definition of Done e fanno parte dell'Incremento; le storie iniziate ma non finite non contribuiscono. Serve soprattutto a **pianificare gli Sprint futuri**: aiuta a decidere quanto lavoro sia realistico includere.
- **Esempio** (p. 52): velocity degli ultimi sprint: Sprint 1 = 28; Sprint 2 = 31; Sprint 3 = 30; Sprint 4 = 29. Si calcola la **media** delle storie completate negli sprint recenti: la velocity è circa **30 SP**; per il prossimo sprint si selezionano storie per circa 30 SP. All'inizio di un progetto la velocity è spesso instabile, ma poi si stabilizza.
- **Inizio del primo Sprint** (p. 53): la velocity non è ancora disponibile; si può solo fare una stima iniziale e la velocity reale si determina alla fine dello Sprint. **Anche se la stima iniziale era sbagliata, non è un problema: stavamo sperimentando…**
- **Velocity vs capacity** (p. 54): la **capacity** rappresenta la disponibilità effettiva del team; se un membro è assente per alcuni giorni la capacity diminuisce proporzionalmente. Esempio: la capacity di un team di **7 persone** su **2 settimane (10 giorni lavorativi)** è normalmente $7 \times 10 = 70$ giorni-persona. Se una persona è in ferie per 5 giorni e uno sviluppatore è assente 2 giorni, la capacity si riduce del **10 %**. Per la stima successiva gli Story Point del backlog si riducono del 10 %.

### Daily Scrum · [[04_Agile_02.pdf#page=55|p. 55]]–[[04_Agile_02.pdf#page=59|59]]

- Nel Daily Scrum il Development Team **sincronizza il proprio lavoro** e **pianifica le attività della giornata** per avvicinarsi allo Sprint Goal. Di preferenza: ogni giorno dello Sprint, alla stessa ora, nello stesso luogo (fisico o virtuale). **Non è un resoconto**: serve a verificare il progresso verso lo Sprint Goal, individuare gli impedimenti, coordinare il lavoro del team, adattare il piano per le prossime 24 ore.

![[lez07-ag2-p55-daily-scrum.png]]
*Daily Scrum — 15 minuti; ogni giorno dello Sprint, stessa ora, stesso luogo; quattro passi: check progress, identify impediments, coordinate work, adapt the plan. «A planning conversation, not a status report.»*

- **Come è cambiato** (p. 57): **ieri** si chiedeva *cosa hai fatto ieri? cosa farai oggi? quali problemi hai?*; **oggi** si preferisce una conversazione sullo Sprint Goal: *a che punto siamo rispetto allo Sprint Goal? cosa dobbiamo fare oggi per avvicinarci all'obiettivo? ci sono impedimenti che possono rallentare lo Sprint?* Così il focus passa dai task individuali al risultato del team.

![[lez07-ag2-p58-daily-scrum-board.png]]
*«Daily Scrum: the scrum board at the center»: Sprint Goal («Enable users to recover their password securely and easily») → Scrum Board come information radiator (To Do / In Progress / Test / Done con post-it) → Daily Scrum; si ispeziona la board da destra a sinistra, si individuano impedimenti, si concorda cosa completare oggi; esempio di conversazione tra Marco, Sara e Luca con la decisione di lavorare insieme subito dopo il Daily su un problema di token.*

**Falsi miti sul Daily Scrum** (p. 59)

| ❌ Mito | ✅ Realtà |
|---|---|
| è la riunione dello Scrum Master | è la riunione del Development Team |
| serve per fare report | serve a pianificare le prossime 24 ore |
| ognuno parla del proprio lavoro | il team riesamina il flusso di lavoro sulla Scrum Board |
| serve a controllare le persone | facilita il coordinamento per raggiungere lo Sprint Goal |
| i problemi si risolvono durante il Daily | i problemi si individuano nel Daily e si affrontano subito dopo, coinvolgendo solo le persone interessate |

### Sprint Review · [[04_Agile_02.pdf#page=60|p. 60]]–[[04_Agile_02.pdf#page=62|62]]

- La Sprint Review è un **incontro informale**, di **al più quattro ore per uno Sprint di un mese**, in cui Scrum Team e stakeholder collaborano per **ispezionare l'incremento completato** a fine Sprint e, se necessario, **adattare il Product Backlog** per cogliere nuove opportunità. In base a ciò che è stato realizzato e ai cambiamenti del backlog, i partecipanti decidono cosa si può fare per ottimizzare il valore del prodotto; le decisioni dipendono anche da cambiamenti di mercato o uso potenziale del prodotto, budget e tempo disponibili per gli Sprint successivi. **Esito:** un Product Backlog rivisto che definisce il lavoro probabilmente scelto per il prossimo Sprint.
- **NOTA: la Sprint Review non è una DEMO!** È un'occasione per ispezionare il prodotto, raccogliere feedback e aggiornare il backlog.

![[lez07-ag2-p61-sprint-review.png]]
*Sprint Review: cos'è (sessione informale a fine Sprint, prima della Retrospective, fino a 4 ore per uno Sprint di un mese; partecipano Scrum Team e stakeholder chiave), cosa si fa (presentare l'Incremento, raccogliere feedback, discutere e adattare, aggiornare il Product Backlog), esiti e benefici, esempio «Speed Boat Game» (le funzionalità sono isole da raggiungere con un budget limitato: gli stakeholder scelgono insieme quali visitare per prime).*

### Sprint Retrospective · [[04_Agile_02.pdf#page=63|p. 63]]–[[04_Agile_02.pdf#page=67|67]]

- **La Sprint Review migliora il prodotto; la Sprint Retrospective migliora il modo di lavorare del team** (p. 63).
- **Obiettivi** (p. 64): analizzare come è stato condotto il lavoro durante lo Sprint; individuare punti di forza e aree di miglioramento; migliorare il processo di sviluppo; aumentare la qualità del prodotto con il miglioramento continuo. **Partecipanti:** Product Owner, Scrum Master, Development Team. **Durata:** a tempo fisso, al massimo 3 ore per uno Sprint di un mese, proporzionalmente meno per Sprint più brevi.
- **Il team riflette su tre domande** (p. 65): 1 **cosa è andato bene?** (collaborazione efficace, stime realistiche, pochi bug, buona comunicazione); 2 **cosa si potrebbe migliorare?** (troppe user story aperte contemporaneamente, ritardi nei test, Product Backlog poco chiaro, dipendenze tra sviluppatori); 3 **cosa faremo esattamente nel prossimo Sprint?** (il team definisce azioni di miglioramento: limitare il Work In Progress; code review quotidiane; coinvolgere prima il Product Owner; scrivere i criteri di accettazione durante il Refinement; programmazione in coppia per le storie più complesse).

**Osservazione → causa → azione** (p. 66)

| Osservazione | Possibile causa | Azione per il prossimo Sprint |
|---|---|---|
| Abbiamo iniziato troppe user story contemporaneamente | troppo Work in Progress (WIP) | limitare a due le storie in «In Progress» |
| I test si sono fatti solo negli ultimi due giorni | il tester è stato coinvolto troppo tardi | coinvolgere il tester dall'inizio di ogni storia |
| Alcune user story erano poco chiare | criteri di accettazione insufficienti | raffinare di più il Product Backlog prima dello Sprint Planning |
| Le stime erano troppo ottimistiche | requisiti non ben compresi | fare più domande nel Backlog Refinement e coinvolgere più attivamente il PO |
| Il PO aveva disponibilità limitata | comunicazione scarsa | fissare una sessione settimanale regolare di Backlog Refinement |
| Abbiamo trovato molti bug durante la demo | mancavano code review e test continui | code review obbligatorie e Continuous Integration |
| Il Daily Scrum è durato 30 minuti | si è cercato di risolvere i problemi durante la riunione | Daily entro 15 minuti, discussioni tecniche subito dopo |
| Non abbiamo raggiunto lo Sprint Goal | abbiamo preso troppo lavoro | pianificare meno Story Point per il prossimo Sprint |

- **Retrospettiva su uno dei vostri progetti passati** (p. 67): qual è stato il problema più frustrante? quale azione concreta introdurreste per evitare che si ripeta? **Ogni retrospettiva dovrebbe produrre al massimo 2–3 azioni di miglioramento**: cercare di migliorare tutto insieme porta quasi sempre a nessun miglioramento; meglio poche azioni chiare e verificabili per lo Sprint successivo.

### Panoramica finale · [[04_Agile_02.pdf#page=68|p. 68]]–[[04_Agile_02.pdf#page=70|70]]

![[lez07-ag2-p68-cerimonie-scrum.png]]
*Le quattro cerimonie Scrum: Daily Scrum Meeting, Sprint Planning Meeting, Sprint Review Meeting, Sprint Retrospective Meeting.*

![[lez07-ag2-p69-scrum-lifecycle.png]]
*Scrum a colpo d'occhio: input da dirigenti, team, stakeholder, clienti, utenti → Product Owner; Product Backlog (lista ordinata) → Sprint Planning Meeting → Sprint Backlog → Sprint di 1–4 settimane con Daily Scrum ogni 24 ore → lavoro finito → Sprint Review → Sprint Retrospective; Scrum Master e burndown/up chart; «la data di fine Sprint e ciò che il team consegna non cambiano».*

- L'ultima slide introduce il workshop: **«Now let's use Scrum in our project!»**

*Approfondimenti nel wiki: [[gestione-progetto-plan-driven-vs-agile]], [[scrum]], [[ciclo-di-vita-scrum]], [[product-backlog-e-sprint-backlog]], [[sprint-e-sprint-planning]], [[stima-story-points-velocity-capacity]], [[planning-poker]], [[daily-scrum-review-retrospective]]*

## Lezione 8 — Stili architetturali

*Fonte: 05_Architectural_Styles_Complete.pdf (157 pagine, «Architectural Styles», prof.ssa Anna Rita Fasolino, basato sul capitolo 4 di Taylor, Medvidovic e Dashofy).*

**Come è organizzata la lezione.**

- La lezione è un **catalogo di stili architetturali**. Per ogni stile dice:
  - quali elementi usa (componenti, connettori, dati);
  - come possono essere collegati;
  - quali qualità favorisce e quali limiti ha.
- L'esempio che ritorna in tutta la lezione è **Lunar Lander**, un semplice videogioco: il giocatore guida l'atterraggio di una navicella sulla Luna.
  - A ogni passo il giocatore sceglie quanto carburante bruciare, il **burn rate** (in figura *br*).
  - Il programma ricalcola **altitudine** (*a*), **velocità** (*v*), **carburante** (*f*, fuel) e **tempo** (*t*) e li mostra.
  - Lo stesso gioco viene riprogettato in quasi ogni stile: confrontando le versioni si vede cosa cambia da uno stile all'altro.

### Che cos'è uno stile architetturale · [[05_Architectural_Styles_Complete.pdf#page=2|p. 2]]–[[05_Architectural_Styles_Complete.pdf#page=3|3]]

#### Definizione · [[05_Architectural_Styles_Complete.pdf#page=2|p. 2]]

- Uno **stile architetturale** (*architectural style*) è un insieme di decisioni di progetto architetturale a cui si dà un nome (ad es. «client–server», «pipe and filter»). Queste decisioni:
  1. **valgono in un certo contesto di sviluppo**: hanno senso solo per un certo tipo di sistema, con certe caratteristiche. Fuori da quel contesto possono diventare un ostacolo (🧩 lo stile batch sequential va bene per elaborare a lotti le transazioni bancarie, ma applicato al Lunar Lander, un gioco interattivo, non funziona: lo si vede più avanti nella lezione);
  2. **limitano le scelte** che si possono fare nei singoli sistemi di quel contesto: chi adotta lo stile deve rispettarne le regole;
  3. **favoriscono qualità desiderabili** nei sistemi che ne risultano.
- 🧩 *Esempio.* Lo stile pipe and filter impone che i componenti si scambino dati solo attraverso canali e non condividano variabili. Chi progetta un sistema in questo stile sceglie quanti componenti creare e cosa fa ciascuno, ma non può farli comunicare in altro modo. In cambio ottiene componenti riusabili ed eseguibili in parallelo.
- **Rispetto ai pattern architetturali, gli stili sono meno legati a un dominio applicativo**: descrivono come è organizzato un sistema, non a quale tipo di applicazione serve. Lo stesso stile va bene per un compilatore, un gioco o un sistema bancario.
- Uno stile si può applicare a **livelli diversi**: dalla struttura di poche subroutine fino alla struttura complessiva di un'applicazione.

#### Dove si collocano gli stili · [[05_Architectural_Styles_Complete.pdf#page=3|p. 3]]

![[lez08-stili-p3-ambito-degli-stili.png]]
*La mappa colloca quattro tipi di soluzione di progetto su due assi. Asse verticale: quanta conoscenza del dominio applicativo incorporano, da superficiale (in basso) a profonda (in alto). Asse orizzontale («Scope»): a che livello si applicano, cioè al codice del programma, alla struttura dell'applicazione (componenti e connettori) o alla struttura dell'intero sistema.*

- **Design pattern (di programma)**: pochissima conoscenza del dominio; si applicano solo al livello del codice (classi e oggetti).
- **Stili**: poca conoscenza del dominio, ma la loro nuvola è la più larga: si applicano a tutti i livelli, dal codice fino all'intero sistema.
- **Pattern architetturali**: un po' più di conoscenza del dominio; riguardano la struttura dell'applicazione e del sistema.
- **Architetture software specifiche di dominio**: conoscenza profonda di un dominio (🧩 ad es. il software di bordo delle automobili); riguardano l'intero sistema.
- Salendo nella mappa le soluzioni diventano più specifiche: dicono di più sul problema concreto, ma si possono riusare in meno contesti.

### Proprietà, benefici e analisi di uno stile · [[05_Architectural_Styles_Complete.pdf#page=4|p. 4]]–[[05_Architectural_Styles_Complete.pdf#page=7|7]]

#### Le quattro proprietà di base · [[05_Architectural_Styles_Complete.pdf#page=4|p. 4]]

Ogni stile fissa quattro cose:

- **Un vocabolario di elementi di progetto**: l'elenco dei tipi di elementi con cui si può costruire il sistema.
  - Tipi di **componente** (le parti che elaborano), di **connettore** (ciò che collega i componenti) e di **elemento dati** (ciò che circola tra loro).
  - Esempi: pipe, filtri, oggetti, server.
- **Regole di configurazione**: vincoli sulla topologia, cioè su come gli elementi si possono collegare.
  - Esempio: ogni componente può essere collegato al massimo ad altri due (si ottiene così una catena).
- **Un'interpretazione semantica**: comporre gli elementi in un certo modo ha un significato preciso.
  - 🧩 *Esempio.* In pipe and filter una pipe da A a B significa «l'output di A diventa l'input di B»; in uno stile a livelli una freccia da A a B significa «A usa i servizi di B». La stessa freccia, in stili diversi, vuol dire cose diverse.
- **Analisi specifiche dello stile**: dato che i sistemi rispettano le regole dello stile, su di essi si possono fare analisi particolari.
  - 🧩 *Esempio.* In pipe and filter si può stimare quanti dati al secondo attraversano la catena o verificare che non ci siano blocchi.

#### Benefici degli stili · [[05_Architectural_Styles_Complete.pdf#page=5|p. 5]]

- **Riuso del progetto**: per problemi che si ripetono si riusano soluzioni architetturali già note.
- **Riuso del codice**: le parti che restano uguali in ogni sistema costruito con lo stile si implementano una volta e si riusano (🧩 ad es. il meccanismo delle pipe).
- **Comprensione strutturale**: basta un nome come «client–server» per far capire subito com'è strutturato il sistema.
- **Interoperabilità**: convenzioni condivise e modi standard di interagire facilitano l'integrazione tra sistemi.
- **Analisi specifiche dello stile**: uno spazio di progetto ristretto rende alcune analisi più facili.
- **Visualizzazioni**: rappresentazioni grafiche tipiche dello stile mostrano la struttura essenziale del sistema.

#### Come analizzare uno stile · [[05_Architectural_Styles_Complete.pdf#page=6|p. 6]]

Per descrivere uno stile (e confrontarlo con altri) si risponde a sette domande:

1. Qual è il **vocabolario** di componenti e connettori?
2. Quali **configurazioni strutturali** sono ammesse?
3. Qual è il **modello computazionale** sottostante, cioè come avviene l'elaborazione?
4. Quali sono gli **invarianti** fondamentali, cioè le proprietà che devono valere sempre?
5. Quali sono gli **esempi d'uso** più comuni?
6. Quali **benefici** e quali **limiti** introduce?
7. Quali **specializzazioni o varianti** esistono?

🧩 Le sezioni che seguono rispondono, stile per stile, proprio a queste domande: sono una buona traccia per esporre uno stile all'orale.

#### Catalogo degli stili · [[05_Architectural_Styles_Complete.pdf#page=7|p. 7]]

| Famiglia | Stili |
|---|---|
| Tradizionali, influenzati dai linguaggi di programmazione | main program e subroutine; object-oriented |
| Layered (a livelli) | virtual machine; client–server |
| Data flow (flusso di dati) | batch sequential; pipe and filter |
| Shared memory (memoria condivisa) | blackboard; rule-based |
| Interpreter | interpreter; mobile code |
| Implicit invocation (invocazione implicita) | event-based; publish–subscribe; peer-to-peer |
| Orientati ai servizi | service-oriented; microservices |

Gli stili orientati ai servizi si studiano nella Lezione 10.

### Main program e subroutine · [[05_Architectural_Styles_Complete.pdf#page=8|p. 8]]–[[05_Architectural_Styles_Complete.pdf#page=10|10]]

È lo stile dei programmi «classici» scritti in linguaggi imperativi come il C: un programma principale chiama delle funzioni (*subroutine*), che a loro volta possono chiamarne altre.

#### Lunar Lander con main program e subroutine · [[05_Architectural_Styles_Complete.pdf#page=8|p. 8]]

![[lez08-stili-p8-main-program-lunar-lander.png]]
*Il Main Program chiama tre subroutine; ogni freccia è una chiamata di procedura («Procedure Call»).*

- **«Get BurnRate from user»**: legge da tastiera quanto carburante bruciare. Non riceve parametri e restituisce la spinta (*throttle*).
- **«Environment Simulator»**: riceve altitudine, spinta, carburante, tempo e velocità; restituisce i nuovi valori di altitudine, carburante e velocità.
- **«Display values to user»**: riceve altitudine, carburante, tempo e velocità e li mostra; non restituisce nulla.
- 🧩 Il main program ripete le tre chiamate, in quest'ordine, finché la partita non finisce.

#### Caratteristiche · [[05_Architectural_Styles_Complete.pdf#page=9|p. 9]]

- **Decomposizione funzionale gerarchica**: il problema si scompone in funzioni, e ogni funzione in funzioni più piccole. Si ottiene un albero: il main program in cima, le subroutine sotto.
- **Un solo thread di controllo**: c'è un unico flusso di esecuzione.
  - In ogni istante lavora una sola subroutine.
  - Quando una subroutine ne chiama un'altra, si ferma e aspetta che quella finisca e le restituisca il risultato.
  - L'ordine di esecuzione è gestito direttamente dal linguaggio di programmazione, con le chiamate e i ritorni delle funzioni.
- **La struttura in sottosistemi resta implicita**: lo stile non ha elementi che rappresentino i sottosistemi (🧩 ad es. «gestione dell'input» o «simulazione»). Questi raggruppamenti non compaiono nell'architettura: esistono solo nelle intenzioni del progettista.
- **Le subroutine sono raggruppate in moduli o file**: è l'unica organizzazione visibile, oltre all'albero delle chiamate.
- **Ragionamento gerarchico**: una subroutine è corretta solo se sono corrette anche le subroutine che chiama.
  - 🧩 *Esempio.* Se «Environment Simulator» calcola male la velocità, il main program dà risultati sbagliati anche se il suo codice è giusto.

#### Scheda dello stile · [[05_Architectural_Styles_Complete.pdf#page=10|p. 10]]

| Aspetto | Main program e subroutine |
|---|---|
| Sintesi | Il sistema è scomposto in passi di elaborazione funzionale |
| Componenti | Il main program e le subroutine |
| Connettori | Chiamate di funzione o di procedura |
| Elementi dati | I valori passati alle subroutine (parametri) e quelli che restituiscono |
| Topologia | Organizzazione gerarchica e statica (fissata quando si scrive il codice); la struttura completa è un grafo orientato |
| Vincoli | Nessuno |
| Benefici di qualità | **Modularità**: si può sostituire una subroutine con un'altra, purché l'interfaccia mantenga lo stesso significato (stessi parametri, stesso risultato atteso) |
| Usi tipici | Piccoli programmi ed esempi didattici |
| Cautele | Scala male per applicazioni grandi; dà poca attenzione alle strutture dati; l'impegno necessario per gestire nuovi requisiti è difficile da prevedere |
| Linguaggi | Linguaggi imperativi tradizionali: BASIC, Pascal, C |

- La struttura è un **grafo orientato** e non un semplice albero perché la stessa subroutine può essere chiamata da più punti: le frecce vanno da chi chiama a chi è chiamato.

### Stile object-oriented · [[05_Architectural_Styles_Complete.pdf#page=11|p. 11]]–[[05_Architectural_Styles_Complete.pdf#page=15|15]]

#### Elementi · [[05_Architectural_Styles_Complete.pdf#page=11|p. 11]]

- **Componenti: oggetti.** Ogni oggetto racchiude (*incapsula*) dei dati e le operazioni che lavorano su quei dati.
- **Connettori: messaggi e invocazioni di metodo.** Un oggetto ne usa un altro chiamandone i metodi.
  - Nelle applicazioni distribuite, con oggetti su macchine diverse, si può usare un middleware come **Java RMI** (*Remote Method Invocation*), che permette di chiamare i metodi di un oggetto remoto come se fosse locale.
- **Topologia**: variabile; spesso fa largo uso di **gerarchie di ereditarietà** (classi che specializzano altre classi).
- **Invariante dello stile**: ogni oggetto è responsabile dell'integrità della propria rappresentazione interna, cioè dei suoi dati. Gli altri oggetti non possono accedere direttamente a quei dati: devono passare dai suoi metodi.

#### Benefici e limiti · [[05_Architectural_Styles_Complete.pdf#page=12|p. 12]]

**Benefici**

- L'**incapsulamento** protegge l'integrità dei dati: solo i metodi dell'oggetto controllano l'accesso al suo stato interno, e possono verificare che ogni modifica sia valida.
  - 🧩 *Esempio.* Un oggetto Spacecraft può rifiutare, nel metodo che imposta il carburante, un valore negativo.
- È adatto a **strutture dati complesse** e a **modellare entità del mondo reale** come oggetti (una navicella, un conto, un cliente).

**Limiti**

- Per usare un servizio, un oggetto deve **conoscere l'identità** (il riferimento) dell'oggetto che lo fornisce: gli oggetti restano legati tra loro.
- Per capire un'applicazione può servire analizzare **relazioni complesse** tra oggetti, sia statiche (classi, ereditarietà) sia dinamiche (chi chiama chi durante l'esecuzione).
- Molti oggetti che interagiscono producono un **overhead**, cioè un costo aggiuntivo in prestazioni.
- Con molti oggetti servono **criteri di strutturazione aggiuntivi** per gestire la complessità (🧩 ad es. raggrupparli in livelli o in componenti più grandi).

#### Lunar Lander a oggetti · [[05_Architectural_Styles_Complete.pdf#page=13|p. 13]]–[[05_Architectural_Styles_Complete.pdf#page=14|14]]

- La **GUI** legge il burn rate inserito dall'utente e recupera i parametri della navicella con operazioni *get*.
- Mostra i parametri all'utente e li passa alla **simulazione dell'ambiente**.
- La simulazione calcola il nuovo stato della navicella, che viene memorizzato con operazioni *set*.

![[lez08-stili-p13-oo-lunar-lander.png]]
*Il modulo «GUI – Get/Display Info» fa tre chiamate: «GET a, f, t, v» e «SET a, f, t, v» verso l'oggetto SpaceCraft, che custodisce lo stato della navicella; «CALCULATE» verso Environment Simulation, che riceve il burn rate (br) e la navicella e restituisce la navicella aggiornata.*

![[lez08-stili-p14-oo-lunar-lander-uml.png]]
*Lo stesso progetto come diagramma delle classi UML. La classe GUI (operazioni getBurnRate() e displayStatus(...)) crea una o più navicelle Spacecraft (attributi a, f, t, v, ciascuno con le sue operazioni get e set) e usa un'unica Environment Simulation, la cui operazione calculateStatus(br, s) riceve il burn rate e una navicella e restituisce la navicella aggiornata.*

#### Confronto con la versione call–return · [[05_Architectural_Styles_Complete.pdf#page=15|p. 15]]

- Nella versione **object-oriented** un solo oggetto, la GUI, gestisce tutto l'input e tutto l'output.
- Nella versione **call–return** (main program e subroutine) input e output sono distribuiti su più moduli: una subroutine legge il burn rate, un'altra mostra i valori.
- 🧩 Cambia anche dove stanno i dati: nella versione a oggetti lo stato della navicella è chiuso dentro Spacecraft e si tocca solo con get e set; nella versione call–return i valori viaggiano come parametri da una subroutine all'altra.

![[lez08-stili-p15-oo-vs-call-return.png]]
*Le due versioni affiancate: a sinistra quella a oggetti, a destra quella call–return.*

### Stile layered (a livelli) · [[05_Architectural_Styles_Complete.pdf#page=16|p. 16]]–[[05_Architectural_Styles_Complete.pdf#page=29|29]]

#### Elementi · [[05_Architectural_Styles_Complete.pdf#page=16|p. 16]]–[[05_Architectural_Styles_Complete.pdf#page=18|18]]

- Il sistema è organizzato **gerarchicamente in livelli** (*layer*), uno sopra l'altro, come una struttura client–server a più livelli.
- Ogni layer offre un'**interfaccia** (API) ai layer che stanno sopra.
- Ogni layer fa da **server** per i layer superiori (offre loro servizi) e da **client** per quelli inferiori (ne usa i servizi).
- **Connettori**: chiamate di procedura o protocolli di interazione.
- Esempio tipico: i **sistemi operativi** (🧩 le applicazioni usano le chiamate di sistema del kernel, il kernel usa i driver, i driver usano l'hardware).
- **Variante virtual machine**: i layer sono *opachi*, cioè ogni layer vede solo quello immediatamente sotto e non ciò che c'è più in basso; le interazioni avvengono solo tra layer adiacenti.

![[lez08-stili-p18-layered-virtual-machines.png]]
*Variante virtual machine con tre layer. Il Program A (Layer 1) usa solo il Layer 2; i Program B e C (Layer 2) usano solo il Layer 3, dove si trova il Program D. Nessuna freccia salta un livello.*

#### Benefici · [[05_Architectural_Styles_Complete.pdf#page=19|p. 19]]

- I layer offrono **livelli di astrazione crescenti**: in basso i dettagli (hardware, rete), in alto i concetti dell'applicazione.
- Le **dipendenze sono controllate**: ogni layer dipende solo da quelli sotto. Questo facilita l'evoluzione e limita la propagazione delle modifiche: un cambiamento in un layer può ripercuotersi solo sui layer superiori.
- Un layer si può **riusare** oppure **sostituire** con un'implementazione diversa, purché mantenga la stessa interfaccia.
  - 🧩 *Esempio.* Si può sostituire il layer che accede a un database MySQL con uno che accede a PostgreSQL senza toccare i layer sopra.
- Interfacce dei layer **standardizzate** permettono di costruire librerie e framework.

#### Limiti · [[05_Architectural_Styles_Complete.pdf#page=20|p. 20]]

- Attraversare molti layer aggiunge **overhead**: ogni richiesta passa da un layer all'altro prima di arrivare a destinazione.
- Per ragioni di efficienza si può decidere di **saltare un layer** (*bypass*), chiamando direttamente un layer più in basso.
- Il bypass però crea **dipendenze aggiuntive**, di cui tenere conto quando si valuta la modificabilità: chi salta un layer dipende anche da quello più in basso.

#### Layer chiusi e layer aperti · [[05_Architectural_Styles_Complete.pdf#page=21|p. 21]]

- **Closed Layers Architecture (CLA)**, architettura a layer chiusi: il layer *i* può usare **solo** il layer immediatamente sotto, *i−1*.
- **Open Layers Architecture (OLA)**, architettura a layer aperti: il layer *i* può usare **qualsiasi** layer sottostante.

#### Layer chiusi · [[05_Architectural_Styles_Complete.pdf#page=22|p. 22]]–[[05_Architectural_Styles_Complete.pdf#page=23|23]]

- Il layer *i* invoca solo servizi e operazioni del layer *i−1*.
- Obiettivi principali: **manutenibilità** e **portabilità**.
  - 🧩 Se cambia un layer, va adattato al massimo quello immediatamente sopra; per portare il sistema su un'altra piattaforma basta riscrivere i layer più bassi.
- Interpretazione come **virtualizzazione**: ogni layer *i* definisce una **macchina virtuale** VM<sub>i</sub>. Per il layer che sta sopra, il layer *i* è «la macchina» su cui gira, di cui vede solo le operazioni.

![[lez08-stili-p22-closed-layers.png]]
*Layer chiusi: quattro layer (VM1–VM4), ciascuno con le sue classi; ogni dipendenza va da un layer a quello immediatamente sotto.*

- **Esempio: lo stack ISO/OSI.** Il modello di riferimento per le reti definisce 7 layer, con livello di astrazione crescente verso l'alto.
  - Ad esempio l'Internet Protocol (IP) realizza una macchina virtuale a livello di rete: sa identificare gli host e trasmettere singoli pacchetti da un host all'altro.

![[lez08-stili-p23-osi-closed-layers.png]]
*Pila ISO/OSI dall'alto in basso: Application, Presentation, Session, Transport, Network, DataLink, Physical. Ogni layer comunica solo con quello immediatamente sotto.*

#### Layer aperti · [[05_Architectural_Styles_Complete.pdf#page=24|p. 24]]–[[05_Architectural_Styles_Complete.pdf#page=25|25]]

- Il layer *i* può invocare servizi e operazioni di **qualsiasi** layer sottostante.
- Obiettivi principali: **tempi di esecuzione ridotti** ed **efficienza**, perché si evitano i passaggi intermedi.
- 🧩 Il prezzo è la modificabilità: un layer alto può dipendere da molti layer sotto, quindi una modifica in basso si ripercuote su più layer.

![[lez08-stili-p24-open-layers.png]]
*Layer aperti: gli stessi quattro layer, ma alcune dipendenze saltano i layer intermedi (una classe del primo layer usa direttamente una classe del quarto).*

- **Esempio: OSF/Motif**, una libreria per costruire interfacce grafiche:
  - *Xlib*: funzioni di disegno di basso livello;
  - *Xt*: gestione dei *widget* di base dell'interfaccia (i widget sono gli elementi grafici: pulsanti, menu, finestre);
  - *Motif*: un gran numero di widget sofisticati;
  - *Application*: può usare ciascun layer in modo indipendente.

![[lez08-stili-p25-motif-open-layers.png]]
*Quattro layer (Application, Motif, Xt, Xlib). Oltre alle dipendenze tra layer adiacenti, le frecce tratteggiate mostrano che Application usa direttamente anche Xt e Xlib, e Motif usa direttamente Xlib.*

#### Interfacce dei layer con il pattern Façade · [[05_Architectural_Styles_Complete.pdf#page=26|p. 26]]–[[05_Architectural_Styles_Complete.pdf#page=27|27]]

- **Problema**: senza una *façade*, chi usa un layer deve coordinare da solo più oggetti di quel layer.
  - Esempio della slide: per validare e salvare i dati di un cliente, AccountManager deve chiamare uno per uno gli oggetti Account, Address e CreditCard.

![[lez08-stili-p26-facade-senza.png]]
*Diagramma di sequenza senza façade: AccountManager chiama direttamente Account, Address e CreditCard, ciascuno con le sue operazioni isValid() e save().*

- **Soluzione**: il pattern **Façade** («facciata») introduce un unico oggetto, CustomerFacade, che offre un'operazione di alto livello, saveCustomerData(), e coordina lui gli oggetti interni.
- 🧩 Così il layer espone un'interfaccia semplice, e gli oggetti interni possono cambiare senza toccare chi sta sopra.

![[lez08-stili-p27-facade-con.png]]
*Con la façade: AccountManager chiama solo saveCustomerData() su CustomerFacade, che coordina Account, Address e CreditCard. A sinistra il diagramma delle classi, a destra la sequenza delle chiamate.*

#### Esercizio: Lunar Lander a layer · [[05_Architectural_Styles_Complete.pdf#page=28|p. 28]]–[[05_Architectural_Styles_Complete.pdf#page=29|29]]

- Domanda: come si organizzerebbe Lunar Lander in layer?

![[lez08-stili-p29-layered-lunar-lander.png]]
*Soluzione con cinque layer, dall'alto in basso; ogni layer chiama quello sotto con una chiamata di procedura.*

1. **Keyboard Input Handler**: legge i tasti e passa l'input da tastiera al layer sotto.
2. **Game Logic and Environment Simulator**: applica le regole del gioco e calcola la variazione di altitudine.
3. **Generic 2D Game Engine**: un motore grafico 2D generico, che riceve le posizioni (x, y) degli oggetti da disegnare.
4. **Operating System**: riceve dal motore i dati da mostrare e li passa all'hardware come dati binari.
5. **Hardware Display / Graphics Card**: lo schermo e la scheda grafica.

- 🧩 Ogni layer è più astratto di quello sotto: in alto si ragiona in termini di «gioco», in basso di pixel e dati binari. Il motore 2D, essendo generico, si può riusare per altri giochi.

### Stile client–server · [[05_Architectural_Styles_Complete.pdf#page=30|p. 30]]–[[05_Architectural_Styles_Complete.pdf#page=34|34]]

#### Idea · [[05_Architectural_Styles_Complete.pdf#page=30|p. 30]]

- Lo stile distingue **due ruoli** in un'interazione: chi chiede un servizio (**client**) e chi lo fornisce (**server**).
- È nato nei **sistemi distribuiti**, per organizzare la comunicazione tra parti che girano su macchine separate.
- Uno o più server forniscono servizi a **molti client**.
- Il client **invoca** un servizio del server e **riceve un risultato**.
- 🧩 *Esempio.* Il browser (client) chiede una pagina al server web, che gliela restituisce.

#### Elementi e usi · [[05_Architectural_Styles_Complete.pdf#page=31|p. 31]]

- **Componenti: client e server.**
  - Il server **non deve sapere in anticipo** quanti client avrà né chi sono.
  - Il client deve sapere **come raggiungere** il server (🧩 ad es. il suo indirizzo).
  - I client possono essere **thin** (leggeri: si limitano all'interfaccia e lasciano il lavoro al server) o **thick** (pesanti: fanno anche parte dell'elaborazione).
- **Connettori**: protocolli di interazione di rete, **RPC** (*Remote Procedure Call*, chiamata di una procedura che gira su un'altra macchina) e **Java RMI**.
- **Uso tipico**: dati o elaborazione centralizzati sul server, con i client che forniscono l'interfaccia utente.
- **Limiti**: quando i client aumentano, la **banda di rete** e le **prestazioni del server** possono diventare colli di bottiglia, perché tutte le richieste passano dallo stesso server.

#### Responsabilità logiche · [[05_Architectural_Styles_Complete.pdf#page=32|p. 32]]

Un sistema client–server si divide logicamente in tre responsabilità:

- **Presentazione**: interfaccia utente, gestione degli eventi grafici (click, tasti premuti) e controlli sull'input.
- **Logica applicativa**: le funzioni del sistema.
- **Gestione dei dati**: i dati persistenti, cioè salvati in modo durevole (🧩 ad es. in un database).

#### Alternative di deployment · [[05_Architectural_Styles_Complete.pdf#page=33|p. 33]]

Le tre responsabilità si possono distribuire su macchine diverse (*tier*) in tre modi:

- **Due tier**: presentazione e logica applicativa possono stare insieme nel client; i dati persistenti stanno su un server.
- **Tre tier**: presentazione, logica applicativa e gestione dei dati stanno su tre tier separati (🧩 ad es. browser, application server, server del database).
- **N tier**: logica applicativa e gestione dei dati sono distribuite lungo una catena di server.

#### Lunar Lander client–server · [[05_Architectural_Styles_Complete.pdf#page=34|p. 34]]

- Versione **multigiocatore**: ogni giocatore ha il suo client, e la partita è gestita da un unico server.

![[lez08-stili-p34-client-server-lunar-lander.png]]
*I client (Client 1, 2, …, n), ognuno con «Get/Display Info» (input e visualizzazione) e «Graphics Processing», chiamano il SERVER con una chiamata di procedura. Il server contiene Game State, Game Logic ed Environment Simulation. Il client invia il burn rate; il server restituisce altitudine, carburante, tempo e velocità.*

- 🧩 Tutta la logica del gioco sta sul server; i client si occupano solo di input e grafica.

### Stili data-flow (flusso di dati) · [[05_Architectural_Styles_Complete.pdf#page=35|p. 35]]–[[05_Architectural_Styles_Complete.pdf#page=51|51]]

#### Introduzione · [[05_Architectural_Styles_Complete.pdf#page=35|p. 35]]–[[05_Architectural_Styles_Complete.pdf#page=36|36]]

- 🧩 Negli stili data-flow il sistema è visto come una sequenza di trasformazioni: i dati entrano, passano da un elemento di elaborazione all'altro e ne escono trasformati.
- Ci sono due varianti: **batch sequential** e **pipe and filter**.

#### Batch sequential · [[05_Architectural_Styles_Complete.pdf#page=37|p. 37]]–[[05_Architectural_Styles_Complete.pdf#page=39|39]]

- I dati passano tra **elementi di elaborazione indipendenti**.
- Gli elementi sono **programmi separati**, eseguiti **uno dopo l'altro** in un ordine stabilito, che si scambiano i dati **a lotti** (*batch*).
  - 🧩 Ogni programma elabora tutto il suo lotto prima che parta il successivo.
- Storicamente i connettori potevano essere **persone** che spostavano i nastri magnetici da un programma all'altro.
- Gli **elementi dati** sono i lotti che passano da un componente all'altro fino alla fine dell'elaborazione.
- Uso tipico: l'elaborazione delle **transazioni nei sistemi finanziari**. È uno dei primissimi stili architetturali.

![[lez08-stili-p38-batch-sequential-finanza.png]]
*Un'applicazione finanziaria. I rettangoli sono i programmi, i cerchi i lotti di dati.*

- Le transazioni del giorno («Daily transactions») vengono ordinate per numero di conto («Sort by account number»).
- Le transazioni ordinate e il nastro con i conti («Master account tape») entrano in «Process transactions», che produce il nastro dei conti aggiornato; quel nastro servirà il giorno dopo («For tomorrow's use»).
- Infine «Print summary of accounts» stampa il riepilogo dei conti.

![[lez08-stili-p39-batch-sequential-lunar-lander.png]]
*Lunar Lander in batch sequential: i valori h, v, t, fuel passano per «Get BurnRate from user», poi per «Compute new h, v, t, fuel», poi per «Display h, v, t, fuel to user», e ricominciano il giro.*

- La slide commenta che questa non è certo «la ricetta per una missione lunare di successo».
- Il motivo: l'elaborazione a lotti non offre il **controllo interattivo in tempo reale** che il gioco richiede (🧩 ogni passo deve finire del tutto prima che parta il successivo).

#### Pipe and filter: obiettivo · [[05_Architectural_Styles_Complete.pdf#page=40|p. 40]]–[[05_Architectural_Styles_Complete.pdf#page=41|41]]

- Scomporre un compito complesso in **passi di elaborazione indipendenti**, i **filtri** (*filters*), collegati da canali, le **pipe** («tubi»).
- Ogni filtro esegue **una specifica trasformazione** dei dati.

![[lez08-stili-p41-pipeline-componenti-riusati.png]]
*Due pipeline. I dati della sorgente 1 passano per i task A, B, C e D e arrivano trasformati alla «Business logic»; quelli della sorgente 2 passano per i task B, E e F. Il task B è lo stesso componente in entrambe: un filtro si può riusare in pipeline diverse.*

#### Elementi e invarianti · [[05_Architectural_Styles_Complete.pdf#page=42|p. 42]]

- **Componenti: filtri**, programmi che trasformano flussi di dati in ingresso in flussi di dati in uscita.
- **Connettori: pipe**, canali per i flussi di dati, realizzati con code, stream, messaggi, file temporanei o meccanismi simili.
- **Invarianti** (regole che valgono sempre):
  - i filtri sono **indipendenti** e **non condividono stato** (nessuna variabile in comune);
  - un filtro **non sa** quali filtri stanno prima di lui (*a monte*) o dopo di lui (*a valle*): conosce solo la sua pipe di ingresso e quella di uscita;
  - i filtri possono girare **in concorrenza**: un filtro a valle non aspetta che quello a monte abbia finito tutto il lavoro, ma elabora i dati man mano che arrivano.
- 🧩 Quest'ultima è la differenza principale con il batch sequential, dove ogni passo aspetta la fine del precedente.

#### Esempi · [[05_Architectural_Styles_Complete.pdf#page=43|p. 43]]

- Shell UNIX, elaborazione di segnali, sistemi distribuiti, programmazione parallela.
- Esempio di shell: `ls invoices | grep -e August | sort`
  - `ls invoices` elenca i file della cartella *invoices* (fatture);
  - `grep -e August` tiene solo le righe che contengono «August»;
  - `sort` le ordina;
  - il simbolo `|` è la pipe: l'output di un comando diventa l'input del comando successivo.
- Un **compilatore Java** può organizzare analisi lessicale, parsing, analisi semantica e ottimizzazione come trasformazioni successive: ogni fase riceve l'output della precedente.

#### Implementare le pipeline · [[05_Architectural_Styles_Complete.pdf#page=44|p. 44]]–[[05_Architectural_Styles_Complete.pdf#page=45|45]]

- In un programma che gira in un **solo processo**, le pipe sono spesso **code in memoria**.
- In un'implementazione **distribuita** (filtri su macchine diverse), un'**infrastruttura di messaggistica** trasporta i flussi tra i filtri remoti, ad esempio con **code di messaggi**.
- Un passo **lento** può essere affidato a **più istanze parallele** dello stesso filtro. Questo migliora le prestazioni e il **throughput** (la quantità di dati elaborati nell'unità di tempo).

![[lez08-stili-p45-filtri-paralleli.png]]
*Pipeline con filtri paralleli: i dati si distribuiscono su tre istanze del task A, passano per i task B e C, poi si distribuiscono su tre istanze del task D, fino alla «Business logic». Gli stadi replicati sono quelli più lenti.*

- I filtri paralleli possono girare su macchine con prestazioni diverse.
- Un filtro passa il suo output, una volta completato, alla pipe verso lo stadio successivo.
- L'elaborazione parallela richiede attenzione:
  - evitare **scritture duplicate** (🧩 due istanze che elaborano e scrivono lo stesso dato);
  - se serve, **preservare l'ordine** dell'output.

#### Comportamento dei filtri · [[05_Architectural_Styles_Complete.pdf#page=46|p. 46]]

- Un filtro può:
  - **arricchire** i dati, calcolando o aggiungendo informazione (🧩 ad es. aggiungere a ogni riga di log il nome del server);
  - **raffinarli**, aggregando o estraendo informazione (🧩 ad es. contare gli errori di ogni ora);
  - **trasformarli** in un'altra rappresentazione (🧩 ad es. da testo a JSON).
- Un filtro **attivo** avvia da sé l'elaborazione, come programma o thread separato: di solito ripete in ciclo «leggi l'input, scrivi l'output».
- Un filtro **passivo** lavora solo quando un altro componente lo invoca:
  - con una **chiamata di funzione** (*pull*): chi sta a valle chiede i dati al filtro;
  - con una **chiamata di procedura** (*push*): chi sta a monte consegna i dati al filtro.

#### Esempio: elaborazione di log · [[05_Architectural_Styles_Complete.pdf#page=47|p. 47]]

- **Filtro A**: legge i file di log.
- **Filtro B**: normalizza i dati, cioè li porta in un formato uniforme.
- **Filtro C**: tiene solo gli errori critici.
- **Filtro D**: aggrega i risultati.
- **Filtro E**: salva i risultati in un database.
- Ogni passo è indipendente: il filtro di normalizzazione si può riusare per un'altra sorgente di log senza ricostruire tutta l'applicazione.

#### Attributi di qualità · [[05_Architectural_Styles_Complete.pdf#page=48|p. 48]]

- **Prestazioni**: i filtri possono girare in parallelo ed elaborare i dati **in modo incrementale**, cioè man mano che arrivano, senza aspettare tutto l'input.
- **Scalabilità**: i filtri costosi si possono replicare e scalare indipendentemente dagli altri.
- **Riuso**: filtri generici possono servire più catene di elaborazione.
- **Modularità**: ogni filtro ha una responsabilità distinta.
- **Modificabilità e testabilità**: ogni filtro è disaccoppiato dagli altri, quindi si può modificare e testare da solo.

#### Benefici · [[05_Architectural_Styles_Complete.pdf#page=49|p. 49]]

- Il comportamento complessivo del sistema si ottiene **componendo** i comportamenti dei filtri (🧩 come una composizione di funzioni: `sort(grep(ls(...)))`).
- I filtri possono girare in concorrenza e produrre output incrementale.
- L'elaborazione incrementale può ridurre la **latenza** (il tempo prima che esca il primo risultato) e permette il parallelismo.
- I filtri si possono aggiungere, sostituire e riusare.
- Si possono analizzare proprietà architetturali come **throughput**, **latenza** e **deadlock** (🧩 blocco reciproco: due filtri che si aspettano a vicenda).

#### Limiti · [[05_Architectural_Styles_Complete.pdf#page=50|p. 50]]

- Le implementazioni orientate al **batch** offrono poca **interattività**.
- Lo stile è scomodo quando i filtri devono avere **conversazioni interattive complesse**, cioè scambi avanti e indietro (🧩 i dati scorrono in una sola direzione).
- Strutture dati complesse possono richiedere **codifica e decodifica costose** (ogni filtro deve convertire i dati per passarli sulla pipe) oppure l'accordo su **formati comuni**.

#### Lunar Lander in pipe and filter · [[05_Architectural_Styles_Complete.pdf#page=51|p. 51]]

- Ogni filtro ripete continuamente la propria azione:
  - il primo chiede all'utente il burn rate e lo scrive nello stream;
  - il secondo aggiorna l'ambiente (altitudine, velocità, …) ogni volta che arriva un nuovo burn rate;
  - il terzo aggiorna il display ogni volta che al suo ingresso arrivano nuovi valori di stato.

![[lez08-stili-p51-pipe-filter-lunar-lander.png]]
*«Get BurnRate from user» → stream (porta br) → «Compute new values» → stream (porta a, f, t, v) → «Display new values to user».*

- 🧩 A differenza della versione batch, qui i tre filtri lavorano contemporaneamente: il gioco resta interattivo.

### Stili shared-data (dati condivisi) · [[05_Architectural_Styles_Complete.pdf#page=52|p. 52]]–[[05_Architectural_Styles_Complete.pdf#page=71|71]]

#### Memoria condivisa e stato condiviso · [[05_Architectural_Styles_Complete.pdf#page=52|p. 52]]–[[05_Architectural_Styles_Complete.pdf#page=54|54]]

- Più **agenti** (componenti indipendenti) accedono allo **stesso archivio centralizzato di dati** e **comunicano attraverso di esso**: un agente scrive un dato, un altro lo legge.
- **Obiettivo**: disaccoppiare gli agenti, che si possono aggiungere o togliere a runtime senza conoscersi tra loro.
- Gli agenti sono indipendenti tra loro, e l'archivio è indipendente dagli agenti.
- Queste architetture supportano l'**integrazione dei dati**: tutti lavorano sugli stessi dati.
- Per certi aspetti ricordano le **variabili globali** di un programma, ma sono un'organizzazione architetturale a sé (🧩 l'archivio ha interfacce, regole di accesso, persistenza).

![[lez08-stili-p54-shared-data.png]]
*Il blocco centrale «Shared Data» è circondato da agenti (gli ovali), che lo leggono e lo scrivono (frecce «Memory Access») ed eseguono le proprie elaborazioni («Computation»): la topologia è a stella.*

#### Elementi · [[05_Architectural_Styles_Complete.pdf#page=55|p. 55]]

- **Componenti**: un **archivio globale di dati** (chiamato *blackboard*, «lavagna») e **agenti indipendenti** che lavorano su di esso.
- **Connettori**: chiamate di procedura, accesso diretto alla memoria oppure operazioni su database.
  - Con un database l'interazione segue di solito lo schema **CRUD**: *Create* (creare), *Read* (leggere), *Update* (aggiornare), *Delete* (cancellare).
- **Topologia**: a **stella**, con l'archivio condiviso al centro.

#### Varianti · [[05_Architectural_Styles_Complete.pdf#page=56|p. 56]]

- **Blackboard**: specialisti indipendenti contribuiscono a una rappresentazione condivisa del problema. Ognuno affronta una parte del problema e aggiorna i dati condivisi.
- **Rule-based**: una **base di conoscenza** memorizza fatti e regole, come nei **sistemi esperti** e in altre applicazioni di intelligenza artificiale.
- **Repository**: componenti diversi condividono e aggiornano dati comuni.
- 🧩 Le tre varianti differiscono per *che cosa* c'è nell'archivio (dati dell'applicazione, stato di un problema, fatti e regole) e per *chi decide* cosa fare dopo.

#### 1. Repository · [[05_Architectural_Styles_Complete.pdf#page=57|p. 57]]–[[05_Architectural_Styles_Complete.pdf#page=59|59]]

![[lez08-stili-p57-repository-componenti.png]]
*Diagramma dei componenti: il componente Repository contiene un Request Validator (stereotipo «executable»), che usa un Database; il Repository espone un'interfaccia (un'operazione) usata dal componente Agent.*

- Un **repository centrale** memorizza dati condivisi da più componenti.
- I componenti leggono e aggiornano il repository attraverso **interfacce di accesso** definite.
- Il repository gestisce:
  - la **persistenza** (i dati sopravvivono allo spegnimento del sistema);
  - i **vincoli di integrità** (regole che i dati devono sempre rispettare);
  - l'**accesso concorrente** (più componenti che lavorano contemporaneamente).
- I componenti condividono un **modello dei dati comune**, che diventa un'importante dipendenza architetturale: se cambia, ne risentono tutti.
- 🧩 *Esempio.* Un gestionale aziendale in cui contabilità, magazzino e vendite lavorano sullo stesso database.

**Benefici**

- I dati condivisi supportano l'integrazione tra le diverse funzioni dell'applicazione.
- Vincoli di integrità, controllo degli accessi e backup si gestiscono **in un solo punto**.
- I nuovi componenti possono usare subito i dati esistenti.

**Limiti**

- **Modificabilità**: un cambio dello schema dei dati può richiedere modifiche in più componenti.
- **Prestazioni**: accessi concorrenti e contesa (più componenti che vogliono gli stessi dati nello stesso momento) possono creare colli di bottiglia.
- **Disponibilità**: un guasto del repository può bloccare molte funzioni dell'applicazione.

#### 2. Blackboard: interazione · [[05_Architectural_Styles_Complete.pdf#page=60|p. 60]]

- In un **repository** i componenti usano i dati condivisi per svolgere le funzioni applicative.
- In una **blackboard** i componenti specialisti aggiungono **risultati parziali**, ed è lo **stato condiviso**, che evolve, a guidare quali componenti devono lavorare dopo.
- 🧩 *Immagine utile.* Alcuni esperti davanti a una lavagna: ognuno guarda cosa c'è scritto e, se sa aggiungere un pezzo di soluzione, lo scrive. Nessuno dirige il lavoro: è il contenuto della lavagna a far capire chi deve intervenire.
- **Blackboard passiva**: i componenti interrogano periodicamente (*poll*) lo stato condiviso e decidono da soli quando agire.
- **Blackboard attiva**: un gestore avvisa i programmi quando cambiano i dati che li riguardano.

#### Blackboard: esempi applicativi · [[05_Architectural_Styles_Complete.pdf#page=61|p. 61]]

- **Intelligenza artificiale**: problem solving, riconoscimento vocale, controllo di robot.
- **Riconoscimento ottico dei caratteri** (OCR): strumenti storici come Adobe Acrobat Capture usavano la blackboard per interpretare oggetti, testo e font in un documento scansionato.
- **Sistemi CAD** grafici.
- **Sistemi di Complex Event Processing** (CEP) (🧩 sistemi che riconoscono situazioni complesse combinando molti eventi semplici).

#### Blackboard: benefici · [[05_Architectural_Styles_Complete.pdf#page=62|p. 62]]

- La strategia per risolvere un problema complesso **non va pianificata tutta in anticipo**.
- Sono i cambiamenti nei dati del problema a stabilire quali contributi servono dopo.
- Così specialisti indipendenti possono cooperare su un problema complesso attraverso una rappresentazione condivisa.

#### Blackboard: limiti · [[05_Architectural_Styles_Complete.pdf#page=63|p. 63]]

- Serve cautela quando le interazioni tra programmi indipendenti richiedono una **logica di coordinamento complessa**.
- Se la rappresentazione dei dati condivisi cambia spesso, molti agenti vanno adattati.
- Se esiste già una strategia di coordinamento chiara, la blackboard aggiunge **complessità inutile**.
- Gli agenti concorrenti richiedono meccanismi per **controllare l'accesso** ai dati condivisi.
- I dati condivisi possono diventare il **collo di bottiglia** dell'architettura.
- È difficile **spiegare come si è arrivati** ai risultati.

#### Lunar Lander con blackboard · [[05_Architectural_Styles_Complete.pdf#page=64|p. 64]]

![[lez08-stili-p64-blackboard-lunar-lander.png]]
*Tre componenti accedono, attraverso un connettore «Data Access», alla blackboard «Data Storage», che contiene altitudine, burn rate, carburante, tempo e velocità. «Enter burn rate from user» scrive il burn rate; «Compute new values and Update» legge tutti i valori e scrive i nuovi a, f, t, v; «Display values» legge a, f, t, v per mostrarli.*

- I componenti accedono allo stato condiviso tramite riferimenti in memoria, chiamate di procedura o query a un database.
- 🧩 Nessun componente chiama gli altri: si coordinano solo leggendo e scrivendo la lavagna.

#### 3. Rule-based · [[05_Architectural_Styles_Complete.pdf#page=65|p. 65]]–[[05_Architectural_Styles_Complete.pdf#page=66|66]]

- La memoria condivisa è una **base di conoscenza** che contiene:
  - **fatti** (🧩 ad es. «il paziente ha la febbre»);
  - **regole di produzione** nella forma IF … THEN: se valgono certe condizioni, allora si deduce un nuovo fatto o si compie un'azione.
- L'**interfaccia utente** raccoglie l'input e mostra l'output; con l'input si aggiungono nuovi fatti o nuove regole alla base di conoscenza.
- Data una **query** o un **obiettivo**, un **motore inferenziale** applica le regole disponibili per stabilire se l'obiettivo è soddisfatto.
- Il motore può ragionare in due modi:
  - **forward chaining** (in avanti): parte dai dati disponibili, applica le regole e ricava nuovi fatti, ad esempio «lo studente è idoneo»;
  - **backward chaining** (all'indietro): parte da un obiettivo («lo studente è idoneo?») e controlla se valgono le condizioni necessarie per dimostrarlo.
- È lo stile tipico dei **sistemi esperti**, anche di quelli scritti in **Prolog**.

#### Rule-based: struttura e usi · [[05_Architectural_Styles_Complete.pdf#page=67|p. 67]]

- **Componenti**: interfaccia utente, motore inferenziale, base di conoscenza.
- **Connettori**: chiamate di procedura e accesso alla memoria condivisa, che legano strettamente i componenti.
- **Elementi dati**: fatti e query.
- **Topologia**: tre parti principali.
- **Beneficio**: aggiungendo o togliendo regole si cambia il comportamento dell'applicazione (🧩 senza riscrivere il codice del motore).
- **Uso**: prototipazione rapida di applicazioni guidate da regole.

#### Lunar Lander rule-based · [[05_Architectural_Styles_Complete.pdf#page=68|p. 68]]

![[lez08-stili-p68-rule-based-lunar-lander.png]]
*L'interfaccia utente invia, con una chiamata di procedura, il fatto burnrate(25) e l'obiettivo landed(spacecraft) («la navicella è atterrata?») all'Inference Engine. Il motore, tramite «Data Access», consulta la Knowledge Base, che contiene i fatti (a, br, f, t, v) e la regola di atterraggio.*

- Il motore verifica una regola di atterraggio, ad esempio: altitudine ≤ 0 AND velocità < 3 ft/s (piedi al secondo).
- In figura la regola è scritta in stile Prolog, `landed(spacecraft) :- (a, 0), (v, 3)`, e si legge «la navicella è atterrata se altitudine e velocità rispettano quelle soglie».

#### Rule-based: interazioni e conflitti tra regole · [[05_Architectural_Styles_Complete.pdf#page=69|p. 69]]–[[05_Architectural_Styles_Complete.pdf#page=70|70]]

- Con molte regole è difficile capire come interagiscono quelle attivate dagli **stessi fatti**.
- Può diventare difficile **ricostruire il ragionamento** che ha portato a un risultato.
- In molte applicazioni conta la **spiegazione** del risultato, non solo il risultato.
- Regole attivate dagli stessi fatti possono **sovrascriversi** a vicenda, e l'**ordine** in cui scattano può cambiare il risultato.
- Esempio della slide (una diagnosi medica):

```text
R1: IF fever AND cough THEN suspect_flu               -- febbre e tosse → sospetta influenza
R2: IF fever AND rash  THEN suspect_measles           -- febbre ed eruzione cutanea → sospetto morbillo
R3: IF suspect_flu     THEN prescribe_antiviral       -- influenza → antivirale
R4: IF suspect_measles THEN prescribe_antibiotic      -- morbillo → antibiotico
```

- Se un paziente ha febbre, tosse ed eruzione cutanea, R1 e R2 scattano insieme: il sistema arriva a due diagnosi e due terapie diverse, cioè a esiti in conflitto o incoerenti.

#### Rule-based: spiegabilità · [[05_Architectural_Styles_Complete.pdf#page=71|p. 71]]

- Per capire un risultato può servire seguire **l'intera catena di inferenza**, cioè tutte le regole scattate una dopo l'altra.
- Spesso avere una risposta non basta: bisogna sapere **come** il motore ci è arrivato.
- **Tracciare le inferenze** (*inference tracing*) e analizzare i **log** rende il ragionamento più facile da ispezionare.

### Stile interpreter · [[05_Architectural_Styles_Complete.pdf#page=72|p. 72]]–[[05_Architectural_Styles_Complete.pdf#page=75|75]]

#### Elementi · [[05_Architectural_Styles_Complete.pdf#page=72|p. 72]]–[[05_Architectural_Styles_Complete.pdf#page=73|73]]

- Il comportamento dell'applicazione **non è fissato nel codice**: è specificato **a runtime** da **comandi** forniti mentre il programma è in esecuzione.
- L'**interprete** analizza ogni comando e lo esegue, aggiornando quando serve il proprio **stato di esecuzione**.
- **Componenti**: interprete dei comandi, stato del programma (o dell'interprete), interfaccia utente.
- **Connettori**: chiamate di procedura e stato condiviso.
- **Topologia**: tre parti principali, con lo stato separato dall'interprete.

#### Caratteristiche · [[05_Architectural_Styles_Complete.pdf#page=74|p. 74]]

- Il comportamento può essere **molto dinamico**, e l'insieme dei comandi può essere a sua volta estendibile.
- L'architettura resta **stabile**, mentre nuove funzionalità si ottengono **componendo comandi primitivi** già esistenti.
- Gli utenti finali possono **programmare** in larga misura il sistema.
- Esempi: Lisp, i motori SQL, gli ambienti di esecuzione di Java o JavaScript, le formule e le macro dei fogli di calcolo.
- In Excel le **formule** sono eseguite dal motore di calcolo e le **macro VBA** dall'ambiente Visual Basic.
- 🧩 *Esempio.* Scrivere in una cella `=SOMMA(A1:A10)` non richiede di modificare Excel: è un comando che il motore di calcolo interpreta.

#### Lunar Lander con interprete · [[05_Architectural_Styles_Complete.pdf#page=75|p. 75]]

![[lez08-stili-p75-interpreter-lunar-lander.png]]
*«Get Command from user» legge i comandi dell'utente e li manda, tramite uno stream, a «Interpret and Execute», che legge e scrive l'«Interpreter State» attraverso due connettori «Data Access».*

- Con un comando come `(Burn, 50)` l'interprete aggiorna la navicella e lo stato del gioco.
- Con `(Check Status)` recupera lo stato rilevante del gioco e mostra il risultato nella GUI.

### Stile mobile code · [[05_Architectural_Styles_Complete.pdf#page=76|p. 76]]–[[05_Architectural_Styles_Complete.pdf#page=83|83]]

#### Idea · [[05_Architectural_Styles_Complete.pdf#page=76|p. 76]]

- Il **codice viene trasmesso a un host remoto**, che lo esegue o lo interpreta.
- È utile quando:
  - le risorse di calcolo locali non bastano, oppure
  - grandi quantità di dati si trovano già su una macchina remota.
- Spostare il codice evita di trasferire grandi quantità di dati.
- Benefici potenziali: **meno traffico di rete**; il comportamento si può cambiare **senza sostituire l'architettura** complessiva.

#### Varianti · [[05_Architectural_Styles_Complete.pdf#page=77|p. 77]]–[[05_Architectural_Styles_Complete.pdf#page=80|80]]

| Variante | Che cosa c'è in locale | Che cosa si sposta |
|---|---|---|
| **Code on demand** | dati e risorse per eseguire | il codice necessario viene scaricato da un altro host |
| **Remote evaluation** | il codice | il codice va su un host remoto, che offre le risorse per eseguirlo |
| **Mobile agent** | il codice e solo una parte delle risorse | codice **e stato di esecuzione** migrano su un altro host, per ottenere le risorse che mancano in locale |

![[lez08-stili-p78-code-on-demand.png]]
*Code on demand: il browser chiede una pagina web al server, che restituisce del codice JavaScript; il codice viene eseguito nel browser.*

![[lez08-stili-p79-remote-evaluation.png]]
*Remote evaluation: il client invia il codice a un server di una griglia di calcolo (grid), dove viene eseguito, e riceve i risultati.*

- Il **grid computing** mette insieme risorse di calcolo distribuite per eseguire carichi di lavoro impegnativi; la fonte lo illustra con il calcolo ad alte prestazioni.
- Grid e **cloud computing** sono concetti distinti (🧩 nel grid si inviano lavori a una rete di macchine che cooperano; nel cloud si usano risorse noleggiate on demand da un provider).

![[lez08-stili-p80-mobile-agent.png]]
*Mobile agent: l'agente ha il codice e alcune risorse, non tutte, e decide da solo di migrare su un altro nodo per ottenere le risorse che gli mancano. In figura l'agente si sposta lungo un anello di nodi (Master, Node 0, 1, 2).*

#### Elementi · [[05_Architectural_Styles_Complete.pdf#page=81|p. 81]]

- **Componenti**: un **execution dock** (il punto di arrivo che riceve codice e stato) e un interprete o ambiente di esecuzione.
- **Connettori**: protocolli di rete e meccanismi per impacchettare codice e dati da trasmettere.
- **Elementi dati**: il codice (trattato come un dato da spedire), lo stato del programma, i dati applicativi.
- **Topologia**: una rete di host capaci di eseguire codice.

#### Lunar Lander con mobile code · [[05_Architectural_Styles_Complete.pdf#page=82|p. 82]]

- I client (browser web) **scaricano il codice del gioco** e lo eseguono in locale.
- Implementazioni storiche: applet Java o JavaScript.
- I client mantengono lo stato del gioco e fanno i calcoli, quindi il server deve elaborare meno.

![[lez08-stili-p82-mobile-code-lunar-lander.png]]
*Tre browser: il primo esegue un programma JavaScript con un interprete JavaScript e il suo stato; il secondo esegue un applet Java in una Java Virtual Machine; il terzo contiene il «Lunar Lander Game Code». Tutti comunicano con il server del gioco tramite Remote Procedure Call su HTTP.*

#### Benefici e limiti · [[05_Architectural_Styles_Complete.pdf#page=83|p. 83]]

**Benefici**

- **Adattamento dinamico**: si cambia il comportamento inviando nuovo codice.
- **Accesso alle risorse di elaborazione di altri host.**
- La migrazione può aiutare la **dependability** (la capacità del sistema di continuare a funzionare correttamente) quando esistono host alternativi: se un host non è disponibile, il codice può spostarsi altrove.

**Limiti**

- Gli host devono **proteggersi da codice non fidato**: il codice ricevuto potrebbe essere dannoso.
- I **costi di comunicazione** o le **connessioni inaffidabili** possono annullare il vantaggio dell'esecuzione remota.

**Usi tipici**

- Spostare il calcolo dove si trovano grandi insiemi di dati remoti.
- Configurare un'applicazione con codice fornito dall'esterno (🧩 ad es. un plugin).

### Cloud computing (cenni) · [[05_Architectural_Styles_Complete.pdf#page=84|p. 84]]–[[05_Architectural_Styles_Complete.pdf#page=88|88]]

#### Definizione · [[05_Architectural_Styles_Complete.pdf#page=84|p. 84]]

- Secondo il **NIST** (l'ente statunitense per gli standard), il cloud computing è un modello che permette di accedere via rete, in modo comodo e **on demand** (quando serve), a un **insieme condiviso di risorse di calcolo configurabili**.
- Le risorse si possono **ottenere e rilasciare rapidamente**, con poco sforzo di gestione e poca interazione con il provider.

#### Benefici potenziali · [[05_Architectural_Styles_Complete.pdf#page=85|p. 85]]

- **Per i clienti**:
  - meno bisogno di possedere e mantenere l'hardware e il software dell'infrastruttura;
  - modelli **pay-per-use** (si paga quanto si usa) e capacità che si può aumentare o ridurre secondo necessità;
  - servizi gestiti dal provider che possono aiutare affidabilità e sicurezza, a seconda dei servizi e della configurazione scelti.
- **Per i provider**: mettendo insieme la domanda di molti clienti, usano meglio le risorse e assorbono meglio le variazioni di carico tra un cliente e l'altro.

#### Modelli di servizio · [[05_Architectural_Styles_Complete.pdf#page=86|p. 86]]–[[05_Architectural_Styles_Complete.pdf#page=87|87]]

- **IaaS** (*Infrastructure as a Service*): il provider offre rete, storage e potenza di calcolo, ad esempio **macchine virtuali**. Il cliente installa e gestisce tutto il resto.
- **PaaS** (*Platform as a Service*): il provider offre l'infrastruttura **più** il sistema operativo e una piattaforma applicativa (application server, servizi di database, middleware). Il cliente porta la sua applicazione.
- **SaaS** (*Software as a Service*): il provider gestisce un'**applicazione completa**, che gli utenti usano di solito con un browser o un'app (🧩 ad es. una webmail).
- In tutti i casi il cliente usa una capacità senza possedere tutte le risorse che servono a fornirla.

![[lez08-stili-p86-modelli-di-servizio-cloud.png]]
*«Everything as a service»: a sinistra la pila SaaS (ad es. fotoritocco, gestione logistica), sopra PaaS (gestione cloud, monitoraggio, database, sviluppo software), sopra IaaS (storage, rete, calcolo, virtualizzazione), sopra il data center del provider; a destra la piramide SaaS – PaaS – IaaS.*

![[lez08-stili-p87-responsabilita-cloud.png]]
*Chi gestisce cosa. Quattro colonne (on premise, IaaS, PaaS, SaaS) con la stessa pila: Data, Application, MW/DBMS, Security, Operating Systems, Virtualization, Storage, Computing Resources, Networking, Data Centers. In blu ciò che gestisce il cliente, in verde ciò che gestisce il provider.*

- **On premise** (tutto nei locali del cliente): il cliente gestisce tutto.
- **IaaS**: il provider gestisce dalla virtualizzazione in giù; il cliente gestisce sistema operativo, sicurezza, middleware, applicazione e dati.
- **PaaS**: il provider gestisce anche sistema operativo, sicurezza e middleware; il cliente gestisce applicazione e dati.
- **SaaS**: il provider gestisce tutto tranne i dati.
- Più si va verso SaaS, meno il cliente deve gestire.

#### Modelli di deployment · [[05_Architectural_Styles_Complete.pdf#page=88|p. 88]]

- **Cloud privato**: infrastruttura per una sola organizzazione; gestita dall'organizzazione, da terzi o da entrambi; può stare nei locali dell'organizzazione (*on premises*) o altrove.
- **Community cloud**: infrastruttura per più organizzazioni con interessi comuni; gestita da uno o più membri, da terzi o da entrambi.
- **Cloud pubblico**: infrastruttura aperta al pubblico, gestita da un provider.
- **Cloud ibrido**: più infrastrutture cloud distinte, collegate tra loro in modo da poter spostare dati e applicazioni dall'una all'altra.

### Architetture con componenti disaccoppiati · [[05_Architectural_Styles_Complete.pdf#page=89|p. 89]]–[[05_Architectural_Styles_Complete.pdf#page=91|91]]

- 🧩 Due componenti sono **accoppiati** quando uno dipende dall'altro per funzionare: deve conoscerlo, deve essere attivo nello stesso momento, deve aspettarlo. Gli stili che seguono servono a ridurre queste dipendenze.

#### Forme di disaccoppiamento · [[05_Architectural_Styles_Complete.pdf#page=90|p. 90]]

- Si usa un **intermediario** (🧩 ad es. un broker di messaggi) che permette ai componenti di comunicare **senza indirizzarsi direttamente**.
- Tre forme di disaccoppiamento:
  - **nello spazio**, o del riferimento (*space / reference decoupling*): i componenti non devono conoscere l'identità l'uno dell'altro (🧩 chi invia non sa chi riceverà);
  - **nel tempo** (*time decoupling*): i componenti non devono essere attivi nello stesso momento; per questo i messaggi devono restare disponibili per essere consegnati più tardi (🧩 come una e-mail letta il giorno dopo);
  - **nella sincronizzazione** (*synchronization decoupling*): i componenti non devono aspettarsi durante l'interazione (🧩 chi invia prosegue subito, senza attendere la risposta).

#### Benefici e costi · [[05_Architectural_Styles_Complete.pdf#page=91|p. 91]]

- Un accoppiamento debole può migliorare l'**adattabilità** e la **scalabilità** dell'architettura.
- Il disaccoppiamento nello spazio permette ai componenti di spostarsi, cambiare, essere aggiunti o migrare.
- Il disaccoppiamento nel tempo tollera componenti che entrano nel sistema e ne escono.
- Il disaccoppiamento nella sincronizzazione riduce i blocchi tra componenti.
- **Costi**:
  - l'intermediario aggiunge **overhead** di elaborazione e di comunicazione;
  - i componenti dipendono comunque dai **formati dei messaggi** condivisi e dal loro significato.

### Stile implicit invocation (invocazione implicita) · [[05_Architectural_Styles_Complete.pdf#page=92|p. 92]]–[[05_Architectural_Styles_Complete.pdf#page=94|94]]

#### Idea · [[05_Architectural_Styles_Complete.pdf#page=92|p. 92]]

- È uno stile per organizzare componenti disaccoppiati.
- Di solito (invocazione *esplicita*) un componente chiama per nome il componente che deve agire. Nell'invocazione **implicita** invece:
  - i componenti **annunciano eventi**, invece di chiamare i componenti che dovrebbero reagire;
  - i componenti interessati **registrano un handler** (un gestore) per certi tipi di evento;
  - quando l'evento si verifica, il **meccanismo di distribuzione degli eventi** invoca o avvisa gli handler registrati;
  - chi annuncia l'evento **non sa** quali componenti risponderanno.
- La gestione degli eventi può essere:
  - **sincrona**: chi annuncia aspetta che gli handler abbiano finito;
  - **asincrona**: chi annuncia prosegue subito;
  - a seconda dell'implementazione.

#### Esempio · [[05_Architectural_Styles_Complete.pdf#page=93|p. 93]]

- Un **pulsante** annuncia l'evento «click»; i **listener** registrati reagiscono, ad esempio validando l'input o aggiornando l'interfaccia.
- **Beneficio**: si possono aggiungere nuovi handler senza modificare il componente che annuncia l'evento (il pulsante).
- **Trade-off**: il flusso di controllo diventa meno esplicito. Per capire cosa succede dopo un click bisogna scoprire quali handler sono registrati e con quali regole vengono eseguiti.
- Le due forme trattate nella lezione sono **publish–subscribe** e le **architetture event-based**.

#### Benefici e limiti · [[05_Architectural_Styles_Complete.pdf#page=94|p. 94]]

- **Benefici**: favorisce il **riuso** dei componenti e l'**evoluzione** del sistema, sia durante lo sviluppo sia a runtime.
- **Limiti**:
  - la struttura effettiva del sistema e il flusso di controllo possono essere difficili da capire;
  - è il meccanismo di consegna degli eventi a decidere quali handler vengono attivati e come;
  - chi annuncia può non sapere quali componenti risponderanno né in che ordine.

### Publish–subscribe · [[05_Architectural_Styles_Complete.pdf#page=95|p. 95]]–[[05_Architectural_Styles_Complete.pdf#page=106|106]]

#### Meccanismo di base · [[05_Architectural_Styles_Complete.pdf#page=95|p. 95]]–[[05_Architectural_Styles_Complete.pdf#page=96|96]]

- I **publisher** pubblicano messaggi **senza indirizzarli** a destinatari precisi.
- I **subscriber** dichiarano a cosa sono interessati: un **topic** (argomento), un tipo di evento o il contenuto dei messaggi.
- Un **meccanismo di distribuzione** consegna ogni messaggio ai subscriber interessati.
- 🧩 *Esempio.* Un'app meteo si iscrive al topic «temperatura Napoli»; il sensore pubblica la temperatura senza sapere quante app la riceveranno.

#### Elementi architetturali · [[05_Architectural_Styles_Complete.pdf#page=97|p. 97]]

- **Componenti**: publisher, subscriber ed eventualmente **proxy** o **broker** di distribuzione (intermediari).
- **Connettori**: chiamate di procedura dentro un programma locale, oppure protocolli di rete tra host diversi.
  - Se le sottoscrizioni sono basate sul **contenuto** dei messaggi, servono meccanismi di confronto (*matching*) e di instradamento (*routing*).
- **Elementi dati**: sottoscrizioni, notifiche, informazioni pubblicate.
- **Topologia**: i subscriber si collegano direttamente ai publisher oppure ricevono i messaggi tramite intermediari.
- **Qualità**: supporta la distribuzione di informazioni **uno-a-molti** con un accoppiamento limitato.

#### Publish–subscribe in un singolo programma · [[05_Architectural_Styles_Complete.pdf#page=98|p. 98]]

- I subscriber si **registrano** presso un publisher per certi messaggi o contenuti.
- Indicano la **callback** da chiamare, cioè la funzione che il publisher invocherà quando ha una notifica. Le callback vanno bene per implementazioni semplici e locali.
- I publisher tengono l'elenco dei propri subscriber e consegnano le notifiche in modo sincrono o asincrono.
- I subscriber possono **annullare la sottoscrizione** quando non sono più interessati.

#### Publish–subscribe in rete · [[05_Architectural_Styles_Complete.pdf#page=99|p. 99]]–[[05_Architectural_Styles_Complete.pdf#page=101|101]]

- Le grandi applicazioni distribuite usano **protocolli di rete** al posto delle callback locali.
- I publisher possono affidarsi a **proxy o broker** intermediari, che distribuiscono i messaggi a gruppi selezionati di subscriber.

![[lez08-stili-p100-pubsub-broker.png]]
*I publisher (a sinistra) inviano messaggi a un «Pub/Sub message broker», che li smista su canali, uno per topic («Channel (Topic)»); ogni canale consegna una copia del messaggio a tutti i subscriber (a destra) interessati a quel topic.*

![[lez08-stili-p101-pubsub-disaccoppiamento.png]]
*Le tre forme di disaccoppiamento ottenute con un middleware publish/subscribe tra un publisher (P) e i subscriber (S).*

- **Nello spazio**: P pubblica una volta e il middleware avvisa (notify()) più subscriber, senza che P sappia chi sono.
- **Nel tempo**: P pubblica mentre S è disconnesso; la notifica arriva più tardi, quando S torna disponibile.
- **Nella sincronizzazione**: P non si blocca ad aspettare; S riceve la notifica in modo asincrono.

#### Benefici potenziali · [[05_Architectural_Styles_Complete.pdf#page=102|p. 102]]

- **Estendibilità**: nuovi subscriber possono reagire alle pubblicazioni esistenti senza modificare il publisher.
- **Modificabilità**: publisher e subscriber evolvono separatamente, purché i **contratti dei messaggi** (formato e significato concordati) restino compatibili.
- **Interoperabilità**: protocolli e formati condivisi permettono la comunicazione tra piattaforme diverse.
- **Reattività**: con la consegna asincrona il publisher prosegue senza aspettare che i subscriber abbiano finito di elaborare.

#### Limiti · [[05_Architectural_Styles_Complete.pdf#page=103|p. 103]]

- Il publisher **non può dare per scontato** che i subscriber abbiano completato l'elaborazione.
- Garanzie di consegna, ordinamento e gestione dei **duplicati** richiedono decisioni esplicite (🧩 il messaggio arriva di sicuro? una volta sola? nell'ordine giusto?).
- Subscriber lenti possono causare **accumuli di messaggi** in attesa.
- Una modifica al contratto dei messaggi può toccare molti subscriber.
- Gli intermediari richiedono **capacità**, **monitoraggio** e meccanismi di **ripristino** in caso di guasto.

#### Applicazioni tipiche · [[05_Architectural_Styles_Complete.pdf#page=104|p. 104]]

- Diffusione di notizie.
- Interfacce grafiche.
- Giochi multigiocatore.
- Sistemi Internet of Things (IoT).

#### Lunar Lander publish–subscribe · [[05_Architectural_Styles_Complete.pdf#page=105|p. 105]]

- I giocatori si **iscrivono** al gioco e ricevono notifiche quando cambiano le informazioni che li interessano.
- Una notifica può contenere direttamente l'informazione aggiornata, oppure solo avvisare che c'è una novità, che il giocatore scaricherà poi esplicitamente.
- Il game server pubblica le informazioni sullo stato corrente della partita.

![[lez08-stili-p105-pubsub-lunar-lander.png]]
*I Subscriber 1, 2, …, n si registrano al Game Server attraverso uno stream (inviano register e le informazioni di registrazione); un connettore Event porta loro le notifiche, ad esempio il nuovo terreno e i dati della navicella.*

#### Esempio: MQTT · [[05_Architectural_Styles_Complete.pdf#page=106|p. 106]]

![[lez08-stili-p106-mqtt.png]]
*Un sensore di temperatura (publisher, client MQTT) pubblica «24 °C» sul topic temperature presso un MQTT Broker, che inoltra il valore ai client iscritti a quel topic: un dispositivo mobile e un sistema di backend.*

- **MQTT** è un protocollo di messaggistica standard (OASIS) per l'Internet of Things.
- È estremamente leggero: adatto a dispositivi remoti con poco codice e poca banda.
- È usato in automotive, manifattura, telecomunicazioni, oil & gas.

### Stile event-based · [[05_Architectural_Styles_Complete.pdf#page=107|p. 107]]–[[05_Architectural_Styles_Complete.pdf#page=118|118]]

#### Idea di base · [[05_Architectural_Styles_Complete.pdf#page=107|p. 107]]–[[05_Architectural_Styles_Complete.pdf#page=108|108]]

- Un **evento** segnala che è successo qualcosa di interessante: un click su un pulsante, un tick dell'orologio, una prenotazione confermata.
- I **producer** annunciano eventi; i **consumer** reagiscono secondo le proprie responsabilità; un componente può avere entrambi i ruoli.
- I **connettori** consegnano gli eventi con meccanismi di smistamento locali (*dispatching*) o con canali di rete, spesso tramite un **bus** o un **broker** di eventi.
- La gestione locale può essere sincrona o asincrona; i sistemi event-driven distribuiti usano di norma la consegna **asincrona**.

#### Eventi, implicit invocation e publish–subscribe · [[05_Architectural_Styles_Complete.pdf#page=109|p. 109]]

Tre concetti vicini, da non confondere:

| Concetto | Che cosa indica |
|---|---|
| **Implicit invocation** | il **principio di interazione**: un evento attiva gli handler senza che il producer li chiami esplicitamente |
| **Architettura event-based** | un modo di **organizzare il sistema**: i componenti cooperano attraverso eventi |
| **Publish–subscribe** | un **meccanismo di distribuzione**: consegna le pubblicazioni in base alle sottoscrizioni; è il meccanismo più comune per comunicare tramite eventi |

- Trasmettere ogni evento a tutti i componenti (*broadcast*) è un'opzione; con filtraggio e instradamento si consegnano a ciascuno solo gli eventi rilevanti.

#### Benefici · [[05_Architectural_Styles_Complete.pdf#page=110|p. 110]]

- **Estendibilità**: nuovi componenti possono reagire a eventi già esistenti, mentre i producer restano invariati.
- **Separazione delle responsabilità**: ogni consumer implementa la propria reazione, ad esempio avvisare un cliente o aggiornare un *read model* (una copia dei dati organizzata per essere letta velocemente).
- **Reattività**: i consumer asincroni possono rimandare il lavoro mentre il producer va avanti.
- **Scalabilità**: i consumer distribuiti possono scalare separatamente, se lo permettono:
  - il partizionamento degli eventi (come gli eventi sono divisi tra le istanze);
  - i vincoli sull'ordine degli eventi;
  - lo stato condiviso.

#### Limiti · [[05_Architectural_Styles_Complete.pdf#page=111|p. 111]]

- Il flusso di controllo attraversa più reazioni: è difficile seguire l'avanzamento di un'operazione e capire dove si è verificato un guasto.
- Con la consegna asincrona i consumer possono aggiornare il proprio stato in momenti diversi (🧩 per un po' possono vedere dati diversi).
- La consegna distribuita richiede decisioni su **retry** (nuovi tentativi), duplicati, ordinamento e ripristino.
- I **contratti degli eventi** creano dipendenze: se cambia la struttura o il significato di un evento, possono risentirne molti consumer.
- Handler lenti, **cicli di eventi** (🧩 A genera un evento che fa reagire B, che ne genera uno che fa reagire di nuovo A…) o canali sovraccarichi possono ritardare altre elaborazioni.

#### Lunar Lander event-based · [[05_Architectural_Styles_Complete.pdf#page=112|p. 112]]

- **Spacecraft** mantiene lo stato del veicolo: a ogni tick del clock ricalcola lo stato ed emette un evento.
- **Game Logic** usa lo stato della navicella e il tempo trascorso per decidere se la partita è finita.
- La **GUI** pubblica l'input dell'utente (il burn rate), riceve gli eventi sullo stato della navicella e aggiorna il display.

![[lez08-stili-p112-event-based-lunar-lander.png]]
*Spacecraft, Clock, Game Logic e GUI sono tutti collegati a un bus «Event». Il Clock invia i tick (t); Spacecraft emette lo stato (a, br, f, v); la GUI invia il burn rate (br).*

- 🧩 Nessun componente chiama direttamente un altro: tutti parlano solo con il bus.

#### Gestione locale degli eventi in Java · [[05_Architectural_Styles_Complete.pdf#page=113|p. 113]]

- Le librerie grafiche Java **AWT** e **Swing** mostrano l'interazione event-based **dentro una singola applicazione**:
  - le **sorgenti** generano oggetti evento;
  - i **listener** registrati li gestiscono con metodi di callback.
- Swing smista normalmente gli eventi grafici su un thread dedicato, l'**event dispatch thread**. Il codice dei listener deve terminare in fretta, altrimenti l'interfaccia smette di rispondere.
- Qui lo smistamento è locale, con callback: non serve un broker di rete.

#### Modello a eventi della GUI Java · [[05_Architectural_Styles_Complete.pdf#page=114|p. 114]]

- **Event source**: l'oggetto che genera l'evento, ad esempio un pulsante.
- **Event object**: l'oggetto che contiene le informazioni sull'evento, compresa la sorgente.
- **Event listener**: l'oggetto avvisato quando l'evento accade; un suo metodo gestisce l'evento.

#### Eventi e interfacce listener · [[05_Architectural_Styles_Complete.pdf#page=115|p. 115]]

- A ogni tipo di evento corrisponde un'**interfaccia listener**.
- Un `JButton` (pulsante) genera un `ActionEvent`, gestito da un oggetto che implementa `ActionListener`.
- Un `JComboBox` (menu a tendina) genera un `ItemEvent`, gestito da un oggetto che implementa `ItemListener`.

#### Collegare sorgenti e listener · [[05_Architectural_Styles_Complete.pdf#page=116|p. 116]]

- Le sorgenti offrono metodi per **registrare** i listener.
- Il listener implementa l'interfaccia richiesta dal tipo di evento: ad esempio `ActionListener` definisce il metodo `actionPerformed(ActionEvent e)`.
- Quando l'evento si verifica, la sorgente avvisa il listener chiamando il suo metodo di gestione.

#### Passi per gestire un evento · [[05_Architectural_Styles_Complete.pdf#page=117|p. 117]]

1. Creare una classe handler che implementa l'interfaccia listener adatta: ad esempio `ButtonClicking implements ActionListener`, con il metodo `actionPerformed(ActionEvent e)`.
2. Registrare l'handler presso la sorgente con `addActionListener`: ad esempio `yesButton.addActionListener(this)`. Qui `this` indica che la classe stessa fa da listener.

```java
// 🧩 Esempio completo, ricostruito dai due passi della slide
class ButtonClicking implements ActionListener {        // passo 1: la classe handler
    public void actionPerformed(ActionEvent e) {        // chiamato a ogni click
        System.out.println("Hai premuto Sì");
    }
}

JButton yesButton = new JButton("Sì");                  // la sorgente dell'evento
yesButton.addActionListener(new ButtonClicking());      // passo 2: registrazione
```

#### Per approfondire · [[05_Architectural_Styles_Complete.pdf#page=118|p. 118]]

- L'organizzazione event-based nelle applicazioni Android.
- La gestione degli eventi nelle interfacce grafiche.
- Il modello a eventi Java per le applicazioni con GUI.
- Altri framework per la gestione degli eventi.

### Appendice: stile peer-to-peer · [[05_Architectural_Styles_Complete.pdf#page=119|p. 119]]–[[05_Architectural_Styles_Complete.pdf#page=157|157]]

#### Idea · [[05_Architectural_Styles_Complete.pdf#page=119|p. 119]]–[[05_Architectural_Styles_Complete.pdf#page=121|121]]

- Architettura **decentralizzata**: le risorse sono distribuite tra nodi alla pari (*peer*) e condivise tra loro.
- Stato e comportamento sono **distribuiti**; ogni peer può fare sia da **client** sia da **server**.
- I peer sono componenti **indipendenti**, ognuno con il proprio stato e il proprio **thread di controllo** (🧩 ognuno esegue per conto suo, al contrario di main program e subroutine).
- **Connettori**: protocolli di rete, spesso specializzati per l'applicazione.
- **Elementi dati**: messaggi di rete.

#### Panoramica, funzioni e requisiti · [[05_Architectural_Styles_Complete.pdf#page=122|p. 122]]–[[05_Architectural_Styles_Complete.pdf#page=123|123]]

- Un sistema P2P è un insieme distribuito di nodi; ogni nodo può fornire servizi agli altri e chiederne, cioè fa da server e da client.
- Obiettivo dello stile: **condividere risorse e servizi** (dati, CPU, spazio su disco, …).
- Funzioni tipiche:
  - condivisione di file (*file sharing*);
  - archiviazione di file;
  - file system distribuito;
  - storage ridondante (più copie degli stessi dati);
  - calcolo distribuito.
- Requisiti non funzionali tipici: disponibilità, affidabilità, prestazioni, scalabilità, anonimato.

#### Sviluppo storico · [[05_Architectural_Styles_Complete.pdf#page=124|p. 124]]

- I sistemi P2P erano stati proposti circa 30 anni prima della slide, ma si sono diffusi soprattutto nell'ultimo decennio.
- L'interesse è cresciuto grazie ai sistemi di file sharing: **Napster** (1999) e **Gnutella** (2000).
- Nel 2000 il client Napster è stato scaricato da 50 milioni di utenti, con picchi di traffico di 7 TB al giorno.
- Gnutella ha seguito le orme di Napster:
  - la slide indica come prima release il 2003;
  - a giugno 2005 la rete Gnutella contava 1,81 milioni di computer;
  - nel 2007 era la rete di file sharing più popolare, con una quota di mercato stimata oltre il 40%;
  - i server host sono elencati su gnutellahost.com.

#### Fasi di un'applicazione P2P · [[05_Architectural_Styles_Complete.pdf#page=125|p. 125]]

1. **Boot**: il peer si collega alla rete e stabilisce le connessioni con altri peer. Un boot completamente P2P è raro (🧩 di solito serve un punto d'accesso noto per entrare).
2. **Lookup**: il peer cerca chi fornisce un certo servizio o informazione; in genere i fornitori sono **SuperPeer** (peer con un ruolo speciale).
3. **Resource sharing**: la risorsa richiesta e trovata viene consegnata, di solito in più segmenti.

#### Esempio di condivisione: BitTorrent · [[05_Architectural_Styles_Complete.pdf#page=126|p. 126]]

![[lez08-stili-p126-bittorrent.png]]
*BitTorrent. Il tracker conosce lo «sciame» (swarm) di peer che condividono un file e aiuta i client a scambiarsene i pezzi. I peer che hanno il file completo (100%) sono i seed; gli altri ne hanno solo una parte (74%, 23%, 19%, 54%). Il computer con il client BitTorrent (37% del file) riceve e invia più pezzi contemporaneamente, da e verso peer diversi.*

#### Classificazione delle architetture P2P · [[05_Architectural_Styles_Complete.pdf#page=127|p. 127]]

Le tre organizzazioni differiscono soprattutto per **come si trovano le risorse**:

| Organizzazione | Come si localizzano le risorse |
|---|---|
| **Centralizzata** | un server di indice centrale tiene un database aggiornato di tutti i contenuti e di tutti gli utenti; il database si aggiorna quando un peer si collega |
| **Decentralizzata** (P2P puro) | nessun server: ogni peer fa da server di indice per le proprie risorse, fa ricerche e fa da router, inoltrando le query agli altri peer |
| **Ibrida** | struttura gerarchica: una dorsale di Super Node fa da server di indice centrale |

#### P2P con indice centralizzato · [[05_Architectural_Styles_Complete.pdf#page=128|p. 128]]–[[05_Architectural_Styles_Complete.pdf#page=133|133]]

- C'è un **indice centralizzato**, usato per cercare le informazioni.
- Quando un peer si connette, comunica al server centrale il proprio indirizzo IP e i contenuti che possiede.
- Il **trasferimento dei file è decentralizzato** (avviene direttamente tra peer), ma la **ricerca dei contenuti è fortemente centralizzata**.
- Esempio: **Napster**.

![[lez08-stili-p128-indice-centralizzato.png]]
*Peer A manda una query (Q) all'Index server; la risposta (R) indica quale peer ha il contenuto; poi il download avviene direttamente tra i peer.*

- **Elementi**:
  - componente **Peer**:
    - ha capacità simili a quelle degli altri peer;
    - fa da server e da client;
    - è autonomo, senza un'autorità amministrativa che lo controlli;
    - è inaffidabile: i peer entrano ed escono dalla rete di frequente;
  - componente **Index Server**:
    - ha capacità speciali: permette ai peer di entrare nel sistema e di cercare i contenuti;
    - tiene un database aggiornato di tutti i contenuti e gli utenti, che si aggiorna quando un peer si collega;
  - connettore: un **protocollo di rete**, spesso specializzato per la comunicazione P2P.

![[lez08-stili-p130-indice-componenti.png]]
*Diagramma dei componenti: Peer A e Peer B (due specializzazioni di Peer) si scambiano dati con le interfacce «Provide data» e «Require data»; entrambi usano le interfacce Login e Search del Directory server.*

![[lez08-stili-p131-indice-classi.png]]
*Diagramma delle classi: Directory Index (operazioni Search() e Login()) è associato a molti Peer; Peer offre FileTransfer() ed è associato a sé stesso nei ruoli «requester» (chi chiede) e «provider» (chi fornisce).*

![[lez08-stili-p132-indice-sequenza.png]]
*Diagramma di sequenza: i peer fanno Login(IP, content) sul Directory server; un peer invia Query(q); il server esegue Search(q) e restituisce la lista dei peer che hanno il contenuto; il peer richiedente chiama Download(q) direttamente su uno di loro.*

![[lez08-stili-p133-napster.png]]
*Napster. A sinistra il flusso numerato tra Peer A, Peer B, Peer C e la directory dei peer e dei contenuti: richiesta, registrazioni, risposta con il peer che ha il file, download diretto. A destra il server di indice centrale di Napster tra i client su Internet, con il trasferimento del file direttamente tra due client.*

#### Indice centralizzato: benefici e trappole · [[05_Architectural_Styles_Complete.pdf#page=134|p. 134]]

**Benefici**

- Poco stato da mantenere su ogni peer (🧩 il peer deve conoscere solo il server).
- Uso limitato della banda.
- Alto tasso di successo delle ricerche.
- Risposte rapide alle ricerche.
- Facile da implementare e da mantenere.

**Trappole**

- **Single point of failure**: se il server cade, nessuno trova più niente.
- Vulnerabile alla censura (🧩 basta chiudere il server).
- Scala limitata.
- Carico possibilmente sbilanciato (🧩 tutto sul server).
- Il database può non essere aggiornato.

#### P2P puro (decentralizzato) · [[05_Architectural_Styles_Complete.pdf#page=135|p. 135]]–[[05_Architectural_Styles_Complete.pdf#page=140|140]]

![[lez08-stili-p136-p2p-decentralizzato.png]]
*Peer A invia una query (Q) ai peer vicini, che la inoltrano ad altri peer; le risposte (R) tornano indietro lungo lo stesso percorso; il download avviene poi direttamente tra Peer A e il peer che ha la risorsa.*

- Il P2P decentralizzato organizza la **rete overlay** (🧩 la rete logica dei collegamenti tra peer, costruita sopra Internet) come un **grafo casuale**.
- Ogni nodo conosce solo un sottoinsieme di nodi, i suoi **vicini**, scelti in modi diversi: nodi fisicamente vicini, nodi entrati nella rete più o meno nello stesso momento, ecc.
- Esempio: **Gnutella**.
- **Elementi**:
  - componente **Peer**: capacità simili agli altri, server e client insieme, autonomo, inaffidabile; ha solo una **conoscenza locale**, perché conosce un piccolo insieme di altri nodi;
  - connettore: protocollo di rete, spesso specializzato per il P2P.

![[lez08-stili-p138-gnutella.png]]
*Gnutella. A sinistra una rete di peer (1–8) collegati ai vicini. A destra una query per il file «Baby Go Home.mp3» si propaga per 6–7 livelli, a seconda del time-to-live; il peer che possiede il file risponde «I've got it!». La query raggiunge 8.000–10.000 computer.*

- **Come funziona Gnutella**:
  - un peer usa un client Gnutella e una *peer cache* (un elenco di peer noti) per scoprire gli indirizzi IP di altri peer;
  - chiede una connessione (*Gnutella Connect*); l'altro nodo, detto *servent* (server + client), accetta (*Gnutella OK*) o rifiuta, per mancanza di capacità o per incompatibilità di protocollo;
  - scambi di messaggi *ping* e *pong* servono a scoprire peer e risorse disponibili;
  - ogni query porta un **time-to-live** (TTL), un contatore che ogni peer decrementa quando la inoltra; quando arriva a zero la query non viene più inoltrata, e così si limitano la propagazione e il carico di rete;
  - ogni messaggio ha un identificativo univoco, che aiuta a evitare che una query giri all'infinito in un ciclo.

![[lez08-stili-p140-p2p-decentralizzato-classi.png]]
*Diagramma delle classi: la classe Peer offre i servizi service1(), service2(), …, serviceN() ed è associata a sé stessa nei ruoli «requester» e «provider»: ogni peer può chiedere e fornire servizi.*

#### P2P puro: benefici e trappole · [[05_Architectural_Styles_Complete.pdf#page=141|p. 141]]

**Benefici**

- Poco stato da mantenere su ogni peer.
- Tolleranza ai guasti (🧩 non c'è un nodo centrale da cui dipendono tutti).

**Trappole**

- Alto uso di banda (🧩 ogni query viene inoltrata a molti peer).
- Tempo lungo per trovare un elemento.
- Nessuna garanzia di trovarlo (🧩 il TTL può esaurirsi prima).
- Carico possibilmente sbilanciato.

#### P2P ibrido · [[05_Architectural_Styles_Complete.pdf#page=142|p. 142]]–[[05_Architectural_Styles_Complete.pdf#page=147|147]]

- Crea una **struttura gerarchica**: una dorsale di **Super Node** (nodi più potenti) che svolgono il ruolo di un server di indice centrale.
- Quando un client entra nella rete, si collega direttamente a un singolo **Super Peer**.
- Esempio: **Skype**.

![[lez08-stili-p143-p2p-ibrido.png]]
*I peer ordinari (Peer A, Peer B) sono collegati ai Super Nodes, che si scambiano tra loro query (Q) e risposte (R); il download avviene poi direttamente tra i peer.*

- **Elementi**:
  - componente **Peer**: come negli altri casi (capacità simili, server e client, autonomo, inaffidabile);
  - componente **Super Peer**:
    - raccoglie e memorizza informazioni sui peer e sui contenuti disponibili per la condivisione;
    - fa da server per i peer normali e da peer verso gli altri super peer;
    - mantiene gli indici di alcuni o di tutti i nodi del sistema;
  - connettore: protocollo di rete, spesso specializzato per il P2P.

![[lez08-stili-p145-ibrido-componenti.png]]
*Diagramma dei componenti: i Simple peer A e B si scambiano dati direttamente; ognuno fa login e ricerca sul proprio Super peer (X o Y); i Super peer si passano le query con l'interfaccia «Disseminate query».*

![[lez08-stili-p146-ibrido-classi.png]]
*Diagramma delle classi: Peer (con FileTransfer() e l'associazione requester/provider) è specializzato in Super Peer, che aggiunge Search(), Login() e DisseminateQuery(), e in Simple Peer.*

![[lez08-stili-p147-ibrido-sequenza.png]]
*Diagramma di sequenza: i peer fanno Login(IP, content) sul proprio SuperPeer; un peer invia Query(q) al suo SuperPeer, che esegue Search(q) e inoltra la query agli altri SuperPeer con DisseminateQuery(q); la lista dei peer trovati torna al richiedente, che scarica con Download(q) direttamente dal peer che ha la risorsa.*

#### Esempio storico: Skype delle origini · [[05_Architectural_Styles_Complete.pdf#page=148|p. 148]]–[[05_Architectural_Styles_Complete.pdf#page=151|151]]

![[lez08-stili-p148-skype-supernodi.png]]
*La rete Skype delle origini: un Login Server, alcuni supernodi (A, B, C) collegati tra loro e, attorno a ciascun supernodo, un gruppo di peer ordinari (1–8).*

Come Skype affrontava i problemi del P2P:

- **Scoperta dei peer** (*discovery*): con un'architettura mista, in parte client–server (il Login Server) e in parte peer-to-peer.
- **Scalabilità e robustezza**, i problemi di Napster: le directory sono replicate e distribuite sui supernodi, invece di stare su un unico server.
- **Prestazioni**: i peer ordinari vengono promossi a supernodi in base alle loro capacità di rete e di elaborazione, perché i servizi importanti non vanno affidati a un peer qualsiasi.
- **Privacy**: un protocollo proprietario con cifratura protegge le chiamate che passano attraverso i supernodi intermediari.
- **Sicurezza**: la rete accetta solo i client rilasciati da Skype, progettati per resistere a ispezioni e modifiche; così i client malevoli non riescono a entrare.

![[lez08-stili-p151-skype-architettura.png]]
*L'architettura di Skype a livelli: registrazione e autenticazione, super node, client. A destra la rete di host ordinari (SC) e super node (SN) con le relazioni di vicinato, e le chiamate tra client pubblici e tra client dietro un firewall.*

#### P2P ibrido: benefici e trappole · [[05_Architectural_Styles_Complete.pdf#page=152|p. 152]]

**Benefici**

- Stato da mantenere su ogni nodo gestibile.
- Uso della banda e tempo di ricerca gestibili.
- Successo della ricerca garantito (🧩 i super peer hanno gli indici dei contenuti).

**Trappole**

- Carico possibilmente sbilanciato (🧩 sui super peer).
- Più difficile garantire la tolleranza ai guasti.

#### Scoperta delle risorse · [[05_Architectural_Styles_Complete.pdf#page=153|p. 153]]

- Senza una directory centrale, **trovare le risorse** diventa il problema fondamentale.
- Nel P2P puro una richiesta viene inoltrata a molti peer; trovata la risorsa, chi l'ha chiesta contatta direttamente chi la fornisce.
- Gli algoritmi di instradamento delle query (*query routing*) e il consumo di banda limitano questo approccio.
- I sistemi ibridi usano peer selezionati o directory per trovare le risorse.
- Ad esempio il Napster originale centralizzava la ricerca delle risorse e decentralizzava il trasferimento dei file.

#### Topologia e qualità · [[05_Architectural_Styles_Complete.pdf#page=154|p. 154]]

- La topologia permette **connessioni multiple** tra peer.
- La topologia può **cambiare dinamicamente**, man mano che i peer entrano o escono.
- Controllo e risorse sono **distribuiti** tra i nodi che partecipano.
- La decentralizzazione può **tollerare il guasto** di alcuni nodi, se ci sono abbastanza peer e percorsi alternativi.
- La **capacità cresce** con le risorse e la potenza di calcolo messe a disposizione dai peer (🧩 più peer entrano, più risorse ha la rete).

#### Esempi applicativi · [[05_Architectural_Styles_Complete.pdf#page=155|p. 155]]

- Distribuzione e archiviazione di contenuti: file e video in streaming.
- Reti, protocolli e client di file sharing: Gnutella, FastTrack, BitTorrent, eMule, uTorrent.
- Sistemi storici di televisione P2P, come PPLive.
- Collaborazione e comunicazione: chat, messaggistica istantanea, telefonia su Internet (le prime versioni di Skype).
- Reti per la distribuzione di contenuti (*content delivery network*) come CoralCDN, e reti di sensori.

#### Lunar Lander peer-to-peer · [[05_Architectural_Styles_Complete.pdf#page=156|p. 156]]

- Al tempo T₀ la navicella LL1 chiede ai peer vicini se altre navicelle sono atterrate; i vicini possono inoltrare la richiesta ad altri peer.
- Quando un peer, ad esempio LL5, trova la risorsa (cioè l'informazione), il risultato torna indietro fino a LL1.
- Al tempo T₁ LL1 contatta direttamente LL5 per chiedere altre informazioni.

![[lez08-stili-p156-p2p-lunar-lander.png]]
*In alto la rete al tempo T₀: LL1 è collegata a LL3 e a LL2, e LL2 è collegata a LL4, LL5 e LL6; ogni collegamento è uno stream. La richiesta di LL1 raggiunge LL5 passando per LL2. In basso il tempo T₁: LL1 e LL5 sono collegate direttamente da uno stream.*

#### Per approfondire · [[05_Architectural_Styles_Complete.pdf#page=157|p. 157]]

- Analizzare gli stili architetturali di applicazioni open source.
- Descrizioni architetturali di molte applicazioni si trovano in *The Architecture of Open Source Applications* (http://aosabook.org/en/index.html).

*Approfondimenti nel wiki: [[stili-architetturali]], [[layered]], [[client-server]], [[pipe-and-filter]], [[publish-subscribe]], [[peer-to-peer]], [[lunar-lander-in-ogni-stile]], [[microservices]], [[pattern-architetturali]]*

## Lezione 9 — Il processo di progettazione architetturale: ASR e il metodo ADD

*Fonte: 06-ADD-Designing a Software Architecture.pdf (41 pagine). Cap. 19–20 di Bass, Clements, Kazman, «Software Architecture in Practice»: requisiti architetturalmente significativi (cap. 19) e progettare un'architettura con ADD (cap. 20).*

### Requisiti architetturalmente significativi (ASR) · [[06-ADD-Designing a Software Architecture.pdf#page=2|p. 2]]–[[06-ADD-Designing a Software Architecture.pdf#page=4|4]]

- Sommario: *Architecturally Significant Requirements* (cap. 19); *Designing an Architecture with ADD* (cap. 20).
- Un **ASR** è un requisito che avrà un **effetto profondo sull'architettura**: l'architettura potrebbe essere drasticamente diversa in sua assenza. Spesso (ma non sempre) gli ASR hanno la forma di **requisiti di attributi di qualità** (prestazioni, sicurezza, modificabilità, disponibilità, usabilità…) che l'architettura deve fornire al sistema.
- **Come trovare gli ASR** (p. 4): gli architetti li identificano **da un documento dei requisiti** oppure **intervistando gli stakeholder** e conducendo un **Quality Attribute Workshop (QAW)**. Il QAW è un metodo facilitato, focalizzato sugli stakeholder, per **generare, prioritizzare e raffinare scenari di attributi di qualità** prima che l'architettura software sia completata. I risultati delle interviste devono includere un **elenco di driver architetturali** e un **insieme di scenari di qualità prioritizzati** dagli stakeholder.

### Scenario concreto d'esempio e utility tree · [[06-ADD-Designing a Software Architecture.pdf#page=5|p. 5]]–[[06-ADD-Designing a Software Architecture.pdf#page=8|8]]

- Scenario di modificabilità d'esempio (p. 5): *uno sviluppatore vuole cambiare l'interfaccia utente; la modifica sarà fatta nel codice in fase di progettazione, richiederà meno di tre ore per essere fatta e collaudata e non ci saranno effetti collaterali.*
- **Se non c'è nessuno stakeholder disponibile** (p. 6): l'architetto può costruire un **utility tree** quando le «fonti primarie» dei requisiti non sono disponibili. È una **rappresentazione top-down degli ASR legati agli attributi di qualità** che l'architetto ritiene critici per il successo del sistema. Per ogni attributo di qualità si riportano **raffinamenti specifici** (per esempio le prestazioni possono essere scomposte in «latenza dei dati» e «throughput delle transazioni», oppure in «tempo di attesa dell'utente» e «tempo di aggiornamento della pagina web»). Sotto ogni raffinamento si registrano gli **ASR specifici, espressi come scenari di qualità**.
- Gli scenari si valutano con **due criteri**: il **valore di business** dello scenario candidato e il **rischio tecnico** di realizzarlo; si può usare un semplice punteggio **H** (alto), **M** (medio), **L** (basso) per ciascun criterio (coppia «valore di business, rischio tecnico»).

**Esempio di utility tree** (pp. 7–8, sistema ospedaliero)

| Attributo | Raffinamento | Scenario ASR | (valore, rischio) |
|---|---|---|---|
| Prestazioni | tempo di risposta delle transazioni | un utente aggiorna l'account di un paziente in risposta a una notifica di cambio indirizzo mentre il sistema è sotto carico di picco, e la transazione si completa in meno di 0,75 secondi | (H, H) |
| Prestazioni | throughput | al carico di picco il sistema completa 150 transazioni normalizzate al secondo | (M, M) |
| Usabilità | formazione | un neoassunto con almeno due anni di esperienza nel settore impara, con 1 settimana di formazione, a eseguire qualsiasi funzione principale del sistema in meno di 5 secondi | (M, L) |
| Usabilità | efficienza delle operazioni | un addetto ai pagamenti dell'ospedale avvia un piano di pagamento per un paziente mentre interagisce con lui e completa il processo senza errori di input | (M, M) |
| Configurabilità | configurabilità dei dati | un ospedale aumenta la tariffa di un servizio; il team di configurazione fa e collauda la modifica in 1 giorno lavorativo, senza cambiare il codice sorgente | (H, L) |
| Manutenibilità | modifiche di routine | un manutentore trova carenze nel tempo di risposta, corregge il bug e distribuisce la correzione con non più di 3 persone-giorno di sforzo | (H, M) |
| Manutenibilità | modifiche di routine | un requisito di reporting richiede di cambiare i metadati di generazione dei report; la modifica è fatta e collaudata in 4 persone-ore | (M, L) |
| Manutenibilità | aggiornamento di componenti commerciali | il fornitore del database rilascia una nuova versione maggiore, che viene collaudata e installata con successo in meno di 3 persone-settimane | (H, M) |
| Manutenibilità | aggiunta di una funzionalità | una funzionalità che traccia i donatori di sangue viene creata e integrata con successo in 2 persone-mesi | (M, M) |
| Sicurezza | riservatezza | un fisioterapista può vedere la parte della cartella di un paziente relativa al trattamento ortopedico, ma non le altre parti né informazioni finanziarie | (H, M) |
| Sicurezza | resistenza agli attacchi | il sistema respinge un tentativo di intrusione non autorizzato e lo segnala alle autorità entro 90 secondi | (H, M) |
| Disponibilità | nessun fermo | il fornitore del database rilascia un nuovo software, sostituito a caldo (*hot-swapped*) senza downtime | (H, L) |
| Disponibilità | nessun fermo | il sistema supporta l'accesso web 24/7/365 ai conti da parte dei pazienti | (M, M) |

![[lez09-add-p7-utility-tree-1.png]]
![[lez09-add-p8-utility-tree-2.png]]
*L'utility tree in forma di tabella (attributo di qualità, raffinamento dell'attributo, scenario ASR con coppia H/M/L).*

### ADD: un processo di progettazione iterativo · [[06-ADD-Designing a Software Architecture.pdf#page=9|p. 9]]–[[06-ADD-Designing a Software Architecture.pdf#page=11|11]]

- *La necessità di un metodo* (p. 9) → **Attribute-Driven Design** (p. 10).
- In ADD la progettazione dell'architettura avviene per **round**. Ogni round può svolgersi dentro un'iterazione di sviluppo, come uno sprint. Dentro i round si compie una serie di **iterazioni di progettazione**: con una o più iterazioni si produce un'architettura adatta allo **scopo di progetto** stabilito per quel round. ADD fornisce una **guida dettagliata, passo per passo**, ai compiti da svolgere dentro le iterazioni.

### System Context Diagram · [[06-ADD-Designing a Software Architecture.pdf#page=12|p. 12]]

- Prima di iniziare la progettazione è importante determinare l'**ambito del sistema**: cosa sta dentro e cosa fuori dal sistema che si sta creando, e con quali **entità esterne** il sistema interagisce. Questo contesto si rappresenta con un **system context diagram**.

![[lez09-add-p12-system-context-diagram.png]]
*Il sistema in progettazione (cerchio) con la workstation dell'utente, i servizi esterni e un database server; legenda: sistema in sviluppo, sistema esterno, flusso di dati.*

### Passi e artefatti di ADD · [[06-ADD-Designing a Software Architecture.pdf#page=13|p. 13]]

![[lez09-add-p13-passi-e-artefatti-add.png]]
*Gli ingressi (driver): scopo del progetto, requisiti funzionali primari, scenari di attributi di qualità, vincoli, preoccupazioni architetturali (in rosso). I sette passi (in blu): **Step 1** Review inputs → **Step 2** Establish iteration goal by selecting drivers → **Step 3** Choose one or more elements of the system to refine → **Step 4** Choose one or more design concepts that satisfy the selected drivers → **Step 5** Instantiate architectural elements, allocate responsibilities, and define interfaces → **Step 6** Sketch views and record design decisions → **Step 7** Perform analysis of current design and review iteration goal and achievement of design purpose. L'uscita è il (raffinato) progetto dell'architettura software (in verde). Si itera se necessario; si parte dal round precedente o, se il sistema esiste, dal sistema esistente (brownfield).*

### Passo 1: rivedere gli ingressi · [[06-ADD-Designing a Software Architecture.pdf#page=14|p. 14]]–[[06-ADD-Designing a Software Architecture.pdf#page=15|15]]

- Prima di iniziare un round di progettazione bisogna assicurarsi che i **driver architetturali** siano disponibili e corretti: lo **scopo** del round di progettazione; i **requisiti funzionali primari** (casi d'uso o user story); gli **scenari primari di attributi di qualità**; gli eventuali **vincoli**; le eventuali **preoccupazioni** (*concerns*).
- I driver entrano a far parte di un **backlog di progettazione architetturale** da usare per svolgere le varie iterazioni di progettazione. Prima di iniziare, bisogna essere certi di avere chiaro **il problema di progetto complessivo da risolvere**.

### Passo 2: stabilire l'obiettivo dell'iterazione · [[06-ADD-Designing a Software Architecture.pdf#page=16|p. 16]]–[[06-ADD-Designing a Software Architecture.pdf#page=17|17]]

- Ogni iterazione di progettazione si concentra su un **obiettivo particolare**, che di solito consiste nel progettare per soddisfare un **sottoinsieme dei driver**. Esempio: creare strutture da elementi che permettano di ottenere un particolare scenario di prestazioni, o un caso d'uso.
- **Il problema di progetto è diviso in più sotto-problemi; un'iterazione comincia decidendo quale sotto-problema affrontare.**

### Passo 3: scegliere uno o più elementi del sistema da raffinare · [[06-ADD-Designing a Software Architecture.pdf#page=18|p. 18]]–[[06-ADD-Designing a Software Architecture.pdf#page=19|19]]

- Soddisfare i driver → prendere **decisioni di progetto architetturale** → le decisioni si manifestano in una o più **strutture architetturali** (fatte di elementi correlati, come moduli o componenti). In ogni iterazione gli elementi si raffinano con un approccio **top-down** o **bottom-up**.
- Per risolvere il sotto-problema si prendono **tre tipi di decisioni** (p. 18, passi 3–5): **1.** scegliere le parti da scomporre; **2.** individuare e selezionare le soluzioni esistenti che supportano la scomposizione; **3.** creare elementi dalla soluzione esistente e stabilirne responsabilità e interfacce.

### Passo 4: scegliere i design concept che soddisfano i driver · [[06-ADD-Designing a Software Architecture.pdf#page=20|p. 20]]–[[06-ADD-Designing a Software Architecture.pdf#page=24|24]]

- Bisogna identificare i vari **design concept** che potrebbero plausibilmente raggiungere l'obiettivo dell'iterazione, e scegliere tra le alternative. Esistono molti tipi di design concept — **tattiche, pattern, architetture di riferimento, componenti sviluppati esternamente** — e per ognuno molte opzioni. Si possono cercare in fonti diverse (blog e siti web, letteratura di ricerca, libri). Ne può risultare un numero considerevole di alternative da analizzare prima della scelta finale.
- **Selezionare i design concept** (p. 21): una volta identificata una lista di design concept bisogna sceglierne uno. Come? **Creando una tabella che elenca pro e contro di ogni alternativa** e scegliendo in base ai propri criteri e driver.

**Tabella d'esempio a supporto della selezione** (p. 22)

| Alternativa | Pro | Contro | Costo |
|---|---|---|---|
| Web application | accessibile da molte piattaforme con un browser web standard; caricamento veloce delle pagine; deployment semplice | non supporta un'interazione «ricca» | basso |
| Rich internet application | supporta un'interazione utente «ricca»; deployment e aggiornamento semplici | tempi di caricamento più lunghi; richiede un ambiente di runtime installato nel browser del client | medio |
| Mobile application | supporta un'interazione utente «ricca» | minore portabilità; limiti dello schermo | alto |

![[lez09-add-p22-tabella-selezione-alternative.png]]
*La tabella originale (nome dell'alternativa, pro, contro, costo).*

- **Se la tabella non basta** (p. 23) si possono creare **prototipi** e raccogliere misurazioni. Ma creare prototipi può essere costoso rispetto all'analisi: *che fare, e perché?*
- **Prototipare o no?** (p. 24) Domande da considerare: il progetto incorpora tecnologie emergenti? la tecnologia è nuova per l'azienda? ci sono driver, in particolare attributi di qualità, la cui soddisfazione con la tecnologia scelta presenta rischi? manca evidenza che la tecnologia scelta aiuterà a soddisfare i driver del progetto? ci sono opzioni di configurazione associate alla tecnologia che vanno testate o capite? non è chiaro se la tecnologia scelta si può integrare con il progetto? **Se la maggior parte delle risposte è «sì» conviene considerare un prototipo usa-e-getta (*throwaway prototype*).**

### Passo 5: istanziare gli elementi, assegnare le responsabilità e definire le interfacce · [[06-ADD-Designing a Software Architecture.pdf#page=25|p. 25]]–[[06-ADD-Designing a Software Architecture.pdf#page=29|29]]

- Scelti uno o più design concept bisogna **istanziarli**. Esempio: se si è scelto il pattern a strati, bisogna decidere il **numero di strati** e le loro **relazioni consentite**.
- Vanno definite le **responsabilità** di ogni elemento istanziato (per esempio gli strati di presentazione, logica di business e dati hanno responsabilità note e diverse). Gli elementi istanziati vanno anche **collegati**, perché possano collaborare: servono relazioni e scambio di informazioni tramite una **interfaccia**, che è una **specifica contrattuale** di come l'informazione deve fluire tra gli elementi.
- **Produrre le strutture** (p. 26): le strutture si classificano in: **strutture di modulo** (elementi che esistono a tempo di sviluppo: file, moduli, classi); **strutture C&C** (elementi dinamici che esistono a runtime: processi, thread); **strutture di allocazione** (elementi software di una struttura di modulo o C&C e elementi non software come file system, hardware, team di sviluppo). Istanziando un design concept può servire produrre più di una struttura.
- **Definire le interfacce** (p. 27): le interfacce sono le proprietà **visibili dall'esterno** degli elementi, che stabiliscono una specifica contrattuale che permette agli elementi di collaborare e scambiare informazioni. Due categorie: **esterne** e **interne**.
- **Interfacce esterne** (p. 28): comprendono le interfacce di altri sistemi **richieste** dal sistema in sviluppo e le interfacce **fornite** dal sistema agli altri sistemi. Un **system context diagram** aiuta a capirle.

![[lez09-add-p28-interfacce-esterne.png]]
*Esempio di system context diagram per il sistema FCAPS: workstation dell'utente, Time Server e database server come sistemi esterni.*

- **Interfacce interne** (p. 29): sono le interfacce **tra gli elementi** che risultano dall'istanziazione dei design concept. Un **diagramma di sequenza** aiuta a capirle.

![[lez09-add-p29-interfacce-interne.png]]
*Diagramma di sequenza d'esempio con le chiamate tra oggetti (TimeServerConnector, TimeServerConfigurationController, TimeServerDataMapper, Time Server, TopologyController).*

### Passo 6: abbozzare le viste e registrare le decisioni · [[06-ADD-Designing a Software Architecture.pdf#page=30|p. 30]]–[[06-ADD-Designing a Software Architecture.pdf#page=38|38]]

- Le **viste** definite nei passi precedenti vanno **abbozzate** (p. 31). Le decisioni significative prese nell'iterazione, e le **ragioni** che le hanno motivate (la **rationale**), vanno annotate per facilitare l'analisi e la comprensione successive: per esempio le decisioni sui trade-off importanti. Durante un'iterazione le decisioni si prendono soprattutto nei **passi 4 e 5**. Il «progetto» (*blueprint*) viene raffinato; può essere fatto **in parallelo al passo 5**. **Non è documentazione completa ma schizzi (*sketches*).**
- **Registrare gli schizzi** (p. 32): se si usa una notazione informale bisogna **mantenere coerenza nell'uso dei simboli** (e aggiungere una **legenda**); sviluppare la disciplina di **scrivere le responsabilità** che si assegnano agli elementi mentre si creano le strutture: scriverle *subito* evita di doverle ricordare dopo.

![[lez09-add-p33-sketch-e-responsabilita.png]]
*Esempio di schizzo (architettura a Batch Layer, Speed Layer e Serving Layer con Data Stream, raw data storage, viste precalcolate, interfacce di query) con la tabella «elemento — responsabilità» (per esempio Data Stream: raccoglie dati da tutte le fonti in tempo reale e li invia sia al Batch Layer sia al Speed Layer; Batch Layer: memorizza i dati grezzi e precalcola le Batch Views da memorizzare nel Serving Layer).*

- **Registrare le decisioni di progetto** (p. 34): in ogni iterazione si prendono decisioni importanti per raggiungere l'obiettivo, per esempio: scegliere un design concept tra diverse alternative; creare strutture istanziando il design concept scelto; stabilire relazioni tra elementi e definire interfacce; allocare risorse (persone, hardware, calcolo…); altro.
- **Registrare la rationale** (pp. 35–36): registrare le decisioni **oltre** a elementi, relazioni e proprietà è fondamentale per aiutare gli altri a capire come si è arrivati al risultato. Informazioni utili da registrare: quali evidenze sono state prodotte per giustificare le decisioni? chi ha fatto cosa? perché si sono prese scorciatoie? perché si sono fatti certi trade-off? quali ipotesi sono state fatte?
- **Tenere traccia dell'avanzamento della progettazione** (p. 37; esempio di kanban board a p. 38): quando si progetta ci sono domande a cui rispondere: quanta progettazione serve? quanta ne è stata fatta finora? abbiamo finito? **Pratiche Agile come backlog e kanban board** aiutano a tracciare l'avanzamento e a rispondere. Qualsiasi progetto, con qualsiasi metodologia, dovrebbe tracciare l'avanzamento.

![[lez09-add-p38-kanban-board.png]]
*Esempio di kanban board di progettazione con colonne «Not Yet Addressed», «Partially Addressed», «Completely Addressed», «Discarded»: ogni scheda è un driver (scenario di qualità QA, vincolo CT, preoccupazione CN, caso d'uso UC) con la sua priorità (High/Medium/Low).*

### Passo 7: analizzare il progetto corrente e rivedere l'obiettivo · [[06-ADD-Designing a Software Architecture.pdf#page=39|p. 39]]–[[06-ADD-Designing a Software Architecture.pdf#page=40|40]]

- **Analisi del progetto corrente:** si può fare da soli rivedendo gli schizzi delle viste e le decisioni registrate, ma è meglio che **qualcun altro** aiuti a rivedere il progetto (con un'esperienza e una prospettiva diverse) e trovi errori. Le decisioni prese a questo punto sono analizzate, insieme ai progressi del processo di progettazione, per decidere se servono altre iterazioni.
- **Rivedere l'obiettivo dell'iterazione:** esaminare lo stato dell'architettura rispetto allo scopo di progetto stabilito: considerare se sono state fatte abbastanza iterazioni per soddisfare i driver associati al round, e se lo scopo di progetto è stato raggiunto o servono ulteriori round in incrementi futuri.
- **Iterare i passi 2–7 per ogni driver**, a partire da quelli a priorità più alta.

### Riepilogo · [[06-ADD-Designing a Software Architecture.pdf#page=41|p. 41]]

- Presentata una guida dettagliata al metodo **Attribute-Driven Design, versione 3.0**. Discussi aspetti aggiuntivi da considerare nei passi: l'uso di un **backlog**; l'identificazione e selezione dei **design concept** e il loro uso nel produrre strutture; la **definizione delle interfacce**; la produzione di **documentazione preliminare**. Documentazione preliminare e attività di analisi vanno svolte regolarmente come parti integranti del processo di progettazione.

*Approfondimenti nel wiki: [[attribute-driven-design]], [[scenari-di-qualita]], [[buone-pratiche-architetturali]], [[strutture-e-viste]]*

## Lezione 10 — Architetture orientate ai servizi e a microservizi (parte 1)

*Fonte: 07— Service-Oriented and Microservice Architectures-1 part.pdf (47 pagine, «Service-Oriented and Microservice Architectures», prof.ssa Anna Rita Fasolino: servizi, contratti e trade-off di qualità). Esempio ricorrente: Food To Go (FTGO).*

### Prospettiva storica · [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=2|p. 2]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=7|7]]

- **Sistemi aziendali precedenti:** applicazioni centralizzate e sistemi client–server organizzavano l'accesso a funzioni e dati aziendali condivisi. **Anni '90:** applicazioni multi-tier e middleware a oggetti distribuiti supportavano la cooperazione tra processi e macchine. **Anni 2000:** SOA e tecnologie di web service affrontavano l'integrazione con **contratti di servizio espliciti** e messaggi interoperabili. **Anni 2010:** i microservizi hanno enfatizzato **capacità di business distribuibili in modo indipendente**. Questi approcci si sovrappongono e continuano a coesistere.
- **Client–server e multi-tier** (p. 3): il *client–server* separa chi richiede da chi fornisce; nei sistemi *multi-tier* presentazione, elaborazione applicativa e gestione dei dati possono girare in tier separati. **Il problema dell'integrazione:** applicazioni di vendite, contabilità e logistica possono usare modelli dati e tecnologie diversi ed essere sviluppate separatamente. **La domanda successiva:** come far condividere a questi sistemi, sviluppati indipendentemente, le capacità di business senza esporne gli interni?
- **Oggetti distribuiti e componenti** (p. 4): middleware degli anni '90 — **CORBA, DCOM, Java RMI** — permettevano interazioni remote tra oggetti o componenti. Interfacce esplicite: il middleware gestiva localizzazione degli oggetti remoti, codifica dei parametri e restituzione dei risultati. **Sfide:** ecosistemi middleware diversi potevano richiedere bridge o adattatori; chiamate remote a grana fine potevano aggiungere latenza e accoppiamento. L'orientamento ai servizi ha messo l'accento su **capacità di business e contratti di interazione espliciti** attraverso i confini di applicazione e proprietà.
- **Perché la SOA si è affermata** (p. 5): **integrazione aziendale** (connettere applicazioni esistenti e nuove, anche di proprietari diversi); **contratti di servizio** (le capacità sono esposte tramite interfacce e messaggi concordati mentre le implementazioni restano incapsulate). **Tappe degli anni 2000:** nota W3C su SOAP 1.1 (2000), W3C Web Services Architecture (2004), OASIS SOA Reference Model (2006). Web service, wrapper ed ESB hanno supportato la realizzazione di SOA, ma **la SOA non richiede una tecnologia specifica**.
- **SOA e microservizi nel tempo** (p. 6): i microservizi **mantengono l'idea** di esporre capacità di business tramite contratti espliciti nascondendo i dettagli di implementazione; l'enfasi successiva è su **confini di business coesi, deployment indipendente e proprietà decentralizzata dei dati**. Riferimento: l'articolo di Lewis e Fowler (2014) che ha documentato le caratteristiche dell'approccio emergente. **Scelta architetturale:** un sistema può combinare un progetto interno a strati o modulare con integrazione basata su servizi; sono gli obiettivi di qualità a determinare quali confini sono utili. La necessità di deployment indipendente può favorire la separazione in servizi; interazioni frequenti e requisiti di bassa latenza possono favorire il tenere insieme responsabilità correlate.
- **Decisioni guidate dalla qualità** (p. 7): *scenario di qualità* (stimolo, ambiente, risposta attesa, misura); *tattica* (un meccanismo che può influire sulla risposta richiesta); *scelta architetturale* (confini, interazioni, proprietà dei dati); *trade-off* (dichiarare il costo e le evidenze necessarie per giustificare la scelta).

### 1. Servizi e SOA

#### Che cos'è un servizio · [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=8|p. 8]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=12|12]]

- Sommario (p. 8): contratti di servizio e interoperabilità; riuso e integrazione di sistemi esistenti; esempio ricorrente **Food To Go (FTGO)**.
- Un **servizio** è un componente software **autonomo** che offre capacità utili, di business o tecniche. La sua interfaccia pubblica definisce come i client le richiedono. Può girare separatamente e interagire con i client tramite **contratti espliciti**. Il confine di un servizio dovrebbe **nascondere i dettagli di implementazione** (p. 9).
- **Il contratto di servizio** (p. 10): specifica operazioni o messaggi, ingressi, uscite ed errori possibili; descrive anche la **semantica** (cosa promette il servizio e cosa devono fornire i client); le aspettative di qualità possono includere tempo di risposta, disponibilità e carico supportato. Conoscere l'interfaccia non richiede di conoscere l'implementazione.
- **Principi di progetto** (p. 11): **accoppiamento debole** (i client dipendono da un contratto limitato ed esplicito); **astrazione** (i dettagli restano dietro l'interfaccia); **autonomia** (il servizio controlla le proprie responsabilità e risorse); **componibilità e riuso** (i servizi partecipano ad applicazioni più grandi).
- **Stato e autonomia** (p. 12): un servizio può possedere dati di business persistenti ed esporre comunque un'interazione **stateless**. Le richieste stateless portano con sé il contesto necessario a elaborarle, comprese le informazioni di autenticazione; sessioni client memorizzate localmente possono vincolare instradamento e recupero. L'**autonomia del servizio** richiede dipendenze controllate e chiara proprietà.

#### Architettura orientata ai servizi · [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=13|p. 13]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=17|17]]

- La **SOA** organizza capacità distribuite come servizi con contratti espliciti. Interfacce standard supportano la comunicazione tra tecnologie e organizzazioni diverse. I **provider** espongono le capacità, i **consumer** le usano, la **discovery** può aiutare a trovarle. SOAP, REST e un ESB sono **scelte di implementazione** dentro questo approccio più ampio (p. 13).
- **FTGO: Food To Go** (esempio, p. 14): i consumatori ordinano cibo tramite sito web o app mobile; i ristoranti mantengono i menu e gestiscono gli ordini; i corrieri ritirano e consegnano i pasti; FTGO coordina queste attività e integra provider di pagamento, messaggistica ed e-mail.
- **SOA e microservizi** (p. 15): la SOA enfatizza l'esposizione e l'integrazione di capacità tramite contratti di servizio; i microservizi enfatizzano **confini di servizio coesi e deployment indipendente**. Entrambi possono usare orchestrazione, coreografia e protocolli di comunicazione diversi. **SOAP, REST o un ESB da soli non bastano a stabilire la distinzione architetturale.**
- **Integrare sistemi legacy** (p. 16): un **wrapper** espone funzionalità esistenti tramite un'interfaccia di servizio; i client usano un contratto stabile mentre l'implementazione legacy resta dietro; supporta integrazione o modernizzazione graduali; il wrapper richiede comunque gestione degli errori, sicurezza e monitoraggio. Riferimento: Canfora, Fasolino, Frattolillo, Tramontana, *A Wrapping Approach for Migrating Legacy System Interactive Functionalities to Service Oriented Architectures*, Journal of Systems and Software 81 (2008), 463–480.

![[lez10-soa-p16-wrapper-legacy.png]]
*Una richiesta di web service entra in un Application Server, dove un Wrapper racchiude il sistema Legacy; la risposta torna come messaggio di web service.*

- **Uno scenario di interoperabilità** (p. 17): *stimolo (illustrativo):* FTGO cambia provider di pagamento durante la manutenzione. *Risposta richiesta:* sostituire l'adapter del provider mantenendo il contratto verso l'applicazione. *Misura (illustrativa):* nessuna modifica alle regole degli ordini né alle applicazioni client. *Tattiche rilevanti:* **incapsulamento** e uso di un **intermediario**. Validare anche la semantica degli errori, non solo i formati dei dati.

### 2. Comunicazione e contratti

#### Comandi, query ed eventi · [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=18|p. 18]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=19|19]]

- Sommario: comandi, query ed eventi; interazioni sincrone e asincrone; API HTTP, SOAP e OpenAPI.
- Un **comando** richiede un'azione: `createOrder`. Una **query** recupera informazioni: `findOrderById`. Un **evento** riporta un fatto: `OrderCreated`. I contratti definiscono sia le operazioni richiesta/risposta sia gli eventi pubblicati.

![[lez10-soa-p19-comandi-query-eventi.png]]
*Il client dell'Order Service invoca l'API di servizio, che definisce operazioni (commands: `createOrder()`, queries: `findOrderById()`); l'Order Service pubblica eventi (OrderCreated, OrderCancelled) quando i dati cambiano e i sottoscrittori li ricevono.*

#### Comunicazione sincrona e asincrona · [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=20|p. 20]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=21|21]]

- **Sincrona** (p. 20): il chiamante invia una richiesta e attende la risposta entro un limite di tempo; è facile da seguire quando serve una risposta immediata. Lunghe catene di chiamate sincrone aumentano il tempo di risposta e possono **propagare i guasti** tra servizi. I **timeout** limitano l'attesa, ma un timeout lascia **incerto l'esito** se il server può aver completato l'operazione: non garantisce che il server abbia smesso di elaborare né che l'operazione sia fallita.
- **Asincrona** (p. 21): un produttore invia un messaggio per un'elaborazione successiva (tramite coda o broker). Il **buffering** può assorbire picchi di carico temporanei o indisponibilità dei consumer. Il mittente ha bisogno di un contratto che distingua **accettazione del messaggio** da **completamento dell'operazione** e definisca come si segnalano o gestiscono i fallimenti. Ritardi di consegna, ordinamento ed elaborazione duplicata richiedono decisioni esplicite.

#### API HTTP e specifica · [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=22|p. 22]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=28|28]]

- **Una API HTTP** (p. 22): un'API definisce come i client software interagiscono con una capacità; un'API HTTP espone le interazioni tramite **URI, metodi, header e rappresentazioni**. I client possono restare indipendenti da archiviazione e dettagli interni; l'API richiede un contratto stabile e una politica di controllo degli accessi.
- **Specifica di un'API** (p. 23): descrive il contratto tra servizio e client: operazioni disponibili e loro significato, struttura di richieste e risposte, ingressi richiesti, errori possibili, requisiti di autenticazione. **OpenAPI** fornisce un formato standard, leggibile dalle macchine, per descrivere il contratto di un'API HTTP.
- **Esempio: creare un ordine** (p. 24): operazione `POST /orders`; ingresso richiesto: un identificativo di ristorante e una lista non vuota di articoli, ciascuno con identificativo e quantità positiva; risposta di successo: **201 Created**, con identificativo dell'ordine, stato iniziale e header `Location`; errori: **400** per ingresso non valido, **401** per credenziali mancanti o non valide, **403** per permessi insufficienti; autenticazione: la richiesta deve includere un **Bearer token**.
- **Risorse e metodi HTTP** (p. 25): `GET /orders/{id}` recupera una rappresentazione dell'ordine; `POST /orders` richiede la creazione; `PUT /orders/{id}` sostituisce lo stato della risorsa indirizzata (`PATCH` può esprimere aggiornamenti parziali); `DELETE /orders/{id}` richiede la rimozione secondo le regole di business dell'API. Rappresentazione JSON di una risorsa:

```json
{ "id": 123, "restaurantId": 42, "status": "PENDING" }
```

- **Risposte ed errori** (p. 26): **200 OK** risposta riuscita con la rappresentazione attesa; **201 Created** creazione riuscita (con `Location`); **400 Bad Request** e **404 Not Found** distinguono richieste non valide da risorse mancanti; **409 Conflict** può rappresentare un conflitto di stato. I corpi degli errori devono spiegare il problema in modo coerente.
- **Richieste stateless** (p. 27): ogni richiesta contiene il contesto necessario all'interazione; il server può comunque memorizzare ordini, anagrafiche clienti e altro stato delle risorse; un **token** può portare il contesto di autenticazione senza una sessione memorizzata in una singola istanza applicativa; l'interazione stateless può semplificare l'instradamento tra repliche. Le dipendenze condivise dai dati richiedono comunque meccanismi di recupero.
- **Stile architetturale REST** (p. 28): *Representational State Transfer*, stile per sistemi ipermediali distribuiti, molto usato per progettare web API. I client interagiscono con **risorse identificate da URI** e scambiano **rappresentazioni** del loro stato (per esempio documenti JSON). REST definisce **vincoli**: separazione client–server, interazioni stateless, caching, interfaccia uniforme e sistema a strati (tramite proxy, gateway); il *code on demand* è opzionale. L'interfaccia uniforme comprende messaggi autodescrittivi e ipermedia che guidano le azioni disponibili. **Usare solo HTTP e JSON non rende un'API RESTful.**

#### Web service SOAP e OpenAPI · [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=29|p. 29]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=32|32]]

- **Web service basati su SOAP** (p. 29): SOAP definisce un framework di messaggistica XML, spesso trasportato su HTTP; **WSDL** descrive l'interfaccia del servizio e il suo binding; le specifiche **WS-\*** affrontano sicurezza e messaggistica affidabile. Queste tecnologie possono supportare l'integrazione aziendale quando contratti e infrastruttura si adattano al contesto.
- **Struttura di WSDL** (p. 30): **types e messages** descrivono i dati scambiati; le **operations** definiscono l'interfaccia astratta; i **binding** collegano le operazioni a formati di messaggio e protocolli; gli **endpoint** identificano dove si raggiunge il servizio.

![[lez10-soa-p30-struttura-wsdl.png]]
*Documento WSDL commentato: `types` (tipi di dati definiti con XML Schema), `message` (messaggi definiti con parametri basati sui tipi), `portType` (operazioni definite su messaggi in/out — astratto), `binding` (meccanismi di binding — concreto), `service` (localizzazione del servizio).*

- **Descrizioni OpenAPI** (p. 31): descrivono percorsi, operazioni, parametri e risposte di un'API HTTP; gli **schemi** definiscono la struttura delle rappresentazioni; le descrizioni possono usare **YAML o JSON**; gli strumenti possono rendere la documentazione e generare codice client o scheletri server.
- **Un'operazione OpenAPI** (p. 32):

```yaml
openapi: 3.1.0
info: {title: FTGO API, version: '1.0'}
paths:
  /orders/{id}:
    get:
      parameters:
        - {name: id, in: path, required: true, schema: {type: integer}}
      responses:
        '200':
          description: Order found
        '404':
          description: Order not found
```

#### Evoluzione del contratto di un'API · [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=33|p. 33]]

- **Cambiamenti compatibili:** client e provider possono aggiornarsi in modo indipendente (per esempio aggiungere un campo di risposta opzionale se i client esistenti ignorano i campi sconosciuti).
- **Cambiamenti incompatibili (breaking):** richiedere un nuovo campo di ingresso, cambiare tipo o significato di un campo, restituire 200 invece di 404 possono rompere i client.
- **Versioning e migrazione:** per i cambiamenti incompatibili definire un percorso di migrazione, un periodo di supporto della vecchia versione e una data di ritiro.
- **Contract test:** verificano interazioni concordate (per esempio 404 per un ordine mancante); mantengono allineate specifica, implementazione e aspettative dei consumer.

### 3. Intermediari e coordinamento

#### Responsabilità degli intermediari · [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=34|p. 34]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=38|38]]

- Sommario: routing e service discovery; gateway e integrazione aziendale; orchestrazione e coreografia.
- **Responsabilità degli intermediari** (p. 35): il **routing** sceglie dove vanno una richiesta o un messaggio; la **trasformazione** adatta una rappresentazione o formato di messaggio; un **gateway** applica politiche selezionate di accesso e traffico; la **discovery** risolve gli endpoint disponibili dei servizi. Queste responsabilità possono stare in componenti diversi.
- **Broker forwarding** (p. 36): il client invia la richiesta al broker; il broker inoltra la richiesta e rilancia la risposta; l'intermediazione può centralizzare routing e controlli di policy; **ogni interazione ha un hop in più e dipende dal broker.**
- **Broker handle** (p. 37): il broker restituisce un **handle** (endpoint) del servizio; il client comunica poi direttamente con il provider; riduce l'intermediazione nelle chiamate successive; i client devono gestire cambi di endpoint, informazioni obsolete e guasti del provider.
- **Service discovery** (p. 38): un **registry** registra servizi ed endpoint; la discovery cerca un'istanza o una capacità; la selezione può considerare disponibilità e politica di routing; registrazione, informazioni di salute e aggiornamento degli endpoint richiedono supporto operativo.

![[lez10-soa-p36-broker-forwarding.png]]
![[lez10-soa-p37-broker-handle.png]]
![[lez10-soa-p38-service-discovery.png]]
*I tre schemi di intermediazione: forwarding (richiesta e risposta passano dal broker: serviceRequest, forwardedRequest, serviceReply, forwardedReply); handle (il broker risponde con un serviceHandle e il requester chiama direttamente il servizio); discovery (queryServices → serviceList → select aService → service handle → serviceRequestWithHandle → serviceReply).*

#### API gateway ed Enterprise Service Bus · [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=39|p. 39]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=42|42]]

- **API gateway** (p. 39): dà ai client un punto d'ingresso alle API di servizi selezionati; può applicare **autenticazione, rate limit, logging e routing**; può **aggregare risposte** se le esigenze dei client lo giustificano. I servizi mantengono la proprietà delle regole di business e dei dati; il gateway gestisce accesso, routing e, quando serve, l'aggregazione.
- **Enterprise Service Bus** (p. 40): fornisce **mediazione** tra sistemi aziendali eterogenei; responsabilità tipiche: routing, trasformazione, bridging di protocolli; supporta l'integrazione con applicazioni e servizi esistenti. La SOA può usare anche altre strutture di integrazione: l'ESB è una realizzazione.
- **API gateway vs ESB** (p. 41): *API Gateway* — punto d'ingresso controllato per le API di servizio verso i client (autenticazione, rate limiting, routing, aggregazione delle risposte). *ESB* — integra applicazioni e servizi eterogenei (trasformazione dei messaggi, bridging di protocolli, collegamenti a sistemi legacy). **Esempio FTGO:** il gateway instrada una richiesta d'ordine a Orders; un ESB potrebbe adattare messaggi contabili per un sistema legacy che richiede un formato o protocollo diverso. **Sovrapposizione e coesistenza:** entrambi possono instradare, proteggere e trasformare messaggi; il gateway si concentra sull'accesso alle API, l'ESB sull'integrazione tra sistemi; possono coesistere.
- **I costi della mediazione** (p. 42): un intermediario condiviso crea una dipendenza che richiede pianificazione di capacità e recupero; le trasformazioni centralizzate nell'ESB possono semplificare i client, ma l'ESB può accumulare logica di integrazione e diventare più complesso; i cambiamenti alle politiche applicate dall'intermediario possono riguardare più client e servizi; il progetto deve bilanciare interoperabilità con latenza, autonomia e complessità operativa.

#### Orchestrazione e coreografia · [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=43|p. 43]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=47|47]]

- **Orchestrazione** (p. 43): un **coordinatore** controlla il flusso di lavoro e chiama i servizi partecipanti. Il coordinatore può essere un servizio di orchestrazione dedicato, un componente dentro un servizio applicativo o un **workflow engine** che esegue una definizione di processo. Il suo stato registra l'avanzamento e il prossimo passo. Il controllo centrale rende più facile **trovare le decisioni** di workflow; il coordinatore richiede logica di recupero e gestione esplicita dei guasti dei partecipanti.
- **Coreografia** (p. 44): i partecipanti **reagiscono a eventi o messaggi** secondo le proprie regole; nessun componente deve emettere ogni passo; il coordinamento si distribuisce nei contratti dei partecipanti. **Tracciare l'intero processo di business** e cambiare le dipendenze tra eventi può diventare più difficile.
- **Coordinamento nello shopping online** (p. 45): l'esempio separa i **coordinatori** dai **servizi di capacità**; il progetto di interazione dettagliato specifica quali passi richiedono risposte, callback o recupero.

![[lez10-soa-p45-coordinamento-shopping-online.png]]
*Sistema OnlineShoppingSystem: interazioni utente (Customer Interaction, Supplier Interaction); coordinatori (Customer Coordinator, Supplier Coordinator, Billing Coordinator); servizi di capacità (Email, CreditCard, CustomerAccount, Catalog, DeliveryOrder, Inventory).*

- **Scegliere il tipo di coordinamento** (p. 46): l'accettazione di un ordine FTGO richiede un esito definito quando un ristorante rifiuta l'ordine. Un **orchestratore** può registrare lo stato pendente e scegliere l'azione di recupero; una **collaborazione a eventi** può distribuire quelle reazioni tra i servizi. La scelta deve tenere conto di **visibilità dell'avanzamento, recupero dei guasti e accoppiamento**.

![[lez10-soa-p47-ftgo-rifiuto-ristorante.png]]
*«FTGO: handling a restaurant rejection» (ordine in attesa, pagamento già autorizzato). Orchestrazione: il Restaurant service invia la risposta di rifiuto all'Order orchestrator, che registra l'avanzamento e coordina il recupero: Payment service rilascia l'autorizzazione, Order service segna l'ordine REJECTED. Coreografia di eventi: il Restaurant service pubblica `RestaurantRejectedOrder` su un Event broker, che consegna l'evento a Payment service (rilascia l'autorizzazione) e Order service (segna l'ordine REJECTED); i servizi reagiscono in modo indipendente. Trade-off di progetto: visibilità dell'avanzamento, recupero dei guasti, accoppiamento.*

*Approfondimenti nel wiki: [[microservices]], [[publish-subscribe]], [[client-server]]*
