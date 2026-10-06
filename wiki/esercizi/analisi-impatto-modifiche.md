---
tipo: esercizio
argomento: "analisi d'impatto delle modifiche sulla vista dei moduli"
difficoltà: bassa
---

# Analisi d'impatto delle modifiche

## Metodo

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=17]]

I sei passi della *change impact analysis* sulle viste dei moduli:
1. identificare lo **stimolo** di modifica;
2. identificare il **modulo responsabile**;
3. tracciare le **dipendenze** verso altri elementi (🧩 relazione *uses* in senso inverso: chi usa il modulo modificato può essere toccato se ne cambia l'interfaccia);
4. determinare gli **artefatti interessati**;
5. **stimare lo sforzo**;
6. valutare gli **effetti su test e deployment**.

## Concetti usati

[[strutture-di-modulo]] · [[valutazione-attributi-di-qualita]] · [[tattiche-architetturali]] (modificabilità) · [[scenari-di-qualita]]

## Casi svolti

### Caso 1 — Nuova regola sui prerequisiti nell'Exam Booking System

**Traccia:** stimolo dello scenario di [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=16]], vista dei moduli di [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=18]] (= [[01-IntroductionOnSoftwareArchitecture.pdf#page=14]]).

![[lez01-intro-p14-vista-moduli-exam-booking.png]]
*Vista dei moduli (relazione uses): Booking usa Authentication, Exam Catalog, Eligibility Checking, Notifications; Administration usa Exam Catalog.*

> 🧩 Svolgimento mio, passo per passo (la slide dà solo il metodo e la conclusione «dovrebbe interessare principalmente Eligibility Checking, non Booking»):

| Passo | Applicazione |
|---|---|
| 1. Stimolo | l'amministrazione richiede una nuova regola sui prerequisiti |
| 2. Modulo responsabile | **Eligibility Checking** (le regole di ammissione sono consolidate lì — *localize changes*, [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=30]]) |
| 3. Dipendenze | chi usa Eligibility Checking: **Booking**. Booking è toccato solo se cambia l'**interfaccia** di Eligibility Checking; aggiungere una regola cambia l'implementazione, non l'interfaccia (la domanda resta «lo studente è ammissibile?») ⇒ Booking non cambia. Se la regola richiede dati nuovi sullo studente, la dipendenza da seguire è verso Student Records ([[01-IntroductionOnSoftwareArchitecture.pdf#page=16]]) |
| 4. Artefatti | codice di Eligibility Checking (o solo la **configurazione** delle regole, se è applicato *defer binding*, [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=30]]); test di Eligibility Checking |
| 5. Sforzo | piccolo: un modulo e i suoi test — compatibile con i «due giorni lavorativi» dello scenario |
| 6. Test e deployment | si rieseguono i test di Eligibility Checking; si rilascia il componente che lo contiene, il **Booking Service** ([[01-IntroductionOnSoftwareArchitecture.pdf#page=28]]) |

**Risultato:** l'impatto è confinato a Eligibility Checking, configurazione e test: lo scenario di modificabilità è **soddisfatto a livello architetturale**. La verifica sul sistema reale si fa con l'esercizio di modifica ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=19]]).

**Controprova (🧩):** se le regole fossero sparse tra Booking ed Eligibility Checking, il passo 2 darebbe due moduli responsabili e il passo 6 due insiemi di test: sforzo e ambito crescerebbero e lo scenario («modifiche limitate a Eligibility Checking») non sarebbe soddisfatto.

### Caso 2 — Booking dipende direttamente da Notifications?

**Traccia:** domanda di [[01-IntroductionOnSoftwareArchitecture.pdf#page=15]].

> 🧩 Svolgimento mio: stimolo = cambia il modo di notificare (es. aggiungere notifiche push). Nella vista di p. 14 Booking **usa** Notifications: se cambia l'interfaccia di Notifications, Booking va modificato e ritestato. Nella vista di p. 16 Booking pubblica eventi su un **contratto** e Notifications lo consuma: il cambiamento resta in Notifications finché il contratto non cambia. La slide conclude che l'invocazione indiretta riduce l'accoppiamento e semplifica modificabilità e disponibilità, al prezzo di complessità.

## Trappole

- Seguire le frecce *uses* nel verso sbagliato: l'impatto si propaga da un modulo **verso chi lo usa**.
- Dimenticare **configurazione** e **test** tra gli artefatti.
- Confondere modulo e componente al passo 6: si rilascia il **componente** che contiene il modulo.

_Aggiornato: 2026-09-26 — ingest lezione 1_
