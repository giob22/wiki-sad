---
tipo: progetto-strumento
stato: bozza non testata su un project reale
data: 2026-10-18
---

# Burndown dello sprint sul GitHub Project

Come mostrare l'avanzamento di uno sprint nel project **Progetto-SAD** (utente `CapHello`, viste *Sprint 1 - Preparazione*, *Current iteration*, ecc.), pesando i task con la loro taglia. Il codice vive nel repository del team: qui ci sono i file da copiare e le spiegazioni.

> 🧩 Elaborazione mia: nelle fonti del corso non c'è nulla su GitHub Projects. Il concetto di burndown è nella Lezione 6 → [[cerimonie-e-artefatti-agile]] (burndown chart: asse = lavoro rimanente nello sprint, linea ideale retta, tratti piatti = giorni senza storie chiuse).

## Cosa si ottiene

![[esempio-burndown-demo.svg]]
*🧩 Grafico di esempio prodotto da [[burndown.py]] con dati finti (`--demo`: 10 task da 2–5 punti, due aggiunti a sprint iniziato). **Linea grigia tratteggiata** = ideale, dal totale iniziale a 0 alla fine dell'iterazione. **Linea blu** = punti rimanenti: scende a gradini quando un task passa a Done, della taglia del task, e **sale** quando si aggiungono task a sprint iniziato. **Linea arancione** = totale assegnato (scope): è la variazione di perimetro. Il tratto piatto tra il 15/10 e il 20/10 significa nessun task chiuso in quei giorni.*

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
| Punti del task | campo **Number** `Punti` se esiste; altrimenti la **taglia** del campo `Size` tramite la mappatura `XS=1, S=2, M=3, L=5, XL=8` in [[burndown.py]]; altrimenti 1 |
| «Fatto» | `Status = Done` |
| Data di completamento | `closedAt` dell'issue; se manca, ultimo aggiornamento dell'item |
| Data di aggiunta | data in cui l'item è stato aggiunto al project |

> ⚖️ Trade-off: la **mappatura delle taglie in punti è una scelta del team** (qui una scala tipo Fibonacci: i task grandi pesano più che proporzionalmente perché sono più incerti). Cambiarla cambia la pendenza di ogni gradino, non la forma del grafico.

## Adattamenti al vostro project

Dalla schermata del board:

- **Colonne di Status:** Backlog, Ready, In progress, In review, Done. Lo script considera fatto solo `Done` (descritto nel board come «lavoro completato e verificato»).
- **Workflows (7):** nel menu *Workflows* del project verificate che **Item closed → Status = Done** sia attivo. Se Done e «issue chiusa» non coincidono, le date di completamento diventano approssimate (ultimo aggiornamento).
- **Durata dell'iterazione:** la preparatoria è un'eccezione di **3 settimane** (15/10–5/11, [[00-Presentazione Progetto Picus.pdf#page=12]]), le altre iterazioni sono di 2: vedi la tabella nella sezione «Più sprint». La linea ideale usa la durata che trova nel campo Iteration.
- **Una iterazione per sprint:** lo script sceglie da solo l'iterazione che contiene la data di oggi. Per rigenerare uno sprint passato impostate `ITERATION_TITLE`, ma ricordate che i task spostati altrove non compaiono più.
- **Task che escono dall'iterazione:** un item spostato in un'altra iterazione sparisce dalla serie anche nel passato: il grafico è fedele per i task che restano nello sprint.
- **Campo Size:** non è visibile sulle card. Se i valori non sono XS/S/M/L/XL, modificate `SIZE_POINTS`. Se preferite un campo Number, create `Punti` (nome configurabile con `POINTS_FIELD`).

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

## Passi per attivarlo (nel repository del progetto)

1. Copiare [[burndown.py]] in `scripts/burndown.py` e [[burndown.yml]] in `.github/workflows/burndown.yml`.
2. Creare un token personale **classico** con scope `project` e `repo` e salvarlo come secret `PROJECT_TOKEN`. Il `GITHUB_TOKEN` di Actions non basta per leggere un project di un utente.
3. Salvare come variabile di repository `PROJECT_NUMBER` il numero del project (dall'URL `.../projects/<numero>`).
4. Lanciare il workflow a mano con *Run workflow* e controllare il risultato.
5. I file `burndown-<iterazione>.svg` e `.csv` finiscono come artefatto e sul branch **`burndown-data`**, non su `main`, perché in `AGENTS.md` i branch principali sono protetti (§7). Aprire l'SVG su GitHub per vederlo.

Prova in locale **senza API** (per vedere il grafico di esempio; per i dati reali vedi la sezione successiva):

```bash
python output/burndown/burndown.py --demo
```

> ⚠️ **Non testato su un project reale:** ho provato solo il calcolo e il grafico con dati finti. Il collegamento con l'API GraphQL e il workflow vanno verificati la prima volta. Il token non deve mai essere scritto nel codice ([[AGENTS]] §3: niente credenziali nel codice).

## Provarlo in locale con dati reali (senza Actions)

Basta l'API: lo script gira sul tuo PC e legge il project con un token. Nessun workflow, nessun commit.

1. **Token.** Ottienilo in uno di questi due modi:
   - con la GitHub CLI già installata: `gh auth refresh -s read:project -s repo` e poi `gh auth token`;
   - oppure da *Settings → Developer settings → Personal access tokens (classic)*, con scope `read:project` e `repo`.
2. **Numero del project:** nell'URL `github.com/users/CapHello/projects/<numero>`.
3. **Variabili d'ambiente** (PowerShell), poi **controllo dei campi**:

```powershell
$env:PROJECT_TOKEN  = (gh auth token)     # oppure il token incollato qui, solo in questa finestra
$env:PROJECT_OWNER  = "CapHello"
$env:PROJECT_NUMBER = "<numero>"
py -3.11 output/burndown/burndown.py --inspect
```

   `--inspect` stampa il project, il numero di item e, per ogni campo trovato, i suoi valori: devono comparire **Status** (con Done), **Iteration** (con *S1 - Preparazione* e i suoi giorni) e, se c'è, **Size**. Se un nome è diverso, impostalo con `ITERATION_FIELD`, `STATUS_FIELD`, `SIZE_FIELD`, `DONE_VALUE`.
4. **Grafico reale:** stesso comando senza `--inspect`, con `OUT_DIR` per scegliere dove scrivere.

```powershell
$env:OUT_DIR = "out"
py -3.11 output/burndown/burndown.py
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

## Varianti grafiche (da scegliere)

La prima versione del grafico è molto essenziale. Quattro proposte con **dati simulati**, generate da [[genera_varianti_grafico.py]]. Il modello è il grafico della docente ([[04_Agile_01.pdf#page=31]]: griglia, linea ideale puntinata, linea reale viola, area colorata tra reale e ideale, linea dello scope con «salto» annotato).

| Variante | Idea | Punti di forza |
|---|---|---|
| **A — stile docente** | ![[A-stile-docente.png]] | più vicina alla slide: area rosa «in ritardo», azzurra «in anticipo», annotazione dell'ambito modificato |
| **B — dashboard** | ![[B-dashboard.png]] | quattro riquadri (rimanenti, completati, giorni rimasti, stato) e **previsione a fine sprint** al ritmo attuale |
| **C — scuro** | ![[C-scuro.png]] | tema scuro, numero grande dei punti rimanenti, aumenti di scope etichettati |
| **D — task e ritmo** | ![[D-task-e-ritmo.png]] | **gradini veri**: ogni task chiuso è un'etichetta con i suoi punti; sotto, i punti completati al giorno |

*🧩 Tutte le varianti mostrano la stessa simulazione: sprint S1 di 21 giorni, 31 punti iniziali, 5 aggiunti in corso, 21 completati al 30/10. Con questi numeri lo sprint risulta in ritardo di circa 7 punti rispetto all'ideale e il ritmo di 1,4 punti al giorno porterebbe a chiudere con circa 8 punti non completati (previsione nella B: è una proiezione lineare, non una promessa).*

Sorgenti vettoriali (SVG, modificabili): [[A-stile-docente.svg]], [[B-dashboard.svg]], [[C-scuro.svg]], [[D-task-e-ritmo.svg]].

Dopo la scelta, il design viene portato in [[burndown.py]], al posto del grafico attuale, e nel workflow.

## Alternative

- **Grafico nativo (Insights):** è un burn-up che conta gli item nel tempo; con un campo Number `Punti` si può provare a sommarlo sull'asse Y. Nessun burndown nativo.
- **Strumento esterno:** Screenful offre un burndown per GitHub Projects con campi numerici e linea attesa.

_Aggiornato: 2026-10-18 — prima stesura_
_Aggiornato: 2026-10-18 — più sprint, durate 21/14 giorni, chiusura dello sprint_
