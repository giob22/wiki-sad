---
tipo: progetto
stato: in attesa di assegnazione
data: 2026-09-26
sprint: ""
---

# Progetto di corso

Pagina di riferimento sul progetto software della classe, da quanto detto nella presentazione del corso. Le decisioni architetturali del team andranno in pagine separate di questa cartella (formato ADR, vedi CLAUDE.md).

## Organizzazione

> 📄 Fonte: [[00_IntroduzioneAlCorso_SAD.pdf#page=19]]–[[00_IntroduzioneAlCorso_SAD.pdf#page=23]]

- Il corso usa tre metodi: **lecture-based learning** (lezioni teoriche con slide, progetti software, esempi), **case-based learning** (applicare metodi e tecniche a casi di studio reali, a team, con discussioni, decisioni, brainstorming, presentazioni) e **team-based learning** ([[00_IntroduzioneAlCorso_SAD.pdf#page=19]]–[[00_IntroduzioneAlCorso_SAD.pdf#page=22]]).
- Benefici del lavoro a team: più motivazione, esperienza realistica, imparare a organizzarsi e comunicare in un gruppo di progetto, soft skill del mondo Agile — sprint/iterazioni, iteration review, requisiti come **user story**, framework **Scrum**, pair programming, project board ([[00_IntroduzioneAlCorso_SAD.pdf#page=22]]).
- **Tutta la classe** sviluppa **da zero un unico sistema software**, diviso in **sottosistemi sufficientemente autonomi**, ciascuno assegnato a un team. Dominio e requisiti sono definiti con un **partner industriale** o un'altra organizzazione esterna. Tutti i team contribuiscono all'**architettura comune** e all'**integrazione finale**. Gestione **Agile** ([[00_IntroduzioneAlCorso_SAD.pdf#page=23]]).

## Iterazioni

> 📄 Fonte: [[00_IntroduzioneAlCorso_SAD.pdf#page=24]]

| Iterazione | Attività principali | Risultato |
|---|---|---|
| 1. **Architectural inception** | analisi del dominio, requisiti di qualità, *bounded context*, scelta dello stile, definizione delle API | architettura comune e **backlog** |
| 2. **Independent development** | ogni team implementa il proprio sottosistema | servizi **funzionanti e testati** in modo indipendente |
| 3. **Integration and evaluation** | integrazione, test end-to-end, analisi di qualità, risoluzione dei problemi | **sistema complessivo eseguibile** |

![[lez00-intro-p24-sviluppo-progetto.png]]
*Figura di [[00_IntroduzioneAlCorso_SAD.pdf#page=24]]: «Shared Vision and Requirements» → «Architecture Defined by the Class» → tre sottosistemi (Team A, B, C) → «Final Integration»; sotto, la tabella delle iterazioni.*

> 💡 Connessione (🧩): la prima iterazione mette in pratica la lezione 1 — requisiti di qualità ([[scenari-di-qualita]]), scelta dello stile ([[pattern-architetturali]]), API come interfacce tra sottosistemi ([[importanza-architettura-software]] §3.6: i team comunicano tramite le specifiche delle interfacce).

## Dettagli tecnici

> 📄 Fonte: [[00_IntroduzioneAlCorso_SAD.pdf#page=25]], [[00_IntroduzioneAlCorso_SAD.pdf#page=26]]

- Gestione: framework Agile, ad esempio **Scrum**.
- Stili e pattern (facoltativi): **Web App con stile client-server** ([[client-server]]), **microservizi** ([[microservices]]), pattern **MVC**, stile **REST** e API.
- Tecnologie possibili: **Java**, **Spring Boot** e altri framework; **Docker** per containerizzazione e deployment. Spring Boot e Spring MVC sono presentati a lezione, con il pattern MVC → [[spring-mvc]].
- La docente presenta il progetto e assegna i sottosistemi ai team; scadenze rigide per assegnazione e sviluppo iterativo; **sprint di 2 settimane**; **iteration review** a fine sprint; a ogni team un **tutor** che fa da **Scrum Master**.

## Calendario

> 📄 Fonte: [[00_IntroduzioneAlCorso_SAD.pdf#page=27]], [[00_IntroduzioneAlCorso_SAD.pdf#page=30]]

| Evento | Data |
|---|---|
| Inizio corso | T0 = 15 settembre (le lezioni risultano dal 14 settembre, [[00_IntroduzioneAlCorso_SAD.pdf#page=30]]) |
| Assegnazione progetto | TA (entro metà ottobre) |
| Prima iteration review | TA + 2 settimane |
| Seconda iteration review | TA + 4 settimane |
| Terza iteration review | TA + 6 settimane |
| Review finale / esami | fine corso (lezioni fino al 18 dicembre 2026) |

## Valutazione

> 📄 Fonte: [[00_IntroduzioneAlCorso_SAD.pdf#page=28]], [[00_IntroduzioneAlCorso_SAD.pdf#page=29]]

- Progetto su **repository GitHub**, consegnato alla docente con una **pull request una settimana prima** dell'esame; la docente invia commenti o issue in tempo per risolverli.
- All'esame i team **presentano e discutono** il lavoro.

| Parte | Peso | Criteri |
|---|---|---|
| **Progetto** | 50 % (max 15 punti) | qualità e coerenza dell'architettura comune; qualità del sottosistema del team; documentazione, test e rispetto dei **contratti d'integrazione**; contributo al sistema integrato |
| **Orale** | 50 % (max 15 punti) | conoscenza degli argomenti; comprensione dell'architettura complessiva; capacità di **spiegare e giustificare le scelte di progetto**; consapevolezza del proprio contributo individuale |

> 🎯 Esame: per l'orale, ogni decisione del team va collegata ai concetti del corso — per questo le decisioni si annotano in questa cartella.

## Esperimenti di disponibilità per gruppo (da confermare)

> 📄 Fonte: [[02-Availability.pdf#page=23]]

La Lez. 2 chiude con una tabella di **otto gruppi**, ognuno con un problema di disponibilità dell'Exam Booking System, le tattiche o i pattern da usare, le tecnologie utilizzabili (Spring Boot, Resilience4j, PostgreSQL, RabbitMQ, Docker, Kubernetes, Prometheus…) e un **esperimento richiesto**. Tabella completa in [[tattiche-availability]] § Dalle tattiche alle tecnologie.

> ❓ Salto non ricostruito: la slide non dice se i «gruppi» sono i team del progetto e se gli esperimenti sono attività da consegnare. Da chiarire con la docente; se confermato, qui si annota il gruppo del tuo team.

## Decisioni architetturali

_nessuna ancora — il progetto non è stato assegnato. Usa `annota decisione [...]`._

_Aggiornato: 2026-09-26 — ingest 00_IntroduzioneAlCorso_SAD.pdf_
_Aggiornato: 2026-09-30 — tabella dei gruppi di 02-Availability.pdf p. 23_
_Aggiornato: 2026-10-06 — collegamento a Spring MVC_
