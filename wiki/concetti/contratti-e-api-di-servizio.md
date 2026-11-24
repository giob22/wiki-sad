---
tipo: concetto
importanza_esame: alta
prerequisiti: ["servizi-e-soa"]
fonti_pdf: ["07— Service-Oriented and Microservice Architectures-1 part.pdf#page=18"]
termine_inglese: "service contracts and APIs (command, query, event; REST; SOAP/WSDL; OpenAPI)"
---

# Contratti e API di servizio

## Definizione

> 📄 Fonte: [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=18]], [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=22]], [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=23]]

Un'**API** definisce come i client software interagiscono con una capacità; un'**API HTTP** espone le interazioni tramite **URI, metodi, header e rappresentazioni**. La **specifica** dell'API è il contratto tra servizio e client: operazioni e significato, struttura di richieste e risposte, ingressi richiesti, errori, requisiti di autenticazione. Un contratto distingue **comandi** (richiedono un'azione: `createOrder`), **query** (recuperano informazioni: `findOrderById`) ed **eventi** (riportano un fatto: `OrderCreated`) ([[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=18]]).

## Spiegazione

> 📄 Fonte: [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=19]]

![[lez10-soa-p19-comandi-query-eventi.png]]
*Il client dell'Order Service invoca l'API di servizio, che definisce operazioni (comandi `createOrder()`, query `findOrderById()`); l'Order Service pubblica eventi (OrderCreated, OrderCancelled) quando i dati cambiano e i sottoscrittori li ricevono.*

I tre elementi hanno **direzioni diverse**: il client *chiama* comandi e query (richiesta/risposta) e *riceve* eventi pubblicati (verso i sottoscrittori, come in [[publish-subscribe]]).

## Esempi espansi

**Creare un ordine (p. 24)** — specifica di `POST /orders`:

| Voce | Valore |
|---|---|
| Ingresso | id del ristorante e lista non vuota di articoli (id e quantità positiva) |
| Successo | **201 Created**, con id ordine, stato iniziale e header `Location` |
| Errori | **400** ingresso non valido; **401** credenziali mancanti/non valide; **403** permessi insufficienti |
| Autenticazione | **Bearer token** nella richiesta |

**Risorse e metodi HTTP (p. 25).** `GET /orders/{id}` recupera; `POST /orders` crea; `PUT /orders/{id}` sostituisce lo stato (`PATCH` per aggiornamenti parziali); `DELETE /orders/{id}` rimuove secondo le regole di business. Rappresentazione JSON 📄:

```json
{ "id": 123, "restaurantId": 42, "status": "PENDING" }
```

**Risposte ed errori (p. 26).** 200 OK; 201 Created (con `Location`); 400 Bad Request e 404 Not Found (richiesta non valida vs risorsa mancante); 409 Conflict (conflitto di stato); i corpi degli errori spiegano il problema in modo coerente.

**Richieste stateless (p. 27).** Ogni richiesta contiene il contesto necessario; il server può comunque memorizzare ordini e anagrafiche; un **token** porta l'autenticazione senza sessione in una singola istanza; semplifica l'instradamento tra repliche; le dipendenze condivise dai dati richiedono comunque recupero.

**REST (p. 28).** *Representational State Transfer*: stile per sistemi ipermediali distribuiti. Risorse identificate da URI, scambio di rappresentazioni. Vincoli: **client–server, stateless, caching, interfaccia uniforme, sistema a strati**; *code on demand* opzionale ([[mobile-code]]). L'interfaccia uniforme include messaggi autodescrittivi e ipermedia. **Usare solo HTTP e JSON non rende un'API RESTful.**

**SOAP e WSDL (pp. 29–30).** SOAP: framework di messaggistica XML, spesso su HTTP; **WSDL** descrive interfaccia e binding; WS-\* per sicurezza e messaggistica affidabile.

| Parte di un WSDL (p. 30) | Contenuto | Astratto/concreto |
|---|---|---|
| `types` e `message` | dati scambiati (XML Schema) | astratto |
| `portType` / operations | interfaccia astratta (operazioni su messaggi in/out) | astratto |
| `binding` | formati di messaggio e protocolli | concreto |
| `service` / endpoint | dove si raggiunge il servizio | concreto |

![[lez10-soa-p30-struttura-wsdl.png]]
*Documento WSDL commentato con le cinque sezioni: types, message, portType, binding, service ([[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=30]]).*

**OpenAPI (pp. 31–32).** Descrive percorsi, operazioni, parametri, risposte di un'API HTTP; gli *schemi* definiscono la struttura delle rappresentazioni; YAML o JSON; gli strumenti generano documentazione e codice client/scheletri server. Esempio 📄:

```yaml
openapi: 3.1.0
info: {title: FTGO API, version: '1.0'}
paths:
  /orders/{id}:
    get:
      parameters:
        - {name: id, in: path, required: true, schema: {type: integer}}
      responses:
        '200':
          description: Order found
        '404':
          description: Order not found
```
*🧩 Commento: descrive l'operazione `GET /orders/{id}` con parametro di percorso intero obbligatorio e due risposte (200 trovato, 404 non trovato), cioè lo stesso contratto della sezione HTTP.*

**Evoluzione del contratto (p. 33).**

| Tipo di cambiamento | Esempio | Effetto |
|---|---|---|
| Compatibile | aggiungere un campo di risposta opzionale (i client ignorano i campi sconosciuti) | client e provider si aggiornano in modo indipendente |
| Incompatibile (*breaking*) | nuovo campo di ingresso obbligatorio; cambiare tipo o significato di un campo; 200 al posto di 404 | rompe i client |

Per i cambiamenti incompatibili: percorso di migrazione, periodo di supporto della vecchia versione, data di ritiro (*versioning*). I **contract test** verificano le interazioni concordate (es. 404 per ordine mancante) e tengono allineati specifica, implementazione e aspettative dei consumer.

## Perché importa

Il contratto è ciò che permette l'**accoppiamento debole** ([[servizi-e-soa]]) e l'evoluzione indipendente; gestirne l'evoluzione è parte della [[modifiability]].

## Connessioni

- [[servizi-e-soa]]: il contratto di servizio.
- [[comunicazione-sincrona-e-asincrona]]: come si invocano le operazioni.
- [[publish-subscribe]]: gli eventi pubblicati.
- [[microservices]]: le API sono il confine dei servizi.

## Fonti

- [[service-oriented-and-microservice-architectures]]; [[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=18]]–[[07— Service-Oriented and Microservice Architectures-1 part.pdf#page=33]]

_Aggiornato: 2026-11-24 — ingest 07— Service-Oriented and Microservice Architectures-1 part.pdf_
