---
tipo: fonte
titolo: "Quality Attributes of an Architecture — Modifiability"
file_raw: "03-Modifiability.pdf"
pagine: "1-33"
data_ingest: 2026-09-30
formato: slide-pdf
riferimento_libro: "Bass, Clements, Kazman — Software Architecture in Practice, capp. 4-13"
argomenti: [modifiability, costi dopo il rilascio, quattro domande, quando e chi modifica, costo della modifica, debito tecnico, scalability, variability, portability, location independence, scenario generale e concreto di modifiability, tattiche increase cohesion, reduce coupling, defer binding, binding time, client-server, plug-in, layers, publish-subscribe]
---

# Modifiability — 03-Modifiability.pdf

## Numerazione pagine ↔ slide

| Pagine PDF | Slide | Regola |
|---|---|---|
| 1–20 | 1–20 | slide = p. |
| 21 | — | nessun numero stampato |
| 22–33 | 23–34 | slide = p. + 1 |

Sulle slide di [[03-Modifiability.pdf#page=10]] e [[03-Modifiability.pdf#page=17]] ci sono **annotazioni a mano** in italiano, riportate nelle pagine del wiki.

## Sommario

Seconda lezione della serie «Quality Attributes of an Architecture». La **modificabilità** riguarda il cambiamento e serve a ridurne costo e rischio, perché la maggior parte dei costi arriva dopo il rilascio. Si pianifica con **quattro domande**: cosa può cambiare, con che probabilità, quando e chi fa il cambiamento (implementazione, compilazione, build, configurazione, esecuzione; sviluppatore, utente, amministratore, sistema) e quanto costa. Il costo ha due componenti (introdurre il meccanismo, usarlo); senza meccanismi, le modifiche frequenti generano **debito tecnico**; gli estremi sono «nessuna predisposizione» (costo pagato al momento del cambiamento) e «adattamento automatico» (costo pagato prima). La modificabilità ha varianti specifiche: **scalabilità** (orizzontale, verticale, elasticità), **variabilità** (linee di prodotto), **portabilità**, **indipendenza dalla posizione**. Seguono lo scenario generale e uno concreto (modificare l'interfaccia utente in meno di tre ore, con annotazione su MVC). Le **tattiche** sono increase cohesion (split module, redistribute responsibilities), reduce coupling (encapsulation, use an intermediary, abstract common service, restrict dependencies) e defer binding, organizzate per momento di binding con esempi tecnologici (Maven, Spring Boot, Spring Cloud, Java). Chiudono quattro **pattern per la modificabilità**: client-server, plug-in, layers, publish-subscribe, ognuno con benefici e trade-off.

## Punti chiave

1. Titolo della serie ([[03-Modifiability.pdf#page=1]]); sezione Modifiability ([[03-Modifiability.pdf#page=2]]).
2. Cambiamenti nei sistemi software e scopo della modificabilità ([[03-Modifiability.pdf#page=3]]).
3. Quattro domande ([[03-Modifiability.pdf#page=4]], [[03-Modifiability.pdf#page=5]]); quando e chi nell'Exam Booking System ([[03-Modifiability.pdf#page=6]]).
4. Due tipi di costo e debito tecnico ([[03-Modifiability.pdf#page=7]]); quando si paga il costo ([[03-Modifiability.pdf#page=8]]); i due estremi nell'esempio ([[03-Modifiability.pdf#page=9]]).
5. Varianti della modificabilità ([[03-Modifiability.pdf#page=10]]): scalabilità ([[03-Modifiability.pdf#page=11]]), variabilità ([[03-Modifiability.pdf#page=12]]), portabilità ([[03-Modifiability.pdf#page=13]]), indipendenza dalla posizione ([[03-Modifiability.pdf#page=14]]).
6. Scenario generale ([[03-Modifiability.pdf#page=15]], [[03-Modifiability.pdf#page=16]]); scenario concreto sull'interfaccia utente ([[03-Modifiability.pdf#page=17]]).
7. Albero delle tattiche ([[03-Modifiability.pdf#page=18]]); increase cohesion ([[03-Modifiability.pdf#page=19]]).
8. Reduce coupling: definizione e tre tattiche ([[03-Modifiability.pdf#page=20]], [[03-Modifiability.pdf#page=21]]); restrict dependencies ([[03-Modifiability.pdf#page=22]]).
9. Defer binding: definizione ([[03-Modifiability.pdf#page=23]]); tattiche per momento di binding ([[03-Modifiability.pdf#page=24]]); esempi con tecnologie ([[03-Modifiability.pdf#page=25]]).
10. Pattern per la modificabilità ([[03-Modifiability.pdf#page=26]], [[03-Modifiability.pdf#page=27]]): client-server ([[03-Modifiability.pdf#page=28]], [[03-Modifiability.pdf#page=29]]), plug-in ([[03-Modifiability.pdf#page=30]]), layers ([[03-Modifiability.pdf#page=31]]), publish-subscribe ([[03-Modifiability.pdf#page=32]], [[03-Modifiability.pdf#page=33]]).

## Concetti introdotti

- [[modifiability]]
- [[tattiche-modifiability]]
- [[pattern-modifiability]]
- Entità: [[plug-in]], [[publish-subscribe]]; aggiornate [[client-server]] e [[layered]]
- Esercizi: casi aggiunti a [[scenari-di-qualita-concreti]] e [[applicazione-tattiche]]

## Domande aperte

- Tattica *Aspects* nell'albero di [[03-Modifiability.pdf#page=18]]: non spiegata.
- L'annotazione a mano di [[03-Modifiability.pdf#page=17]] cita MVC, non ancora trattato.
- Refusi nell'albero di [[03-Modifiability.pdf#page=18]]: «Couple-Time Parameterization» per *Compile-Time*, «Ristrict Dependencies» per *Restrict*.

## Domande da esame

- Perché la modificabilità è importante? Quali sono le quattro domande per pianificarla?
- In quali momenti si può fare un cambiamento e chi lo fa? Esempi.
- Quali costi comporta la modificabilità? Cos'è il debito tecnico?
- Definisci scalabilità (orizzontale/verticale, elasticità), variabilità, portabilità e indipendenza dalla posizione.
- Descrivi le tattiche di increase cohesion, reduce coupling e defer binding con esempi.
- Cos'è il binding? Elenca le tattiche per momento di binding.
- Descrivi i pattern client-server, plug-in, layers e publish-subscribe con benefici e trade-off.

_Aggiornato: 2026-09-30 — ingest_
