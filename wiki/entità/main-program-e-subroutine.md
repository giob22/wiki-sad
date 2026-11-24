---
tipo: entità
categoria: stile
famiglia: "tradizionali e influenzati dal linguaggio"
---

# Main program e subroutine (call–return)

## Contesto e problema

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=9]]

Un programma si costruisce per **decomposizione funzionale gerarchica**: il compito principale è spezzato in sottocompiti, ciascuno in una subroutine, e così via. C'è **un solo thread di controllo**, gestito dal linguaggio di programmazione.

## Soluzione

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=9]], [[05_Architectural_Styles_Complete.pdf#page=10]]

| Aspetto | Valore |
|---|---|
| Componenti | main program e subroutine |
| Connettori | chiamate di funzione o procedura |
| Elementi dati | valori passati alle e restituiti dalle subroutine |
| Topologia | gerarchia statica; la struttura complessiva è un grafo orientato |
| Vincoli | nessuno |
| Invariante | ragionamento gerarchico: la correttezza di una subroutine dipende da quella delle subroutine che chiama |

La struttura dei sottosistemi resta **implicita**: le subroutine sono raggruppate in moduli o file, ma lo stile non lo impone.

## Diagramma

![[lez08-stili-p8-main-program-lunar-lander.png]]
*Lunar Lander in call–return ([[05_Architectural_Styles_Complete.pdf#page=8]]): il Main Program chiama tre procedure — acquisire il burn rate (ingresso: nessuno, uscita: throttle), simulare l'ambiente (ingresso: altitudine, throttle, carburante, tempo, velocità; uscita: altitudine, carburante, velocità), mostrare i valori (ingresso: altitudine, carburante, tempo, velocità; nessuna uscita). Le scatole sono i moduli, quelle gialle i connettori «Procedure Call».*

## Attributi di qualità

| Attributo | Effetto | Perché | Fonte |
|---|---|---|---|
| Modularità | + | si sostituisce una subroutine preservando la semantica della sua interfaccia | [[05_Architectural_Styles_Complete.pdf#page=10]] |
| Scalabilità (applicazioni grandi) | − | non regge la crescita: la struttura implicita non guida l'organizzazione | [[05_Architectural_Styles_Complete.pdf#page=10]] |
| Modificabilità (nuovi requisiti) | − | «sforzo imprevedibile» per i nuovi requisiti; poca attenzione alle strutture dati | [[05_Architectural_Styles_Complete.pdf#page=10]] |

## Quando usarlo / quando no

> 📄 Fonte: [[05_Architectural_Styles_Complete.pdf#page=10]]

Piccoli programmi ed esempi didattici. Da evitare per applicazioni grandi (scalabilità limitata, dati trascurati).

## Varianti ed esempi

- Linguaggi imperativi tradizionali: BASIC, Pascal, C ([[05_Architectural_Styles_Complete.pdf#page=10]]).
- Lunar Lander in versione call–return, confrontata con quella a oggetti in [[object-oriented]] e [[lunar-lander-in-ogni-stile]].

## Connessioni

- [[object-oriented]]: stessa funzione, responsabilità di I/O distribuite diversamente.
- [[stili-architetturali]]: famiglia degli stili tradizionali.

## Fonti

- [[architectural-styles]]

_Aggiornato: 2026-11-24 — ingest 05_Architectural_Styles_Complete.pdf_
