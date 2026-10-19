---
tipo: progetto-artefatto
stato: pronto — gesti extra da validare dal team
data: 2026-10-19
---

# Mascotte del team: il pinguino con elmetto e fragola

Animazione della mascotte del gruppo *Pinguini alla Fragola*, ricavata da una tavola di **25 frame** (5 × 5) fornita dal team ([[tavola-25-frame.webp]]). Qui ci sono le animazioni, come sono state costruite e come rigenerarle. Non c'entra con il corso: è materiale per presentazioni, README e review.

> 🧩 Elaborazione mia, senza fonti nelle slide: tutto il resto della pagina è lavoro su un'immagine del team.

## Animazione principale

![[pinguino-lavoro-fluida.webp]]
*Ciclo completo: 77 fotogrammi, 4,15 secondi, sfondo trasparente, 660 × 508 px. La stessa animazione in GIF su sfondo bianco: [[pinguino-lavoro-fluida.gif]].*

**Cosa racconta**, dai frame della tavola:

| Frame | Azione |
|---|---|
| 1–5 | il pinguino abbraccia la fragola, la abbassa e la appoggia a terra, alla sua sinistra |
| 6–7 | si rialza e prende il martello |
| 8–11 | primo colpo: alza il martello, lo cala (linee di movimento) e colpisce (scintille) |
| 12–15 | secondo colpo: carica con il martello in alto, cala, colpisce |
| 16–19 | rialza il martello, lo abbassa alla cintura, sorride, posizione neutra |
| 20–25 | si china, raccoglie la fragola, la solleva e la abbraccia sorridendo; il frame 25 coincide con il 1, quindi il ciclo si chiude senza salti |

**Versione fedele ai 25 disegni**, senza fotogrammi aggiunti (12 fotogrammi al secondo circa, con le stesse pose tenute): ![[pinguino-lavoro-originale.webp]] — GIF: [[pinguino-lavoro-originale.gif]].

## Versione estesa: più lunga e più fluida

![[pinguino-lavoro-estesa.webp]]
*Storia completa di **11,3 secondi**, 341 fotogrammi, fino a **50 fotogrammi al secondo** (un fotogramma ogni 20 ms) durante il movimento, sfondo trasparente, 652 × 597 px. GIF su fondo bianco (326 × 298 px): [[pinguino-lavoro-estesa.gif]].*

**La storia**, in ordine:

1. il pinguino **respira** tenendo la fragola;
2. **posa la fragola** a terra e prende il martello;
3. **primo colpo**, poi **secondo colpo** (le pose originali 8–15);
4. **due colpi in più**: il martello torna su lentamente, si ferma in alto e cala veloce, con scossa all'impatto;
5. **ripone il martello**, sorride e **annuisce** due volte;
6. **riprende la fragola**, la abbraccia e fa il **salto di gioia**;
7. **dondola** contento e torna alla posa iniziale, per ripartire.

**Cosa cambia rispetto alla versione precedente**

| | Versione fluida (4,15 s) | Versione estesa (11,3 s) |
|---|---|---|
| Fotogrammi intermedi tra due pose | 2–3, ogni 30–40 ms | 6 (4 dove il flusso è meno affidabile), ogni 20 ms |
| Colpi di martello | 2 | 4 |
| Gesti extra dentro la storia | no | respiro, cenno di assenso, salto, dondolio |
| Ombra a terra | no | sì, uguale in tutta la storia (nel salto si rimpicciolisce) |
| Peso WebP | 3 MB | 6,5 MB |

Gli intermedi sono sempre in numero **pari**: così nessun fotogramma cade esattamente a metà tra due pose, dove la deformazione del flusso ottico sarebbe massima. Il passaggio da un frame sorgente all'altro avviene tra il terzo e il quarto intermedio, con deformazione di al massimo circa un terzo.

## Come è fatta (e perché è fluida)

1. **Ritaglio.** Lo sfondo della tavola è già trasparente. Un frame è un gruppo di pixel collegati; scintille e linee di movimento restano con il loro frame (dilatazione di 9 px, che dà esattamente 25 gruppi).
2. **Allineamento a terra.** Ogni frame è appoggiato sulla stessa linea dei piedi. Orizzontalmente si usa il centro della **parte bassa del corpo**, escludendo fragola e martello, che si muovono. Anteprima dei frame allineati: [[anteprima-frame-allineati.png]].
3. **Fotogrammi intermedi.** Tra due pose si calcola il movimento dei pixel (*flusso ottico*, algoritmo DIS di OpenCV) e si deforma **un solo frame per volta**, il primo fino a metà e il secondo da metà in poi. Non si sovrappongono mai due immagini, per questo non compare la «doppia figura» tipica delle dissolvenze. Il flusso è smussato (sigma 8) perché non strappi i contorni neri.
4. **Ritmo da animatore.**
   - 3 intermedi tra le pose, 2 dove il flusso è meno affidabile (la fragola che sale, la testa che gira);
   - la discesa del martello **accelera**: la curva è quadratica;
   - gli impatti arrivano in fretta (un solo intermedio da 40 ms) e poi la posa è **tenuta** 150 ms;
   - tenute anche sulla posa iniziale (240 ms), sul martello in alto (90 ms) e sulla posa sorridente (120 ms).

## Gesti extra

Sono movimenti che ho **dedotto dalle pose esistenti** (schiacciamento, stiramento, rotazione, ombra a terra), non nuovi disegni.

| Gesto | Posa usata | Cosa fa |
|---|---|---|
| Salto di gioia | 23 (occhi felici) | si schiaccia, si stira, salta con l'ombra che si rimpicciolisce, atterra con rimbalzo |
| Martellata ripetuta | 12–15 | alza, cala veloce, impatto con scossa, torna su lentamente, tre volte |
| Dondolio felice | 25 | oscilla di circa 3° sui piedi, con un leggero schiacciamento |
| Respiro | 19 | si gonfia e si sgonfia piano, per le pause tra un gesto e l'altro |
| Annuisce | 18 | due cenni di assenso con un piccolo schiacciamento |

![[pinguino-salto-di-gioia.webp]] ![[pinguino-martellata.webp]]

![[pinguino-dondolio.webp]] ![[pinguino-respiro.webp]] ![[pinguino-si.webp]]

*Questi gesti sono solo in WebP animato. File: [[pinguino-salto-di-gioia.webp]], [[pinguino-martellata.webp]], [[pinguino-dondolio.webp]], [[pinguino-respiro.webp]], [[pinguino-si.webp]].*

## Limiti, detti chiaramente

- **Le pose sono solo le 25 disegnate.** Non ho potuto disegnare pose nuove (salutare con la mano, pollice in su) nello stesso stile della mascotte: i gesti extra sono movimenti delle pose esistenti. Se generi altre pose con lo stesso strumento che ha prodotto la tavola, lo script può integrarle.
- **Gli intermedi sono calcolati, non disegnati.** In alcune transizioni, per esempio quando la fragola viene sollevata (frame 21 → 22), i contorni si deformano un po' come gomma per qualche fotogramma. Ho controllato i fotogrammi uno per uno nei fogli di anteprima e non ci sono doppie immagini né strappi, ma non ho potuto **guardare l'animazione in riproduzione**: ho verificato fotogrammi, numero e durate.
- **GIF e WebP:** il WebP ha lo sfondo trasparente, la GIF è su fondo bianco (un GIF trasparente avrebbe i bordi seghettati).
- **Peso:** circa 33 MB in tutto. I gesti sono solo in WebP e la versione estesa è compressa (qualità 52, alpha 70, margini ritagliati): a 2× di ingrandimento i contorni restano nitidi. Per una pagina web conviene la versione fluida (3 MB) oppure l'estesa solo se il peso non è un problema.

## Rigenerare o modificare

Lo script [[genera_animazione_pinguino.py]] fa tutto dalla tavola:

```powershell
py -3.11 output\pinguino\genera_animazione_pinguino.py output\pinguino\sorgente\tavola-25-frame.webp output\pinguino
```
Servono `numpy`, `pillow` e `opencv-python-headless`. Con `--frame` salva anche i 25 frame allineati come PNG trasparenti; con `--solo-estesa` rigenera soltanto la versione estesa (circa sei minuti, quasi tutti per la compressione del WebP). I parametri (ingrandimento, durata dei fotogrammi, numero di intermedi per coppia, pose tenute) sono costanti in testa al file.

_Aggiornato: 2026-10-19 — prima stesura_
_Aggiornato: 2026-10-19 — versione estesa (11,3 s, 50 fps)_
