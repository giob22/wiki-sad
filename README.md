# Wiki Software Architecture Design

Wiki personale del corso **Software Architecture Design** (LM Ingegneria Informatica, UNINA, a.a. 2026/27, prof.ssa Anna Rita Fasolino). Lo mantiene Claude Code secondo lo schema in [CLAUDE.md](CLAUDE.md); si consulta con Obsidian (la cartella della repo è il vault) e con il **sito di studio**, che contiene tutta e sola la teoria.

Struttura derivata dal template `giob22/wiki-template`.

## Come è organizzata

| Cartella / file | Contenuto |
|---|---|
| `raw/` | PDF delle lezioni (una sola versione, la più completa), figure estratte in `raw/assets/` |
| `wiki/corso-completo.md` | testo di studio: tutte le lezioni, solo teoria, solo contenuto delle slide; **sorgente del sito** |
| `wiki/` | indice, log, panoramica, lezioni, glossario, avanzamento; pagine concetto / entità / fonte / esercizio |
| `wiki/progetto/` e `progetto/` | il progetto PICUS (pagine e file): **non è teoria**, non va sul sito |
| `corso.toml` | dati del corso e configurazione del sito |
| `output/` | script del sito (`crea_sito.py`), PDF di studio, controlli, animazioni e grafici |

## Sito di studio (in locale)

```bash
pip install -r requirements.txt
python output/crea_sito.py                 # genera _site/
python -m http.server -d _site 8000        # anteprima su http://localhost:8000
python output/controlla_corso.py           # controllo di integrità di corso-completo.md
```

Ogni lezione è una pagina; sotto, a comparsa, le spiegazioni e gli esempi espansi delle pagine concetto. La pubblicazione online (Cloudflare) è rimandata.
