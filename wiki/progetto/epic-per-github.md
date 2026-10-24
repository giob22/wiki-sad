---
tipo: progetto-artefatto
stato: bozza per il team — testi pronti da incollare nelle issue, da rivedere insieme
data: 2026-10-24
sprint: "S1 — Preparazione PICUS (attività 4)"
fonte: "template epic.yml del repository Progetto-SAD; epic-da-lezione-progetto"
---

# Epic PICUS nel formato del template GitHub

Le sette epic di [[epic-da-lezione-progetto]], già **riconciliate con il diagramma dei casi d'uso della docente** ([[PICUS-casi-d-uso.pdf]]), scritte nei campi del modulo **«Epic»** del repository `Pinguini-alla-Fragola/Progetto-SAD`. L'analisi che ha portato a queste scelte (corrispondenze, lacune, cosa è stato fuso) è nella pagina [[epic-da-lezione-progetto]].

> 🧩 **Come usarla.** Per ogni epic: nuova issue → modulo **Epic** → titolo e campi come sotto. Il modulo del repository (versione allineata al template della docente, `.github/ISSUE_TEMPLATE/epic.yml` su `main`) ha sei campi, con le etichette in inglese: *Objective* (obiettivo), *Stakeholders and value* (stakeholder e valore), *Scope* (perimetro), *Out of scope* (fuori perimetro, facoltativo), *Epic completion criteria* (criteri di completamento), *Dependencies, risks and constraints* (dipendenze, rischi e vincoli). Nel modulo la prima riga raccomanda di **scomporre ogni epic in User Story collegate come sub-issue**. I testi sotto sono **in italiano** (traduzione della prima stesura in inglese, ancora nella cronologia di Git); le etichette dei campi restano quelle del modulo.
> Dati di esempio: **solo sintetici**, nessun dato identificativo degli assistiti.

Marcatori nei testi: **[Concordato]** = detto dal direttore, nei desiderata o nel diagramma della docente; **[Proposta]** = proposta del team da validare; **[Aperto]** = da chiarire. Così si distinguono fonte, accordi e proposte come richiede [[guida-progetto-picus]] § 6.7.

| ID | Titolo della issue | Casi d'uso della docente coperti |
|---|---|---|
| EP-01 | `[EPIC] Gestione di account, accessi e ruoli` | Assegna Credenziali alle OPT · Assegna Credenziali ad Operatori |
| EP-02 | `[EPIC] Catalogo delle misure e offerta delle OPT` | Aggiornare Catalogo Misure · Comunicare Misure Offerte |
| EP-03 | `[EPIC] Richieste di misura e stato delle richieste (lato OPT)` | Richiesta Misura · Visualizzare Stato Richiesta |
| EP-04 | `[EPIC] Gestione delle richieste e assegnazione dell'erogatore (lato Banco)` | Gestione Richieste da OPT |
| EP-05 | `[EPIC] Risposta degli erogatori e appuntamenti` | Accettare Richiesta Ricevuta · frecce da «Gestione Richieste» verso Operatore Interno/Esterno e OPT |
| EP-06 | `[EPIC] Comunicazioni del Banco alle OPT` | Invio Comunicazioni |
| EP-07 | `[EPIC] Scheda di monitoraggio trimestrale` | Invio Scheda Monitoraggio |

---

## EP-01

**Title**
```text
[EPIC] Gestione di account, accessi e ruoli
```

**Objective**
```text
Permettere al Banco di creare, assegnare e revocare le credenziali di accesso di OPT e operatori, in modo che ogni utente entri in PICUS con il proprio ruolo e veda solo le informazioni che gli competono.
```

**Stakeholders and value**
```text
- Banco: decide chi usa il sistema e gestisce centinaia di account (400–450 OPT) senza l'aiuto di uno sviluppatore. [Concordato]
- OPT: un solo account per OPT, un unico punto di accesso semplice, anche per organizzazioni piccole con poche competenze informatiche. [Concordato]
- Operatori (interni al Banco ed esterni): un accesso personale per le attività che li riguardano. [Concordato]
- Le persone assistite sono stakeholder ma NON utenti: nessun account, nessun dato identificativo. [Concordato]
Valore: accessi controllati e tracciabili; visibilità limitata per ruolo e per proprietà (un'OPT vede solo i propri dati, il Banco ha la vista complessiva).
```

**Scope**
```text
- Il Banco assegna le credenziali alle OPT, una per una o in blocco (per esempio con un caricamento annuale da CSV, facoltativo). [Concordato]
- Il Banco assegna le credenziali agli operatori. [Concordato per gli operatori interni; Aperto per gli esterni]
- Le credenziali iniziali sono consegnate fuori dal sistema (per esempio via e-mail). [Concordato]
- Accesso con credenziali; visibilità per ruolo e per proprietà. [Concordato]
- Il Banco revoca l'accesso di un'OPT che cessa; le credenziali non scadono. [Concordato]
- Recupero delle credenziali. [Aperto: previsto dai desiderata, non discusso]
```

**Out of scope**
```text
- Auto-registrazione degli utenti senza l'approvazione del Banco.
- Gestione degli operatori e dei volontari propri dell'OPT (scatola nera: l'OPT usa il suo unico account).
- Autenticazione biometrica e registrazione con documenti.
- Account per le persone assistite.
```

**Epic completion criteria**
```text
- [ ] Tutte le User Story necessarie sono state completate
- [ ] Il Banco può creare (singolarmente e in blocco) e revocare gli account delle OPT e creare gli account degli operatori
- [ ] Un utente può accedere e vede solo i dati consentiti dal suo ruolo (controllo al confine dell'applicazione, non solo nascondendo i pulsanti)
- [ ] Sono stati verificati gli scenari di qualità pertinenti (sicurezza, privacy)
```

**Dependencies, risks and constraints**
```text
- Non è deciso quali operatori abbiano un account: nel diagramma dei casi d'uso della docente «Assegna Credenziali ad Operatori» raggiunge solo gli operatori interni, ma anche gli operatori esterni ricevono richieste e inviano la scheda trimestrale (vedi EP-05, EP-07). [Aperto]
- Conservazione dei dati dopo la revoca (responsabile della privacy). [Aperto]
- Vincolo: una sola e-mail per OPT (confermato); nessun dato personale delle persone assistite in nessun punto.
- Correlate: EP-05, EP-07. Fonti: trascrizione della lezione (24/10), diagramma dei casi d'uso della docente, desiderata §5.1, appunti dello stakeholder (BA).
```

---

## EP-02

**Title**
```text
[EPIC] Catalogo delle misure e offerta delle OPT
```

**Objective**
```text
Permettere al Banco di pubblicare e tenere aggiornato il catalogo delle misure di accompagnamento, e a ogni OPT di dichiarare quali misure offre, così che il Banco sappia chi può erogare cosa.
```

**Stakeholders and value**
```text
- Banco: aggiorna il catalogo senza uno sviluppatore e individua i possibili erogatori per una richiesta. [Concordato]
- OPT: dichiara le misure che svolge effettivamente e può poi essere chiamata a erogarle per altre OPT. [Concordato]
Valore: un catalogo configurabile (nessun elenco fisso nel codice) e un quadro aggiornato dell'offerta sul territorio regionale.
```

**Scope**
```text
- Il Banco pubblica il catalogo (elenco iniziale di dodici misure) e lo modifica nel tempo. [Concordato]
- L'OPT consulta il catalogo e comunica le misure che offre; può aggiornarle. [Concordato]
- Il Banco vede quali OPT offrono una certa misura (serve a EP-04). [Proposta]
```

**Out of scope**
```text
- Pubblicare nel sistema la disponibilità delle OPT: il direttore è stato esplicito, la disponibilità non si gestisce; il Banco contatta le OPT una per una.
- Contatori o dati aggregati sull'attività ordinaria dell'OPT (discussi in aula e tolti finché non c'è conferma). [Aperto]
- Un profilo informativo dell'OPT (per esempio l'indirizzo). [Aperto: proposto in aula, non confermato]
```

**Epic completion criteria**
```text
- [ ] Tutte le User Story necessarie sono state completate
- [ ] Il Banco può modificare il catalogo senza interventi sul codice
- [ ] Un'OPT può dichiarare e aggiornare le misure che offre, e il Banco può vederle
- [ ] È stato dimostrato il flusso end-to-end «catalogo → offerta → uso nella ricerca dell'erogatore»
```

**Dependencies, risks and constraints**
```text
- Dati quantitativi delle OPT: i desiderata (§5.2) li prevedono, in aula si è ricordato che il direttore non ne ha bisogno. Da chiedere. [Aperto]
- Uso della categoria «Altro» e misure che richiedono una qualifica professionale. [Aperto]
- Correlata: EP-04. Fonti: trascrizione della lezione, diagramma dei casi d'uso della docente, desiderata §5.2.
```

---

## EP-03

**Title**
```text
[EPIC] Richieste di misura e stato delle richieste (lato OPT)
```

**Objective**
```text
Permettere a un'OPT che non riesce a soddisfare da sola il bisogno di una persona assistita di chiedere una misura al Banco, senza identificare la persona, e di seguire lo stato delle proprie richieste.
```

**Stakeholders and value**
```text
- OPT: un solo posto dove chiedere e vedere cosa succede, al posto di telefonate, messaggi e schede separate. [Concordato]
- Banco: riceve le richieste in ordine di arrivo attraverso un unico canale tracciabile. [Concordato]
- Persone assistite (indirettamente): risposte più rapide e affidabili; nel sistema non entra nessun dato identificativo.
Valore: le richieste sono tracciabili; le OPT non si parlano mai direttamente.
```

**Scope**
```text
- L'OPT crea una richiesta per una misura del catalogo, per una persona o un nucleo familiare, senza dati identificativi. [Concordato]
- L'OPT vede lo stato delle proprie richieste (e solo delle proprie). [Proposta: ragionevole, non richiesta]
- L'OPT riceve la notifica dei cambi di stato (secondaria). [Proposta]
```

**Out of scope**
```text
- Richieste tra OPT; la ricerca interna di una risposta da parte dell'OPT; il contatto con la persona assistita (gestito fuori dal sistema).
- Priorità delle richieste: si servono in ordine di arrivo.
```

**Epic completion criteria**
```text
- [ ] Tutte le User Story necessarie sono state completate
- [ ] Un'OPT può inviare una richiesta e seguirla fino a uno stato finale
- [ ] Nessun dato identificativo delle persone assistite viene richiesto, memorizzato o registrato nei log
- [ ] Sono stati verificati gli scenari di qualità pertinenti (privacy, usabilità da smartphone)
```

**Dependencies, risks and constraints**
```text
- Informazioni minime di una richiesta che non identifichino la persona; servono esempi reali (anonimizzati). [Aperto]
- Stati delle richieste e casi limite (suggeriti: In programmazione, Completata, Annullata, Rifiutata). [Aperto]
- Una richiesta corrisponde a un solo incontro o a un percorso di più incontri? [Aperto]
- Correlate: EP-04, EP-05. Fonti: trascrizione della lezione, diagramma dei casi d'uso della docente, desiderata §5.3, appunti dello stakeholder (BA).
```

---

## EP-04

**Title**
```text
[EPIC] Gestione delle richieste e assegnazione dell'erogatore (lato Banco)
```

**Objective**
```text
Permettere al Banco di ricevere le richieste delle OPT, trovare chi può erogare la misura (operatore interno, OPT o professionista esterno) e assegnarla, mantenendo l'intero processo tracciabile.
```

**Stakeholders and value**
```text
- Banco: è il cuore del suo lavoro; la decisione finale sull'assegnazione è sempre presa da un operatore del Banco. [Concordato]
- OPT e operatori contattati come possibili erogatori.
- Ministero (indirettamente): il Banco deve monitorare le transazioni OPT 1 → Banco → OPT 2. [Concordato]
Valore: abbinamento più rapido e tracciabilità completa, al posto di telefonate e messaggi.
```

**Scope**
```text
- Il Banco vede le richieste in arrivo, in ordine di arrivo, e quelle ancora in attesa. [Concordato]
- Il Banco individua i possibili erogatori per misura, territorio e disponibilità e li contatta. [Concordato]
- Il Banco assegna l'erogatore; se nessuno risponde o l'erogatore rifiuta, il Banco riassegna. [Concordato]
- Il Banco consulta lo storico di una richiesta. [Proposta]
- Miglioramenti facoltativi da validare con il direttore: il sistema suggerisce i candidati ordinati per vicinanza, carico e competenza; il Banco può inviare una richiesta di disponibilità a un numero limitato di candidati (non un broadcast); nulla è confermato finché il Banco non assegna; gli altri erogatori contattati vengono liberati, con la disponibilità trattenuta per un tempo limitato (per esempio due ore). [Proposta]
```

**Out of scope**
```text
- Pubblicare la disponibilità nel sistema; contatto diretto tra OPT; invio della richiesta a tutte le OPT in broadcast.
- Assegnazione automatica senza una decisione del Banco.
- Priorità delle richieste.
```

**Epic completion criteria**
```text
- [ ] Tutte le User Story necessarie sono state completate
- [ ] È stato dimostrato il flusso end-to-end richiesta → ricerca dell'erogatore → assegnazione
- [ ] Il Banco può vedere stato e storico di ogni richiesta
- [ ] Sono stati verificati gli scenari di qualità pertinenti (tracciabilità, prestazioni nei picchi trimestrali, disponibilità)
```

**Dependencies, risks and constraints**
```text
- Ordine di ricerca: prima OPT e operatori esterni sul territorio e gli operatori interni come ripiego, oppure il contrario; potrebbe dipendere dalla misura (in presenza o a distanza). [Aperto]
- Un erogatore alla volta o più in parallelo? Il desiderio del direttore di assegnare un'OPT alla volta è in conflitto con la richiesta di disponibilità in parallelo. [Aperto]
- Tempi di risposta: il direttore ha escluso timeout e notifiche (sezione delle richieste in attesa); la disponibilità trattenuta è solo una proposta. [Aperto]
- Criteri e significato di «vicino». [Aperto]
- Correlate: EP-02, EP-03, EP-05. Fonti: trascrizione della lezione, diagramma dei casi d'uso della docente («Gestione Richieste da OPT»), desiderata §5.3, appunti dello stakeholder (BA).
```

---

## EP-05

**Title**
```text
[EPIC] Risposta degli erogatori e appuntamenti
```

**Objective**
```text
Permettere agli erogatori (OPT, operatori interni, operatori esterni) di ricevere una richiesta dal Banco, accettarla o rifiutarla e confermare l'appuntamento, e permettere al Banco di comunicare i dettagli all'OPT richiedente.
```

**Stakeholders and value**
```text
- Erogatori (OPT, operatore interno, operatore esterno): ricevono le richieste e rispondono in un unico posto. [Concordato per le OPT; Proposta per gli operatori]
- Banco: sa chi ha accettato e quando, e quali appuntamenti sono confermati. [Concordato]
- OPT richiedente: riceve i dettagli dell'appuntamento e li comunica alla persona assistita. [Concordato]
Valore: appuntamenti confermati e tracciabili senza telefonate; report che si riferiscono a prestazioni realmente accettate.
```

**Scope**
```text
- L'erogatore riceve una richiesta che il Banco gli ha indirizzato. [Concordato]
- L'erogatore accetta o rifiuta (con un motivo). [Proposta: sollevato in aula, ancora senza caso d'uso]
- L'operatore conferma l'appuntamento; in presenza: data, luogo, orario e referente; a distanza: data, orario e collegamento alla videochiamata. [Concordato]
- Il Banco comunica i dettagli all'OPT richiedente. [Concordato]
- Il Banco vede gli appuntamenti confermati. [Proposta]
```

**Out of scope**
```text
- La piattaforma di videochiamata in sé (il sistema gestisce solo il collegamento). [Proposta]
- Come un'OPT organizza il proprio personale per erogare la misura (scatola nera).
- Il contatto tra OPT richiedente e persona assistita (fuori dal sistema).
```

**Epic completion criteria**
```text
- [ ] Tutte le User Story necessarie sono state completate
- [ ] È stato dimostrato il flusso end-to-end assegnazione → accettazione → appuntamento confermato → informazioni all'OPT richiedente
- [ ] I casi di rifiuto e di mancata risposta sono gestiti e visibili al Banco
```

**Dependencies, risks and constraints**
```text
- Il diagramma dei casi d'uso della docente ha «Accettare Richiesta Ricevuta» solo per l'OPT; gli operatori interni ed esterni sono raggiunti da «Gestione Richieste da OPT» ma non hanno un caso d'uso per accettare, rifiutare o confermare. [Aperto]
- Gli operatori esterni hanno bisogno di un account, ma «Assegna Credenziali ad Operatori» riguarda solo gli interni; come il Banco contatta un operatore esterno non registrato. [Aperto]
- Chi riceve la richiesta di appuntamento: l'OPT o l'operatore messo a disposizione dall'OPT. [Aperto]
- Visite a distanza (quali misure, quale piattaforma) e significato di «referente». [Aperto]
- Correlate: EP-01, EP-04. Fonti: trascrizione della lezione, diagramma dei casi d'uso della docente, desiderata §5.3.
```

---

## EP-06

**Title**
```text
[EPIC] Comunicazioni del Banco alle OPT
```

**Objective**
```text
Permettere al Banco di inviare comunicazioni alle OPT e di avere la certezza che siano state ricevute.
```

**Stakeholders and value**
```text
- Banco: raggiunge tutte le OPT o un sottogruppo con notizie importanti (per esempio convocazioni, avvisi, promemoria di scadenza) e sa chi le ha ricevute. [Concordato]
- OPT: riceve le comunicazioni in un solo posto e ne conferma la ricezione. [Concordato]
Valore: nessun broadcast senza evidenza di consegna; comunicazione affidabile verso circa 400 destinatari.
```

**Scope**
```text
- Il Banco invia una comunicazione, con allegati, a tutte le OPT o a un sottogruppo. [Concordato]
- L'OPT la legge e conferma la ricezione. [Concordato]
- Il Banco vede quali OPT hanno confermato. [Concordato]
```

**Out of scope**
```text
- Broadcast semplice senza conferma; comunicazioni alle persone assistite.
- Comunicazioni agli operatori propri dell'OPT (l'OPT fa da intermediario). [Aperto]
- Ricerca e organizzazione delle comunicazioni passate, se non giustificate.
```

**Epic completion criteria**
```text
- [ ] Tutte le User Story necessarie sono state completate
- [ ] Una comunicazione con allegato raggiunge un sottogruppo scelto e le conferme sono visibili al Banco
- [ ] Gli allegati rispettano i vincoli di memorizzazione del progetto
```

**Dependencies, risks and constraints**
```text
- Nel diagramma dei casi d'uso della docente «Invio Comunicazioni» non ha frecce verso i destinatari: chi riceve le comunicazioni e con quale canale. [Aperto]
- Tipi di comunicazione, allegati ammessi (formato, dimensione), chi legge la notifica. [Aperto]
- Correlata: EP-01. Fonti: trascrizione della lezione, diagramma dei casi d'uso della docente, desiderata §5.4, appunti dello stakeholder (BA).
```

---

## EP-07

**Title**
```text
[EPIC] Scheda di monitoraggio trimestrale
```

**Objective**
```text
Permettere agli operatori di inviare la scheda di monitoraggio di ogni trimestre e al Banco di raccogliere le schede per la rendicontazione al ministero.
```

**Stakeholders and value**
```text
- Operatori (interni al Banco ed esterni): compilano e inviano la scheda direttamente al Banco. [Concordato per gli interni; Concordato nel diagramma della docente per gli esterni]
- Banco: raccoglie le schede e le usa per la rendicontazione; oggi i dati si inseriscono a mano nel portale ministeriale. [Concordato]
- Ministero e responsabile della privacy: destinatari della rendicontazione e responsabili delle regole di conservazione.
Valore: meno lavoro manuale e meno errori; le schede contengono dati personali e amministrativi degli operatori e dati aggregati sui destinatari, quindi richiedono una protezione adeguata.
```

**Scope**
```text
- L'operatore compila la scheda di un trimestre e la invia al Banco. [Concordato]
- Il Banco vede le schede ricevute e chi non l'ha ancora inviata. [Proposta]
- Il Banco esporta i dati per facilitare l'inserimento manuale nel portale ministeriale. [Proposta]
- Controlli di coerenza sulla scheda (regole da definire). [Proposta]
```

**Out of scope**
```text
- Integrazione diretta con il portale ministeriale (non richiesta).
- Schede degli operatori propri delle OPT (non consegnate al Banco).
- Dati identificativi delle persone assistite: solo conteggi aggregati.
- Collegare la scheda a una specifica OPT, misura o richiesta: la rendicontazione trimestrale è separata dal flusso delle richieste.
```

**Epic completion criteria**
```text
- [ ] Tutte le User Story necessarie sono state completate
- [ ] Un operatore può inviare una scheda trimestrale e il Banco può raccoglierla
- [ ] I dati delle schede sono accessibili solo ai ruoli autorizzati
- [ ] Sono stati verificati gli scenari di qualità pertinenti (privacy, prestazioni alla scadenza trimestrale)
```

**Dependencies, risks and constraints**
```text
- Secondo il diagramma della docente gli operatori esterni inviano la scheda; gli appunti sul direttore dicevano che gli operatori delle OPT non la inviano. Chi inserisce i dati quando l'attività è svolta da un'OPT. [Aperto]
- Rischio di rendicontazione duplicata quando un operatore è associato a un'OPT. [Aperto]
- Regole di validazione (le categorie che si sovrappongono non devono per forza sommare al totale) e conservazione dei dati. [Aperto]
- Correlata: EP-01. Fonti: trascrizione della lezione, diagramma dei casi d'uso della docente («Invio Scheda Monitoraggio»), desiderata §5.5 e Appendice B, appunti dello stakeholder (BA).
```

---

## Dopo le epic

1. **Creare le sette issue** dal modulo Epic e assegnare i **tipi/etichette** come prevede il repository (le issue non sono state create da me).
2. **Scrivere le User Story** come sub-issue di ogni epic con il modulo *User Story* (campi: user story, contesto e valore, criteri di accettazione, dipendenze, epic padre, fonte e stato del requisito, *Definition of Ready*): partire dai «semi» di [[epic-da-lezione-progetto]], controllare INVEST ([[valutare-user-stories-invest]]).
3. **Portare i punti [Aperto]** all'Open Questions Log ([[domande-al-committente]]).

## Fonti

[[epic-da-lezione-progetto]] · [[PICUS-casi-d-uso.pdf]] · [[trascrizione-lezione-progetto-1]] · [[guida-progetto-picus]] § 4.5, 5.2 · [[incontro-stakeholder-ba]] · [[user-stories]]

_Aggiornato: 2026-10-24 — prima stesura nel formato del template_
_Aggiornato: 2026-10-24 — testi tradotti in italiano_
