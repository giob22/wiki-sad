---
tipo: concetto
importanza_esame: media
prerequisiti: ["dssa", "modifiability"]
fonti_pdf: ["3-Architectural Patterns-complete.pdf#page=18", "3-Architectural Patterns-complete.pdf#page=19", "3-Architectural Patterns-complete.pdf#page=20"]
termine_inglese: "Software Product Line (SPL)"
---

# Linee di prodotto software

## Definizione

> 📄 Fonte: [[3-Architectural Patterns-complete.pdf#page=18]]

> 🔑 Definizione chiave: una **linea di prodotto software** (*Software Product Line*, SPL) è una **famiglia di prodotti** a forte componente software, correlati tra loro, che:
> - rispondono alle esigenze di uno **specifico segmento di mercato o missione**;
> - **condividono un insieme gestito di funzionalità comuni**;
> - **differiscono per variazioni pianificate esplicitamente**;
> - sono sviluppati a partire da un **insieme comune di asset riusabili** (*core assets*).

**Idea di fondo:** **sviluppare per il riuso**, poi **derivare i prodotti tramite configurazione**.

![[lez04-ap-p18-linee-di-prodotto.png]]
*Figura di [[3-Architectural Patterns-complete.pdf#page=18]] (a destra): tre cerchi «Common», ciascuno con due cerchietti A e B. Legenda: **Common** = funzionalità comuni a tutti i prodotti; **A** = funzionalità specifiche del prodotto A, quindi *Product A = Common + A*; **B** = funzionalità specifiche del prodotto B, *Product B = Common + B*.*

## Comunanza e variabilità

> 📄 Fonte: [[3-Architectural Patterns-complete.pdf#page=19]]

Una linea di prodotto **riusa sistematicamente ciò che è comune** e **gestisce esplicitamente ciò che è variabile**.

| Comunanza: asset di base condivisi | Variabilità: differenze pianificate |
|---|---|
| architettura della linea di prodotto | funzionalità opzionali o alternative |
| componenti e servizi riusabili | implementazioni alternative dei componenti |
| requisiti comuni | requisiti specifici del prodotto |
| test e ambienti di test condivisi | test specifici del prodotto |
| strumenti comuni di build e deployment | opzioni di configurazione e di deployment |

🧩 Ogni riga accoppia un asset comune con il suo «punto di variazione»: anche i test e la build hanno una parte condivisa e una per prodotto.

## Esempi espansi — linee di prodotto in domini diversi

> 📄 Fonte: [[3-Architectural Patterns-complete.pdf#page=20]]

![[lez04-ap-p20-esempi-linee-di-prodotto.png]]
*Figura di [[3-Architectural Patterns-complete.pdf#page=20]]: tabella dominio / linea di prodotto / elementi comuni / variabilità pianificata.*

| Dominio | Linea di prodotto | Elementi comuni | Variabilità pianificata |
|---|---|---|---|
| Automotive | sistemi di infotainment | navigazione, interfaccia utente, connettività | display, comandi vocali, servizi online, lingue |
| Avionica | software per una famiglia di aerei | controllo di volo, diagnostica, comunicazioni | sensori, configurazioni dei motori, varianti di aereo |
| Smart TV | famiglia di modelli di televisori | sistema operativo, streaming, aggiornamenti | schermo, tuner, sistema audio, applicazioni, mercato di destinazione |
| Smartphone | famiglia di dispositivi dello stesso produttore | sistema operativo, sicurezza, servizi cloud | fotocamere, display, sensori, memoria |
| Stampanti | famiglia di stampanti multifunzione | gestione della stampa, driver, diagnostica | scanner, stampa a colori, fronte-retro, velocità |
| Dispositivi medici | famiglia di monitor per pazienti | acquisizione dati, allarmi, visualizzazione | parametri vitali, sensori, interfacce, contesti clinici |
| Industrial IoT | famiglia di sistemi di monitoraggio | raccolta dati, comunicazione, gestione dei dispositivi | sensori, protocolli, frequenza di campionamento, analytics |
| E-commerce | piattaforma per negozi online diversi | catalogo, carrello, ordini, autenticazione | pagamenti, valute, promozioni, branding, spedizioni |
| Home banking | soluzioni bancarie configurabili | conti, transazioni, autenticazione, auditing | prodotti finanziari, normative nazionali, regole di autorizzazione |
| ERP | suite per organizzazioni diverse | utenti, contabilità, reportistica, dati anagrafici (*master data*) | ❓ cella tagliata nella slide |

> ❓ Salto non ricostruito: l'ultima riga della tabella di [[3-Architectural Patterns-complete.pdf#page=20]] è tagliata dal bordo della slide («master da…») e la colonna della variabilità per l'ERP è vuota.

## Perché importa

Riprende tre fili già visti: la motivazione §3.8 dell'architettura come **modello trasferibile e riusabile**, con la definizione di linea di prodotto ([[importanza-architettura-software]], [[01-IntroductionOnSoftwareArchitecture-2 parte.pdf#page=40]]); la **variabilità** come variante della modificabilità, con l'esempio della linea di prodotto Booking ([[modifiability]], [[03-Modifiability.pdf#page=12]]); le tattiche di **defer binding**, che sono il meccanismo con cui si «derivano i prodotti tramite configurazione» ([[tattiche-modifiability]]).

> 💡 Connessione: «Product A = Common + A» è la traduzione dell'esempio di [[03-Modifiability.pdf#page=12]]: il nucleo comune di prenotazione è *Common*, le regole di ammissibilità e le notifiche scelte da ogni università sono *A*, *B*… Il pattern [[plug-in]] (nucleo + estensioni con interfacce fisse) è un modo di realizzarlo.

> 🎯 Esame: definizione con i quattro punti; comunanza vs variabilità; un esempio di dominio.

## Connessioni

- [[dssa]]: entrambe riusano architetture, ma la DSSA vale per un dominio, la linea di prodotto per una famiglia di prodotti di un'organizzazione.
- [[progettazione-basata-sul-riuso]]: la linea di prodotto è riuso pianificato.
- [[modifiability]], [[tattiche-modifiability]]: variabilità e binding.

## Fonti

- [[approcci-riuso-progettazione-architettura]] — [[3-Architectural Patterns-complete.pdf#page=18]]–[[3-Architectural Patterns-complete.pdf#page=20]]

_Aggiornato: 2026-10-01 — ingest 3-Architectural Patterns-complete.pdf_
