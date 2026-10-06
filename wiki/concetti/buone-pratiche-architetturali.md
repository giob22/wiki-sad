---
tipo: concetto
importanza_esame: media
prerequisiti: ["architettura-software", "strutture-e-viste"]
fonti_pdf: ["01-IntroductionOnSoftwareArchitecture.pdf#page=48", "01-IntroductionOnSoftwareArchitecture.pdf#page=50"]
termine_inglese: "process recommendations and rules of thumb"
---

# Buone pratiche architetturali

## Definizione

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture.pdf#page=48]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=50]]

La lezione dà due elenchi di indicazioni per costruire buone architetture: **raccomandazioni di processo** (come si lavora) e **regole pratiche sulle strutture** (*rules of thumb*: come deve essere il risultato).

## Raccomandazioni di processo

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture.pdf#page=48]]

| Raccomandazione | Motivo / dettaglio |
|---|---|
| L'architettura dovrebbe essere prodotta da **un solo architetto** o da un **piccolo gruppo** di architetti | per l'**integrità concettuale** e la **coerenza tecnica** |
| **Forte legame** tra architetti e team di sviluppo | 🧩 l'architettura deve essere capita e realizzata da chi scrive il codice ([[importanza-architettura-software]] §3.5) |
| L'architettura va basata su una **lista prioritizzata** di **requisiti di qualità ben specificati** | 🧩 cioè su [[scenari-di-qualita]] ordinati per importanza |
| Va **documentata** con **viste** che rispondono alle preoccupazioni (*concerns*) dei vari stakeholder | → [[strutture-e-viste]] |
| Va **valutata** per la sua capacità di fornire gli attributi di qualità importanti | → [[valutazione-attributi-di-qualita]] |
| Deve prestarsi all'**implementazione incrementale** | creare un sistema **scheletro** in cui i **percorsi di comunicazione** sono esercitati e che all'inizio ha **funzionalità minima** (→ [[importanza-architettura-software]] §3.7) |

## Regole pratiche per buone strutture

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture.pdf#page=50]]

1. Moduli **ben definiti**, con responsabilità funzionali assegnate secondo i principi di **information hiding** e **separation of concerns**.
2. Applicare **pattern e tattiche architetturali noti** per ogni attributo di qualità ([[pattern-architetturali]], [[tattiche-architetturali]]).
3. L'architettura **non deve mai dipendere da una particolare versione** di un prodotto o strumento commerciale.
4. **Non aspettarsi una corrispondenza uno-a-uno** tra moduli e componenti ([[strutture-e-viste]]).
5. Un **numero ridotto** di **schemi di interazione** tra componenti, **semplici**.
6. … (la slide lascia l'elenco aperto)

> 🧩 Elaborazione mia — le regole applicate all'[[exam-booking-system]]:
> - regola 1: le regole di ammissione sono il «segreto» di Eligibility Checking, i dati degli studenti di Student Records (*information hiding*);
> - regola 3: l'accesso al SIS passa da un adapter, quindi un cambio di versione dell'API del SIS resta confinato ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=30]]);
> - regola 4: il Booking Service contiene due moduli ([[01-IntroductionOnSoftwareArchitecture.pdf#page=28]]);
> - regola 5: il sistema usa pochi tipi di interazione (chiamate HTTPS/REST, accesso JDBC, messaggi AMQP).

## Perché importa

Riassume in forma di regole ciò che la lezione argomenta altrove. Il metodo che mette insieme driver, concetti di progetto e strutture è l'[[attribute-driven-design]] ([[01-IntroductionOnSoftwareArchitecture.pdf#page=49]]).

> 🎯 Esame: le raccomandazioni di processo (in particolare «un solo architetto o un piccolo gruppo» e «sistema scheletro») e le cinque regole pratiche.

## Connessioni

- [[attribute-driven-design]]: metodo di progetto guidato dagli attributi.
- [[importanza-architettura-software]]: §3.5 vincoli, §3.7 sviluppo incrementale.
- [[valutazione-attributi-di-qualita]]: la raccomandazione di valutare.

## Fonti

- [[introduzione-architettura-software]] — [[01-IntroductionOnSoftwareArchitecture.pdf#page=48]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=50]]

_Aggiornato: 2026-09-26 — ingest lezione 1_
