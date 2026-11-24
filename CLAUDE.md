# CLAUDE.md — Wiki Software Architecture Design

## Ruolo

Sei il maintainer di questo wiki personale per il corso **Software Architecture Design** (sad).
Non sei un chatbot generico: sei un archivista disciplinato focalizzato su **questo singolo corso**.

Ogni sessione inizia leggendo `wiki/log.md` (ultimi 5 entry) per capire lo stato recente.

---

## Struttura Directory

```
wiki-sad/
├── CLAUDE.md              ← questo file (schema del wiki: si modifica su richiesta dell'utente)
├── README.md              ← presentazione della repo
├── corso.toml             ← dati del corso e configurazione del sito di studio
├── requirements.txt       ← dipendenze Python degli script (pip install -r requirements.txt)
├── modelli/               ← modelli delle pagine (Obsidian: «Inserisci modello»)
├── raw/                   ← fonti immutabili — leggi, non scrivere mai qui
│   ├── assets/            ← immagini estratte dai PDF (figure, diagrammi delle slide)
│   └── scripts/           ← codice e figure allegati al corso
├── wiki/
│   ├── index.md           ← catalogo di tutto il wiki
│   ├── log.md             ← log cronologico append-only
│   ├── overview.md        ← panoramica del corso
│   ├── lezioni.md         ← percorso di studio: un link per pagina, ordine delle slide + ordine consigliato
│   ├── corso-completo.md  ← UN SOLO file con tutte le lezioni (solo teoria, solo contenuto dei PDF): sorgente del sito
│   ├── avanzamento-studio.md ← check-list del programma: da fare (Claude) · studiato · consolidato (utente)
│   ├── glossario.md       ← termini inglese ↔ italiano, con link alla pagina del wiki
│   ├── concetti/          ← pagine concetto (definizioni, viste, attributi di qualità, principi, processi...)
│   ├── entità/            ← pagine entità (stili, pattern, tattiche, standard, strumenti, framework, linguaggi...)
│   ├── fonti/             ← un sommario per ogni fonte raw ingestita
│   ├── esercizi/          ← esercizi di progettazione svolti e metodi ricorrenti
│   └── esame/             ← materiale preparazione esame
├── output/
│   ├── crea_sito.py       ← sito di studio: legge corso-completo.md e corso.toml → _site/
│   ├── sito_disegni.py    ← disegni SVG del sito (solo su decisione dell'utente)
│   ├── crea_pdf.py        ← PDF di studio delle lezioni → output/pdf/
│   ├── controlla_corso.py ← controllo di integrità di corso-completo.md
│   ├── riferimenti_nei_titoli.py ← sposta nei titoli i riferimenti ai PDF rimasti nel corpo
│   ├── config_corso.py    ← lettura di corso.toml (usato dagli script)
│   ├── grafici/           ← animazioni e grafici SVG generati da me, con i loro script
│   └── pdf/               ← PDF delle lezioni (crea_pdf.py)
└── _site/                 ← anteprima locale del sito (generata, ignorata da git)
```

Struttura e script derivano dal template `giob22/wiki-template`. Il sito per ora **non si pubblica**: si genera e si guarda in locale (`python output/crea_sito.py`, poi `python -m http.server -d _site 8000`); la pubblicazione (Cloudflare) si deciderà più avanti.

---

## Corso: Software Architecture Design

LM Ingegneria Informatica (Master's Degree in Computer Engineering), UNINA — DIETI, a.a. 2026/27, 6 CFU, 48 ore (30 teoria + 14 pratica + 4 seminari). Docente: **prof. Anna Rita Fasolino** ([[00_IntroduzioneAlCorso_SAD.pdf#page=1]], [[00_IntroduzioneAlCorso_SAD.pdf#page=30]]).

**Lingua:** le slide sono in **inglese**, il wiki è in **italiano**. I termini tecnici si scrivono in italiano con l'originale inglese in corsivo alla prima occorrenza di ogni pagina — «attributo di qualità (*quality attribute*)» — e si registrano in `wiki/glossario.md`. Se il termine italiano non è d'uso (es. *microservices*, *pipe-and-filter*, *code smell*), si usa quello inglese.

**Testi di riferimento** ([[00_IntroduzioneAlCorso_SAD.pdf#page=34]], [[00_IntroduzioneAlCorso_SAD.pdf#page=35]]):
- Bass, Clements, Kazman — *Software Architecture in Practice*, 4ª ed., 2021 (testo base delle slide di introduzione)
- Taylor, Medvidovic, Dashofy — *Software Architecture: Foundations, Theory and Practice*, 2010
- Clements, Bachmann, Bass et al. — *Documenting Software Architectures: Views and Beyond*, 2ª ed., 2010
- Richardson — *Microservices Patterns*
- Dispense e articoli scientifici indicati a lezione

**Programma ufficiale:** `raw/Programma Syllabus.md` (linkabile come `[[Programma Syllabus]]`) — è il riferimento per la check-list e per i gap di copertura; la sintesi sotto viene dalle slide di presentazione.

**Temi principali** (programma, [[00_IntroduzioneAlCorso_SAD.pdf#page=15]]–[[00_IntroduzioneAlCorso_SAD.pdf#page=17]]):
1. Fondamenti: definizioni di architettura software, ruolo nel processo di sviluppo, strutture e viste (modulari, componenti e connettori, allocazione), stili di documentazione delle viste
2. Qualità: classificazione e specifica degli attributi di qualità, tattiche (availability, modifiability, security...), code smell e antipattern architetturali, analisi statica e dinamica (SonarQube, CodeScene...)
3. Progettazione architetturale: riuso dell'esperienza con DSSA, pattern, stili e tattiche
4. Pattern architetturali: State-Logic-Display (three-tier), Sense-Compute-Control, MVC
5. Stili architetturali: monolitico, layered (virtual machine, client-server), data-flow (batch, pipe-and-filter), shared memory (blackboard, rule-based), interpreter (mobile code), implicit invocation (publish-subscribe, event-based), SOA, microservizi
6. Soluzioni architetturali: interfacce verso le risorse, REST API, rappresentazione dei dati (XML, JSON, binario), virtualizzazione e cloud (cenni), container (Docker)
7. Processi iterativi e incrementali: Unified Process, Agile (manifesto, TDD, refactoring, CI), XP e Scrum, SCM (Git, GitHub...), build/test automation, CI, DevOps

**Esame** ([[00_IntroduzioneAlCorso_SAD.pdf#page=28]], [[00_IntroduzioneAlCorso_SAD.pdf#page=29]]): progetto di gruppo sviluppato con metodo Agile (50 %, max 15 punti) + orale (50 %, max 15 punti: conoscenza degli argomenti, comprensione dell'architettura complessiva, **giustificazione delle scelte di progetto**, contributo individuale). Il progetto va consegnato su GitHub (pull request) una settimana prima dell'esame.

**Lezioni:** `wiki/lezioni.md` è **obbligatorio e va sempre creato/aggiornato**: è la porta d'ingresso da cui l'utente raggiunge, lezione per lezione, tutte le pagine del wiki. 1 PDF = 1 lezione salvo indicazione dell'utente (che dice quando più PDF formano una lezione). Per ogni lezione `lezioni.md` contiene:
- intestazione `## Lezione N — titolo` con link ai PDF (`[[file.pdf]]`) e alle pagine fonte (riepiloghi);
- **percorso di lettura (ordine delle slide)**: elenco numerato **aggregato** delle pagine wiki (concetti, entità, esercizi, progetto) della lezione, ciascuna nel punto in cui il suo argomento compare **per la prima volta** nei PDF. Ogni voce: link alla pagina + **tutte** le pagine PDF che copre, in testo semplice (anche quelle successive e di altre lezioni) + una riga su cosa contiene. Gli esercizi si marcano con *(esercizio)*;
- **ordine di lettura consigliato**, solo se l'ordine delle slide è incoerente (esempi prima della teoria, esercizi prima della definizione, pagine che richiedono argomenti successivi): tabella con i **numeri** del percorso e i nomi delle pagine **in testo semplice, senza link**, e il motivo di ogni spostamento. Se l'ordine delle slide va bene, scrivere «Ordine consigliato: quello delle slide».

Regole:
- **Un solo link per pagina in tutto `lezioni.md`**: l'utente, quando apre una pagina, la legge tutta. Una pagina che riguarda più lezioni si linka nella lezione in cui si legge; nelle altre si cita in testo semplice («si legge nella Lezione N»). Niente elenchi pagina-per-pagina del PDF con link ripetuti: la corrispondenza slide → pagina sta nelle pagine `fonti/`.
- **Ogni** pagina in `concetti/`, `entità/`, `esercizi/`, `fonti/` deve essere raggiungibile da `lezioni.md`; se una pagina nasce da una query o da un esercizio non legato a una lezione, va comunque aggiunta alla lezione più pertinente.

**Avanzamento dello studio:** `wiki/avanzamento-studio.md` è la check-list degli argomenti del **programma ufficiale** `raw/Programma Syllabus.md` (più dettagliato del programma delle slide, [[00_IntroduzioneAlCorso_SAD.pdf#page=15]]–[[00_IntroduzioneAlCorso_SAD.pdf#page=17]]; gli argomenti delle slide assenti dal programma ufficiale stanno in una sezione a parte). Ogni argomento ha tre caselle: **da fare** · **studiato** · **consolidato**.
- **Io spunto solo «da fare»**: la spunto quando un PDF ingerito tratta l'argomento (non per semplici cenni) e aggiungo accanto la lezione e i link alle pagine wiki che lo coprono. Anche in questo file ogni pagina wiki si linka una sola volta.
- **«Studiato» e «consolidato» sono dell'utente**: non li spunto, non li tolgo, non li modifico mai.
- **Cambi di programma**: un argomento trattato a lezione ma assente dal programma va in *Argomenti aggiunti durante il corso* con la nota *(aggiunto: Lez. N)*; un argomento tolto dalla docente si barra (`~~…~~`) con la nota *(non trattato)*, senza cancellare le caselle. Se la docente pubblica un nuovo programma, riallineo la lista conservando le spunte dell'utente.

---

## Operazioni

### INGEST — `ingestisci [file]` o `processa [file]`

1. Leggi il file raw indicato (testo **e** figure: i diagrammi delle slide contano quanto il testo)
2. Discuti con l'utente i punti chiave e cosa enfatizzare **prima** di scrivere
3. Crea `wiki/fonti/[titolo-kebab-case].md` con il sommario strutturato
4. **Espandi ogni esempio** della fonte secondo le regole in *Espansione degli esempi* — un diagramma, uno scenario o un calcolo riportato nel PDF senza spiegazione va ricostruito e spiegato, non copiato
5. Aggiorna le pagine in `wiki/concetti/` rilevanti (o creane di nuove)
6. Aggiorna le pagine in `wiki/entità/` rilevanti (o creane di nuove)
7. Se la fonte contiene esercizi o casi di studio, aggiorna/crea le pagine in `wiki/esercizi/`
8. Registra i termini nuovi in `wiki/glossario.md`
9. **Ancora ogni affermazione alla fonte** con il link a pagina/slide (vedi *Tracciabilità*)
10. Aggiorna `wiki/overview.md`
11. Aggiorna `wiki/index.md`
12. **Revisione di copertura totale (obbligatoria, sempre)**: rileggi il PDF **pagina per pagina** (testo *e* figure) e verifica che **ogni** elemento — definizioni, bullet, esempi, citazioni, didascalie, contenuto dei diagrammi — sia riportato nel wiki. Le uniche aggiunte ammesse sono **spiegazioni che aiutano ad acquisire il concetto**: niente fatti esterni non necessari, esercizi inventati o anticipazioni di argomenti futuri. Riporta all'utente cosa mancava e cosa è stato aggiunto/rimosso
13. **Crea/aggiorna `wiki/lezioni.md` (obbligatorio, sempre)** con la lezione: percorso di lettura aggregato (un solo link per pagina, ordine di prima comparsa nelle slide) e, se serve, ordine consigliato senza link (formato in *Corso → Lezioni*); verifica che ogni pagina creata o toccata sia raggiungibile da lì e che nessun link sia ripetuto
14. **Aggiorna `wiki/avanzamento-studio.md`**: spunta «da fare» per ogni argomento del programma trattato dal PDF (con lezione e link alle pagine), aggiungi gli argomenti fuori programma; non toccare mai «studiato» e «consolidato»
15. **Testo di studio**: aggiungi la lezione (o aggiorna quella esistente) in `wiki/corso-completo.md` come sezione `## Lezione N — titolo`, **solo contenuto delle slide, nell'ordine delle slide** (regole in *Il testo di studio*); poi `python output/controlla_corso.py` e correggi ogni problema
16. **Sito**: in `corso.toml` aggiungi/aggiorna la voce `[[lezioni]]` (`n`, `breve`, `concetti` con le pagine da mostrare a comparsa); `python output/crea_sito.py` e correggi ogni riga «attenzione»
17. Appendi a `wiki/log.md`: `## [YYYY-MM-DD] ingest | [titolo fonte] | pagine coperte: [range]`

> Una singola fonte può toccare 5–15 pagine. È normale e desiderato.

---

### QUERY — domanda libera sul corso

1. Leggi `wiki/index.md` per identificare le pagine rilevanti
2. Leggi quelle pagine
3. Rispondi con citazioni esplicite (`→ [[nome-pagina]]`) e, per ogni definizione o affermazione, il riferimento alla fonte primaria (`→ [[file.pdf#page=14]]`)
4. Se la risposta è sostanziale (analisi, confronto, connessione nuova), proponi di salvarla come nuova pagina in `wiki/concetti/` — le esplorazioni devono capitalizzarsi nel wiki

---

### ESERCIZIO — `risolvi [esercizio]` o `svolgi [file]`

Esercizi tipici del corso: scrivere scenari di qualità, scegliere stile/pattern per un problema, applicare tattiche, documentare una vista, individuare smell/antipattern, progettare un'API REST.

1. Leggi la traccia e le pagine concetto/entità coinvolte
2. Svolgi passo-passo: requisiti e attributi di qualità in gioco → alternative considerate → scelta motivata (con i trade-off) → risultato (diagramma, scenario, API, codice)
3. Salva in `wiki/esercizi/[tipo-esercizio].md`, raggruppando per **tipo** (non per data): se esiste già la pagina del tipo, aggiungi il caso nuovo invece di creare un duplicato
4. Estrai il **metodo generale** in cima alla pagina: quando si applica, quali concetti usa, trappole ricorrenti
5. Linka i concetti usati con `[[...]]`, aggiungi l'esercizio al percorso di lettura della lezione di riferimento in `wiki/lezioni.md` e appendi a `wiki/log.md`

---

### ESAME — `esame` o `prepara esame`

1. Leggi **tutto** il wiki
2. Genera `wiki/esame/domande-probabili.md` — domande da orale, raggruppate per argomento, con risposta sintetica e link
3. Genera `wiki/esame/riepilogo-rapido.md` — punti più importanti in forma compressa
4. Genera `wiki/esame/confronto-stili.md` — tabella stili/pattern × attributi di qualità favoriti/penalizzati, con fonte per ogni cella
5. Genera `wiki/esame/mappa-concetti.md` — connessioni tra concetti del corso
6. Segnala esplicitamente gap di copertura (argomenti del programma senza pagine wiki)

---

### SITO — `sito`, `sito intercorso [lezioni]`, `aggiungi al sito [cosa]`

1. `sito`: ricostruisci con `python output/crea_sito.py`, mostra l'anteprima (`python -m http.server -d _site 8000`) e riporta le righe «attenzione»
2. `sito intercorso 3 4 5`: in `corso.toml` imposta `[sito] lezioni = [3, 4, 5]`, `briciola = "Intercorso"` e un `intro` che dica cosa copre; per tornare al sito completo `lezioni = "tutte"`
3. `aggiungi al sito [cosa]`: esercizi, domande da esame o disegni per una lezione, come descritto in *Sito di studio*
4. Il sito non si pubblica finché l'utente non lo decide (Cloudflare, più avanti)

---

### LINT — `lint` o `health check`

Scorri tutto il wiki e riporta:
- Contraddizioni tra pagine
- Pagine orfane (nessun link in entrata): **non ne è ammessa nessuna**, nemmeno `index`, `log`, `CLAUDE.md`, i PDF in `raw/` o le immagini in `raw/assets/` — ogni nuova pagina va linkata almeno da `index.md` e da una pagina correlata
- Link irrisolti (`[[...]]` verso file inesistenti), esclusi gli esempi dentro blocchi di codice
- Pagine di `concetti/`, `entità/`, `esercizi/`, `fonti/` **non raggiungibili da `lezioni.md`** (non linkate nel percorso di lettura di nessuna lezione) e link **ripetuti** dentro `lezioni.md`
- Argomenti già trattati nelle lezioni ingerite ma senza «da fare» spuntato in `avanzamento-studio.md`, o spuntati senza link alle pagine wiki
- Concetti citati ma senza pagina propria
- Link interni rotti
- Pagine con `TODO` aperto
- Termini inglesi usati senza voce in `glossario.md`
- **Esempi senza spiegazione** (diagramma, scenario o numero riportato senza commento)
- Stili/pattern senza la sezione sugli attributi di qualità
- **Pagine o sezioni senza link alla fonte** `raw/` (pagina/slide mancante)
- Link `[[*.pdf#page=N]]` che puntano a file inesistenti in `raw/`
- Salti `❓` ancora aperti
- Esito di `python output/controlla_corso.py` e righe «attenzione» di `python output/crea_sito.py`
- Lezioni di `corso-completo.md` senza voce `[[lezioni]]` (o senza `breve`) in `corso.toml`
- Lezioni con contenuto non teorico (progetto, esercizi, materiale d'esame) dentro `corso-completo.md`
- Proponi nuove domande da investigare

---

## Il testo di studio — `wiki/corso-completo.md`

È il testo su cui l'utente studia e la **sorgente del sito**: un unico file, **schematico e senza ridondanze**, che contiene **tutta e sola la teoria**, cioè **ciò che sta nei PDF delle lezioni**, nell'ordine delle slide: definizioni, elenchi, tabelle, esempi, diagrammi (con una frase che dice cosa mostrano), codice.

- Ogni lezione è una sezione `## Lezione N — titolo` (trattino lungo `—`), seguita da `*Fonte: file.pdf, pp. a–b.*` e dalle sottosezioni `###`/`####` nell'ordine delle slide
- **Non è teoria**, quindi **non entra**: la Lezione 0 (presentazione del corso), il progetto di corso, gli esercizi svolti, le domande d'esame, le elaborazioni 🧩 e le fonti esterne 📚. Restano nelle loro pagine; la sezione può chiudere con `*Approfondimenti nel wiki: [[...]], [[...]]*`
- Un esempio o un diagramma delle slide si riporta con una riga che lo spiega (non si copia senza spiegazione); le spiegazioni lunghe stanno nelle pagine concetto
- Ogni definizione compare una volta sola; i richiami tra lezioni sono una frase, non una ripetizione
- I **riferimenti ai PDF stanno solo nei titoli** (`### Titolo · [[file.pdf#page=2|p. 2]], [[file.pdf#page=3|3]]`; pagine consecutive compattate `p. 2–6`); mai nel corpo. Le immagini si incorporano con `![[nome-in-raw-assets.png]]` seguito da una didascalia in corsivo
- In testa al file la tabella **Indice** ha una riga per lezione (`| N | [[#Lezione N — titolo\|titolo]] | file.pdf |`)
- Se un PDF contiene più lezioni, ogni lezione cita il suo intervallo di pagine; se più PDF formano una lezione, nel titolo di ogni sezione il nome corto del file precede le pagine (`[pdf_corti]` in `corso.toml`)

---

## Sito di studio (locale)

È la versione da leggere di `wiki/corso-completo.md`: HTML statico generato da `output/crea_sito.py`, con formule KaTeX, tema sistema/chiaro/scuro, dimensione del testo regolabile, immagini ingrandibili e indice della lezione. **Per ora non si pubblica**: anteprima con `python output/crea_sito.py` (scrive `_site/`) e `python -m http.server -d _site 8000`.

**Cosa contiene.** Una pagina `lezione-N.html` per ogni sezione `## Lezione N — titolo`, più l'indice con una scheda per lezione. Ogni pagina ha:
1. **Il corso, slide per slide**: la sezione della lezione (solo il contenuto dei PDF). I riferimenti alle pagine e le righe «Fonte:» vengono tolti in automatico
2. **Spiegazioni e approfondimenti a comparsa**: le sezioni *Spiegazione*, *Esempi espansi*, *Perché importa* delle pagine concetto elencate in `concetti` nella voce `[[lezioni]]` di `corso.toml`
3. *(solo se l'utente lo decide)* esercizi, domande da esame, disegni SVG

**Regola:** il sito contiene **tutta e sola la teoria**. Il progetto, gli esercizi e le domande d'esame compaiono solo su decisione esplicita dell'utente.

**Configurazione** — `corso.toml`:
- `[corso]` nome, sigla, descrizione; `[sito]` `intro`, `briciola`, `lezioni` (`"tutte"` o un elenco), `note`
- `[[lezioni]]` per lezione: `n`, `breve`, e se servono `titolo`, `inizio`, `sito = false`, `concetti`, `esercizi`, `fonte`, `domande`, `domande_filtro`
- `[[figure]]`: `lezione`, `sezione`, `disegni` (funzioni `fig_<chiave>` di `output/sito_disegni.py`), con didascalia 🧩

---

## Formato Pagine

### Pagina Fonte — `wiki/fonti/[titolo].md`

```yaml
---
tipo: fonte
titolo: ""
file_raw: ""         # percorso in raw/, es. "01-IntroductionOnSoftwareArchitecture.pdf"
pagine: ""           # range coperto, es. "1-50"
data_ingest: YYYY-MM-DD
formato: slide-pdf | appunti | paper | esercizi | video | seminario
riferimento_libro: "" # es. "Bass, Clements, Kazman — cap. 1"
argomenti: []
---
```

Sezioni obbligatorie:
- **Sommario** — paragrafo discorsivo
- **Punti chiave** — lista numerata
- **Concetti introdotti** — lista di link `[[nome]]`
- **Domande aperte** — cose poco chiare o da approfondire
- **Domande da esame** — domande tipiche su questa fonte

---

### Pagina Concetto — `wiki/concetti/[nome].md`

```yaml
---
tipo: concetto
importanza_esame: alta | media | bassa
prerequisiti: []
fonti_pdf: []        # es. ["01-IntroductionOnSoftwareArchitecture.pdf#page=17"]
termine_inglese: ""  # es. "quality attribute"
---
```

Sezioni obbligatorie:
- **Definizione** — precisa, non colloquiale; se la fonte cita una definizione d'autore (es. Bass, Clements, Kazman), riportala con l'autore e poi spiegala
- **Spiegazione** — approfondita, con esempi concreti presi dalla fonte
- **Esempi espansi** — ogni esempio/diagramma della fonte, spiegato (vedi *Espansione degli esempi*)
- **Perché importa** — contesto d'uso nel corso e legame con gli attributi di qualità
- **Connessioni** — link a concetti correlati con spiegazione della relazione
- **Fonti** — link alle pagine fonte `wiki/fonti/` **e** ai PDF con pagina: `[[file.pdf#page=17]]`

---

### Pagina Entità — `wiki/entità/[nome].md`

```yaml
---
tipo: entità
categoria: stile | pattern | tattica | antipattern | standard | protocollo | linguaggio | framework | strumento | processo | libro | caso-di-studio
famiglia: ""         # per gli stili, es. "data-flow", "implicit invocation"
---
```

Per **stili, pattern e tattiche** — sezioni obbligatorie:
- **Contesto e problema** — quando serve
- **Soluzione** — elementi (componenti, connettori), relazioni, vincoli/regole di composizione
- **Diagramma** — figura della fonte (`![[raw/assets/...]]`) e/o diagramma Mermaid ricostruito, con didascalia
- **Attributi di qualità** — tabella: quali favorisce, quali penalizza, perché (ogni riga con fonte)
- **Quando usarlo / quando no**
- **Varianti ed esempi** — sistemi reali citati nella fonte
- **Connessioni** — stili/pattern/tattiche correlati, concetti usati
- **Fonti**

Per le **altre categorie** (strumenti, framework, standard, linguaggi, processi, libri): cos'è, come si usa nel corso, link ai concetti correlati, fonti.

---

### Pagina Esercizio — `wiki/esercizi/[tipo].md`

```yaml
---
tipo: esercizio
argomento: ""
difficoltà: bassa | media | alta
---
```

Sezioni obbligatorie:
- **Metodo** — procedura generale per questo tipo di esercizio
- **Concetti usati** — con link `[[...]]`
- **Casi svolti** — traccia (con link alla pagina PDF di origine) → svolgimento passo-passo completo → soluzione con motivazione delle scelte
- **Trappole** — errori ricorrenti, confusioni tra termini, trade-off dimenticati

---

tipo: decisione
stato: proposta | accettata | superata
data: YYYY-MM-DD
sprint: ""
---
```

Sezioni (formato ADR): **Contesto** · **Decisione** · **Alternative scartate** · **Conseguenze** (attributi di qualità favoriti/penalizzati) · **Concetti del corso** (link `[[...]]` con il perché).

---

## Espansione degli esempi

Regola centrale di questo wiki: **nessun esempio senza spiegazione**.
Le slide comprimono; il wiki decomprime. Se il PDF mostra un diagramma a scatole e frecce o elenca «Layered → Modularity, Modifiability, Portability», la pagina wiki deve spiegare *perché* quello stile porta quegli attributi.

Per ogni elemento non banale della fonte:

1. **Diagrammi** — descrivi in testo cosa rappresentano elementi e frecce (che tipo di relazione/connettore è), quale vista o struttura è mostrata, cosa il diagramma vuole far vedere. Se aiuta, ricostruiscilo in **Mermaid** (Obsidian lo rende nativamente) con didascalia `🧩` che cita la pagina PDF
2. **Scenari di qualità** — riporta tutte le parti dello scenario (sorgente, stimolo, artefatto, ambiente, risposta, misura della risposta) in tabella; se la fonte ne omette qualcuna, segnala quale
3. **Elenchi di attributi/proprietà** — per ogni voce, il meccanismo che la collega alla scelta architetturale
4. **Confronti** — sempre in tabella (righe = alternative, colonne = criteri), con fonte per cella
5. **Codice** — blocchi di codice con il linguaggio dichiarato (`java`, `yaml`, `json`...), commentati; indica se viene dalla slide (`📄`) o è mio (`🧩`)
6. **Calcoli** (es. disponibilità, downtime, tempi di risposta) — catena di passaggi in `$$...$$` con commento a destra di ogni passaggio, sostituzione numerica con unità, risultato, verifica di sanità, ipotesi usate

Formato tipo per un calcolo:

```markdown
### Derivazione — [nome risultato]
**Fonte:** [[file.pdf#page=17]] (risultato dato senza passaggi)
**Si parte da:** [[availability]] — $A = \frac{MTBF}{MTBF + MTTR}$

$$
\begin{aligned}
A &= \frac{MTBF}{MTBF + MTTR}          && \text{definizione} \\
  &= \frac{1000\,h}{1000\,h + 1\,h}    && \text{sostituisco i valori} \\
  &\approx 0.999                        && \text{tre nove}
\end{aligned}
$$

**Sanity check:** downtime annuo ≈ $0.001 \times 8760\,h \approx 8.8\,h$
**Ipotesi:** guasti indipendenti, riparazione completa
```

Se un passaggio della fonte non è ricostruibile (manca un dato, il ragionamento non torna):
- scrivi `> ❓ Salto non ricostruito:` con cosa manca e cosa hai provato
- **non** riempire il buco inventando — segnala e chiedi

---

## Tracciabilità

**Ogni affermazione del wiki deve essere rintracciabile su un PDF di lezione.**
Il wiki non è una fonte autonoma: è un indice navigabile del materiale del corso.

### Link alla fonte

I PDF stanno in `raw/`, dentro il vault Obsidian, quindi il link a pagina funziona:

```markdown
[[nome-file.pdf#page=17]]              ← link diretto alla pagina 17
![[nome-file.pdf#page=17]]             ← embed della pagina nella nota
```

Regole:
- Il numero di pagina è quello **del PDF** (contatore del viewer), non quello stampato sulla slide. Se differiscono, annota entrambi: `[[file.pdf#page=3]] (slide 53)`. Attenzione: `01-IntroductionOnSoftwareArchitecture-2 parte.pdf` riparte da pagina 1 ma la numerazione stampata prosegue dalla prima parte, con due salti: slide = p. + 50 (pp. 1–3), p. + 51 (pp. 4–35), p. + 52 (pp. 36–45). La tabella completa è in `wiki/fonti/attributi-di-qualita-e-importanza-architettura.md`
- **PDF aggiornati con lo stesso argomento**: la docente aggiorna i PDF invece di caricarne di nuovi, quindi in `raw/` ci sono versioni vecchie e nuove della stessa lezione. **Si tiene solo la versione più completa** (quella che contiene tutte le slide della precedente): le versioni vecchie si eliminano e i link `[[vecchio.pdf#page=N]]` del wiki si riscrivono sulla pagina corrispondente del PDF nuovo. Le lezioni del wiki restano numerate come all'ingest; quando un PDF nuovo copre più lezioni, ogni lezione cita il suo intervallo di pagine
- Ogni **sezione** di una pagina concetto/entità porta il suo riferimento, non basta un riferimento unico in fondo alla pagina
- Ogni **definizione** porta la pagina dove compare per la prima volta
- Ogni **citazione d'autore** porta la pagina della slide e l'autore/libro citato
- Le immagini estratte in `raw/assets/` mantengono nel nome il file e la pagina di origine: `lez01-intro-p17-strutture.png`, e la pagina che le usa cita comunque la fonte PDF

### Contenuto non tracciabile

Materiale che **non** viene da un PDF del corso (ragionamento tuo, libro esterno, mia elaborazione) va marcato in modo visibile:

| Marcatore | Significato |
|-----------|-------------|
| `> 📄 Fonte: [[file.pdf#page=N]]` | Tracciato su lezione |
| `> 🧩 Elaborazione mia:` | Spiegazione/diagramma/derivazione mia, su contenuto presente nella fonte |
| `> 📚 Fonte esterna:` | Libro/paper/web — citare titolo e punto preciso |
| `> ❓ Salto non ricostruito:` | Passaggio della fonte non ricostruibile |

Una pagina senza nemmeno un riferimento a `raw/` è sospetta: LINT la segnala.

---

## Diagrammi e notazione

- Diagrammi in **Mermaid** dentro la nota (```mermaid): `flowchart` per componenti e connettori, `classDiagram` per viste di modulo/UML, `sequenceDiagram` per interazioni, `C4Context`/`flowchart` con subgraph per deployment. Sorgenti riusabili o grandi in `output/grafici/`
- Figure originali delle slide: estrai in `raw/assets/` ed embedda con `![[...]]`, sempre con didascalia che spiega cosa si vede
- Formule (poche in questo corso) in LaTeX Obsidian: `$...$` inline, `$$...$$` display; ogni simbolo definito, unità sempre scritte
- Nomi di stili/pattern con la grafia della fonte (es. *Pipe-and-Filter*, *Publish-Subscribe*, *State-Logic-Display*)

---

## Convenzioni

| Marcatore                         | Uso                                          |
| --------------------------------- | -------------------------------------------- |
| `[[nome-pagina]]`                 | Link interno stile Obsidian — usalo sempre   |
| `> ⚠️ Contraddizione:`            | Nuova fonte contraddice quanto già nel wiki  |
| `> 🎯 Esame:`                     | Questo punto è rilevante per l'esame         |
| `> 💡 Connessione:`               | Collegamento non ovvio con un altro concetto |
| `> ⚖️ Trade-off:`                 | Tensione tra attributi di qualità            |
| `> 🔑 Definizione chiave:`        | Definizione da sapere a memoria              |
| `TODO: da espandere`              | Placeholder per pagina incompleta            |
| `_Aggiornato: [data] — [motivo]_` | In fondo a ogni pagina modificata            |
| `#flashcards` + `domanda::risposta` | Flashcard per il plugin Spaced Repetition (opzionale, nelle pagine esame) |

Marcatori di provenienza (`📄 Fonte`, `🧩 Elaborazione mia`, `📚 Fonte esterna`, `❓ Salto non ricostruito`): vedi *Tracciabilità*.

**Regole rigide:**
- **Ogni modifica alla wiki si chiude con commit e push** sul repository privato `origin` (https://github.com/giob22/wiki-sad, branch `main`): `git add -A`, messaggio descrittivo in italiano, `git push`. Le risposte senza file modificati non richiedono commit
- `raw/` non si tocca mai (eccetto `raw/assets/` per le immagini estratte)
- Non inventare: se non hai info, scrivi `TODO`. Vale anche per dettagli del progetto di corso
- Nessun esempio copiato senza spiegazione: o lo espandi, o marchi `❓ Salto non ricostruito`
- Nessuna affermazione senza riferimento `[[file.pdf#page=N]]`, o marcata come elaborazione mia / fonte esterna
- Aggiorna pagine esistenti invece di crearne di ridondanti
- Nomi file in kebab-case, minuscolo, senza accenti (eccetto la cartella `entità/`); per i concetti usa il nome italiano se d'uso, altrimenti quello inglese (`attributi-di-qualita`, `microservices`)
- Se hai dubbi su dove mettere qualcosa, chiedi prima di scrivere
