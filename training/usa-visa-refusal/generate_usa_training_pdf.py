#!/usr/bin/env python3
"""
USA Visa Refusal → Administrative Options → Federal Court Training Manual
Times New Roman (Times-Roman) throughout — US court drafting convention.
Embassy refusal in Pakistan; self-represented client model.
"""

from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import letter  # US Letter — American practice
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
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

OUT = Path(__file__).parent / "USA-Visa-Refusal-Appeal-JR-Training-Manual.pdf"

# US court look: black text, Times, Letter size
NAVY = colors.HexColor("#1A1A1A")
RULE = colors.HexColor("#333333")
LIGHT = colors.HexColor("#F5F5F5")
SOFT = colors.HexColor("#EDEDED")
GREEN = colors.HexColor("#1B5E20")
RED = colors.HexColor("#8B0000")

# Standard US legal fonts (ReportLab Times = Times New Roman metric equivalent)
F = "Times-Roman"
FB = "Times-Bold"
FI = "Times-Italic"
FBI = "Times-BoldItalic"


def S():
    return {
        "cover": ParagraphStyle("c", fontName=FB, fontSize=18, leading=22,
                                textColor=NAVY, alignment=TA_CENTER, spaceAfter=10),
        "cover2": ParagraphStyle("c2", fontName=FI, fontSize=11, leading=14,
                                 textColor=RULE, alignment=TA_CENTER, spaceAfter=6),
        "h1": ParagraphStyle("h1", fontName=FB, fontSize=13, leading=16,
                             textColor=NAVY, spaceBefore=12, spaceAfter=6),
        "h2": ParagraphStyle("h2", fontName=FB, fontSize=11, leading=14,
                             textColor=NAVY, spaceBefore=9, spaceAfter=4),
        "h3": ParagraphStyle("h3", fontName=FB, fontSize=10, leading=12,
                             textColor=RULE, spaceBefore=7, spaceAfter=3),
        "body": ParagraphStyle("body", fontName=F, fontSize=10, leading=13,
                               alignment=TA_JUSTIFY, spaceAfter=6),
        "bullet": ParagraphStyle("bu", fontName=F, fontSize=10, leading=12.5,
                                 leftIndent=12, spaceAfter=2),
        "note": ParagraphStyle("note", fontName=FI, fontSize=9, leading=11.5,
                               textColor=RED, spaceBefore=3, spaceAfter=6),
        "settle": ParagraphStyle("set", fontName=F, fontSize=9, leading=11.5,
                                 textColor=GREEN, spaceBefore=3, spaceAfter=6),
        "mono": ParagraphStyle("mono", fontName=F, fontSize=8.5, leading=11,
                               backColor=SOFT, leftIndent=4, rightIndent=4, spaceBefore=3,
                               spaceAfter=6, borderPadding=6),
        "toc": ParagraphStyle("toc", fontName=F, fontSize=10, leading=14, leftIndent=6),
        "center": ParagraphStyle("ctr", fontName=F, fontSize=10, leading=13,
                                 alignment=TA_CENTER, spaceAfter=5),
        "th": ParagraphStyle("th", fontName=FB, fontSize=8, leading=10,
                             textColor=colors.white),
        "td": ParagraphStyle("td", fontName=F, fontSize=8, leading=10.5),
        "tt": ParagraphStyle("tt", fontName=FB, fontSize=10, leading=12,
                             textColor=NAVY, spaceBefore=4, spaceAfter=3),
        "caption": ParagraphStyle("cap", fontName=FB, fontSize=11, leading=14,
                                  alignment=TA_CENTER, spaceAfter=4),
    }


def hf(c, doc):
    c.saveState()
    c.setStrokeColor(RULE)
    c.setLineWidth(0.6)
    w, h = letter
    c.line(0.85 * inch, h - 0.55 * inch, w - 0.85 * inch, h - 0.55 * inch)
    c.setFont(F, 8)
    c.setFillColor(colors.grey)
    c.drawString(0.85 * inch, h - 0.45 * inch,
                 "U.S. Visa Refusal → Administrative Options → Federal Court | Pakistan Team")
    c.drawRightString(w - 0.85 * inch, h - 0.45 * inch, "CONFIDENTIAL")
    c.line(0.85 * inch, 0.6 * inch, w - 0.85 * inch, 0.6 * inch)
    c.drawCentredString(
        w / 2, 0.4 * inch,
        f"Page {doc.page}  |  Times New Roman drafting  |  Self-represented model  |  Not legal advice — verify fees/forms",
    )
    c.restoreState()


def bullets(items, style):
    return ListFlowable(
        [ListItem(Paragraph(i, style), leftIndent=8, value="•") for i in items],
        bulletType="bullet", start="•", leftIndent=10, bulletFontSize=9, bulletFontName=F,
    )


def box(title, text, s, color=LIGHT, border=RULE):
    t = Table(
        [[Paragraph(f"<b>{title}</b>", s["tt"])], [Paragraph(text, s["body"])]],
        colWidths=[7.1 * inch],
    )
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), color),
        ("BOX", (0, 0), (-1, -1), 0.8, border),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


def settle_box(text, s):
    return box(
        "SETTLEMENT / NO-HEARING RESOLUTION FLAG",
        text, s,
        color=colors.HexColor("#E8F5E9"),
        border=GREEN,
    )


def mono(text, s):
    return Preformatted(text.strip("\n"), s["mono"])


def tbl(headers, rows, s, widths):
    head = [Paragraph(h, s["th"]) for h in headers]
    body = [[Paragraph(c, s["td"]) for c in r] for r in rows]
    t = Table([head] + body, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
        ("GRID", (0, 0), (-1, -1), 0.4, SOFT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


def build():
    s = S()
    story = []

    # COVER
    story.append(Spacer(1, 1.2 * inch))
    story.append(Paragraph("UNITED STATES", s["cover2"]))
    story.append(Paragraph("VISA REFUSAL TO FINAL RESOLUTION", s["cover"]))
    story.append(Paragraph(
        "Practice Manual for Pakistan Case Teams<br/>"
        "Embassy Refusal → Reapplication / Administrative Appeal → Federal Court<br/>"
        "Self-Represented Client Model",
        s["center"],
    ))
    story.append(Spacer(1, 0.25 * inch))
    story.append(Paragraph(
        "<i>Drafting typography: Times New Roman (U.S. federal court convention)<br/>"
        "Page size: U.S. Letter (8.5 × 11 in.)</i>",
        s["center"],
    ))
    story.append(Spacer(1, 0.3 * inch))
    meta = [
        ["Scope", "F-1 Student &amp; B-1/B-2 Visitor refusals at U.S. Embassy/Consulate in Pakistan; related USCIS denials; limited federal court paths"],
        ["Client model", "Client is self-represented. Pakistan team prepares the complete file; client signs and files in own name."],
        ["Critical U.S. rule", "Most consular visa refusals under INA § 214(b) have <b>no administrative appeal</b> and are generally barred from judicial review (consular nonreviewability). Training covers what <b>is</b> available."],
        ["Includes", "Intake, reapplication packs, I-290B/AAO (where available), Mandamus/APA (narrow), fees, payment, filing methods, settlement flags, full scenario pleadings in Times New Roman"],
        ["Version", "1.0 · July 2026 · Internal training — verify all fees/forms on uscis.gov / justice.gov / court websites before filing"],
    ]
    mt = Table(
        [[Paragraph(f"<b>{a}</b>", s["td"]), Paragraph(b, s["td"])] for a, b in meta],
        colWidths=[1.3 * inch, 5.8 * inch],
    )
    mt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
        ("BOX", (0, 0), (-1, -1), 1, NAVY),
        ("INNERGRID", (0, 0), (-1, -1), 0.3, SOFT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(mt)
    story.append(Spacer(1, 0.25 * inch))
    story.append(Paragraph(
        "<b>DISCLAIMER:</b> Educational internal training only. Not legal advice. U.S. immigration law, fees, "
        "and forms change frequently. Consular nonreviewability severely limits court challenges to Embassy "
        "visa refusals. Pakistan team members must not hold out as U.S. attorneys unless licensed. "
        "Where removal, detention, or complex federal litigation arises, brief admitted U.S. counsel.",
        s["note"],
    ))
    story.append(PageBreak())

    # TOC
    story.append(Paragraph("TABLE OF CONTENTS", s["h1"]))
    for line in [
        "PART 1 — Intake: Client Walks In After U.S. Embassy Refusal (Day 0)",
        "PART 2 — End-to-End Pathway Map &amp; Settlement Windows",
        "PART 3 — Consular Refusal Reality: INA § 214(b), § 221(g), and What Is Not Appealable",
        "PART 4 — Stage A: Professional Reapplication Pack (Primary Remedy)",
        "PART 5 — Stage B: USCIS Motions &amp; AAO Appeals (Form I-290B) — When Available",
        "PART 6 — Stage C: Federal Court Options (Mandamus / APA / Petition for Review)",
        "PART 7 — Fee Schedules, Payment Methods &amp; Filing Methods",
        "PART 8 — Master Scenario Case File (F-1 &amp; B-1/B-2)",
        "PART 9 — Full Drafting Templates (Times New Roman / U.S. Caption Style)",
        "PART 10 — Team SOPs, Ethics, Quality Gates &amp; Assessment",
        "APPENDIX — Forms Index &amp; Official Links",
    ]:
        story.append(Paragraph(line, s["toc"]))
    story.append(PageBreak())

    # PART 1
    story.append(Paragraph("PART 1 — INTAKE: CLIENT WALKS IN AFTER U.S. EMBASSY REFUSAL", s["h1"]))
    story.append(Paragraph(
        "Engagement begins when the client arrives at your Pakistan office with a refusal from the "
        "U.S. Embassy / Consulate (Islamabad, Karachi, or other designated post) of an <b>F-1 student</b> "
        "or <b>B-1/B-2 visitor</b> visa. You handle strategy from that moment through reapplication, "
        "any available administrative appeal, and—only where jurisdiction exists—federal court.",
        s["body"],
    ))
    story.append(Paragraph("1.1 Same-Day Intake Protocol", s["h2"]))
    story.append(bullets([
        "<b>Identity:</b> Passport bio page; prior U.S. visas; refusals; travel history; DS-160 confirmation page; CEAC status printout.",
        "<b>Refusal instrument:</b> Refusal letter / CEAC annotation; statute cited (§ 214(b), § 221(g), § 212(a), etc.); any 221(g) document checklist.",
        "<b>Interview notes:</b> Client’s contemporaneous write-up of questions asked and answers given (same day).",
        "<b>Application file:</b> DS-160 PDF; I-20 (F-1) / invitation &amp; itinerary (B); financials; ties evidence; SEVIS fee (I-901) receipt; MRV fee receipt.",
        "<b>Prior immigration history:</b> Overstays, unlawful presence, prior petitions (I-130/I-129/I-539), pending asylum/removal (rare but critical).",
        "<b>Deadline diary:</b> If any USCIS denial is also involved, diary I-290B deadline (typically 30/33 days). Consular 214(b) has no appeal clock—but evidence freshness matters.",
        "<b>Engagement letter:</b> Self-represented model; frank advice that most Embassy refusals are <b>not</b> court-appealable; costs by stage.",
    ], s["bullet"]))
    story.append(box(
        "FIRST STRATEGIC QUESTION (DO NOT SKIP)",
        "Is this a <b>consular</b> visa refusal (DS-160 / Embassy interview), or a <b>USCIS</b> denial "
        "(I-539, I-129, I-485, etc.)? Consular F-1/B refusals under § 214(b) → almost always "
        "<b>reapplication</b>, not AAO, not district-court “appeal.” Misrouting the client into a "
        "hopeless federal lawsuit is malpractice-level error for training purposes.",
        s,
    ))
    story.append(Paragraph("1.2 F-1 vs B-1/B-2 Triage", s["h2"]))
    story.append(tbl(
        ["Issue", "F-1 Student", "B-1/B-2 Visitor"],
        [
            ["Core consular test", "INA § 214(b) — immigrant intent / nonimmigrant intent; ties; academic plan; funds", "INA § 214(b) — temporary visit; ties; purpose; return incentives"],
            ["Key documents", "I-20, SEVIS I-901, school acceptance, funds, ties, study plan", "Invitation/itinerary, employer leave, funds, property/family ties"],
            ["Typical refusal code", "214(b); sometimes 221(g) for documents", "214(b); 221(g); occasionally 212(a) grounds"],
            ["Primary remedy", "Rebuild file → new DS-160 → re-interview", "Same — reapplication with stronger temporary-stay proof"],
            ["AAO / I-290B?", "Generally <b>no</b> for Embassy refusal", "Generally <b>no</b> for Embassy refusal"],
            ["Federal court?", "Usually barred (consular nonreviewability); Mandamus only for discrete delayed duties", "Same"],
        ],
        s, [1.4 * inch, 2.85 * inch, 2.85 * inch],
    ))
    story.append(PageBreak())

    # PART 2
    story.append(Paragraph("PART 2 — END-TO-END PATHWAY &amp; SETTLEMENT WINDOWS", s["h1"]))
    story.append(mono("""
STAGE A   U.S. Embassy / Consulate refuses F-1 or B visa (§ 214(b) / § 221(g) / other)
          ↓  [FLAG A1: 221(g) — submit checklist docs; may overcome without new interview]
          ↓  [FLAG A2: informal supervisory review request — limited, usually not available as of right]
STAGE B   Professional REAPPLICATION (primary path for 214(b))
          ↓  [FLAG B1: withdraw/abandon weak reapply; wait for material change in circumstances]
STAGE C   If underlying case is USCIS denial (not Embassy) → Form I-290B (Motion / AAO Appeal)
          ↓  [FLAG C1: USCIS may reopen favorably on motion without AAO hearing]
STAGE D   Narrow federal court (Mandamus / APA for unreasonable delay or discrete unlawful action;
          Petition for Review only after final removal order — different track)
          ↓  [FLAG D1: government may grant relief / adjudicate / settle → dismiss as moot]
STAGE E   Final: visa issued / petition approved / case closed / stop advice
""", s))
    story.append(settle_box(
        "Train officers to pause at every FLAG. For U.S. consular refusals, the most common "
        "“settlement without hearing” is not a courtroom deal — it is <b>overcoming 221(g)</b>, "
        "or a <b>successful reapplication</b> after material new evidence, without litigation. "
        "In federal court, cases often end by <b>mootness</b> when the agency acts.",
        s,
    ))
    story.append(PageBreak())

    # PART 3
    story.append(Paragraph("PART 3 — CONSULAR REFUSAL REALITY", s["h1"]))
    story.append(Paragraph("3.1 INA § 214(b) — Presumption of Immigrant Intent", s["h2"]))
    story.append(Paragraph(
        "Every nonimmigrant visa applicant is presumed to be an intending immigrant until the applicant "
        "demonstrates entitlement to nonimmigrant status. A § 214(b) refusal means the consular officer "
        "was not satisfied—usually regarding home ties, purpose, or overall credibility. "
        "<b>There is no appeal to a higher administrative tribunal</b> from a routine § 214(b) refusal.",
        s["body"],
    ))
    story.append(Paragraph("3.2 INA § 221(g) — Temporary Refusal / Administrative Processing", s["h2"]))
    story.append(Paragraph(
        "A § 221(g) refusal is often a temporary refusal pending documents or security/administrative processing. "
        "Team action: read the checklist; submit exactly what is requested via the channel stated (CEAC upload / "
        "email / courier); diary follow-ups; do not flood the post with irrelevant material.",
        s["body"],
    ))
    story.append(Paragraph("3.3 Consular Nonreviewability (why “JR like Australia” usually fails)", s["h2"]))
    story.append(bullets([
        "U.S. courts generally will not review the substance of a consular visa refusal.",
        "Narrow exceptions are rare and highly fact-specific (e.g., certain constitutional claims by U.S. citizen petitioners in immigrant-visa contexts—not typical F-1/B tourist refusals by Pakistani applicants).",
        "Do <b>not</b> sell “judicial review of 214(b)” as a standard product. That is an ethics red line.",
    ], s["bullet"]))
    story.append(box(
        "TRAINING RULE",
        "For Embassy F-1/B refusals from Pakistan, your default litigation product is <b>zero</b>. "
        "Your default professional product is a <b>reapplication war file</b> that would survive a skeptical "
        "consular officer. Federal court is exceptional and must be jurisdiction-screened by a U.S.-qualified reviewer.",
        s,
    ))
    story.append(PageBreak())

    # PART 4 Reapplication
    story.append(Paragraph("PART 4 — STAGE A: PROFESSIONAL REAPPLICATION PACK", s["h1"]))
    story.append(Paragraph(
        "This is the American equivalent of “merits review” for consular student/visitor refusals: "
        "you rebuild the case and present it anew.",
        s["body"],
    ))
    story.append(Paragraph("4.1 Reapplication Checklist (F-1)", s["h2"]))
    story.append(bullets([
        "New DS-160 (accurate; consistent with prior filing—explain any corrections in interview prep notes).",
        "Current I-20; SEVIS I-901 paid; school contact ready.",
        "Financial: liquid funds covering first year; sponsor affidavit (Form I-134 only if truly applicable—often informal sponsor letters + bank evidence used carefully); source-of-funds trail.",
        "Ties: employment letter with leave/return; business/property; family dependents; prior travel compliance.",
        "Academic: degree plan essay; why this U.S. program; why not Pakistan/elsewhere; career path returning home.",
        "Prior refusal explanation: one-page factual letter addressing each 214(b) concern without arguing with the officer.",
        "Interview coaching script (truthful, short answers).",
    ], s["bullet"]))
    story.append(Paragraph("4.2 Reapplication Checklist (B-1/B-2)", s["h2"]))
    story.append(bullets([
        "New DS-160; clear purpose (tourism / family visit / business meetings—match documents).",
        "Employer leave letter + return date; business registration if self-employed.",
        "Itinerary, hotel/host letter, proof of funds, strong home ties.",
        "Address any prior overstay by relatives carefully—do not invent facts; distinguish the applicant.",
        "If previously 221(g): bring proof all items were submitted.",
    ], s["bullet"]))
    story.append(settle_box(
        "<b>FLAG B1:</b> If nothing material has changed since refusal, advise <b>waiting</b> rather than "
        "immediate reapply. A quick re-refusal without new facts wastes MRV fees and hardens the record. "
        "Document client instruction in writing.",
        s,
    ))
    story.append(Paragraph("4.3 Prior Refusal Explanation Letter — Model (Times New Roman style)", s["h2"]))
    story.append(mono("""
                                                    [Date]

Consular Officer
Nonimmigrant Visa Unit
U.S. Embassy / Consulate [Islamabad / Karachi]
Pakistan

Re:  Prior Refusal under INA § 214(b); New Application of [FULL NAME]
     Passport No. [          ]; DS-160 Confirmation [          ]

Dear Consular Officer:

I respectfully submit this letter in connection with my new nonimmigrant visa application.
On [date], my application for an [F-1 / B-1/B-2] visa was refused under INA § 214(b). I
understand that I must establish entitlement to nonimmigrant status.

Since that refusal, I have assembled additional evidence addressing the concerns that
appeared to arise at interview, including:

     1.  [Stronger employment / study-leave / return-to-post evidence];
     2.  [Updated financial documentation with clear source of funds];
     3.  [Property / family / business ties in Pakistan]; and
     4.  [For F-1: clarified academic plan and program relevance].

I intend to [study for a temporary period / visit for a temporary period] and then return
to Pakistan because [specific incentives to return]. I respectfully request that you
consider this application and the enclosed evidence.

I declare under penalty of perjury under the laws of the United States of America that
the foregoing is true and correct to the best of my knowledge.

                                              Respectfully submitted,


                                              _______________________________
                                              [FULL NAME]
                                              [Address in Pakistan]
                                              [Email]  |  [Telephone]
""", s))
    story.append(PageBreak())

    # PART 5 I-290B
    story.append(Paragraph("PART 5 — STAGE B: FORM I-290B (MOTION / AAO APPEAL)", s["h1"]))
    story.append(Paragraph(
        "Use <b>only</b> when the adverse decision is a USCIS decision that confers appeal or motion rights "
        "(e.g., certain I-129, I-539, I-130, I-485 denials). <b>Not</b> for routine Embassy DS-160 refusals. "
        "The denial notice controls.",
        s["body"],
    ))
    story.append(Paragraph("5.1 What Form I-290B Does", s["h2"]))
    story.append(tbl(
        ["Filing type", "When to use", "What you must file"],
        [
            ["Appeal to AAO", "Denial notice says AAO appeal available", "I-290B + fee + brief/evidence (now or within 30 days to AAO)"],
            ["Motion to Reopen", "New facts/evidence", "I-290B + fee + new evidence + brief with motion"],
            ["Motion to Reconsider", "Wrong application of law/policy to existing record", "I-290B + fee + legal brief (no new facts required)"],
            ["Combined MTR + MTC", "Both new evidence and legal error", "Select combined box; full brief + evidence"],
        ],
        s, [1.6 * inch, 2.4 * inch, 3.1 * inch],
    ))
    story.append(Paragraph("5.2 Deadlines (typical — verify notice)", s["h2"]))
    story.append(bullets([
        "Generally <b>30 calendar days</b> from date of service of the decision; <b>33 days</b> if decision mailed.",
        "Some revocation appeals: shorter (e.g., 15/18 days)—read the notice.",
        "File at the correct Lockbox / address on uscis.gov/i-290b-addresses — <b>do not</b> mail directly to AAO.",
    ], s["bullet"]))
    story.append(settle_box(
        "<b>FLAG C1:</b> A well-supported Motion to Reopen can be granted by the originating USCIS office "
        "<b>without</b> a contested AAO “hearing.” That is the main no-hearing win on the administrative track. "
        "After favorable reopen, the benefit request is adjudicated again.",
        s,
    ))
    story.append(Paragraph("5.3 I-290B Filing Pack", s["h2"]))
    story.append(bullets([
        "Form I-290B (current edition from uscis.gov) — one form per appeal/motion.",
        "Filing fee per Form G-1055 / Fee Schedule (confirm live; commonly cited ~$675 historically—<b>verify</b>) or Form I-912 if eligible.",
        "Copy of the decision being appealed/moved on.",
        "Legal brief (Times New Roman, double-spaced preferred for federal-style briefs).",
        "New evidence index (motions to reopen).",
        "G-28 only if a U.S. attorney/accredited representative appears—self-rep leaves blank.",
        "Mail with tracking to correct address; keep copy of entire packet.",
    ], s["bullet"]))
    story.append(PageBreak())

    # PART 6 Federal Court
    story.append(Paragraph("PART 6 — STAGE C: FEDERAL COURT OPTIONS (NARROW)", s["h1"]))
    story.append(Paragraph("6.1 Mandamus / APA (District Court)", s["h2"]))
    story.append(Paragraph(
        "A complaint for writ of mandamus (28 U.S.C. § 1361) and/or relief under the Administrative Procedure Act "
        "may be considered when an agency has unreasonably delayed a <b>nondiscretionary</b> duty "
        "(classic example: long-pending adjudication). This is <b>not</b> a substitute appeal of a § 214(b) merits refusal. "
        "Jurisdiction, venue, exhaustion, and consular nonreviewability must be screened case-by-case by U.S.-qualified counsel.",
        s["body"],
    ))
    story.append(Paragraph("6.2 Petition for Review (Court of Appeals)", s["h2"]))
    story.append(Paragraph(
        "A Petition for Review in the appropriate U.S. Court of Appeals challenges a <b>final order of removal</b> "
        "(and certain related orders) under INA § 242 / 8 U.S.C. § 1252. This is a different track from Embassy "
        "F-1/B tourist refusals. Include in training so the team does not confuse “JR” products.",
        s["body"],
    ))
    story.append(Paragraph("6.3 Filing a Civil Action (high-level self-rep map)", s["h2"]))
    story.append(bullets([
        "Draft Complaint (caption, parties, jurisdiction, facts, claims, prayer for relief) in Times New Roman.",
        "Civil Cover Sheet (JS-44 or local equivalent).",
        "Pay district court filing fee (confirm current fee with clerk; historically $405 civil fee—<b>verify</b>) or IFP application (Form AO 239/240).",
        "File via CM/ECF if admitted/registered, or clerk’s office procedures for pro se.",
        "Serve United States / agency defendants under Fed. R. Civ. P. 4(i).",
        "Diary response deadlines; consider settlement if agency adjudicates (mootness).",
    ], s["bullet"]))
    story.append(settle_box(
        "<b>FLAG D1:</b> Many Mandamus/APA delay cases end <b>without merits hearing</b> when the agency "
        "completes adjudication and parties stipulate to dismissal. Train the team to send a short status "
        "letter and be ready to dismiss as moot—do not chase unnecessary oral argument.",
        s,
    ))
    story.append(PageBreak())

    # PART 7 Fees
    story.append(Paragraph("PART 7 — FEE SCHEDULES, PAYMENT &amp; FILING METHODS", s["h1"]))
    story.append(Paragraph(
        "Amounts change. Always confirm on the live USCIS Fee Schedule (Form G-1055), travel.state.gov, "
        "EOIR payment portal, and the relevant federal court’s fee schedule on the day of filing.",
        s["note"],
    ))
    story.append(Paragraph("7.1 Consular / Department of State", s["h2"]))
    story.append(tbl(
        ["Item", "Typical amount / note", "How to pay / file"],
        [
            ["MRV fee (DS-160 interview)", "Check travel.state.gov current fee", "Pay via approved Pakistan channels; bring receipt to interview"],
            ["SEVIS I-901 (F-1)", "Check ICE FMJfee site", "Pay online; print receipt"],
            ["Visa issuance fee (reciprocity)", "Country/class specific", "If approved—pay as post instructs"],
        ],
        s, [2.2 * inch, 2.4 * inch, 2.5 * inch],
    ))
    story.append(Spacer(1, 0.12 * inch))
    story.append(Paragraph("7.2 USCIS — Form I-290B", s["h2"]))
    story.append(tbl(
        ["Item", "Note", "How to pay / file"],
        [
            ["I-290B filing fee", "See current USCIS Fee Schedule / G-1055 (commonly referenced ~$675—verify)", "Check, money order, or as Lockbox instructions allow; some payments via G-1450"],
            ["Fee waiver", "Form I-912 if eligible", "File with I-290B packet"],
            ["Filing method", "Paper mail to correct address on uscis.gov/i-290b-addresses", "USPS/courier with tracking; keep complete copy"],
            ["AAO brief after filing", "If you selected “brief within 30 days”", "Mail brief to AAO address on uscis.gov/aao with clear case identifiers"],
        ],
        s, [2.0 * inch, 2.6 * inch, 2.5 * inch],
    ))
    story.append(Spacer(1, 0.12 * inch))
    story.append(Paragraph("7.3 EOIR (Immigration Court / BIA) — if removal track", s["h2"]))
    story.append(bullets([
        "EOIR now collects many fees via <b>https://epay.eoir.justice.gov</b> — payment ≠ filing; you must still file the document.",
        "BIA appeal / motion fees have been substantially revised under recent legislation—check justice.gov/eoir fee pages before quoting any number to a client.",
        "Fee waiver processes exist for certain filings—use current EOIR forms.",
    ], s["bullet"]))
    story.append(Paragraph("7.4 Federal District Court / Court of Appeals", s["h2"]))
    story.append(bullets([
        "District court civil filing fee: confirm with clerk (commonly cited $405—verify).",
        "Court of Appeals Petition for Review fee: confirm with circuit clerk (commonly cited around $600—verify).",
        "Pay by methods the clerk accepts (online pay.gov / clerk’s office). IFP available for qualifying pro se litigants.",
    ], s["bullet"]))
    story.append(Paragraph("7.5 How to File I-290B — Step Card", s["h2"]))
    story.append(bullets([
        "Step 1: Download current I-290B + instructions from uscis.gov/i-290b.",
        "Step 2: Select exactly one: AAO appeal / MTR / MTC / combined.",
        "Step 3: Attach decision, brief, evidence, fee or I-912.",
        "Step 4: Look up Direct Filing Address chart; address envelope exactly.",
        "Step 5: Ship with tracking at least several days before deadline (mail receipt rules).",
        "Step 6: If brief to follow to AAO, diary Day 30 and mail to AAO with receipt proof.",
    ], s["bullet"]))
    story.append(PageBreak())

    # PART 8 Scenario
    story.append(Paragraph("PART 8 — MASTER SCENARIO CASE FILE", s["h1"]))
    story.append(Paragraph("8.1 Client Walks In — F-1 Facts", s["h2"]))
    story.append(Paragraph(
        "<b>Ms. Ayesha Khan</b>, age 27, Lahore. Holds a B.S. in Computer Science. Employed as IT support "
        "executive. Receives I-20 for M.S. in Information Systems at a U.S. university. Pays SEVIS and MRV fees. "
        "Interview at U.S. Embassy Islamabad on April 10, 2026. Refused under <b>INA § 214(b)</b>. "
        "Officer questions career progression and ties to Pakistan. She attends your office on April 12, 2026.",
        s["body"],
    ))
    story.append(Paragraph("8.2 Stage Plan Opened That Day", s["h2"]))
    story.append(tbl(
        ["Stage", "Action", "Hearing?", "Fee focus"],
        [
            ["A Intake", "Scan DS-160, I-20, refusal notes; engagement letter", "No", "Professional retainer"],
            ["B Rebuild", "New ties/funds/academic pack; refusal explanation letter", "No", "Document costs"],
            ["C Reapply", "New DS-160 + MRV if required + interview", "Interview (not court)", "MRV / SEVIS if new I-20"],
            ["D Optional court", "Only if separate delayed USCIS duty / other jurisdiction", "Often settles/moots", "Court filing fee"],
        ],
        s, [1.2 * inch, 3.0 * inch, 1.5 * inch, 1.4 * inch],
    ))
    story.append(Spacer(1, 0.12 * inch))
    story.append(Paragraph("8.3 Visitor Variant — Bilal Ahmed", s["h2"]))
    story.append(Paragraph(
        "B-2 refused under § 214(b) for weak temporary intent after short answers about employment and property. "
        "Rebuild with employer leave, land records, family dependents, itinerary, and a precise purpose letter. "
        "No I-290B. No “JR.” Reapply when the file is materially stronger.",
        s["body"],
    ))
    story.append(Paragraph("8.4 Evidence Index (Reapplication War File)", s["h2"]))
    story.append(tbl(
        ["Tab", "Document", "Purpose"],
        [
            ["A", "Passport biodata + prior visas", "Identity / history"],
            ["B", "CEAC refusal screenshot + client interview memo", "Record of § 214(b)"],
            ["C", "Prior DS-160 confirmation + new DS-160 confirmation", "Consistency"],
            ["D", "I-20 + SEVIS I-901 receipt (F-1)", "Student status basis"],
            ["E", "Employer letter + organogram + leave/return", "Ties / career logic"],
            ["F", "Bank statements + sponsor docs + source trail", "Funds"],
            ["G", "Property / family affidavits + translations", "Home ties"],
            ["H", "Academic plan statement (signed)", "Genuine student intent"],
            ["I", "Prior refusal explanation letter", "Address officer concerns"],
        ],
        s, [0.7 * inch, 3.5 * inch, 2.9 * inch],
    ))
    story.append(PageBreak())

    # PART 9 Templates
    story.append(Paragraph("PART 9 — FULL DRAFTING TEMPLATES (U.S. STYLE / TIMES NEW ROMAN)", s["h1"]))
    story.append(Paragraph(
        "All templates below are set in Times New Roman. For federal court briefs, use U.S. Letter, "
        "Times New Roman 14-point (or as local rules require), double-spaced text, one-inch margins.",
        s["note"],
    ))

    story.append(Paragraph("TEMPLATE A — F-1 Academic / Ties Statement (Reapply)", s["h2"]))
    story.append(mono("""
STATEMENT OF [FULL NAME]
In Support of Application for F-1 Student Visa

I, [FULL NAME], declare as follows:

1.   I am a citizen of Pakistan residing at [address], Lahore, Pakistan.

2.   I have been admitted to [University], [City, State], for the [Master of ___] program
     beginning [term/year]. My Form I-20 was issued on [date]. I paid the SEVIS I-901 fee
     on [date], Receipt No. [     ].

3.   My educational objective is [specific skills]. This program is necessary for my career
     because [logic tied to current job and Pakistan labor market]. After completion, I intend
     to return to Pakistan to [employer / business plan], as confirmed in the letter from
     [Employer] dated [date].

4.   I have strong ties to Pakistan, including: (a) continuing employment with approved study
     leave; (b) [property/family]; and (c) [other]. I do not intend to immigrate to the
     United States on this application.

5.   I previously was refused under INA § 214(b) on [date]. Since then I have [material changes /
     additional evidence]. I respectfully submit that I qualify for F-1 classification.

I declare under penalty of perjury under the laws of the United States of America that the
foregoing is true and correct.

Executed on [date] at Lahore, Pakistan.


_________________________________
[FULL NAME]
""", s))

    story.append(Paragraph("TEMPLATE B — Form I-290B Legal Brief (Skeleton — AAO / Motion)", s["h2"]))
    story.append(mono("""
                    UNITED STATES DEPARTMENT OF HOMELAND SECURITY
                         U.S. CITIZENSHIP AND IMMIGRATION SERVICES
                              ADMINISTRATIVE APPEALS OFFICE
                                   [or originating office]

In the Matter of:                        )
                                         )    Form Type Denied: [I-129 / I-539 / etc.]
[FULL NAME],                             )    Receipt No.: [          ]
                                         )    Decision Date: [          ]
                  Applicant/Petitioner.  )


               BRIEF IN SUPPORT OF FORM I-290B
        [APPEAL TO THE AAO / MOTION TO REOPEN / MOTION TO RECONSIDER]


                                  I.   INTRODUCTION

1.   Applicant/Petitioner respectfully submits this brief in support of Form I-290B filed
     on [date]. The decision denying [Form] should be withdrawn because [one-sentence theory].

                               II.  STATEMENT OF FACTS

2.   [Chronology with exhibit citations, e.g., Ex. A–F.]

                            III.  STANDARD OF REVIEW

3.   [Cite 8 C.F.R. provisions governing motions/appeals; AAO de novo review as applicable.]

                                  IV.  ARGUMENT

A.   USCIS Erred as a Matter of Law
4.   [Precise regulation/statute misapplied — quote text — apply to facts.]

B.   USCIS Failed to Consider Relevant Evidence
5.   [Identify evidence in record ignored — materiality.]

C.   New Evidence Warrants Reopening (if MTR)
6.   [What is new, why previously unavailable, why outcome changes.]

                                  V.   CONCLUSION

7.   For the foregoing reasons, Applicant/Petitioner respectfully requests that the decision
     be withdrawn and the benefit granted, or the matter reopened and approved.

Respectfully submitted this ___ day of __________, 20__.


_________________________________
[FULL NAME], Self-Represented
[Address]
[Email] | [Telephone]
""", s))
    story.append(PageBreak())

    story.append(Paragraph("TEMPLATE C — Federal Complaint Caption &amp; Prayer (Mandamus/APA — Training Only)", s["h2"]))
    story.append(mono("""
                IN THE UNITED STATES DISTRICT COURT
            FOR THE [          ] DISTRICT OF [          ]


[FULL NAME],                               )
                                           )
                  Plaintiff,               )
                                           )    Civil Action No. _____________
      v.                                   )
                                           )
[SECRETARY OF HOMELAND SECURITY, et al.],  )
                                           )
                  Defendants.              )


                           COMPLAINT FOR DECLARATORY,
                      INJUNCTIVE, AND MANDAMUS RELIEF


                                 I.  INTRODUCTION

1.   Plaintiff brings this action to compel Defendants to perform nondiscretionary duties
     owed to Plaintiff under the Immigration and Nationality Act and the Administrative
     Procedure Act arising from unreasonable delay in adjudicating [benefit], Receipt No.
     [     ], pending since [date].

                        II.  JURISDICTION AND VENUE

2.   This Court has jurisdiction under 28 U.S.C. §§ 1331, 1361 and 5 U.S.C. §§ 701–706.
3.   Venue is proper under 28 U.S.C. § 1391(e).

                           III.  PARTIES

4–6. [Identify Plaintiff and agency Defendants with official capacity.]

                        IV.  STATEMENT OF FACTS

7–20. [Numbered factual allegations — dates, filings, inquiries, delay.]

                              V.  CLAIMS FOR RELIEF

Count I — Mandamus (28 U.S.C. § 1361)
Count II — APA Unreasonable Delay (5 U.S.C. § 706(1))
Count III — APA Arbitrary and Capricious Action (as applicable)

                           VI.  PRAYER FOR RELIEF

WHEREFORE, Plaintiff respectfully prays that this Court:
A.    Declare Defendants’ delay unlawful;
B.    Order Defendants to adjudicate the application within a fixed time;
C.    Award costs and such other relief as is just and proper.

                              Respectfully submitted,


                              _______________________________
                              [FULL NAME], Plaintiff Pro Se
                              [Address, Email, Telephone]
""", s))

    story.append(Paragraph("TEMPLATE D — Without-Prejudice Settlement / Mootness Letter", s["h2"]))
    story.append(settle_box(
        "Use after agency action moots a Mandamus/APA case, or to invite adjudication to avoid hearing.",
        s,
    ))
    story.append(mono("""
WITHOUT PREJUDICE

[Date]

Counsel for Defendants
[U.S. Attorney’s Office / Agency Counsel]
[Email]

Re:  [Case Caption], Case No. [     ]
     Proposal to Hold / Dismiss Upon Adjudication

Dear Counsel:

I am the pro se Plaintiff. The application at issue, Receipt No. [     ], remains pending.
To conserve judicial resources, I propose that Defendants complete adjudication within
[30/60] days. Upon written confirmation of a final decision, I will promptly file a
stipulation of dismissal under Fed. R. Civ. P. 41(a)(1)(A)(ii), with each party to bear
its own costs.

Please advise whether Defendants consent to a stipulated stay pending adjudication.

Respectfully,


_______________________________
[FULL NAME]
""", s))
    story.append(PageBreak())

    # PART 10 SOP
    story.append(Paragraph("PART 10 — TEAM SOPS, ETHICS, QUALITY GATES &amp; ASSESSMENT", s["h1"]))
    story.append(Paragraph("10.1 File Naming", s["h2"]))
    story.append(mono("""
CLIENT_SURNAME_US_Visa/
  00_Intake/
  01_Embassy_Refusal_CEAC/
  02_Reapplication_Pack/
  03_USCIS_I-290B/          (only if applicable)
  04_Federal_Court/         (only if jurisdiction-cleared)
  05_Settlement_Mootness/
  06_Outcome/
""", s))
    story.append(Paragraph("10.2 Quality Gates", s["h2"]))
    story.append(bullets([
        "<b>Gate 1:</b> Correctly classify consular vs USCIS decision.",
        "<b>Gate 2:</b> If § 214(b), reapplication pack complete—material change documented.",
        "<b>Gate 3:</b> If I-290B, deadline and correct Lockbox address verified by second officer.",
        "<b>Gate 4:</b> Federal court only after written jurisdiction memo (U.S.-qualified review).",
        "<b>Gate 5:</b> Settlement/mootness considered before any hearing.",
    ], s["bullet"]))
    story.append(Paragraph("10.3 Ethics Red Lines", s["h2"]))
    story.append(bullets([
        "Do not promise judicial reversal of § 214(b) consular refusals.",
        "Do not fabricate ties, employment, or financial documents.",
        "Do not file frivolous federal complaints to “pressure” the Embassy.",
        "Do not hold out as a U.S. attorney unless licensed and authorized.",
        "Give frank written advice when the case should wait or stop.",
    ], s["bullet"]))
    story.append(Paragraph("10.4 Assessment — Officer Is “U.S.-Ready” When They Can", s["h2"]))
    story.append(tbl(
        ["#", "Competency", "Pass"],
        [
            ["1", "Run Day-0 intake and identify 214(b) vs 221(g) vs USCIS denial", "[ ]"],
            ["2", "Build complete F-1 or B reapplication war file with Tabs A–I", "[ ]"],
            ["3", "Draft prior-refusal explanation letter in Times New Roman", "[ ]"],
            ["4", "Correctly refuse a request to “file JR on 214(b)” and explain why", "[ ]"],
            ["5", "Prepare I-290B packet with brief when denial notice allows", "[ ]"],
            ["6", "Demonstrate Lockbox address lookup and fee verification steps", "[ ]"],
            ["7", "Draft jurisdiction-screening memo before any federal complaint", "[ ]"],
            ["8", "Draft mootness/settlement letter for a delay case", "[ ]"],
            ["9", "Coach client for consular interview (truthful short answers)", "[ ]"],
            ["10", "Complete Scenario File to peer-review standard", "[ ]"],
        ],
        s, [0.5 * inch, 5.8 * inch, 0.8 * inch],
    ))
    story.append(PageBreak())

    # APPENDIX
    story.append(Paragraph("APPENDIX — FORMS INDEX &amp; OFFICIAL LINKS", s["h1"]))
    story.append(tbl(
        ["Form / Tool", "Use", "Where"],
        [
            ["DS-160", "Nonimmigrant visa application", "ceac.state.gov"],
            ["I-20 / SEVIS I-901", "F-1 school / fee", "School + fmjfee.com"],
            ["Form I-290B", "AAO appeal / USCIS motion", "uscis.gov/i-290b"],
            ["Form I-912", "Fee waiver (if eligible)", "uscis.gov/i-912"],
            ["Form G-1055", "Fee schedule reference", "uscis.gov/forms"],
            ["I-290B addresses", "Correct Lockbox", "uscis.gov/i-290b-addresses"],
            ["EOIR Payment Portal", "EOIR fees", "epay.eoir.justice.gov"],
            ["Federal court fees", "Complaint / PFR", "uscourts.gov + local clerk"],
            ["Travel.State.Gov", "Visa fees / reciprocity / 214(b) guidance", "travel.state.gov"],
        ],
        s, [1.8 * inch, 2.5 * inch, 2.8 * inch],
    ))
    story.append(Spacer(1, 0.2 * inch))
    story.append(box(
        "TRAINER DELIVERY PLAN",
        "Day 1 (3 hrs): Intake + consular nonreviewability + reapplication workshop (Scenario). "
        "Day 2 (3 hrs): I-290B lab + fee/filing drills + Times New Roman brief writing. "
        "Day 3 (2 hrs): Federal court jurisdiction screening + settlement/mootness role-play + assessment. "
        "Outcome: each officer produces a complete F-1 reapplication pack and a sample I-290B brief to peer-review standard.",
        s,
    ))
    story.append(Spacer(1, 0.35 * inch))
    story.append(Paragraph(
        "END OF MANUAL — U.S. Edition v1.0<br/>"
        "Typography: Times New Roman · Page size: U.S. Letter<br/>"
        "Verify all fees, forms, and jurisdictional rules before every real filing.",
        s["center"],
    ))

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=letter,
        leftMargin=0.85 * inch,
        rightMargin=0.85 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
        title="USA Visa Refusal Appeal Federal Court Training Manual",
        author="Internal Training",
    )
    doc.build(story, onFirstPage=hf, onLaterPages=hf)
    print(f"✓ {OUT}")
    print(f"  Size: {OUT.stat().st_size // 1024} KB")


if __name__ == "__main__":
    build()
