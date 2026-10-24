---
tipo: progetto-artefatto
stato: bozza per il team — testi pronti da incollare nelle issue, da rivedere insieme
data: 2026-10-24
sprint: "S1 — Preparazione PICUS (attività 4)"
fonte: "template epic.yml del repository Progetto-SAD; epic-da-lezione-progetto"
---

# Epic PICUS nel formato del template GitHub

Le sette epic di [[epic-da-lezione-progetto]], già **riconciliate con il diagramma dei casi d'uso della docente** ([[PICUS-casi-d-uso.pdf]]), scritte nei campi del modulo **«Epic»** del repository `Pinguini-alla-Fragola/Progetto-SAD`. L'analisi che ha portato a queste scelte (corrispondenze, lacune, cosa è stato fuso) è nella pagina [[epic-da-lezione-progetto]].

> 🧩 **Come usarla.** Per ogni epic: nuova issue → modulo **Epic** → titolo e campi come sotto. Il modulo del repository (versione allineata al template della docente, `.github/ISSUE_TEMPLATE/epic.yml` su `main`) ha sei campi: *Objective*, *Stakeholders and value*, *Scope*, *Out of scope* (facoltativo), *Epic completion criteria*, *Dependencies, risks and constraints*; nel modulo la prima riga raccomanda di **scomporre ogni epic in User Story collegate come sub-issue**. Il testo è in **inglese**, come il modulo e il formato delle story del corso (*As a… I want… so that…*, [[00-Presentazione Progetto Picus.pdf#page=22]]); se preferite l'italiano si traduce.
> Dati di esempio: **solo sintetici**, nessun dato identificativo degli assistiti.

Marcatori nei testi: **[Agreed]** = detto dal direttore, nei desiderata o nel diagramma della docente; **[Proposal]** = proposta del team da validare; **[Open]** = da chiarire. Così si distinguono fonte, accordi e proposte come richiede [[guida-progetto-picus]] § 6.7.

| ID | Titolo della issue | Casi d'uso della docente coperti |
|---|---|---|
| EP-01 | `[EPIC] Account, access and role management` | Assegna Credenziali alle OPT · Assegna Credenziali ad Operatori |
| EP-02 | `[EPIC] Measures catalogue and OPT offering` | Aggiornare Catalogo Misure · Comunicare Misure Offerte |
| EP-03 | `[EPIC] Measure requests and status tracking (OPT side)` | Richiesta Misura · Visualizzare Stato Richiesta |
| EP-04 | `[EPIC] Request handling and provider assignment (Banco side)` | Gestione Richieste da OPT |
| EP-05 | `[EPIC] Provider response and appointments` | Accettare Richiesta Ricevuta · frecce da «Gestione Richieste» verso Operatore Interno/Esterno e OPT |
| EP-06 | `[EPIC] Banco communications to OPTs` | Invio Comunicazioni |
| EP-07 | `[EPIC] Quarterly monitoring form` | Invio Scheda Monitoraggio |

---

## EP-01

**Title**
```text
[EPIC] Account, access and role management
```

**Objective**
```text
Let the Banco create, assign and revoke the access credentials of OPTs and operators, so that every user enters PICUS with the right role and sees only the information they are entitled to.
```

**Stakeholders and value**
```text
- Banco: decides who uses the system and manages hundreds of accounts (400–450 OPTs) without a developer. [Agreed]
- OPT: one account per OPT, a single and simple access point, also for small organisations with limited IT skills. [Agreed]
- Operators (internal to the Banco and external): a personal access for the activities that concern them. [Agreed]
- Assisted persons are stakeholders but NOT users: no account, no identifying data. [Agreed]
Value: controlled and traceable access; visibility limited by role and ownership (an OPT sees only its own data, the Banco has the overall view).
```

**Scope**
```text
- The Banco assigns credentials to OPTs, one by one or in bulk (e.g. a yearly CSV upload, optional). [Agreed]
- The Banco assigns credentials to operators. [Agreed for internal operators; Open for external ones]
- Initial credentials are delivered outside the system (e.g. e-mail). [Agreed]
- Sign-in with credentials; role-based and ownership-based visibility. [Agreed]
- The Banco revokes the access of an OPT that ceases; credentials do not expire. [Agreed]
- Credential recovery. [Open: required by the desiderata, not discussed]
```

**Out of scope**
```text
- Self-registration of users without the Banco's approval.
- Management of the OPT's own operators and volunteers (black box: the OPT uses its single account).
- Biometric authentication and document-based registration.
- Accounts for assisted persons.
```

**Epic completion criteria**
```text
- [ ] All required User Stories have been completed
- [ ] The Banco can create (single and bulk) and revoke OPT accounts, and create operator accounts
- [ ] A user can sign in and sees only the data allowed by their role (checked at the application boundary, not only by hiding buttons)
- [ ] Relevant quality scenarios (security, privacy) have been verified
```

**Dependencies, risks and constraints**
```text
- Which operators need an account is not settled: in the professor's use case diagram "Assegna Credenziali ad Operatori" targets only internal operators, but external operators also receive requests and submit the quarterly form (see EP-05, EP-07). [Open]
- Retention of data after revocation (privacy officer). [Open]
- Constraint: one e-mail per OPT (confirmed); no personal data of assisted persons anywhere.
- Related: EP-05, EP-07. Sources: lecture transcript (24/10), professor's use case diagram, desiderata §5.1, stakeholder notes (BA).
```

---

## EP-02

**Title**
```text
[EPIC] Measures catalogue and OPT offering
```

**Objective**
```text
Let the Banco publish and keep up to date the catalogue of accompaniment measures, and let each OPT declare which measures it offers, so that the Banco knows who can deliver what.
```

**Stakeholders and value**
```text
- Banco: updates the catalogue without a developer and identifies potential providers for a request. [Agreed]
- OPT: declares the measures it actually carries out and can then be asked to deliver them for other OPTs. [Agreed]
Value: a configurable catalogue (no hard-coded list of measures) and an up-to-date picture of the offering across the region.
```

**Scope**
```text
- The Banco publishes the catalogue (initial list of twelve measures) and modifies it over time. [Agreed]
- The OPT consults the catalogue and communicates the measures it offers; it can update them. [Agreed]
- The Banco sees which OPTs offer a given measure (used by EP-04). [Proposal]
```

**Out of scope**
```text
- Publishing the OPT's availability in the system: the director was explicit that availability is not managed; the Banco contacts OPTs individually.
- Counters or aggregate data about the OPT's regular activity (discussed in class and removed until confirmed). [Open]
- An information profile of the OPT (e.g. address). [Open: proposed in class, not confirmed]
```

**Epic completion criteria**
```text
- [ ] All required User Stories have been completed
- [ ] The Banco can change the catalogue without code changes
- [ ] An OPT can declare and update the measures it offers, and the Banco can see them
- [ ] The end-to-end flow "catalogue → offering → used in provider search" has been demonstrated
```

**Dependencies, risks and constraints**
```text
- Quantitative data from the OPTs: the desiderata (§5.2) foresee them, the lecture recalls that the director does not need them. To be asked. [Open]
- Use of the "Other" category and measures requiring a professional qualification. [Open]
- Related: EP-04. Sources: lecture transcript, professor's use case diagram, desiderata §5.2.
```

---

## EP-03

**Title**
```text
[EPIC] Measure requests and status tracking (OPT side)
```

**Objective**
```text
Let an OPT that cannot meet the need of an assisted person by itself ask the Banco for a measure, without identifying the person, and follow the status of its requests.
```

**Stakeholders and value**
```text
- OPT: one place to ask and to see what happens, instead of phone calls, messages and separate sheets. [Agreed]
- Banco: receives requests in order of arrival through a single, traceable channel. [Agreed]
- Assisted persons (indirectly): faster and more reliable answers; no identifying data enters the system.
Value: requests are traceable; OPTs never talk to each other directly.
```

**Scope**
```text
- The OPT creates a request for a measure of the catalogue, for one person or one household, with no identifying data. [Agreed]
- The OPT sees the status of its own requests (and only its own). [Proposal: reasonable, not requested]
- The OPT is notified of status changes (secondary). [Proposal]
```

**Out of scope**
```text
- Requests between OPTs; the OPT's internal search for an answer; the contact with the assisted person (handled outside the system).
- Prioritisation of requests: they are served in order of arrival.
```

**Epic completion criteria**
```text
- [ ] All required User Stories have been completed
- [ ] An OPT can submit a request and follow it until a final status
- [ ] No identifying data of assisted persons is requested, stored or logged
- [ ] Relevant quality scenarios (privacy, usability on smartphones) have been verified
```

**Dependencies, risks and constraints**
```text
- Minimum information of a request that does not identify the person; real (anonymised) examples needed. [Open]
- Request statuses and edge cases (suggested: In programming, Completed, Cancelled, Refused). [Open]
- One request = one meeting or a path of several meetings? [Open]
- Related: EP-04, EP-05. Sources: lecture transcript, professor's use case diagram, desiderata §5.3, stakeholder notes (BA).
```

---

## EP-04

**Title**
```text
[EPIC] Request handling and provider assignment (Banco side)
```

**Objective**
```text
Let the Banco receive the requests of the OPTs, find who can deliver the measure (internal operator, OPT or external professional) and assign it, keeping the whole process traceable.
```

**Stakeholders and value**
```text
- Banco: the core of its work; the final decision on the assignment is always taken by a Banco operator. [Agreed]
- OPTs and operators contacted as possible providers.
- Ministry (indirectly): the Banco must monitor the transactions OPT 1 → Banco → OPT 2. [Agreed]
Value: faster matching and full traceability, replacing phone calls and messages.
```

**Scope**
```text
- The Banco sees incoming requests in order of arrival and the pending ones. [Agreed]
- The Banco finds possible providers by measure, territory and availability, and contacts them. [Agreed]
- The Banco assigns the provider; if nobody answers or the provider refuses, the Banco reassigns. [Agreed]
- The Banco consults the history of a request. [Proposal]
- Optional improvements to validate with the director: the system suggests candidates ranked by proximity, load and competence; the Banco can send an availability request to a limited number of candidates (not a broadcast); nothing is confirmed until the Banco assigns; the other contacted providers are released, with availability held for a limited time (e.g. two hours). [Proposal]
```

**Out of scope**
```text
- Publishing availability in the system; direct contact between OPTs; broadcast of a request to all OPTs.
- Automatic assignment without a Banco decision.
- Prioritisation of requests.
```

**Epic completion criteria**
```text
- [ ] All required User Stories have been completed
- [ ] The end-to-end flow request → provider search → assignment has been demonstrated
- [ ] The Banco can see the status and history of every request
- [ ] Relevant quality scenarios (traceability, performance under quarterly peaks, availability) have been verified
```

**Dependencies, risks and constraints**
```text
- Search order: OPTs/external operators on the territory first and internal operators as fallback, or the opposite; it may depend on the measure (in person vs remote). [Open]
- One provider at a time or several in parallel? The director's wish to assign one OPT at a time conflicts with the parallel availability request. [Open]
- Response times: the director excluded timeouts and notifications (pending-requests section); the held availability is only a proposal. [Open]
- Criteria and meaning of "close". [Open]
- Related: EP-02, EP-03, EP-05. Sources: lecture transcript, professor's use case diagram ("Gestione Richieste da OPT"), desiderata §5.3, stakeholder notes (BA).
```

---

## EP-05

**Title**
```text
[EPIC] Provider response and appointments
```

**Objective**
```text
Let the providers (OPTs, internal operators, external operators) receive a request from the Banco, accept or refuse it and confirm the appointment, and let the Banco pass the details back to the requesting OPT.
```

**Stakeholders and value**
```text
- Providers (OPT, internal operator, external operator): receive requests and answer in one place. [Agreed for OPTs; Proposal for operators]
- Banco: knows who accepted and when, and which appointments are confirmed. [Agreed]
- Requesting OPT: receives the details of the appointment and communicates them to the assisted person. [Agreed]
Value: confirmed, traceable appointments without phone calls; reports that refer to real accepted services.
```

**Scope**
```text
- The provider receives a request addressed to it by the Banco. [Agreed]
- The provider accepts or refuses it (with a reason). [Proposal: raised in class, no use case yet]
- The operator confirms the appointment; in person: date, place, time and contact person; remote: date, time and link to the video call. [Agreed]
- The Banco informs the requesting OPT of the details. [Agreed]
- The Banco sees the confirmed appointments. [Proposal]
```

**Out of scope**
```text
- The video-call platform itself (the system handles only the link). [Proposal]
- How an OPT organises its own staff to deliver the measure (black box).
- Contact between the requesting OPT and the assisted person (outside the system).
```

**Epic completion criteria**
```text
- [ ] All required User Stories have been completed
- [ ] The end-to-end flow assignment → acceptance → confirmed appointment → information to the requesting OPT has been demonstrated
- [ ] Refusal and no-answer cases are handled and visible to the Banco
```

**Dependencies, risks and constraints**
```text
- The professor's use case diagram has "Accettare Richiesta Ricevuta" only for the OPT; internal and external operators are reached by "Gestione Richieste da OPT" but have no use case to accept, refuse or confirm. [Open]
- External operators need an account, but "Assegna Credenziali ad Operatori" targets internal operators only; how the Banco contacts an unregistered external operator. [Open]
- Who receives the appointment request: the OPT or the operator made available by the OPT. [Open]
- Remote visits (which measures, which platform) and the meaning of "contact person". [Open]
- Related: EP-01, EP-04. Sources: lecture transcript, professor's use case diagram, desiderata §5.3.
```

---

## EP-06

**Title**
```text
[EPIC] Banco communications to OPTs
```

**Objective**
```text
Let the Banco send communications to the OPTs and be sure that they have been received.
```

**Stakeholders and value**
```text
- Banco: reaches all OPTs or a subgroup with important news (e.g. convocations, notices, deadline reminders) and knows who received them. [Agreed]
- OPT: receives communications in one place and confirms receipt. [Agreed]
Value: no broadcast without evidence of delivery; reliable communication with about 400 recipients.
```

**Scope**
```text
- The Banco sends a communication, with attachments, to all OPTs or to a subgroup. [Agreed]
- The OPT reads it and confirms receipt. [Agreed]
- The Banco sees which OPTs have confirmed. [Agreed]
```

**Out of scope**
```text
- Plain broadcast without confirmation; communications to assisted persons.
- Communications to the OPT's own operators (the OPT acts as intermediary). [Open]
- Search and organisation of past communications unless justified.
```

**Epic completion criteria**
```text
- [ ] All required User Stories have been completed
- [ ] A communication with an attachment reaches a chosen subgroup and the confirmations are visible to the Banco
- [ ] Attachments respect the storage constraints of the project
```

**Dependencies, risks and constraints**
```text
- In the professor's use case diagram "Invio Comunicazioni" has no arrow towards the recipients: who receives communications, and the channel. [Open]
- Types of communication, allowed attachments (format, size), who reads the notification. [Open]
- Related: EP-01. Sources: lecture transcript, professor's use case diagram, desiderata §5.4, stakeholder notes (BA).
```

---

## EP-07

**Title**
```text
[EPIC] Quarterly monitoring form
```

**Objective**
```text
Let the operators submit the monitoring form of each quarter and let the Banco collect the forms for the reporting to the ministry.
```

**Stakeholders and value**
```text
- Operators (internal to the Banco and external): fill and submit the form directly to the Banco. [Agreed for internal operators; Agreed in the professor's diagram for external ones]
- Banco: collects the forms and uses them for reporting; today the data is entered manually in the ministry portal. [Agreed]
- Ministry and privacy officer: recipients of the reporting and responsible for retention rules.
Value: less manual work and fewer errors; forms contain personal and administrative data of operators and aggregated data on recipients, so they need adequate protection.
```

**Scope**
```text
- The operator fills the form of a quarter and submits it to the Banco. [Agreed]
- The Banco sees the received forms and who has not yet submitted. [Proposal]
- The Banco exports the data to help the manual entry in the ministry portal. [Proposal]
- Consistency checks on the form (rules to be defined). [Proposal]
```

**Out of scope**
```text
- Direct integration with the ministry portal (not requested).
- Forms of the OPT's own operators (not delivered to the Banco).
- Identifying data of assisted persons: only aggregated counts.
- Linking the form to a specific OPT, measure or request: the quarterly report is separate from the request flow.
```

**Epic completion criteria**
```text
- [ ] All required User Stories have been completed
- [ ] An operator can submit a quarterly form and the Banco can collect it
- [ ] The form data is accessible only to authorised roles
- [ ] Relevant quality scenarios (privacy, performance at the quarterly deadline) have been verified
```

**Dependencies, risks and constraints**
```text
- External operators submit the form according to the professor's diagram; the director's notes said the OPT's operators do not. Who enters the data when the activity is delivered by an OPT. [Open]
- Risk of duplicate reporting when an operator is associated with an OPT. [Open]
- Validation rules (overlapping categories must not be forced to sum to the total) and retention of the data. [Open]
- Related: EP-01. Sources: lecture transcript, professor's use case diagram ("Invio Scheda Monitoraggio"), desiderata §5.5 and Appendix B, stakeholder notes (BA).
```

---

## Dopo le epic

1. **Creare le sette issue** dal modulo Epic e assegnare i **tipi/etichette** come prevede il repository (le issue non sono state create da me).
2. **Scrivere le User Story** come sub-issue di ogni epic con il modulo *User Story* (campi: user story, contesto e valore, criteri di accettazione, dipendenze, epic padre, fonte e stato del requisito, *Definition of Ready*): partire dai «semi» di [[epic-da-lezione-progetto]], controllare INVEST ([[valutare-user-stories-invest]]).
3. **Portare i punti [Open]** all'Open Questions Log ([[domande-al-committente]]).

## Fonti

[[epic-da-lezione-progetto]] · [[PICUS-casi-d-uso.pdf]] · [[trascrizione-lezione-progetto-1]] · [[guida-progetto-picus]] § 4.5, 5.2 · [[incontro-stakeholder-ba]] · [[user-stories]]

_Aggiornato: 2026-10-24 — prima stesura nel formato del template_
