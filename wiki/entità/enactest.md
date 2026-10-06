---
tipo: entità
categoria: caso-di-studio
famiglia: ""
---

# ENACTEST (architettura del progetto)

## Cos'è

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=42]] (slide 94)

Esempio mostrato dalla docente (slide in italiano: «L'Esempio dell'Architettura dell'ENACTEST project») come caso di **architettura che incorpora elementi sviluppati indipendentemente** (§3.9). La slide contiene solo il diagramma dei componenti. 🧩 Dai nomi dei componenti (Game Engine, Test Run Environment, Java Classes Under Test) sembra un sistema di gioco per l'apprendimento del testing; la slide non lo dice.

![[lez01b-qa-p42-enactest.png]]
*Figura di [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=42]], diagramma dei componenti UML: `«component» Web Front End`, `«component» Game Engine`, `«component» Test Run Environment`, `«component» Java Classes Under Test Repository`, `«component» Games Repository`. Interfacce in notazione *ball-and-socket* (cerchio = interfaccia fornita, semicerchio = interfaccia richiesta): **RoundExecutor** (fornita dal Game Engine, richiesta dal Web Front End); **ClassUTReader** (fornita dal Java Classes Under Test Repository, richiesta dal Web Front End); **CRUD Student** (fornita dal Games Repository, richiesta dal Web Front End); **CRUD Game** e **CRUD Round** (fornite dal Games Repository, richieste dal Game Engine); **TestExecutor** collega Game Engine e Test Run Environment.*

> ❓ Salto non ricostruito: dalla figura non si distingue con certezza quale lato di **TestExecutor** sia il cerchio e quale il semicerchio, quindi chi fornisca l'interfaccia. Dal nome ci si aspetterebbe che la fornisca il Test Run Environment, ma per analogia grafica con le interfacce CRUD sembrerebbe il contrario. Da chiarire con la docente.

## Come si usa nel corso

🧩 Ogni componente espone ed usa solo interfacce nominate: si possono sviluppare separatamente e poi assemblare, come richiede §3.9 ([[importanza-architettura-software]]). È anche un esempio di vista C&C in notazione [[uml]].

## Link ai concetti correlati

[[importanza-architettura-software]] · [[strutture-componenti-e-connettori]]

## Fonti

- [[attributi-di-qualita-e-importanza-architettura]] — [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=42]]

_Aggiornato: 2026-09-26 — ingest lezione 1_
