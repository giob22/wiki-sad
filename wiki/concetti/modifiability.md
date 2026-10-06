---
tipo: concetto
importanza_esame: alta
prerequisiti: ["attributi-di-qualita", "scenari-di-qualita", "strutture-di-modulo"]
fonti_pdf: ["03-Modifiability.pdf#page=3", "03-Modifiability.pdf#page=4", "03-Modifiability.pdf#page=5", "03-Modifiability.pdf#page=6", "03-Modifiability.pdf#page=7", "03-Modifiability.pdf#page=8", "03-Modifiability.pdf#page=9", "03-Modifiability.pdf#page=10", "03-Modifiability.pdf#page=11", "03-Modifiability.pdf#page=12", "03-Modifiability.pdf#page=13", "03-Modifiability.pdf#page=14", "03-Modifiability.pdf#page=15", "03-Modifiability.pdf#page=16", "03-Modifiability.pdf#page=17"]
termine_inglese: "modifiability"
---

# Modifiability (modificabilità)

## Definizione

> 📄 Fonte: [[03-Modifiability.pdf#page=3]]

> 🔑 Definizione chiave: la **modificabilità** (*modifiability*) riguarda il **cambiamento**; ci interessa per **ridurre il costo e il rischio** di fare modifiche.

Motivazione: **la maggior parte dei costi di un sistema software si ha dopo il rilascio**. I cambiamenti avvengono:
- per **aggiungere** nuove funzionalità, **modificare** o anche **ritirare** quelle vecchie;
- per **correggere difetti**, rafforzare la sicurezza o migliorare le prestazioni;
- per **migliorare** l'esperienza dell'utente;
- per **adottare** nuove tecnologie, piattaforme, protocolli, standard;
- per **far lavorare insieme** sistemi mai progettati per farlo.

È un attributo **non osservabile a runtime** ([[Programma Syllabus]]; nella Lez. 1 era tra gli attributi «di sviluppo», [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=6]]).

## Le quattro domande per pianificare la modificabilità

> 📄 Fonte: [[03-Modifiability.pdf#page=4]], [[03-Modifiability.pdf#page=5]]

| Domanda | Dettaglio |
|---|---|
| **Cosa** può cambiare? | funzioni del sistema, piattaforma, ambiente, qualità, capacità |
| Qual è la **probabilità** del cambiamento? | quali cambiamenti sono probabili, e quindi quali verranno supportati e quali no |
| **Quando** si fa il cambiamento e **chi** lo fa? | quando: nell'**implementazione** (modificando il codice sorgente), in **compilazione** (switch a tempo di compilazione), nella **build** (scelta delle librerie), nella **configurazione** (varie tecniche, tra cui l'impostazione di parametri), in **esecuzione** (parametri, plug-in, allocazione all'hardware…). Chi: uno **sviluppatore**, un **utente finale**, un **amministratore di sistema**, o il **sistema stesso** (capace di imparare ad adattarsi) |
| Qual è il **costo** del cambiamento? | vedi sotto |

![[lez03-mo-p4-quattro-domande.png]]
*Figura di [[03-Modifiability.pdf#page=4]]: le quattro domande in colonna, con le parole chiave evidenziate (what, likelihood, when/who, cost).*

> 🧩 Elaborazione mia: la domanda sulla **probabilità** è quella che rende la modificabilità un problema di progetto. Rendere tutto modificabile costa troppo; si investe solo sui cambiamenti probabili.

### Esempio — quando e chi, nell'Exam Booking System

> 📄 Fonte: [[03-Modifiability.pdf#page=6]]

![[lez03-mo-p6-quando-e-chi-modifica.png]]
*Figura di [[03-Modifiability.pdf#page=6]]: tabella a tre colonne (fase, cosa cambia, esempio).*

| Fase | Cosa cambia | Esempio | 🧩 Chi |
|---|---|---|---|
| Implementazione | codice sorgente | uno sviluppatore cambia la logica che verifica se lo studente può prenotare | sviluppatore |
| Compilazione | una scelta fissata alla compilazione | un'opzione a tempo di compilazione (uno switch) abilita una versione di una funzionalità; **cambiarla richiede di ricompilare** | sviluppatore |
| Build | i componenti inclusi nell'applicazione | il team sceglie quale libreria connettore per il SIS includere; **cambiarla richiede una nuova build** | team di sviluppo |
| Configurazione | valori impostati prima dell'avvio | un amministratore imposta l'endpoint del SIS o un limite di prenotazioni in un file di configurazione | amministratore |
| Esecuzione | valori o componenti cambiati mentre l'applicazione gira | un amministratore aggiorna una regola di prenotazione da un'interfaccia di gestione, oppure il sistema carica un plug-in supportato | amministratore o sistema |

🧩 Più la fase è tardiva, meno persone tecniche servono e meno lavoro richiede la modifica — ma più meccanismi vanno costruiti in anticipo. È l'idea delle tattiche *defer binding* ([[tattiche-modifiability]]).

## Il costo del cambiamento

> 📄 Fonte: [[03-Modifiability.pdf#page=7]], [[03-Modifiability.pdf#page=8]], [[03-Modifiability.pdf#page=9]]

Due tipi di costo ([[03-Modifiability.pdf#page=7]]):
1. il costo di **introdurre il meccanismo** (o i meccanismi) che rendono il sistema più modificabile;
2. il costo di **fare la modifica usando** quel meccanismo.

Se il codice viene modificato spesso e non si introduce nessun meccanismo architetturale, **accumulare modifica su modifica** porta di solito a un **debito tecnico** (*technical debt*) sostanziale.

![[lez03-mo-p7-costo-della-modifica.png]]
*Figura di [[03-Modifiability.pdf#page=7]]: tre riquadri blu — «Two types of cost are involved», il costo di introdurre il meccanismo, il costo di fare la modifica con il meccanismo — e in basso l'avvertenza sul debito tecnico.*

![[lez03-mo-p8-quando-si-paga-il-costo.png]]
*Figura di [[03-Modifiability.pdf#page=8]], «When is the cost of change paid?»: due linee temporali su tre momenti (sviluppo del sistema → il cambiamento avviene → sistema adattato). **No provision for the change** (esempio: il numero massimo di prenotazioni è scritto nel codice): costo iniziale 0; il costo si paga **quando arriva il cambiamento** (modificare il codice, testare, rilasciare); segue un nuovo deployment con il limite più alto. **Automatic adaptation** (esempio: Booking aggiunge istanze quando il traffico cresce): il costo si paga **in anticipo** (costruire e testare monitoraggio e scaling); al picco di traffico lo scaling è automatico, senza modifiche al codice — ma le risorse aggiuntive costano comunque. Nota: gli esempi riguardano cambiamenti diversi, una regola di business e la capacità di carico.*

Il testo della slide successiva ([[03-Modifiability.pdf#page=9]]) descrive i due estremi:

| | Nessuna predisposizione | Adattamento automatico |
|---|---|---|
| Costo iniziale | **zero** | alto: progettare, implementare e testare la capacità di adattamento **può essere costoso** |
| Costo al cambiamento | si paga **in quel momento**: modificare il codice sorgente e **rivalidare** il sistema | nessuna modifica manuale |
| Esempio | il numero massimo di prenotazioni è **scritto nel codice**: alzarlo richiede modifica, test e nuovo deployment | Booking rileva l'aumento di richieste e **regola automaticamente il numero di istanze**; il meccanismo di monitoraggio e scaling va però costruito e testato prima |

> 🧩 Elaborazione mia — quando conviene il meccanismo: se $C_m$ è il costo del meccanismo, $C_{senza}$ il costo di una modifica senza meccanismo, $C_{con}$ il costo con il meccanismo e $n$ il numero atteso di modifiche, il meccanismo conviene quando
> $$C_m + n \cdot C_{con} < n \cdot C_{senza} \iff n > \frac{C_m}{C_{senza} - C_{con}}$$
> Per questo contano le domande su **probabilità** e **frequenza** del cambiamento: un meccanismo costoso si ripaga solo se il cambiamento è frequente. La slide lo dice a parole (debito tecnico se il codice cambia spesso senza meccanismo); la formula è mia.

## Varianti specifiche della modificabilità

> 📄 Fonte: [[03-Modifiability.pdf#page=10]]–[[03-Modifiability.pdf#page=14]]

Oltre ai cambiamenti dei requisiti funzionali, un sistema può dover assorbire cambiamenti di **carico**, **varianti di prodotto**, **piattaforme di esecuzione** o **posizione dei servizi**.

![[lez03-mo-p10-varianti-modificabilita.png]]
*Figura di [[03-Modifiability.pdf#page=10]]: quattro riquadri — Scalability, Variability, Portability, Location Independence. **Annotazioni a mano sulla slide**: «a seconda del motivo per cui si modifica il software si distinguono diversi attributi per la modificabilità» e, con una freccia verso Variability, «ad esempio sistemi SAP possono essere modificati in base alle esigenze del cliente».*

| Variante | Definizione | Come si ottiene | Esempio Booking | Fonte |
|---|---|---|---|---|
| **Scalabilità** (*scalability*) | capacità di **assorbire un carico crescente aggiungendo risorse** | **orizzontale** (*scale out*): aggiungere istanze, es. un altro server nel cluster; **verticale** (*scale up*): aumentare le risorse di un'istanza, es. CPU o memoria. Nel cloud la capacità di aggiungere o togliere risorse secondo la domanda si chiama **elasticità** | Booking aggiunge istanze applicative per un'ondata di prenotazioni | [[03-Modifiability.pdf#page=11]] |
| **Variabilità** (*variability*) | capacità di produrre **varianti pianificate** di un sistema da software e artefatti condivisi | è centrale nelle **linee di prodotto** software: famiglie di prodotti con un nucleo comune che differiscono per alcune funzionalità | una linea di prodotto Booking offre un **nucleo comune di prenotazione**; ogni università sceglie le proprie regole di ammissibilità e opzioni di notifica | [[03-Modifiability.pdf#page=12]] |
| **Portabilità** (*portability*) | facilità di **adattare il software a una piattaforma diversa** | minimizzare le dipendenze dalla piattaforma o **isolarle dietro interfacce chiare**; scrivere il software per una **macchina virtuale** come la JVM riduce la dipendenza dal sistema operativo | Booking genera ricevute di prenotazione: con le API di file indipendenti dalla piattaforma di Java e un percorso di salvataggio configurabile passa da Linux a Windows senza cambiare la logica di prenotazione | [[03-Modifiability.pdf#page=13]] |
| **Indipendenza dalla posizione** (*location independence*) | componenti distribuiti comunicano **senza conoscere in anticipo l'indirizzo fisico** dell'altro | il client usa un **nome logico** del servizio e scopre l'indirizzo a runtime; il servizio può spostarsi con impatto minimo sui client. Serve un'**indirezione** tra identità logica e posizione fisica: **DNS**, **service discovery** o un intermediario come un **load balancer** | Booking chiama il SIS con un nome di servizio; se il SIS cambia server, il registry o il DNS risolvono il nuovo indirizzo e il codice di Booking non cambia | [[03-Modifiability.pdf#page=14]] |

> 💡 Connessione: la **scalabilità** qui è una variante della modificabilità (cambia il carico), mentre nella Lez. 1 «replicare le risorse» era una tattica di **prestazioni** ([[tattiche-architetturali]]): lo stesso meccanismo serve a più attributi. La **variabilità** riprende le **linee di prodotto** di [[importanza-architettura-software]] §3.8. La **portabilità** è l'attributo tipico dello stile [[layered]].

## Scenari di modificabilità

### Scenario generale

> 📄 Fonte: [[03-Modifiability.pdf#page=15]], [[03-Modifiability.pdf#page=16]]

![[lez03-mo-p15-scenario-generale-1.png]]
![[lez03-mo-p16-scenario-generale-2.png]]
*Figure di [[03-Modifiability.pdf#page=15]] e [[03-Modifiability.pdf#page=16]]: tabella dello scenario generale di modificabilità (parte, descrizione, valori possibili), dal libro di Bass, Clements, Kazman.*

| Parte | Descrizione | Valori possibili |
|---|---|---|
| Sorgente | l'agente che causa la modifica; di solito attori umani, ma il sistema può imparare o automodificarsi, e allora la sorgente è il sistema | utente finale, sviluppatore, amministratore di sistema, product line owner, il sistema stesso |
| Stimolo | la modifica che il sistema deve accogliere (anche correggere un difetto conta come modifica, a qualcosa che presumibilmente non funzionava) | una richiesta di aggiungere/cancellare/modificare funzionalità, o di cambiare un attributo di qualità, capacità, piattaforma o tecnologia; di aggiungere un prodotto a una linea di prodotto; di spostare un servizio in un'altra posizione |
| Artefatti | gli artefatti modificati: componenti o moduli specifici, la piattaforma, l'interfaccia utente, l'ambiente, o un altro sistema con cui interopera | codice, dati, interfacce, componenti, risorse, casi di test, configurazioni, documentazione |
| Ambiente | il momento o la fase in cui si fa la modifica | runtime, compile time, build time, initiation time, design time |
| Risposta | fare la modifica e incorporarla nel sistema | una o più tra: fare la modifica, testarla, rilasciarla, automodificarsi |
| Misura | le risorse spese per fare la modifica | costo in termini di: numero, dimensione, complessità degli artefatti toccati; sforzo; tempo trascorso; denaro (spesa diretta o costo opportunità); quanto la modifica influenza altre funzioni o attributi di qualità; nuovi difetti introdotti; quanto ci ha messo il sistema ad adattarsi |

🧩 L'**ambiente** qui è la **fase** del ciclo di vita (design, build, runtime…): corrisponde alla domanda «quando» di [[03-Modifiability.pdf#page=5]].

### Scenario concreto: modificare l'interfaccia utente

> 📄 Fonte: [[03-Modifiability.pdf#page=17]]

*«Uno sviluppatore vuole cambiare l'interfaccia utente. La modifica sarà fatta al codice in fase di progetto, richiederà meno di tre ore per farla e testarla, e non ci saranno effetti collaterali.»*

![[lez03-mo-p17-scenario-concreto-ui.png]]
*Figura di [[03-Modifiability.pdf#page=17]]: schema delle sei parti. **Annotazione a mano sulla slide**: «disaccoppia la vista del modello (logica architetturale)» — «MVC permette di avere un'alta modificabilità dell'interfaccia».*

| Sorgente | Stimolo | Artefatto | Ambiente | Risposta | Misura |
|---|---|---|---|---|---|
| sviluppatore | vuole cambiare l'interfaccia utente | interfaccia utente | design time | la modifica è fatta | < 3 ore per fare e testare la modifica; nessun effetto collaterale |

> 💡 Connessione: l'annotazione collega lo scenario al pattern **MVC** (in programma, [[Programma Syllabus]]): separando la vista dal modello, la modifica dell'interfaccia non tocca la logica e resta entro le 3 ore senza effetti collaterali. MVC non è ancora stato spiegato a lezione (TODO quando verrà trattato).

## Perché importa

La modificabilità è l'attributo su cui si ragiona con le [[strutture-di-modulo]], e l'unico dei due visti finora che riguarda il **costo dello sviluppo** e non il comportamento a runtime. Le sue varianti (scalabilità, variabilità, portabilità, indipendenza dalla posizione) ritornano negli stili architetturali e nei microservizi.

> 🎯 Esame: definizione e motivazione (costi dopo il rilascio); le quattro domande; quando/chi con esempi; i due tipi di costo e il debito tecnico; le quattro varianti con esempi; scenario generale e concreto.

## Connessioni

- [[tattiche-modifiability]]: come si ottiene.
- [[pattern-modifiability]]: pattern che la favoriscono.
- [[valutazione-attributi-di-qualita]]: analisi d'impatto ed esercizio di modifica (Lez. 1).
- [[scenari-di-qualita-concreti]]: casi svolti.

## Fonti

- [[quality-attributes-modifiability]] — [[03-Modifiability.pdf#page=3]]–[[03-Modifiability.pdf#page=17]]

_Aggiornato: 2026-09-30 — ingest 03-Modifiability.pdf_
