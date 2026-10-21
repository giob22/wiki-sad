"""Genera il file Word del capitolo A2 «Stakeholder e contesto» (issue S1-01), versione snella.

Uso:  py -3.11 genera_docx_a2.py <png-context-diagram> <file-docx-di-output>
Richiede python-docx.  Contenuto allineato a wiki/progetto/a2-stakeholder-e-contesto.md.
Etichette di stato come nel documento del gruppo: Fonte, Proposta, Ipotesi, Da compilare o verificare.
Fonti: F01 presentazione PICUS, F02 desiderata del committente, F03 AGENTS.md, F06 incontro con lo stakeholder (BA.pdf).
"""
import re
import sys

from docx import Document
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

PNG, OUT = sys.argv[1], sys.argv[2]
doc = Document()

# ---------- pagina e stili ----------
sec = doc.sections[0]
sec.orientation = WD_ORIENT.PORTRAIT
sec.page_width, sec.page_height = Cm(21), Cm(29.7)
sec.left_margin = sec.right_margin = Cm(2)
sec.top_margin = sec.bottom_margin = Cm(2)

normal = doc.styles["Normal"]
normal.font.name = "Calibri"
normal.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
normal.font.size = Pt(10.5)
normal.paragraph_format.space_after = Pt(6)

for name, size, color in (("Heading 1", 18, "1F3864"), ("Heading 2", 13, "2F5496"), ("Heading 3", 11, "2F5496")):
    st = doc.styles[name]
    st.font.name = "Calibri"
    for att in ("eastAsia", "ascii", "hAnsi"):
        st.element.rPr.rFonts.set(qn(f"w:{att}"), "Calibri")
    st.font.size = Pt(size)
    st.font.bold = True
    st.font.color.rgb = RGBColor.from_string(color)
    st.paragraph_format.space_before = Pt(14 if name != "Heading 3" else 10)
    st.paragraph_format.space_after = Pt(6)
    st.paragraph_format.keep_with_next = True

hp = sec.header.paragraphs[0]
hp.text = "Elaborato di Software Architecture Design\nPinguini alla Fragola"
for r in hp.runs:
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(0x59, 0x59, 0x59)


def numero_pagina(paragraph):
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = paragraph.add_run()
    for kind, txt in (("begin", None), (None, "PAGE"), ("end", None)):
        if kind:
            el = OxmlElement("w:fldChar")
            el.set(qn("w:fldCharType"), kind)
        else:
            el = OxmlElement("w:instrText")
            el.set(qn("xml:space"), "preserve")
            el.text = txt
        run._r.append(el)
    run.font.size = Pt(9)


numero_pagina(sec.footer.paragraphs[0])


# ---------- utilità ----------
def runs(par, s, size=None, color=None):
    for part in re.split(r"(\*\*[^*]+\*\*)", s):
        if not part:
            continue
        bold = part.startswith("**") and part.endswith("**")
        r = par.add_run(part[2:-2] if bold else part)
        r.bold = bold
        if size:
            r.font.size = Pt(size)
        if color:
            r.font.color.rgb = RGBColor.from_string(color)


def para(s, size=None, italic=False, after=None):
    p = doc.add_paragraph()
    runs(p, s, size)
    if italic:
        for r in p.runs:
            r.italic = True
    if after is not None:
        p.paragraph_format.space_after = Pt(after)
    return p


def bullet(s):
    p = doc.add_paragraph(style="List Bullet")
    runs(p, s)
    p.paragraph_format.space_after = Pt(2)


def numerato(n, s):
    """Elenco numerato a mano: la numerazione automatica di Word proseguirebbe tra elenchi diversi."""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.8)
    p.paragraph_format.first_line_indent = Cm(-0.6)
    p.paragraph_format.space_after = Pt(2)
    runs(p, f"{n}.  " + s)


def sezione(orizzontale):
    """Nuova pagina, in orizzontale o in verticale."""
    sc = doc.add_section(WD_SECTION.NEW_PAGE)
    sc.orientation = WD_ORIENT.LANDSCAPE if orizzontale else WD_ORIENT.PORTRAIT
    sc.page_width, sc.page_height = (Cm(29.7), Cm(21)) if orizzontale else (Cm(21), Cm(29.7))
    sc.left_margin = sc.right_margin = Cm(1.5) if orizzontale else Cm(2)
    sc.top_margin = sc.bottom_margin = Cm(1.8) if orizzontale else Cm(2)


def casella(spuntata, s):
    p = doc.add_paragraph()
    r = p.add_run("☑ " if spuntata else "☐ ")
    r.font.name = "Segoe UI Symbol"
    runs(p, s)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.left_indent = Cm(0.5)


def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hexcolor)
    tcPr.append(shd)


def tabella(header, rows, widths, size=9):
    t = doc.add_table(rows=1, cols=len(header))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    for i, h in enumerate(header):
        c = t.rows[0].cells[i]
        c.text = ""
        runs(c.paragraphs[0], f"**{h}**", size, "FFFFFF")
        shade(c, "2F5496")
    th = OxmlElement("w:tblHeader")
    th.set(qn("w:val"), "true")
    t.rows[0]._tr.get_or_add_trPr().append(th)
    for row in rows:
        cells = t.add_row().cells
        for i, val in enumerate(row):
            cells[i].text = ""
            runs(cells[i].paragraphs[0], f"**{val}**" if i == 0 else val, size)
            cells[i].paragraphs[0].paragraph_format.space_after = Pt(0)
            if i == 0:
                shade(cells[i], "EAF0FA")
    for row in t.rows:
        cs = OxmlElement("w:cantSplit")
        cs.set(qn("w:val"), "true")
        row._tr.get_or_add_trPr().append(cs)
        for i, w in enumerate(widths):
            row.cells[i].width = Cm(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


# ---------- contenuto ----------
doc.add_heading("A2 Stakeholder e contesto", level=1)
para("Attività **S1-01** dello **Sprint 1 – Preparazione PICUS**. Versione aggiornata dopo il primo confronto con lo "
     "stakeholder, che sostituisce la prima stesura basata solo sui desiderata. Come ogni artefatto di una "
     "iterazione Scrum, A2 è un incremento: si aggiorna a ogni confronto e il dettaglio si approfondisce nelle user "
     "story quando serve, non in anticipo.")
para("**Obiettivo dello sprint per S1-01:** capire il contesto operativo, individuare gli stakeholder e fissare i "
     "confini del sistema, così che il processo as-is e to-be (S1-02, S1-03) possa partire da basi condivise.")

doc.add_heading("Contesto", level=2)
bullet("PICUS sostiene un programma di aiuti che comprende, oltre alla distribuzione di beni, misure di "
       "accompagnamento. Il Banco gestisce il centro operativo regionale ed è **capofila verso il ministero**. "
       "[F02 §2; F06]")
bullet("Le dimensioni emerse nel confronto sono **400–450 OPT**, **200 comuni** e circa **230.000 utenti** "
       "(le persone assistite). I desiderata parlavano di circa 200 OPT: **il numero più alto è quello dello "
       "stakeholder**, da riconfermare. [F06; F02 §2]")
bullet("Il flusso centrale è **OPT 1 → Banco → OPT 2** (o un altro erogatore): il Banco intermedia e **monitora le "
       "transazioni**. L'OPT si rivolge al Banco quando non riesce a soddisfare da sola i bisogni dei propri "
       "assistiti. [F06]")
bullet("Oggi tutto passa da telefono, messaggi, documenti e schede separate, senza strumenti integrati. [F02 §4]")
para("**Da preservare:** tutela dei dati, separazione dei ruoli, nessun dato identificativo delle persone assistite e "
     "ruolo di coordinamento del Banco. [F02 §1]")

doc.add_heading("Stakeholder", level=2)
tabella(
    ["Stakeholder", "Cosa fa e cosa vuole", "Usa l'app?"],
    [
        ["Banco", "Coordina le richieste e trova l'erogatore, monitora le transazioni, gestisce cataloghi e account "
                  "delle OPT (anche con caricamento massivo), invia comunicazioni con conferma di ricezione, "
                  "raccoglie i dati per la rendicontazione al ministero.", "Sì, con visione complessiva"],
        ["OPT", "Chiede una misura per le persone che assiste quando non riesce a soddisfarle da sola, e dichiara le "
                "misure che offre agli altri. Un solo accesso per OPT (una email).", "Sì, solo i propri dati"],
        ["Operatori", "Interni al Centro PICUS o professionisti esterni: erogano le misure, confermano gli "
                      "appuntamenti e compilano la scheda trimestrale.", "Sì, accesso personale (ipotesi)"],
        ["Persone assistite", "Ricevono la misura tramite l'OPT. Nessun accesso e nessun dato identificativo "
                              "registrato.", "No"],
        ["Ministero e responsabile privacy", "Il ministero riceve la rendicontazione; il responsabile privacy "
                                              "definisce la conservazione dei dati. Interlocutori dell'analisi, non "
                                              "ruoli applicativi.", "No"],
    ],
    widths=[3.4, 10.6, 3.0],
)
para("**Gli operatori e i volontari delle singole OPT non sono utenti.** La gestione interna di ogni OPT non riguarda "
     "PICUS: contano solo i servizi che offre e i dati quantitativi, e il Banco non comunica direttamente con loro "
     "né chiede la scheda trimestrale. [F06]", size=10)

doc.add_heading("Cosa abbiamo capito dal confronto con lo stakeholder", level=2)
para("Stato: **Fonte** (appunti dell'incontro, F06). Per ogni punto, l'effetto su stakeholder e confini.", size=9.5)
bullet("**Una sola email per OPT, confermato:** un account per OPT. Chiude per l'MVP l'ipotesi sugli account (Q-01).")
bullet("**Gli operatori delle OPT non hanno accesso** e il Banco non li contatta: restano utenti solo gli operatori "
       "interni e i professionisti esterni (Q-09 in gran parte risolta).")
bullet("**Niente messaggi broadcast:** le notizie importanti arrivano alle OPT con **conferma di ricezione**, e "
       "possono essere inviate solo a un **sottogruppo** di OPT (Q-08 in parte risolta).")
bullet("**Le richieste non sono prioritizzate:** si lavorano **in ordine di arrivo**.")
bullet("**Registrazione senza documenti.** Le credenziali si possono caricare **in massa ogni anno da un file CSV** "
       "(funzione opzionale), **non scadono**, e il Banco rimuove a mano le OPT scadute.")
bullet("**Confine:** quello che accade dentro l'OPT non interessa; il sistema tratta solo i servizi offerti, le "
       "richieste e la scheda trimestrale.")

doc.add_heading("Confini e Context Diagram", level=2)
para("Il diagramma mostra PICUS come un'unica scatola, con gli attori applicativi (Banco, OPT, Operatore) e le "
     "informazioni che scambiano con il sistema. **Dentro PICUS:** account, catalogo, richieste, appuntamenti, "
     "comunicazioni, scheda trimestrale. **Fuori:** la gestione interna delle OPT, il contatto tra OPT e persona "
     "assistita, l'inserimento manuale nel portale ministeriale.")
para("Il diagramma, in una pagina orizzontale per essere leggibile, è nella pagina seguente.", size=9.5, italic=True)
sezione(True)
doc.add_picture(PNG, width=Cm(26.5))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
para("Figura A2.1 — Context Diagram CTX-01 (versione del gruppo).", size=9, italic=True)
sezione(False)
para("**Osservazioni da discutere nel team** (proposte, non ancora decisioni):", after=2)
numerato(1, "**Soggetti esterni.** Persone assistite e portale ministeriale non compaiono: se si vuole mostrare il confine "
         "completo, aggiungerli come soggetti esterni con un collegamento tratteggiato (contatto OPT-assistito e "
         "inserimento manuale nel portale). [F02 §5.5]")
numerato(2, "**Scheda trimestrale.** Il diagramma la lega all'Operatore, mentre l'OPT «inserisce dati quantitativi "
         "aggregati». Da chiarire se sono la stessa scheda o due dati diversi, perché F06 dice che gli operatori delle "
         "OPT non la compilano.")
numerato(3, "**Etichette.** Alcune sono molto lunghe: per la review conviene accorciarle e tenere i dettagli nelle user "
         "story.")

doc.add_heading("Ipotesi e domande ancora aperte", level=2)
para("**Ipotesi** (da verificare): il Banco è un unico ruolo con visione complessiva; la videochiamata avviene su "
     "una piattaforma esterna e PICUS tratta solo il collegamento; gli operatori hanno un accesso personale limitato "
     "alla propria scheda e agli appuntamenti.")
para("**Domande per il prossimo confronto**, in ordine di priorità:", after=2)
numerato(1, "Quali **informazioni minime** servono per una richiesta senza identificare la persona? (Q-02, con 3–5 "
         "richieste reali anonime)")
numerato(2, "Con quali **criteri** si sceglie l'erogatore: competenza, territorio, disponibilità, e in che ordine? (Q-03)")
numerato(3, "Quali **stati** ha una richiesta e che casi limite esistono: rifiuto, nessun erogatore, riassegnazione? "
         "Cosa si intende per «monitorare le transazioni»? (Q-04)")
numerato(4, "Per quanto tempo si **conservano** i dati e cosa succede a quelli di una OPT rimossa? (Q-05)")
numerato(5, "Che **regole** ha la scheda trimestrale e che formato serve per il portale? Chi la compila per le attività "
         "svolte dalle OPT? (Q-06)")
numerato(6, "Quante **richieste al mese** e quali **picchi** ci sono, ora che le OPT sono 400–450? (Q-07)")
para("L'elenco completo con ipotesi è in A6.", size=9.5, italic=True)

doc.add_heading("Stato dell'attività (Definition of Done di S1-01)", level=2)
casella(True, "Gli stakeholder principali sono descritti con obiettivi e responsabilità.")
casella(True, "Il diagramma distingue il sistema dai soggetti esterni (da completare con le osservazioni sopra).")
casella(True, "Le persone assistite sono stakeholder, senza accesso all'applicazione.")
casella(True, "Sono preservati il coordinamento del Banco e il ruolo dell'OPT nei contatti con gli assistiti.")
casella(True, "Sono esplicitati i vincoli sui dati identificativi degli assistiti.")
casella(True, "Ipotesi e dubbi sono distinti dalle informazioni presenti nelle fonti.")
casella(False, "Analisi e diagramma sono stati revisionati da un altro membro. **Da fare** (revisore e data da "
               "registrare).")
para("**Prossimi passi nello sprint:** riconfermare i numeri con lo stakeholder, aggiornare CTX-01 con le osservazioni "
     "di sopra, usare le risposte per S1-02 (as-is), S1-04 (Epic) e S1-05 (backlog), e portare le domande aperte alla "
     "Sprint Review del 05/11.")

doc.add_heading("Fonti", level=2)
para("F01 — 00-Presentazione Progetto Picus.pdf, slide 18 e 27.\n"
     "F02 — 01-PICUS_richieste_informali_del_committente (1).pdf, §§1–5 e 7–8.\n"
     "F03 — AGENTS.md, §§8–9.\n"
     "F06 — BA.pdf, appunti del confronto con lo stakeholder (Banco Alimentare). **Da registrare in D2.**", size=9.5)

doc.save(OUT)
print("salvato", OUT)
