"""Aggiunge o sostituisce lezioni in wiki/corso-completo.md e ricostruisce l'indice.

Uso:  python output/assembla_corso.py parte-lezione-8.md [altre-parti.md ...]

Ogni file «parte» contiene UNA lezione, che comincia con «## Lezione N — titolo» e ha la riga «*Fonte: file.pdf (...)*».
La lezione N sostituisce quella già presente (o viene aggiunta); le lezioni restano ordinate per numero.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FILE = ROOT / "wiki" / "corso-completo.md"
TITOLO = re.compile(r"(?m)^## Lezione (\d+) — (.+?)\s*$")


def dividi(testo):
    """(testata fino a «## Indice» escluso, {n: testo della lezione})"""
    i = testo.index("## Indice")
    testata = testo[:i]
    resto = testo[i:]
    resto = resto[resto.index("## Lezione"):] if "## Lezione" in resto else ""
    parti = re.split(r"(?m)^(?=## Lezione \d+ — )", resto)
    lezioni = {}
    for p in parti:
        m = TITOLO.match(p)
        if m:
            lezioni[int(m.group(1))] = p.strip("\n")
    return testata, lezioni


def riga_indice(n, testo):
    titolo = TITOLO.match(testo).group(2)
    fonte = re.search(r"(?m)^\*Fonte:(.*)$", testo).group(1)
    nomi = [re.sub(r"^\s*e\s+", "", x).strip() for x in re.findall(r"([A-Za-z0-9][^()]*?\.pdf)(?=\s*\()", fonte)]
    return f"| {n} | [[#Lezione {n} — {titolo}\\|{titolo}]] | {', '.join(dict.fromkeys(nomi))} |"


def main():
    testata, lezioni = dividi(FILE.read_text(encoding="utf-8"))
    for nome in sys.argv[1:]:
        t = pathlib.Path(nome).read_text(encoding="utf-8").strip("\n")
        m = TITOLO.match(t)
        if not m:
            raise SystemExit(f"{nome}: non comincia con «## Lezione N — titolo»")
        lezioni[int(m.group(1))] = t
    righe = [riga_indice(n, lezioni[n]) for n in sorted(lezioni)]
    out = (testata + "## Indice\n\n| # | Lezione | PDF sorgente |\n|---|---|---|\n" + "\n".join(righe) + "\n\n"
           + "\n\n".join(lezioni[n] for n in sorted(lezioni)) + "\n")
    FILE.write_text(out, encoding="utf-8", newline="\n")
    print(f"scritto {FILE.name}: {len(lezioni)} lezioni, {len(out.splitlines())} righe")


if __name__ == "__main__":
    main()
