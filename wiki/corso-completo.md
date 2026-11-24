# Software Architecture Design — corso completo

Testo unico di studio del corso (LM Ingegneria Informatica, UNINA, DIETI, prof.ssa Anna Rita Fasolino). Contiene **tutta e sola la teoria**, cioè solo ciò che sta nei PDF delle lezioni, nell'ordine delle slide: definizioni, elenchi, tabelle, esempi, diagrammi e codice. Non c'è la presentazione del corso (Lezione 0) né il progetto PICUS. Le spiegazioni estese, gli esempi espansi, i grafici aggiuntivi e gli esercizi stanno nelle pagine concetto ed esercizio, richiamate in fondo a ogni lezione («Approfondimenti nel wiki»).

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
