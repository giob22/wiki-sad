---
tipo: progetto-strumento
stato: bozza non testata su un project reale
data: 2026-10-18
---

# Burndown dello sprint sul GitHub Project

Come mostrare l'avanzamento di uno sprint nel project **Progetto-SAD** (project dell'organizzazione `Pinguini-alla-Fragola`; viste *Sprint 1 - Preparazione*, *Current iteration*, ecc.), pesando i task con la loro taglia. Il codice vive nel repository del team: qui ci sono i file da copiare e le spiegazioni.

> 🧩 Elaborazione mia: nelle fonti del corso non c'è nulla su GitHub Projects. Il concetto di burndown è nella Lezione 6 → [[cerimonie-e-artefatti-agile]] (burndown chart: asse = lavoro rimanente nello sprint, linea ideale retta, tratti piatti = giorni senza storie chiuse).

## Cosa si ottiene

![[esempio-burndown-demo.svg]]
*🧩 Grafico di esempio prodotto da [[burndown.py]] con dati finti (`--demo`; anteprima raster: [[esempio-burndown-demo.png]]): sprint di 21 giorni, 10 task, 5 punti aggiunti a sprint iniziato. **Quattro riquadri**: punti rimanenti, completati su totale (con la percentuale), giorni rimasti, stato («In ritardo / In anticipo / In linea» e di quanti punti rispetto alla linea ideale). **Grafico**: linea grigia tratteggiata = ideale, dal totale iniziale a 0 alla fine dell'iterazione; linea blu = punti rimanenti, che scende quando un task passa a Done, della sua taglia, e sale se si aggiungono task a sprint iniziato; **area rosa** = scostamento in ritardo rispetto all'ideale, **area azzurra** = in anticipo (come nel grafico della docente, [[04_Agile_01_bis.pdf#page=31]]); linea rossa «OGGI»; linea arancione = **previsione** a fine sprint continuando al ritmo attuale. A sprint concluso i riquadri passano a «Concluso» e la previsione sparisce.*

## Come funziona il calcolo

Per ogni mezzanotte dello sprint, più «adesso» se lo sprint è in corso:

$$
\text{rimanenti}(t) = \underbrace{\sum_{\text{task aggiunti entro } t} p_i}_{\text{scope}(t)} \;-\; \underbrace{\sum_{\text{task Done entro } t} p_i}_{\text{completati}(t)}
$$

dove $p_i$ sono i **punti** del task $i$. La linea ideale parte da $\text{scope}(\text{inizio})$ e arriva a 0 alla data di fine (inizio + durata dell'iterazione).

| Dato | Da dove viene |
|---|---|
| Task dello sprint | item del project con il campo **Iteration** uguale all'iterazione scelta (di default quella in corso oggi) |
| Inizio e durata | dal campo Iteration (data di inizio e durata in giorni) |
| Punti del task | campo **Number** `Estimate` (stima del task nel project) se compilato; altrimenti la **taglia** del campo `Size` tramite la mappatura `XS=1, S=2, M=3, L=5, XL=8` in [[burndown.py]]; altrimenti 1 |
| «Fatto» | `Status = Done` |
| Data di completamento | `closedAt` dell'issue; se manca, ultimo aggiornamento dell'item |
| Data di aggiunta | data in cui l'item è stato aggiunto al project. I task aggiunti **nel primo giorno** dello sprint (la planning) contano come scope **iniziale**; solo quelli aggiunti dopo sono un aumento di perimetro |

> ⚖️ Trade-off: la **mappatura delle taglie in punti è una scelta del team** (qui una scala tipo Fibonacci: i task grandi pesano più che proporzionalmente perché sono più incerti). Cambiarla cambia la pendenza di ogni gradino, non la forma del grafico.

## Quale campo usare per le stime

Nel project e nelle issue ci sono più campi che sembrano fare la stessa cosa:

| Campo | Tipo | Valori | Adatto alla pendenza? |
|---|---|---|---|
| **Estimate** (nel project) | **numero** | libero | **sì, è la scelta consigliata**: già numerico, nessuna mappatura, sommabile anche da Insights |
| **Size** (nel project) | selezione singola | XS, S, M, L, XL | ripiego: serve la mappatura in punti (XS=1 … XL=8) |
| **Effort** (campo delle issue) | selezione singola | Low, Medium, High | **no**: solo 3 livelli, i gradini sarebbero quasi tutti uguali; inoltre è un campo dell'issue e non del project, che lo script non legge |

> 🧩 Elaborazione mia: conviene concordare nel team una **scala unica** per Estimate, per esempio 1, 2, 3, 5, 8 (stile Fibonacci). Un task da più di 8 va **spezzato**: è il criterio *Small* di INVEST ([[valutare-user-stories-invest]]). Non mescolate Estimate e Size nello stesso sprint: lo script usa Estimate quando c'è e Size solo se manca, e un task senza nessuno dei due vale **1 punto**, quindi distorce il grafico. `--inspect` segnala quanti task sono senza stima.

> ⚠️ **Durata di S1 nel project:** la scheda di un'issue mostra l'iterazione *S1 - Preparazione* come «Oct 15 – Nov 3». Se l'interfaccia mostra la data finale inclusa, sono **20 giorni**, mentre il piano della docente prevede 3 settimane, cioè **21 giorni**, con review il 5/11 ([[00-Presentazione Progetto Picus.pdf#page=12]]). `--inspect` stampa i giorni e li confronta con il piano: se segnala «ATTENZIONE», correggete la durata nelle impostazioni del campo Iteration.

## Adattamenti al vostro project

Dalla schermata del board:

- **Colonne di Status:** Backlog, Ready, In progress, In review, Done. Lo script considera fatto solo `Done` (descritto nel board come «lavoro completato e verificato»).
- **Workflows (7):** nel menu *Workflows* del project verificate che **Item closed → Status = Done** sia attivo. Se Done e «issue chiusa» non coincidono, le date di completamento diventano approssimate (ultimo aggiornamento).
- **Durata dell'iterazione:** la preparatoria è un'eccezione di **3 settimane** (15/10–5/11, [[00-Presentazione Progetto Picus.pdf#page=12]]), le altre iterazioni sono di 2: vedi la tabella nella sezione «Più sprint». La linea ideale usa la durata che trova nel campo Iteration.
- **Una iterazione per sprint:** lo script sceglie da solo l'iterazione che contiene la data di oggi. Per rigenerare uno sprint passato impostate `ITERATION_TITLE`, ma ricordate che i task spostati altrove non compaiono più.
- **Task che escono dall'iterazione:** un item spostato in un'altra iterazione sparisce dalla serie anche nel passato: il grafico è fedele per i task che restano nello sprint.
- **Campo Size:** non è visibile sulle card; è il ripiego se un task non ha Estimate. Se i valori non sono XS/S/M/L/XL, modificate `SIZE_POINTS`. Il campo preferito è **Estimate** (Number); il nome si cambia con `POINTS_FIELD`.

## Più sprint: board diverse, durate diverse, chiusura

Le **board** (le viste con il filtro `iteration:"S1 - Preparazione"`) non influiscono: lo script legge i dati dal campo **Iteration** degli item, non dalle viste. Quando create la board del nuovo sprint non dovete cambiare nulla nello script.

**Durate.** Ogni iterazione ha la **sua** data di inizio e la sua durata nel campo Iteration. Impostatele come nel piano del progetto ([[00-Presentazione Progetto Picus.pdf#page=11]], [[00-Presentazione Progetto Picus.pdf#page=12]]):

| Sprint | Inizio | Durata | Fine (esclusa) | Review |
|---|---|---|---|---|
| S1 - Preparazione | 15/10/2026 | **21 giorni** (3 settimane, eccezione) | 05/11/2026 | 05/11 |
| Costruzione 1 | 05/11/2026 | 14 giorni | 19/11/2026 | 19/11 |
| Costruzione 2 | 19/11/2026 | 14 giorni | 03/12/2026 | 03/12 |
| Costruzione 3 | 03/12/2026 | 14 giorni | 17/12/2026 | 17/12 |

> 🧩 I titoli delle iterazioni successive alla prima sono un esempio: usate quelli che avete in GitHub. Contano le **date** e le **durate**.

`--inspect` confronta le iterazioni trovate con questo piano e segnala con «ATTENZIONE» una durata o una data di inizio diverse (per esempio S1 impostata a 14 giorni).

**Chiusura dello sprint.**
- Il workflow scrive **solo l'iterazione in corso**. I file degli sprint finiti restano com'erano: un file per sprint (`burndown-s1-preparazione.svg`, poi quello dello sprint dopo, ecc.), conservati sul branch `burndown-data`.
- Questo evita un problema: i task **non finiti**, spostati nello sprint successivo, cambiano iterazione e, se lo sprint fosse ricalcolato dopo, **sparirebbero** dalla sua storia. Così il grafico dello sprint chiuso resta quello vero.
- L'ultimo aggiornamento dello sprint avviene alle **23:50 UTC dell'ultimo giorno** (data di fine esclusa meno un giorno, es. 4/11 per S1). Se spostate i task non finiti **prima** di quell'ora, o lavorate fino a tardi, lanciate a mano il workflow con il titolo dell'iterazione nel campo *iteration_title* **prima** di spostarli.
- Lo sprint successivo parte alla data di fine del precedente: da quel giorno lo script sceglie da solo la nuova iterazione.

> ⚠️ Limite: un task già nel project ma assegnato all'iterazione **dopo** l'inizio dello sprint risulta, per lo script, presente fin dall'inizio: **non** compare come aumento di perimetro (cioè come salita dello scope). Compaiono come aumento solo i task **aggiunti al project** durante lo sprint.

## Attivarlo su GitHub: workflow e README

**Idea.** `main` è protetto ([[AGENTS]] §7), quindi il workflow **non riscrive il README**. Il README contiene un'immagine con un indirizzo **fisso**; il workflow sovrascrive ogni sera il file a quell'indirizzo, sul branch `burndown-data`, con il grafico dello sprint in corso. Così il README mostra sempre l'ultimo sprint senza nessuna modifica a `main`.

Il workflow ([[burndown.yml]]) fa, ogni giorno alle 23:50 UTC e a richiesta:
1. legge il project con il token;
2. calcola il burndown dello sprint in corso con [[burndown.py]];
3. pubblica sul branch `burndown-data`: **`burndown-latest.svg`** (usato dal README), un `burndown-<sprint>.svg` e `.csv` per ogni sprint, conservati per lo storico;
4. salva gli stessi file come artefatto dell'esecuzione.

### Passi, in ordine

1. **Token.** Su GitHub: *Settings → Developer settings → Personal access tokens → Tokens (classic)*, scope `project` e `repo`. Metti una **scadenza dopo il 17/12/2026**: a token scaduto il workflow smette di aggiornare il grafico senza avvisi evidenti.
2. **Secret e variabile** nel repository *Progetto-SAD*, in *Settings → Secrets and variables → Actions*:
   - scheda *Secrets* → nuovo secret `PROJECT_TOKEN` con il token;
   - scheda *Variables* → nuova variabile `PROJECT_NUMBER` con il numero del project.
3. **File nel repository**, su un branch dedicato (regola del team: un branch per attività, Conventional Commits, niente push su `main`):

   | File | Contenuto |
   |---|---|
   | `scripts/burndown.py` | copia di [[burndown.py]] |
   | `.github/workflows/burndown.yml` | copia di [[burndown.yml]] |
   | `README.md` | il blocco del punto 5, **per ultimo** |

   Per esempio branch `feat/burndown-sprint`, commit `feat(ci): aggiungi il burndown dello sprint`, poi pull request verso `main`. Il workflow pianificato parte **solo dopo il merge** perché le esecuzioni programmate usano il file presente sul branch predefinito.
4. **Prima esecuzione a mano, prima di inserire l'immagine nel README:** scheda *Actions* → *burndown* → *Run workflow*. A fine esecuzione devono esistere il branch `burndown-data` e il file `burndown-latest.svg`. Se il run fallisce, il log del passo «Calcola il burndown» dice perché (stessi sintomi della tabella più sotto).
5. **README.** Nel punto che preferite, un blocco con delimitatori, così il posto resta riconoscibile:

```markdown
<!-- BURNDOWN:START — grafico dello sprint in corso, aggiornato ogni sera dal workflow "burndown"; non modificare il link -->
## Avanzamento dello sprint

![Burndown dello sprint in corso](https://github.com/Pinguini-alla-Fragola/Progetto-SAD/raw/burndown-data/burndown-latest.svg)

*Aggiornato ogni sera. Gli sprint precedenti sono nel branch [`burndown-data`](https://github.com/Pinguini-alla-Fragola/Progetto-SAD/tree/burndown-data).*
<!-- BURNDOWN:END -->
```

   🧩 Repository e **project** sono dell'organizzazione `Pinguini-alla-Fragola`: nel workflow `PROJECT_OWNER` e `OWNER_TYPE` valgono di default `Pinguini-alla-Fragola` e `organization`, e si possono cambiare con le variabili di repository omonime senza toccare il file. Un project **personale** ha invece `OWNER_TYPE=user` e il login dell'utente.

### Cosa succede a ogni cambio di sprint

- Dalla data di inizio del nuovo sprint lo script sceglie la nuova iterazione, e `burndown-latest.svg` passa a mostrarla: il README cambia da solo.
- Il file dello sprint concluso resta nel branch come `burndown-<sprint>.svg`, fissato all'ultimo aggiornamento (vedi «Chiusura dello sprint»).
- Nei primissimi giorni di uno sprint il grafico ha pochi punti e la previsione è poco affidabile.

> ⚠️ **Da verificare al primo giro.** Se il repository è **privato**, l'immagine nel README si vede **a chi ha accesso** al repository ed è collegato a GitHub nel browser, ma non l'ho potuto provare. Il link `.../raw/burndown-data/...` viene reindirizzato con un permesso temporaneo. Se invece l'immagine non compare, scegliete una di queste strade:
> 1. un link cliccabile al file sul branch `burndown-data` al posto dell'immagine (si apre il grafico, ma non è incorporato);
> 2. una versione PNG al posto dell'SVG (l'SVG è il formato più delicato con le immagini esterne): richiede una piccola modifica allo script;
> 3. far aggiornare al workflow un blocco del README direttamente su `main`, permesso solo se i branch protetti lo consentono al bot e se il team lo accetta.
>
> Il browser può tenere in cache il grafico per qualche minuto dopo l'aggiornamento.

> ⚠️ Repository di un'**organizzazione**: se il primo run risponde che l'organizzazione non consente l'accesso con un token personale **classico**, un owner dell'organizzazione deve consentirlo in *Organization settings → Personal access tokens* (criteri per i token). Se l'organizzazione usa il single sign-on, il token va anche **autorizzato** per l'organizzazione dalla pagina dei token.

> ⚠️ Limiti da conoscere: se una regola dei branch del repository si applica a **tutti** i branch, il push su `burndown-data` fallisce; se in *Settings → Actions → General* i permessi del workflow sono bloccati in sola lettura da una regola dell'organizzazione, `permissions: contents: write` nel file può non bastare. Il token non va mai scritto nel codice ([[AGENTS]] §3: niente credenziali nel codice).

Prova in locale **senza API** (per vedere il grafico di esempio; per i dati reali vedi la sezione successiva):

```bash
python progetto/burndown/burndown.py --demo
```

## Provarlo in locale con dati reali (senza Actions)

Basta l'API: lo script gira sul tuo PC e legge il project con un token. Nessun workflow, nessun commit.

1. **Token.** Ottienilo in uno di questi due modi:
   - con la GitHub CLI già installata: `gh auth refresh -s read:project -s repo` e poi `gh auth token`;
   - oppure da *Settings → Developer settings → Personal access tokens (classic)*, con scope `read:project` e `repo`.
2. **Numero del project:** nell'URL `github.com/orgs/Pinguini-alla-Fragola/projects/<numero>`; oppure `gh project list --owner Pinguini-alla-Fragola` (per un project personale: `--owner <utente>`).
3. **Variabili d'ambiente** (PowerShell), poi **controllo dei campi**:

```powershell
$env:PROJECT_TOKEN  = (gh auth token)     # oppure il token incollato qui, solo in questa finestra
$env:PROJECT_OWNER  = "Pinguini-alla-Fragola"
$env:OWNER_TYPE     = "organization"
$env:PROJECT_NUMBER = "<numero>"
py -3.11 progetto/burndown/burndown.py --inspect
```

   `--inspect` stampa il project, il numero di item e, per ogni campo trovato, i suoi valori: devono comparire **Status** (con Done), **Iteration** (con *S1 - Preparazione* e i suoi giorni) e, se c'è, **Size**. Se un nome è diverso, impostalo con `ITERATION_FIELD`, `STATUS_FIELD`, `SIZE_FIELD`, `DONE_VALUE`.
4. **Grafico reale:** stesso comando senza `--inspect`, con `OUT_DIR` per scegliere dove scrivere.

```powershell
$env:OUT_DIR = "out"
py -3.11 progetto/burndown/burndown.py
```

   Compare `out/burndown-s1-preparazione.svg` (aprilo nel browser) e il `.csv` con i numeri giorno per giorno.

| Sintomo | Causa probabile |
|---|---|
| `INSUFFICIENT_SCOPES` | al token manca `read:project` |
| `Could not resolve to a User` | `PROJECT_OWNER` sbagliato, o project di un'organizzazione (`OWNER_TYPE=organization`) |
| `Iterazione … non trovata` | nome del campo Iteration diverso (`ITERATION_FIELD`) o titolo diverso (`ITERATION_TITLE`) |
| 0 task o tutti da 1 punto | nome o valori di Status/Size diversi: guarda l'output di `--inspect` |
| gradini nei giorni sbagliati | Done non coincide con «issue chiusa» (vedi Workflows del project) |

> ⚠️ Il token è una credenziale: tienilo solo nella variabile d'ambiente della finestra, non nei file, non in chat, non nei commit.

## Varianti grafiche provate

Scelta del team: variante **B (dashboard)** con l'**area colorata della A (stile docente)**, ora in [[burndown.py]]. Le quattro proposte iniziali, su dati simulati e generate da [[genera_varianti_grafico.py]], restano come archivio:

| Variante | Idea |
|---|---|
| **A — stile docente** ![[A-stile-docente.png]] | più vicina alla slide: area rosa «in ritardo», azzurra «in anticipo», annotazione dell'ambito modificato |
| **B — dashboard** ![[B-dashboard.png]] | quattro riquadri e **previsione a fine sprint** (scelta) |
| **C — scuro** ![[C-scuro.png]] | tema scuro, numero grande dei punti rimanenti |
| **D — task e ritmo** ![[D-task-e-ritmo.png]] | gradini veri con etichette dei task e punti completati al giorno |

Sorgenti vettoriali (SVG): [[A-stile-docente.svg]], [[B-dashboard.svg]], [[C-scuro.svg]], [[D-task-e-ritmo.svg]].

> 🧩 Non è nel grafico finale la linea dello **scope** (totale assegnato) della variante A: l'aumento di perimetro si legge dal totale nel riquadro «Completati» (es. 21 / 36) e dalla salita della linea blu. Si può riaggiungere.

## Alternative

- **Grafico nativo (Insights):** è un burn-up che conta gli item nel tempo; con il campo Number `Estimate` si può provare a sommarlo sull'asse Y. Nessun burndown nativo.
- **Strumento esterno:** Screenful offre un burndown per GitHub Projects con campi numerici e linea attesa.

_Aggiornato: 2026-10-18 — prima stesura_
_Aggiornato: 2026-10-18 — più sprint, durate 21/14 giorni, chiusura dello sprint
_Aggiornato: 2026-10-18 — design scelto: dashboard con area colorata
_Aggiornato: 2026-10-18 — workflow completo e posizione nel README (burndown-latest.svg)
_Aggiornato: 2026-10-18 — repository dell'organizzazione Pinguini-alla-Fragola
_Aggiornato: 2026-10-19 — project dell'organizzazione (owner e tipo configurabili)_
