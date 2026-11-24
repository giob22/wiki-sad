---
tipo: esercizio
argomento: "scrivere criteri di accettazione e tradurli in scenari BDD (Given–When–Then)"
difficoltà: bassa
---

# Dai criteri di accettazione agli scenari BDD

## Metodo

> 📄 Fonte: [[04_Agile_01_bis.pdf#page=52]], [[04_Agile_01_bis.pdf#page=55]], [[04_Agile_01_bis.pdf#page=61]]

1. **Discussione**: per la storia, elenca le domande aperte (durate, limiti, casi d'errore, cosa vede l'utente).
2. **Criteri**: trasforma ogni risposta in un criterio di accettazione verificabile, con valori concreti.
3. **Scenari**: per ogni criterio scrivi almeno uno scenario **Given** (contesto iniziale) – **When** (azione/evento) – **Then** (risultato atteso), con **And** per i risultati aggiuntivi.
4. Per ogni criterio con un **limite** (tempo, lunghezza, numero di tentativi) scrivi **due scenari**: uno **positivo** dentro il limite e uno **negativo** fuori.
5. Usa **valori concreti** negli scenari (20 minuti, 35 minuti, 8 caratteri): sono quelli che diventano dati di test.

## Concetti usati

[[criteri-di-accettazione-e-bdd]] · [[user-stories]]

## Casi svolti

### Caso 1 — Recupero della password

**Traccia:** [[04_Agile_01_bis.pdf#page=52]] (storia e criteri), [[04_Agile_01_bis.pdf#page=57]]–[[04_Agile_01_bis.pdf#page=60]] (scenari).

**Storia:** come cliente, voglio recuperare la mia password così da poter accedere di nuovo al sistema.

| Criterio | Scenari della slide |
|---|---|
| 1. Il link è valido 30 minuti | **positivo**: link usato entro la validità; **negativo**: link usato dopo la scadenza ([[04_Agile_01_bis.pdf#page=57]]) |
| 2. Ogni link si usa una sola volta | riuso di un link già usato ([[04_Agile_01_bis.pdf#page=58]]) |
| 3. La password nuova ha almeno 12 caratteri | **scenario 1**: password valida; **scenario 2**: password troppo corta ([[04_Agile_01_bis.pdf#page=59]]) |
| 4. Email inesistente → messaggio generico | richiesta di reset con email non registrata ([[04_Agile_01_bis.pdf#page=60]]) |

**Gli scenari in Gherkin** (📄 il contenuto è delle slide; 🧩 la formattazione come file `.feature` e la traduzione in italiano sono mie):

```gherkin
# 📄 slide 56-59 — 🧩 impaginato come file Gherkin
Feature: Recupero della password
  Come cliente voglio recuperare la mia password
  così da poter accedere di nuovo al sistema

  # Criterio 1 — il link è valido 30 minuti
  Scenario: Uso del link entro i 30 minuti di validità
    Given un utente ha ricevuto il link di reset 20 minuti fa
    When apre il link
    Then il sistema permette di inserire una nuova password

  Scenario: Uso del link dopo la scadenza
    Given un utente ha ricevuto il link di reset 35 minuti fa
    When apre il link
    Then il sistema lo informa che il link è scaduto
    And gli chiede di richiederne uno nuovo

  # Criterio 2 — ogni link si usa una sola volta
  Scenario: Riuso di un link già usato
    Given un utente ha già usato il link di reset
    When prova a usarlo una seconda volta
    Then il sistema rifiuta la richiesta
    And mostra un messaggio che dice che il link non è più valido

  # Criterio 3 — almeno 12 caratteri
  Scenario: Password valida
    Given un utente ha aperto un link di reset valido
    When inserisce una password di almeno 12 caratteri
    Then il sistema aggiorna la password
    And conferma che l'operazione è completata

  Scenario: Password troppo corta
    Given un utente ha aperto un link di reset valido
    When inserisce una password di 8 caratteri
    Then il sistema rifiuta la password
    And lo informa che la lunghezza minima è 12 caratteri

  # Criterio 4 — email inesistente
  Scenario: Richiesta di reset con email non registrata
    Given l'email "utente@example.com" non è presente nel sistema
    When viene richiesto il recupero della password
    Then il sistema mostra un messaggio generico
    And non rivela se l'indirizzo email è registrato o no
```

**Svolgimento (🧩) — perché questi scenari:**
- **20 e 35 minuti** stanno uno sotto e uno sopra il limite di 30: verificano il confine da entrambi i lati. Un test ancora più rigoroso proverebbe anche **esattamente 30 minuti**, per decidere se il limite è incluso: il criterio non lo dice, ed è una domanda da riportare alla discussione con il PO.
- Allo stesso modo, per la password si potrebbe provare **11 e 12 caratteri**, i valori a ridosso del limite.
- Il criterio 2 ha un solo scenario: il caso positivo (primo uso) è già coperto dal criterio 1.
- Lo scenario del criterio 4 controlla **due** cose (messaggio generico **e** nessuna rivelazione dell'email): la seconda è il motivo di sicurezza del criterio.

**Risultato:** 4 criteri → **6 scenari**. È la conclusione della slide 60: non c'è corrispondenza uno-a-uno, un criterio può richiedere più scenari, e si passa da un requisito funzionale a test eseguibili.

> 📚 Fonte esterna: un file `.feature` come questo si esegue con strumenti BDD come **Cucumber** (per Java), che collegano ogni riga Given/When/Then a un metodo di test. Le slide non citano strumenti.

### Caso 2 — Scenari per il login (esercizio mio sui criteri della slide)

> 🧩 Esercizio mio sui criteri di [[04_Agile_01_bis.pdf#page=53]]: applico il metodo a due dei cinque criteri.

```gherkin
Feature: Login con email e password

  # AC2 — password errata, messaggio che non dice quale credenziale è sbagliata
  Scenario: Password errata
    Given un utente registrato con email "mario@example.com"
    When effettua il login con la password sbagliata
    Then il sistema mostra un messaggio di errore
    And il messaggio non indica se è sbagliata l'email o la password

  # AC4 — blocco dopo 5 tentativi falliti (limite → scenario positivo e negativo)
  Scenario: Quarto tentativo fallito, account ancora attivo
    Given un utente ha sbagliato la password 3 volte di seguito
    When sbaglia la password una quarta volta
    Then l'account non viene bloccato

  Scenario: Quinto tentativo fallito, account bloccato
    Given un utente ha sbagliato la password 4 volte di seguito
    When sbaglia la password una quinta volta
    Then l'account viene bloccato per 15 minuti
```

## Trappole

- Scrivere scenari **senza valori concreti** («dopo un po' di tempo»): non diventano test.
- Dimenticare lo **scenario negativo** per i criteri con un limite.
- Mettere dettagli d'implementazione negli scenari (tabelle, classi): il BDD descrive il **comportamento** dal punto di vista dell'utente.
- Pensare che ogni criterio dia esattamente uno scenario.

_Aggiornato: 2026-10-10 — ingest 04_Agile_01_bis.pdf_
