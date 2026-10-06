---
tipo: concetto
importanza_esame: alta
prerequisiti: ["progettazione-basata-sul-riuso"]
fonti_pdf: ["04-Architectural Patterns.pdf#page=10", "04-Architectural Patterns.pdf#page=11", "04-Architectural Patterns.pdf#page=12", "04-Architectural Patterns.pdf#page=13", "04-Architectural Patterns.pdf#page=14", "04-Architectural Patterns.pdf#page=15", "04-Architectural Patterns.pdf#page=16", "04-Architectural Patterns.pdf#page=17"]
termine_inglese: "Domain-Specific Software Architecture (DSSA), reference architecture"
---

# DSSA — Domain-Specific Software Architecture (architetture di riferimento)

## Definizione

> 📄 Fonte: [[04-Architectural Patterns.pdf#page=10]]

> 🔑 Definizione chiave: una **DSSA** è un'architettura software **raccomandata per i sistemi di uno specifico dominio**; si chiama anche **architettura di riferimento** (*reference architecture*).

Esempi di domini: compilatori per linguaggi di programmazione; elettronica di consumo, avionica; sistemi di e-commerce/negozi web; videogiochi…

Una DSSA è un insieme di componenti software:
- **specializzati** per un tipo particolare di compito (dentro un dominio);
- **generalizzati**, così da poter essere usati efficacemente nel dominio;
- **composti in una struttura standardizzata** (**topologia**) efficace per costruire architetture di successo.

🧩 «Specializzati» e «generalizzati» non si contraddicono: un componente è specializzato rispetto al software in generale (fa una cosa tipica del dominio, es. il decoder video in una TV) e generalizzato rispetto ai singoli prodotti (serve a tutti i modelli di TV, non a uno solo).

## Vantaggi e limiti

> 📄 Fonte: [[04-Architectural Patterns.pdf#page=13]], [[04-Architectural Patterns.pdf#page=14]]

| | |
|---|---|
| **Vantaggio** | le DSSA **massimizzano il riuso** della conoscenza e degli sviluppi precedenti quando si creano nuove architetture |
| **Limite** | si possono usare **solo per costruire nuove applicazioni nello stesso dominio** |

Le architetture di riferimento forniscono **strutture, punti di vista (*viewpoints*), responsabilità e interfacce riusabili** per una **famiglia di sistemi** in un dominio. Vanno però **specializzate** secondo i requisiti del sistema e gli **scenari degli attributi di qualità** ([[04-Architectural Patterns.pdf#page=14]] → [[scenari-di-qualita]]).

## Esempi di architetture di riferimento

> 📄 Fonte: [[04-Architectural Patterns.pdf#page=14]]

| Dominio | Architettura di riferimento |
|---|---|
| Automotive | **AUTOSAR** → [[autosar]] |
| IoT | **ISO/IEC 30141** |
| Industria 4.0 | **RAMI 4.0** |
| Industrial IoT | **IIRA** |
| Smart Grid | **SGAM** |
| Cloud computing | **NIST Cloud Computing Reference Architecture** |
| Telecomunicazioni | **TM Forum ODA** |
| Sanità | **openEHR** |

## Esempi espansi

### Architettura di riferimento per applicazioni web (Microsoft)

> 📄 Fonte: [[04-Architectural Patterns.pdf#page=11]]

![[lez04-ap-p11-architettura-riferimento-web-microsoft.png]]
*Figura di [[04-Architectural Patterns.pdf#page=11]], dalla *Microsoft Application Architecture Guide*. **Client**: Browser. **Server**, a strati: *Presentation Layer* (User Interface, UI Process Logic); *Business Layer* (Application Facade, opzionale; Business Workflow, Business Logic, Business Entities); *Data Layer* (Data Access, Helpers and Utilities, Service Agents). Una colonna **Cross-Cutting** attraversa tutti gli strati: Security, Operational Management, Communication. Sotto: **Data Sources** e **Other systems**.*

🧩 È la stessa architettura citata nella presentazione del corso come «Web-Application Ms reference Architecture», associata a manutenibilità, scalabilità, sicurezza e prestazioni ([[00_IntroduzioneAlCorso_SAD.pdf#page=9]] → [[architettura-software]]). Combina lo stile [[layered]] (tre strati logici) con una distribuzione client/server su tier diversi ([[architetture-multi-tier]]).

### Architettura di riferimento per una piattaforma TV

> 📄 Fonte: [[04-Architectural Patterns.pdf#page=12]]

![[lez04-ap-p12-architettura-riferimento-tv.png]]
*Figura di [[04-Architectural Patterns.pdf#page=12]]: diagramma a componenti di una `CTvPlatform`. Componenti: `CFrontEnd` (cfre), `CBackEnd` (cbke), `CTunerDriver` (ctun), `CHipDriver` (chip), `CHopDriver` (chop), più un componente `m` di inizializzazione. Interfacce fornite e richieste con nomi come `IProgram`, `IPicture`, `ITuner`, `IIf`, `IColor`, `IScreen`, `IInit`, `II2c` (bus I²C, con versioni *fast* e *slow*).*

🧩 Il dettaglio dei nomi conta poco: la figura mostra che una DSSA è una **topologia standardizzata di componenti con interfacce fissate**, su cui ogni modello di TV monta le proprie implementazioni (driver diversi per hardware diverso).

### AUTOSAR

> 📄 Fonte: [[04-Architectural Patterns.pdf#page=15]]

![[lez04-ap-p15-autosar.png]]
*Figura di [[04-Architectural Patterns.pdf#page=15]], «AUTOSAR: piattaforme e architetture software standardizzate per i sistemi elettronici automotive». Dall'alto: **Application Layer** (componenti software); **AUTOSAR Runtime Environment (RTE)**; **Basic Software**, a sua volta a strati — Services (System Services, Memory Services, Communication Services), ECU Abstraction (Onboard Device Abstraction, Memory/Communication/I/O Hardware Abstraction), Microcontroller Abstraction (Microcontroller, Memory, Communication, I/O Drivers), più Complex Drivers; alla base il **Microcontroller** (risorse dell'ECU).*

Dettagli e collegamento con i sistemi aperti → [[autosar]].

### Architettura di riferimento IoT

> 📄 Fonte: [[04-Architectural Patterns.pdf#page=16]]

![[lez04-ap-p16-architettura-riferimento-iot.png]]
*Figura di [[04-Architectural Patterns.pdf#page=16]]. **A sinistra** (modello di riferimento per domini, 🧩 quello di ISO/IEC 30141): User Domain (UD) in alto; al centro Operations & Management Domain (OMD), Application & Service Domain (ASD), Access & Communication Domain (ACD); sotto Sensing & Controlling Domain (SCD) e Physical Entity Domain (PED); frecce bidirezionali tra domini adiacenti. **A destra** (vista a strati): Web/Portal, Dashboard, API Management; Event Processing and Analytics; Aggregation/Bus Layer (ESB e Message Broker); Communications (MQTT/HTTP); dispositivi; colonne trasversali Devices Manager e Identity & Access Management.*

### Modello di riferimento del cloud computing (NIST)

> 📄 Fonte: [[04-Architectural Patterns.pdf#page=17]]

![[lez04-ap-p17-cloud-computing-reference-model.png]]
*Figura di [[04-Architectural Patterns.pdf#page=17]], «Figure 1: The Conceptual Reference Model». Attori: **Cloud Consumer**, **Cloud Auditor** (Security Audit, Privacy Impact Audit, Performance Audit), **Cloud Provider** (Service Orchestration con Service Layer SaaS/PaaS/IaaS, Resource Abstraction and Control Layer, Physical Resource Layer con hardware e facility; Cloud Service Management con Business Support, Provisioning/Configuration, Portability/Interoperability; Security e Privacy trasversali), **Cloud Broker** (Service Intermediation, Aggregation, Arbitrage), **Cloud Carrier** alla base.*

## Perché importa

È la terza alternativa di progetto della lezione — la soluzione specifica del dominio, con il riuso maggiore ([[progettazione-basata-sul-riuso]]). Il programma la cita nelle slide di presentazione (DSSA, [[00_IntroduzioneAlCorso_SAD.pdf#page=16]]); il programma ufficiale parla di riuso tramite pattern, stili e tattiche ([[Programma Syllabus]]).

> 🎯 Esame: definizione di DSSA/architettura di riferimento; specializzati + generalizzati + topologia standard; vantaggi e limiti; esempi (AUTOSAR, IoT, cloud); differenza con i pattern architetturali.

## Connessioni

- [[progettazione-basata-sul-riuso]]: DSSA tra le forme di riuso.
- [[linee-di-prodotto-software]]: una linea di prodotto ha una propria architettura di riferimento interna (*product-line architecture*).
- [[autosar]]: esempio dettagliato.
- [[pattern-architetturali]]: più pattern si combinano dentro una DSSA.

## Fonti

- [[approcci-riuso-progettazione-architettura]] — [[04-Architectural Patterns.pdf#page=10]]–[[04-Architectural Patterns.pdf#page=17]]

_Aggiornato: 2026-10-01 — ingest 04-Architectural Patterns.pdf_
