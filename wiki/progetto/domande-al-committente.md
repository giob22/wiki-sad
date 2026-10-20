---
tipo: progetto-artefatto
stato: bozza per il team — domande da validare prima di porle
data: 2026-10-20
sprint: "S1 — Preparazione PICUS (attività 8: Open Questions Log)"
---

# Domande da porre al direttore del Banco

Elenco ragionato dei dubbi più rilevanti da chiarire con il committente (il direttore del Banco) per l'**Open Questions Log** (attività 8, [[00-Presentazione Progetto Picus.pdf#page=25]]). Le domande sono scritte in linguaggio non tecnico, così si possono leggere così come sono.

| Marcatore | Significato |
|---|---|
| 📄 | dubbio già presente nelle fonti: [[01-PICUS_richieste_informali_del_committente (1).pdf#page=5]] (§8) o decisioni aperte di [[AGENTS]] §8 |
| 🧩 | domanda ricavata da me analizzando requisiti, MVP e architettura: non è nelle fonti |

Gli ID `Q-01…Q-08` sono quelli già nell'elenco candidato del Word (A6), `Q-09…Q-11` sono quelli proposti in [[a2-stakeholder-e-contesto]], `Q-12…Q-19` sono nuovi e da aggiungere. Le **ipotesi provvisorie** sono mie, da discutere nel team.

> Vincoli già dati dal committente, **da non riaprire come dubbi**: le persone assistite non hanno account né dati identificativi; la scheda trimestrale è distinta dal flusso delle richieste; l'integrazione con il portale ministeriale non è richiesta; audit completo e biometria non sono richiesti. [[01-PICUS_richieste_informali_del_committente (1).pdf#page=1]] (§1, §3), §5.5.

## Priorità alta: bloccano l'MVP, la sicurezza o l'architettura

| # | Q | Domanda al direttore | Perché serve | Ipotesi provvisoria 🧩 | Fonte |
|---|---|---|---|---|---|
| 1 | Q-01, Q-09 | **Chi, in ogni OPT, userà l'app?** Una persona, due, più referenti? Cambiano spesso? Chi decide chi ha l'accesso e chi lo toglie? Gli operatori esterni e i volontari delle OPT devono avere un accesso personale, oppure agiscono tramite l'OPT? | decide il modello degli account, le autorizzazioni e la continuità quando cambia il referente: tocca quasi tutte le storie | un account per OPT (ipotesi della fonte) e accesso personale per gli operatori | 📄 §5.1, §8; [[a2-stakeholder-e-contesto]] |
| 2 | Q-02 | **Quali informazioni minime servono al Banco per lavorare una richiesta, senza identificare la persona?** Per esempio composizione del nucleo, fascia d'età, comune, lingua, urgenza, esigenze particolari. Potete darci 3–5 **richieste recenti reali, rese anonime**? | definisce i campi del modulo e testa il vincolo sulla privacy: troppo poco e il Banco non sa cosa cercare, troppo e si rischia di identificare | solo i campi strettamente necessari alla scelta dell'erogatore | 📄 §5.3, §8 |
| 3 | Q-03 | **Come scegliete oggi l'erogatore?** Quali criteri (competenza, territorio, disponibilità) e in che ordine? Cosa vuol dire «vicino» (stesso comune, provincia, distanza)? Cosa fate quando ce n'è più di uno o nessuno? Quando consultate altre OPT, come e quante? | è il cuore del processo: decide la ricerca dell'erogatore e quanto va automatizzato | il Banco sceglie, il sistema propone i candidati per misura, territorio e disponibilità | 📄 §5.3, §8 |
| 4 | Q-04 | **Quali sono i passaggi veri di una richiesta?** Oltre a In programmazione, Completata, Annullata, Rifiutata: chi può rifiutare e perché serve il motivo? E se nessuno è disponibile, o l'incontro non avviene, o l'assistito non si presenta? Si può riassegnare? | definisce il ciclo di vita, i permessi di ogni ruolo e le transizioni da testare | quattro stati base più motivazioni; stati intermedi solo se emergono casi reali | 📄 §5.3, §8 |
| 5 | Q-12 🧩 | **Una richiesta corrisponde a un solo incontro o a un percorso di più incontri?** (per esempio sostegno psicologico, sostegno scolastico). Chi decide quante sedute? | cambia il modello dati (richiesta, appuntamento, ciclo) e lo stato «Completata» | una richiesta = un appuntamento, con possibilità di richiederne altri | 🧩 |
| 6 | Q-05 | **Privacy e conservazione:** chi è il responsabile privacy da coinvolgere? Per quanto tempo si conservano richieste, appuntamenti e schede? Cosa succede ai dati di una OPT che cessa? Dove possono stare i dati (server in UE)? | regole di cancellazione, accessi e dove ospitare il sistema; serve a scrivere gli scenari di privacy | nessuna policy inventata: si chiede | 📄 §5.1, §7, §8 |
| 7 | Q-06, Q-11 | **Scheda trimestrale:** chi la controlla e quali errori capitano più spesso? Quali regole di coerenza esistono (ore, trimestre, categorie che si sovrappongono)? Cosa succede se un operatore non la invia o la corregge dopo l'invio? Il portale ministeriale chiede un formato o dei campi precisi per l'inserimento manuale? | prevenire errori e capire che esportazione serve al Banco | validazioni leggere + esportazione in formato tabellare | 📄 §5.5, §8, app. B |
| 8 | Q-13 🧩 | **Cosa vi fa perdere più tempo oggi?** Richieste e ricerca dell'erogatore, schede trimestrali, comunicazioni alle OPT? Quale miglioramento vi cambierebbe di più la settimana? | serve a scegliere l'**MVP** e le priorità del backlog con un criterio del committente, non solo nostro | il flusso richiesta → erogatore → appuntamento | 🧩; [[00-Presentazione Progetto Picus.pdf#page=26]] |
| 9 | Q-07 | **Quante persone useranno il sistema e quando?** Quante OPT, quanti operatori, quante richieste al mese? Come sono i **picchi** vicino alle scadenze trimestrali (date e durata)? Che telefoni e che connessione hanno le OPT, anche nei comuni piccoli? Cosa fate quando il sistema non funziona per qualche ora o un paio di giorni? | scenari misurabili di performance, disponibilità e usabilità senza inventare numeri | si evita di dedurre gli utenti contemporanei dalle ~200 OPT | 📄 §7, §8; [[AGENTS]] §9 |
| 10 | Q-08 | **Comunicazioni:** che tipi ne mandate (convocazioni, avvisi, promemoria), a chi (tutte le OPT, gruppi) e quanto spesso? Che allegati (formato, dimensione)? Serve sapere chi le ha lette? Che canali vi vanno bene (email, notifica)? | decide notifiche, allegati e riepiloghi senza ampliare il perimetro | solo avvisi dentro l'app e allegati; email e conferma di lettura come proposta | 📄 §5.4, §8 |

## Priorità media: da chiarire entro la prima iterazione di costruzione

| # | Q | Domanda al direttore | Perché serve | Fonte |
|---|---|---|---|---|
| 11 | Q-10 | **Visite a distanza:** quali delle dodici misure si possono fare in videochiamata? Avete già una piattaforma di videochiamata, oppure serve che il sistema generi i collegamenti? | decide se esiste un sistema esterno nel Context Diagram | 📄 §5.3; IP-03 |
| 12 | Q-11 | **Incontri in presenza:** chi è il «referente» citato nel documento? Dove si svolgono (sede dell'OPT, del Centro, dello studio del professionista)? | definisce i campi dell'appuntamento | 📄 §5.3 |
| 13 | Q-14 🧩 | **Catalogo delle misure:** chi lo aggiorna e quanto spesso? Come si usa «Altro»? Quali misure richiedono una qualifica professionale? | rende il catalogo configurabile davvero e modella le competenze degli erogatori | 📄 §5.2, app. A |
| 14 | Q-15 🧩 | **Dentro il Banco chi fa cosa?** Chi coordina le richieste, chi amministra i cataloghi e gli account, chi fa la rendicontazione? Servono più profili? | decide se «Banco» è un solo ruolo o più (ipotesi IP-01) | 📄 §3; IP-01 |
| 15 | Q-16 🧩 | **Dati già esistenti:** in che formato è l'anagrafica delle ~200 OPT (Excel, altro)? È aggiornata? Va caricata così com'è? Serve portare dentro anche lo storico di richieste e schede? | caricamento iniziale e migrazione, anche se lo storico completo non è richiesto | 📄 §5.2, §6 |
| 16 | Q-17 🧩 | **Perimetro:** il sistema deve riguardare anche la **distribuzione dei beni**, oppure solo le misure di accompagnamento? Ci sono integrazioni previste in futuro? | confini del sistema e del Context Diagram | 📄 §2 |
| 17 | Q-18 🧩 | **Tracciabilità minima:** quali domande vorreste poter rispondere guardando la storia di una richiesta («chi l'ha rifiutata e quando»)? | definisce il «livello minimo di registrazione eventi» proposto | 📄 §7 |
| 18 | Q-19 🧩 | **Come lavoriamo insieme:** chi è l'interlocutore che valida le proposte e con che tempi risponde? Quando potete essere presenti alle review? | le proposte funzionali entrano nella baseline solo dopo il confronto con il committente | 📄 §1, §9; [[00-Presentazione Progetto Picus.pdf#page=8]] |

## Documenti da chiedere in aggiunta alle risposte

- un **esempio reale (anonimo)** della scheda trimestrale compilata e di una **richiesta** recente;
- l'**elenco delle OPT** nel formato attuale, senza dati personali sensibili;
- un **esempio di comunicazione** con allegato mandata alle OPT;
- il **calendario delle scadenze trimestrali** e il **modulo o i campi richiesti dal portale ministeriale**;
- eventuali **regole interne o istruzioni sulla privacy** già in uso.

## Come condurre l'incontro (🧩)

1. Partire da **casi concreti**, non dalle funzioni: «raccontatemi l'ultima richiesta che avete gestito, passaggio per passaggio». È il modo più sicuro per far emergere i casi limite delle domande 3–5.
2. Per ogni risposta chiedere **«e se invece…?»** su una situazione anomala: rifiuto, assenza, errore.
3. Distinguere **fatto** («oggi si fa così»), **desiderio** («vorremmo») e **vincolo** («per legge dobbiamo»): nel Word si registrano in modo diverso (Fonte, Proposta, Ipotesi).
4. Chiudere ogni punto con una frase che si possa **registrare**: risposta, data, interlocutore. Una risposta parziale non chiude tutte le questioni collegate ([[a2-stakeholder-e-contesto]], gestione del registro).
5. Se la risposta cambia un'**ipotesi**, aggiornare gli artefatti coinvolti (storie, criteri, scenari) e annotare la decisione precedente.

_Aggiornato: 2026-10-20 — prima stesura_
