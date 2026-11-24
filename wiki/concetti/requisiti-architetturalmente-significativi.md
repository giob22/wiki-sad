---
tipo: concetto
importanza_esame: alta
prerequisiti: ["attributi-di-qualita", "scenari-di-qualita"]
fonti_pdf: ["06-ADD-Designing a Software Architecture.pdf#page=2"]
termine_inglese: "architecturally significant requirements (ASR)"
---

# Requisiti architetturalmente significativi (ASR)

## Definizione

> 🔑 Definizione chiave — 📄 Fonte: [[06-ADD-Designing a Software Architecture.pdf#page=3]] (cap. 19 di Bass, Clements, Kazman)

Un **ASR** (*architecturally significant requirement*) è un requisito che avrà un **effetto profondo sull'architettura**: senza di esso l'architettura potrebbe essere drasticamente diversa. Spesso — ma non sempre — gli ASR sono **requisiti di attributi di qualità** (prestazioni, sicurezza, modificabilità, disponibilità, usabilità…) che l'architettura deve fornire al sistema.

## Spiegazione

> 📄 Fonte: [[06-ADD-Designing a Software Architecture.pdf#page=4]], [[06-ADD-Designing a Software Architecture.pdf#page=6]]

**Come si trovano.** Dal documento dei requisiti, oppure **intervistando gli stakeholder** e conducendo un **Quality Attribute Workshop (QAW)**: un metodo facilitato, centrato sugli stakeholder, per *generare, prioritizzare e raffinare* scenari di attributi di qualità prima che l'architettura sia completata. Il risultato deve includere un **elenco di driver architetturali** e un **insieme di scenari di qualità prioritizzati** dagli stakeholder ([[scenari-di-qualita]]).

**Utility tree.** Se nessuno stakeholder è disponibile, l'architetto può costruire un *utility tree*: una **rappresentazione top-down degli ASR** legati agli attributi di qualità critici per il successo del sistema. Per ogni attributo ci sono raffinamenti (es. prestazioni → «latenza dei dati» e «throughput delle transazioni», oppure «tempo di attesa dell'utente» e «tempo di aggiornamento della pagina») e sotto ogni raffinamento gli **scenari di qualità** che esprimono gli ASR. Ogni scenario è valutato con due criteri — **valore di business** e **rischio tecnico** — con un punteggio H/M/L ciascuno.

> 🧩 Elaborazione mia: la coppia (valore, rischio) serve a ordinare il lavoro: gli scenari (H, H) — grande valore e grande rischio — sono i candidati a guidare per primi le iterazioni di [[attribute-driven-design]].

## Esempi espansi

> 📄 Fonte: [[06-ADD-Designing a Software Architecture.pdf#page=5]], [[06-ADD-Designing a Software Architecture.pdf#page=7]], [[06-ADD-Designing a Software Architecture.pdf#page=8]]

**Scenario di modificabilità (p. 5).** «Uno sviluppatore vuole cambiare l'interfaccia utente; la modifica è fatta nel codice in fase di progettazione, richiede meno di tre ore per essere fatta e collaudata e non ci sono effetti collaterali.»

| Parte dello scenario | Valore |
|---|---|
| Sorgente | sviluppatore |
| Stimolo | vuole cambiare l'interfaccia utente |
| Artefatto | codice (interfaccia utente) |
| Ambiente | fase di progettazione (*design time*) |
| Risposta | la modifica è fatta e collaudata |
| Misura della risposta | meno di tre ore; nessun effetto collaterale |

**Utility tree di un sistema ospedaliero (pp. 7–8)** — ogni riga è uno scenario ASR; tra parentesi (valore di business, rischio tecnico):

| Attributo | Raffinamento | Scenario | (V, R) |
|---|---|---|---|
| Prestazioni | tempo di risposta | aggiornare l'account di un paziente sotto carico di picco in meno di 0,75 s | (H, H) |
| Prestazioni | throughput | al picco, 150 transazioni normalizzate al secondo | (M, M) |
| Usabilità | formazione | un neoassunto impara con 1 settimana di formazione a eseguire ogni funzione principale in meno di 5 s | (M, L) |
| Usabilità | efficienza | avviare un piano di pagamento durante l'interazione col paziente senza errori di input | (M, M) |
| Configurabilità | dati | aumentare la tariffa di un servizio in 1 giorno senza cambiare il codice | (H, L) |
| Manutenibilità | modifiche di routine | correggere un bug sui tempi di risposta e distribuire con ≤ 3 persone-giorno | (H, M) |
| Manutenibilità | modifiche di routine | cambiare i metadati di generazione dei report in 4 persone-ore | (M, L) |
| Manutenibilità | componenti commerciali | nuova versione maggiore del database installata in < 3 persone-settimane | (H, M) |
| Manutenibilità | nuova funzionalità | funzione di tracciamento dei donatori di sangue in 2 persone-mesi | (M, M) |
| Sicurezza | riservatezza | il fisioterapista vede solo la parte ortopedica della cartella, nessuna informazione finanziaria | (H, M) |
| Sicurezza | resistenza agli attacchi | un'intrusione non autorizzata è respinta e segnalata entro 90 s | (H, M) |
| Disponibilità | nessun fermo | nuovo software del database sostituito a caldo senza downtime | (H, L) |
| Disponibilità | nessun fermo | accesso web 24/7/365 ai conti dei pazienti | (M, M) |

![[lez09-add-p7-utility-tree-1.png]]
![[lez09-add-p8-utility-tree-2.png]]
*L'utility tree originale ([[06-ADD-Designing a Software Architecture.pdf#page=7]], [[06-ADD-Designing a Software Architecture.pdf#page=8]]): le stesse righe in forma di tabella.*

## Perché importa

Gli ASR sono il **primo ingresso** del metodo ADD: i driver architetturali sono ASR (scenari primari, vincoli, preoccupazioni) più lo scopo del progetto ([[06-ADD-Designing a Software Architecture.pdf#page=14]]). Senza ASR chiari non si può dire quando un'architettura è «abbastanza buona».

> 🎯 Esame: sapere definire un ASR, dire come si individuano (QAW, utility tree) e come si prioritizzano (valore di business, rischio tecnico).

## Connessioni

- [[scenari-di-qualita]]: lo scenario è la forma in cui si scrive un ASR.
- [[attributi-di-qualita]]: gli ASR più frequenti sono requisiti di qualità.
- [[attribute-driven-design]]: gli ASR sono i driver del metodo.

## Fonti

- [[designing-a-software-architecture]]; [[06-ADD-Designing a Software Architecture.pdf#page=2]]–[[06-ADD-Designing a Software Architecture.pdf#page=8]]

_Aggiornato: 2026-11-24 — ingest 06-ADD-Designing a Software Architecture.pdf_
