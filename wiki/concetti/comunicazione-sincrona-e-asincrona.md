---
tipo: concetto
importanza_esame: media
prerequisiti: ["servizi-e-soa"]
fonti_pdf: ["07— Service-Oriented and Microservice Architectures-1 part.pdf#page=20"]
termine_inglese: "synchronous and asynchronous communication"
---

# Comunicazione sincrona e asincrona tra servizi

## Definizione

> 📄 Fonte: [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=20]], [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=21]]

**Sincrona:** il chiamante invia una richiesta e **attende la risposta** entro un limite di tempo. **Asincrona:** un produttore invia un messaggio per un'elaborazione successiva, tramite coda o broker, senza attendere il completamento.

## Spiegazione

> 📄 Fonte: [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=20]], [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=21]]

| | Sincrona | Asincrona |
|---|---|---|
| Quando | serve una risposta immediata; facile da seguire | elaborazione differibile; assorbire picchi |
| Vantaggi | flusso lineare | il **buffering** assorbe picchi di carico o indisponibilità temporanea dei consumer |
| Rischi | catene lunghe di chiamate allungano il tempo di risposta e **propagano i guasti**; il **timeout** limita l'attesa ma lascia **incerto l'esito** (il server può aver completato o no) | ritardi di consegna, ordinamento, **elaborazione duplicata** richiedono decisioni esplicite |
| Contratto | operazione richiesta/risposta | deve distinguere **accettazione del messaggio** da **completamento dell'operazione** e dire come si gestiscono i fallimenti |

> 🧩 Elaborazione mia: il timeout non dice se l'operazione è fallita; per questo, ritentare una richiesta non idempotente (ad es. `POST /orders`) può creare duplicati — è la ragione per cui la slide chiede decisioni esplicite su duplicati e recupero.

## Perché importa

La scelta incide su disponibilità, prestazioni e accoppiamento ([[availability]], [[disaccoppiamento-dei-componenti]]): l'asincrono realizza il time e synchronization decoupling, il sincrono lascia più semplice la comprensione.

## Connessioni

- [[publish-subscribe]], [[event-based]]: comunicazione asincrona per eventi.
- [[contratti-e-api-di-servizio]]: operazioni e eventi.
- [[circuit-breaker]]: protegge dalle catene di chiamate sincrone che propagano guasti.

## Fonti

- [[service-oriented-and-microservice-architectures]]; [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=20]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=21]]

_Aggiornato: 2026-11-24 — ingest 07— Service-Oriented and Microservice Architectures-1 part.pdf_
