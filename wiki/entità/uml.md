---
tipo: entità
categoria: linguaggio
famiglia: ""
---

# UML (Unified Modeling Language)

## Cos'è

Linguaggio grafico di modellazione usato nelle slide per disegnare le viste architetturali. 🧩 La lezione 1 non lo introduce: lo usa come notazione.

## Come si usa nel corso

| Vista | Elementi / stereotipi UML usati | Fonte |
|---|---|---|
| Moduli | package, classe, classe astratta (corsivo), compartimenti attributi/operazioni, interfaccia (a «lecca-lecca» o con «interface») | [[01-IntroductionOnSoftwareArchitecture.pdf#page=10]] |
| Relazioni tra moduli | *is-part-of* (annidamento di package), *depends-on* (freccia tratteggiata «use»), *is-a* (ereditarietà tra classi e realizzazione di interfaccia) | [[01-IntroductionOnSoftwareArchitecture.pdf#page=10]] |
| Decomposizione | package annidati (`«package»`) | [[01-IntroductionOnSoftwareArchitecture.pdf#page=18]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=19]] |
| Uses | frecce tratteggiate «use» tra package | [[01-IntroductionOnSoftwareArchitecture.pdf#page=20]] |
| Classi (generalizzazione) | ereditarietà con triangolo vuoto | [[01-IntroductionOnSoftwareArchitecture.pdf#page=22]] |
| Deployment | `«device»`, `«executionEnvironment»`, `«artifact»`, percorsi di comunicazione etichettati con il protocollo, relazione «deploy» | [[01-IntroductionOnSoftwareArchitecture.pdf#page=39]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=40]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=44]] |
| Install | `«artifact»` = file di qualsiasi tipo; `«manifest»` = un componente/classe/artifact è dentro un artifact | [[01-IntroductionOnSoftwareArchitecture.pdf#page=46]] |
| Componenti | `«component»` con interfacce fornite (cerchio) e richieste (semicerchio) | [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=42]] |

## Link ai concetti correlati

[[strutture-di-modulo]] · [[strutture-di-allocazione]] · [[strutture-componenti-e-connettori]]

## Fonti

- [[introduzione-architettura-software]], [[attributi-di-qualita-e-importanza-architettura]]

_Aggiornato: 2026-09-26 — ingest lezione 1_
