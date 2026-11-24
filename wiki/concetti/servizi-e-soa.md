---
tipo: concetto
importanza_esame: alta
prerequisiti: ["stili-architetturali", "attributi-di-qualita"]
fonti_pdf: ["07— Service-Oriented and Microservice Architectures-1 part.pdf#page=8"]
termine_inglese: "service, service-oriented architecture (SOA)"
---

# Servizi e architettura orientata ai servizi (SOA)

## Definizione

> 🔑 Definizione chiave — 📄 Fonte: [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=9]], [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=13]]

Un **servizio** è un componente software **autonomo** che offre capacità utili, di business o tecniche; la sua interfaccia pubblica definisce come i client le richiedono; può girare separatamente e interagisce tramite **contratti espliciti**, nascondendo i dettagli di implementazione. La **SOA** organizza capacità distribuite come servizi con contratti espliciti: i *provider* le espongono, i *consumer* le usano, la *discovery* aiuta a trovarle; SOAP, REST e un ESB sono scelte di implementazione, non la definizione.

## Spiegazione

> 📄 Fonte: [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=3]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=7]], [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=10]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=12]]

**Prospettiva storica (pp. 2–7).**

| Epoca | Approccio | Idea |
|---|---|---|
| Sistemi aziendali precedenti | applicazioni centralizzate, client–server | accesso a funzioni e dati condivisi |
| Anni '90 | multi-tier, oggetti distribuiti (CORBA, DCOM, Java RMI) | cooperazione tra processi e macchine; interfacce esplicite, ma bridge tra middleware e chiamate a grana fine con latenza e accoppiamento |
| Anni 2000 | SOA, web service | integrazione con **contratti di servizio espliciti** e messaggi interoperabili (SOAP 1.1 nota W3C 2000, W3C WS Architecture 2004, OASIS SOA Reference Model 2006) |
| Anni 2010 | microservizi | capacità di business **distribuibili in modo indipendente** |

Gli approcci si sovrappongono e coesistono. Il **problema dell'integrazione** (p. 3): vendite, contabilità e logistica usano modelli dati e tecnologie diverse; la domanda è come condividere capacità di business senza esporre gli interni.

**Il contratto di servizio (p. 10)** specifica operazioni o messaggi, ingressi, uscite, errori possibili, e anche la **semantica** (cosa promette il servizio, cosa devono fornire i client); le aspettative di qualità possono includere tempo di risposta, disponibilità, carico supportato.

**Principi di progetto (p. 11):** *accoppiamento debole* (i client dipendono da un contratto limitato), *astrazione* (i dettagli restano dietro l'interfaccia), *autonomia* (il servizio controlla le proprie responsabilità e risorse), *componibilità e riuso*.

**Stato e autonomia (p. 12):** un servizio può possedere dati persistenti ed esporre comunque un'interazione **stateless** (la richiesta porta il contesto necessario, autenticazione inclusa); sessioni memorizzate localmente possono vincolare instradamento e recupero.

## Esempi espansi

> 📄 Fonte: [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=14]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=17]]

**FTGO (Food To Go)** è l'esempio ricorrente (p. 14): i consumatori ordinano da sito o app; i ristoranti mantengono menu e gestiscono gli ordini; i corrieri ritirano e consegnano; FTGO coordina e integra provider di pagamento, messaggistica ed e-mail.

**Wrapper per sistemi legacy (p. 16).** Un wrapper espone funzionalità esistenti con un'interfaccia di servizio: i client usano un contratto stabile e l'implementazione legacy resta dietro; permette integrazione o modernizzazione graduali; richiede comunque gestione degli errori, sicurezza e monitoraggio. Riferimento: Canfora, Fasolino, Frattolillo, Tramontana, *J. Systems and Software* 81 (2008).

![[lez10-soa-p16-wrapper-legacy.png]]
*Una richiesta di web service entra in un Application Server, dove un Wrapper racchiude il sistema Legacy; la risposta torna come messaggio di web service ([[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=16]]).*

**Scenario di interoperabilità (p. 17).**

| Parte | Valore (illustrativo, dalla slide) |
|---|---|
| Stimolo | FTGO cambia provider di pagamento durante la manutenzione |
| Risposta | sostituire l'adapter del provider mantenendo il contratto verso l'applicazione |
| Misura | nessuna modifica alle regole degli ordini né alle applicazioni client |
| Tattiche | incapsulamento, intermediario |
| Sorgente/ambiente/artefatto | non esplicitati dalla slide (la fonte dà stimolo, risposta e misura) |

La slide aggiunge: validare anche la **semantica degli errori**, non solo i formati dei dati.

**SOA vs microservizi (p. 15).** SOA: esporre e integrare capacità tramite contratti. Microservizi: **confini di servizio coesi e deployment indipendente** (p. 6: anche proprietà decentralizzata dei dati; Lewis e Fowler 2014). Entrambi possono usare orchestrazione, coreografia e protocolli diversi; **SOAP, REST o un ESB da soli non bastano a distinguerli**. Scegliere i confini dipende dagli obiettivi di qualità: il deployment indipendente favorisce la separazione, interazioni frequenti e bassa latenza favoriscono il tenere insieme responsabilità correlate (p. 6).

## Perché importa

> ⚖️ Trade-off: la slide di p. 7 chiede di motivare le scelte con *scenario di qualità → tattica → scelta architetturale → trade-off* (dichiarando costo ed evidenze). È lo schema da usare per giustificare, all'orale, la scelta di servizi o microservizi nel progetto ([[progetto-di-corso]]).

## Connessioni

- [[microservices]], [[client-server]], [[architetture-multi-tier]]: l'evoluzione storica.
- [[contratti-e-api-di-servizio]], [[comunicazione-sincrona-e-asincrona]], [[intermediari-di-servizio]], [[orchestrazione-e-coreografia]]: le altre pagine della lezione.
- [[scenari-di-qualita]], [[tattiche-architetturali]]: lo scenario di interoperabilità.

## Fonti

- [[service-oriented-and-microservice-architectures]]; [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=2]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=17]]

_Aggiornato: 2026-11-24 — ingest 07— Service-Oriented and Microservice Architectures-1 part.pdf_
