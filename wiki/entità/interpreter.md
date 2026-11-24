---
tipo: entità
categoria: stile
famiglia: "interpreter"
---

# Interpreter

## Contesto e problema

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=73]]

Il comportamento dell'applicazione non è fissato in anticipo ma **specificato dinamicamente da comandi forniti a runtime**: serve un componente che li analizzi e li esegua.

## Soluzione

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=73]], [[05_Architectural_Styles_Complete.pdf#page=74]]

- **Componenti:** interprete di comandi, programma/**stato dell'interprete**, interfaccia utente.
- **Connettori:** chiamate di procedura e stato condiviso.
- **Topologia:** tre parti principali, con lo stato separato dall'interprete.
- L'interprete analizza ed esegue i comandi, aggiornando lo stato di esecuzione quando serve.
- Il comportamento può essere molto dinamico e l'insieme di comandi estendibile; l'architettura resta stabile mentre nuove capacità si compongono da primitive esistenti.

## Diagramma

![[lez08-stili-p75-interpreter-lunar-lander.png]]
*Lunar Lander con interprete ([[05_Architectural_Styles_Complete.pdf#page=75]]): «Get Command from user» → «Stream» → «Interpret and Execute» → «Data Access» verso «Interpreter State». Per `(Burn, 50)` l'interprete aggiorna navicella e stato di gioco; per `(Check Status)` legge lo stato rilevante e lo mostra nella GUI.*

## Attributi di qualità

| Attributo | Effetto | Perché | Fonte |
|---|---|---|---|
| Programmabilità da parte dell'utente | + | gli utenti finali compongono nuove capacità dai comandi | [[05_Architectural_Styles_Complete.pdf#page=74]] |
| Estensibilità | + | l'insieme di comandi è estendibile senza cambiare l'architettura | [[05_Architectural_Styles_Complete.pdf#page=74]] |
| Flessibilità | + | comportamento molto dinamico | [[05_Architectural_Styles_Complete.pdf#page=74]] |

> 🧩 Elaborazione mia: come ogni livello di indirezione, l'interpretazione costa in prestazioni rispetto a codice compilato; la slide non lo dice esplicitamente, quindi non è un'affermazione tracciata.

## Quando usarlo / quando no

Quando l'utente deve poter «programmare» l'applicazione (formule, macro, query).

## Varianti ed esempi

- Lisp, motori SQL, ambienti di esecuzione Java e JavaScript, formule e macro dei fogli di calcolo. In Excel: le formule passano dal motore di calcolo, le macro VBA dall'ambiente Visual Basic ([[05_Architectural_Styles_Complete.pdf#page=74]]).
- Variante distribuita: [[mobile-code]].

## Connessioni

- [[mobile-code]]: il codice mobile richiede un interprete/ambiente di esecuzione sull'host.
- [[rule-based]]: un motore inferenziale è un tipo di interprete.

## Fonti

- [[architectural-styles]]

_Aggiornato: 2026-11-24 — ingest 05_Architectural_Styles_Complete.pdf_
