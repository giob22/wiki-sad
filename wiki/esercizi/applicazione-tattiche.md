---
tipo: esercizio
argomento: "scegliere e applicare tattiche architetturali a un sistema"
difficoltà: media
---

# Applicazione di tattiche architetturali

## Metodo

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=21]]–[[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=30]] (schema ricorrente nelle slide: tattica → dove → effetto → trade-off)

1. Parti dallo **scenario** (o dal requisito) che non è soddisfatto.
2. Individua la **vista** su cui agire: C&C/deployment per prestazioni, disponibilità, sicurezza; moduli per modificabilità.
3. Scegli la **tattica** dal catalogo dell'attributo ([[tattiche-architetturali]]).
4. Scrivi **dove** si applica nel sistema (quale elemento si aggiunge o si modifica).
5. Scrivi l'**effetto** atteso sulla misura della risposta.
6. Scrivi il **trade-off**: quale altro attributo peggiora e cosa bisogna gestire in più.
7. Ridisegna la vista con la tattica applicata.

## Concetti usati

[[tattiche-architetturali]] · [[scenari-di-qualita]] · [[strutture-componenti-e-connettori]] · [[strutture-di-allocazione]] · [[strutture-di-modulo]]

## Casi svolti

Tutti sull'[[exam-booking-system]]. Le tabelle «dove / effetto / trade-off» sono delle slide; la colonna «scenario» e i commenti 🧩 sono miei.

### Caso 1 — Prestazioni al picco delle iscrizioni

**Traccia:** scenario di [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=14]]; tattiche di [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=23]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=24]].

| Tattica | Dove | Effetto | Trade-off |
|---|---|---|---|
| Replicate resources | più application server + load balancer | più richieste servite insieme | sessioni, sincronizzazione, concorrenza sui dati |
| Introduce a cache | cache del calendario esami | meno latenza, meno carico sul DB | dati non aggiornati |
| Asynchronous tasks | Booking → Message Queue → Notification | meno tempo di risposta percepito | notifiche in ritardo, messaggi persi o duplicati |

> 🧩 Ragionamento: con $\lambda \approx 83$ richieste/s e un DB da 30 transazioni/s ([[valutazione-attributi-di-qualita]]) la sola replicazione non soddisfa lo scenario. La cache toglie dal DB le **letture** del calendario; l'asincronia toglie dal percorso sincrono l'**invio della conferma**. Resta la **scrittura** della prenotazione, che il DB deve comunque fare: se la capacità di scrittura non basta, servono altre tattiche sul DB (non trattate in questa lezione).

### Caso 2 — Disponibilità in caso di guasto di un application server

**Traccia:** [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=25]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=26]].

| Tattica | Dove | Effetto |
|---|---|---|
| Detecting failures | health check periodici del load balancer | il guasto viene rilevato |
| Redirecting requests | l'istanza guasta esce temporaneamente dal pool | il traffico va sulle istanze sane |
| Introducing redundancy | repliche di application server, DB (primario + standby), broker | nessun single point of failure sul percorso |

> 🧩 Collegamento con lo scenario generale di availability ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=13]]): stimolo = crash di un server; ambiente = funzionamento normale → degradato; risposta = rilevare il guasto e impedire che diventi un malfunzionamento; misura = percentuale di disponibilità, tempo di rilevazione (legato all'intervallo degli health check). La slide non dà numeri per questo scenario.

### Caso 3 — Sicurezza delle prenotazioni

**Traccia:** [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=27]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=28]].

| # | Tattica | Dove | Effetto | Trade-off |
|---|---|---|---|---|
| ① | Protect data in transit | TLS browser ↔ application server | confidenzialità e integrità | |
| ② | Authenticate users | delega all'identity provider dell'università | niente accesso anonimo | |
| ③ | Authorize operations | RBAC su ruolo, risorsa, operazione | ogni utente fa solo ciò che il ruolo permette | |
| ④ | Log relevant events | audit log protetto (chi, cosa, quando) | auditing, anomalie | log con dati personali da proteggere |
| ⑤ | Protect data in transit | TLS verso i sistemi esterni | come ① | |

> 🧩 Le domande di sicurezza della vista C&C ([[01-IntroductionOnSoftwareArchitecture.pdf#page=31]]) trovano qui risposta: «quali comunicazioni cifrare?» → ① e ⑤; «quale componente autentica lo studente?» → l'identity provider (②); «chi può accedere al database?» → solo operazioni permesse dall'RBAC (③).

### Caso 4 — Modificabilità e testabilità della verifica di ammissibilità

**Traccia:** [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=29]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=30]]; requisiti di [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=5]].

| Tattica | Dove | Effetto | Requisito servito (🧩) |
|---|---|---|---|
| Localize changes | regole in Eligibility Checking | cambiare i prerequisiti non tocca Booking | modificabilità |
| Hide information | dati studenti via Student Records | formato, provenienza, accesso nascosti | modificabilità |
| Use an intermediary | SIS Adapter | cambiare l'API del SIS tocca l'adapter | testabilità (adapter finto nei test), modificabilità |
| Defer binding | regole da configurazione a runtime | varianti senza ricompilare | modificabilità |

### Caso 5 — Dallo scenario di disponibilità alle decisioni architetturali

**Traccia:** [[02-Availability.pdf#page=21]]. La slide dà la tabella; per ogni riga indico le tattiche di [[tattiche-availability]] che la realizzano (🧩).

| Guasto | Rilevazione | Risposta | Misura | 🧩 Tattiche |
|---|---|---|---|---|
| application server non risponde | health check del load balancer | togliere l'istanza, reindirizzare | rilevazione ≤ 30 s; ripristino ≤ 60 s | ping/echo (detect); redundant spare (recover); active redundancy |
| University SIS non disponibile | timeout e probe falliti | retry limitato; fallire in modo sicuro; segnalare «ammissibilità non disponibile» | nessuna decisione di ammissibilità scorretta | exception detection; retry; exception handling; increase competence set; circuit breaker |
| DB primario guasto | replicazione e monitoraggio del cluster | promuovere lo standby; riconnettere le istanze | RTO ≤ 5 min; RPO ≤ 1 min | monitor; passive (warm) o active (hot) redundancy |

> 🧩 Ragionamento sulla terza riga: RPO ≤ 1 min significa che lo standby può essere indietro al massimo di un minuto rispetto al primario, quindi la replicazione deve aggiornarlo almeno una volta al minuto (warm spare con aggiornamenti frequenti, o hot spare); un **cold spare** non soddisfa né l'RTO né l'RPO ([[02-Availability.pdf#page=18]]).

**Domanda di discussione della slide** («quali single point of failure restano dopo aver replicato gli application server?»): risposta in [[availability]] § Dallo scenario alle decisioni.

### Caso 6 — Scegliere il momento di binding

**Traccia:** esempi di [[03-Modifiability.pdf#page=6]] e [[03-Modifiability.pdf#page=25]].

| Cambiamento richiesto | Chi lo fa | Tattica di binding | 🧩 Perché questa |
|---|---|---|---|
| connettore SIS dell'Università A o B | team, alla build | component replacement (Maven build profiles) | il connettore cambia solo tra installazioni diverse; basta una build per università |
| endpoint del SIS | amministratore, al deployment | configuration-time binding (variabile d'ambiente, Spring Boot) | cambia tra ambienti (test, produzione) senza ricompilare |
| numero massimo di prenotazioni | amministratore | resource files (`application.yml`) | evita il limite scritto nel codice di [[03-Modifiability.pdf#page=9]] |
| posizione del SIS | nessuno (automatico) | discovery (Spring Cloud DiscoveryClient) | indipendenza dalla posizione ([[03-Modifiability.pdf#page=14]]) |
| regola secondo il tipo d'esame | il sistema, per ogni richiesta | interpret parameters | la scelta dipende dai dati della richiesta |
| regole attive | amministratore, a runtime | shared repositories (tabella nel DB) | modificabili da un'interfaccia di gestione senza riavvio |
| politica di ammissibilità per università | sviluppatore (nuova classe) + configurazione | polymorphism (`EligibilityPolicy`) | nuove politiche senza toccare Booking |

> ⚖️ Trade-off (🧩, dai due tipi di costo di [[03-Modifiability.pdf#page=7]]): più tardi si fa il binding, più il meccanismo costa da costruire e testare; si sceglie il binding più tardivo che ripaga la frequenza attesa del cambiamento.

## Trappole

- Proporre una tattica **senza trade-off**: ogni tattica delle slide ne ha uno (o complessità aggiunta).
- Applicare la tattica **nel posto sbagliato**: replicare il livello applicativo quando il collo di bottiglia è il DB ([[01-IntroductionOnSoftwareArchitecture.pdf#page=41]]).
- Confondere **tattica** (una decisione, un attributo) e **pattern** (insieme di tattiche) → [[pattern-architetturali]].
- Dimenticare che l'asincronia richiede di gestire messaggi **persi o duplicati**.

_Aggiornato: 2026-09-26 — ingest lezione 1_
_Aggiornato: 2026-09-30 — casi 5 (availability, Lez. 2) e 6 (defer binding, Lez. 3)_
