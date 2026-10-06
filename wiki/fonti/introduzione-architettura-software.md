---
tipo: fonte
titolo: "Software Architecture — An Introduction (parte 1)"
file_raw: "01-IntroductionOnSoftwareArchitecture.pdf"
pagine: "1-50"
data_ingest: 2026-09-26
formato: slide-pdf
riferimento_libro: "Bass, Clements, Kazman — Software Architecture in Practice, cap. 1"
argomenti: [definizione di architettura, strutture e viste, strutture di modulo, decomposizione, uses, layer, class, data model, componenti e connettori, allocazione, deployment, install view, Exam Booking System, scelta delle strutture, raccomandazioni di processo, Attribute-Driven Design, regole pratiche]
---

# Introduzione all'architettura software (parte 1) — 01-IntroductionOnSoftwareArchitecture.pdf

Numerazione: pagina del PDF = numero stampato sulla slide.

## Sommario

Prima parte della lezione sul capitolo 1 di *Software Architecture in Practice* ([[software-architecture-in-practice]]). La lezione ha tre sezioni (1. cos'è l'architettura; 2. attributi di qualità; 3. perché è importante): questo PDF copre la prima. L'architettura è definita come **l'insieme delle strutture necessarie per ragionare sul sistema** (elementi, relazioni, proprietà); una struttura è architetturale se serve a ragionare su un attributo importante per qualche stakeholder. Le strutture sono di tre categorie — **modulo**, **componenti e connettori**, **allocazione** — ognuna rappresentata da viste diverse, come le viste di un corpo umano per medici diversi. Un **esempio guida**, l'Exam Booking System, è esaminato con le tre viste: la vista dei moduli per la **modificabilità** (dove mettere le regole di ammissione, eventi al posto di dipendenze dirette, un modulo che nasconde i dati degli studenti), la vista runtime per **prestazioni e resilienza** (notifica asincrona tramite coda e suo trade-off) e le domande su sicurezza e scalabilità, la vista di deployment per **disponibilità e scalabilità** (replicazione dietro un load balancer e il limite del componente meno scalabile). Per ogni categoria vengono mostrati esempi di strutture utili (decomposizione, uses, layer, class, data model; C&C, client-server ATM, servizi; deployment e install). Chiudono i criteri per scegliere le strutture, le raccomandazioni di processo, il diagramma dell'**Attribute-Driven Design** e le regole pratiche per buone strutture.

## Punti chiave

1. Outline della lezione in tre sezioni ([[01-IntroductionOnSoftwareArchitecture.pdf#page=2]]); ruolo dell'architettura nei processi di sviluppo, esempio dei microservizi ([[01-IntroductionOnSoftwareArchitecture.pdf#page=3]]).
2. Definizione di Bass, Clements, Kazman; più strutture, ciascuna una prospettiva; differenza dalle definizioni precedenti ([[01-IntroductionOnSoftwareArchitecture.pdf#page=4]]).
3. Tre categorie di strutture; criterio di struttura architetturale; insieme né fisso né limitato ([[01-IntroductionOnSoftwareArchitecture.pdf#page=5]]); analogia del corpo umano ([[01-IntroductionOnSoftwareArchitecture.pdf#page=6]]).
4. Punti fermi: astrazione; design ≠ architettura; ogni sistema ha un'architettura; non tutte sono buone; l'architettura include il comportamento ([[01-IntroductionOnSoftwareArchitecture.pdf#page=7]]).
5. Moduli: unità di implementazione con responsabilità; relazioni uses, generalizzazione, is-part-of; vista statica ([[01-IntroductionOnSoftwareArchitecture.pdf#page=9]]); notazione UML ([[01-IntroductionOnSoftwareArchitecture.pdf#page=10]]); domande; strumento principale per la modificabilità ([[01-IntroductionOnSoftwareArchitecture.pdf#page=11]]).
6. Exam Booking System e le sue tre viste ([[01-IntroductionOnSoftwareArchitecture.pdf#page=12]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=13]]); vista uses ([[01-IntroductionOnSoftwareArchitecture.pdf#page=14]]); ragionamento di modificabilità ([[01-IntroductionOnSoftwareArchitecture.pdf#page=15]]); versione con contratto di eventi e Student Records ([[01-IntroductionOnSoftwareArchitecture.pdf#page=16]]).
7. Strutture di modulo utili: decomposizione ([[01-IntroductionOnSoftwareArchitecture.pdf#page=18]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=19]]), uses e social debt ([[01-IntroductionOnSoftwareArchitecture.pdf#page=20]]), layer e portabilità ([[01-IntroductionOnSoftwareArchitecture.pdf#page=21]]), class ([[01-IntroductionOnSoftwareArchitecture.pdf#page=22]]), data model ([[01-IntroductionOnSoftwareArchitecture.pdf#page=23]]).
8. C&C: componenti = unità di computazione, connettori = veicoli di comunicazione ([[01-IntroductionOnSoftwareArchitecture.pdf#page=25]]); esempio con publish-subscribe e failover ([[01-IntroductionOnSoftwareArchitecture.pdf#page=26]]); domande e proprietà runtime ([[01-IntroductionOnSoftwareArchitecture.pdf#page=27]]).
9. Vista runtime dell'Exam Booking System, flusso di una richiesta, trade-off della notifica asincrona ([[01-IntroductionOnSoftwareArchitecture.pdf#page=28]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=29]]); domande per prestazioni, disponibilità, sicurezza, scalabilità ([[01-IntroductionOnSoftwareArchitecture.pdf#page=30]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=31]]).
10. C&C ortogonali ai moduli; stili di connettori ([[01-IntroductionOnSoftwareArchitecture.pdf#page=33]]); client-server ATM su socket TCP ([[01-IntroductionOnSoftwareArchitecture.pdf#page=34]]); struttura a servizi ([[01-IntroductionOnSoftwareArchitecture.pdf#page=35]]); relazioni tra strutture ([[01-IntroductionOnSoftwareArchitecture.pdf#page=36]]).
11. Allocazione: corrispondenza con strutture non software; tre domande ([[01-IntroductionOnSoftwareArchitecture.pdf#page=38]]); deployment iniziale e scalabile ([[01-IntroductionOnSoftwareArchitecture.pdf#page=39]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=40]]); «il sistema è limitato dal componente meno scalabile» ([[01-IntroductionOnSoftwareArchitecture.pdf#page=41]]).
12. Tre stili di allocazione e usi della vista di deployment ([[01-IntroductionOnSoftwareArchitecture.pdf#page=43]]); deployment structure ([[01-IntroductionOnSoftwareArchitecture.pdf#page=44]]); install view informale e UML ([[01-IntroductionOnSoftwareArchitecture.pdf#page=45]], [[01-IntroductionOnSoftwareArchitecture.pdf#page=46]]).
13. Quali strutture scegliere; pattern come strategie preconfezionate ([[01-IntroductionOnSoftwareArchitecture.pdf#page=47]]).
14. Raccomandazioni di processo ([[01-IntroductionOnSoftwareArchitecture.pdf#page=48]]); Attribute-Driven Design ([[01-IntroductionOnSoftwareArchitecture.pdf#page=49]]); regole pratiche ([[01-IntroductionOnSoftwareArchitecture.pdf#page=50]]).

Pagine di sola intestazione di sezione: [[01-IntroductionOnSoftwareArchitecture.pdf#page=8]] (Module Structures), [[01-IntroductionOnSoftwareArchitecture.pdf#page=17]] (Examples of Useful Module Structures), [[01-IntroductionOnSoftwareArchitecture.pdf#page=24]] (C&C), [[01-IntroductionOnSoftwareArchitecture.pdf#page=32]] (Examples of Useful C&C Structures), [[01-IntroductionOnSoftwareArchitecture.pdf#page=37]] (Allocation Structures), [[01-IntroductionOnSoftwareArchitecture.pdf#page=42]] (Examples of Allocation Structures).

## Concetti introdotti

- [[architettura-software]]
- [[strutture-e-viste]]
- [[strutture-di-modulo]]
- [[strutture-componenti-e-connettori]]
- [[strutture-di-allocazione]]
- [[buone-pratiche-architetturali]]
- Entità: [[exam-booking-system]], [[uml]], [[attribute-driven-design]], [[client-server]], [[layered]], [[microservices]], [[software-architecture-in-practice]]

## Domande aperte

- Lo stile di allocazione **work assignment** è solo nominato ([[01-IntroductionOnSoftwareArchitecture.pdf#page=43]]): nessun esempio.
- Nella figura dell'ADD compaiono strutture non spiegate: *Concurrency*, *Process*, *Shared Data*, *Implementation* ([[01-IntroductionOnSoftwareArchitecture.pdf#page=49]]).
- La slide [[01-IntroductionOnSoftwareArchitecture.pdf#page=47]] cita una «vista di concorrenza» mai definita nella lezione.
- Refuso: «Nowasdays» per «Nowadays» ([[01-IntroductionOnSoftwareArchitecture.pdf#page=34]]); «allocatedto» senza trattino ([[01-IntroductionOnSoftwareArchitecture.pdf#page=44]]); «instanciates» per «instantiates» ([[01-IntroductionOnSoftwareArchitecture.pdf#page=49]]).

## Domande da esame

- Dai la definizione di architettura software di Bass, Clements e Kazman e commentala.
- Quando una struttura è architetturale? Quali sono le tre categorie di strutture e a quali domande rispondono?
- Cos'è un modulo? Quali relazioni esistono tra moduli? Perché le viste di modulo servono per la modificabilità?
- Descrivi decomposizione, uses e layer structure. Cos'è il *social debt*?
- Cosa sono componenti e connettori? Perché le strutture C&C sono ortogonali a quelle di modulo?
- Quali domande si pongono alla vista runtime per prestazioni, disponibilità, sicurezza e scalabilità?
- Replicare l'application server elimina tutti i colli di bottiglia? Perché?
- Cosa sono deployment e install view? Cosa indicano gli stereotipi «artifact» e «manifest»?
- Quali raccomandazioni di processo valgono per costruire buone architetture?

_Aggiornato: 2026-09-26 — ingest_
