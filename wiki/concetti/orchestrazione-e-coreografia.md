---
tipo: concetto
importanza_esame: alta
prerequisiti: ["servizi-e-soa", "comunicazione-sincrona-e-asincrona"]
fonti_pdf: ["07— Service-Oriented and Microservice Architectures-1 part.pdf#page=43"]
termine_inglese: "orchestration and choreography"
---

# Orchestrazione e coreografia

## Definizione

> 🔑 Definizione chiave — 📄 Fonte: [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=43]], [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=44]]

**Orchestrazione:** un **coordinatore** controlla il flusso di lavoro e chiama i servizi partecipanti (un servizio di orchestrazione dedicato, un componente dentro un servizio applicativo o un *workflow engine*). **Coreografia:** i partecipanti **reagiscono a eventi o messaggi** secondo le proprie regole; nessun componente emette ogni passo; il coordinamento è distribuito nei contratti dei partecipanti.

## Spiegazione

> 📄 Fonte: [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=43]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=46]]

| | Orchestrazione | Coreografia |
|---|---|---|
| Controllo | centrale (il coordinatore tiene lo stato: avanzamento e prossimo passo) | distribuito |
| Vantaggio | più facile **trovare le decisioni** di workflow | accoppiamento ridotto, ogni partecipante reagisce in modo indipendente |
| Svantaggio | richiede logica di recupero e gestione esplicita dei guasti dei partecipanti | **tracciare il processo di business** e cambiare le dipendenze tra eventi è più difficile |

**Come scegliere (p. 46):** si valutano **visibilità dell'avanzamento, recupero dei guasti e accoppiamento**.

## Esempi espansi

![[lez10-soa-p45-coordinamento-shopping-online.png]]
*Coordinamento nello shopping online ([[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=45]]): le interazioni utente (Customer Interaction, Supplier Interaction) passano per tre **coordinatori** (Customer, Supplier, Billing) che chiamano **servizi di capacità** (Email, CreditCard, CustomerAccount, Catalog, DeliveryOrder, Inventory). L'esempio separa i coordinatori dai servizi di capacità; il progetto dettagliato dice quali passi richiedono risposte, callback o recupero.*

**FTGO: il ristorante rifiuta l'ordine (pp. 46–47).** Situazione: ordine in attesa, pagamento già autorizzato.

| Passo | Orchestrazione | Coreografia di eventi |
|---|---|---|
| 1 | Restaurant service invia il rifiuto all'**Order orchestrator** | Restaurant service pubblica `RestaurantRejectedOrder` sull'**Event broker** |
| 2 | l'orchestrator registra l'avanzamento | il broker consegna l'evento a Payment e Order service |
| 3 | chiede a Payment service di rilasciare l'autorizzazione | Payment service rilascia l'autorizzazione (da solo) |
| 4 | chiede a Order service di segnare l'ordine REJECTED | Order service segna l'ordine REJECTED (da solo) |

![[lez10-soa-p47-ftgo-rifiuto-ristorante.png]]
*Le due soluzioni a confronto ([[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=47]]): a sinistra l'orchestrator coordina il recupero; a destra i servizi reagiscono in modo indipendente all'evento sul broker.*

> 🧩 Elaborazione mia: in orchestrazione basta guardare l'orchestrator per sapere a che punto è l'ordine (alta visibilità) ma esso è un punto da rendere resiliente; in coreografia aggiungere un nuovo reattore non richiede di toccare nessuno (basso accoppiamento) ma «dove è arrivato l'ordine?» richiede di correlare gli eventi.

## Perché importa

È la decisione tipica nella progettazione di sistemi a servizi (e nel progetto di corso, se si usano microservizi): rapporta controllo e accoppiamento. La coreografia si regge su [[event-based]] e [[publish-subscribe]].

## Connessioni

- [[comunicazione-sincrona-e-asincrona]]: l'orchestrazione usa spesso chiamate sincrone; la coreografia è asincrona.
- [[intermediari-di-servizio]]: l'event broker.
- [[microservices]], [[servizi-e-soa]].

## Fonti

- [[service-oriented-and-microservice-architectures]]; [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=43]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=47]]

_Aggiornato: 2026-11-24 — ingest 07— Service-Oriented and Microservice Architectures-1 part.pdf_
