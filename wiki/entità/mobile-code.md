---
tipo: entità
categoria: stile
famiglia: "interpreter"
---

# Mobile code

## Contesto e problema

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=76]]

Le risorse di calcolo locali sono insufficienti o grandi insiemi di dati stanno già altrove: conviene **spostare il codice** invece dei dati.

## Soluzione

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=76]], [[05_Architectural_Styles_Complete.pdf#page=77]], [[05_Architectural_Styles_Complete.pdf#page=81]]

- **Idea:** il codice è trasmesso a un host remoto per essere eseguito o interpretato.
- **Componenti:** un **execution dock** che riceve codice e stato, e un interprete/ambiente di esecuzione.
- **Connettori:** protocolli di rete e meccanismi per impacchettare codice e dati.
- **Elementi dati:** codice rappresentato come dato, stato del programma, dati applicativi.
- **Topologia:** una rete di host di esecuzione.

**Tre varianti** (p. 77):

| Variante | Dove sono dati/risorse | Che cosa si sposta | Esempio |
|---|---|---|---|
| **Code on demand** | dati e risorse di esecuzione sono locali | il codice viene scaricato sul client | browser che scarica JavaScript |
| **Remote evaluation** | il codice è locale, le risorse di esecuzione sono remote | il codice va a un host remoto | grid computing |
| **Mobile agent** | l'iniziatore ha codice e alcune risorse, non tutte | codice **e stato di esecuzione** migrano su un altro nodo | agente che si sposta lungo una rete di nodi |

## Diagramma

![[lez08-stili-p78-code-on-demand.png]]
*Code on demand ([[05_Architectural_Styles_Complete.pdf#page=78]]): il browser richiede una pagina web, il server restituisce codice JavaScript, che è eseguito nel browser.*

![[lez08-stili-p79-remote-evaluation.png]]
*Remote evaluation ([[05_Architectural_Styles_Complete.pdf#page=79]]): il client invia il codice a un server (grid), che lo esegue e restituisce i risultati. Grid e cloud computing sono concetti distinti.*

![[lez08-stili-p80-mobile-agent.png]]
*Mobile agent ([[05_Architectural_Styles_Complete.pdf#page=80]]): un agente migra autonomamente lungo un anello di nodi (Master, Node 0, 1, 2) per ottenere risorse che non ha localmente.*

![[lez08-stili-p82-mobile-code-lunar-lander.png]]
*Lunar Lander con mobile code ([[05_Architectural_Styles_Complete.pdf#page=82]]): tre browser — uno con un programma JavaScript eseguito da un JavaScript Interpreter con proprio stato, uno con una Java Virtual Machine che esegue un Game Applet, uno con il «Lunar Lander Game Code» — parlano con il (Game) Server solo tramite Remote Procedure Call su HTTP; calcolo e stato di gioco stanno nei client.*

## Attributi di qualità

| Attributo | Effetto | Perché | Fonte |
|---|---|---|---|
| Traffico di rete | + | si sposta il codice invece di grandi quantità di dati | [[05_Architectural_Styles_Complete.pdf#page=76]] |
| Adattabilità | + | si cambia il comportamento senza sostituire l'architettura; adattamento dinamico | [[05_Architectural_Styles_Complete.pdf#page=76]], [[05_Architectural_Styles_Complete.pdf#page=83]] |
| Dependability | + | la migrazione può aiutare quando esistono host alternativi | [[05_Architectural_Styles_Complete.pdf#page=83]] |
| Sicurezza | − | gli host devono proteggersi da codice non fidato | [[05_Architectural_Styles_Complete.pdf#page=83]] |
| Prestazioni (comunicazione) | − | costi di comunicazione o connessioni inaffidabili possono annullare il vantaggio | [[05_Architectural_Styles_Complete.pdf#page=83]] |

## Quando usarlo / quando no

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=83]]

Per spostare il calcolo verso grandi insiemi di dati remoti o per configurare un'applicazione con codice fornito dall'esterno; da evitare se non ci si può proteggere da codice non fidato o la rete è inaffidabile.

## Varianti ed esempi

- Lunar Lander: i client web scaricano il codice del gioco ed eseguono il calcolo in locale (applet Java o JavaScript), alleggerendo il server ([[05_Architectural_Styles_Complete.pdf#page=82]]).

## Connessioni

- [[interpreter]]: serve un ambiente di esecuzione.
- [[client-server]]: code on demand sposta logica dal server al client.
- [[cloud-computing]]: concetto distinto dal grid.

## Fonti

- [[architectural-styles]]

_Aggiornato: 2026-11-24 — ingest 05_Architectural_Styles_Complete.pdf_
