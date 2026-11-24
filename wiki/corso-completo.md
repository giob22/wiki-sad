# Software Architecture Design — corso completo

Testo unico di studio del corso (LM Ingegneria Informatica, UNINA, DIETI, prof.ssa Anna Rita Fasolino). Contiene **tutta e sola la teoria**, cioè solo ciò che sta nei PDF delle lezioni, nell'ordine delle slide: definizioni, elenchi, tabelle, esempi, diagrammi e codice. Non c'è la presentazione del corso (Lezione 0) né il progetto PICUS. Le spiegazioni estese, gli esempi espansi, i grafici aggiuntivi e gli esercizi stanno nelle pagine concetto ed esercizio, richiamate in fondo a ogni lezione («Approfondimenti nel wiki»).

**Come leggerlo.** Il riferimento al PDF compare solo nel titolo di ogni sezione (`p. N` apre la pagina). Il sito di studio si genera da questo file con `python output/crea_sito.py`; il controllo di integrità con `python output/controlla_corso.py`.

## Indice

| # | Lezione | PDF sorgente |
|---|---|---|
| 1 | [[#Lezione 1 — Introduzione all'architettura software\|Introduzione all'architettura software]] | 01-IntroductionOnSoftwareArchitecture.pdf, 01-IntroductionOnSoftwareArchitecture-2 parte.pdf |

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

## Strutture di modulo

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

## Strutture componenti-e-connettori (C&C)

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

## Strutture di allocazione

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
