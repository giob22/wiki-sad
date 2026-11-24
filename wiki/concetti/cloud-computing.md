---
tipo: concetto
importanza_esame: media
prerequisiti: ["stili-architetturali"]
fonti_pdf: ["05_Architectural_Styles_Complete.pdf#page=84"]
termine_inglese: "cloud computing"
---

# Cloud computing (cenni)

## Definizione

> 🔑 Definizione chiave — 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=84]] (definizione NIST)

Il **cloud computing** è un modello per l'accesso di rete comodo e *on demand* a un **pool condiviso di risorse di calcolo configurabili**; le risorse possono essere allocate e rilasciate rapidamente con minimo sforzo di gestione o interazione con il provider.

## Spiegazione

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=85]], [[05_Architectural_Styles_Complete.pdf#page=86]], [[05_Architectural_Styles_Complete.pdf#page=88]]

**Benefici (p. 85).** *Per i clienti:* meno bisogno di possedere e mantenere infrastruttura; modelli pay-per-use e capacità scalabile; affidabilità e sicurezza supportate dal provider (secondo servizi e configurazione). *Per i provider:* la domanda aggregata migliora l'utilizzo delle risorse e aiuta a gestire la variabilità tra clienti.

**Modelli di servizio (p. 86):**

| Modello | Che cosa offre il provider | Esempi dalla slide |
|---|---|---|
| **IaaS** — Infrastructure as a Service | rete, storage, calcolo | macchine virtuali |
| **PaaS** — Platform as a Service | infrastruttura + sistema operativo e piattaforma applicativa | application server, servizi di database, middleware |
| **SaaS** — Software as a Service | un'applicazione gestita dal provider | accesso via browser o app mobile |

**Modelli di deployment (p. 88):** *privato* (una sola organizzazione, gestito da lei o da terzi, on o off premises), *community* (organizzazioni con interessi comuni), *pubblico* (offerto al pubblico, operato da un provider), *ibrido* (infrastrutture distinte collegate per la portabilità di dati e applicazioni).

## Esempi espansi

![[lez08-stili-p87-responsabilita-cloud.png]]
*Responsabilità nei modelli di servizio ([[05_Architectural_Styles_Complete.pdf#page=87]]): quattro colonne con lo stesso stack (Data, Application, MW/DBMS, Security, Operating Systems, Virtualization, Storage, Computing Resources, Networking, Data Centers). In blu ciò che gestisce il cliente, in verde ciò che gestisce il provider. On premise: tutto del cliente. IaaS: il provider gestisce da Virtualization in giù. PaaS: da MW/DBMS in giù (incluso sistema operativo, sicurezza). SaaS: tutto tranne i dati. Più si sale verso SaaS, meno il cliente gestisce.*

## Perché importa

Il cloud è il substrato su cui girano molte architetture moderne (container, [[microservices]]); distinguere grid (remote evaluation, [[mobile-code]]) e cloud è richiesto dalle slide ([[05_Architectural_Styles_Complete.pdf#page=79]]).

## Connessioni

- [[mobile-code]]: grid ≠ cloud.
- [[microservices]]: deployment tipico sul cloud.

## Fonti

- [[architectural-styles]]; [[05_Architectural_Styles_Complete.pdf#page=84]]–[[05_Architectural_Styles_Complete.pdf#page=88]]

_Aggiornato: 2026-11-24 — ingest 05_Architectural_Styles_Complete.pdf_
