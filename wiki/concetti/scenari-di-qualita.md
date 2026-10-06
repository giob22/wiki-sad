---
tipo: concetto
importanza_esame: alta
prerequisiti: ["attributi-di-qualita"]
fonti_pdf: ["01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=8", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=9", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=10", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=11", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=12", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=13", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=14", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=16"]
termine_inglese: "quality attribute scenario"
---

# Scenari di qualità

## Definizione

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=8]] (slide 59)

Gli attributi di qualità **diventano osservabili attraverso gli scenari**:
- un attributo di qualità **non ha significato da solo**;
- diventa osservabile quando il sistema **risponde a un evento rilevante** in **condizioni specificate**;
- la risposta attesa deve essere **misurabile**.

Esempi della slide:
- la **sicurezza** si dimostra quando, di fronte a un tipo specifico di **attacco**, il sistema resiste senza perdere dati o funzionalità;
- la **modificabilità** si dimostra quando, di fronte a un tipo specifico di **richiesta di modifica**, lo sforzo per realizzarla resta entro limiti ragionevoli.

> 🔑 Definizione chiave: uno scenario di qualità ha **sei parti** ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=8]]) e si legge come ***Given** un ambiente e un artefatto interessato — **When** una sorgente genera uno stimolo — **Then** il sistema produce una risposta misurabile* ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=9]]).

![[lez01b-qa-p9-parti-scenario.png]]
*Figura di [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=9]] (slide 60): la mano che preme (① **Source**) invia lo ② **Stimulus** al riquadro ③ **Artifact**, che sta dentro il ④ **Environment**; dal riquadro esce la ⑤ **Response**, che arriva al quadrante del ⑥ **Response Measure** (un orologio/grafico).*

## Le sei parti

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=10]]–[[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=12]] (slide 61–63)

| # | Parte | Definizione | Note della slide |
|---|---|---|---|
| ① | **Sorgente dello stimolo** (*stimulus source*) | un'entità (persona, sistema informatico o altro attore) che ha generato lo stimolo | |
| ② | **Stimolo** (*stimulus*) | un evento che arriva al **sistema** o al **progetto** (evento, attacco, richiesta dell'utente…) | 🧩 «o al progetto»: per le qualità di sviluppo lo stimolo è es. una richiesta di modifica rivolta al team |
| ③ | **Artefatto** (*artifact*) | il **bersaglio** dello stimolo: il sistema o progetto stesso, un insieme di sistemi, l'intero sistema, o uno o più suoi pezzi | un guasto o una richiesta di modifica può toccare solo una piccola parte del sistema: un guasto nel *data store* si può trattare diversamente da uno nel *metadata store*; le modifiche all'interfaccia utente possono avere tempi di risposta più rapidi di quelle al middleware |
| ④ | **Ambiente** (*environment*) | l'insieme delle **circostanze** in cui avviene lo scenario | a sistema **in esecuzione**: stato normale o anomalo; a sistema **non in esecuzione**: in sviluppo, in test, durante l'aggiornamento dei dati, mentre ricarica la batteria tra un uso e l'altro |
| ⑤ | **Risposta** (*response*) | l'attività che avviene **come risultato** dell'arrivo dello stimolo | è ciò che l'architetto si impegna a soddisfare; consiste nelle responsabilità che il **sistema** (qualità runtime) o gli **sviluppatori** (qualità di sviluppo) devono svolgere in risposta |
| ⑥ | **Misura della risposta** (*response measure*) | serve a **misurare la risposta** e **testare lo scenario**, così da stabilire se l'architetto l'ha ottenuta | per le prestazioni: **latenza** o **throughput**; per la modificabilità: **lavoro o tempo** per fare, testare e rilasciare la modifica |

## Scenari generali e concreti

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=13]] (slide 64)

- Uno **scenario generale** è **indipendente dal sistema** e può riguardare qualunque sistema.
- Uno **scenario concreto** è **specifico** del sistema in esame.

🧩 Lo scenario generale è un modello con i valori possibili per ogni parte; lo scenario concreto sceglie un valore per ogni parte e mette numeri nella misura.

### Esempio — scenario generale di disponibilità

![[lez01b-qa-p13-scenario-generale-availability.png]]
*Figura di [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=13]]: lo schema delle sei parti con i valori possibili per l'availability.*

| Parte | Valori possibili ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=13]]) |
|---|---|
| Sorgente | interna/esterna: persone, hardware, software, infrastruttura fisica, ambiente fisico |
| Stimolo | **guasto** (*fault*): omissione, crash, tempistica errata, risposta errata |
| Artefatto | processori, canali di comunicazione, memoria, processi, artefatti interessati nell'ambiente del sistema |
| Ambiente | funzionamento normale, avvio, spegnimento, modalità di riparazione, funzionamento degradato, funzionamento in sovraccarico |
| Risposta | impedire che il guasto diventi un malfunzionamento (*failure*); rilevare il guasto; recuperare dal guasto |
| Misura | intervallo di tempo in cui il sistema deve essere disponibile; **percentuale di disponibilità**; tempo per rilevare il guasto |

🧩 La distinzione *fault* → *failure* è implicita nella risposta «prevent the fault from becoming a failure»: il guasto è la causa interna, il malfunzionamento è ciò che vede l'utente; le tattiche di disponibilità cercano di fermarsi al primo ([[tattiche-architetturali]]).

## Esempi espansi — scenari concreti dell'Exam Booking System

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=14]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=16]]

Gli scenari completi, con il ragionamento e il calcolo del carico, sono in [[scenari-di-qualita-concreti]]. In breve:

| Parte | Performance ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=14]]) | Modifiability ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=16]]) |
|---|---|---|
| Sorgente | studenti | amministrazione universitaria |
| Stimolo | 5.000 richieste di prenotazione in un minuto | richiesta di una nuova regola sui prerequisiti |
| Ambiente | apertura delle iscrizioni | sistema in sviluppo; test automatici esistenti |
| Artefatto | sottosistema Booking | modulo Eligibility Checking e i suoi test |
| Risposta | validare e registrare ogni prenotazione ammissibile | gli sviluppatori implementano, testano e rilasciano la regola |
| Misura | 95 % entro 2 s, tutte entro 5 s | entro due giorni lavorativi; modifiche limitate a Eligibility Checking, configurazione e test relativi |

Messaggi delle slide: la misura della risposta rende il requisito **testabile** e sostiene la **valutazione architetturale** ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=14]]); lo scenario di modificabilità la rende testabile vincolando **sia lo sforzo sia l'ambito** della modifica ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=16]]).

## Perché importa

È la risposta alla prima delle tre domande su architettura e qualità (come **esprimere** le qualità, [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=7]]). Uno scenario ben scritto è anche un **caso di test** per l'architettura. Nel progetto di corso, i requisiti di qualità fanno parte della prima iterazione (*architectural inception*, [[00_IntroduzioneAlCorso_SAD.pdf#page=24]]).

> 🎯 Esame: elencare e definire le sei parti; general vs concrete; scrivere uno scenario concreto con misura verificabile.

## Connessioni

- [[attributi-di-qualita]]: lo scenario è la forma operativa di un QA.
- [[valutazione-attributi-di-qualita]]: la misura della risposta è ciò che si valuta.
- [[scenari-di-qualita-concreti]]: esercizi svolti.
- [[attribute-driven-design]]: gli attributi di qualità sono tra i *driver* architetturali.

## Fonti

- [[attributi-di-qualita-e-importanza-architettura]] — [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=8]]–[[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=16]]

_Aggiornato: 2026-09-26 — ingest lezione 1_
