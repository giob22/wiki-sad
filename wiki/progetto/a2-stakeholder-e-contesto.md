---
tipo: progetto-artefatto
stato: aggiornato dopo il primo confronto con lo stakeholder
data: 2026-10-21
sprint: "S1 — Preparazione PICUS"
attivita: "S1-01 — Stakeholder e Context Diagram (capitolo A2 della documentazione)"
fonti: ["00-Presentazione Progetto Picus.pdf", "01-PICUS_richieste_informali_del_committente (1).pdf", "AGENTS.md", "BA.pdf"]
---

# A2 — Stakeholder e contesto (attività S1-01)

Capitolo A2 del documento «Documentazione SAD 2026» del gruppo *Pinguini alla Fragola*, per l'issue **S1-01**. Questa è la **versione snella** dopo il primo confronto con lo stakeholder ([[incontro-stakeholder-ba]]): sostituisce la prima stesura, basata solo sui desiderata, che era più lunga e con molte tabelle. Il file Word da scaricare è [[A2-stakeholder-e-contesto.docx]].

Sigle delle fonti, come nel Word: **F01** = [[00-Presentazione Progetto Picus.pdf]]; **F02** = [[01-PICUS_richieste_informali_del_committente (1).pdf]]; **F03** = [[AGENTS]]; **F06** = [[BA.pdf]] (appunti dell'incontro: da registrare in D2). Marcatori: 📄 fonte, 🧩 elaborazione mia.

> 🧩 **Come si lega a Scrum.** L'attività S1-01 è un elemento dello Sprint 1 con un obiettivo (capire il contesto, individuare gli stakeholder, fissare i confini) e una **Definition of Done**: i sette criteri dell'issue, ripresi in fondo. Come ogni artefatto di una iterazione, A2 è un **incremento**: si aggiorna a ogni confronto e il dettaglio dei flussi si approfondisce nelle user story quando serve, non in anticipo ([[cerimonie-e-artefatti-agile]], [[sviluppo-agile]]).

## Contesto

- PICUS sostiene un programma di aiuti con distribuzione di beni e **misure di accompagnamento**. Il Banco gestisce il centro operativo regionale ed è **capofila verso il ministero**. 📄 [[01-PICUS_richieste_informali_del_committente (1).pdf#page=1]] §2; [[BA.pdf#page=1]]
- Dimensioni emerse nel confronto: **400–450 OPT**, **200 comuni**, circa **230.000 utenti** (le persone assistite). I desiderata dicevano circa 200 OPT: il numero dello stakeholder è più alto ed è da riconfermare (Q-20).
- Flusso centrale: **OPT 1 → Banco → OPT 2** (o un altro erogatore). Il Banco intermedia e **monitora le transazioni**. L'OPT si rivolge al Banco quando non riesce a soddisfare da sola i bisogni dei propri assistiti.
- Oggi tutto passa da telefono, messaggi, documenti e schede separate. 📄 F02 §4

**Da preservare:** tutela dei dati, separazione dei ruoli, nessun dato identificativo delle persone assistite, ruolo di coordinamento del Banco. 📄 F02 §1

## Stakeholder

| Stakeholder | Cosa fa e cosa vuole | Usa l'app? |
|---|---|---|
| **Banco** | coordina le richieste e trova l'erogatore, monitora le transazioni, gestisce cataloghi e account delle OPT (anche con caricamento massivo), invia comunicazioni con conferma di ricezione, raccoglie i dati per la rendicontazione al ministero | sì, visione complessiva |
| **OPT** | chiede una misura per le persone che assiste quando non riesce a soddisfarle da sola e dichiara le misure che offre; **un solo accesso per OPT** (una email) | sì, solo i propri dati |
| **Operatori** | interni al Centro PICUS o professionisti esterni: erogano le misure, confermano gli appuntamenti, compilano la scheda trimestrale | sì, accesso personale (ipotesi) |
| **Persone assistite** | ricevono la misura tramite l'OPT; nessun accesso, nessun dato identificativo | no |
| **Ministero e responsabile privacy** | il ministero riceve la rendicontazione; il responsabile privacy definisce la conservazione dei dati | no (interlocutori) |

**Gli operatori e i volontari delle singole OPT non sono utenti**: la gestione interna di ogni OPT non riguarda PICUS, il Banco non comunica direttamente con loro e non chiede la scheda trimestrale. 📄 F06

## Cosa abbiamo capito dal confronto con lo stakeholder

Dettaglio e confronto con i desiderata in [[incontro-stakeholder-ba]]. In sintesi:

- **Una sola email per OPT:** un account per OPT (Q-01 risolta per l'MVP).
- **Operatori delle OPT senza accesso**, il Banco non li contatta (Q-09 quasi risolta).
- **Niente messaggi broadcast:** notizie importanti alle OPT con **conferma di ricezione**, anche solo a un **sottogruppo** (Q-08 in gran parte risolta).
- **Richieste non prioritizzate:** in ordine di arrivo.
- **Registrazione senza documenti**; credenziali caricabili in massa ogni anno da un CSV (opzionale), senza scadenza; il Banco rimuove a mano le OPT scadute.
- **Confine:** quello che accade dentro l'OPT non interessa; contano i servizi offerti, le richieste e la scheda trimestrale.

## Confini e Context Diagram

PICUS è una scatola unica con tre attori applicativi (Banco, OPT, Operatore) e le informazioni che scambiano con il sistema. **Dentro:** account, catalogo, richieste, appuntamenti, comunicazioni, scheda trimestrale. **Fuori:** la gestione interna delle OPT, il contatto tra OPT e persona assistita, l'inserimento manuale nel portale ministeriale.

![[ctx-01-diagramma-team.png]]
*Figura A2.1 — Context Diagram CTX-01, versione del gruppo. A sinistra il Banco (in alto) e l'Operatore (in basso), a destra l'OPT, al centro «Sistema PICUS». Ogni freccia è un'informazione e la punta ne indica la direzione. Dal Banco: configurazione del catalogo, creazione e revoca di account con caricamento massivo di credenziali, assegnazione dell'erogatore con verifica di disponibilità e coordinamento dell'appuntamento, comunicazioni con allegati a gruppi e sottogruppi di OPT. Verso il Banco: vista complessiva delle richieste e dello stato, disponibilità e misure offerte, conferme di lettura, dati aggregati e schede trimestrali per la rendicontazione. Dall'OPT: dichiarazione delle misure e della disponibilità, richiesta di misura senza dati personali, risposte sulla disponibilità, dati quantitativi, conferme di ricezione. All'OPT: catalogo, stato delle richieste e dettagli dell'appuntamento, richieste di disponibilità, comunicazioni. Dall'Operatore: conferma di disponibilità e appuntamenti, scheda trimestrale; verso l'Operatore: richieste di appuntamento da confermare e riepilogo storico.*

Versione in Mermaid dello stesso diagramma, con i flussi riassunti per direzione (nota del gruppo): [[Context Diagram]].

**Osservazioni da discutere nel team** 🧩 (proposte, non decisioni):

1. **Soggetti esterni.** Persone assistite e portale ministeriale non compaiono: per mostrare il confine completo si possono aggiungere con un collegamento tratteggiato (contatto OPT-assistito, inserimento manuale nel portale). 📄 F02 §5.5
2. **Scheda trimestrale.** Il diagramma la lega all'Operatore, mentre l'OPT «inserisce dati quantitativi aggregati»: da chiarire se sono la stessa scheda o due dati diversi (Q-21), perché F06 dice che gli operatori delle OPT non la compilano.
3. **Etichette.** Alcune sono molto lunghe: per la review conviene accorciarle e lasciare i dettagli alle user story.

## Ipotesi e domande ancora aperte

**Ipotesi:** il Banco è un unico ruolo con visione complessiva; la videochiamata avviene su una piattaforma esterna e PICUS tratta solo il collegamento; gli operatori hanno un accesso personale limitato alla propria scheda e agli appuntamenti.

**Domande per il prossimo confronto**, in ordine di priorità (elenco completo in [[domande-al-committente]]):

1. informazioni minime per una richiesta senza identificare la persona, con 3–5 richieste reali anonime (Q-02);
2. criteri di scelta dell'erogatore (Q-03);
3. stati di una richiesta e casi limite; cosa significa «monitorare le transazioni» (Q-04);
4. conservazione dei dati e destino di quelli di una OPT rimossa (Q-05);
5. regole della scheda trimestrale e formato per il portale; chi la compila per le attività svolte dalle OPT (Q-06, Q-21);
6. richieste al mese e picchi, ora che le OPT sono 400–450 (Q-07, Q-20).

## Definition of Done di S1-01

- ☑ stakeholder principali descritti con obiettivi e responsabilità;
- ☑ il diagramma distingue il sistema dai soggetti esterni (da completare con le osservazioni sopra);
- ☑ persone assistite come stakeholder, senza accesso all'applicazione;
- ☑ coordinamento del Banco e ruolo dell'OPT preservati;
- ☑ vincoli sui dati identificativi degli assistiti espliciti;
- ☑ ipotesi e dubbi distinti dalle fonti;
- ☐ analisi e diagramma **revisionati da un altro membro** (da fare: revisore e data).

**Prossimi passi nello sprint:** riconfermare i numeri con lo stakeholder, aggiornare CTX-01, usare le risposte per S1-02 (as-is), S1-04 (Epic) e S1-05 (backlog), portare le domande aperte alla Sprint Review del 05/11 ([[00-Presentazione Progetto Picus.pdf#page=11]]).

## File

Word: [[A2-stakeholder-e-contesto.docx]], generato da [[genera_docx_a2.py]]. Il diagramma è un file del gruppo.

_Aggiornato: 2026-10-21 — riscritta in versione snella dopo il confronto con lo stakeholder; la prima stesura è nella cronologia di Git_
