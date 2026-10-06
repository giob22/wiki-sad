---
tipo: esercizio
argomento: "scrivere e analizzare scenari di qualità concreti"
difficoltà: bassa
---

# Scenari di qualità concreti

## Metodo

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=8]]–[[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=16]]

1. **Scegli la responsabilità** del sistema e l'**attributo** in gioco (requisiti funzionali e di qualità vanno insieme, per responsabilità — [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=4]]).
2. Parti dallo **scenario generale** dell'attributo, se c'è, e scegli un valore per ogni parte ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=13]]).
3. Compila le **sei parti** in tabella: sorgente, stimolo, ambiente, artefatto, risposta, misura.
4. Leggi la tabella in forma **Given** (ambiente, artefatto) — **When** (sorgente, stimolo) — **Then** (risposta, misura).
5. Controlla che la **misura** sia **verificabile**: numeri con unità, percentili, limiti di ambito.
6. Indica **su quale vista** si valuterà lo scenario (C&C per runtime, moduli per modificabilità — [[valutazione-attributi-di-qualita]]).

## Concetti usati

[[scenari-di-qualita]] · [[attributi-di-qualita]] · [[valutazione-attributi-di-qualita]]

## Casi svolti

### Caso 1 — Scenario di prestazioni all'apertura delle iscrizioni

**Traccia:** [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=14]] (Exam Booking: requisito di qualità che guida progetto e valutazione).

![[lez01b-qa-p14-scenario-performance.png]]
*Figura di [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=14]]: tabella delle sei parti; la misura della risposta è evidenziata in arancione. Nota: la misura rende il requisito testabile e sostiene la valutazione architetturale.*

| Parte | Valore | G/W/T |
|---|---|---|
| Sorgente | studenti | When |
| Stimolo | 5.000 richieste di prenotazione in un minuto | When |
| Ambiente | apertura delle iscrizioni all'esame | Given |
| Artefatto | sottosistema Booking | Given |
| Risposta | validare e registrare ogni prenotazione ammissibile | Then |
| Misura | **95 %** completate entro **2 s** e **tutte** entro **5 s** | Then |

**Svolgimento (🧩):**
- *Lettura:* dato il sottosistema Booking durante l'apertura delle iscrizioni, quando gli studenti inviano 5.000 richieste in un minuto, allora ogni prenotazione ammissibile è validata e registrata, il 95 % entro 2 s e tutte entro 5 s.
- *Perché la misura ha due soglie:* il 95° percentile vincola l'esperienza tipica; il massimo vincola i casi peggiori (nessuno studente aspetta più di 5 s).
- *Carico:* $\lambda = 5000/60\ \text{s} \approx 83.3$ richieste/s in media (derivazione completa e confronto con il DB in [[valutazione-attributi-di-qualita]]).
- *Vista di valutazione:* C&C, completata da deployment ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=15]]).

### Caso 2 — Scenario di modificabilità: nuova regola sui prerequisiti

**Traccia:** [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=16]].

![[lez01b-qa-p16-scenario-modifiability.png]]
*Figura di [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=16]]: tabella a tre colonne (elemento dello scenario, Given–When–Then, scenario concreto). Nota: lo scenario rende la modificabilità testabile vincolando sia lo sforzo richiesto sia l'ambito della modifica.*

| Parte | G/W/T | Valore |
|---|---|---|
| Sorgente | When | amministrazione universitaria |
| Stimolo | When | richiede una nuova regola sui prerequisiti |
| Ambiente | Given | sistema in sviluppo; test automatici esistenti |
| Artefatto | Given | modulo Eligibility Checking e la sua suite di test |
| Risposta | Then | gli sviluppatori implementano, testano e rilasciano la nuova regola |
| Misura | Then | entro **due giorni lavorativi**; modifiche **limitate** a Eligibility Checking, configurazione e test relativi |

**Svolgimento (🧩):**
- La risposta è svolta dagli **sviluppatori**, non dal sistema: è un attributo di sviluppo ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=10]]).
- La misura ha due componenti: **sforzo** (due giorni) e **ambito** (quali artefatti si toccano). La seconda è verificabile contando i file modificati (valutazione empirica, [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=19]]).
- L'ambiente «test automatici esistenti» è una **precondizione**: senza test, il vincolo dei due giorni includerebbe anche scriverli.
- *Vista di valutazione:* moduli, con analisi d'impatto → [[analisi-impatto-modifiche]].

### Caso 3 — Dai requisiti di una responsabilità agli scenari

**Traccia:** [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=5]] — requisiti della responsabilità «verificare se uno studente può prenotare un esame».

> 🧩 Elaborazione mia: la slide dà i requisiti in forma di frase. Riscrivo i due runtime come scenari, per mostrare cosa manca.

| Parte | Performance | Availability |
|---|---|---|
| Sorgente | studente (❓ non specificato nella slide) | ❓ non specificata (il SIS stesso, per un guasto interno?) |
| Stimolo | richiesta di verifica di ammissibilità | il SIS è **temporaneamente indisponibile** durante una richiesta |
| Ambiente | **carico normale** | ❓ funzionamento normale del sistema di prenotazione |
| Artefatto | Eligibility Checking (❓ implicito) | Eligibility Checking / accesso al SIS |
| Risposta | restituire l'esito | restituire una **risposta controllata** |
| Misura | entro **500 ms** | entro **2 s** |

Le celle ❓ sono parti che il requisito in frase lascia implicite: scriverlo come scenario obbliga a esplicitarle, e questo è uno dei motivi per cui si usano gli scenari.

### Caso 4 — Scenario di disponibilità: un application server smette di rispondere

**Traccia:** [[02-Availability.pdf#page=9]] (ripetuto a [[02-Availability.pdf#page=20]]).

| Parte | Valore | G/W/T |
|---|---|---|
| Sorgente | ❓ non esplicitata (🧩 guasto interno hardware o software) | When |
| Stimolo | un application server smette di rispondere | When |
| Ambiente | periodo di prenotazione | Given |
| Artefatto | application server del pool | Given |
| Risposta | il load balancer rileva il guasto, toglie l'istanza dal pool e reindirizza le nuove richieste | Then |
| Misura | rilevazione ≤ **30 s**; ripristino ≤ **60 s**; almeno il **99 %** delle richieste completate; **nessuna** prenotazione confermata persa | Then |

**Svolgimento (🧩):**
- La misura ha **quattro** componenti, ognuna verificabile: due tempi (rilevazione, ripristino), una percentuale (richieste completate) e un vincolo sui dati (nessuna prenotazione confermata persa).
- Il vincolo sui dati impone che la prenotazione confermata sia **già scritta nel database** (non solo nella memoria del server guasto) — è la tattica *transactions* di [[02-Availability.pdf#page=17]].
- Il 99 % (e non il 100 %) ammette che le richieste in corso sull'istanza guasta falliscano.
- Confronto con lo scenario della **server farm** di [[02-Availability.pdf#page=8]]: lì la misura è «nessun downtime» e la risposta include **informare l'operatore**; qui la notifica all'operatore non c'è. Lo schema accanto al testo della slide è quello della server farm (vedi [[availability]]).

### Caso 5 — Scenario di modificabilità: cambiare l'interfaccia utente

**Traccia:** [[03-Modifiability.pdf#page=17]].

| Parte | Valore | G/W/T |
|---|---|---|
| Sorgente | sviluppatore | When |
| Stimolo | vuole cambiare l'interfaccia utente | When |
| Ambiente | design time (la modifica è fatta al codice) | Given |
| Artefatto | interfaccia utente | Given |
| Risposta | la modifica è fatta (e testata) | Then |
| Misura | meno di **tre ore** per farla e testarla; **nessun effetto collaterale** | Then |

**Svolgimento (🧩):**
- «Nessun effetto collaterale» vincola l'**ambito** della modifica, come «modifiche limitate a Eligibility Checking» nel caso 2.
- L'annotazione a mano sulla slide («MVC permette di avere un'alta modificabilità della interfaccia», separando la vista dal modello) indica la soluzione architetturale: se la vista è separata dalla logica, cambiarla non tocca il resto, e la misura è raggiungibile.
- Valori dallo scenario generale di [[03-Modifiability.pdf#page=15]]–[[03-Modifiability.pdf#page=16]]: sorgente «developer», stimolo «modificare funzionalità», ambiente «design time», misura «effort, elapsed time, new defects introduced».

## Trappole

- **Misura non verificabile**: «il sistema deve essere veloce» non è uno scenario; servono numeri, unità, percentili.
- **Confondere sorgente e stimolo**: la sorgente è *chi* (studenti), lo stimolo è *cosa arriva* (5.000 richieste in un minuto).
- **Dimenticare l'ambiente**: lo stesso stimolo in ambiente normale o di picco dà scenari diversi.
- **Risposta del sistema vs degli sviluppatori**: per gli attributi di sviluppo chi risponde è il team ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=10]]).
- **Modificabilità misurata solo in tempo**: la slide vincola anche l'**ambito** della modifica.

_Aggiornato: 2026-09-26 — ingest lezione 1_
_Aggiornato: 2026-09-30 — casi 4 (availability, Lez. 2) e 5 (modifiability, Lez. 3)_
