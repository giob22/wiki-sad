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
- **Durata dell'iterazione:** la preparatoria è un'eccezione di **3 settimane** (15/10–5/11, [[00-Presentazione Progetto Picus.pdf#page=12]]), le altre iterazioni sono di 2. Controllate nelle impostazioni del campo Iteration che *S1 - Preparazione* abbia **21 giorni**: la linea ideale si basa su quella durata.
- **Una iterazione per sprint:** così com'è, lo script sceglie da solo l'iterazione che contiene la data di oggi. Per vedere uno sprint passato impostate `ITERATION_TITLE`.
- **Task che escono dall'iterazione:** un item spostato in un'altra iterazione sparisce dalla serie anche nel passato: il grafico è fedele per i task che restano nello sprint.
- **Campo Size:** non è visibile sulle card. Se i valori non sono XS/S/M/L/XL, modificate `SIZE_POINTS`. Se preferite un campo Number, create `Punti` (nome configurabile con `POINTS_FIELD`).

## Passi per attivarlo (nel repository del progetto)

1. Copiare [[burndown.py]] in `scripts/burndown.py` e [[burndown.yml]] in `.github/workflows/burndown.yml`.
2. Creare un token personale **classico** con scope `project` e `repo` e salvarlo come secret `PROJECT_TOKEN`. Il `GITHUB_TOKEN` di Actions non basta per leggere un project di un utente.
3. Salvare come variabile di repository `PROJECT_NUMBER` il numero del project (dall'URL `.../projects/<numero>`).
4. Lanciare il workflow a mano con *Run workflow* e controllare il risultato.
5. I file `burndown-<iterazione>.svg` e `.csv` finiscono come artefatto e sul branch **`burndown-data`**, non su `main`, perché in `AGENTS.md` i branch principali sono protetti (§7). Aprire l'SVG su GitHub per vederlo.

Prova in locale **senza API**, per vedere il grafico di esempio:

```bash
python output/burndown/burndown.py --demo
```

> ⚠️ **Non testato su un project reale:** ho provato solo il calcolo e il grafico con dati finti. Il collegamento con l'API GraphQL e il workflow vanno verificati la prima volta. Il token non deve mai essere scritto nel codice ([[AGENTS]] §3: niente credenziali nel codice).

## Alternative

- **Grafico nativo (Insights):** è un burn-up che conta gli item nel tempo; con un campo Number `Punti` si può provare a sommarlo sull'asse Y. Nessun burndown nativo.
- **Strumento esterno:** Screenful offre un burndown per GitHub Projects con campi numerici e linea attesa.

_Aggiornato: 2026-10-18 — prima stesura_
