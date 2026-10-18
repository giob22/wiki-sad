#!/usr/bin/env python3
"""Burndown di uno sprint da un GitHub Project (v2), pesato con la taglia dei task.

Legge gli item della iterazione scelta, calcola i punti rimanenti giorno per giorno
(scope - completati) e scrive un CSV e un grafico SVG con la linea ideale.
Solo libreria standard: nessuna dipendenza da installare nella CI.

Variabili d'ambiente (le prime tre servono, le altre hanno un default):
  PROJECT_TOKEN     token personale classico con scope `project` e `repo`
  PROJECT_OWNER     login proprietario del project (es. CapHello)
  PROJECT_NUMBER    numero del project (dall'URL .../projects/<numero>)
  OWNER_TYPE        user | organization                      (default: user)
  ITERATION_TITLE   titolo dell'iterazione; vuoto = quella in corso oggi
  ITERATION_FIELD   nome del campo iterazione                (default: Iteration)
  STATUS_FIELD      nome del campo stato                     (default: Status)
  DONE_VALUE        valore di stato che vale «fatto»         (default: Done)
  POINTS_FIELD      campo Number con i punti                 (default: Punti)
  SIZE_FIELD        campo Size (selezione singola)           (default: Size)
  OUT_DIR           cartella di output                       (default: docs/burndown)

Scrive solo l'iterazione in corso: i file degli sprint conclusi restano com'erano, cosi'
i task non finiti e spostati nello sprint successivo non alterano la storia (un file per sprint).

I punti di un task: campo Number se presente, altrimenti mappatura della taglia
(SIZE_POINTS qui sotto), altrimenti 1.  Prova senza API:  python burndown.py --demo
Controlla i nomi dei campi sul project reale:  python burndown.py --inspect
"""
import csv
import json
import os
import re
import sys
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

SIZE_POINTS = {"XS": 1, "S": 2, "M": 3, "L": 5, "XL": 8}   # mappatura da concordare nel team
# Calendario del progetto PICUS (presentazione, slide 11-12): data di inizio -> durata in giorni.
# La preparatoria dura 3 settimane (eccezione); le tre iterazioni di costruzione 2 settimane.
PIANO = {date(2026, 10, 15): 21, date(2026, 11, 5): 14, date(2026, 11, 19): 14, date(2026, 12, 3): 14}
UTC = timezone.utc

QUERY = """
query($login:String!, $num:Int!, $after:String) {
  OWNER(login:$login) {
    projectV2(number:$num) {
      title
      items(first:100, after:$after) {
        pageInfo { hasNextPage endCursor }
        nodes {
          createdAt updatedAt
          content {
            __typename
            ... on Issue { number title closedAt }
            ... on PullRequest { number title closedAt }
            ... on DraftIssue { title }
          }
          fieldValues(first:30) {
            nodes {
              __typename
              ... on ProjectV2ItemFieldSingleSelectValue { name field { ... on ProjectV2FieldCommon { name } } }
              ... on ProjectV2ItemFieldNumberValue { number field { ... on ProjectV2FieldCommon { name } } }
              ... on ProjectV2ItemFieldIterationValue { title startDate duration field { ... on ProjectV2FieldCommon { name } } }
            }
          }
        }
      }
    }
  }
}
"""


def graphql(token, owner_type, login, num):
    query = QUERY.replace("OWNER", "organization" if owner_type == "organization" else "user")
    nodes, after = [], None
    while True:
        body = json.dumps({"query": query, "variables": {"login": login, "num": num, "after": after}}).encode()
        req = urllib.request.Request("https://api.github.com/graphql", data=body, headers={
            "Authorization": f"Bearer {token}", "Content-Type": "application/json"})
        with urllib.request.urlopen(req) as r:
            data = json.load(r)
        if "errors" in data:
            raise SystemExit(f"Errore GraphQL: {data['errors']}")
        proj = data["data"][owner_type if owner_type == "organization" else "user"]["projectV2"]
        nodes += proj["items"]["nodes"]
        if not proj["items"]["pageInfo"]["hasNextPage"]:
            return proj["title"], nodes
        after = proj["items"]["pageInfo"]["endCursor"]


def parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00")) if s else None


def normalize(nodes, cfg):
    """Trasforma gli item grezzi in dizionari semplici (iterazione, punti, date)."""
    items = []
    for n in nodes:
        f = {"iter": None, "status": None, "points": None, "size": None}
        for v in n["fieldValues"]["nodes"]:
            name = (v.get("field") or {}).get("name")
            if v["__typename"] == "ProjectV2ItemFieldIterationValue" and name == cfg["iter_field"]:
                f["iter"] = v
            elif v["__typename"] == "ProjectV2ItemFieldSingleSelectValue":
                if name == cfg["status_field"]:
                    f["status"] = v["name"]
                elif name == cfg["size_field"]:
                    f["size"] = v["name"]
            elif v["__typename"] == "ProjectV2ItemFieldNumberValue" and name == cfg["points_field"]:
                f["points"] = v["number"]
        c = n["content"] or {}
        points = f["points"] if f["points"] is not None else SIZE_POINTS.get(f["size"], 1)
        done = f["status"] == cfg["done_value"]
        # data di completamento: chiusura dell'issue se c'è, altrimenti ultimo aggiornamento
        done_at = (parse_ts(c.get("closedAt")) or parse_ts(n["updatedAt"])) if done else None
        items.append({"title": c.get("title", "?"), "iter": f["iter"], "points": float(points),
                      "created": parse_ts(n["createdAt"]), "done_at": done_at})
    return items


def pick_iteration(items, title, today):
    iters = {}
    for it in items:
        v = it["iter"]
        if v:
            iters[v["title"]] = (date.fromisoformat(v["startDate"]), int(v["duration"]))
    if title:
        if title not in iters:
            raise SystemExit(f"Iterazione «{title}» non trovata. Disponibili: {sorted(iters)}")
        return title, *iters[title]
    for t, (s, d) in iters.items():
        if s <= today < s + timedelta(days=d):
            return t, s, d
    t = max(iters, key=lambda k: iters[k][0])      # nessuna in corso: l'ultima
    return t, *iters[t]


def compute(items, title, start, days, now):
    """Serie (giorni dall'inizio, scope, completati, rimanenti) a ogni mezzanotte e adesso."""
    mine = [i for i in items if i["iter"] and i["iter"]["title"] == title]
    t0 = datetime.combine(start, datetime.min.time(), UTC)
    stops = [t0 + timedelta(days=k) for k in range(days + 1) if t0 + timedelta(days=k) <= now]
    if now < t0 + timedelta(days=days):
        stops.append(now)                           # punto «adesso» se lo sprint è in corso
    rows = []
    for t in stops:
        scope = sum(i["points"] for i in mine if i["created"] <= t)
        done = sum(i["points"] for i in mine if i["done_at"] and i["done_at"] <= t)
        rows.append(((t - t0).total_seconds() / 86400, scope, done, scope - done))
    base = rows[0][1] if rows and rows[0][1] > 0 else sum(i["points"] for i in mine)
    return mine, base, rows


def render_svg(title, start, days, base, rows, unit="punti"):
    W, H, L, R, T, B = 900, 440, 70, 30, 60, 70
    pw, ph = W - L - R, H - T - B
    ymax = max([base] + [r[1] for r in rows] + [1]) * 1.1
    X = lambda d: L + pw * d / days
    Y = lambda v: T + ph * (1 - v / ymax)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Arial">',
         f'<rect width="{W}" height="{H}" fill="#fff"/>',
         f'<text x="{W/2}" y="28" text-anchor="middle" font-size="17" font-weight="bold">Burndown — {title}</text>',
         f'<text x="{W/2}" y="46" text-anchor="middle" font-size="11" fill="#555">'
         f'{start:%d/%m/%Y} → {(start + timedelta(days=days)):%d/%m/%Y} · {unit} rimanenti</text>']
    step = max(1, round(ymax / 6))
    for v in range(0, int(ymax) + 1, step):
        o.append(f'<line x1="{L}" y1="{Y(v)}" x2="{L+pw}" y2="{Y(v)}" stroke="#e5e7eb"/>')
        o.append(f'<text x="{L-8}" y="{Y(v)+4}" text-anchor="end" font-size="11" fill="#555">{v}</text>')
    for d in range(0, days + 1, max(1, days // 10)):
        day = start + timedelta(days=d)
        o.append(f'<line x1="{X(d)}" y1="{T+ph}" x2="{X(d)}" y2="{T+ph+5}" stroke="#555"/>')
        o.append(f'<text x="{X(d)}" y="{T+ph+20}" text-anchor="middle" font-size="11" fill="#555">{day:%d/%m}</text>')
    o.append(f'<rect x="{L}" y="{T}" width="{pw}" height="{ph}" fill="none" stroke="#555"/>')
    o.append(f'<line x1="{X(0)}" y1="{Y(base)}" x2="{X(days)}" y2="{Y(0)}" stroke="#9ca3af" stroke-width="2" stroke-dasharray="7 5"/>')
    if rows:
        o.append('<polyline fill="none" stroke="#b45309" stroke-width="1.5" stroke-dasharray="2 3" points="'
                 + " ".join(f"{X(r[0]):.1f},{Y(r[1]):.1f}" for r in rows) + '"/>')
        o.append('<polyline fill="none" stroke="#1d4ed8" stroke-width="2.5" points="'
                 + " ".join(f"{X(r[0]):.1f},{Y(r[3]):.1f}" for r in rows) + '"/>')
        for r in rows:
            o.append(f'<circle cx="{X(r[0]):.1f}" cy="{Y(r[3]):.1f}" r="3.5" fill="#1d4ed8"/>')
    ly = H - 24
    for x, color, dash, label in ((L, "#9ca3af", "7 5", "ideale"), (L + 120, "#1d4ed8", "", "rimanenti"),
                                  (L + 250, "#b45309", "2 3", "scope (totale assegnato)")):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        o.append(f'<line x1="{x}" y1="{ly}" x2="{x+30}" y2="{ly}" stroke="{color}" stroke-width="2.5"{d}/>')
        o.append(f'<text x="{x+38}" y="{ly+4}" font-size="12">{label}</text>')
    o.append("</svg>")
    return "\n".join(o)


def demo_items():
    """Dati finti: sprint di 21 giorni, 10 task di taglie diverse, qualcuno aggiunto in corso."""
    start = date(2026, 10, 15)
    def it(title, pts, created_day, done_day):
        t0 = datetime.combine(start, datetime.min.time(), UTC)
        return {"title": title, "points": float(pts), "created": t0 + timedelta(days=created_day),
                "done_at": t0 + timedelta(days=done_day, hours=12) if done_day is not None else None,
                "iter": {"title": "S1 - Preparazione", "startDate": start.isoformat(), "duration": 21}}
    return [it("S1-01", 3, -2, 5), it("S1-02", 5, -2, 8), it("S1-03", 5, -2, 12), it("S1-04", 3, -2, 9),
            it("S1-05", 5, -2, 15), it("S1-06", 3, -2, None), it("S1-07", 5, -2, None), it("S1-08", 2, -2, None),
            it("S1-09", 3, 4, None), it("S1-10", 2, 6, None)]


def inspect(ptitle, nodes):
    """Diagnostica: mostra project, campi e valori trovati, per controllare i nomi in configurazione."""
    seen = {}
    for n in nodes:
        for v in n["fieldValues"]["nodes"]:
            name = (v.get("field") or {}).get("name")
            if not name:
                continue
            val = v.get("name") or v.get("number") or (f"{v['title']} ({v['startDate']}, {v['duration']} gg)"
                                                       if "startDate" in v else "?")
            seen.setdefault((name, v["__typename"].replace("ProjectV2ItemField", "")), set()).add(str(val))
    print(f"Project «{ptitle}»: {len(nodes)} item")
    for (name, kind), vals in sorted(seen.items()):
        print(f"  campo «{name}» [{kind}]: {sorted(vals)}")
    iters = {}
    for n in nodes:
        for v in n["fieldValues"]["nodes"]:
            if "startDate" in v:
                iters[v["title"]] = (date.fromisoformat(v["startDate"]), int(v["duration"]))
    print("Iterazioni trovate (con item) e confronto con il piano del progetto:")
    for t, (st, d) in sorted(iters.items(), key=lambda kv: kv[1][0]):
        esito = "ok" if PIANO.get(st) == d else (
            f"ATTENZIONE: il piano prevede {PIANO[st]} giorni da quella data" if st in PIANO
            else "ATTENZIONE: data di inizio non presente nel piano")
        print(f"  «{t}»: {st:%d/%m/%Y}, {d} gg, fine {st + timedelta(days=d):%d/%m/%Y} -> {esito}")
    print("Item senza issue collegata (bozze):", sum(1 for n in nodes if (n['content'] or {}).get('__typename') == 'DraftIssue'))


def main():
    if "--demo" in sys.argv:
        items = demo_items()
        now = datetime(2026, 10, 30, 12, tzinfo=UTC)
        out = Path(os.environ.get("OUT_DIR", "."))
    else:
        cfg = {"iter_field": os.environ.get("ITERATION_FIELD", "Iteration"),
               "status_field": os.environ.get("STATUS_FIELD", "Status"),
               "done_value": os.environ.get("DONE_VALUE", "Done"),
               "points_field": os.environ.get("POINTS_FIELD", "Punti"),
               "size_field": os.environ.get("SIZE_FIELD", "Size")}
        ptitle, nodes = graphql(os.environ["PROJECT_TOKEN"], os.environ.get("OWNER_TYPE", "user"),
                                os.environ["PROJECT_OWNER"], int(os.environ["PROJECT_NUMBER"]))
        if "--inspect" in sys.argv:
            inspect(ptitle, nodes)
            return
        items = normalize(nodes, cfg)
        now = datetime.now(UTC)
        out = Path(os.environ.get("OUT_DIR", "docs/burndown"))
    title, start, days = pick_iteration(items, os.environ.get("ITERATION_TITLE", ""), now.date())
    mine, base, rows = compute(items, title, start, days, now)
    out.mkdir(parents=True, exist_ok=True)
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    with open(out / f"burndown-{slug}.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["giorno", "scope", "completati", "rimanenti"])
        w.writerows([(f"{r[0]:.2f}", r[1], r[2], r[3]) for r in rows])
    (out / f"burndown-{slug}.svg").write_text(render_svg(title, start, days, base, rows), encoding="utf-8")
    print(f"{title}: {len(mine)} task, base {base:g} punti, rimanenti {rows[-1][3]:g}" if rows else "nessun dato")


if __name__ == "__main__":
    main()
