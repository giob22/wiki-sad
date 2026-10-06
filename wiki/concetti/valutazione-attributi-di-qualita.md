---
tipo: concetto
importanza_esame: alta
prerequisiti: ["scenari-di-qualita", "strutture-di-modulo", "strutture-componenti-e-connettori"]
fonti_pdf: ["01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=15", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=17", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=18", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=19", "01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=34"]
termine_inglese: "architecture evaluation"
---

# Valutazione degli attributi di qualità

## Definizione

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture.pdf#page=7]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=34]] (slide 85)

Valutare un'architettura significa verificare se le decisioni prese permettono di ottenere gli attributi di qualità richiesti, cioè di soddisfare le **misure della risposta** dei [[scenari-di-qualita]]. Serve perché **non tutte le architetture sono buone** ([[01-IntroductionOnSoftwareArchitecture.pdf#page=7]]) e perché l'architettura va valutata per la sua capacità di fornire le qualità importanti ([[01-IntroductionOnSoftwareArchitecture.pdf#page=48]]).

> 🔑 Definizione chiave: è possibile fare **previsioni di qualità** su un sistema basandosi **solo sulla valutazione della sua architettura** ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=34]]).

Se sappiamo che certi tipi di decisioni architetturali portano a certi attributi di qualità, possiamo prendere quelle decisioni e aspettarci a ragione di ottenere quelle qualità. Esaminando un'architettura possiamo verificare se quelle decisioni sono state prese e **prevedere con fiducia** che l'architettura avrà le qualità associate ([[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=34]] → [[importanza-architettura-software]] §3.2).

La lezione mostra due casi: **prestazioni** e **modificabilità**, ciascuno valutato sulla vista adatta.

## Valutare le prestazioni

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=15]] (slide 66)

**Cosa si valuta**, per ogni elemento, durante il progetto architetturale:
tempo di elaborazione · numero di richieste gestibili · numero e costo delle comunicazioni · accessi al database · contesa sulle risorse · lunghezza delle code · possibilità di elaborazione parallela.

**Con quali approcci:**
modelli di prestazioni · **modelli a code** (*queuing models*) · simulazioni · prototipi architetturali · benchmark dei componenti critici · analisi dei colli di bottiglia.

**Su quale vista:** le prestazioni si valutano **principalmente sulle viste componenti e connettori** ([[strutture-componenti-e-connettori]]), completate dalle viste di **deployment** e di **concorrenza** quando l'allocazione delle risorse e l'esecuzione parallela influiscono sul risultato ([[strutture-di-allocazione]]).

**Esempio della slide:** la replicazione dell'application server può essere **insufficiente** se il database riesce a completare solo **30 transazioni al secondo**.

### Derivazione — perché 30 transazioni/s non bastano

**Fonte:** [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=15]] (limite del DB) e [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=14]] (carico dello scenario concreto). La slide non fa il confronto numerico.

> 🧩 Elaborazione mia — ipotesi: le 5.000 richieste sono distribuite uniformemente nel minuto e ogni prenotazione richiede **almeno una** transazione sul database.

$$
\begin{aligned}
\lambda &= \frac{5000\ \text{richieste}}{60\ \text{s}} && \text{tasso medio di arrivo, scenario di p. 14} \\
        &\approx 83.3\ \text{richieste/s} && \\
\mu_{DB} &= 30\ \text{transazioni/s} && \text{capacità del DB, p. 15} \\
\rho &= \frac{\lambda}{\mu_{DB}} = \frac{83.3}{30} \approx 2.8 && \text{utilizzo richiesto al DB} > 1
\end{aligned}
$$

**Risultato:** il database dovrebbe lavorare a circa il 280 % della sua capacità: la coda davanti al DB cresce per tutto il minuto di picco.

**Quanto cresce la coda:** in 60 s arrivano 5.000 richieste e il DB ne completa $30 \times 60 = 1800$; alla fine del minuto ne restano in attesa circa $5000 - 1800 = 3200$. Smaltirle richiede $3200 / 30 \approx 107\ \text{s}$ ulteriori, ben oltre i 5 s della misura della risposta.

**Sanity check:** il risultato non dipende dal numero di application server: aggiungere server aumenta la capacità del livello applicativo, non quella del DB. È esattamente l'affermazione della slide e la conclusione di [[01-IntroductionOnSoftwareArchitecture.pdf#page=41]] («il sistema è limitato dal componente meno scalabile»).

**Ipotesi:** arrivi uniformi (con arrivi a raffica va peggio); una transazione per prenotazione (con più transazioni va peggio); nessuna cache o scrittura asincrona che riduca il carico sul DB — proprio le tattiche che la lezione introduce subito dopo ([[tattiche-architetturali]]).

## Valutare la modificabilità

### A livello architetturale — analisi d'impatto

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=17]] (slide 68), [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=18]]

Sulle **viste dei moduli** si applica un'**analisi d'impatto delle modifiche** (*change impact analysis*):
1. si identifica lo **stimolo** di modifica;
2. si identifica il **modulo responsabile**;
3. si tracciano le **dipendenze** verso altri elementi;
4. si determinano gli **artefatti interessati**;
5. si **stima lo sforzo** richiesto;
6. si valutano gli **effetti su test e deployment**.

La slide [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=18]] ripropone la vista dei moduli dell'[[exam-booking-system]] (uguale a [[01-IntroductionOnSoftwareArchitecture.pdf#page=14]], vedi [[strutture-di-modulo]]) con la nota: *una modifica a una regola di ammissione dovrebbe interessare principalmente Eligibility Checking, non Booking*. L'analisi svolta passo per passo è in [[analisi-impatto-modifiche]].

### Empirica — esercizio di modifica

> 📄 Fonte: [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=19]] (slide 70)

Quando il sistema o un prototipo è disponibile, si conduce un **esercizio di modifica**:
- la modifica è assegnata a uno o più sviluppatori;
- si registra il **tempo** dall'inizio al completamento;
- si **contano gli artefatti modificati**;
- si eseguono i **test**;
- si verifica che **non siano state introdotte regressioni**.

🧩 Le grandezze misurate (tempo, artefatti toccati) sono esattamente la misura della risposta dello scenario di modificabilità di [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=16]] («entro due giorni lavorativi; modifiche limitate a…»): la valutazione empirica verifica lo scenario sul sistema reale, quella architetturale lo prevede sul modello.

## Perché importa

Chiude il ciclo scenario → decisione → verifica. All'orale del corso si chiede di **giustificare le scelte di progetto** ([[00_IntroduzioneAlCorso_SAD.pdf#page=29]]): la giustificazione è proprio una valutazione (questa scelta soddisfa questo scenario perché…).

> 🎯 Esame: cosa si valuta e con quali approcci per le prestazioni; su quali viste; i sei passi dell'analisi d'impatto; valutazione architetturale vs empirica della modificabilità.

## Connessioni

- [[scenari-di-qualita]]: definiscono cosa misurare.
- [[strutture-componenti-e-connettori]], [[strutture-di-allocazione]]: viste per le prestazioni.
- [[strutture-di-modulo]]: vista per la modificabilità.
- [[tattiche-architetturali]]: cosa cambiare quando la valutazione dà esito negativo.

## Fonti

- [[attributi-di-qualita-e-importanza-architettura]] — [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=15]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=17]]–[[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=19]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=34]]

_Aggiornato: 2026-09-26 — ingest lezione 1_
