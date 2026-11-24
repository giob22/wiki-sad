---
tipo: entità
categoria: stile
famiglia: "implicit invocation / decentralizzati"
---

# Peer-to-peer (P2P)

## Contesto e problema

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=121]], [[05_Architectural_Styles_Complete.pdf#page=122]], [[05_Architectural_Styles_Complete.pdf#page=123]]

Condividere **risorse e servizi** (dati, CPU, disco) tra molti nodi senza un server centrale che sia collo di bottiglia. Funzioni tipiche: file sharing, file storage, file system distribuito, storage ridondante, calcolo distribuito. Requisiti non funzionali tipici: disponibilità, affidabilità, prestazioni, scalabilità, anonimato. (Lo stile compare nell'appendice delle slide, «additional styles».)

## Soluzione

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=121]], [[05_Architectural_Styles_Complete.pdf#page=122]], [[05_Architectural_Styles_Complete.pdf#page=125]]

- Architettura **decentralizzata**; stato e comportamento **distribuiti**; ogni peer è **client e server** insieme.
- I peer sono componenti indipendenti con stato e thread di controllo propri; **connettori** = protocolli di rete, spesso specializzati; **elementi dati** = messaggi di rete.
- **Tre fasi:** *boot* (connessione alla rete; raro nel P2P), *lookup* (ricerca di un fornitore del servizio, di solito SuperPeer), *resource sharing* (consegna delle risorse, in più segmenti).

**Tre organizzazioni** (p. 127), che differiscono per **come si localizzano le risorse**:

| | Centralizzato | Decentralizzato (puro) | Ibrido |
|---|---|---|---|
| Localizzazione | un index server centrale con il database di contenuti e utenti | ogni peer è index server e router delle query | dorsale di **Super Node** con funzione di indice |
| Esempio | Napster | Gnutella | Skype (delle origini) |
| Pagine | 128–134 | 135–141 | 142–152 |

## Diagramma

![[lez08-stili-p128-indice-centralizzato.png]]
*Indice centralizzato ([[05_Architectural_Styles_Complete.pdf#page=128]]): Peer A manda la query (Q) all'Index server, che risponde (R) indicando il peer con il contenuto; il download avviene direttamente tra i peer. Quando un peer si collega informa il server di IP e contenuti.*

![[lez08-stili-p130-indice-componenti.png]]
*Componenti ([[05_Architectural_Styles_Complete.pdf#page=130]]): Peer A e Peer B si scambiano dati con interfacce Provide/Require data; entrambi usano le interfacce Login e Search del Directory server.*

![[lez08-stili-p131-indice-classi.png]]
*Classi ([[05_Architectural_Styles_Complete.pdf#page=131]]): Directory Index (`Search()`, `Login()`) – 1 … * – Peer (`FileTransfer()`), con ruoli requester/provider tra peer.*

![[lez08-stili-p132-indice-sequenza.png]]
*Sequenza ([[05_Architectural_Styles_Complete.pdf#page=132]]): i peer fanno `Login(IP, content)`; un peer invia `Query(q)`, il Directory server fa `Search(q)` e restituisce `List<peer>`; il richiedente chiama `Download(q)` direttamente dai peer elencati.*

![[lez08-stili-p133-napster.png]]
*Napster ([[05_Architectural_Styles_Complete.pdf#page=133]]): a sinistra la sequenza numerata tra Peer A, B, C e «Peer & Content Directory»; a destra il Central Index Server al centro dei client su Internet, con il trasferimento diretto tra due client.*

![[lez08-stili-p136-p2p-decentralizzato.png]]
*P2P decentralizzato ([[05_Architectural_Styles_Complete.pdf#page=136]]): le query (Q) si propagano di vicino in vicino, le risposte (R) tornano indietro, poi il download è diretto.*

![[lez08-stili-p138-gnutella.png]]
*Gnutella ([[05_Architectural_Styles_Complete.pdf#page=138]]): a sinistra l'overlay di peer; a destra una query «Baby Go Home.mp3» che attraversa 6–7 livelli secondo il «time to live» fino al peer che risponde «I've got it!», su una rete di 8.000–10.000 computer.*

![[lez08-stili-p140-p2p-decentralizzato-classi.png]]
*Classi ([[05_Architectural_Styles_Complete.pdf#page=140]]): un'unica classe Peer con `service1() … serviceN()` e associazione \* – \* con sé stessa (requester/provider).*

![[lez08-stili-p143-p2p-ibrido.png]]
*Ibrido ([[05_Architectural_Styles_Complete.pdf#page=143]]): i peer ordinari si collegano ai Super Node, che si scambiano query e risposte; il download è diretto.*

![[lez08-stili-p145-ibrido-componenti.png]]
*Componenti ([[05_Architectural_Styles_Complete.pdf#page=145]]): due Simple peer si scambiano dati; ciascuno fa login/search sul proprio Super peer; i Super peer si scambiano «Disseminate query».*

![[lez08-stili-p146-ibrido-classi.png]]
*Classi ([[05_Architectural_Styles_Complete.pdf#page=146]]): Peer (`FileTransfer()`) è specializzato in Super Peer (`Search()`, `Login()`, `DisseminateQuery()`) e Simple Peer.*

![[lez08-stili-p147-ibrido-sequenza.png]]
*Sequenza ([[05_Architectural_Styles_Complete.pdf#page=147]]): login sul SuperPeer; `Query(q)` al proprio SuperPeer, che esegue `Search(q)` e `DisseminateQuery(q)` agli altri SuperPeer; la lista dei peer torna al richiedente, che scarica con `Download(q)`.*

![[lez08-stili-p148-skype-supernodi.png]]
*Skype delle origini ([[05_Architectural_Styles_Complete.pdf#page=148]]): un Login Server, tre supernodi (A, B, C) in triangolo e i peer ordinari collegati ciascuno al proprio supernodo.*

![[lez08-stili-p151-skype-architettura.png]]
*Architettura Skype ([[05_Architectural_Styles_Complete.pdf#page=151]]): livelli di registrazione/autenticazione, super node e client; a destra la rete di host ordinari (SC) e super node (SN); chiamate tra client pubblici e tra client dietro firewall.*

![[lez08-stili-p126-bittorrent.png]]
*BitTorrent ([[05_Architectural_Styles_Complete.pdf#page=126]]): il tracker identifica lo *swarm*; i peer che hanno il file completo sono *seed* (100%), gli altri hanno percentuali parziali; ogni client riceve e invia più pezzi del file contemporaneamente.*

## Attributi di qualità

| Variante | Benefici | Trappole | Fonte |
|---|---|---|---|
| Centralizzato | poco stato per nodo; banda limitata; alto tasso di successo; ricerca rapida; facile da implementare | single point of failure; vulnerabile alla censura; scala limitata; carico sbilanciato; database obsoleto | [[05_Architectural_Styles_Complete.pdf#page=134]] |
| Decentralizzato | poco stato per nodo; tollerante ai guasti | molta banda; tempo lungo per localizzare; nessuna garanzia di successo; carico sbilanciato | [[05_Architectural_Styles_Complete.pdf#page=141]] |
| Ibrido | stato per nodo, banda e tempo di ricerca gestibili; successo garantito | carico sbilanciato; tolleranza ai guasti più difficile | [[05_Architectural_Styles_Complete.pdf#page=152]] |

In generale (p. 154): la decentralizzazione può tollerare alcuni guasti di nodo se esistono peer e percorsi alternativi; la capacità può crescere con le risorse messe a disposizione dai peer; la topologia cambia dinamicamente. **Scoperta delle risorse (p. 153):** senza directory centrale è il problema fondamentale; nel P2P puro la richiesta è inoltrata a molti peer (limitata da algoritmi di *query routing* e dalla banda); gli ibridi usano peer o directory selezionati; l'originale Napster centralizzava la ricerca e decentralizzava il trasferimento.

## Quando usarlo / quando no

🧩 Si sceglie la variante in base al compromesso tra semplicità di ricerca (centralizzato) e resistenza ai guasti (decentralizzato), con l'ibrido come via di mezzo ([[05_Architectural_Styles_Complete.pdf#page=153]]).

## Varianti ed esempi

- **Gnutella** ([[05_Architectural_Styles_Complete.pdf#page=139]]): client e *peer cache* per scoprire gli IP; richiesta *Gnutella Connect*, risposta *Gnutella OK* o rifiuto (capacità o protocollo incompatibile); *ping/pong* per scoprire peer e risorse; le query hanno un **TTL** decrementato a ogni inoltro (limita propagazione e carico); identificatori di messaggio univoci evitano i cicli.
- **Skype delle origini** (pp. 148–150): architettura mista client–server e P2P risolve la *discovery*; i supernodi replicano le directory risolvendo scalabilità e robustezza di Napster; la promozione dei peer a supernodi per capacità di rete e di calcolo: «non un peer qualsiasi» per i servizi importanti; protocollo proprietario cifrato per le chiamate rilanciate dai supernodi; solo client emessi da Skype, resistenti a ispezione e modifica, entrano in rete.
- **Storia (p. 124):** Napster (1999) e Gnutella (2000); nel 2000 il client Napster scaricato da 50 milioni di utenti, picco di 7 TB/giorno.
- **Applicazioni (p. 155):** distribuzione/storage di contenuti, file sharing (Gnutella, FastTrack, BitTorrent, eMule, uTorrent), TV P2P storica (PPLive), chat e telefonia Internet storica, CDN (CoralCDN), reti di sensori.
- **Lunar Lander P2P (p. 156):** a T₀ LL1 chiede ai peer vicini se altre navicelle sono atterrate; la richiesta è inoltrata; quando LL5 trova la risorsa il risultato torna a LL1; a T₁ LL1 contatta LL5 direttamente.

## Connessioni

- [[client-server]]: il P2P elimina la distinzione dei ruoli.
- [[publish-subscribe]], [[event-based]]: altri stili decentralizzati/disaccoppiati.
- [[stili-architetturali]], [[lunar-lander-in-ogni-stile]].

## Fonti

- [[architectural-styles]]

_Aggiornato: 2026-11-24 — ingest 05_Architectural_Styles_Complete.pdf_
