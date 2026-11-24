---
tipo: esercizio
argomento: "scegliere e confrontare stili architetturali su un problema comune (Lunar Lander)"
difficoltà: media
---

# Lunar Lander in ogni stile

## Metodo

Le slide di Taylor, Medvidovic e Dashofy ripropongono la stessa applicazione — il gioco **Lunar Lander**, in cui l'utente sceglie il *burn rate* del motore e il sistema calcola altitudine, velocità, carburante e tempo — in quasi ogni stile. Il metodo per riusare l'esercizio:

1. Identificare le **funzioni** da assegnare: acquisire l'input (burn rate), simulare l'ambiente (calcolare il nuovo stato), mostrare lo stato.
2. Scegliere i **componenti** del vocabolario dello stile e i **connettori** che li legano (chiamate, pipe, accesso ai dati condivisi, eventi…).
3. Disegnare il diagramma a scatole e frecce con i **dati scambiati** sulle frecce (a = altitudine, f = carburante, t = tempo, v = velocità, br = burn rate).
4. Valutare l'adeguatezza: il gioco richiede **controllo interattivo in tempo reale** ([[05_Architectural_Styles_Complete.pdf#page=39]]).

Concetti usati: [[stili-architetturali]], [[attributi-di-qualita]].

## Casi svolti

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=28]] (traccia: «How would you organize the Lunar Lander application into layers?»)

| Stile | Come si organizza Lunar Lander | Valutazione | Fonte |
|---|---|---|---|
| [[main-program-e-subroutine]] | main program che chiama tre procedure: input burn rate, simulazione, display | semplice, struttura implicita | [[05_Architectural_Styles_Complete.pdf#page=8]] |
| [[object-oriented]] | GUI che usa *get/set* su Spacecraft e invoca Environment Simulation | un solo oggetto gestisce tutto l'I/O | [[05_Architectural_Styles_Complete.pdf#page=13]], [[05_Architectural_Styles_Complete.pdf#page=15]] |
| [[layered]] | tastiera → logica di gioco e simulatore → game engine 2D → sistema operativo → hardware grafico | ogni layer usa solo quello sotto (CLA) | [[05_Architectural_Styles_Complete.pdf#page=29]] |
| [[client-server]] | N client (input e grafica) → un server (stato, logica, simulazione) | versione multigiocatore | [[05_Architectural_Styles_Complete.pdf#page=34]] |
| [[batch-sequential]] | tre programmi in sequenza sui lotti (h, v, t, fuel) | **inadatto**: non c'è controllo in tempo reale | [[05_Architectural_Styles_Complete.pdf#page=39]] |
| [[pipe-and-filter]] | tre filtri: chiede il burn rate; aggiorna l'ambiente a ogni nuovo valore; aggiorna il display | filtri sempre attivi, flusso continuo | [[05_Architectural_Styles_Complete.pdf#page=51]] |
| [[blackboard]] | tre componenti che leggono/scrivono una blackboard con altitudine, burnRate, fuel, time, velocity | dati condivisi, componenti indipendenti | [[05_Architectural_Styles_Complete.pdf#page=64]] |
| [[rule-based]] | fatto `burnrate(25)` e obiettivo `landed(spacecraft)`; regola altitudine ≤ 0 AND velocità < 3 ft/s | l'atterraggio è una regola nella base di conoscenza | [[05_Architectural_Styles_Complete.pdf#page=68]] |
| [[interpreter]] | comandi `(Burn, 50)` e `(Check Status)` eseguiti dall'interprete sullo stato | gioco comandabile | [[05_Architectural_Styles_Complete.pdf#page=75]] |
| [[mobile-code]] | il client scarica il codice del gioco (applet Java / JavaScript) e calcola in locale | meno carico sul server | [[05_Architectural_Styles_Complete.pdf#page=82]] |
| [[publish-subscribe]] | i giocatori si sottoscrivono al Game Server che pubblica lo stato | notifiche con l'informazione aggiornata o con invito al download | [[05_Architectural_Styles_Complete.pdf#page=105]] |
| [[event-based]] | Spacecraft, Clock, Game Logic e GUI collegati da un bus di eventi | ogni componente reagisce agli eventi | [[05_Architectural_Styles_Complete.pdf#page=112]] |
| [[peer-to-peer]] | a T₀ LL1 chiede ai vicini se altri sono atterrati; a T₁ contatta direttamente LL5 | ricerca decentralizzata | [[05_Architectural_Styles_Complete.pdf#page=156]] |

**Svolgimento dell'esercizio a layer (p. 28–29).** *Passo 1 — funzioni:* input da tastiera; logica di gioco e simulazione dell'ambiente; disegno di oggetti 2D; accesso alle risorse del sistema; visualizzazione. *Passo 2 — layer:* ognuna delle funzioni è un layer che offre un servizio al layer sopra, dall'astrazione più alta (input utente) alla più bassa (hardware grafico). *Passo 3 — dati sui connettori:* input da tastiera → variazione di altitudine → coordinate (x, y) degli oggetti → dati binari. *Soluzione:* la pila in [[layered]] (figura p. 29), un'architettura a **layer chiusi**: ogni layer usa solo quello immediatamente inferiore.

## Trappole

> 🧩 Elaborazione mia

- Confondere il **connettore** dello stile (chiamata, pipe, evento) con il dato che vi transita.
- Scegliere uno stile elegante ma inadatto al requisito dominante: il batch sequential non può fare controllo in tempo reale.
- Dimenticare di dire quali attributi di qualità lo stile sacrifica (es. nel [[blackboard]] la spiegabilità).

## Fonti

- [[architectural-styles]]; [[05_Architectural_Styles_Complete.pdf#page=28]]

_Aggiornato: 2026-11-24 — ingest 05_Architectural_Styles_Complete.pdf_
