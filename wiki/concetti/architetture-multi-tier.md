---
tipo: concetto
importanza_esame: alta
prerequisiti: ["strutture-di-allocazione", "layered", "client-server"]
fonti_pdf: ["04-Architectural Patterns.pdf#page=24", "04-Architectural Patterns.pdf#page=26", "04-Architectural Patterns.pdf#page=27", "04-Architectural Patterns.pdf#page=28", "04-Architectural Patterns.pdf#page=29", "04-Architectural Patterns.pdf#page=30", "04-Architectural Patterns.pdf#page=31", "04-Architectural Patterns.pdf#page=32", "04-Architectural Patterns.pdf#page=33", "04-Architectural Patterns.pdf#page=34", "04-Architectural Patterns.pdf#page=35", "04-Architectural Patterns.pdf#page=36", "04-Architectural Patterns.pdf#page=37"]
termine_inglese: "multi-tier architecture"
---

# Architetture multi-tier

## Definizione

> 📄 Fonte: [[04-Architectural Patterns.pdf#page=24]]

> 🔑 Definizione chiave: un'**architettura multi-tier** divide il sistema in **unità che si possono installare ed eseguire separatamente**, chiamate **tier**. Ogni tier fornisce un **insieme correlato di servizi** e comunica con gli altri tier tramite **interfacce esplicite**.

I tier possono essere eseguiti:
- su **macchine diverse** o nodi virtuali;
- in **processi** o **container** diversi;
- attraverso **confini di rete o organizzativi**.

> ⚠️ **Non confondere tier e layer** ([[04-Architectural Patterns.pdf#page=24]]): i **layer** (strati) rappresentano una **decomposizione logica** delle responsabilità del software; i **tier** rappresentano la **distribuzione fisica o runtime** degli elementi software.

🧩 Nei termini della Lez. 1: i layer appartengono alle **strutture di modulo** ([[strutture-di-modulo]], layer structure), i tier alle **strutture di allocazione** ([[strutture-di-allocazione]], deployment). Si può avere 3 layer in 1 tier (il mainframe di p. 28) o 1 layer distribuito su più tier.

Il pattern [[state-logic-display]] (*three-tiered pattern*) è un tipo particolare di architettura multi-tier.

## Tipi di multi-tier

> 📄 Fonte: [[04-Architectural Patterns.pdf#page=26]], [[04-Architectural Patterns.pdf#page=27]]

Esempi tipici ([[04-Architectural Patterns.pdf#page=26]]):
- **two-tier**: client e server di database;
- **three-tier**: client, application server e server di database;
- **n-tier**: tier aggiuntivi per integrazione, messaggistica, caching o servizi esterni.

![[lez04-ap-p27-evoluzione-tier.png]]
*Figura di [[04-Architectural Patterns.pdf#page=27]], «From Centralised Deployment to Distributed Services»: le stesse responsabilità logiche — **Presentation**, **Application logic**, **Integration**, **Data** — si possono assegnare a un numero crescente di unità installabili in modo indipendente. **One tier** (sistema centralizzato): un'unica unità di deployment con tutte e quattro, nello stesso ambiente di esecuzione. **Two tiers** (fat client + server): fat client con presentazione, logica e integrazione → Data server. **Three tiers** (thin client + app + data): Client con la presentazione → Application server con logica e integrazione → Data server. **N services** (deployment indipendente): Client più Service A (logica + integrazione), B e C (logica + dati), collegati da API/messaging. Una freccia verticale indica distribuzione crescente e deployment indipendente. Nota: alternative illustrative, non un percorso evolutivo obbligato e non determinato dalla piattaforma di hosting.*

> 💡 Connessione: la riga «N services» è la struttura dei [[microservices]] (ogni servizio con i propri dati, collegati da API o messaggi).

## 1-tier

> 📄 Fonte: [[04-Architectural Patterns.pdf#page=28]], [[04-Architectural Patterns.pdf#page=29]]

- Presentazione, logica applicativa e gestione delle risorse sono installate ed eseguite su **un unico sistema centralizzato**.
- Utenti o programmi esterni accedono tramite **terminali «stupidi»** (*dumb terminals*) gestiti dal sistema informativo centrale.
- I terminali forniscono solo input e output; **calcolo e gestione dei dati** avvengono nel sistema centrale.
- Architettura tipica dei **mainframe** tradizionali.

**L'assenza di tier separati non implica l'assenza di modularità logica**: significa solo che tutti gli elementi software sono installati nello stesso ambiente di esecuzione.

![[lez04-ap-p28-one-tier.png]]
*Figura di [[04-Architectural Patterns.pdf#page=28]], «One-Tier Architecture»: due terminali utente inviano input/output (nessuna elaborazione applicativa sul terminale) a un **Centralised Information System** con tre strati — Presentation (interazione utente e gestione dello schermo), Application Logic (regole di business ed elaborazione), Resource Management (dati, file, dispositivi, risorse condivise). Riquadro: **1 tier fisico, 3 strati logici** — stessa macchina, stesso ambiente di esecuzione.*

| Attributo | Benefici potenziali | Limiti potenziali |
|---|---|---|
| Prestazioni | la comunicazione locale tra componenti evita l'overhead di rete | il sistema centrale può diventare un **collo di bottiglia** di calcolo e I/O |
| Disponibilità | meno componenti distribuiti e collegamenti semplificano la gestione dei guasti | il sistema centrale può essere un **single point of failure** |
| Scalabilità | le risorse centralizzate si possono potenziare **verticalmente** | scalare **orizzontalmente** o scalare funzioni in modo indipendente è difficile |
| Sicurezza | dati e controllo degli accessi gestiti centralmente | un attacco riuscito al sistema centrale compromette tutto il sistema |
| Modificabilità | il deployment centralizzato può semplificare il rilascio | l'accoppiamento stretto aumenta l'impatto delle modifiche e impedisce deployment indipendenti |
| Deployability | un solo ambiente di esecuzione da gestire | anche piccole modifiche possono richiedere di rilasciare di nuovo l'intera applicazione |
| Testabilità | il sistema completo si testa in un solo ambiente | i componenti possono essere difficili da isolare e testare singolarmente |
| Interoperabilità | non serve integrazione tra tier distribuiti interni | integrarsi con sistemi esterni o moderni può richiedere adapter specializzati |

Fonte della tabella: [[04-Architectural Patterns.pdf#page=29]]

![[lez04-ap-p29-one-tier-attributi.png]]
*Figura di [[04-Architectural Patterns.pdf#page=29]]: la tabella originale (attributo di qualità, benefici, limiti), trascritta sopra.*

## 2-tier: client/server (fat client)

> 📄 Fonte: [[04-Architectural Patterns.pdf#page=30]], [[04-Architectural Patterns.pdf#page=31]], [[04-Architectural Patterns.pdf#page=32]]

- La **logica di presentazione** e **parte della logica applicativa** si spostano dal sistema centrale al client (**fat client**).
- Il client **invoca direttamente** i servizi di un server di risorse o di database.
- Client e server sono **unità di esecuzione separate**, eventualmente su macchine diverse.
- La loro interazione richiede una **API remota** o un **protocollo di comunicazione** esplicito.
- L'API definisce **operazioni, dati scambiati, errori e regole di interazione**.
- L'API stabilisce un **contratto esplicito** attraverso il confine client–server e **nasconde l'implementazione interna** del server.

![[lez04-ap-p31-two-tier.png]]
*Figura di [[04-Architectural Patterns.pdf#page=31]], «Two-Tier Client–Server Architecture»: un fat client esegue interfaccia utente e logica applicativa; il server gestisce le risorse condivise. **Client Tier (fat client)**: Presentation (UI e interazione) e Application Logic (regole di business ed elaborazione locale, installate su ogni client) — «aggiornato e installato su ogni client». **Server Tier (shared server)**: Resource Management (dati persistenti, transazioni e risorse condivise) e Database/files — «dati e risorse gestiti centralmente». Tra i due una **Remote API** (confine di rete, richieste ↔ risposte). Nota: due tier fisici, tre gruppi logici di responsabilità.*

| Attributo | Benefici | Limiti |
|---|---|---|
| Prestazioni | l'esecuzione locale di presentazione e logica dà un'interazione reattiva e riduce il carico del server | chiamate remote frequenti o accesso diretto al database possono creare colli di bottiglia di rete e database |
| Scalabilità | le risorse dei client contribuiscono alla capacità di elaborazione | un server o database condiviso può limitare la scalabilità al crescere dei client |
| Disponibilità | i client possono continuare alcune operazioni locali durante disconnessioni temporanee | il server condiviso resta un potenziale **single point of failure** |
| Modificabilità | la presentazione può evolvere indipendentemente dal server se l'API resta stabile | cambiare le regole di business può richiedere di **aggiornare ogni client** |
| Deployability | le modifiche lato server si rilasciano centralmente | installare, configurare e aggiornare molti fat client è costoso |
| Sicurezza | il server può centralizzare autenticazione e accesso alle risorse | il codice del client non è del tutto affidabile; l'accesso diretto al database aumenta la superficie d'attacco |
| Interoperabilità | un'API esplicita permette a tipi diversi di client di usare i servizi del server | i client possono dipendere fortemente da una specifica API, protocollo o schema del database |
| Manutenibilità | responsabilità divise tra client e server | la logica di business può essere duplicata o diventare incoerente tra versioni diverse dei client |

Fonte della tabella: [[04-Architectural Patterns.pdf#page=32]]

![[lez04-ap-p32-two-tier-attributi.png]]
*Figura di [[04-Architectural Patterns.pdf#page=32]]: la tabella originale (attributo di qualità, benefici, limiti), trascritta sopra.*

Collegamento con il pattern della Lez. 3 → [[client-server]].

## 3-tier

> 📄 Fonte: [[04-Architectural Patterns.pdf#page=33]], [[04-Architectural Patterns.pdf#page=34]]

- L'**interfaccia utente** gira su un desktop o una workstation e fornisce un'interfaccia grafica standard (**thin client**).
- La **logica di business** è formata da uno o più moduli su un **application server** o, in alcune configurazioni, su una workstation.
- Un **RDBMS**, su un server di database o mainframe, fornisce **memorizzazione dei dati, elaborazione delle query, gestione delle transazioni e controllo della concorrenza**.
- È una delle **specializzazioni più usate** del modello n-tier.

![[lez04-ap-p33-three-tier.png]]
*Figura di [[04-Architectural Patterns.pdf#page=33]], «Three-Tier Client–Server Architecture»: **Client Tier** (browser/app mobile — Presentation: mostra la UI, raccoglie l'input; thin client) → **HTTPS API** (confine fisico) → **Application Tier** (application server — Application Logic: regole di business e workflow, autenticazione e accesso ai dati; installato centralmente) → **SQL/JDBC** (confine fisico) → **Data Tier** (database server — persistenza e query, transazioni e concorrenza; dati condivisi). Note: i tre tier descrivono la distribuzione fisica/runtime; presentazione, logica e gestione dei dati sono responsabilità logiche assegnate a quei tier. **Ogni tier si può installare, scalare e proteggere in modo indipendente.***

| Attributo | Benefici | Limiti |
|---|---|---|
| Modificabilità | le modifiche si possono localizzare in uno strato | le modifiche si propagano se le interfacce tra strati sono instabili |
| Manutenibilità | la chiara separazione delle responsabilità semplifica la comprensione | troppi strati possono introdurre complessità inutile |
| Testabilità | gli strati si testano indipendentemente con mock o stub | le interazioni end-to-end richiedono comunque test di integrazione |
| Riusabilità | servizi di business e di persistenza possono servire interfacce diverse | i componenti possono restare legati a ipotesi specifiche dello strato |
| Sicurezza | i controlli di accesso si applicano a confini ben definiti | **aggirare gli strati** può eludere i controlli di sicurezza |
| Prestazioni | gli strati permettono ottimizzazioni come il caching | le richieste che attraversano più strati introducono overhead |
| Deployability | gli strati possono essere assegnati a tier di deployment diversi | gli strati logici non sono necessariamente installabili in modo indipendente |
| Scalabilità | i singoli tier si possono replicare quando gli strati sono installati separatamente | un tier dei dati condiviso può restare un **collo di bottiglia** |

Fonte della tabella: [[04-Architectural Patterns.pdf#page=34]]

![[lez04-ap-p34-three-tier-attributi.png]]
*Figura di [[04-Architectural Patterns.pdf#page=34]]: la tabella originale (attributo di qualità, benefici, limiti), trascritta sopra.*

> 💡 Connessione: la tabella del 3-tier ragiona sugli **strati** (layer) più che sui tier: molte righe coincidono con i benefici e trade-off del pattern [[layered]] della Lez. 3 (modifiche localizzate, overhead, layer bridging che aggira i controlli). Il limite «tier dei dati condiviso come collo di bottiglia» è la stessa conclusione della Lez. 1 sul database ([[01-IntroductionOnSoftwareArchitecture.pdf#page=41]]).

### Confronto sintetico

> 🧩 Elaborazione mia, riassumendo le tre tabelle (pp. 29, 32, 34):

| | 1-tier | 2-tier (fat client) | 3-tier (thin client) |
|---|---|---|---|
| Dove sta la logica di business | sistema centrale | su ogni client | application server |
| Single point of failure | il sistema centrale | il server condiviso | (non indicato nella tabella; il tier dei dati è il collo di bottiglia) |
| Costo di una modifica alla logica | ridistribuire tutto | aggiornare **ogni client** | aggiornare solo l'application server |
| Scalabilità | solo verticale | limitata dal server condiviso | replica dei singoli tier |

## Middleware nell'architettura three-tier (Lez. 5)

> 📄 Fonte: [[3-Architectural Patterns-complete.pdf#page=35]], [[3-Architectural Patterns-complete.pdf#page=36]]

- Il middleware è uno **strato infrastrutturale trasversale** (*cross-cutting*) che sostiene le **interazioni tra i diversi tier**.
- Verso i **sistemi esterni** può realizzare **adattamento, trasformazione dei dati, mediazione di protocollo e instradamento**.

> 🔑 Definizione chiave: l'**n-tier** definisce **come sono separate le responsabilità** dell'applicazione; il **middleware** fornisce i **meccanismi di comunicazione e integrazione** che servono a collegare i tier e i sistemi esterni ([[3-Architectural Patterns-complete.pdf#page=36]]).

![[lez05-ap-p35-middleware-three-tier.png]]
*Figura di [[3-Architectural Patterns-complete.pdf#page=35]]: Client/User → dentro la «Three-tier application»: **Presentation Tier** (interfaccia utente, pagine web, web controller) → **Communication Middleware** (chiamate remote, serializzazione, sicurezza) → **Business Tier** (logica applicativa, regole di business, servizi) → **Data and Integration Middleware** (adapter, mediazione di protocollo, trasformazione dei dati, routing) → **Data Tier** (database, repository, servizi di dati). Il middleware di integrazione è collegato anche agli **External and Legacy Systems** fuori dall'applicazione.*

> 🧩 Elaborazione mia: la figura mostra **due** middleware con ruoli diversi. Il primo serve la comunicazione **interna** tra tier (le chiamate remote che nascono quando gli strati diventano tier separati: serializzare i dati, proteggerli). Il secondo serve l'**integrazione** con dati e sistemi esterni (gli adapter). Il trade-off di p. 36 vale per entrambi: ogni middleware è un componente in più sul percorso della richiesta, quindi latenza e possibile single point of failure ([[availability]]).

## Middleware come abilitatore di integrazione

> 📄 Fonte: [[04-Architectural Patterns.pdf#page=35]]

Il middleware fornisce:
- un'**interfaccia comune** per accedere a sistemi diversi;
- **adapter e wrapper** che nascondono i dettagli specifici dei sistemi;
- **mediazione di protocollo** tra tecnologie diverse;
- **trasformazione dei dati** tra formati diversi;
- **instradamento e orchestrazione** delle richieste.

**Beneficio:** i client non devono conoscere l'architettura interna o la tecnologia dei sistemi integrati.
**Trade-off:** il middleware introduce **complessità aggiuntiva, latenza** e un potenziale **single point of failure**.

![[lez04-ap-p35-middleware.png]]
La stessa slide compare nel PDF completo a [[3-Architectural Patterns-complete.pdf#page=36]] con l'aggiunta della definizione chiave riportata sopra.

*Figura di [[04-Architectural Patterns.pdf#page=35]], «Middleware Integration Across Heterogeneous Architectures»: una Client Application (presentation layer) usa una **Unified API**; sotto, il **Middleware** (strato di integrazione comune) con Integration Logic (routing, trasformazione, orchestrazione, mediazione di protocollo) e Application Services (operazioni condivise e workflow di business); tre **Adapter/Wrapper** collegano il middleware a sistemi esistenti o esterni: un sistema one-tier (applicazione legacy/database), uno two-tier (applicazione client–server) e uno three-tier (client + applicazione + dati). Nota: il middleware nasconde l'eterogeneità dietro interfacce stabili e meccanismi di interazione comuni.*

> 💡 Connessione: adapter/wrapper e interfaccia comune sono le tattiche di modificabilità *use an intermediary*, *abstract common service* e *restrict dependencies* (wrapper) ([[tattiche-modifiability]]); il SIS Adapter dell'Exam Booking System è un caso piccolo dello stesso principio ([[tattiche-architetturali]]).

## Pattern di deployment

### 4-tier per applicazioni web

> 📄 Fonte: [[04-Architectural Patterns.pdf#page=36]]

![[lez04-ap-p36-four-tier-deployment.png]]
*Figura di [[04-Architectural Patterns.pdf#page=36]], «Figure 2.6 Four-tier deployment pattern» dalla *Microsoft Application Architecture Guide* (notazione UML): **Client Tier** (Client) → **Web Tier** (Web Server) → **Business Logic Tier** (App Server) → **Database Tier** (Database). Didascalia della slide: «per Web Applications».*

🧩 Rispetto al 3-tier, il server web (che serve pagine e gestisce HTTP) è separato dall'application server (logica di business), così i due si scalano e si proteggono separatamente.

### Load-Balanced Cluster

> 📄 Fonte: [[04-Architectural Patterns.pdf#page=37]]

Altro pattern di deployment, **per garantire le prestazioni**.

![[lez04-ap-p37-load-balanced-cluster.png]]
*Figura di [[04-Architectural Patterns.pdf#page=37]], «Figure 2.7 Load-Balanced Cluster deployment pattern for performance» dalla *Microsoft Application Architecture Guide* (UML): **Client Tier** (Client) → Firewall* → **Load Balancer** → **Application Tier** con istanze replicate Instance 1, 2, …, n di AppServer → Firewall* → **Data Tier** (Database Server). L'asterisco indica un elemento opzionale.*

> 💡 Connessione: è la configurazione scalabile dell'Exam Booking System ([[01-IntroductionOnSoftwareArchitecture.pdf#page=40]]) e la tattica *replicate resources* ([[tattiche-architetturali]]). Nella figura il load balancer e il database server sono in una sola copia: restano possibili single point of failure, come discusso in [[availability]].

## Perché importa

Collega i pattern alla **vista di allocazione**: decidere quanti tier usare e cosa mettere in ciascuno determina prestazioni, disponibilità, scalabilità, deployability e costo delle modifiche, come mostrano le tabelle. Il progetto di corso propone una web app client-server o a microservizi ([[progetto-di-corso]]): la scelta tra 3-tier, 4-tier e N servizi è una decisione architetturale da giustificare all'orale.

> 🎯 Esame: tier vs layer; 1-, 2-, 3-tier con benefici e limiti per attributo; fat vs thin client; ruolo e trade-off del middleware; pattern 4-tier e load-balanced cluster.

## Connessioni

- [[state-logic-display]]: il pattern three-tier.
- [[client-server]]: il 2-tier è il client-server della Lez. 3.
- [[layered]]: layer logici, distinti dai tier.
- [[strutture-di-allocazione]]: i tier sono una decisione di deployment.
- [[microservices]]: la riga «N services» della figura di p. 27.

## Fonti

- [[approcci-riuso-progettazione-architettura]] — [[04-Architectural Patterns.pdf#page=24]], [[04-Architectural Patterns.pdf#page=26]]–[[04-Architectural Patterns.pdf#page=37]]

_Aggiornato: 2026-10-01 — ingest 04-Architectural Patterns.pdf_
_Aggiornato: 2026-10-06 — middleware nel three-tier (3-Architectural Patterns-complete.pdf pp. 35–36)_
