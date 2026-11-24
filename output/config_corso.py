"""Legge corso.toml (radice della repo) e restituisce la configurazione con i valori di default.

Usato da crea_sito.py, crea_pdf.py e riferimenti_nei_titoli.py. Richiede Python 3.11+ (tomllib).
"""
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILE = ROOT / "corso.toml"

DEFAULT_LEZIONE = dict(titolo="", breve="", inizio="", sito=True, concetti=[], esercizi=[], fonte="",
                       domande=False, domande_filtro=[])


def carica():
    dati = tomllib.loads(FILE.read_text(encoding="utf-8")) if FILE.exists() else {}
    corso = {"nome": "Corso", "sigla": "wiki", "descrizione": "", **dati.get("corso", {})}
    sito = {"intro": "", "briciola": "Corso", "lezioni": "tutte", "note": [], **dati.get("sito", {})}
    lezioni = {}
    for voce in dati.get("lezioni", []):
        if "n" not in voce:
            raise SystemExit(f"corso.toml: una voce [[lezioni]] non ha il numero n: {voce}")
        lezioni[int(voce["n"])] = {**DEFAULT_LEZIONE, **voce}
    figure = []
    for voce in dati.get("figure", []):
        figure.append((int(voce["lezione"]), voce["sezione"], list(voce.get("disegni", []))))
    return dict(corso=corso, sito=sito, lezioni=lezioni, figure=figure, pdf_corti=dati.get("pdf_corti", {}))


def segnaposto(testo):
    """True se il testo è ancora un segnaposto del template ({{...}})."""
    return "{{" in str(testo)
