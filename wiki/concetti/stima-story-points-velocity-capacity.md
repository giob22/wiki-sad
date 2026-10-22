---
tipo: concetto
importanza_esame: alta
prerequisiti: ["user-stories", "product-backlog-e-sprint-backlog"]
fonti_pdf: ["04_Agile_02 (1).pdf#page=47", "04_Agile_02 (1).pdf#page=48", "04_Agile_02 (1).pdf#page=50", "04_Agile_02 (1).pdf#page=51", "04_Agile_02 (1).pdf#page=52", "04_Agile_02 (1).pdf#page=53", "04_Agile_02 (1).pdf#page=54"]
termine_inglese: "story points, velocity, capacity"
---

# Stima con gli Story Point, velocity e capacity

## Definizione

| Termine | Definizione (slide) | Fonte |
|---|---|---|
| **Story Point (SP)** | misura della **dimensione relativa** di una user story: **non si stima il tempo**; rappresenta una combinazione di **complessità, quantità di lavoro, rischio e incertezza** | [[04_Agile_02 (1).pdf#page=48]] |
| **Velocity** (velocità del team) | il **numero di Story Point che un team completa durante uno Sprint**; contano **solo le storie completate** | [[04_Agile_02 (1).pdf#page=51]] |
| **Capacity** (capacità) | la **disponibilità effettiva** del team | [[04_Agile_02 (1).pdf#page=54]] |

## Spiegazione

### Quando e da chi si stima

> 📄 Fonte: [[04_Agile_02 (1).pdf#page=47]]

La stima si fa durante il **Backlog Refinement** ed è eseguita dal **Development Team**, perché sono gli sviluppatori a conoscere la **complessità tecnica, i rischi, le dipendenze e il lavoro coinvolto**. Il **Product Owner può chiarire il requisito ma non assegna gli Story Point**. (Così si risolve la questione «la stima è rimandata alla prossima lezione» lasciata aperta in [[user-stories]].)

### Come si stima: dimensione relativa

> 📄 Fonte: [[04_Agile_02 (1).pdf#page=48]]

Si stima la **dimensione relativa** della storia, non il tempo. Il metodo più usato è il **Planning Poker** → [[planning-poker]]. La scala delle carte è di tipo **Fibonacci** (1, 2, 3, 5, 8, 13, 21, …, [[04_Agile_02 (1).pdf#page=49]]): il perché è nella sezione seguente.

> 🧩 Elaborazione mia — perché non i giorni: dire «3 giorni» lega la stima a una persona e al suo ritmo («a me servono 3 giorni, a te 5»); dire «questa storia è grande il triplo di quella di riferimento» è un confronto che vale per tutto il team ed è più facile da fare (e più stabile) di una misura assoluta.

### Perché Fibonacci, invece del tempo

> 📄 Fonte: [[04_Agile_02 (1).pdf#page=50]] (titolo in italiano; infografica in inglese)

![[lez07-ag2-p50-perche-fibonacci.png]]
*Figura di [[04_Agile_02 (1).pdf#page=50]], «Why do we use Fibonacci? Because we estimate complexity, not time». Sei riquadri e un messaggio finale, trascritti qui sotto.*

| # | Riquadro | Contenuto |
|---|---|---|
| 1 | **Comparare è più facile che misurare** | «Chi è più grande: topo, cane, elefante?» è facile; «quanto pesa un elefante?» (3, 5, 6 tonnellate…) è una domanda difficile, le risposte variano. Gli Story Point funzionano come i confronti di dimensione |
| 2 | **Usa un riferimento e stima in modo relativo** | il topo è il riferimento: **1 punto**; gatto 2, cane 3, elefante 8–13–21? «Più un elemento è grande o complesso, maggiore è l'incertezza. Una precisione eccessiva non serve» |
| 3 | **La sequenza di Fibonacci** | 1, 2, 3, 5, 8, 13, 21, … I valori **crescono in modo non lineare**; **gli intervalli tra i valori aumentano**; **intervalli più ampi riflettono maggiore incertezza al crescere della complessità**. «Quando il lavoro raddoppia o triplica, l'incertezza può crescere più che proporzionalmente» |
| 4 | **Un esempio con gli animali** | topo, gatto, cane, cavallo, elefante ↔ complessità molto bassa, bassa, media, alta, molto alta ↔ **1, 2, 3, 8, 21** |
| 5 | **Un esempio con user story** | Change the logo **1**; Password recovery **3**; Product search **5**; Shopping cart **8**; PayPal payment **13**. «Perché non 11? La precisione artificiale non aiuta. Usa categorie di dimensione più ampie» |
| 6 | **Perché non una scala da 1 a 10** | confronto riga per riga: *Change a logo* 1 / 1; *Password recovery* 3 / 3; *PayPal payment* **«7 o 8?»** (scala 1–10) / **8** (Fibonacci); *New search engine* **«9 o 10?»** / **13**. Con 1–10 si perde tempo a discutere differenze che non esistono. La scala di Fibonacci aiuta a: **stimare in modo coerente, accettare l'incertezza, confrontare la complessità (non il tempo)** |

**Messaggio chiave dell'infografica:** *«Fibonacci non rende le stime più precise. Ci aiuta ad accettare che la precisione diminuisce quando la complessità aumenta.»*

> 🧩 Elaborazione mia — verifica sui numeri: nella sequenza, il passo da 8 a 13 è di 5 punti, da 13 a 21 di 8 (sempre il termine precedente); in una scala 1–10 il passo è sempre 1. Per elementi piccoli (1→2→3) la scala distingue finemente; per quelli grandi **vieta** di distinguere 11 da 12: se la storia è così grande da essere incerta, la differenza non è affidabile (e di solito conviene scomporla, [[user-stories]]).

### Velocity

> 📄 Fonte: [[04_Agile_02 (1).pdf#page=51]]

La velocity è il numero di SP completati in uno Sprint. **Contano solo le storie completate**: quelle che **rispettano la Definition of Done** e **fanno parte dell'Incremento** ([[product-backlog-e-sprint-backlog]]). Le storie **iniziate ma non finite non contribuiscono**. Serve soprattutto a **pianificare gli Sprint futuri**: aiuta il team a decidere quanto lavoro sia **realistico** includere.

> 🧩 Elaborazione mia — conseguenza: una storia al 90 % vale **0 punti** di velocity. Non è severità: serve a non gonfiare il numero con lavoro non verificato e a incentivare il team a **finire** le storie prima di iniziarne altre (azione tipica di retrospettiva: limitare il WIP, [[condurre-una-retrospettiva]]).

#### Esempio: calcolo della velocity media

> 📄 Fonte: [[04_Agile_02 (1).pdf#page=52]] (il risultato «circa 30 SP» è dato senza passaggi)

| Sprint | Velocity (SP) |
|---|---|
| Sprint 1 | 28 |
| Sprint 2 | 31 |
| Sprint 3 | 30 |
| Sprint 4 | 29 |

La slide calcola la **media delle storie completate negli sprint recenti**: la velocity è **circa 30 SP**; per il prossimo sprint si selezionano storie per **circa 30 SP**. All'inizio di un progetto la velocity è spesso instabile ma **alla fine si stabilizza**.

$$
\begin{aligned}
\bar v &= \frac{28 + 31 + 30 + 29}{4} && \text{media dei quattro sprint (SP/sprint)} \\
       &= \frac{118}{4}               && \text{somma: } 28+31=59,\ 59+30=89,\ 89+29=118 \\
       &= 29{,}5\ \text{SP/sprint}    && \text{divisione} \\
       &\approx 30\ \text{SP/sprint}  && \text{arrotondato, come nella slide}
\end{aligned}
$$

**Verifica di sanità:** ogni valore è entro ±1,5 SP dalla media (28 è –1,5; 31 è +1,5; 30 è +0,5; 29 è –0,5): la serie è già stabile. **Ipotesi:** gli sprint hanno la stessa durata e lo stesso team; vale per i soli sprint **recenti**, quindi la media si aggiorna man mano.

> 🧩 Elaborazione mia — la velocity è una **previsione, non un impegno**: la slide di planning dice che «past velocity informs the forecast; it is not a fixed commitment» ([[04_Agile_02 (1).pdf#page=45]]).

### Inizio del primo Sprint

> 📄 Fonte: [[04_Agile_02 (1).pdf#page=53]]

Nel **primo Sprint la velocity non è disponibile**: si può solo fare una **stima iniziale** e si determina la **velocity reale** alla fine dello Sprint. **Anche se la stima iniziale era sbagliata non è un problema: stavamo sperimentando…** 🧩 È l'empirismo di Scrum: si agisce, si misura, si adatta ([[scrum]]).

### Velocity vs Capacity

> 📄 Fonte: [[04_Agile_02 (1).pdf#page=54]]

La **capacity** rappresenta la **disponibilità effettiva** del team: se un membro è assente o in ferie per alcuni giorni, la capacity **diminuisce proporzionalmente**.

Esempio della slide: un team di **7 persone** su **2 settimane (10 giorni lavorativi)** ha normalmente una capacity di **7 × 10 = 70 giorni-persona**. Se **una persona è in ferie per 5 giorni** e uno sviluppatore è **assente 2 giorni**, la capacity è **ridotta del 10 %**; per la stima successiva **gli SP del backlog si riducono del 10 %**.

#### Derivazione — riduzione della capacity

**Fonte:** [[04_Agile_02 (1).pdf#page=54]] (risultato «10 %» dato senza passaggi)

$$
\begin{aligned}
C_0 &= N \cdot G = 7 \cdot 10 = 70\ \text{giorni-persona} && \text{capacity piena: 7 persone × 10 giorni} \\
A   &= 5 + 2 = 7\ \text{giorni-persona}                    && \text{giorni di assenza totali} \\
C   &= C_0 - A = 70 - 7 = 63\ \text{giorni-persona}        && \text{capacity disponibile} \\
r   &= \frac{A}{C_0} = \frac{7}{70} = 0{,}10 = 10\,\%      && \text{riduzione}
\end{aligned}
$$

**Verifica:** $63/70 = 0{,}9$, cioè il 90 % della capacity piena. **Ipotesi:** ogni giorno-persona vale lo stesso (tutti ugualmente produttivi) e l'assenza «due giorni di uno sviluppatore» è in aggiunta ai 5 giorni dell'altra persona.

> 🧩 Elaborazione mia — applicazione alla velocity di p. 52: se la velocity media è ≈30 SP con il team al completo, una capacity al 90 % porta a pianificare circa $30 \times 0{,}9 = 27$ SP. La slide dice di ridurre «gli SP del backlog» del 10 %; in pratica si riduce il **carico da selezionare**, che è lo stesso conto. Esempio completo in [[pianificare-uno-sprint]].

| | Velocity | Capacity |
|---|---|---|
| **Misura** | SP **effettivamente completati** (passato) | giorni-persona **disponibili** (futuro) |
| **Unità** | story point per sprint | giorni-persona |
| **Uso** | calibrare quanto lavoro prendere | correggere la velocity per assenze e carichi |
| **Si calcola** | dopo lo sprint, come media | prima dello sprint, dal calendario del team |

Fonte della distinzione: [[04_Agile_02 (1).pdf#page=51]], [[04_Agile_02 (1).pdf#page=54]] (la tabella è una sintesi mia 🧩).

## Perché importa

È ciò che rende la pianificazione di Scrum **realistica senza promettere date**: la stima in punti è relativa, la velocity trasforma i punti in una previsione per sprint, la capacity la corregge. Nel progetto di corso le stime (taglie) delle issue alimentano il burndown dello sprint ([[burndown-github-project]]).

> 🎯 Esame: cos'è uno Story Point e cosa combina; perché Fibonacci e non il tempo; chi stima e quando; definizione di velocity e quali storie contano; esempio di media; capacity e come cambia con le assenze; velocity vs capacity.

> ⚖️ Trade-off: **precisione vs sforzo di stima** — stimare in giorni sembra più preciso ma richiede più discussione e rimane inaffidabile; i punti accettano l'incertezza.

## Connessioni

- [[planning-poker]]: la tecnica di stima di gruppo.
- [[user-stories]]: INVEST (E = Estimable) e la scomposizione di storie troppo grandi.
- [[sprint-e-sprint-planning]]: la velocity e la capacity guidano la selezione.
- [[cerimonie-e-artefatti-agile]]: il burndown in SP (Lez. 6).

## Fonti

- [[agile-scrum-framework]] — [[04_Agile_02 (1).pdf#page=47]]–[[04_Agile_02 (1).pdf#page=54]]

_Aggiornato: 2026-10-22 — ingest 04_Agile_02 (1).pdf_
