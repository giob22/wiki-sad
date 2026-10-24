---
tipo: progetto-artefatto
stato: bozza per il team — epic da rifinire, poi da scomporre in user story
data: 2026-10-24
sprint: "S1 — Preparazione PICUS (attività 4: individuare le funzionalità principali)"
fonte: "trascrizione-lezione-progetto-1.md"
---

# Epic emerse dalla lezione sul progetto (prima parte)

Sette **epic candidate** ricavate dalla trascrizione della lezione in cui si è discusso il progetto e si è costruito insieme un diagramma dei casi d'uso ([[trascrizione-lezione-progetto-1]]). Servono all'**attività 4** dell'iterazione preparatoria: raggruppare le funzionalità in **5–8 Epic** coerenti ([[00-Presentazione Progetto Picus.pdf#page=21]], [[guida-progetto-picus]] § 5.2–5.3); dalle epic si scrivono poi le **15–25 user story** dell'attività 5 ([[user-stories]], [[valutare-user-stories-invest]]).

| Marcatore | Significato |
|---|---|
| 📄 | detto o deciso nella lezione; tra parentesi il blocco della trascrizione: **T1** 00:00–23:26 · **T2** 23:26–26:22 · **T3** 26:22–46:37 · **T4** 46:37–47:05 · **T5** 47:05–fine |
| 📘 | già nel wiki: desiderata del committente (R §…, [[guida-progetto-picus]] § 4.5), appunti dello stakeholder ([[incontro-stakeholder-ba]]) |
| 🧩 | mia proposta o lettura: non è stata detta così in aula |
| ❓ | non confermato o contraddittorio: da chiedere |

> 🧩 **Come usare questa pagina.** Una epic è un'area funzionale che dà valore a uno stakeholder, troppo grande per entrare in uno sprint ([[user-stories]] § Epic). Qui ogni epic ha: scopo, attori, cosa è emerso in aula, **«semi» di storie** (titoli candidati, ancora da scrivere nel formato *As a… I want… so that…* e da verificare con INVEST), punti aperti e legame con i desiderata. Le aree funzionali **non sono automaticamente i moduli architetturali finali** (📘 AGENTS.md §9).

## 1. Sintesi

| ID | Epic | Attori principali | Maturità | Desiderata (R §) |
|---|---|---|---|---|
| **EP-01** | Accesso, account e ruoli | Banco, OPT, Operatore | media: chi riceve un account è ancora aperto | 5.1 |
| **EP-02** | Catalogo delle misure e offerta delle OPT | Banco, OPT | buona; il profilo e i dati sull'attività sono incerti | 5.2 |
| **EP-03** | Richiesta di misura (lato OPT) | OPT | buona | 5.3 |
| **EP-04** | Ricerca dell'erogatore e assegnazione (lato Banco) | Banco, OPT, Operatore | **cuore del sistema**; molte opzioni, poche certezze | 5.3 |
| **EP-05** | Appuntamenti e conferma degli operatori | Operatore, Banco, OPT | bassa: dipende dal chiarimento sugli operatori | 5.3 |
| **EP-06** | Comunicazioni del Banco alle OPT | Banco, OPT | media (conferma di ricezione già emersa) | 5.4 |
| **EP-07** | Monitoraggio trimestrale (scheda degli operatori) | Operatore, Banco | media: certi solo gli operatori interni | 5.5 |

> 🧩 In aula si è detto che il **nucleo minimale** richiesto dal direttore è: l'OPT fa le richieste, il Banco le gestisce, invia comunicazioni, assegna le credenziali agli operatori e gli operatori interni inviano la scheda di monitoraggio; tutto il resto sono **proposte opzionali da validare con lui** (📄 T4, T5). Questo corrisponde a EP-01, 03, 04, 06, 07 (più il catalogo EP-02, che è comunque nei desiderata); EP-05 e le parti «proposte» di EP-04 sono quelle da confermare.

## 2. Il diagramma dei casi d'uso costruito in aula

> 📄 T2–T5: la professoressa ha guidato la costruzione di un diagramma dei casi d'uso partendo da uno schema preparato da una studentessa; gli attori sono Banco, OPT e Operatore.

```mermaid
flowchart LR
    OPT(["OPT"])
    BANCO(["Banco"])
    OPE(["Operatore interno"])
    subgraph PICUS["Sistema PICUS"]
        UC1["Comunicare le misure offerte"]
        UC2["Fare richiesta di misura"]
        UC3["Visualizzare lo stato di una richiesta"]
        UC4["Accettare una richiesta ricevuta"]
        UC5["Assegnare le credenziali alle OPT (massivo)"]
        UC6["Assegnare le credenziali agli operatori"]
        UC7["Aggiornare il catalogo delle misure"]
        UC8["Gestire le richieste da OPT"]
        UC9["Inviare comunicazioni"]
        UC10["Inviare la scheda di monitoraggio trimestrale"]
    end
    OPT --- UC1
    OPT --- UC2
    OPT --- UC3
    OPT --- UC4
    BANCO --- UC5
    BANCO --- UC6
    BANCO --- UC7
    BANCO --- UC8
    BANCO --- UC9
    OPE --- UC10
    UC8 -.->|"coinvolge"| OPT
```
*🧩 Ricostruzione mia a partire da T2–T5 (la lavagna non è nella trascrizione). Linee piene = «l'attore esegue il caso d'uso»; la linea tratteggiata è la freccia del caso «gestione richieste da OPT» verso l'OPT, tracciata in aula e rimasta in dubbio perché dovrebbe finire anche sull'operatore esterno o interno (📄 T5). Il caso «visualizzare le notifiche» è stato nominato come secondario (📄 T2) e non è disegnato.*

## 3. Le epic

### EP-01 — Accesso, account e ruoli

**Scopo.** Il Banco crea e toglie gli accessi di OPT e operatori; ognuno vede solo ciò che gli compete (📘 R §5.1).
**Attori.** Banco (assegna), OPT, Operatore.

**Cosa è emerso**
- Il Banco **assegna le credenziali alle OPT, anche in modo massivo** (📄 T3). Le registrazioni sono **annuali** e se ne perdono in media **circa cinque all'anno**; il Banco le toglie lui (📄 T3, riferito al direttore); 📘 BA: CSV opzionale ogni anno, senza scadenza.
- Le **credenziali iniziali** arrivano **fuori dal sistema** (per esempio e-mail), perché all'inizio non esistono (📄 T1).
- Il Banco **assegna anche le credenziali agli operatori**, invece di farli registrare da soli: l'accesso degli operatori è più delicato (📄 T3). Per gli operatori interni sono **circa 25 dipendenti** del Banco, quindi un caricamento una tantum con modifiche occasionali (📄 T3). Si è pensato a una gestione **unica** delle registrazioni di OPT e operatori (📄 T3).
- A livello applicativo **non serve distinguere i tipi di operatore**: un ruolo «operatore» e il Banco decide a chi darlo; la distinzione servirebbe solo se i tipi avessero flussi diversi (per esempio un report distinto). Un campo del form di registrazione potrebbe indicare se l'operatore è associato a un'OPT (📄 T1, T3).
- Per iscritto il direttore ha parlato di **tre tipi di operatori**: del Banco, esterni, appartenenti alle OPT (📄 T1, T3, T5).
- Gli **operatori interni alle OPT** sono una *black box*: PICUS non entra nella gestione interna delle OPT (📄 T1; coerente con 📘 BA).
- Le OPT piccole (una parrocchia) possono non avere nemmeno un computer: serve **un unico punto di accesso** semplice (📄 T3).

**Semi di user story** 🧩
1. Il Banco crea l'account di una OPT (con caricamento massivo da file).
2. Il Banco revoca l'accesso di una OPT che cessa.
3. Il Banco crea l'account di un operatore.
4. Un utente accede con le proprie credenziali e vede solo i dati del suo ruolo.
5. Un utente recupera le credenziali (previsto nei desiderata, ❓ non discusso in aula).

**Punti aperti.** Quali operatori devono avere un account (DL-1) e come ci si registra; recupero credenziali; conservazione dei dati dopo la revoca.
**Collegamenti.** 📘 R §5.1 · Q-01 (risolta), Q-05, Q-09, Q-15 ([[domande-al-committente]]).

### EP-02 — Catalogo delle misure e offerta delle OPT

**Scopo.** Il Banco pubblica il catalogo delle misure; le OPT dichiarano quali offrono, così il Banco sa a chi rivolgersi (📘 R §5.2).
**Attori.** Banco, OPT.

**Cosa è emerso**
- Il Banco **pubblica e modifica nel tempo il catalogo** delle misure (📄 T3).
- L'OPT **consulta il catalogo e dichiara ciò che offre** («io offro questo, questo e questo») (📄 T2, T3).
- **Profilo/scheda informativa dell'OPT** (per esempio l'indirizzo): proposta emersa in aula, non confermata (📄 T3 ❓).
- **Non si pubblicano le disponibilità** nel sistema: il direttore è stato molto chiaro; il Banco contatta le OPT una per una (📄 T1, T3: «l'OPT non deve dare la sua disponibilità»). *Misure offerte* ≠ *disponibilità*: le prime sono nel profilo, la seconda non si gestisce.
- **Dati aggregati sull'attività svolta** (l'esempio della parrocchia con 60 bambini al catechismo): discussi e **tolti dal diagramma** perché non c'è certezza che al direttore interessino («quello di cui non siamo sicuri per ora non lo mettiamo») (📄 T3). ⚠️ Contraddizione con 📘 R §5.2, che prevede dati quantitativi, e con il Context Diagram del gruppo: vedi § 6.

**Semi di user story** 🧩
1. Il Banco pubblica il catalogo delle misure.
2. Il Banco modifica il catalogo (aggiunge, cambia o toglie una misura) senza uno sviluppatore.
3. L'OPT dichiara le misure che offre.
4. L'OPT aggiorna le misure offerte.
5. Il Banco vede quali OPT offrono una certa misura (serve a EP-04).

**Punti aperti.** Profilo con indirizzo: sì o no; dati quantitativi (DL-3); come usare «Altro» (Q-14).
**Collegamenti.** 📘 R §5.2 · Q-14, Q-21.

### EP-03 — Richiesta di misura (lato OPT)

**Scopo.** Quando un'OPT non riesce a soddisfare da sola il bisogno di un assistito, lo chiede al Banco senza identificare la persona.
**Attori.** OPT.

**Cosa è emerso**
- L'OPT prima cerca **da sé** (la sua organizzazione interna non interessa); solo se non riesce, **si rivolge al Banco** (📄 T1).
- La richiesta **deve passare per il Banco**: le OPT non parlano tra loro, **il Banco vuole tracciare tutto** (📄 T1). Rifiutata l'idea di mandare l'assistito direttamente a un'OPT vicina trovata sul sito.
- L'OPT **visualizza lo stato della richiesta**: idea del gruppo, ragionevole ma non detta dal direttore (📄 T2, T3).
- L'OPT **accetta** la richiesta quando il Banco la contatta come possibile erogatrice (preferito «accettare» a «confermare») (📄 T2, T3).
- L'OPT **vede le notifiche**: caso d'uso secondario (📄 T2).
- 📘 BA: richieste **non prioritizzate**, in ordine di arrivo; 📘 R §5.3: richiesta per una persona o un nucleo, **senza dati identificativi**.

**Semi di user story** 🧩
1. L'OPT crea una richiesta scegliendo una misura del catalogo, senza dati identificativi.
2. L'OPT vede lo stato delle proprie richieste (e solo delle proprie).
3. L'OPT riceve la notifica di un cambio di stato.
4. L'OPT accetta o rifiuta una richiesta di disponibilità ricevuta dal Banco (→ EP-04).

**Punti aperti.** Informazioni minime di una richiesta (Q-02); stati e casi limite (Q-04); una richiesta = un incontro o un percorso (Q-12).
**Collegamenti.** 📘 R §5.3, BA · Q-02, Q-04, Q-12.

### EP-04 — Ricerca dell'erogatore e assegnazione (lato Banco)

**Scopo.** Il Banco riceve una richiesta, individua chi può erogare la misura (operatore interno, OPT, professionista esterno) e assegna. È **il cuore** («gestione richieste da OPT», 📄 T3).
**Attori.** Banco (principale), OPT ed operatori contattati.

**Cosa è emerso**
- Il Banco cerca l'erogatore con **criteri** come vicinanza, carico, competenze; i criteri vanno **ruotati** per non chiedere sempre agli stessi (📄 T1).
- **Ordine di ricerca: ancora non chiaro.** Nella spiegazione in aula il Banco cerca prima tra gli operatori interni e poi tra le OPT (📄 T1); i partecipanti hanno invece ipotizzato **prima il territorio** (OPT e operatori esterni vicini) e **gli operatori interni come ultima risorsa** (videochiamata), perché le OPT sono ~450 e gli interni pochi; l'ordine potrebbe dipendere dal tipo di misura (in presenza o a distanza) (📄 T5 ❓).
- **Vincoli del direttore:** l'**assegnazione la fa un operatore del Banco** (📄 T1); le OPT non si parlano; niente disponibilità sul sito. Sui tempi di risposta aveva detto che **non serve gestire timeout e notifiche**: basta una **sezione delle richieste pendenti** che il Banco controlla periodicamente e rimanda lui a una seconda persona dopo giorni (📄 T1).
- **Proposta del gruppo (opzionale, da validare):** il sistema **suggerisce** un numero limitato di OPT potenzialmente disponibili (non un broadcast), e il Banco può **far partire in automatico una richiesta di disponibilità** a 4–5 di loro oppure chiamarle a mano; la prima che risponde è candidata, ma **la conferma finale resta al Banco** (📄 T1).
- **Regola proposta:** finché il Banco non assegna, **nulla è confermato**; all'assegnazione le altre richieste si annullano; le OPT contattate **mantengono la disponibilità per un tempo massimo** (per esempio **due ore**) e poi si liberano (📄 T1).
- **Controproposta di Alberto:** secondo lui il committente vuole assegnare **un'OPT alla volta**, in modo non concorrente, e gestirlo direttamente (📄 T1): conflitto da sciogliere (DL-6).
- Il Banco deve **monitorare le transazioni** OPT 1 → Banco → OPT 2 (📘 BA) e tracciare tutto (📄 T1).

**Semi di user story** 🧩
1. Il Banco vede le richieste in arrivo, in ordine di arrivo, e quelle ancora senza risposta (sezione «pendenti»).
2. Il Banco vede l'elenco delle OPT/operatori che offrono la misura richiesta nel territorio.
3. *(Proposta)* Il sistema ordina i candidati per vicinanza, carico e competenze.
4. *(Proposta)* Il Banco invia una richiesta di disponibilità a uno o più candidati.
5. Il Banco assegna l'erogatore e la richiesta cambia stato.
6. Il Banco riassegna la richiesta se l'erogatore non risponde o rifiuta.
7. Il Banco consulta lo storico di una richiesta (chi, quando, cosa).

**Punti aperti.** Ordine di ricerca (DL-5); parallelo o uno alla volta (DL-6); tempi massimi e solleciti (Q-04); criteri e «vicino» (Q-03).
**Collegamenti.** 📘 R §5.3, BA · Q-03, Q-04, Q-18.

### EP-05 — Appuntamenti e conferma degli operatori

**Scopo.** Chi eroga la misura riceve la richiesta, la accetta o rifiuta e conferma l'appuntamento; il Banco restituisce all'OPT le informazioni.
**Attori.** Operatore (interno, esterno), Banco, OPT.

**Cosa è emerso**
- Risposta scritta del direttore: gli operatori che presidiano il centro PICUS sono **interni** (due psicologi per le visite online), **tutti gli altri sono esterni** e dislocati sul territorio, **alcuni messi a disposizione presso le OPT**; sembra che il Banco **mandi la richiesta di appuntamento direttamente agli operatori** e non all'OPT (📄 T3). Ma si è anche detto che internamente a un'OPT «il primo che si collega tra le figure abilitate alla misura può accettarla» (📄 T3): ❓ non è chiaro a chi vada la richiesta.
- Gli **operatori devono poter accettare o rifiutare** le richieste; senza questo i report «sono fatti sul nulla»: punto **rimasto appeso**, perché «la gestione delle richieste» dovrebbe toccare sia l'OPT sia l'operatore (📄 T5).
- 📘 R §5.3: l'operatore conferma l'appuntamento; incontri in presenza (data, luogo, orario, referente) o a distanza (data, orario, collegamento); l'OPT richiedente comunica all'assistito.
- Per mandare una richiesta a un operatore esterno **l'operatore deve essere registrato**: altrimenti il Banco non sa come contattarlo (📄 T5: DL-4).

**Semi di user story** 🧩
1. L'operatore vede le richieste di appuntamento a lui rivolte.
2. L'operatore accetta o rifiuta una richiesta (con motivo).
3. L'operatore conferma data, ora e luogo o collegamento.
4. Il Banco comunica all'OPT richiedente i dettagli dell'appuntamento.
5. Il Banco vede gli appuntamenti confermati.

**Punti aperti.** Chi riceve la richiesta (OPT o operatore); come si registrano gli operatori esterni (DL-1, DL-4); visite a distanza (Q-10); referente (Q-11).
**Collegamenti.** 📘 R §5.3 · Q-04, Q-09, Q-10, Q-11.

### EP-06 — Comunicazioni del Banco alle OPT

**Scopo.** Il Banco invia comunicazioni alle OPT con certezza che siano arrivate.
**Attori.** Banco, OPT.

**Cosa è emerso**
- «Invio comunicazioni» è un caso d'uso del Banco; il **tipo** di comunicazione è da chiarire (📄 T3).
- Serve **evidenza che il messaggio è stato letto** (osservazione in aula legata alla velocità di una richiesta) (📄 T1); 📘 BA: **niente broadcast**, notizie con **conferma di ricezione**, anche a un **sottogruppo**.
- Le comunicazioni vanno **solo all'OPT come intermediario**, oppure serve che anche l'operatore abbia un account per ricevere almeno una notifica? Dubbio aperto (📄 T5, DL-8).

**Semi di user story** 🧩
1. Il Banco invia una comunicazione, con allegati, a tutte le OPT o a un sottogruppo.
2. L'OPT legge la comunicazione e conferma la ricezione.
3. Il Banco vede quali OPT hanno confermato.

**Punti aperti.** Tipi di comunicazione, canali, formato degli allegati (Q-08).
**Collegamenti.** 📘 R §5.4, BA · Q-08.

### EP-07 — Monitoraggio trimestrale (scheda degli operatori)

**Scopo.** Gli operatori inviano al Banco la scheda del trimestre; il Banco la raccoglie per la rendicontazione al ministero.
**Attori.** Operatore, Banco.

**Cosa è emerso**
- La scheda di monitoraggio la **invia l'operatore interno**: su questo «non ci piove» (📄 T3). **Il Banco la raccoglie**, non la manda: per questo non è una responsabilità del Banco nel diagramma (📄 T3).
- **Operatori esterni:** se debbano mandare la scheda è **controverso**. Chi dice sì: è l'unico modo per avere la tracciabilità delle persone e il ministero usa i dati per analisi (📄 T1). Chi dice no: gli esterni sono entità assistenti che caricano i report da soli sul portale ministeriale (📄 T1). Le OPT che fanno capo direttamente al ministero non rendicontano (📄 T1). 📘 BA: gli operatori **delle OPT** non danno la scheda.
- **Rischio di duplicati:** se un operatore è associato a un'OPT e rendiconta l'OPT, la scheda dell'operatore duplica le informazioni al ministero (📄 T5).
- La scheda può includere attività svolte **fuori da PICUS** (📘 R §5.5): ❓ perdiamo le prestazioni che le OPT erogano senza passare dal Banco? Il direttore ne ha parlato solo per gli operatori che passano dal Banco (📄 T3).

**Semi di user story** 🧩
1. L'operatore compila la scheda del trimestre.
2. L'operatore invia la scheda al Banco.
3. Il Banco consulta le schede ricevute e sa chi non l'ha ancora inviata.
4. Il Banco esporta i dati per l'inserimento nel portale ministeriale.
5. Il sistema controlla la coerenza dei dati della scheda (regole da chiarire).

**Punti aperti.** Gli operatori esterni devono rendicontare (DL-2); chi inserisce i dati se l'attività è svolta da un'OPT (Q-21); regole di validazione (Q-06).
**Collegamenti.** 📘 R §5.5, App. B, BA · Q-06, Q-11, Q-21.

## 4. Cosa è stato fissato in aula e cosa no

| | Punto | Fonte |
|---|---|---|
| ✅ fissato | le richieste passano **sempre dal Banco**; le OPT non si parlano | 📄 T1 |
| ✅ fissato | l'assegnazione finale la fa **un operatore del Banco** | 📄 T1 |
| ✅ fissato | **non si pubblicano disponibilità** nel sistema | 📄 T1, T3 |
| ✅ fissato | la gestione interna delle OPT è una **black box** | 📄 T1 |
| ✅ fissato | il Banco **assegna le credenziali** (OPT e operatori); non c'è auto-registrazione | 📄 T3 |
| ✅ fissato | l'**operatore interno invia la scheda** trimestrale | 📄 T3 |
| 🟡 da validare | suggerimento dei candidati e richiesta di disponibilità automatica come **proposta** al committente | 📄 T1 |
| 🟡 da validare | regola «nulla è confermato fino all'assegnazione» e disponibilità trattenuta per un massimo di ~2 ore | 📄 T1 |
| ❓ aperto | ordine di ricerca; uno alla volta o in parallelo; chi riceve la richiesta di appuntamento; operatori esterni (registrazione, scheda); dati quantitativi delle OPT; comunicazioni agli operatori | 📄 T1, T3, T5 |

## 5. Lasciato volutamente fuori

- **Disponibilità** delle OPT nel sistema (vincolo del direttore).
- **Dati sull'attività «normale» dell'OPT** (catechismo, parrocchia): tolti finché non c'è conferma (📄 T3).
- **Gestione degli operatori interni alle OPT** (black box).
- **Beneficiari come utenti**: restano non utenti (📘 R §2–§3).
- **Amministrazione e reporting**: l'attività 4 li cita ([[00-Presentazione Progetto Picus.pdf#page=21]]) ma la lezione non li ha trattati ❓. 🧩 Potrebbero diventare una **EP-08** (vista complessiva del Banco, storico e tracciabilità, esportazioni) se il team li ritiene distinti da EP-04 e EP-07.

## 6. Contraddizioni con le fonti già nel wiki

> ⚠️ **Contraddizione 1 — dati quantitativi dell'OPT.** I desiderata li prevedono ([[guida-progetto-picus]] § 4.5, R §5.2) e il Context Diagram del gruppo ha l'arco «dati quantitativi» dall'OPT ([[a2-stakeholder-e-contesto]]); in aula si è ricordato che per il direttore l'OPT **non deve comunicare niente** (esempio «60 famiglie / 70 famiglie») e si è tolto il caso d'uso (📄 T3). Va chiesto, poi allineato A2 o questa epic (Q-21 è affine).

> ⚠️ **Contraddizione 2 — operatori delle OPT.** In aula il direttore ha scritto che gli operatori sono di **tre tipi** (Banco, esterni, appartenenti alle OPT) e si è discusso se registrarli; 📘 BA dice che gli operatori **delle OPT** non sono utenti e il Banco non comunica con loro. Le due cose sono compatibili solo se «operatore appartenente all'OPT» e «operatore messo a disposizione presso l'OPT» (📄 T3) sono figure diverse ❓ (DL-1).

> ⚠️ **Contraddizione 3 — tempi di risposta.** Il direttore ha escluso timeout e notifiche (sezione pendenti, 📄 T1); la proposta del gruppo prevede una disponibilità trattenuta per un massimo di ~2 ore e annullamenti automatici. È una **proposta migliorativa**, non un requisito: va presentata come opzionale.

> ⚠️ **Contraddizione 4 — ricerca in parallelo.** Secondo Alberto il committente vuole assegnare un'OPT alla volta; la proposta è chiedere la disponibilità a 4–5 OPT insieme (📄 T1). Si concilia solo se il Banco **sceglie lui** chi assegnare dopo aver ricevuto le disponibilità.

## 7. Dubbi emersi in aula (da portare al direttore)

I dubbi sono stati raccolti da Ilaria per essere inviati al direttore (📄 T5). **DL-n** sono etichette di questa pagina; la colonna «Q» indica la domanda già in [[domande-al-committente]] a cui sono vicine.

| # | Dubbio | Q affine | Epic |
|---|---|---|---|
| DL-1 | **Quali tipi di operatori esistono** (interni al Banco, esterni, appartenenti all'OPT), cosa può fare ciascuno e che rapporto hanno; **quali devono registrarsi** | Q-09, Q-15 | EP-01, EP-05 |
| DL-2 | L'**operatore esterno** deve rendicontare (scheda trimestrale)? A chi? | Q-06, Q-21 | EP-07 |
| DL-3 | L'**OPT deve comunicare quanti servizi offre / il suo carico**? | Q-21 | EP-02 |
| DL-4 | **Come contatta il Banco un operatore esterno** se non è registrato? Serve un elenco di pre-registrati? | — nuova | EP-05 |
| DL-5 | **Priorità nella ricerca** dell'erogatore (OPT vicine, esterni, interni), eventualmente per tipo di misura | Q-03 | EP-04 |
| DL-6 | Richiesta **a più OPT insieme o una alla volta**? Per il direttore la conferma finale resta al Banco? | Q-03, Q-04 | EP-04 |
| DL-7 | **Che margine** abbiamo di proporre funzioni nuove sugli operatori, in particolare interni alle OPT? | Q-19 | EP-01, EP-05 |
| DL-8 | Le **comunicazioni** vanno solo all'OPT (intermediario) o anche agli operatori con un account? | Q-08 | EP-06 |
| DL-9 | Se un operatore è **associato a un'OPT**, la sua scheda duplica quella dell'OPT? Un operatore può rispondere sia al Banco sia all'OPT? | Q-21 | EP-07 |

> 🧩 DL-4 è l'unico senza un Q-n corrispondente: se il team è d'accordo si può aggiungere come **Q-22** a [[domande-al-committente]].

## 8. Come procedere

1. **Allineare le epic** con il team: si fondono, si dividono, si rinominano (per i vincoli: **5–8**). Dare **ID stabili** (EP-01…) per la tracciabilità desiderata → epic → storia → criteri di accettazione (📘 AGENTS.md §9, [[guida-progetto-picus]] § 6.7).
2. **Scrivere le storie** dai «semi», nel formato *As a [ruolo], I want [obiettivo], so that [beneficio]*, con ID, epic, stakeholder, priorità e criteri di accettazione; controllare **INVEST** e dividere quelle troppo grandi ([[valutare-user-stories-invest]], [[criteri-di-accettazione-e-bdd]]).
3. **Marcare «da approfondire»** le storie che dipendono dai dubbi DL-1…DL-9, invece di inventare un comportamento.
4. **Candidati all'MVP** 🧩: un flusso end-to-end minimo (EP-01 → EP-03 → EP-04 → EP-05) con l'assegnazione manuale del Banco; le parti «proposta» di EP-04 e EP-02 (profilo) come incrementi successivi.

> 🧩 Distribuzione indicativa dei semi sopra: EP-01 (5), EP-02 (5), EP-03 (4), EP-04 (7), EP-05 (5), EP-06 (3), EP-07 (5) = **34 semi**: più delle 15–25 storie richieste, quindi alcuni vanno fusi o rimandati (per esempio la notifica in EP-03, il recupero credenziali in EP-01, il controllo di coerenza in EP-07).

## Fonti

- [[trascrizione-lezione-progetto-1]] — trascrizione della lezione (T1–T5)
- [[guida-progetto-picus]] § 4.5 (desiderata), § 5.2 (attività 4), § 6.5–6.7 (regole del team) · [[incontro-stakeholder-ba]] · [[domande-al-committente]] · [[a2-stakeholder-e-contesto]]
- [[00-Presentazione Progetto Picus.pdf#page=21]] — attività 4: individuare le funzionalità principali

_Aggiornato: 2026-10-24 — prima stesura dalla trascrizione_
