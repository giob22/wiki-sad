---
tipo: esercizio
argomento: "mappare un sistema sul pattern Sense–Compute–Control"
difficoltà: bassa
---

# Applicare il pattern Sense–Compute–Control

## Metodo

> 📄 Fonte: [[3-Architectural Patterns-complete.pdf#page=84]], [[3-Architectural Patterns-complete.pdf#page=87]], [[3-Architectural Patterns-complete.pdf#page=93]]

1. Individua l'**ambiente** e come cambia nel tempo.
2. **Sense**: quali grandezze si misurano e con quali sensori.
3. **Compute**: come si stima la situazione (contesto) dai dati grezzi.
4. **Control**: quale decisione si prende e quali comandi vanno agli attuatori.
5. Chiudi il **ciclo**: come gli attuatori cambiano l'ambiente.
6. Scegli la **variante**: tre stadi se la logica è semplice; quattro stadi se lo stesso contesto serve più politiche o il sistema è distribuito.
7. Se distribuito (IoT): decidi cosa resta **locale** sull'edge (risposte rapide, funziona senza cloud) e cosa va **remoto** (dati aggregati, analisi complesse).

## Concetti usati

[[sense-compute-control]] · [[tattiche-modifiability]] (separazione dei moduli) · [[availability]] (controllo locale senza cloud)

## Casi svolti

### Caso 1 — Rilevamento di intrusioni in casa

**Traccia:** [[3-Architectural Patterns-complete.pdf#page=86]].

| Fase | Sistema antintrusione |
|---|---|
| Ambiente | la casa (persone che si muovono) |
| Sense | sensori di movimento |
| Compute | i dati indicano una possibile intrusione? |
| Control | attivare un allarme o inviare una notifica |
| Effetto sull'ambiente | l'allarme suona / qualcuno interviene |

🧩 In quattro stadi: «possibile intrusione» (contesto) è separato da «allarme o notifica» (decisione). Così la stessa stima serve una politica notturna (allarme) e una diurna (solo notifica) senza toccare l'interpretazione dei sensori.

### Caso 2 — Controllo accessi e rilevamento intrusioni

**Traccia:** [[3-Architectural Patterns-complete.pdf#page=89]] (figura descritta in [[sense-compute-control]]).

| Stadio | Elementi |
|---|---|
| Sensing (sorgenti) | Camera, Motion Detector, Locker, Authorization Database, Identifier |
| Context processing | Scene Image, Presence, Intrusion, Secure Building, Authenticated Access |
| Control logic | Intrusion Manager, Secure Manager, Access Controller |
| Actuation (azioni) | Screen (display), Alarm (on/off), Locker (lock), Door (lock) |

🧩 **Riuso del contesto:** *Secure Building* alimenta sia il Secure Manager sia, tramite *Intrusion*, l'Intrusion Manager. **Dati del contesto:** valori booleani (presenza, chiuso/aperto, accesso autorizzato) arricchiti di `location` e `user`; i controller ricevono situazioni già interpretate, non dati grezzi.

### Caso 3 — Lunar Lander

**Traccia:** [[3-Architectural Patterns-complete.pdf#page=92]], [[3-Architectural Patterns-complete.pdf#page=93]], [[3-Architectural Patterns-complete.pdf#page=94]].

**Il gioco** ([[3-Architectural Patterns-complete.pdf#page=92]]): videogioco semplice nato alla fine degli anni '60. Obiettivo: far **atterrare in sicurezza** una navicella sulla Luna. Il giocatore controlla la discesa; la **manetta** (*throttle*) regola la spinta del motore e quindi la velocità di discesa; il **carburante** è limitato; quota e velocità iniziali sono fissate. **Si vince atterrando con velocità verticale inferiore a 5 piedi al secondo**, che sia rimasto carburante o no. Le versioni avanzate hanno un joystick per movimento orizzontale, orientamento e spinta.

![[lez05-ap-p92-lunar-lander.png]]
*Figura di [[3-Architectural Patterns-complete.pdf#page=92]]: schermata in bianco e nero del gioco, con il profilo del terreno lunare e i valori di volo in alto; link a un video dimostrativo.*

**Il pattern applicato** ([[3-Architectural Patterns-complete.pdf#page=93]]):

| Fase | Lunar Lander |
|---|---|
| Sense | leggere quota, velocità, orientamento e carburante residuo |
| Compute | determinare la spinta necessaria e la correzione d'assetto |
| Control | attivare il motore e i propulsori di manovra |
| Ambiente | la gravità lunare cambia posizione e velocità della navicella |

![[lez05-ap-p93-lunar-lander-tabella.png]]
*Figura di [[3-Architectural Patterns-complete.pdf#page=93]]: la tabella originale, trascritta sopra.*

![[lez05-ap-p94-scc-lunar-lander.png]]
*Figura di [[3-Architectural Patterns-complete.pdf#page=94]] (da Taylor, Medvidovic, Dashofy): **Lunar Environment and Spacecraft Dynamics** (gravità lunare, quota, velocità, orientamento) → *physical state* → **SENSING** (Altimeter, Gyroscope, Vertical velocity, Fuel level) → *measurements* → **Flight Control Computer** (State estimation, Control logic), che riceve anche i *pilot commands* da **PILOT INPUTS** (Engine/Throttle Control, Attitude Joystick) e manda *status information* ai **Cockpit Displays**; → *control commands* → **ACTUATION** (Main Descent Engine, Attitude Control Thrusters) → *thrust changes vehicle state* → ambiente. Riquadro «Control loop»: 1. leggere i sensori; 2. stimare lo stato della navicella; 3. calcolare le uscite di controllo; 4. inviare i comandi agli attuatori; 5. ripetere.*

🧩 Il Flight Control Computer ha due parti — *State estimation* e *Control logic* — quindi la figura è in realtà la **variante a quattro stadi**: Sensing → stima dello stato (contesto) → logica di controllo → attuazione.

**Simulazione (🧩 elaborazione mia).** Per vedere cosa fa il ciclo di controllo, ho simulato la discesa con le unità della slide (piedi, secondi), con lo script `output/grafici/genera_animazioni_lez05.py`.

$$
\begin{aligned}
g &\approx 5.32\ \text{ft/s}^2 && \text{gravità lunare } (1.62\ \text{m/s}^2) \\
v_{ref}(h) &= -\max(3,\ 0.08\,h)\ \text{ft/s} && \text{velocità desiderata: più lenta vicino al suolo} \\
a_{spinta} &= g + k\,(v_{ref} - v),\quad k = 0.8\ \text{s}^{-1} && \text{COMPUTE: compensa la gravità + correzione} \\
a_{spinta} &\in [0,\ 16]\ \text{ft/s}^2 && \text{CONTROL: limiti del motore} \\
v(t+\Delta t) &= v + (a_{spinta} - g)\,\Delta t,\quad h(t+\Delta t) = h + v\,\Delta t && \text{AMBIENTE, con } \Delta t = 0.05\ \text{s}
\end{aligned}
$$

Ogni passo da 0,05 s è un giro del ciclo: si **legge** $(h, v)$ (sense), si **calcola** la spinta (compute), si **comanda** il motore (control), la gravità e la spinta **cambiano** quota e velocità (ambiente).

![[grafico-lunar-lander-controllo.svg]]
*🧩 Grafico mio: partenza a 1000 ft con −50 ft/s. Linea blu = con il ciclo Sense–Compute–Control: la navicella frena e tocca il suolo a **−3,0 ft/s dopo circa 50 s**, sotto la soglia di 5 ft/s della slide (linea rossa). Linea grigia tratteggiata = motore spento: cade per sola gravità e impatta a circa **−115 ft/s dopo circa 12 s**.*

**Sanity check:** a motore spento $v(t) = v_0 - g\,t$ e $h(t) = h_0 + v_0 t - \tfrac{1}{2} g t^2$. Imponendo $h = 0$: $2.66\,t^2 + 50\,t - 1000 = 0 \Rightarrow t \approx 12.2\ \text{s}$, e $v \approx -50 - 5.32 \times 12.2 \approx -115\ \text{ft/s}$ ✔ (coincide con la simulazione).
**Ipotesi:** moto solo verticale, nessun ritardo tra misura e comando, sensori perfetti, carburante sufficiente (la simulazione lo stima ma non lo limita). Con un ritardo nel ciclo — come in un'implementazione distribuita, [[3-Architectural Patterns-complete.pdf#page=91]] — la correzione arriva tardi e l'atterraggio peggiora: è il problema di latenza e safety citato dalla slide.

### Caso 4 — Sistema di guida autonoma (ADS)

**Traccia:** [[3-Architectural Patterns-complete.pdf#page=95]] (figura in [[sense-compute-control]]).

| Stadio Sense–Compute–Control (4 stadi) | Blocco ADS | Componenti |
|---|---|---|
| Sensing | Sensing | GPS/IMU, Camera, LiDAR, Radar |
| Context processing | Perception | Localization, Detection |
| Control logic | Planning | Prediction, Planning |
| Actuation | Control | Control algorithms, Control functions |

🧩 Il modulo *End-to-End* attraversa Perception, Planning e Control: unisce interpretazione e decisione, cioè va verso la variante a tre stadi.

## Trappole

- Fermarsi a tre fasi senza **chiudere il ciclo** con l'effetto sull'ambiente.
- Mettere la stima del contesto e la politica di controllo nello stesso componente quando servono più politiche.
- Dimenticare i rischi delle versioni distribuite: latenza, disponibilità, safety, sicurezza ([[3-Architectural Patterns-complete.pdf#page=91]]).

_Aggiornato: 2026-10-06 — ingest 3-Architectural Patterns-complete.pdf_
