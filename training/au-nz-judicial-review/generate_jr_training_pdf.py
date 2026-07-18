#!/usr/bin/env python3
"""Generate AU/NZ Judicial Review Training Manual PDF for Pakistan team."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm, mm
from reportlab.platypus import (
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

OUT = Path(__file__).parent / "AU-NZ-Judicial-Review-Training-Manual.pdf"

NAVY = colors.HexColor("#0D1B2A")
GOLD = colors.HexColor("#8B7355")
LIGHT = colors.HexColor("#F5F3EF")
SOFT = colors.HexColor("#E8E4DC")
RED = colors.HexColor("#8B1E1E")


def styles():
    base = getSampleStyleSheet()
    s = {
        "cover_title": ParagraphStyle(
            "cover_title", parent=base["Title"], fontName="Helvetica-Bold",
            fontSize=22, leading=28, textColor=NAVY, alignment=TA_CENTER, spaceAfter=12,
        ),
        "cover_sub": ParagraphStyle(
            "cover_sub", parent=base["Normal"], fontName="Helvetica",
            fontSize=12, leading=16, textColor=GOLD, alignment=TA_CENTER, spaceAfter=8,
        ),
        "h1": ParagraphStyle(
            "h1", parent=base["Heading1"], fontName="Helvetica-Bold",
            fontSize=14, leading=18, textColor=NAVY, spaceBefore=16, spaceAfter=8,
            borderPadding=4,
        ),
        "h2": ParagraphStyle(
            "h2", parent=base["Heading2"], fontName="Helvetica-Bold",
            fontSize=12, leading=15, textColor=NAVY, spaceBefore=12, spaceAfter=6,
        ),
        "h3": ParagraphStyle(
            "h3", parent=base["Heading3"], fontName="Helvetica-Bold",
            fontSize=10.5, leading=13, textColor=GOLD, spaceBefore=8, spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "body", parent=base["Normal"], fontName="Helvetica",
            fontSize=9.5, leading=13, alignment=TA_JUSTIFY, spaceAfter=6, textColor=colors.black,
        ),
        "bullet": ParagraphStyle(
            "bullet", parent=base["Normal"], fontName="Helvetica",
            fontSize=9.5, leading=12.5, leftIndent=12, spaceAfter=3,
        ),
        "note": ParagraphStyle(
            "note", parent=base["Normal"], fontName="Helvetica-Oblique",
            fontSize=8.5, leading=11, textColor=RED, spaceBefore=4, spaceAfter=8,
            backColor=LIGHT, borderPadding=6,
        ),
        "template_title": ParagraphStyle(
            "template_title", parent=base["Normal"], fontName="Helvetica-Bold",
            fontSize=9, leading=11, textColor=NAVY, spaceBefore=6, spaceAfter=4,
        ),
        "mono": ParagraphStyle(
            "mono", parent=base["Code"], fontName="Courier",
            fontSize=7.5, leading=9.5, textColor=colors.black, backColor=SOFT,
            leftIndent=4, rightIndent=4, spaceBefore=4, spaceAfter=8, borderPadding=6,
        ),
        "toc": ParagraphStyle(
            "toc", parent=base["Normal"], fontName="Helvetica",
            fontSize=10, leading=15, leftIndent=8, spaceAfter=2,
        ),
        "footer": ParagraphStyle(
            "footer", parent=base["Normal"], fontName="Helvetica",
            fontSize=7.5, textColor=colors.grey, alignment=TA_CENTER,
        ),
        "center": ParagraphStyle(
            "center", parent=base["Normal"], fontName="Helvetica",
            fontSize=9.5, leading=13, alignment=TA_CENTER, spaceAfter=6,
        ),
        "table_cell": ParagraphStyle(
            "table_cell", parent=base["Normal"], fontName="Helvetica",
            fontSize=8, leading=10,
        ),
        "table_head": ParagraphStyle(
            "table_head", parent=base["Normal"], fontName="Helvetica-Bold",
            fontSize=8, leading=10, textColor=colors.white,
        ),
    }
    return s


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(0.5)
    canvas.line(1.8 * cm, A4[1] - 1.2 * cm, A4[0] - 1.8 * cm, A4[1] - 1.2 * cm)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(colors.grey)
    canvas.drawString(1.8 * cm, A4[1] - 1.0 * cm, "AU / NZ Judicial Review Training Manual — Pakistan Team")
    canvas.drawRightString(A4[0] - 1.8 * cm, A4[1] - 1.0 * cm, "Confidential Training Material")
    canvas.line(1.8 * cm, 1.3 * cm, A4[0] - 1.8 * cm, 1.3 * cm)
    canvas.drawCentredString(A4[0] / 2, 0.9 * cm, f"Page {doc.page}  |  Self-represented focus  |  Educational use only — not legal advice")
    canvas.restoreState()


def bullets(items, style):
    return ListFlowable(
        [ListItem(Paragraph(i, style), leftIndent=8, value="•") for i in items],
        bulletType="bullet", start="•", leftIndent=10, bulletFontSize=9,
    )


def info_box(title, text, s):
    data = [[Paragraph(f"<b>{title}</b>", s["template_title"])],
            [Paragraph(text, s["body"])]]
    t = Table(data, colWidths=[16.5 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
        ("BOX", (0, 0), (-1, -1), 0.5, GOLD),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


def mono_block(text, s):
    return Preformatted(text.strip("\n"), s["mono"])


def make_table(headers, rows, s, col_widths=None):
    head = [Paragraph(h, s["table_head"]) for h in headers]
    body = [[Paragraph(c, s["table_cell"]) for c in row] for row in rows]
    t = Table([head] + body, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("BACKGROUND", (0, 1), (-1, -1), colors.white),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
        ("GRID", (0, 0), (-1, -1), 0.4, SOFT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


def build():
    s = styles()
    story = []

    # COVER
    story.append(Spacer(1, 2.5 * cm))
    story.append(Paragraph("JUDICIAL REVIEW TRAINING MANUAL", s["cover_title"]))
    story.append(Paragraph("Australia &amp; New Zealand — Visa Refusal Challenges", s["cover_sub"]))
    story.append(Paragraph("For Pakistan-based Case Team · Self-Represented Clients", s["cover_sub"]))
    story.append(Spacer(1, 0.6 * cm))
    story.append(Paragraph(
        "A to Z practical training: procedure, forms, drafting templates,<br/>"
        "jurisdictional error grounds, and a full worked scenario case.",
        s["center"],
    ))
    story.append(Spacer(1, 0.8 * cm))
    data = [
        [Paragraph("<b>Audience</b>", s["table_cell"]),
         Paragraph("Immigration case officers / junior lawyers / client support team (Pakistan)", s["table_cell"])],
        [Paragraph("<b>Objective</b>", s["table_cell"]),
         Paragraph("After this training, the team can prepare and guide a self-represented client through AU/NZ JR filing end-to-end.", s["table_cell"])],
        [Paragraph("<b>Client model</b>", s["table_cell"]),
         Paragraph("Client is <b>self-represented at all stages</b>. Team drafts / coaches; client signs and files in own name.", s["table_cell"])],
        [Paragraph("<b>Level</b>", s["table_cell"]),
         Paragraph("Practitioner-grade (15+ years litigation / migration judicial review experience)", s["table_cell"])],
        [Paragraph("<b>Version</b>", s["table_cell"]),
         Paragraph("1.0 · July 2026 · Training use only", s["table_cell"])],
    ]
    t = Table(data, colWidths=[3.5 * cm, 13 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
        ("BOX", (0, 0), (-1, -1), 1, NAVY),
        ("INNERGRID", (0, 0), (-1, -1), 0.3, SOFT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(t)
    story.append(Spacer(1, 1 * cm))
    story.append(Paragraph(
        "<b>CRITICAL DISCLAIMER:</b> This manual is educational training material for internal team capacity-building. "
        "It is <b>not legal advice</b> to any client. Laws, forms, fees, and court practice directions change. "
        "Always verify against the current FCFCOA / Federal Court of Australia / NZ High Court / Immigration and Protection Tribunal "
        "websites before filing. Where a matter is complex (character, national security, detention, removal urgency), "
        "urge the client to obtain admitted counsel in AU/NZ.",
        s["note"],
    ))
    story.append(PageBreak())

    # TOC
    story.append(Paragraph("1. TABLE OF CONTENTS", s["h1"]))
    toc = [
        "2. Training Outcomes &amp; How to Use This Manual",
        "3. The Golden Rule: Merits Review vs Judicial Review",
        "4. Decision Map — What Stage Is the Client At?",
        "5. AUSTRALIA — End-to-End Judicial Review",
        "   5.1 Pathway before court (Department → ART)",
        "   5.2 Court jurisdiction (FCFCOA Div 2 / Federal Court)",
        "   5.3 Time limits &amp; extension of time",
        "   5.4 Grounds — jurisdictional error catalogue",
        "   5.5 Documents to file &amp; serve",
        "   5.6 Step-by-step filing checklist (self-rep)",
        "   5.7 Hearing preparation &amp; after judgment",
        "6. NEW ZEALAND — End-to-End Judicial Review",
        "   6.1 Pathway before court (INZ → IPT)",
        "   6.2 ss 247 &amp; 249 Immigration Act 2009",
        "   6.3 Leave applications &amp; High Court JR",
        "   6.4 Step-by-step filing checklist (self-rep)",
        "7. SCENARIO CASE — Full Worked File (AU + NZ notes)",
        "8. COMPLETE DRAFTING TEMPLATES (fillable)",
        "9. FORMS DIRECTORY &amp; OFFICIAL LINKS",
        "10. Team SOPs, Ethics &amp; Quality Control",
        "11. Quick Reference Cards",
        "12. Training Assessment Checklist",
    ]
    for line in toc:
        story.append(Paragraph(line, s["toc"]))
    story.append(PageBreak())

    # 2 Outcomes
    story.append(Paragraph("2. TRAINING OUTCOMES &amp; HOW TO USE THIS MANUAL", s["h1"]))
    story.append(Paragraph(
        "By the end of this session, every team member must be able to:",
        s["body"],
    ))
    story.append(bullets([
        "Explain in plain English what judicial review can and cannot do for a refused visa applicant.",
        "Identify the correct forum, respondent, and deadline for an AU or NZ refusal from Pakistan.",
        "Spot arguable <b>jurisdictional errors</b> (not mere disagreement with the outcome).",
        "Draft the core court documents for a self-represented client (application, affidavit / statement of claim, chronology).",
        "Assemble the court book / evidence index and a service pack.",
        "Coach the client on filing, service, case management, and hearing etiquette as a self-represented litigant.",
        "Know when to stop and escalate (hopeless case / conflict / removal risk).",
    ], s["bullet"]))
    story.append(Paragraph(
        "<b>Team role vs client role:</b> The client is the litigant. The client signs affidavits, appears at hearing "
        "(or by video if permitted), and is responsible to the Court. The Pakistan team prepares drafts, evidence packs, "
        "and checklists; does <b>not</b> hold out as an Australian or New Zealand lawyer unless admitted and authorised.",
        s["note"],
    ))
    story.append(PageBreak())

    # 3 Golden Rule
    story.append(Paragraph("3. THE GOLDEN RULE: MERITS REVIEW VS JUDICIAL REVIEW", s["h1"]))
    story.append(make_table(
        ["Question", "Merits Review (ART / IPT)", "Judicial Review (Court)"],
        [
            ["What is asked?", "Was the decision the <b>correct or preferable</b> one on the facts?", "Was the decision made <b>lawfully</b>?"],
            ["Can court/tribunal grant the visa?", "Tribunal may remake the decision (within power).", "<b>No.</b> Court usually sets aside and remits."],
            ["New evidence?", "Often yes (rules vary).", "Generally only if relevant to legal error."],
            ["Typical outcome if win", "Visa granted or remitted with fresh look.", "Decision quashed → remitted to decision-maker."],
            ["If you only say “the decision was unfair / wrong”", "May be enough if facts support.", "<b>Not enough.</b> Need jurisdictional error."],
        ],
        s, [3.5 * cm, 6.5 * cm, 6.5 * cm],
    ))
    story.append(Spacer(1, 0.3 * cm))
    story.append(info_box(
        "PRACTITIONER WARNING",
        "Most self-represented JR applications fail because they argue the case as if it were a second merits appeal. "
        "Train every client to say: <b>“The decision-maker made a legal error. Here is the error. Here is where it appears in the reasons.”</b>",
        s,
    ))
    story.append(PageBreak())

    # 4 Decision Map
    story.append(Paragraph("4. DECISION MAP — WHAT STAGE IS THE CLIENT AT?", s["h1"]))
    story.append(Paragraph("<b>AUSTRALIA (typical offshore / onshore Pakistan pathway)</b>", s["h2"]))
    story.append(bullets([
        "<b>Stage A:</b> Department of Home Affairs refusal → check if ART review rights exist and deadline (often 21 or 28 days depending on decision type / location — <b>verify the refusal letter</b>).",
        "<b>Stage B:</b> Administrative Review Tribunal (ART) Migration &amp; Refugee Division affirms refusal → <b>this is the usual JR target</b>.",
        "<b>Stage C:</b> File JR in Federal Circuit and Family Court of Australia (Division 2) within <b>35 days</b> of the migration decision date.",
        "<b>Stage D (limited):</b> Some decisions (e.g. certain character / Ministerial) may start in Federal Court — check Migration Act s 476A.",
    ], s["bullet"]))
    story.append(Paragraph("<b>NEW ZEALAND</b>", s["h2"]))
    story.append(bullets([
        "<b>Stage A:</b> Immigration New Zealand (INZ) decline.",
        "<b>Stage B:</b> Appeal to Immigration and Protection Tribunal (IPT) <b>where available</b> — often mandatory before JR (s 249).",
        "<b>Stage C:</b> After IPT final determination → apply to High Court for <b>leave</b> to bring JR (usually within <b>28 days</b> of notification) under s 249.",
        "<b>Stage D:</b> Where the matter is <b>outside</b> IPT jurisdiction, JR may proceed under s 247 (28 days; extension must generally be sought within that period).",
    ], s["bullet"]))
    story.append(Paragraph(
        "Team SOP: On intake, complete the Decision Map worksheet (Section 11) before drafting a single court document.",
        s["note"],
    ))
    story.append(PageBreak())

    # 5 AUSTRALIA
    story.append(Paragraph("5. AUSTRALIA — END-TO-END JUDICIAL REVIEW", s["h1"]))
    story.append(Paragraph("5.1 Pathway before court", s["h2"]))
    story.append(Paragraph(
        "Almost every Pakistan-based student, partner, visitor, or skilled refusal that reaches JR has already been through "
        "Department → ART. JR attacks the <b>ART decision</b> (or other reviewable migration decision), not simply “I disagree with Home Affairs.”",
        s["body"],
    ))
    story.append(Paragraph("5.2 Court jurisdiction", s["h2"]))
    story.append(bullets([
        "<b>Primary court:</b> Federal Circuit and Family Court of Australia (Division 2) — migration JR under Migration Act s 476.",
        "<b>Respondent:</b> Usually the Minister for Immigration and Citizenship / Home Affairs (title as current on refusal / ART decision). Name the Minister correctly from the decision cover page.",
        "<b>Relief:</b> Writs in the nature of certiorari / mandamus / prohibition / declaration / injunction (as available under the Act and Constitution).",
        "<b>What Court will NOT do:</b> Re-weigh evidence, grant the visa, or act as a general appeal.",
    ], s["bullet"]))

    story.append(Paragraph("5.3 Time limits &amp; extension of time", s["h2"]))
    story.append(make_table(
        ["Item", "Rule of thumb (verify)", "Team action"],
        [
            ["JR filing deadline", "Within <b>35 days</b> of the date of the migration decision", "Diary Day 0 = decision date on ART/decision record"],
            ["Late filing", "Court may extend time if marked on application + explained in affidavit", "Draft extension grounds: delay explanation, prejudice, merits, public interest"],
            ["ART merits deadline", "Printed on refusal — often short", "Never skip ART if rights exist and time remains"],
            ["Bridging visa / status", "Separate from JR", "Client must manage status; JR does not automatically grant stay"],
        ],
        s, [4 * cm, 6.5 * cm, 6 * cm],
    ))

    story.append(Paragraph("5.4 Grounds — jurisdictional error catalogue", s["h2"]))
    story.append(Paragraph(
        "Train the team to plead <b>specific</b> grounds with paragraph references to the ART reasons:",
        s["body"],
    ))
    story.append(make_table(
        ["Ground (short name)", "What it means", "Evidence / proof tip"],
        [
            ["Failure to consider a relevant consideration", "Ignored a claim, integer of claim, or mandatory criterion", "Show claim was made + not addressed in reasons"],
            ["Irrelevant consideration", "Took into account something forbidden / extraneous", "Show the irrelevant matter actually affected the outcome"],
            ["Wrong question / misconstruction of statute", "Misapplied Migration Act / Regulations / Direction", "Compare statute text to what Tribunal said it asked"],
            ["Procedural fairness / natural justice", "No meaningful opportunity to respond to adverse info", "Show surprise material + no invitation to comment"],
            ["Legal unreasonableness", "Outcome / process lacks evident justification (high bar)", "Use sparingly; build from primary errors"],
            ["No evidence / illogical fact finding", "Critical finding with no evidence or irrational leap", "Pinpoint the finding and the missing evidence"],
            ["Bias / prejudgment (actual or apprehended)", "Fair-minded observer might think mind closed", "Rare; need clear conduct record"],
            ["Failure to warn / apply policy correctly", "Bound Direction / PAM applied wrongly", "Extract Direction clauses vs reasons"],
        ],
        s, [4.2 * cm, 6.2 * cm, 6.1 * cm],
    ))
    story.append(Spacer(1, 0.25 * cm))
    story.append(Paragraph(
        "<b>Pleading discipline:</b> Prefer 2–4 strong grounds over 12 weak ones. Each ground = (1) legal principle, "
        "(2) where Tribunal erred, (3) why it was material.",
        s["note"],
    ))

    story.append(Paragraph("5.5 Documents to file &amp; serve (FCFCOA Div 2 — usual first instance)", s["h2"]))
    story.append(bullets([
        "<b>Originating Application – Migration Act</b> (current FCFCOA form — download from fcfcoa.gov.au; do not use obsolete templates).",
        "<b>Affidavit</b> of the Applicant (facts, chronology, extension if needed) with annexures:",
        "— ART decision and reasons (full)",
        "— Department refusal (if relevant)",
        "— Key evidence that proves the legal error (not a full re-hearing dump)",
        "— Passport bio page / identity",
        "<b>Filing fee</b> or fee exemption / reduction application (financial hardship forms as current on Federal Court / FCFCOA fee pages).",
        "After filing: <b>serve</b> the Minister (usually via Australian Government Solicitor / service address notified by Registry — follow sealed copy instructions).",
    ], s["bullet"]))
    story.append(Paragraph(
        "If the matter is in Federal Court original jurisdiction (rare for ordinary ART MRD decisions), use <b>Form 70</b> "
        "(Originating application for review of a migration decision) under Federal Court Rules r 31.22 — confirm jurisdiction first.",
        s["body"],
    ))

    story.append(Paragraph("5.6 Step-by-step filing checklist (self-represented client)", s["h2"]))
    steps_au = [
        "<b>Day 0–2:</b> Receive ART decision. Extract decision date. Calculate Day 35. Open case file.",
        "<b>Day 1–5:</b> Error conference — team marks up ART reasons with highlighters: ignored claim / wrong test / procedural fairness.",
        "<b>Day 3–10:</b> Draft Originating Application grounds + Affidavit + annexure index. Client reviews.",
        "<b>Day 10–14:</b> Client signs affidavit before authorised witness (rules vary — typically JP / lawyer / authorised person; if client in Pakistan, use method accepted by Court for overseas affidavits — check current practice note).",
        "<b>Before Day 35:</b> File electronically via Commonwealth Courts Portal / Registry instructions. Pay fee or lodge exemption.",
        "<b>+1–7 days after filing:</b> Serve sealed documents on Minister. File Affidavit of Service.",
        "<b>Case management:</b> Diary directions hearing. Prepare Court Book / List of Authorities if ordered.",
        "<b>Outline of Submissions:</b> Short, page-limited, ground-by-ground. Attach authorities list.",
        "<b>Hearing:</b> Client appears (in person / AVL as directed). Speak to grounds; answer Judge’s questions; do not re-argue visa merits.",
        "<b>Judgment:</b> If successful → remittal. Prepare remittal pack for ART. If dismissed → advise appeal prospects to Full Court / Federal Court (strict timelines).",
    ]
    for i, st in enumerate(steps_au, 1):
        story.append(Paragraph(f"<b>Step {i}.</b> {st}", s["bullet"]))

    story.append(Paragraph("5.7 Hearing preparation &amp; after judgment", s["h2"]))
    story.append(bullets([
        "Prepare a 1-page ‘oral roadmap’ for the client: Ground 1 (60 seconds), Ground 2, Ground 3, materiality.",
        "Authorities: 3–6 key cases max for self-rep (e.g. classic High Court statements on jurisdictional error — update list annually).",
        "Costs risk: explain that unsuccessful applicants may face costs orders.",
        "Remittal: winning JR is not a visa grant — rebuild ART case properly.",
    ], s["bullet"]))
    story.append(PageBreak())

    # 6 NEW ZEALAND
    story.append(Paragraph("6. NEW ZEALAND — END-TO-END JUDICIAL REVIEW", s["h1"]))
    story.append(Paragraph("6.1 Pathway before court", s["h2"]))
    story.append(Paragraph(
        "INZ declines many temporary and residence applications from Pakistan. Where an appeal right to the "
        "<b>Immigration and Protection Tribunal (IPT)</b> exists, that path usually comes <b>before</b> judicial review.",
        s["body"],
    ))
    story.append(Paragraph("6.2 Immigration Act 2009 — ss 247 and 249 (team must master this)", s["h2"]))
    story.append(make_table(
        ["Provision", "When it applies", "Practical effect"],
        [
            ["s 249", "Decision (or its effect) could be appealed to IPT", "Must complete IPT first. JR only with <b>leave</b> of High Court (or CA if HC refuses). Leave app usually within <b>28 days</b> of IPT notification."],
            ["s 247", "Review of statutory power of decision under the Act where s 249 does not force the IPT-first path", "JR as of right if filed within <b>28 days</b> of notification; extension generally sought <b>within</b> the 28 days."],
            ["Leave test (s 249)", "Issues not adequately dealt with on IPT appeal + of general/public importance or other reason", "Draft leave around discrete legal issues, not merits re-run."],
        ],
        s, [3.2 * cm, 6.5 * cm, 6.8 * cm],
    ))
    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph(
        "Wrong pathway = strike-out / leave refused. Always ask: <b>Could this have been appealed to IPT?</b> "
        "If yes, has IPT finished? Then leave + JR.",
        s["note"],
    ))

    story.append(Paragraph("6.3 Documents (High Court — self-rep)", s["h2"]))
    story.append(bullets([
        "<b>Statement of Claim</b> (judicial review) — parties, decision under challenge, grounds, relief.",
        "<b>Notice of Proceeding</b> (High Court Rules Form G2 content).",
        "<b>Affidavit(s)</b> in support (exhibits: INZ decision, IPT decision, key documents).",
        "Where s 249 applies: <b>Interlocutory application for leave</b> + supporting affidavit + draft statement of claim.",
        "Filing fee (check Ministry of Justice current fees). Hardship / fee waiver pathways if available.",
        "Service on the respondent (typically Minister of Immigration / Attorney-General as required).",
    ], s["bullet"]))

    story.append(Paragraph("6.4 Step-by-step filing checklist (self-represented)", s["h2"]))
    steps_nz = [
        "Confirm whether IPT appeal existed and was exhausted.",
        "Diary 28-day leave / JR clock from notification date (keep envelope / email header proof).",
        "Identify 1–3 reviewable legal issues for leave (s 249) or JR grounds (s 247).",
        "Draft leave application + affidavit + proposed statement of claim.",
        "Client swears affidavit in NZ-acceptable form (overseas oaths — follow High Court / NZ consular practice).",
        "File in correct High Court registry; pay fee.",
        "Serve respondents; file affidavit of service.",
        "Attend leave hearing if required; if leave granted, proceed on the issues stated by the Court.",
        "Substantive JR hearing → judgment → remittal / dismissal → advice on Court of Appeal.",
    ]
    for i, st in enumerate(steps_nz, 1):
        story.append(Paragraph(f"<b>NZ Step {i}.</b> {st}", s["bullet"]))
    story.append(PageBreak())

    # 7 SCENARIO
    story.append(Paragraph("7. SCENARIO CASE — FULL WORKED FILE", s["h1"]))
    story.append(Paragraph("7.1 Fact pattern (training scenario — fictional)", s["h2"]))
    story.append(Paragraph(
        "<b>Client:</b> Ms Ayesha Khan, Pakistani national, currently in Lahore.<br/>"
        "<b>Application:</b> Australia Subclass 500 Student visa (offshore).<br/>"
        "<b>Course:</b> Master of Information Technology, private institute in Melbourne.<br/>"
        "<b>Department:</b> Refused for failure to satisfy Genuine Temporary Entrant (GTE) / Genuine Student criteria "
        "(as framed in the decision record — training uses GTE language as in classic refusals).<br/>"
        "<b>ART:</b> Affirmed refusal on 2 June 2026. Decision date on cover: <b>2 June 2026</b>. "
        "Reasons allege: (a) career progression not logical; (b) weak home ties; (c) failed to consider "
        "updated employment letter and property documents that were validly before the Tribunal after a post-hearing direction.<br/>"
        "<b>Client goal:</b> Self-represented JR in FCFCOA Div 2. Pakistan team prepares drafts.",
        s["body"],
    ))
    story.append(Paragraph("7.2 Error analysis (what we plead)", s["h2"]))
    story.append(bullets([
        "<b>Ground 1 — Failure to consider relevant material:</b> ART failed to engage with the 15 May 2026 employer letter and property documents lodged in response to Tribunal direction (integer of home ties claim).",
        "<b>Ground 2 — Procedural fairness:</b> ART relied on an adverse inference about ‘unexplained career change’ drawn from LinkedIn printout never put to Applicant for comment.",
        "<b>Ground 3 (alternative) — Misconstruction / wrong test:</b> ART assessed ‘permanent migration intention’ as determinative contrary to the correct Genuine Student / GTE framework requiring evaluative assessment of all circumstances.",
        "<b>Materiality:</b> Each error could realistically have resulted in a different decision on home ties / intention.",
    ], s["bullet"]))
    story.append(Paragraph("7.3 Deadline calculation", s["h2"]))
    story.append(Paragraph(
        "Decision date: 2 June 2026 → Day 35 = <b>7 July 2026</b>. File on or before that date. "
        "Team internal deadline: drafts locked by 30 June 2026; client swearing 2–3 July; e-file 4 July.",
        s["body"],
    ))
    story.append(Paragraph("7.4 Evidence index (Court Book lite)", s["h2"]))
    story.append(make_table(
        ["Tab", "Document", "Purpose"],
        [
            ["A", "ART Decision &amp; Reasons (2 Jun 2026)", "Decision under review"],
            ["B", "Department refusal record", "Background"],
            ["C", "Applicant passport bio page", "Identity"],
            ["D", "Tribunal direction (1 May 2026) + lodging email (15 May 2026)", "Proves material was before ART"],
            ["E", "Employer letter + property docs (15 May pack)", "Relevant material not considered"],
            ["F", "Hearing transcript / audio extract (if available)", "PF / LinkedIn issue"],
            ["G", "LinkedIn printout used by ART (if in reasons/file)", "Adverse material"],
        ],
        s, [1.5 * cm, 8 * cm, 7 * cm],
    ))
    story.append(Spacer(1, 0.25 * cm))
    story.append(Paragraph("7.5 NZ parallel note (same facts adapted)", s["h2"]))
    story.append(Paragraph(
        "If this were an NZ student decline affirmed by IPT on similar ‘bona fide student’ reasoning with ignored post-hearing documents, "
        "the pathway would be: confirm IPT exhausted → within 28 days file <b>leave under s 249</b> focusing on failure to consider relevant evidence "
        "and natural justice — not a re-argument of study plans.",
        s["body"],
    ))
    story.append(PageBreak())

    # 8 TEMPLATES
    story.append(Paragraph("8. COMPLETE DRAFTING TEMPLATES (FILLABLE)", s["h1"]))
    story.append(Paragraph(
        "Copy into Word, replace [BRACKETED] text. Have client sign where indicated. "
        "Always align captions with current Court form fields.",
        s["note"],
    ))

    story.append(Paragraph("TEMPLATE A — AU Originating Application grounds (insert into current FCFCOA Migration Act form)", s["h2"]))
    story.append(mono_block("""
IN THE FEDERAL CIRCUIT AND FAMILY COURT OF AUSTRALIA (DIVISION 2)
AT [REGISTRY e.g. MELBOURNE]

File number: [to be allocated]

AYESHA KHAN
Applicant

MINISTER FOR IMMIGRATION AND CITIZENSHIP
Respondent

ORIGINATING APPLICATION – MIGRATION ACT
(Judicial review of a migration decision)

1. The Applicant applies for judicial review of the decision of the Administrative Review Tribunal
   made on 2 June 2026 affirming the refusal of a Subclass 500 Student visa (the Decision).

2. The Applicant seeks:
   (a) an order that the Decision be quashed;
   (b) an order that the matter be remitted to the Tribunal (differently constituted) for
       determination according to law;
   (c) such further or other order as the Court thinks fit;
   (d) costs.

GROUNDS OF APPLICATION

Ground 1 — Failure to consider relevant considerations / relevant material
3. The Tribunal constructively failed to exercise jurisdiction by failing to consider relevant
   material that was before it, namely the Applicant's employer letter dated 15 May 2026 and
   supporting property documents lodged on 15 May 2026 in response to the Tribunal's direction,
   which went to the Applicant's home ties / intentions integer of the Genuine Student / GTE assessment.

Ground 2 — Denial of procedural fairness
4. The Tribunal denied the Applicant procedural fairness by relying on adverse information /
   inferences drawn from a LinkedIn profile printout (referred to at [xx] of the Reasons) without
   giving the Applicant a meaningful opportunity to comment.

Ground 3 — Misconstruction of the applicable legal test (in the alternative)
5. The Tribunal misconstrued / misapplied the applicable Genuine Student / GTE criteria by treating
   an asserted desire for long-term career mobility as determinative of failure, rather than evaluating
   all circumstances as required by law / the applicable Ministerial Direction.

6. Each error was material in the sense that there is a realistic possibility of a different outcome
   if the error had not been made.

Extension of time (only if needed)
7. [If filing after Day 35:] The Applicant seeks an extension of time because [reasons: late receipt /
   illness / waiting for reasons / impecuniosity / arguable case / no prejudice].

Prepared by: [Name of person who prepared the application]
Applicant signature: _____________________  Date: ________
""", s))

    story.append(Paragraph("TEMPLATE B — AU Affidavit of Applicant (structure)", s["h2"]))
    story.append(mono_block("""
AFFIDAVIT

I, Ayesha Khan, of [address], Lahore, Pakistan, [occupation], affirm / swear:

1. I am the Applicant. I make this affidavit from my own knowledge except where otherwise stated.

2. I am a citizen of Pakistan. A copy of my passport biodata page is annexed and marked "AK-1".

3. On [date] I applied for a Subclass 500 Student visa to study [course] at [institution].

4. On [date] a delegate of the Minister refused the visa. A copy is annexed "AK-2".

5. I applied to the Administrative Review Tribunal for review. On 2 June 2026 the Tribunal affirmed
   the refusal. The Decision and Reasons are annexed "AK-3".

6. On 1 May 2026 the Tribunal directed me to provide further documents about employment and assets.
   On 15 May 2026 I lodged an employer letter and property documents. Copies of the direction,
   lodging email, and documents are annexed "AK-4", "AK-5", and "AK-6".

7. I have read the Reasons. The Reasons do not engage with the 15 May 2026 employer letter or
   property documents when discussing home ties / intentions at paragraphs [xx]–[yy].

8. At the hearing / in the Reasons the Tribunal referred to a LinkedIn printout. I was not given
   that printout before the Decision or invited to comment on the adverse inference at [zz].
   [Attach transcript extract if available — "AK-7".]

9. I seek the relief in the Originating Application. I believe the Tribunal made jurisdictional errors
   as set out in the Grounds.

10. [Extension of time facts if any.]

11. Except as stated, I have not received legal advice from an Australian lawyer. I am self-represented.
    This affidavit was prepared with drafting assistance from [organisation], who are not acting as
    my Australian legal representatives on the Court record.

AFFIRMED / SWORN at [place] on [date]
Before me: [qualified witness — name, capacity, seal]
Signature of deponent: __________________
""", s))

    story.append(Paragraph("TEMPLATE C — AU Outline of Submissions (hearing)", s["h2"]))
    story.append(mono_block("""
OUTLINE OF SUBMISSIONS OF THE APPLICANT (SELF-REPRESENTED)

A. Introduction (1 page max)
1. Decision under review; date; relief sought.
2. Real issues: Grounds 1–3.

B. Ground 1 — Failure to consider relevant material
3. Legal principle: Tribunal must consider relevant material / integers of claims.
4. Evidence: Tabs D–F (direction; lodging; documents).
5. Reasons silence at [xx]–[yy].
6. Materiality: home ties was a decisive adverse finding.

C. Ground 2 — Procedural fairness
7. Principle: adverse information from third-party source must be put.
8. LinkedIn use at [zz]; no opportunity to comment.
9. Materiality.

D. Ground 3 — Misconstruction (alternative)
10. Correct test vs Tribunal's approach at [aa].

E. Orders sought
11. Quash + remit + costs.

Authorities (short list): [insert 3–6 current authorities]
""", s))
    story.append(PageBreak())

    story.append(Paragraph("TEMPLATE D — NZ Application for Leave (s 249) — skeleton", s["h2"]))
    story.append(mono_block("""
IN THE HIGH COURT OF NEW ZEALAND
[REGISTRY] REGISTRY
CIV-[year]-[number]

UNDER        the Immigration Act 2009 and the Judicial Review Procedure Act 2016
IN THE MATTER of an application for leave to commence review proceedings under s 249

BETWEEN      [FULL NAME]
             Applicant

AND          MINISTER OF IMMIGRATION
             Respondent

INTERLOCUTORY APPLICATION FOR LEAVE TO BRING REVIEW PROCEEDINGS

To: The Registrar of the High Court at [city]
And: The Respondent

This document notifies you that —

1. The Applicant will on [date] apply for orders:
   (a) granting leave under s 249 of the Immigration Act 2009 to bring review proceedings
       in respect of the Immigration and Protection Tribunal decision dated [date]
       in [IPT reference];
   (b) directing that the issues for review be:
       Issue 1: Whether the Tribunal failed to consider relevant evidence lodged on [date]
                regarding [topic];
       Issue 2: Whether the Tribunal breached natural justice by relying on [adverse material]
                without giving the Applicant an opportunity to comment;
   (c) costs.

2. The grounds are:
   (a) the proposed review issues could not be adequately dealt with in the IPT appeal process
       as determined, because they concern legality / process errors;
   (b) the issues are of general or public importance / ought to be submitted for review because
       [brief reasons — e.g. recurring IPT approach; clear arguable error; significant consequences];
   (c) the application is made within 28 days of notification of the IPT determination
       (notified on [date] — proof annexed).

3. The application is made in reliance on ss 247 and 249 Immigration Act 2009, the Judicial Review
   Procedure Act 2016, and the affidavit of [Name] dated [date].

Date: ________    Signature of Applicant: ______________________
""", s))

    story.append(Paragraph("TEMPLATE E — NZ Statement of Claim (Judicial Review) — skeleton", s["h2"]))
    story.append(mono_block("""
STATEMENT OF CLAIM

Parties
1. The Applicant is [name], a citizen of Pakistan, of [address].
2. The Respondent is the Minister of Immigration, sued in respect of the decision of the
   Immigration and Protection Tribunal dated [date] (the Decision).

Decision under challenge
3. On [date] the Tribunal dismissed the Applicant's appeal against INZ's decline of a
   [visa type] application.

Grounds of review
4. Error of law / failure to consider relevant considerations: The Tribunal failed to consider
   [identify documents and paragraphs].
5. Natural justice: The Tribunal relied on [material] without giving the Applicant an opportunity
   to respond.
6. Unreasonableness (if truly available on facts): [plead narrowly].

Relief
7. An order setting aside the Decision;
8. An order remitting the matter to the Tribunal for reconsideration;
9. Costs.

Date: ________    Signature: ______________________
""", s))

    story.append(Paragraph("TEMPLATE F — Affidavit of Service (AU/NZ common structure)", s["h2"]))
    story.append(mono_block("""
AFFIDAVIT OF SERVICE

I, [Name], of [address], [occupation], say:

1. On [date] at [time] I served the Respondent with the following documents:
   (a) sealed Originating Application / Notice of Proceeding;
   (b) Affidavit of [Applicant] sworn [date] with exhibits;
   (c) [any other].

2. Service was effected by [personal service / email to nominated address / post — as permitted]
   at [address / email].

3. Annexed "S-1" is proof of service ([email delivery receipt / courier tracking / acknowledgment]).

Signature / witness jurat as required.
""", s))

    story.append(Paragraph("TEMPLATE G — Client coaching script (15 minutes)", s["h2"]))
    story.append(mono_block("""
COACHING SCRIPT — SELF-REPRESENTED JR CLIENT

1) "The Court will not grant your visa. We are asking the Court to check if the Tribunal
    followed the law."
2) "Your three errors are: [1], [2], [3]. Memorise them."
3) "If the Judge asks why the Tribunal was wrong on the facts, answer: 'That is a merits point.
    My case is the legal error at paragraph [xx].'"
4) "Bring passport, sealed documents, Court Book tabs, and a bottle of water."
5) "Address the Judge as 'Your Honour'. Stand when required. Do not interrupt counsel for Minister."
6) "If you do not know an answer: 'I am self-represented; may I take a moment to find the page?'"
7) "After judgment, call us the same day. Do not post about the case on social media."
""", s))
    story.append(PageBreak())

    # 9 Forms directory
    story.append(Paragraph("9. FORMS DIRECTORY &amp; OFFICIAL LINKS", s["h1"]))
    story.append(Paragraph("Australia", s["h2"]))
    story.append(make_table(
        ["Item", "Where to get it", "Notes"],
        [
            ["Originating Application – Migration Act", "fcfcoa.gov.au → Migration → I want to apply", "Primary form for Div 2 JR"],
            ["Affidavit form / rules", "FCFCOA forms + Federal Circuit and Family Court Rules", "Annex decision + reasons"],
            ["Fee exemption / reduction", "Federal Court / FCFCOA fees pages", "Financial hardship evidence"],
            ["Form 70 (Federal Court)", "fedcourt.gov.au forms (FCA Form 70)", "Only if FCA original jurisdiction"],
            ["Commonwealth Courts Portal", "portal instructions on court sites", "E-filing for self-rep"],
            ["ART decision access", "ART online account / decision letter", "Keep PDF + covering email"],
        ],
        s, [4.5 * cm, 6.5 * cm, 5.5 * cm],
    ))
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph("New Zealand", s["h2"]))
    story.append(make_table(
        ["Item", "Where to get it", "Notes"],
        [
            ["Statement of Claim / Notice of Proceeding", "justice.govt.nz — representing yourself in High Court", "Follow High Court Rules formats"],
            ["Form G2 content (Notice of Proceeding)", "High Court Rules", "JR respondent notice"],
            ["IPT appeal forms", "justice.govt.nz / IPT pages", "Exhaust before s 249 JR"],
            ["Leave application", "Interlocutory application + affidavit", "28-day clock critical"],
            ["Judicial Review Procedure Act 2016", "legislation.govt.nz", "Procedural backbone"],
            ["Immigration Act 2009 ss 247, 249", "legislation.govt.nz", "Mandatory reading"],
        ],
        s, [4.5 * cm, 6.5 * cm, 5.5 * cm],
    ))
    story.append(Spacer(1, 0.3 * cm))
    story.append(info_box(
        "FEE WARNING",
        "Court filing fees change. Never rely on a fee figure printed in old training notes. "
        "Check the live fees schedule on filing day. Fee waiver / exemption may be available for impecunious self-represented applicants.",
        s,
    ))
    story.append(PageBreak())

    # 10 SOPs
    story.append(Paragraph("10. TEAM SOPs, ETHICS &amp; QUALITY CONTROL", s["h1"]))
    story.append(Paragraph("10.1 Intake SOP (same day)", s["h2"]))
    story.append(bullets([
        "Collect: passport, refusal, ART/IPT decision+reasons, complete Department/INZ file if held, hearing recording/transcript request status, bridging/visa status, removal/deportation risk flags.",
        "Complete Decision Map worksheet.",
        "Conflict check + engagement letter stating: drafting assistance only; client self-represented; no AU/NZ practising certificate held by Pakistan team (unless true).",
        "Diary hard deadlines in shared calendar with two reminders (T-10 and T-3).",
    ], s["bullet"]))
    story.append(Paragraph("10.2 Quality gate before client swears", s["h2"]))
    story.append(bullets([
        "Second lawyer reviews grounds for ‘merits dressed as JR’.",
        "Every ground has a pinpoint paragraph reference to reasons.",
        "Annexures paginated and labelled.",
        "Extension of time facts complete if late.",
        "Client understands costs risk and remittal outcome.",
    ], s["bullet"]))
    story.append(Paragraph("10.3 Ethics red lines", s["h2"]))
    story.append(bullets([
        "Do not fabricate evidence or coach false testimony.",
        "Do not file hopeless JR solely to delay removal without frank advice on prospects.",
        "Do not hold out as Australian / NZ solicitors / migration agents if not licensed.",
        "If client is in immigration detention or faces imminent removal — escalate immediately; consider urgent injunction advice from local counsel.",
    ], s["bullet"]))
    story.append(PageBreak())

    # 11 Quick reference
    story.append(Paragraph("11. QUICK REFERENCE CARDS", s["h1"]))
    story.append(Paragraph("Card 1 — Decision Map Worksheet (print &amp; fill)", s["h2"]))
    story.append(mono_block("""
Client: _______________________  Country: Pakistan
Visa subclass / type: _______________________
Department / INZ decision date: _____________
Tribunal (ART / IPT) decision date: _________
Notification date (email/post proof): _______
JR / Leave deadline calculated: ____________
Forum: [ ] FCFCOA Div 2  [ ] Fed Court  [ ] NZ HC leave (s249)  [ ] NZ HC JR (s247)
Respondent correct name: __________________
Top 3 alleged jurisdictional errors:
1. ________________________________________
2. ________________________________________
3. ________________________________________
Status / bridging / deportation risk: ______
Self-rep confirmed (client signs): [ ] Yes
Reviewer sign-off: ________________________
""", s))
    story.append(Paragraph("Card 2 — AU 35-day countdown", s["h2"]))
    story.append(Paragraph(
        "Day 0 = decision date on ART record → add 35 days → filing deadline. "
        "If reasons arrive later, deadline still usually runs from decision date — do not wait passively; seek reasons urgently.",
        s["body"],
    ))
    story.append(Paragraph("Card 3 — NZ 28-day countdown", s["h2"]))
    story.append(Paragraph(
        "Day 0 = date client notified of IPT (or other) decision → 28 days for leave / JR. "
        "If extension needed under s 247, application for extension generally must be made before the 28 days expire.",
        s["body"],
    ))
    story.append(PageBreak())

    # 12 Assessment
    story.append(Paragraph("12. TRAINING ASSESSMENT CHECKLIST", s["h1"]))
    story.append(Paragraph(
        "Team lead signs off when each member can perform the following without assistance:",
        s["body"],
    ))
    story.append(make_table(
        ["#", "Competency", "Pass?"],
        [
            ["1", "Explain JR vs merits review to a client in under 3 minutes", "[ ]"],
            ["2", "Calculate AU 35-day and NZ 28-day deadlines from sample letters", "[ ]"],
            ["3", "Choose correct AU forum (FCFCOA vs FCA) for a sample decision", "[ ]"],
            ["4", "Choose correct NZ path (s 249 leave vs s 247 JR) for a sample decision", "[ ]"],
            ["5", "Mark up ART reasons and draft 2 jurisdictional error grounds with pinpoints", "[ ]"],
            ["6", "Assemble affidavit annexure list and service pack", "[ ]"],
            ["7", "Role-play 10-minute self-rep oral submissions using Scenario Case", "[ ]"],
            ["8", "Identify a hopeless ‘merits only’ case and write frank advice note", "[ ]"],
            ["9", "Locate current forms/fees on official websites (live demo)", "[ ]"],
            ["10", "Complete Scenario Case file to filing-ready standard (peer reviewed)", "[ ]"],
        ],
        s, [1.2 * cm, 13.3 * cm, 2 * cm],
    ))
    story.append(Spacer(1, 0.5 * cm))
    story.append(Paragraph("APPENDIX — SCENARIO CASE FILING-READY CHECKLIST", s["h1"]))
    story.append(bullets([
        "[ ] Originating Application grounds final (Templates A)",
        "[ ] Affidavit sworn/affirmed (Template B) with Tabs A–G",
        "[ ] Fee paid or exemption lodged",
        "[ ] E-filing receipt saved",
        "[ ] Service on Minister completed + Affidavit of Service (Template F)",
        "[ ] Directions hearing diary note",
        "[ ] Outline of Submissions draft (Template C)",
        "[ ] Client coaching completed (Template G)",
        "[ ] Remittal contingency plan filed in CMS",
    ], s["bullet"]))
    story.append(Spacer(1, 0.4 * cm))
    story.append(info_box(
        "END OF MANUAL — TRAINER NOTES",
        "Recommended delivery: Day 1 (theory + AU) 3 hours; Day 2 (NZ + scenario drafting workshop) 3 hours; "
        "Day 3 (mock hearing + assessment) 2 hours. Update forms/fees quarterly. Maintain a shared folder of "
        "successful anonymised precedents. For live cases with removal risk, brief admitted AU/NZ counsel.",
        s,
    ))
    story.append(Spacer(1, 0.5 * cm))
    story.append(Paragraph(
        "© Training material for internal professional development. Verify all procedure against official sources before filing.",
        s["center"],
    ))

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=1.8 * cm,
        rightMargin=1.8 * cm,
        topMargin=1.8 * cm,
        bottomMargin=1.8 * cm,
        title="AU NZ Judicial Review Training Manual — Pakistan Team",
        author="Internal Training",
    )
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print(f"✓ PDF written: {OUT}")
    print(f"  Size: {OUT.stat().st_size // 1024} KB")
    return OUT


if __name__ == "__main__":
    build()
