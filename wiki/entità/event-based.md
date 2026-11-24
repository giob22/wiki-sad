---
tipo: entità
categoria: stile
famiglia: "implicit invocation"
---

# Event-based

## Contesto e problema

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=108]]

La cooperazione tra componenti si organizza attorno a **eventi** — occorrenze di interesse come il click di un pulsante, il tick di un clock, una prenotazione confermata — senza che i componenti si chiamino direttamente.

## Soluzione

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=108]], [[05_Architectural_Styles_Complete.pdf#page=109]]

- **Producer** annunciano eventi; **consumer** reagiscono secondo le proprie responsabilità; un componente può avere entrambi i ruoli.
- **Connettori:** meccanismi di dispatching locali o canali di rete, spesso con un **bus** o **broker**. Locale: sincrono o asincrono; distribuito: di norma asincrono.
- **Rapporto con gli altri concetti (p. 109):** [[implicit-invocation]] è il *principio* di interazione; l'architettura event-based è l'*organizzazione* dei componenti attorno agli eventi; [[publish-subscribe]] è un *meccanismo* comune di consegna. Trasmettere ogni evento a tutti è un'opzione; filtraggio e instradamento consegnano solo i rilevanti.

## Diagramma

![[lez08-stili-p112-event-based-lunar-lander.png]]
*Lunar Lander event-based ([[05_Architectural_Styles_Complete.pdf#page=112]]): SpaceCraft, Clock, Game Logic e GUI sono collegati a un bus Event. Spacecraft riceve i tick del Clock (t), ricalcola lo stato ed emette un evento (a, br, f, v); Game Logic ne deduce se la partita è finita; la GUI pubblica l'input utente (br), riceve gli stati e aggiorna il display.*

## Esempi espansi

**Gestione locale degli eventi in Java** ([[05_Architectural_Styles_Complete.pdf#page=113]]–[[05_Architectural_Styles_Complete.pdf#page=117]]): AWT e Swing mostrano l'interazione event-based dentro una sola applicazione, con dispatching locale e callback; un broker di rete non serve. Gli elementi sono:

| Elemento (p. 114) | Ruolo | Esempio (p. 115–117) |
|---|---|---|
| Event source | genera l'evento | `JButton`, `JComboBox` |
| Event object | porta le informazioni sull'evento, inclusa la sorgente | `ActionEvent`, `ItemEvent` |
| Event listener | oggetto notificato; il suo metodo gestisce l'evento | `ActionListener` con `actionPerformed(ActionEvent e)`; `ItemListener` |

Passi (p. 117): (1) creare una classe handler che implementa il listener adatto (`ButtonClicking implements ActionListener`); (2) registrarla presso la sorgente (`yesButton.addActionListener(this)`). Swing smista gli eventi sul *event dispatch thread*: il codice del listener deve finire in fretta per non bloccare l'interfaccia (p. 113).

## Attributi di qualità

| Attributo | Effetto | Perché | Fonte |
|---|---|---|---|
| Estensibilità | + | nuovi componenti reagiscono agli eventi esistenti senza cambiare i producer | [[05_Architectural_Styles_Complete.pdf#page=110]] |
| Separazione delle responsabilità | + | ogni consumer implementa la sua reazione (notificare un cliente, aggiornare un read model) | [[05_Architectural_Styles_Complete.pdf#page=110]] |
| Reattività | + | i consumer asincroni differiscono il lavoro mentre il producer prosegue | [[05_Architectural_Styles_Complete.pdf#page=110]] |
| Scalabilità | + | consumer distribuiti scalano separatamente, se partizionamento, ordine e stato condiviso lo permettono | [[05_Architectural_Styles_Complete.pdf#page=110]] |
| Tracciabilità del flusso | − | il controllo attraversa più reazioni: avanzamento e guasti difficili da tracciare | [[05_Architectural_Styles_Complete.pdf#page=111]] |
| Consistenza | − | con consegna asincrona i consumer aggiornano lo stato in momenti diversi | [[05_Architectural_Styles_Complete.pdf#page=111]] |
| Modificabilità dei contratti | − | cambiare struttura o significato di un evento può toccare più consumer | [[05_Architectural_Styles_Complete.pdf#page=111]] |
| Prestazioni | − | handler lenti, cicli di eventi o canali sovraccarichi ritardano altro lavoro | [[05_Architectural_Styles_Complete.pdf#page=111]] |

## Quando usarlo / quando no

Quando molti componenti devono reagire in modo indipendente a ciò che accade; con cautela se servono garanzie su retry, duplicati, ordinamento e ripristino (p. 111).

## Varianti ed esempi

- Applicazioni Android, GUI, framework per eventi ([[05_Architectural_Styles_Complete.pdf#page=118]]).

## Connessioni

- [[implicit-invocation]], [[publish-subscribe]], [[disaccoppiamento-dei-componenti]].
- [[microservices]]: la coreografia di eventi tra servizi è event-based.

## Fonti

- [[architectural-styles]]

_Aggiornato: 2026-11-24 — ingest 05_Architectural_Styles_Complete.pdf_
