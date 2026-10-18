"""Genera il file Word del capitolo A2 «Stakeholder e contesto» (issue S1-01).

Uso:  py -3.11 genera_docx_a2.py <png-context-diagram> <file-docx-di-output>
Richiede python-docx.  Contenuto allineato a wiki/progetto/a2-stakeholder-e-contesto.md.
Etichette di stato come nel documento del gruppo: Fonte, Proposta, Ipotesi, Da compilare o verificare.
"""
import sys

from docx import Document
from docx.enum.section import WD_ORIENT
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
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    st.element.rPr.rFonts.set(qn("w:ascii"), "Calibri")
    st.element.rPr.rFonts.set(qn("w:hAnsi"), "Calibri")
    st.font.size = Pt(size)
    st.font.bold = True
    st.font.color.rgb = RGBColor.from_string(color)
    st.paragraph_format.space_before = Pt(14 if name != "Heading 3" else 10)
    st.paragraph_format.space_after = Pt(6)
    st.paragraph_format.keep_with_next = True

# intestazione e piè di pagina (come nel documento del gruppo)
hp = sec.header.paragraphs[0]
hp.text = "Elaborato di Software Architecture Design\nPinguini alla Fragola"
for r in hp.runs:
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(0x59, 0x59, 0x59)


def add_page_number(paragraph):
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


add_page_number(sec.footer.paragraphs[0])


# ---------- utilità ----------
def runs(par, s, size=None, color=None):
    """Aggiunge testo con **grassetto** e _corsivo_ minimale."""
    import re
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


def para(s, size=None, italic=False, color=None, after=None):
    p = doc.add_paragraph()
    runs(p, s, size, color)
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
    return p


def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hexcolor)
    tcPr.append(shd)


def table(header, rows, widths, size=8.5, first_bold=True):
    t = doc.add_table(rows=1, cols=len(header))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    for i, h in enumerate(header):
        c = t.rows[0].cells[i]
        c.text = ""
        runs(c.paragraphs[0], f"**{h}**", size, "FFFFFF")
        shade(c, "2F5496")
    # intestazione ripetuta su ogni pagina
    trPr = t.rows[0]._tr.get_or_add_trPr()
    th = OxmlElement("w:tblHeader")
    th.set(qn("w:val"), "true")
    trPr.append(th)
    for row in rows:
        cells = t.add_row().cells
        for i, val in enumerate(row):
            cells[i].text = ""
            txt = f"**{val}**" if (i == 0 and first_bold and not val.startswith("**")) else val
            runs(cells[i].paragraphs[0], txt, size)
            cells[i].paragraphs[0].paragraph_format.space_after = Pt(0)
            if i == 0:
                shade(cells[i], "EAF0FA")
    for row in t.rows:
        # evita che una riga si spezzi tra due pagine
        trPr = row._tr.get_or_add_trPr()
        cs = OxmlElement("w:cantSplit")
        cs.set(qn("w:val"), "true")
        trPr.append(cs)
        for i, w in enumerate(widths):
            row.cells[i].width = Cm(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t


def kv_table(rows, widths=(3.6, 13.4), size=9):
    t = doc.add_table(rows=0, cols=2)
    t.style = "Table Grid"
    t.autofit = False
    for k, v in rows:
        cells = t.add_row().cells
        cells[0].text = ""
        cells[1].text = ""
        runs(cells[0].paragraphs[0], f"**{k}**", size)
        shade(cells[0], "EAF0FA")
        runs(cells[1].paragraphs[0], v, size)
        for c in cells:
            c.paragraphs[0].paragraph_format.space_after = Pt(0)
        for i, w in enumerate(widths):
            cells[i].width = Cm(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


# ---------- contenuto ----------
doc.add_heading("A2 Stakeholder e contesto", level=1)
para("Attività collegata **S1-01** (issue «Stakeholder e Context Diagram»). Obiettivo: comprendere il contesto "
     "operativo di PICUS, identificare gli stakeholder e rappresentare i confini del sistema. "
     "Fonti: F01 (presentazione PICUS, attività 1, slide 18) e F02 (desiderata del committente, sezioni 2 e 3, "
     "con 5–8). Le sezioni contrassegnate **Ipotesi** o **Proposta** non sono conferme del committente.")

# --- contesto ---
doc.add_heading("Contesto operativo", level=2)
bullet("PICUS sostiene un programma di aiuti che comprende, oltre alla distribuzione di beni, misure di "
       "accompagnamento. [F02, §2]")
bullet("Il Banco gestisce il centro operativo regionale e coordina circa 200 OPT in circa 200 comuni. [F02, §2]")
bullet("Le misure sono erogate da operatori interni al Centro PICUS, da professionisti esterni sul territorio o da "
       "OPT con propri operatori o volontari. [F02, §2]")
bullet("Il Banco riceve le richieste delle OPT, individua un erogatore, ne verifica la disponibilità e coordina "
       "l'appuntamento; i contatti con la persona o il nucleo assistito restano all'OPT richiedente. [F02, §2]")
bullet("Oggi il processo si svolge con telefono, messaggi, documenti e schede separate, senza strumenti "
       "integrati. [F02, §4]")
para("**Vincoli da preservare:** tutela dei dati; separazione dei ruoli; assenza di dati identificativi delle "
     "persone assistite; ruolo di coordinamento del Banco. [F02, §1]")

# --- stakeholder principali ---
doc.add_heading("Stakeholder principali", level=2)
para("Stato: **Fonte**, salvo dove indicato. Ogni riga riporta obiettivi, responsabilità e informazioni usate o "
     "prodotte.", size=9.5)
table(
    ["ID", "Stakeholder", "Obiettivi", "Responsabilità", "Informazioni usate o prodotte", "Fonte"],
    [
        ["SH-01", "Banco",
         "Coordinare richieste, erogatori e appuntamenti; avere una visione aggiornata; rendicontare.",
         "Riceve le richieste; individua e contatta gli erogatori; verifica la disponibilità; organizza gli "
         "appuntamenti; crea e revoca gli account delle OPT; gestisce account e cataloghi; invia comunicazioni; "
         "inserisce i dati nel portale ministeriale.",
         "Usa: richieste, anagrafica OPT, catalogo, misure svolte, disponibilità, appuntamenti, schede "
         "trimestrali. Produce: assegnazioni, appuntamenti, comunicazioni. Visione complessiva.",
         "F02 §§2, 3, 5.1–5.5"],
        ["SH-02", "OPT richiedente",
         "Ottenere una misura di accompagnamento per una persona o un nucleo.",
         "Invia la richiesta; mantiene i contatti con l'assistito e gli comunica le informazioni ricevute dal Banco.",
         "Produce: richieste (misura, persona o nucleo, senza dati identificativi). Usa: stato e dettagli "
         "dell'appuntamento, comunicazioni. Vede solo le proprie informazioni e richieste; accesso soprattutto da "
         "smartphone.",
         "F02 §§2, 3, 5.3, 7"],
        ["SH-03", "OPT erogatrice",
         "Rendersi disponibile a erogare le misure che svolge effettivamente.",
         "Dichiara le misure svolte; verifica e comunica la propria disponibilità; se scelta, eroga con propri "
         "operatori o volontari; registra dati quantitativi senza dati personali.",
         "Produce: misure svolte, disponibilità, dati quantitativi. Usa: richieste di altre OPT inoltrate dal Banco.",
         "F02 §§3, 5.2, 5.3"],
        ["SH-04", "Operatore",
         "Erogare le misure e adempiere agli obblighi di monitoraggio.",
         "Eroga le attività (anche più misure); conferma gli appuntamenti; compila e invia al Banco una scheda per "
         "trimestre.",
         "Produce: conferma o rifiuto dell'appuntamento; scheda trimestrale (dati personali e amministrativi propri "
         "e conteggi aggregati). Usa: appuntamenti assegnati. Accesso personale ipotizzato dalla fonte, limitato "
         "alla propria scheda e alle informazioni necessarie.",
         "F02 §§3, 5.3, 5.5, 6, app. B"],
        ["SH-05", "Persona o nucleo assistito",
         "Ricevere la misura di cui ha bisogno.",
         "Nessuna verso il sistema: è il destinatario finale; il contatto passa sempre dall'OPT.",
         "Non produce né usa informazioni in PICUS; dei destinatari esistono solo conteggi aggregati.",
         "F02 §§1, 3, 5.2, 6"],
    ],
    widths=[1.1, 2.0, 3.0, 4.3, 4.6, 2.0], size=8,
)

doc.add_heading("Altri stakeholder e interlocutori dell'analisi", level=3)
table(
    ["ID", "Stakeholder", "Perché conta", "Stato", "Fonte"],
    [
        ["SH-06", "Committente",
         "Origine dei desiderata; ogni requisito nuovo o riformulato va discusso con lui prima di entrare nella "
         "baseline.", "Fonte", "F02 §§1, 9"],
        ["SH-07", "Responsabile privacy",
         "Con lui vanno definiti tempi e regole di conservazione dei dati. Interlocutore dell'analisi, non un "
         "ruolo applicativo già definito.", "Fonte", "F02 §§5.1, 7"],
        ["SH-08", "Ente destinatario della rendicontazione (titolare del portale ministeriale)",
         "Riceve i dati trimestrali inseriti dal Banco; ha interesse alla coerenza e completezza della scheda.",
         "Ipotesi (dedotta dalla presenza del portale; la fonte non nomina l'ente)", "F02 §5.5"],
    ],
    widths=[1.1, 3.6, 6.8, 3.4, 2.1], size=8.5,
)
para("Nota: F02 nomina un referente esplicito solo per la privacy (§7). I riferimenti agli obblighi di "
     "rendicontazione (§§5.1, 5.5) non indicano chi siano i referenti: la questione è registrata come Q-11.",
     size=9, italic=True)

doc.add_heading("Un soggetto, più ruoli", level=3)
para("**Ipotesi (IP-02).** OPT richiedente e OPT erogatrice sono due funzioni della stessa organizzazione, non due "
     "organizzazioni: F02 §3 prevede che l'OPT possa «inviare richieste o rendersi disponibile come erogatrice». "
     "Sono su righe separate perché obiettivi, informazioni e rischi sono diversi. Se il modello degli account "
     "resterà «un account per OPT» [F02, §5.1], corrisponderanno a funzioni di quell'account.", size=10)
table(
    ["Tipo di erogatore", "Chi è", "Interagisce con PICUS?", "Domanda aperta"],
    [
        ["Operatore interno al Centro PICUS", "Dipendente del Banco", "Sì, come SH-04", "—"],
        ["Professionista esterno", "Professionista sul territorio", "Probabilmente come SH-04",
         "Quale accesso ha? (Q-09)"],
        ["OPT erogatrice", "L'organizzazione, con propri operatori o volontari",
         "Come SH-03; per i suoi operatori da chiarire", "Operatori e volontari dell'OPT hanno account personale? (Q-09)"],
    ],
    widths=[3.8, 4.4, 4.2, 4.6], size=8.5,
)
para("Fonte: F02 §§2, 3, 6.", size=9, italic=True)

# --- stakeholder / utenti / sistemi esterni ---
doc.add_heading("Stakeholder, utenti applicativi e sistemi esterni", level=2)
table(
    ["Soggetto", "Stakeholder", "Utente applicativo", "Sistema esterno", "Motivo"],
    [
        ["Banco", "Sì", "Sì (visibilità complessiva)", "No", "Usa PICUS per coordinare. [F02, §3]"],
        ["OPT (richiedente ed erogatrice)", "Sì", "Sì, solo i propri dati", "No",
         "Accede da smartphone e invia richieste. [F02, §3]"],
        ["Operatore", "Sì", "Sì (ipotesi della fonte), accesso personale limitato", "No",
         "Conferma appuntamenti e compila la scheda. [F02, §3]"],
        ["Persona o nucleo assistito", "Sì", "No", "No", "Non è utente; nessun dato identificativo. [F02, §3]"],
        ["Committente", "Sì", "No", "No", "Interlocutore dell'analisi. [F02, §§1, 9]"],
        ["Responsabile privacy", "Sì", "No", "No", "Interlocutore dell'analisi. [F02, §7]"],
        ["Ente destinatario della rendicontazione", "Sì", "No", "No", "Riceve i dati dal portale (ipotesi)."],
        ["Portale ministeriale", "—", "No", "Sì",
         "Destinazione della rendicontazione; inserimento manuale del Banco, integrazione diretta non richiesta. "
         "[F02, §5.5]"],
    ],
    widths=[3.6, 1.8, 3.4, 1.8, 6.4], size=8.5,
)
para("Ogni utente è uno stakeholder, ma non vale il contrario. Il confine del sistema si traccia sugli utenti "
     "applicativi e sui sistemi esterni; gli altri stakeholder influenzano i requisiti senza essere attori "
     "dell'applicazione. [F03, §9: «distinguere stakeholder reali da utenti dell'applicazione»]", size=10)

# --- confini ---
doc.add_heading("Confini del sistema", level=2)
table(
    ["Dentro PICUS (da progettare e costruire)", "Fuori da PICUS"],
    [
        ["Gestione di account, ruoli e autorizzazioni",
         "Contatto tra OPT e persona assistita (telefono, di persona)"],
        ["Catalogo delle misure, configurabile dal Banco",
         "Portale ministeriale e inserimento manuale del Banco"],
        ["Dichiarazione delle misure svolte e dati quantitativi aggregati",
         "Dati identificativi degli assistiti (non entrano mai in PICUS)"],
        ["Richieste, ricerca dell'erogatore, appuntamenti e relativi stati",
         "Erogazione concreta della misura (colloquio, visita, lezione)"],
        ["Comunicazioni dal Banco alle OPT, con allegati",
         "Eventuali piattaforme di videochiamata di terzi (ipotesi IP-03)"],
        ["Scheda trimestrale dell'operatore",
         "Processo di conservazione dei dati definito con il responsabile privacy"],
    ],
    widths=[8.5, 8.5], size=9, first_bold=False,
)
para("Vincoli espliciti che fissano il confine: assistiti senza account né dati identificativi [F02, §§1, 3]; "
     "scheda trimestrale distinta dal flusso delle richieste [F02, §5.5]; integrazione ministeriale non "
     "richiesta [F02, §5.5]; audit completo e biometria non richiesti [F02, §§5.1, 7; F03, §8].", size=10)

# --- interazioni ---
doc.add_heading("Interazioni previste", level=2)
doc.add_heading("Flussi applicativi (attraversano il confine)", level=3)
table(
    ["ID", "Da → A", "Informazione", "Fonte"],
    [
        ["IF-01", "OPT richiedente → PICUS",
         "Richiesta di una misura del catalogo, per persona o nucleo, senza dati identificativi.", "F02 §5.3"],
        ["IF-02", "OPT erogatrice → PICUS",
         "Misure effettivamente svolte e dati quantitativi (senza dati personali).", "F02 §5.2"],
        ["IF-03", "OPT erogatrice → PICUS", "Disponibilità a erogare, in risposta alla verifica del Banco.", "F02 §5.3"],
        ["IF-04", "PICUS → OPT richiedente",
         "Stato della richiesta e dettagli dell'appuntamento: in presenza data, luogo, orario e referente; a "
         "distanza data, orario e collegamento alla videochiamata.", "F02 §5.3"],
        ["IF-05", "Banco → PICUS",
         "Gestione degli account (creazione e revoca per le OPT, accessi degli operatori) e del catalogo.",
         "F02 §§5.1, 5.2"],
        ["IF-06", "Banco → PICUS",
         "Individuazione e contatto degli erogatori, verifica di disponibilità, organizzazione dell'appuntamento; "
         "emissione di comunicazioni.", "F02 §§3, 5.3, 5.4"],
        ["IF-07", "PICUS → Banco",
         "Vista complessiva di richieste, disponibilità, stato degli appuntamenti, schede trimestrali ricevute, "
         "dati di monitoraggio per la rendicontazione.", "F02 §§3, 4, 5.5"],
        ["IF-08", "PICUS → OPT",
         "Comunicazioni del Banco (convocazioni, avvisi, promemoria di scadenza), anche con allegati.", "F02 §5.4"],
        ["IF-09", "PICUS → Operatore",
         "Appuntamento da confermare assegnato dal Banco. Ipotesi: implicito, F02 dice solo che l'operatore "
         "«dovrebbe poter confermare».", "F02 §5.3"],
        ["IF-10", "Operatore → PICUS", "Conferma o rifiuto dell'appuntamento.", "F02 §5.3"],
        ["IF-11", "Operatore → PICUS",
         "Scheda trimestrale: dati personali e amministrativi dell'operatore e conteggi aggregati (app. B).",
         "F02 §5.5, app. B"],
    ],
    widths=[1.3, 3.7, 9.6, 2.4], size=8.5,
)
doc.add_heading("Flussi fuori dal sistema (non applicativi)", level=3)
table(
    ["ID", "Da → A", "Informazione", "Perché è fuori", "Fonte"],
    [
        ["IF-12", "OPT ↔ persona o nucleo assistito", "Informazioni sull'appuntamento, contatto, bisogno.",
         "Il contatto con l'assistito resta all'OPT; PICUS non registra dati identificativi.", "F02 §§2, 5.3"],
        ["IF-13", "Banco → portale ministeriale", "Dati di rendicontazione (dalle schede trimestrali).",
         "Inserimento manuale; nessuna integrazione diretta richiesta.", "F02 §5.5"],
        ["IF-14", "Operatore → persona assistita", "Erogazione della misura, in presenza o a distanza.",
         "L'erogazione è il fine del processo, non una funzione di PICUS.", "F02 §§2, 5.3"],
    ],
    widths=[1.3, 3.5, 4.4, 5.7, 2.1], size=8.5,
)

# --- Context diagram ---
doc.add_heading("Context Diagram CTX-01", level=2)
para("Il diagramma rappresenta il confine di PICUS e gli scambi informativi di Banco, OPT e operatori. Le persone "
     "assistite sono soggetti esterni al sistema, con contatto mediato dalla OPT. Il passaggio manuale al "
     "portale ministeriale è tracciato come flusso non applicativo (linea tratteggiata).")
doc.add_picture(PNG, width=Cm(17))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
para("Figura A2.1 — Context Diagram CTX-01. Linee continue: interazioni applicative IF-01…IF-11. Linee tratteggiate: "
     "contatti o passaggi fuori dal sistema IF-12…IF-14.", size=9, italic=True)
kv_table([
    ("Artefatto", "Diagramma di contesto; gli ID IF-xx corrispondono alle tabelle «Interazioni previste»."),
    ("Stato", "**Proposta**: prima stesura. Da ridisegnare in Visual Paradigm."),
    ("Versione, data, file", "**Da compilare o verificare**: versione, data e percorso del file Visual Paradigm "
                             "o dell'esportazione leggibile."),
    ("Autore del contributo", "**Da compilare o verificare**."),
    ("Revisione", "**Da compilare o verificare**: revisore, data, punti verificati e questioni collegate."),
])

# --- ipotesi e domande ---
doc.add_heading("Ipotesi e domande aperte", level=2)
doc.add_heading("Ipotesi", level=3)
table(
    ["ID", "Assunzione", "Base nella fonte", "Riesame", "Impatto se errata"],
    [
        ["IP-01", "Il Banco è un unico ruolo applicativo con visione complessiva.",
         "F02 §3 non distingue sotto-ruoli.", "Alla definizione delle storie di amministrazione.",
         "Servono ruoli distinti (es. chi amministra il catalogo e chi coordina): cambiano account e autorizzazioni."],
        ["IP-02", "OPT richiedente e OPT erogatrice sono funzioni della stessa organizzazione, con lo stesso account.",
         "F02 §3; F02 §5.1 «prima ipotesi: un account per OPT».", "Alla risposta di Q-01.",
         "Account separati o più utenti per OPT: cambia il modello di sicurezza."],
        ["IP-03", "La videochiamata si svolge su una piattaforma esterna; PICUS memorizza e comunica solo il "
                  "collegamento.", "F02 §5.3: per il servizio a distanza servono data, orario e collegamento.",
         "Alla risposta di Q-10.",
         "Se PICUS generasse il collegamento comparirebbe un sistema esterno nel CTX-01."],
        ["IP-04", "Le notifiche (email, push) non sono nel baseline del CTX-01: restano proposte da valutare.",
         "F02 §§5.4, 8.", "Alla valutazione della proposta di notifiche (Q-08).",
         "Compare un sistema esterno di notifica."],
        ["IP-05", "L'operatore ha un accesso personale, limitato alla propria scheda e agli appuntamenti assegnati.",
         "F02 §3: «il committente immagina».", "Alla risposta di Q-01 e Q-09.",
         "Un operatore di OPT potrebbe agire tramite l'account dell'OPT."],
    ],
    widths=[1.2, 4.6, 3.6, 3.2, 4.4], size=8,
)
doc.add_heading("Domande aperte", level=3)
para("Q-01, Q-05 e Q-08 sono già nell'elenco candidato di A6; Q-09, Q-10 e Q-11 sono nuove e vanno aggiunte ad A6.",
     size=9.5)
table(
    ["ID", "Domanda", "Perché serve e fonte", "Ipotesi provvisoria"],
    [
        ["Q-01", "Per una OPT basta un account condiviso o servono utenti nominativi?",
         "Responsabilità e continuità quando cambia il referente. F02 §§5.1, 8.", "IP-02"],
        ["Q-05", "Quali regole per recupero credenziali, revoca e dati dopo la cessazione di una OPT?",
         "Accessi e conservazione, da chiarire con il responsabile privacy (SH-07). F02 §§5.1, 7.",
         "Nessuna policy inventata"],
        ["Q-08", "Quali notifiche o riepiloghi riducono davvero i solleciti manuali?",
         "Evitare di ampliare il perimetro per implicito. F02 §§5.4, 8.", "IP-04"],
        ["Q-09", "Professionisti esterni e operatori o volontari delle OPT hanno un account personale o agiscono "
                 "tramite altri?",
         "Definisce gli utenti reali e il perimetro degli erogatori. F02 §§3, 5.1.", "IP-05"],
        ["Q-10", "Per le prestazioni a distanza, chi fornisce il collegamento alla videochiamata?",
         "Decide se esiste un sistema esterno aggiuntivo. F02 §5.3.", "IP-03"],
        ["Q-11", "Chi è il referente di rendicontazione da coinvolgere per validare la scheda trimestrale e gli esiti "
                 "verso il portale? E chi è il «referente» di un incontro in presenza?",
         "F02 nomina un «referente» (§5.3) e obblighi di rendicontazione (§§5.1, 5.5) senza dire chi sono.",
         "Nessuna"],
    ],
    widths=[1.3, 5.9, 6.5, 3.3], size=8.5,
)
para("Non riaprire come dubbi i vincoli espliciti: assistiti senza account né identificativi; scheda trimestrale "
     "distinta dalle richieste; integrazione ministeriale non richiesta. [F02, §§1, 3, 5.5]", size=9.5, italic=True)

# --- controllo ---
doc.add_heading("Controllo dei criteri di completamento (S1-01)", level=2)
table(
    ["Criterio dell'issue", "Esito", "Dove"],
    [
        ["Gli stakeholder principali sono descritti con obiettivi e responsabilità.", "Soddisfatto nel testo",
         "Stakeholder principali"],
        ["Il diagramma distingue chiaramente sistema e soggetti esterni.", "Soddisfatto nel testo",
         "Confini; CTX-01"],
        ["Le persone assistite sono rappresentate come stakeholder, senza prevedere un loro accesso "
         "all'applicazione.", "Soddisfatto nel testo", "SH-05; tabella stakeholder/utenti"],
        ["Sono preservati il coordinamento del Banco e il ruolo dell'OPT nei contatti con le persone assistite.",
         "Soddisfatto nel testo", "SH-01; IF-12"],
        ["Sono esplicitati i vincoli sui dati identificativi degli assistiti.", "Soddisfatto nel testo",
         "Vincoli; IF-01; IF-12"],
        ["Ipotesi e dubbi sono distinti dalle informazioni presenti nelle fonti.", "Soddisfatto nel testo",
         "IP-01…05; Q-01…11"],
        ["Analisi e diagramma sono stati revisionati da un altro membro.", "**Da compilare o verificare**",
         "Registrare revisore, data e punti verificati"],
    ],
    widths=[9.5, 3.5, 4.0], size=8.5, first_bold=False,
)
para("«Soddisfatto nel testo» indica che il contenuto di questa sezione risponde al criterio. Prima di spuntare le "
     "caselle dell'issue vanno completati il Context Diagram in Visual Paradigm e la revisione di un altro membro.",
     size=9, italic=True)

doc.add_heading("Fonti", level=2)
para("F01 — 00-Presentazione Progetto Picus.pdf, slide 18 (attività 1) e slide 27 (deliverable).\n"
     "F02 — 01-PICUS_richieste_informali_del_committente (1).pdf, §§1–3, 5–9 e appendice B.\n"
     "F03 — AGENTS.md, §§8–9 (regole di dominio; distinzione fra stakeholder e utenti).", size=9.5)

doc.save(OUT)
print("salvato", OUT)
