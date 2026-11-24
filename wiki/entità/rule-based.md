---
tipo: entità
categoria: stile
famiglia: "shared memory"
---

# Rule-based

## Contesto e problema

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=66]]

Applicazioni la cui logica si esprime come **conoscenza dichiarativa** (fatti e regole) e il cui comportamento deve poter cambiare aggiungendo o togliendo regole: sistemi esperti, applicazioni di intelligenza artificiale.

## Soluzione

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=66]], [[05_Architectural_Styles_Complete.pdf#page=67]]

- **Componenti:** interfaccia utente, **motore inferenziale** (*inference engine*), **base di conoscenza** (*knowledge base*).
- **Connettori:** chiamate di procedura e accesso alla memoria condivisa (legano strettamente i componenti).
- **Elementi dati:** fatti e query; **regole di produzione** IF … THEN.
- **Topologia:** tre parti principali.
- **Funzionamento:** l'utente aggiunge fatti o regole alla base di conoscenza; per una query o un obiettivo, il motore applica le regole per stabilire se l'obiettivo è soddisfatto.
  - *Forward chaining:* parte dai dati e applica le regole derivando nuovi fatti («lo studente è idoneo»).
  - *Backward chaining:* parte da un obiettivo («lo studente è idoneo?») e verifica le condizioni necessarie.
- Stile tipico dei sistemi esperti (inclusi quelli in Prolog).

## Diagramma

![[lez08-stili-p68-rule-based-lunar-lander.png]]
*Lunar Lander rule-based ([[05_Architectural_Styles_Complete.pdf#page=68]]): l'interfaccia utente fornisce il fatto `burnrate(25)` e l'obiettivo `landed(spacecraft)`; il motore inferenziale, tramite «Data Access», consulta la base di conoscenza (fatti a, br, f, t, v e la regola di atterraggio `landed(spacecraft)` con altitudine ≤ 0 e velocità < 3 ft/s) e risponde vero/falso.*

## Esempi espansi

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=70]], [[05_Architectural_Styles_Complete.pdf#page=71]]

**Conflitto tra regole (p. 70).** Regole: R1 `IF fever AND cough THEN suspect_flu`; R2 `IF fever AND rash THEN suspect_measles`; R3 `IF suspect_flu THEN prescribe_antiviral`; R4 `IF suspect_measles THEN prescribe_antibiotic`.

| Fatti presenti | Regole che scattano | Esito |
|---|---|---|
| fever, cough | R1 → R3 | sospetta influenza, antivirale |
| fever, rash | R2 → R4 | sospetto morbillo, antibiotico |
| fever, cough, rash | R1 **e** R2 insieme → R3 e R4 | due diagnosi e due terapie: esito potenzialmente conflittuale o incoerente |

🧩 Il problema è che nessuna regola dice come risolvere il conflitto: l'esito dipende dall'ordine di scatto e dalla strategia del motore. **Spiegabilità (p. 71):** per capire un risultato bisogna seguire tutta la catena di inferenza; per questo servono *inference tracing* e analisi dei log.

## Attributi di qualità

| Attributo | Effetto | Perché | Fonte |
|---|---|---|---|
| Modificabilità del comportamento | + | aggiungere/togliere regole cambia il comportamento senza toccare il codice | [[05_Architectural_Styles_Complete.pdf#page=67]] |
| Prototipazione rapida | + | adatto a applicazioni guidate da regole | [[05_Architectural_Styles_Complete.pdf#page=67]] |
| Comprensibilità delle interazioni | − | con molte regole è difficile capire come interagiscono quelle toccate dagli stessi fatti | [[05_Architectural_Styles_Complete.pdf#page=69]] |
| Spiegabilità | − | il ragionamento che porta a un risultato è difficile da ricostruire | [[05_Architectural_Styles_Complete.pdf#page=69]], [[05_Architectural_Styles_Complete.pdf#page=71]] |

## Quando usarlo / quando no

Per prototipi rapidi di applicazioni guidate da regole ([[05_Architectural_Styles_Complete.pdf#page=67]]); da evitare quando conta spiegare il risultato e le regole sono molte e interagenti.

## Varianti ed esempi

- Sistemi esperti, Prolog ([[05_Architectural_Styles_Complete.pdf#page=66]]).

## Connessioni

- [[repository]], [[blackboard]]: la base di conoscenza è la memoria condivisa.
- [[interpreter]]: anche il motore inferenziale «interpreta» regole.

## Fonti

- [[architectural-styles]]

_Aggiornato: 2026-11-24 — ingest 05_Architectural_Styles_Complete.pdf_
