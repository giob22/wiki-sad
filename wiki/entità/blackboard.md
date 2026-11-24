---
tipo: entità
categoria: stile
famiglia: "shared memory"
---

# Blackboard

## Contesto e problema

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=60]], [[05_Architectural_Styles_Complete.pdf#page=62]]

Un problema complesso non ha una strategia risolutiva pianificabile in anticipo: la soluzione emerge dal contributo di **specialisti indipendenti** che lavorano su una rappresentazione comune del problema.

## Soluzione

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=56]], [[05_Architectural_Styles_Complete.pdf#page=60]]

- Come in [[repository]], c'è un'area di dati condivisa (la *blackboard*) e agenti che vi accedono. La differenza: nella blackboard i componenti specialisti contribuiscono con **risultati parziali** e **lo stato condiviso in evoluzione guida quali componenti eseguire**.
- **Blackboard passiva:** i componenti fanno *polling* dello stato condiviso e decidono quando agire.
- **Blackboard attiva:** un *manager* notifica i programmi quando i dati rilevanti cambiano.

## Diagramma

![[lez08-stili-p64-blackboard-lunar-lander.png]]
*Lunar Lander con blackboard ([[05_Architectural_Styles_Complete.pdf#page=64]]): tre componenti — immissione del burn rate (fornisce br), visualizzazione (ottiene a, f, t, v), calcolo e aggiornamento (ottiene a, br, f, t, v; fornisce a, f, t, v) — usano un connettore «Data Access» verso la blackboard, il cui contenuto è altitudine, burnRate, fuel, time, velocity.*

## Attributi di qualità

| Attributo | Effetto | Perché | Fonte |
|---|---|---|---|
| Flessibilità della strategia risolutiva | + | non pianificata in anticipo; i dati determinano il contributo successivo | [[05_Architectural_Styles_Complete.pdf#page=62]] |
| Cooperazione tra specialisti | + | specialisti indipendenti collaborano su una rappresentazione condivisa | [[05_Architectural_Styles_Complete.pdf#page=62]] |
| Modificabilità | − | cambiare la rappresentazione dei dati può coinvolgere molti agenti | [[05_Architectural_Styles_Complete.pdf#page=63]] |
| Prestazioni | − | i dati condivisi possono diventare un collo di bottiglia | [[05_Architectural_Styles_Complete.pdf#page=63]] |
| Spiegabilità | − | difficile spiegare come sono stati ottenuti i risultati | [[05_Architectural_Styles_Complete.pdf#page=63]] |
| Semplicità | − | può aggiungere complessità inutile se esiste già una strategia di coordinamento chiara | [[05_Architectural_Styles_Complete.pdf#page=63]] |

## Quando usarlo / quando no

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=63]]

Cautela quando le interazioni tra programmi indipendenti richiedono coordinamento complesso; gli agenti concorrenti richiedono meccanismi di controllo degli accessi.

## Varianti ed esempi

- Intelligenza artificiale (problem solving, riconoscimento vocale, controllo di robot); OCR (strumenti storici come Adobe Acrobat Capture); CAD grafici; sistemi di Complex Event Processing ([[05_Architectural_Styles_Complete.pdf#page=61]]).

## Connessioni

- [[repository]]: la blackboard è un repository in cui lo stato guida il controllo.
- [[rule-based]]: altra specializzazione.
- [[publish-subscribe]]: la blackboard attiva (il manager notifica) ricorda la notifica per sottoscrizione.

## Fonti

- [[architectural-styles]]

_Aggiornato: 2026-11-24 — ingest 05_Architectural_Styles_Complete.pdf_
