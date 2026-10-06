---
tipo: entità
categoria: standard
famiglia: ""
---

# AUTOSAR

## Cos'è

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=43]] (slide 95)

Esempio di **architettura a standard aperto** citato per i **sistemi aperti**: un sistema aperto definisce standard per gli elementi software (comportamento, interazioni, condivisione dei dati) così che **molti fornitori diversi** possano produrre elementi. 🧩 AUTOSAR è lo standard dell'industria automobilistica per il software delle centraline (ECU).

![[lez01b-qa-p43-autosar.png]]
*Figura di [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=43]]: in alto i componenti **AUTOSAR Software** (Application Software Component, Actuator Software Component, Sensor Software Component, …), ognuno con una **AUTOSAR Interface**; sotto, la barra arancione **AUTOSAR Runtime Environment (RTE)**; sotto ancora il **Basic Software** (Standardized Interface, Operating System, Services, Communication, ECU Abstraction, Microcontroller Abstraction, Complex Device Drivers); alla base l'**ECU-Hardware**.*

## Come si usa nel corso

🧩 Mostra la motivazione §3.9 ([[importanza-architettura-software]]): è l'architettura — con interfacce standardizzate e un ambiente di esecuzione comune (RTE) — che permette di comporre componenti di fornitori diversi.

### Come architettura di riferimento (Lez. 4)

> 📄 Fonte: [[04-Architectural Patterns.pdf#page=13]], [[04-Architectural Patterns.pdf#page=14]], [[04-Architectural Patterns.pdf#page=15]]

AUTOSAR è il primo esempio di **DSSA** (architettura di riferimento) per il dominio **automotive**: «piattaforme e architetture software standardizzate per i sistemi elettronici automotive». La figura di p. 15 (Application Layer, RTE, Basic Software a strati, Microcontroller) è descritta in [[dssa]].

🧩 Le due lezioni guardano AUTOSAR da due lati: nella Lez. 1 come **sistema aperto** (molti fornitori producono componenti compatibili), nella Lez. 4 come **architettura di riferimento** (riuso dell'architettura in tutto il dominio).

## Link ai concetti correlati

[[importanza-architettura-software]] · [[layered]] (🧩 la figura è organizzata a strati)

## Fonti

- [[attributi-di-qualita-e-importanza-architettura]] — [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=43]]

_Aggiornato: 2026-09-26 — ingest lezione 1_
_Aggiornato: 2026-10-01 — ingest 04-Architectural Patterns.pdf_
