#!/usr/bin/env python3
"""
Professional AU/NZ Visa Refusal → Appeal → JR Training Manual PDF
Start-to-end from Embassy refusal in Pakistan. Self-represented client model.
"""

from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
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
NAVY = colors.HexColor("#0B1F33")
GOLD = colors.HexColor("#8A7048")
LIGHT = colors.HexColor("#F4F1EA")
SOFT = colors.HexColor("#E6E0D4")
GREEN = colors.HexColor("#1F5C3A")
RED = colors.HexColor("#7A1F1F")


def S():
    b = getSampleStyleSheet()
    return {
        "cover": ParagraphStyle("c", fontName="Helvetica-Bold", fontSize=20, leading=25,
                                textColor=NAVY, alignment=TA_CENTER, spaceAfter=10),
        "cover2": ParagraphStyle("c2", fontName="Helvetica", fontSize=11, leading=15,
                                 textColor=GOLD, alignment=TA_CENTER, spaceAfter=6),
        "h1": ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=13, leading=16,
                             textColor=NAVY, spaceBefore=12, spaceAfter=6),
        "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=11, leading=14,
                             textColor=NAVY, spaceBefore=9, spaceAfter=4),
        "h3": ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=10, leading=12,
                             textColor=GOLD, spaceBefore=7, spaceAfter=3),
        "body": ParagraphStyle("body", fontName="Helvetica", fontSize=9, leading=12,
                               alignment=TA_JUSTIFY, spaceAfter=5),
        "bullet": ParagraphStyle("bu", fontName="Helvetica", fontSize=9, leading=11.5,
                                 leftIndent=10, spaceAfter=2),
        "note": ParagraphStyle("note", fontName="Helvetica-Oblique", fontSize=8, leading=10.5,
                               textColor=RED, spaceBefore=3, spaceAfter=6),
        "settle": ParagraphStyle("set", fontName="Helvetica", fontSize=8.5, leading=11,
                                 textColor=GREEN, spaceBefore=3, spaceAfter=6),
        "mono": ParagraphStyle("mono", fontName="Courier", fontSize=7, leading=8.8,
                               backColor=SOFT, leftIndent=2, rightIndent=2, spaceBefore=3,
                               spaceAfter=6, borderPadding=5),
        "toc": ParagraphStyle("toc", fontName="Helvetica", fontSize=9, leading=13, leftIndent=6),
        "center": ParagraphStyle("ctr", fontName="Helvetica", fontSize=9, leading=12,
                                 alignment=TA_CENTER, spaceAfter=5),
        "th": ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=7.5, leading=9,
                             textColor=colors.white),
        "td": ParagraphStyle("td", fontName="Helvetica", fontSize=7.5, leading=9.5),
        "tt": ParagraphStyle("tt", fontName="Helvetica-Bold", fontSize=9, leading=11,
                             textColor=NAVY, spaceBefore=4, spaceAfter=3),
    }


def hf(c, doc):
    c.saveState()
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.5)
    c.line(1.6 * cm, A4[1] - 1.15 * cm, A4[0] - 1.6 * cm, A4[1] - 1.15 * cm)
    c.setFont("Helvetica", 7)
    c.setFillColor(colors.grey)
    c.drawString(1.6 * cm, A4[1] - 0.95 * cm, "AU/NZ Visa Refusal → Appeal → JR | Pakistan Team Training")
    c.drawRightString(A4[0] - 1.6 * cm, A4[1] - 0.95 * cm, "CONFIDENTIAL")
    c.line(1.6 * cm, 1.25 * cm, A4[0] - 1.6 * cm, 1.25 * cm)
    c.drawCentredString(A4[0] / 2, 0.85 * cm,
                        f"Page {doc.page} | Self-represented client model | Verify fees/forms before filing | Not legal advice")
    c.restoreState()


def bullets(items, style):
    return ListFlowable(
        [ListItem(Paragraph(i, style), leftIndent=6, value="•") for i in items],
        bulletType="bullet", start="•", leftIndent=8, bulletFontSize=8,
    )


def box(title, text, s, color=LIGHT, border=GOLD):
    t = Table(
        [[Paragraph(f"<b>{title}</b>", s["tt"])], [Paragraph(text, s["body"])]],
        colWidths=[17 * cm],
    )
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), color),
        ("BOX", (0, 0), (-1, -1), 0.7, border),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


def settle_box(text, s):
    return box("SETTLEMENT / NO-HEARING RESOLUTION FLAG", text, s,
               color=colors.HexColor("#E8F3EC"), border=GREEN)


def mono(text, s):
    return Preformatted(text.strip("\n"), s["mono"])


def tbl(headers, rows, s, widths):
    head = [Paragraph(h, s["th"]) for h in headers]
    body = [[Paragraph(c, s["td"]) for c in r] for r in rows]
    t = Table([head] + body, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
        ("GRID", (0, 0), (-1, -1), 0.35, SOFT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


def build():
    s = S()
    story = []

    # ===================== COVER =====================
    story.append(Spacer(1, 1.8 * cm))
    story.append(Paragraph("VISA REFUSAL TO FINAL RESOLUTION", s["cover"]))
    story.append(Paragraph("Australia &amp; New Zealand", s["cover2"]))
    story.append(Paragraph(
        "Complete Practice Manual for Pakistan Case Teams<br/>"
        "Embassy Refusal → Merits Appeal/Review → Judicial Review<br/>"
        "Self-Represented Client Model · Professional Drafting Pack",
        s["center"],
    ))
    story.append(Spacer(1, 0.4 * cm))
    meta = [
        ["Scope", "Student (Subclass 500) &amp; Visitor visa refusals from Australian/NZ posts in Pakistan — start to end"],
        ["Client model", "Client is self-represented at ART/IPT and Court. Team prepares the entire file; client signs and files."],
        ["Standard", "Senior practitioner drafting (15+ years migration litigation approach)"],
        ["Includes", "Full appeal submissions, full JR pleadings, fee schedules, payment methods, e-filing steps, settlement flags"],
        ["Version", "2.0 · July 2026 · Internal training — verify live fees/forms before every filing"],
    ]
    mt = Table(
        [[Paragraph(f"<b>{a}</b>", s["td"]), Paragraph(b, s["td"])] for a, b in meta],
        colWidths=[3.2 * cm, 13.8 * cm],
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
    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph(
        "<b>DISCLAIMER:</b> Educational internal training only. Not legal advice to any client. "
        "Fees cited are based on publicly notified schedules as at July 2026 and change periodically. "
        "Always confirm on art.gov.au, fcfcoa.gov.au, fedcourt.gov.au, justice.govt.nz and legislation.govt.nz "
        "on the day of filing. Pakistan team members must not hold out as Australian/NZ lawyers unless admitted.",
        s["note"],
    ))
    story.append(PageBreak())

    # TOC
    story.append(Paragraph("CONTENTS", s["h1"]))
    for line in [
        "PART 1 — Intake: Client walks in after Embassy refusal (Day 0)",
        "PART 2 — End-to-end pathway map &amp; settlement windows",
        "PART 3 — AUSTRALIA: ART merits review (full prepared file)",
        "PART 4 — AUSTRALIA: Judicial review (full prepared pleadings)",
        "PART 5 — NEW ZEALAND: IPT appeal + High Court leave/JR",
        "PART 6 — Fee schedules, payment methods &amp; filing methods",
        "PART 7 — Master Scenario Case File (Student + Visitor variants)",
        "PART 8 — Team SOPs, ethics, quality gates &amp; assessment",
        "APPENDIX — Document checklists &amp; official form index",
    ]:
        story.append(Paragraph(line, s["toc"]))
    story.append(PageBreak())

    # ===================== PART 1 INTAKE =====================
    story.append(Paragraph("PART 1 — INTAKE: CLIENT WALKS IN AFTER EMBASSY REFUSAL", s["h1"]))
    story.append(Paragraph(
        "The engagement begins the moment the client sits in your Lahore / Islamabad / Karachi office with an "
        "Australian or New Zealand <b>student or visitor visa refusal</b> from the Embassy/High Commission / processing office. "
        "You handle the matter from that moment until final resolution (grant, remittal success, or exhausted litigation).",
        s["body"],
    ))
    story.append(Paragraph("1.1 Same-day intake protocol (non-negotiable)", s["h2"]))
    story.append(bullets([
        "<b>Identity &amp; passport:</b> Bio page, all visas, travel history, previous refusals/cancellations.",
        "<b>Refusal package:</b> Full decision record / notification of refusal; PIC findings; GTE/Genuine Student reasons; visitor purpose findings; any s 57 natural justice letter and reply.",
        "<b>Application as lodged:</b> ImmiAccount/INZ portal PDF; Form 157A / visitor form; GTE statement; COE; financials; ties evidence; agent correspondence.",
        "<b>Deadlines:</b> Extract review/appeal rights paragraph word-for-word. Diary ART/IPT last day immediately.",
        "<b>Status:</b> Is client offshore (usual for Embassy refusal) or onshore? Bridging visa? Departure deadline?",
        "<b>Prospects conference (30–45 min):</b> Merits salvageable? Integrity issue (PIC 4020)? Character/health? Or thin case?",
        "<b>Engagement letter:</b> Self-represented model; team = drafting/coaching; client = litigant; costs estimate stages A–D.",
    ], s["bullet"]))
    story.append(box(
        "FIRST STRATEGIC QUESTION",
        "Do <b>not</b> jump to Judicial Review. Embassy refusal → almost always <b>merits review first</b> "
        "(Australia: ART if reviewable; New Zealand: IPT if appealable). JR is Stage 3 after Tribunal affirmance "
        "(or in limited NZ paths under s 247). Filing JR from an Embassy refusal without exhausting merits rights "
        "is usually incompetent and fatal.",
        s,
    ))
    story.append(Paragraph("1.2 Student vs Visitor — triage differences", s["h2"]))
    story.append(tbl(
        ["Issue", "Student (AU 500 / NZ student)", "Visitor (AU 600 / NZ visitor)"],
        [
            ["Core test", "Genuine Temporary Entrant / Genuine Student; enrolment; funds; ties", "Genuine temporary stay; purpose; incentives to return"],
            ["Typical refusal themes", "Career progression, home ties, funds, study history gaps", "Tourism purpose weak, overstay risk, prior refusals"],
            ["AU review body", "ART (migration) — many student refusals now <b>on the papers</b> (verify)", "ART if review rights stated on refusal"],
            ["NZ appeal body", "IPT where Act confers appeal right", "Often more limited — check refusal notice carefully"],
            ["Evidence rebuild", "New COE, academic plan, employer leave letter, assets, family ties", "Itinerary, leave letter, return ticket funds, property, dependents"],
        ],
        s, [3.2 * cm, 7 * cm, 6.8 * cm],
    ))
    story.append(PageBreak())

    # ===================== PART 2 PATHWAY =====================
    story.append(Paragraph("PART 2 — END-TO-END PATHWAY &amp; SETTLEMENT WINDOWS", s["h1"]))
    story.append(Paragraph("2.1 Australia pathway (Embassy refusal in Pakistan)", s["h2"]))
    story.append(mono("""
STAGE A  Embassy / Department refusal received
    ↓  [SETTLEMENT FLAG A1: rarely — only if obvious Department error → s 56/57 reopen request]
STAGE B  ART application for review (strict deadline on refusal letter — often 21/28 days)
    ↓  [SETTLEMENT FLAG B1: Minister may agree to remittal/consent orders if conceded error;
         FLAG B2: applicant withdraws if hopeless; FLAG B3: on-papers decision without oral hearing]
STAGE C  ART affirms refusal
    ↓
STAGE D  FCFCOA Div 2 Judicial Review within 35 days of ART decision
    ↓  [SETTLEMENT FLAG D1: Consent remittal before hearing if Minister concedes jurisdictional error;
         FLAG D2: Court-ordered mediation (fee may apply); FLAG D3: discontinue on terms]
STAGE E  Remittal → fresh ART → grant/refusal  OR  JR dismissed → consider appeal / stop
""", s))
    story.append(Paragraph("2.2 New Zealand pathway", s["h2"]))
    story.append(mono("""
STAGE A  INZ / Embassy decline
    ↓  [FLAG A1: request reconsideration only if policy allows — usually limited]
STAGE B  IPT appeal (where available) + fee — check appeal type & deadline on letter
    ↓  [FLAG B1: IPT may decide on papers; FLAG B2: withdrawal; FLAG B3: Ministerial intervention rare]
STAGE C  IPT dismisses
    ↓
STAGE D  High Court leave under s 249 (usually 28 days) → if leave granted → substantive JR
         OR s 247 JR if outside IPT path
    ↓  [FLAG D1: consent quashing/remittal; FLAG D2: discontinuance]
STAGE E  Remittal / appeal to Court of Appeal / stop
""", s))
    story.append(settle_box(
        "<b>Train every officer to pause at each FLAG.</b> Ask: Can we obtain a remittal, withdrawal on terms, "
        "or consent orders <b>without</b> a contested hearing? Document the advice and client instruction in writing. "
        "Settlement is often the best outcome for a self-represented client.",
        s,
    ))
    story.append(PageBreak())

    # ===================== PART 3 AU ART =====================
    story.append(Paragraph("PART 3 — AUSTRALIA: ART MERITS REVIEW (FULL PREPARED FILE)", s["h1"]))
    story.append(Paragraph("3.1 When ART is available", s["h2"]))
    story.append(Paragraph(
        "Open the refusal notification. If it states the decision is reviewable by the Administrative Review Tribunal "
        "and gives a deadline, that deadline is sacred. Offshore student and many visitor refusals commonly carry ART rights — "
        "<b>but always follow the letter</b>, not assumptions.",
        s["body"],
    ))
    story.append(Paragraph("3.2 Documents to lodge (ART pack)", s["h2"]))
    story.append(bullets([
        "Online ART application via ART digital services / approved lodgement channel (follow current art.gov.au instructions).",
        "Copy of Department refusal + decision record.",
        "Passport bio page; COE (student); evidence of funds; ties; GTE/Genuine Student statement (updated).",
        "Application fee payment confirmation (see Part 6).",
        "Appointment of representative form only if someone is authorised — for self-rep, leave blank / mark self.",
        "Later: written submissions + evidence bundle responding to Tribunal issues (especially for on-papers student reviews).",
    ], s["bullet"]))
    story.append(Paragraph("3.3 Professional ART written submissions — structure (use this every time)", s["h2"]))
    story.append(mono("""
ADMINISTRATIVE REVIEW TRIBUNAL
MIGRATION JURISDICTION

Applicant:              [FULL NAME]
Date of birth:          [DD/MM/YYYY]
Nationality:            Pakistan
Visa subclass:          [500 Student / 600 Visitor]
Department file / TRN:  [ ]
ART case number:        [once allocated]
Decision under review:  Refusal dated [ ] by [post/delegate]

WRITTEN SUBMISSIONS OF THE APPLICANT
(Self-represented — prepared with drafting assistance)

A. INTRODUCTION AND RELIEF SOUGHT
1. The Applicant seeks review of the decision to refuse [visa]. The correct or preferable
   decision is that the visa be granted.
2. These submissions address each reason for refusal and the applicable criteria in Schedule 2
   of the Migration Regulations 1994 and any applicable Ministerial Direction.

B. PROCEDURAL HISTORY
3. Application lodged [date] via ImmiAccount.
4. [Any s 56/57 natural justice letter and response dates].
5. Refusal notified [date]. ART application lodged [date] within time.

C. APPLICABLE LAW (keep tight — 1 page)
6. Set out the precise criteria in issue (e.g. cl 500.212 Genuine Student / Direction;
   or subclass 600 genuine temporary stay criteria). Quote the text. Do not paraphrase loosely.

D. RESPONSE TO EACH REFUSAL REASON (the heart of the case)
Reason 1 — [e.g. "career progression not logical"]
7. The delegate found [quote].
8. That finding is incorrect / incomplete because [facts].
9. Evidence: Tab [ ] Employment letter; Tab [ ] Academic plan; Tab [ ] Industry analysis.
10. Conclusion on Reason 1: criterion satisfied.

Reason 2 — [e.g. home ties]
11–14. Same structure: quote → answer → evidence → conclusion.

Reason 3 — [funds / purpose / overstay risk]
15–18. Same structure.

E. OVERALL EVALUATION
19. Weighing all circumstances, the Applicant is a genuine [student/visitor]. Incentives to
    return to Pakistan include [family, employment, property, business]. Study/visit purpose
    is specific, time-limited, and supported by documents.

F. ORDERS / OUTCOME SOUGHT
20. The Tribunal set aside the refusal and substitute a decision that the visa be granted;
    or remit with a direction that the Applicant meets [criteria].

Annexure Index: Tabs A–N (paginated).
""", s))
    story.append(settle_box(
        "<b>FLAG B1–B3 (ART stage):</b> (1) If Department/Minister identifies a clear legal error in the refusal "
        "during Tribunal proceedings, explore consent remittal. (2) If new evidence cures the only refusal ground "
        "(e.g. fresh COE + funds), push for favourable on-papers decision without oral hearing. "
        "(3) If case becomes hopeless (e.g. proven PIC 4020), advise withdrawal to save fee/cost exposure and protect future applications.",
        s,
    ))
    story.append(PageBreak())

    # ===================== PART 4 AU JR =====================
    story.append(Paragraph("PART 4 — AUSTRALIA: JUDICIAL REVIEW (FULL PREPARED PLEADINGS)", s["h1"]))
    story.append(Paragraph(
        "JR is filed only after ART affirms (typical case). Court: <b>Federal Circuit and Family Court of Australia (Division 2)</b>. "
        "Deadline: <b>35 days</b> from the date of the migration decision (ART). The Court reviews for <b>jurisdictional error</b> only.",
        s["body"],
    ))
    story.append(Paragraph("4.1 Court documents (filing set)", s["h2"]))
    story.append(tbl(
        ["Document", "Source", "Notes"],
        [
            ["Originating Application – Migration Act", "fcfcoa.gov.au (current form)", "Must name preparer; plead jurisdictional errors"],
            ["Affidavit of Applicant", "Court rules format", "Annex ART decision+reasons; key proof of error"],
            ["Annexures / exhibit bundle", "Your pagination", "Not a full merits dump"],
            ["Fee / reduced fee / exemption application", "FCFCOA / Federal Court fee pages", "Pay on eLodgment or apply hardship"],
            ["Later: Affidavit of Service", "After serving Minister", "Proof of service"],
            ["Outline of Submissions + List of Authorities", "As directed", "Short; ground-by-ground"],
            ["Court Book (if ordered)", "Practice direction", "Follow Migration CPD"],
        ],
        s, [5 * cm, 5.5 * cm, 6.5 * cm],
    ))
    story.append(Paragraph("4.2 Filing method (self-rep)", s["h2"]))
    story.append(bullets([
        "<b>Primary:</b> eLodge via Commonwealth Courts Portal / Federal Court eLodgment system as directed for migration matters (comcourts.gov.au / fedcourt eLodgment guidance).",
        "Create portal account in the <b>client’s name</b> (self-represented).",
        "Upload Originating Application + Affidavit + annexures in accepted PDF format; complete online fields.",
        "Pay filing fee by <b>card online</b> during lodgment, or lodge hardship/reduced-fee documents as prompted.",
        "If unable to eLodge: email the correct registry migration filing address (listed on fcfcoa.gov.au) — confirm current address before sending.",
        "After sealing: serve the Minister (usually via Australian Government Solicitor / address for service notified). File Affidavit of Service.",
    ], s["bullet"]))
    story.append(settle_box(
        "<b>FLAG D1–D3 (JR stage — no hearing):</b> After the Minister files a response / Court Book, the Minister’s lawyers "
        "sometimes concede a jurisdictional error. Typical no-hearing outcomes: "
        "<b>(a) consent orders</b> quashing ART decision and remitting; "
        "<b>(b) Court mediation</b> leading to remittal; "
        "<b>(c) discontinuance</b> with no order as to costs (negotiate). "
        "Team duty: after reading the Minister’s submissions, run a ‘concession prospects’ memo within 7 days.",
        s,
    ))
    story.append(PageBreak())

    story.append(Paragraph("4.3 FULL ORIGINATING APPLICATION GROUNDS — SCENARIO (PROFESSIONAL DRAFT)", s["h2"]))
    story.append(Paragraph(
        "Insert into the current FCFCOA Originating Application – Migration Act form fields. This is filing-ready language for training.",
        s["note"],
    ))
    story.append(mono("""
IN THE FEDERAL CIRCUIT AND FAMILY COURT OF AUSTRALIA (DIVISION 2)
REGISTRY: MELBOURNE

AYESHA KHAN                                                          Applicant
MINISTER FOR IMMIGRATION AND CITIZENSHIP                             Respondent

ORIGINATING APPLICATION – MIGRATION ACT

Details of migration decision
1. Decision maker: Administrative Review Tribunal
2. Date of decision: 2 June 2026
3. Decision: Affirmation of refusal of Subclass 500 (Student) visa

Orders sought
1. A writ of certiorari, or an order in the nature of certiorari, quashing the decision of the
   Administrative Review Tribunal made on 2 June 2026 in matter [ART NUMBER].
2. A writ of mandamus, or an order in the nature of mandamus, requiring the Tribunal
   (differently constituted) to determine the Applicant's application for review according to law.
3. Such further or other order as the Court considers appropriate.
4. Costs.

GROUNDS

Ground 1 — Constructive failure to exercise jurisdiction / failure to consider relevant material
1. The Tribunal was obliged to consider relevant material advanced by the Applicant in support of
   her claim to satisfy the Genuine Student / Genuine Temporary Entrant criteria, including material
   going to home ties and intention to return to Pakistan.
2. On 1 May 2026 the Tribunal directed the Applicant to provide further evidence concerning her
   employment and assets in Pakistan. On 15 May 2026, within time, the Applicant lodged:
   (a) an employer letter from [Employer] confirming ongoing employment and approved study leave; and
   (b) property ownership documents relating to [property], together with an index email.
3. That material was relevant to a central integer of the Tribunal's adverse reasoning on home ties
   and intention (Reasons at [41]-[52]).
4. On a fair reading of the Reasons, the Tribunal failed to consider that material. The Reasons do
   not refer to the 15 May 2026 lodgement, the employer letter, or the property documents, and
   contain no path of reasoning demonstrating engagement with them.
5. The failure was material. Had the material been considered, there is a realistic possibility that
   the Tribunal's home-ties / intention findings, and therefore the outcome, would have been different.

Ground 2 — Denial of procedural fairness
6. The Tribunal relied on adverse information, namely a LinkedIn profile printout and inferences
   drawn from it concerning an "unexplained career change" (Reasons at [33]-[36]).
7. Procedural fairness required that the Applicant be given notice of that adverse information and
   a meaningful opportunity to comment before it was used against her.
8. The Applicant was not provided with the LinkedIn printout prior to the Decision, nor invited to
   comment on the specific adverse inference ultimately drawn.
9. The breach was material. Comment from the Applicant could realistically have affected the
   Tribunal's assessment of career progression and genuineness.

Ground 3 — Misconstruction of the applicable criteria (alternative)
10. Further or alternatively, the Tribunal misconstrued the applicable Genuine Student / GTE framework
    by treating a desire for long-term international career mobility as necessarily inconsistent with
    satisfaction of the criteria, rather than undertaking the required evaluative assessment of all
    circumstances (Reasons at [55]-[58]).
11. That misconstruction caused the Tribunal to ask itself the wrong question and was material to
    the outcome.

Extension of time (only if applicable)
12. [If needed:] The Applicant seeks an extension of time under s 477 of the Migration Act 1958.
    The delay is [X] days. Explanation: [facts]. The grounds are reasonably arguable. Any prejudice
    to the Respondent is limited. It is in the interests of the administration of justice to extend time.

Prepared by: [Name] | Applicant signature: _____________ | Date: ________
""", s))
    story.append(PageBreak())

    story.append(Paragraph("4.4 FULL AFFIDAVIT — SCENARIO (PROFESSIONAL DRAFT)", s["h2"]))
    story.append(mono("""
AFFIDAVIT

I, Ayesha Khan, of House [ ], Street [ ], Lahore, Pakistan, Information Technology Professional,
affirm as follows:

1. I am the Applicant. I am self-represented. I make this affidavit from my own knowledge except
   where I state otherwise. Where I state information from documents, I believe it to be true.

2. I am a citizen of the Islamic Republic of Pakistan. Now produced and shown to me and marked
   "AK-1" is a true copy of the biodata page of my passport.

3. On [date] I applied for a Subclass 500 Student visa to undertake a Master of Information
   Technology at [Institution], Melbourne. Now produced and marked "AK-2" is a copy of the
   Confirmation of Enrolment current at the time of application / review.

4. On [date] a delegate of the Minister refused the visa. The notification and decision record
   are marked "AK-3".

5. I applied to the Administrative Review Tribunal for review within time. On 2 June 2026 the
   Tribunal affirmed the refusal. The Decision and Statement of Reasons are marked "AK-4".

6. On 1 May 2026 the Tribunal issued a direction requiring further evidence about my employment
   and assets. A copy is marked "AK-5".

7. On 15 May 2026 I lodged, by email to the Tribunal, an employer letter dated 15 May 2026 and
   property documents. Copies of the email and attachments are marked "AK-6" and "AK-7".

8. I have carefully read the Reasons. Paragraphs [41] to [52] deal with home ties and my intention
   to return to Pakistan. Those paragraphs do not refer to the employer letter or property documents
   lodged on 15 May 2026, nor to my email of that date.

9. At paragraphs [33] to [36] the Reasons refer to a LinkedIn profile and state that my career change
   is unexplained. I was not given a copy of that LinkedIn printout before the Decision. I was not
   invited to comment on that specific adverse inference. If asked, I would have explained [brief facts]
   and provided [documents]. A copy of the hearing invitation / relevant extract is marked "AK-8"
   [if available].

10. I respectfully seek the orders in the Originating Application. I believe the Tribunal made
    jurisdictional errors as set out in the Grounds.

11. [Extension facts if any — dates of receipt, illness, impecuniosity, steps taken.]

12. Drafting assistance for this affidavit was provided by [Firm/Team], Pakistan. They are not
    Australian legal practitioners on the record. I have read this affidavit and agree with its contents.

AFFIRMED by the deponent at Lahore on [date]
Before me: [Name, capacity — e.g. Notary Public / Oaths Officer as accepted]
Signature of deponent: __________________    Witness: __________________
""", s))
    story.append(PageBreak())

    # ===================== PART 5 NZ =====================
    story.append(Paragraph("PART 5 — NEW ZEALAND: IPT APPEAL + HIGH COURT LEAVE / JR", s["h1"]))
    story.append(Paragraph("5.1 From Embassy/INZ decline — first move", s["h2"]))
    story.append(bullets([
        "Read the decline letter for <b>appeal rights</b>, deadline, and IPT form type (residence vs temporary vs deportation — visitor/student rights vary).",
        "If IPT appeal exists: lodge form + fee within time (fee generally <b>cannot be waived</b>).",
        "If no IPT right: assess s 247 JR urgency (28 days) and whether any other pathway exists; do not invent IPT rights.",
    ], s["bullet"]))
    story.append(Paragraph("5.2 IPT lodging methods (self-rep from Pakistan)", s["h2"]))
    story.append(bullets([
        "<b>Email:</b> Send completed form + documents + proof of payment to ipt@justice.govt.nz; also send hard copy by courier/post as required. Filing date = email receipt date if hard copy follows rules.",
        "<b>File and Pay:</b> Pay fee online via Ministry of Justice File and Pay link on the IPT forms page.",
        "<b>Courier:</b> Level 1, 41 Federal St, Auckland (do not use ordinary post to that physical address).",
        "<b>Post:</b> DX EX 11086, Auckland (with proof of payment).",
        "<b>In person (if in NZ):</b> Tribunal or nearest court counter — EFTPOS/credit/debit/cash.",
    ], s["bullet"]))
    story.append(Paragraph("5.3 Professional IPT appeal submissions — skeleton of quality", s["h2"]))
    story.append(mono("""
IMMIGRATION AND PROTECTION TRIBUNAL
APPELLANT: [FULL NAME] | IPT REF: [ ] | VISA: [Student/Visitor]

STATEMENT OF EVIDENCE / SUBMISSIONS

1. Introduction — decision appealed; outcome sought (approve visa / remit to INZ).
2. Facts — chronology with document references.
3. Legal framework — cite Immigration Act 2009 provisions / immigration instructions applied.
4. Errors in INZ assessment — each decline reason answered with evidence.
5. Humanitarian / special circumstances (only if legally available on that appeal type).
6. Conclusion — why appeal should be allowed.

Evidence bundle: paginated, indexed, certified translations for Urdu documents.
""", s))
    story.append(Paragraph("5.4 After IPT dismissal — leave (s 249) / JR", s["h2"]))
    story.append(bullets([
        "Diary <b>28 days</b> from notification of IPT determination.",
        "File interlocutory application for leave + affidavit + draft statement of claim (High Court).",
        "Leave test: issues not adequately dealt with on appeal + general/public importance or other reason.",
        "If leave granted, Court states the issues — litigate only those issues.",
        "Service on Minister of Immigration / Crown as required; pay High Court filing fee.",
    ], s["bullet"]))
    story.append(settle_box(
        "<b>NZ settlement flags:</b> IPT on-papers determination; withdrawal; after leave application, "
        "Crown may consent to remittal if error is clear; High Court may encourage resolution without substantive hearing. "
        "Record every without-prejudice discussion carefully.",
        s,
    ))
    story.append(Paragraph("5.5 NZ Leave application — professional draft (training)", s["h2"]))
    story.append(mono("""
IN THE HIGH COURT OF NEW ZEALAND  [CITY] REGISTRY
CIV-[ ]-[ ]

UNDER the Immigration Act 2009 and the Judicial Review Procedure Act 2016
BETWEEN [NAME] Applicant AND MINISTER OF IMMIGRATION Respondent

INTERLOCUTORY APPLICATION FOR LEAVE TO BRING REVIEW PROCEEDINGS (s 249)

The Applicant applies for orders that:
(a) leave be granted under s 249 to bring review proceedings in respect of the Immigration and
    Protection Tribunal determination dated [date], notified on [date], reference [IPT ref];
(b) the issues for review be:
    Issue 1 — Whether the Tribunal failed to consider relevant evidence lodged on [date] regarding
              [home ties / bona fides / funds], thereby erring in law / failing to take into account
              relevant considerations;
    Issue 2 — Whether the Tribunal breached natural justice by relying on [adverse material] without
              giving the Applicant an opportunity to comment;
(c) costs be reserved.

Grounds
1. The proposed issues concern the legality of the Tribunal's process and reasoning and could not be
   adequately remedied merely by disagreeing with the Tribunal's factual weighing on appeal.
2. The issues ought to be submitted for review because they disclose an arguable and material error
   with significant consequences for the Applicant, and because [public importance / recurring issue].
3. This application is made within 28 days of notification (proof annexed to supporting affidavit).

Reliance: ss 247–249 Immigration Act 2009; Judicial Review Procedure Act 2016; affidavit of [Name].

Date: ____    Signature of Applicant: ______________________
""", s))
    story.append(PageBreak())

    # ===================== PART 6 FEES & FILING =====================
    story.append(Paragraph("PART 6 — FEE SCHEDULES, PAYMENT &amp; FILING METHODS", s["h1"]))
    story.append(Paragraph(
        "Figures below reflect publicly reported schedules around <b>1 July 2025 / 1 July 2026</b> updates. "
        "<b>Re-check on filing day.</b> Payment date can determine which fee applies.",
        s["note"],
    ))
    story.append(Paragraph("6.1 Australia — ART (merits review)", s["h2"]))
    story.append(tbl(
        ["Item", "Fee (AUD)", "Payment / filing method"],
        [
            ["Reviewable migration decision (typical student/visitor review)", "$3,727 (from 1 Jul 2026; was $3,580)", "Pay via ART online payment when lodging; card; follow art.gov.au"],
            ["Financial hardship reduction", "Often 50% if approved", "Lodge hardship request with evidence as ART form requires"],
            ["Concessional circumstances fee", "$100 (limited categories)", "Only if ART criteria met"],
            ["Protection review fee", "$2,293 (usually if unsuccessful)", "Different scheme — not typical student/visitor"],
        ],
        s, [5.5 * cm, 5 * cm, 6.5 * cm],
    ))
    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph("6.2 Australia — FCFCOA migration JR fees", s["h2"]))
    story.append(tbl(
        ["Item", "Fee (AUD)", "Payment / filing method"],
        [
            ["Filing application (migration JR) item 201A", "Full ~$4,180 from 1 Jul 2026 (was $4,015); Reduced ~$2,090 (was $2,005)", "Pay online on Commonwealth Courts Portal / eLodgment by card"],
            ["Reduced fee (s 2.06A hardship)", "Registrar determination required", "File financial hardship documents with application"],
            ["Setting down for hearing (individual)", "Check live schedule (~$995 band historically)", "Invoiced / payable as Court directs"],
            ["Daily hearing fee after day 1", "Check live schedule", "As directed"],
            ["Mediation by court officer", "Check live schedule (~$665 historically)", "Settlement opportunity — see flags"],
            ["Cheque / money order (if used)", "Payable to Federal Court of Australia", "Confirm registry still accepts; e-pay preferred"],
        ],
        s, [5.5 * cm, 5.5 * cm, 6 * cm],
    ))
    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph("6.3 New Zealand — IPT + High Court", s["h2"]))
    story.append(tbl(
        ["Item", "Fee (NZD)", "Payment / filing method"],
        [
            ["IPT residence / certain deportation appeals", "$943 incl. GST (as at 1 Jul 2025 schedule; confirm live)", "File and Pay online; or court counter EFTPOS/credit/debit/cash"],
            ["Refugee/protected person IPT appeal", "No fee", "Lodge form per IPT rules"],
            ["IPT fee waiver", "Generally <b>not available</b>", "Must pay or appeal not accepted"],
            ["High Court JR / originating civil filing", "Confirm live MoJ fee schedule (commonly several hundred NZD)", "Court fee counter / online channels as directed"],
        ],
        s, [5.5 * cm, 5.5 * cm, 6 * cm],
    ))
    story.append(Spacer(1, 0.25 * cm))
    story.append(Paragraph("6.4 How to e-file — Australia JR (step card for team)", s["h2"]))
    story.append(bullets([
        "Step 1: Client creates Commonwealth Courts Portal / eLodgment account (email + ID).",
        "Step 2: Select Federal Circuit and Family Court — migration originating application.",
        "Step 3: Enter parties: Applicant = client; Respondent = Minister (correct current title).",
        "Step 4: Upload PDFs: Application, Affidavit, exhibits (file size limits — split if needed).",
        "Step 5: Pay fee by Visa/Mastercard (or upload hardship application).",
        "Step 6: Save lodgment receipt + sealed documents PDF.",
        "Step 7: Serve sealed pack on Minister’s address for service; complete Affidavit of Service and eLodge it.",
        "Step 8: Diary first court date from listing notice.",
    ], s["bullet"]))
    story.append(Paragraph("6.5 How to file — NZ IPT (step card)", s["h2"]))
    story.append(bullets([
        "Step 1: Download correct IPT appeal form + guide from justice.govt.nz IPT pages.",
        "Step 2: Complete form in English; attach decline letter and evidence index.",
        "Step 3: Pay fee via File and Pay; print/save receipt.",
        "Step 4: Email ipt@justice.govt.nz with form, documents, receipt; courier/post hard copy as required.",
        "Step 5: Keep email send proof and tracking; diary IPT timetable.",
    ], s["bullet"]))
    story.append(PageBreak())

    # ===================== PART 7 SCENARIO MASTER FILE =====================
    story.append(Paragraph("PART 7 — MASTER SCENARIO CASE FILE", s["h1"]))
    story.append(Paragraph("7.1 Client walks in — facts", s["h2"]))
    story.append(Paragraph(
        "<b>Ms Ayesha Khan</b>, 27, Lahore. IT support executive at [TechCo]. On 10 April 2026 the Australian "
        "visa office refuses her offshore Subclass 500 application for a 2-year Master of IT in Melbourne. "
        "Refusal grounds: not a Genuine Student — (i) career progression illogical; (ii) insufficient home ties; "
        "(iii) funds path unclear. Refusal letter states ART review rights and a deadline of <b>21 days</b> "
        "(training assumption — always use the letter). She attends your office on <b>12 April 2026</b> with the refusal printout.",
        s["body"],
    ))
    story.append(Paragraph("7.2 Stage plan you open that day", s["h2"]))
    story.append(tbl(
        ["Stage", "Action", "Deadline", "Fee"],
        [
            ["A Intake", "Conflict check, engagement, scan file, diary ART day", "Same day", "Professional fee (your retainer)"],
            ["B ART lodge", "Online ART application + fee + refusal upload", "Before ART last day", "AUD 3,727 (or hardship)"],
            ["C Evidence rebuild", "New GTE statement, employer leave, property, funds, COE", "Within ART directions", "—"],
            ["D ART submissions", "Full written submissions (Part 3 template)", "As directed / on-papers invite", "—"],
            ["E ART outcome", "If win → visa path; if lose → JR clock", "Decision date = Day 0 for JR", "—"],
            ["F JR", "FCFCOA application + affidavit within 35 days", "Day 35", "AUD ~4,180 / reduced ~2,090"],
            ["G Settlement watch", "Consent remittal memo after Minister’s response", "Ongoing", "Possible mediation fee"],
        ],
        s, [2.8 * cm, 6.2 * cm, 4 * cm, 4 * cm],
    ))
    story.append(Spacer(1, 0.25 * cm))
    story.append(Paragraph("7.3 Visitor visa variant (same office visit)", s["h2"]))
    story.append(Paragraph(
        "<b>Mr Bilal Ahmed</b>, visitor (subclass 600) refused for not being a genuine temporary entrant — "
        "weak itinerary, insufficient ties, prior overstay by relative cited. Same intake discipline. "
        "Rebuild: employer leave letter, property, family dependents, prepaid itinerary, return funds, "
        "explanation distinguishing relative’s history. ART if rights exist; JR only after ART affirmance "
        "with jurisdictional error (e.g. irrelevant consideration of relative’s conduct without logical connection).",
        s["body"],
    ))
    story.append(Paragraph("7.4 ART submissions excerpt — professional quality (student scenario)", s["h2"]))
    story.append(mono("""
D. RESPONSE TO REASON 1 — "Career progression not logical"

19. The delegate found that moving from IT support to a Master of Information Technology was not
    a logical progression (Decision Record at p 4).

20. That finding gives insufficient weight to the Applicant's evidence that:
    (a) her current role is limited to tier-1 support without a pathway to systems analysis;
    (b) the nominated Master's specialisation in [field] is directly aligned to her employer's
        documented workforce plan; and
    (c) she holds a confirmed study-leave and return-to-role letter dated 15 May 2026 (Tab E).

21. A desire to upskill in a cognate discipline is consistent with the Genuine Student criterion.
    International study for a time-limited Master's, with a job to return to, supports rather than
    undermines genuineness.

22. The Tribunal should find Reason 1 is not a proper basis for refusal.
""", s))
    story.append(Paragraph("7.5 Evidence index (ART + later JR)", s["h2"]))
    story.append(tbl(
        ["Tab", "Document", "Stage used"],
        [
            ["A", "Passport biodata", "ART + JR"],
            ["B", "Refusal notification + decision record", "ART + JR"],
            ["C", "ImmiAccount application PDF + GTE as lodged", "ART"],
            ["D", "COE + offer letter + course outline", "ART"],
            ["E", "Employer letter + study leave + organogram", "ART + JR Ground 1"],
            ["F", "Property documents + Fard/registry extract + translation", "ART + JR Ground 1"],
            ["G", "Bank statements / education loan / sponsor affidavit", "ART"],
            ["H", "Updated Genuine Student statement (signed)", "ART"],
            ["I", "Family composition / dependents evidence", "ART"],
            ["J", "ART decision + reasons", "JR"],
            ["K", "Tribunal direction + 15 May lodgement email", "JR Ground 1"],
            ["L", "LinkedIn adverse material / hearing extracts", "JR Ground 2"],
        ],
        s, [1.5 * cm, 10 * cm, 5.5 * cm],
    ))
    story.append(PageBreak())

    story.append(Paragraph("7.6 Outline of JR submissions — professional (hearing or consent negotiations)", s["h2"]))
    story.append(mono("""
OUTLINE OF SUBMISSIONS OF THE APPLICANT

I. Introduction
1. This is an application under s 476 of the Migration Act 1958 for judicial review of the ART
   decision dated 2 June 2026 affirming refusal of a Subclass 500 visa.
2. The Applicant is self-represented. The real issues are Grounds 1 and 2; Ground 3 is alternative.

II. Applicable principles
3. Jurisdictional error includes constructive failure to exercise jurisdiction by failing to consider
   relevant material / integers of claims, and denial of procedural fairness.
4. Materiality: a realistic possibility of a different outcome (Applicant relies on High Court authority
   as current — update List of Authorities before filing).

III. Ground 1 — failure to consider relevant material
5. The home-ties integer was live and decisive (Reasons [41]-[52]).
6. Material responsive to the Tribunal's own direction was lodged on 15 May 2026 (CB Tabs K, E, F).
7. Absence of reference or engagement in the Reasons is not a mere drafting omission; it is a failure
   to perform the statutory task.
8. Materiality is plain: the Tribunal's adverse conclusion turned on home ties.

IV. Ground 2 — procedural fairness
9. Adverse LinkedIn material at Reasons [33]-[36] was used to support an unexplained career-change finding.
10. Fairness required disclosure and an opportunity to comment. Neither occurred.
11. The error was material to genuineness reasoning.

V. Relief
12. Quash; remit to ART differently constituted; costs.

LIST OF AUTHORITIES (attach separately — keep to essentials; update to current law).
""", s))
    story.append(settle_box(
        "<b>Scenario settlement playbook:</b> After the Court Book is prepared, send (via proper channel / or invite "
        "Minister’s solicitors to consider) a short without-prejudice letter identifying Ground 1 pinpoints. "
        "Offer consent remittal with no order as to costs. Many matters resolve here <b>without hearing</b> if the silence "
        "in reasons is indefensible. If refused, proceed to hearing with the Outline above.",
        s,
    ))
    story.append(PageBreak())

    # ===================== PART 8 SOPs =====================
    story.append(Paragraph("PART 8 — TEAM SOPs, ETHICS, QUALITY GATES &amp; ASSESSMENT", s["h1"]))
    story.append(Paragraph("8.1 File stages naming convention", s["h2"]))
    story.append(mono("""
CLIENT_SURNAME_Visa_Country/
  00_Intake/
  01_Embassy_Refusal/
  02_ART_or_IPT_Appeal/
     Application/
     Evidence_Tabs/
     Submissions/
     Correspondence/
  03_Tribunal_Decision/
  04_Judicial_Review/
     Application_Affidavit/
     Service/
     Court_Book/
     Submissions/
     Settlement_Without_Prejudice/
  05_Outcome_Remittal_or_Appeal/
""", s))
    story.append(Paragraph("8.2 Quality gates (cannot skip)", s["h2"]))
    story.append(bullets([
        "<b>Gate 1 (ART/IPT lodge):</b> Deadline correct? Fee paid? Refusal attached? Client signed truth statement?",
        "<b>Gate 2 (Submissions):</b> Every refusal reason answered? Tabs match footnotes? Translations certified?",
        "<b>Gate 3 (JR):</b> Is this jurisdictional error or merits complaint? Pinpoints to reasons? Day-35 safe?",
        "<b>Gate 4 (Settlement):</b> Concession memo done after Respondent’s documents?",
        "<b>Gate 5 (Hearing):</b> Client coached; Outline final; authorities citechecked.",
    ], s["bullet"]))
    story.append(Paragraph("8.3 Ethics red lines", s["h2"]))
    story.append(bullets([
        "No false documents; no coaching untruths; no undisclosed paid agents onshore breaching AU/NZ law.",
        "Frank written advice if prospects poor — especially PIC 4020 / integrity.",
        "Do not file JR only as a delay tactic without arguable error.",
        "Clear retainer: self-rep; Pakistan team not on Court record as AU/NZ solicitors unless true.",
    ], s["bullet"]))
    story.append(Paragraph("8.4 Assessment — team member is ‘JR ready’ when they can", s["h2"]))
    story.append(tbl(
        ["#", "Task", "Pass"],
        [
            ["1", "Run Day-0 intake on a live Embassy refusal and diary correct ART/IPT deadline", "[ ]"],
            ["2", "Build a full ART evidence index and fee payment pack", "[ ]"],
            ["3", "Draft ART submissions answering each refusal ground with tabs", "[ ]"],
            ["4", "Spot three true jurisdictional errors in a sample ART decision", "[ ]"],
            ["5", "Produce filing-ready Originating Application + Affidavit for scenario", "[ ]"],
            ["6", "Demonstrate portal eLodgment steps + fee payment path (sandbox/demo)", "[ ]"],
            ["7", "Write a without-prejudice consent remittal letter (settlement flag)", "[ ]"],
            ["8", "Coach client for 10-minute self-rep oral roadmap", "[ ]"],
            ["9", "Complete NZ IPT lodgment + File and Pay checklist", "[ ]"],
            ["10", "Draft NZ s 249 leave application with stated issues", "[ ]"],
        ],
        s, [1.2 * cm, 13.5 * cm, 2.3 * cm],
    ))
    story.append(PageBreak())

    # EXTRA PROFESSIONAL PACKS
    story.append(Paragraph("PART 7B — FULL ART WRITTEN SUBMISSIONS (SCENARIO — FILING QUALITY)", s["h1"]))
    story.append(Paragraph(
        "Use as the model answer in training. Replace bracketed facts. This is the standard your team must meet.",
        s["note"],
    ))
    story.append(mono("""
ADMINISTRATIVE REVIEW TRIBUNAL — MIGRATION JURISDICTION
Applicant: Ayesha Khan | DOB: [ ] | Pakistan | Subclass 500
Department TRN: [ ] | ART Number: [ ]
Decision under review: Refusal dated 10 April 2026

WRITTEN SUBMISSIONS OF THE APPLICANT (Self-represented)

A. INTRODUCTION
1. The Applicant seeks review of the decision to refuse her Subclass 500 Student visa. The correct
   or preferable decision is that she satisfies the Genuine Student / applicable GTE criteria and
   that the visa be granted, or that the matter be remitted with appropriate directions.
2. The Applicant is offshore in Lahore, Pakistan, and is self-represented. She relies on the evidence
   indexed at Tabs A–I.

B. PROCEDURAL HISTORY
3. Application lodged via ImmiAccount on [date] with COE for Master of Information Technology at
   [Institution] (Tab D).
4. Refusal notified on 10 April 2026 (Tab B). ART application lodged on [date] within time, fee paid.

C. APPLICABLE CRITERIA
5. The criteria in issue are those identified in the Decision Record concerning whether the Applicant
   is a genuine applicant for entry and stay as a student. The Tribunal must evaluate all circumstances,
   including the Applicant's circumstances in Pakistan, potential circumstances in Australia, the value
   of the course, the Applicant's immigration history, and any other relevant matter (as framed by the
   applicable Direction / regulations in force — attach extract as Tab Law-1).

D. REASON 1 — CAREER PROGRESSION
6. The delegate found the proposed study was not a logical progression from IT support work (Tab B p.4).
7. That finding should be rejected. The Applicant's role is tier-1 support without a pathway into systems
   analysis (Tab E employment letter; Tab H statement [paras 8-14]). The Master's specialisation is
   aligned to her employer's workforce plan and her approved study leave and return-to-role undertaking
   (Tab E). Upskilling within the same broad discipline for a finite course is consistent with genuineness.
8. Conclusion: Reason 1 does not justify refusal.

E. REASON 2 — HOME TIES
9. The delegate found home ties were weak (Tab B p.5).
10. The Applicant has continuous employment, approved leave, property interests in Lahore (Tabs E–F),
    and dependent family circumstances set out in Tab I. These are strong incentives to return.
11. Conclusion: Reason 2 should not be sustained.

F. REASON 3 — FUNDS
12. The Decision Record doubted the funds path (Tab B p.6). Tab G demonstrates capacity to meet course
    fees and living costs from salary savings and [sponsor/loan] with a clear trail of funds.
13. Conclusion: financial capacity is established.

G. OVERALL
14. Weighing all circumstances, the Applicant is a genuine student. The Tribunal should set aside the
    refusal and substitute a decision that the visa be granted, or remit for finalisation.

Annexure Index: Tabs A–I (paginated PDF).
Date: ____    Signature of Applicant: ____________________
""", s))
    story.append(PageBreak())

    story.append(Paragraph("PART 7C — WITHOUT-PREJUDICE CONSENT REMITTAL LETTER (NO HEARING)", s["h1"]))
    story.append(settle_box(
        "Send only after JR is on foot and Court Book / Reasons silence is clear. Mark WITHOUT PREJUDICE. "
        "This is a primary <b>settlement-without-hearing</b> tool.",
        s,
    ))
    story.append(mono("""
WITHOUT PREJUDICE SAVE AS TO COSTS

[Date]

Australian Government Solicitor / Solicitors for the Minister
By email: [address for service]

Dear Colleagues

Khan v Minister — FCFCOA(Div2) [file number]
Proposal for consent remittal

1. I am the self-represented Applicant.

2. The Tribunal's Reasons at [41]-[52] deal with home ties / intention but do not refer to, or engage with,
   the employer letter and property documents lodged on 15 May 2026 in response to the Tribunal's direction
   of 1 May 2026 (Court Book Tabs [ ]).

3. In my respectful submission that silence discloses a jurisdictional error (failure to consider relevant
   material) that is material to the outcome.

4. To avoid further costs and a hearing, I propose consent orders substantially as follows:
   (a) the decision of the Administrative Review Tribunal made on 2 June 2026 be quashed;
   (b) the matter be remitted to the Tribunal (differently constituted) for determination according to law;
   (c) no order as to costs.

5. Please let me know within 14 days whether the Minister consents. I remain ready to attend any
   case management listing.

Yours faithfully
Ayesha Khan
[Email] [Phone] [Postal address]
""", s))

    story.append(Paragraph("PART 7D — VISITOR VISA JR GROUNDS EXCERPT (BILAL AHMED)", s["h1"]))
    story.append(mono("""
Ground 1 — Irrelevant consideration / illogical use of third-party immigration history
1. The Tribunal treated the overstay of the Applicant's cousin as supporting a finding that the Applicant
   himself intends to overstay (Reasons at [27]-[30]).
2. Absent findings linking the cousin's conduct to the Applicant's own intentions, that reasoning was
   legally irrelevant / illogical and caused the Tribunal to exceed / constructively fail to exercise
   its jurisdiction.
3. The error was material to the genuine temporary stay conclusion.

Ground 2 — Failure to consider relevant ties material
4. The Tribunal failed to consider the Applicant's employer leave letter and property documents lodged
   on [date] (CB Tabs [ ]), which were relevant to incentives to return.
5. Materiality follows from the Tribunal's adverse "weak ties" finding at [31]-[35].
""", s))
    story.append(PageBreak())

    # APPENDIX
    story.append(Paragraph("APPENDIX — DOCUMENT CHECKLISTS &amp; OFFICIAL FORM INDEX", s["h1"]))
    story.append(Paragraph("A. Embassy refusal → ART (Australia) checklist", s["h2"]))
    story.append(bullets([
        "[ ] Refusal letter + decision record",
        "[ ] ART online application submitted",
        "[ ] Fee paid / hardship lodged — receipt saved",
        "[ ] Passport, COE/itinerary, funds, ties, updated statement uploaded",
        "[ ] Calendar: ART directions + on-papers submission date",
        "[ ] Settlement review after Department brief arrives",
    ], s["bullet"]))
    story.append(Paragraph("B. ART affirm → JR checklist", s["h2"]))
    story.append(bullets([
        "[ ] Day-35 calculation dual-checked",
        "[ ] Current Originating Application – Migration Act downloaded",
        "[ ] Affidavit sworn/affirmed in acceptable form",
        "[ ] Fee paid or reduced-fee documents filed",
        "[ ] eLodgment receipt + sealed docs",
        "[ ] Service on Minister + Affidavit of Service",
        "[ ] Concession/settlement memo scheduled",
    ], s["bullet"]))
    story.append(Paragraph("C. Official sources (bookmark)", s["h2"]))
    story.append(bullets([
        "ART: https://www.art.gov.au",
        "FCFCOA migration apply/fees/filing: https://www.fcfcoa.gov.au",
        "Federal Court eLodgment / Form 70 (if FCA jurisdiction): https://www.fedcourt.gov.au",
        "Commonwealth Courts Portal: https://www.comcourts.gov.au",
        "NZ IPT forms &amp; fees: https://www.justice.govt.nz/tribunals/immigration/",
        "NZ legislation (ss 247, 249): https://www.legislation.govt.nz",
    ], s["bullet"]))
    story.append(Spacer(1, 0.4 * cm))
    story.append(box(
        "TRAINER DELIVERY PLAN (UPDATED)",
        "Day 1 (3h): Intake + ART full drafting workshop on Scenario. "
        "Day 2 (3h): Fees/filing labs + JR pleadings workshop. "
        "Day 3 (2h): Settlement negotiation role-play + NZ IPT/leave + assessment sign-off. "
        "Outcome: each officer produces a complete Scenario filing pack (ART + JR) to peer-review standard.",
        s,
    ))
    story.append(Spacer(1, 0.5 * cm))
    story.append(Paragraph(
        "END OF MANUAL v2.0 — Verify all fees, forms, and practice directions before every real filing.",
        s["center"],
    ))

    doc = SimpleDocTemplate(
        str(OUT), pagesize=A4,
        leftMargin=1.6 * cm, rightMargin=1.6 * cm,
        topMargin=1.7 * cm, bottomMargin=1.7 * cm,
        title="AU NZ Visa Refusal Appeal JR Practice Manual v2",
        author="Internal Training",
    )
    doc.build(story, onFirstPage=hf, onLaterPages=hf)
    print(f"✓ {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    build()
