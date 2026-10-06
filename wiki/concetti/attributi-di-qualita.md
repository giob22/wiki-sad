---
tipo: concetto
importanza_esame: alta
prerequisiti: ["architettura-software"]
fonti_pdf: ["01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=2", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=3", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=4", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=5", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=6", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=7", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=32", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=33"]
termine_inglese: "quality attribute (QA)"
---

# Attributi di qualità

## Definizione

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=2]] (slide 52)

> 🔑 Definizione chiave: un **attributo di qualità** (*quality attribute*, QA) è una **proprietà misurabile o verificabile** (*measurable or testable*) di un sistema, usata per indicare **quanto bene il sistema soddisfa le esigenze dei suoi stakeholder**, **oltre la funzione di base** del sistema.

La funzionalità è importante, ma gli attributi di qualità possono esserlo **ancora di più**: molti sistemi vanno **riprogettati** non per la funzionalità, ma perché sono difficili da **manutenere**, **portare** o **scalare**, perché sono **troppo lenti**, o perché sono stati **compromessi da attaccanti** ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=2]]).

## Requisiti funzionali e requisiti di qualità

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=3]] (slide 53), [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=4]] (slide 55)

- La **funzionalità** è la capacità del sistema di svolgere il lavoro per cui è stato pensato.
- **La funzionalità non determina l'architettura.** Si scompone l'architettura in moduli e si assegnano le responsabilità **in base alla qualità che si vuole ottenere**.
- Si progettano architetture modulari, a strati, a servizi, peer-to-peer… **perché si vogliono qualità diverse**; altrimenti si potrebbe progettare **un unico modulo monolitico** (*a single blob module*).

> 🧩 Elaborazione mia: qualunque funzionalità si può realizzare con un solo blocco di codice. Due architetture diverse possono offrire esattamente le stesse funzioni; ciò che le distingue sono le qualità (modificabilità, prestazioni…). Per questo il progetto architetturale è guidato dalle qualità.

**Requisiti funzionali e di qualità non vanno definiti separatamente** ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=4]]). Se la funzione del software è controllare un motore, come si può implementarla correttamente senza considerare il **comportamento temporale**? Meglio parlare di **responsabilità del software** e specificare, per ciascuna, le caratteristiche di qualità richieste. Domande come queste hanno senso e si possono tradurre in azioni:
- «Quali sono i **vincoli temporali** su quell'insieme di responsabilità?»
- «Quali **modifiche** sono previste per quell'insieme di responsabilità?»
- «Quale **classe di utenti** può eseguire quell'insieme di responsabilità?»

### Esempio espanso — una responsabilità con i suoi requisiti di qualità

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=5]] (slide 56)

La responsabilità **«verificare se uno studente può prenotare un esame»** dell'[[exam-booking-system]] richiede:

| Attributo | Requisito | 🧩 Cosa implica per l'architettura |
|---|---|---|
| **Performance** | il risultato deve arrivare entro **500 ms** con carico normale | percorso della richiesta corto; attenzione alle chiamate al SIS |
| **Availability** | se lo University SIS è temporaneamente indisponibile, il sistema deve dare una **risposta controllata entro 2 s** | timeout sulle chiamate al SIS e risposta di ripiego |
| **Security** | solo **studenti autenticati** e **applicazioni amministrative autorizzate** possono chiedere l'informazione | autenticazione e autorizzazione davanti alla funzione |
| **Modifiability** | una nuova regola sui prerequisiti si introduce modificando **solo Eligibility Checking e i suoi test** | regole concentrate in un modulo (*localize changes*) |
| **Testability** | Eligibility Checking deve essere **testabile senza collegarsi al SIS di produzione** | accesso al SIS dietro un'interfaccia sostituibile con un finto (*use an intermediary*, adapter) |

🧩 Ogni requisito è formulato in modo **misurabile o verificabile** (500 ms, 2 s, «solo Eligibility Checking»): è la definizione di attributo di qualità applicata. Le soluzioni della terza colonna sono le tattiche che la lezione mostra più avanti ([[tattiche-architetturali]]).

## Due categorie di attributi

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=6]] (slide 57)

| Categoria | Descrive una proprietà… | Esempi |
|---|---|---|
| **Runtime** | del **sistema in esecuzione** | availability, performance, usability |
| **Di sviluppo** | dello **sviluppo** del sistema | modifiability, testability, deployability |

Il programma nelle slide della presentazione parla di attributi **osservabili a runtime**, **non osservabili a runtime** e **intrinseci** ([[00_IntroduzioneAlCorso_SAD.pdf#page=15]]). Il programma ufficiale ([[Programma Syllabus]]) elenca:

| Classe (programma ufficiale) | Attributi | Pagine del wiki |
|---|---|---|
| **Osservabili a runtime** | performance, security, availability, functionality, usability | [[availability]] (Lez. 2) |
| **Non osservabili a runtime** | modifiability, portability, reusability, integrability, testability | [[modifiability]] (Lez. 3; la portabilità è trattata lì come sua variante) |

🧩 Corrisponde alla divisione runtime / sviluppo della Lez. 1. Gli attributi «intrinseci» delle slide di presentazione non compaiono nel programma ufficiale. TODO: da espandere quando la classificazione verrà spiegata a lezione.

Gli attributi trattati in dettaglio finora, ognuno con definizione, scenari, tattiche e pattern (capp. 4–13 di Bass, Clements, Kazman): [[availability]] e [[modifiability]].

## Trade-off tra attributi

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=6]] (slide 57)

> ⚖️ Trade-off: ottenere un attributo ha un effetto (**positivo o negativo**) su un altro. Esempio: per la **portabilità** si possono isolare le dipendenze dal sistema, ma questo introduce **overhead** nell'esecuzione e peggiora le **prestazioni**.

Altri trade-off visti nella lezione:

| Scelta | Migliora | Peggiora | Fonte |
|---|---|---|---|
| notifica asincrona tramite coda | tempo di risposta, resilienza | consistenza (finale), complessità gestione errori | [[01-IntroductionOnSoftwareArchitecture.pdf#page=29]] |
| invocazione indiretta (eventi) tra moduli | modificabilità, disponibilità | complessità | [[01-IntroductionOnSoftwareArchitecture.pdf#page=15]] |
| pattern Layers | modificabilità, testabilità, portabilità | latenza, complessità | [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=22]] |
| replicazione con load balancer | richieste servite in parallelo | gestione sessioni, sincronizzazione, concorrenza sui dati | [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=23]] |
| cache | latenza, carico sul DB | dati potenzialmente vecchi | [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=23]] |
| log degli eventi | auditing, rilevazione anomalie | i log contengono dati personali da proteggere | [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=27]] |

## Tre domande su architettura e qualità

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=7]] (slide 58)

1. Come **esprimere** le qualità che l'architettura deve avere? → [[scenari-di-qualita]]
2. Come **ottenerle** con mezzi architetturali? → [[tattiche-architetturali]], [[pattern-architetturali]]
3. Come **determinare le decisioni di progetto** da prendere rispetto a quelle qualità? → 🧩 nella lezione la risposta passa per la valutazione ([[valutazione-attributi-di-qualita]]) e per il metodo [[attribute-driven-design]].

## L'architettura abilita o inibisce le qualità

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=32]] (slide 83), [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=33]] (slide 84)

Se il sistema richiede…

| Qualità | A cosa prestare attenzione nell'architettura |
|---|---|
| **Alte prestazioni** | comportamento **temporale** degli elementi; uso di **risorse condivise**; **frequenza e volume** delle comunicazioni tra elementi |
| **Modificabilità** | **assegnazione delle responsabilità** agli elementi; **limitare le interazioni**, così che le modifiche tocchino pochi moduli |
| **Alta sicurezza** | gestire e **proteggere le comunicazioni** tra elementi; controllare **quali elementi accedono a quali informazioni**; eventualmente elementi specializzati **anti-intrusione** |
| **Scalabilità delle prestazioni** | **localizzare l'uso delle risorse** per poterle sostituire con altre di capacità maggiore; **evitare di codificare** ipotesi o limiti sulle risorse |
| **Riusabilità** degli elementi in altri sistemi | **limitare l'accoppiamento** tra elementi, così che un elemento estratto non si porti dietro troppi legami con l'ambiente attuale |

Naturalmente il progetto architetturale è importante, ma anche le **decisioni di progetto di dettaglio e di implementazione** influiscono sulla qualità finale ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=33]]).

## Perché importa

Gli attributi di qualità sono il **filo conduttore** del corso: si scelgono le strutture in base a essi ([[strutture-e-viste]]), si specificano con gli scenari, si ottengono con tattiche e pattern, si valutano sull'architettura. Il programma dedica loro un intero blocco: classificazione, specifica, tattiche, code smell, analisi statica e dinamica ([[00_IntroduzioneAlCorso_SAD.pdf#page=15]]).

> 🎯 Esame: definizione di QA; perché la funzionalità non determina l'architettura; runtime vs sviluppo; esempi di trade-off; le tre domande.

## Connessioni

- [[scenari-di-qualita]]: come specificare un QA in modo verificabile.
- [[tattiche-architetturali]]: come ottenerlo.
- [[valutazione-attributi-di-qualita]]: come verificarlo sull'architettura.
- [[importanza-architettura-software]]: §3.1 e §3.2 sono i paragrafi «abilita/inibisce» e «predice» le qualità.

## Fonti

- [[attributi-di-qualita-e-importanza-architettura]] — [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=1]]–[[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=7]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=32]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=33]]
- [[presentazione-corso]] — [[00_IntroduzioneAlCorso_SAD.pdf#page=15]]

_Aggiornato: 2026-09-26 — ingest lezione 1_
_Aggiornato: 2026-09-30 — classificazione del programma ufficiale; link ad availability e modifiability_
