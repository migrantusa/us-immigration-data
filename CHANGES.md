# What changed in US immigration data

A dated record of changes to US government immigration data, each verified
against its primary source. Government agencies publish the *current* value and
overwrite it; this file keeps the change itself.

**This page is generated** from [`data/change_log.json`](data/change_log.json)
(machine-readable, with the Spanish text and the affected dataset paths) by
[`scripts/refresh.py`](scripts/refresh.py). Canonical human-readable version, with
full context on each entry: <https://migrantusa.com/updates/>

Showing the 40 most recent of 103 recorded changes. Source data as of 2026-09-05.

---

### 2026-09-09 · TAXES

**Proposed: Census Bureau would use tax records to set your "usual residence" and would not count most noncitizens for apportionment**

The Census Bureau filed a proposed rule on September 9, 2026 (FR document 2026-18481, docket USBC-2026-0628), scheduled to publish September 10. Proposed 15 CFR 60.2(a) would define "usual residence" as the residence at which they "have lawfully spent the greatest number of days," and says it "should be consistent with, and evidenced by, their tax records (e.g., tax returns, W-2 forms)." Proposed 15 CFR 60.4 governs foreign citizens in the United States: those who are also US citizens or lawful permanent residents would be counted at their usual residence, and "all other citizens of foreign countries" are "not counted for apportionment"; the preamble proposes excluding "illegal aliens and aliens whose legal status is less durable and indefinite in length than lawful permanent resident status," and invites comment on whether other statuses are materially similar to LPR status. It also asks whether to add a legal-status question to the questionnaire. This is a proposal and nothing in it is in effect; it does not change anyone's obligation to file. Census responses stay confidential under 13 U.S.C. 9, which the rule does not amend and in fact relies on. Comments are due 30 days after publication; the filed text carries a placeholder rather than a printed date, so we are not publishing a computed deadline — check the published notice or the docket. Our taxes guide now carries this in both languages.

Primary source: <https://www.federalregister.gov/public-inspection/2026-18481/decennial-census-of-the-population-of-americans-proposed-residence-criteria-and-proposed-regulations>

### 2026-09-09 · LITIGATION

**Correction: our CHNV parole page pointed readers at the wrong proceeding — the Family Reunification Parole injunction is under appeal**

Our CHNV humanitarian parole page told readers to watch a district-court summary-judgment motion, and said nothing about the appeal of the preliminary injunction that is the only thing currently blocking termination of Family Reunification Parole and its work authorization. That was the wrong milestone to hand someone whose work permit depends on it. What the docket actually shows: the government appealed to the First Circuit as Doe v. Mullin, Nos. 26-1314 and 26-1628 (the second docketed June 4, 2026 on notice of appeal doc. #304); on July 28, 2026 the court ordered the two consolidated for briefing and oral argument; and on July 29 it set the schedule, with the appellants' brief and appendix due September 8, 2026, the appellees' brief 30 days after service, and the reply 21 days after that. Merits briefing is underway now. We do not claim to know what happened on or after September 8: the public docket reproduction we can read was last retrieved July 29, 2026 and RECAP's newest entry is August 11, 2026, so neither shows whether the brief was filed on time or extended — the page says exactly that. The district-court motion remains fully briefed since December 8, 2025 with no ruling docketed. The FRP injunction remains in effect. Both language versions and the case dataset now carry the appeal, its docket numbers, the consolidation, the schedule and that limitation. Shipped alongside: the third-country-removals case now names its First Circuit docket (No. 26-1212, D.V.D. v. DHS, argued May 13, 2026) instead of "expedited appeal"; the DACA timeline records the July 10, 2026 order that is the newest entry on Judge Hanen's docket; and a Spanish-wording sweep replaced "por improcedente" with "por haber quedado sin objeto" in six places across four cases, because the first loses the mootness rationale and reads as a rejection on the merits.

Primary source: <https://dockets.justia.com/docket/circuit-courts/ca1/26-1628>

### 2026-09-08 · TPS

**Correction: USCIS DID act on Executive Order 14418 — we said it had published nothing, on 28 pages**

Twenty-eight pages (14 EN + 14 ES) stated that USCIS, the Social Security Administration and the Justice Department "had published nothing as of September 5, 2026" about Executive Order 14418. That was false when we wrote it. DHS filed an interim final rule on September 4, 2026 at 4:15 pm EDT (FR doc 2026-18345, publishing September 9), and USCIS announced it the same day. The rule replaces "foreign diplomatic officer" with the broader "foreign government employee" — expressly covering embassy and consulate employees who are nationals of that country, which is our consulate audience — and lets such children register as lawful permanent residents. It is effective September 4, 2026 and applies only to children born on or after that date; it also updates Forms I-485 and G-325R. Critically, and this is the part that most protects readers: DHS states it will NOT implement the rule against members of the certified class in Casa Inc. v. Trump, No. 8:25-cv-00201 (D. Md.), while that preliminary injunction stands. All 28 pages now carry the rule, its effective date and scope, and the injunction carve-out. SSA and DOJ have still published nothing. Comments on the rule close about October 4, 2026.

Primary source: <https://www.uscis.gov/newsroom/alerts/dhs-announces-rule-for-certain-children-born-in-the-united-states-to-foreign-government-employees>

### 2026-09-08 · TPS

**Sudan and Ukraine TPS: USCIS is mailing notices that extend expired work permits to Oct. 19 — our pages implied they had lapsed**

Our Sudan and Ukraine entries said only that "an EAD auto-extension ran through April 19, 2026; verify current EAD validity with the latest USCIS notice." A holder whose card expired after that date could read our page and conclude they had no work authorization. E-Verify guidance dated September 3, 2026 shows otherwise: USCIS is mailing individual notices extending expired TPS-based EADs to October 19, 2026, and for Form I-9 a qualifying A12 or C19 card plus that notice is valid List A proof through October 19, 2026. Qualifying card-expiry is on or after July 22, 2026 for Sudan and on or after April 20, 2026 for Ukraine. Both bulletins also state the designations are set to terminate October 19, 2026. This is the same omission we corrected for El Salvador; it is now fixed in tps_designations.json and tps_work_permits.json, EN and ES.

Primary source: <https://www.e-verify.gov/about-e-verify/whats-new/update-on-temporary-protected-status-for-sudan-release-sept-03-2026>

### 2026-09-08 · TPS

**El Salvador TPS: E-Verify says it terminates Sept. 9, but no Federal Register notice exists — we now publish both halves**

E-Verify guidance dated September 3, 2026 states that the El Salvador TPS designation "and related benefits are set to terminate on Sept. 9, 2026" and instructs employers to enter September 9, 2026 as the expiration date on Form I-9 and in E-Verify. At the same time, NO Federal Register notice exists — no extension, no redesignation and no termination — and nothing about El Salvador TPS sat on the FR public-inspection desk for the September 9 issue when we checked on September 8. That is a genuine gap, and the pages now report both halves instead of only one. The statutory backdrop: 8 U.S.C. 1254a(b)(3)(B) makes a termination effective no earlier than 60 days after a notice is published, and 1254a(b)(3)(C) extends a designation 6 months when the Secretary makes no timely determination (the deadline here fell about July 11, 2026). We can confirm nothing was PUBLISHED by then; we CANNOT confirm whether a determination was made, and the statute keys on the determination — so we assert no outcome and publish no computed end date. Two corrections to our earlier framing, both caught in cross-AI review: (1) the statute extends the DESIGNATION, while Lebanon's work permits were extended by the NOTICE itself ("Through this Federal Register notice, DHS automatically extends the validity of EADs") — so a statute alone is not what an employer enters into E-Verify, and the same gap reaches driver's-licence renewals and state benefits via SAVE; (2) the Lebanon analogy is weaker than it first appeared, because that notice was already on public inspection before its period ended ("FR Doc. 2026-10704 Filed 5-27-26; 11:15 am", printed May 29) whereas El Salvador's desk is empty. Reader guidance is now: plan around September 9, keep every document, do not quit on a rumor, do not tell an employer you are cleared to work past September 9, and get individual legal advice. Updated EN+ES: the El Salvador country page (rewritten section, callout, work FAQ and removal FAQ), the TPS-by-country hub, the TPS work-permit dataset page, and tps_designations.json.

Primary source: <https://content.govdelivery.com/accounts/USDHSCISEVERIFY/bulletins/42855a4>

### 2026-09-06 · TPS

**Correction: El Salvador TPS work permits — USCIS no longer lists the July 22, 2026 date; pending renewals get a notice extending the EAD to September 9, 2026**

The status box on our El Salvador TPS page (EN + ES) said USCIS listed EADs expiring March 9, 2025 as valid through July 22, 2026. USCIS updated its El Salvador TPS page on September 3, 2026 and that date no longer appears anywhere on it. The page now lists EADs as auto-extended by Federal Register notice through March 9, 2026, and says that TPS holders whose renewal EAD (category A12 or C19) is still pending receive an individual USCIS notice extending the EAD to September 9, 2026; with that notice, cards with a Card Expires date of March 9, 2025, June 30, 2024, December 31, 2022, October 4, 2021, January 4, 2021, January 2, 2020, September 9, 2019 or March 9, 2018 remain proof of work authorization through September 9, 2026. Our status box now says exactly that, matching the page body and FAQ. USCIS has published nothing about the period after September 9, 2026.

Primary source: <https://www.uscis.gov/humanitarian/temporary-protected-status/temporary-protected-status-designated-country-el-salvador>

### 2026-09-05 · PROCEDURES

**Correction: the H.R.1 car-loan interest deduction has no SSN requirement — ITIN pages said all four new deductions required one**

Six ITIN tax pages (EN + ES) stated that the four new H.R.1 deductions — tips, overtime, car-loan interest and the senior deduction — all require a Social Security number. Three do: 26 U.S.C. §§ 224(d), 225(d) and 151(d)(5) each contain an SSN rule. The car-loan interest deduction, 26 U.S.C. § 163(h)(4), contains none: it requires the vehicle identification number on the return and a loan taken out after December 31, 2024 that is secured by a first lien on a new (first-use) vehicle bought for personal use with final assembly in the United States; interest is capped at $10,000 a year and reduced above $100,000 of modified adjusted gross income ($200,000 joint). The IRS final regulations (2026-18219, Federal Register September 8, 2026) also contain no SSN rule. The pages now state the three-of-four rule and describe the car-loan exception.

Primary source: <https://www.law.cornell.edu/uscode/text/26/163>

### 2026-09-05 · CORRECTION

**Correction: LSC civil legal aid directories reconciled with LSC's current grantee roster (7 states)**

The state directories were built from LSC's service-area map snapshot of May 27, 2026, whose 2018 reporting year predates several mergers. Checked page by page against LSC's own grantee roster (lsc.gov/about-lsc/our-grantees) on September 5, 2026: Wisconsin still listed Judicare Legal Aid, which merged into Legal Action of Wisconsin on January 1, 2026; Minnesota listed Legal Services of Northwest Minnesota, now part of Justice North, and omitted Anishinabe Legal Services; Michigan omitted Michigan Indian Legal Services and Oklahoma omitted Oklahoma Indian Legal Services (Native American Basic Field grantees that LSC's map feed does not carry); Arkansas and Pennsylvania counted dissolved or merged organizations as current grantees; Tennessee counted one grantee twice because it holds two service areas. Each page now lists only current grantees, states the number of distinct organizations, and keeps former grantees in a labeled note with their 2018 figures. No 2018 figures were invented for the added grantees: LSC publishes none, and the cells say so.

Primary source: <https://www.lsc.gov/about-lsc/our-grantees>

### 2026-09-04 · BENEFITS

**Court pauses a third USCIS hold memo: Diversity Visa adjustment applications (PM-602-0193) — Medani v. Trump**

On August 28, 2026 the Northern District of California, in Medani v. Trump, No. 26-cv-6332, temporarily vacated PM-602-0193 — the memo holding adjustment-of-status applications of FY-2026 Diversity Visa selectees — pending further litigation, ordered USCIS to resume ordinary adjudication of the plaintiffs' pending applications for the rest of the DV fiscal year, and certified a subclass of FY-2026 DV selectees and derivative beneficiaries subject to the hold. USCIS's September 4, 2026 alert says it strongly disagrees but will comply pending possible further review. Added to the standing hold-policies case page (EN + ES) and the litigation tracker.

Primary source: <https://www.uscis.gov/newsroom/alerts/court-order-on-diversity-immigrant-visa-program-hold-policy>

### 2026-09-04 · PROCEDURES

**State Department publishes its Executive Order 14418 implementation plan: a sworn parental attestation for a child's passport when neither parent is a U.S. citizen**

On September 4, 2026 the State Department posted a three-page proposed Implementation Plan for Executive Order 14418 (prospective only, effective on publication, subject to modification) and marked its EO 14160 page superseded. For a child's U.S. passport where neither parent is a U.S. citizen, an attestation from each parent, under penalty of perjury, about whether either parent meets any of the order's conditions must be submitted; if it is missing it is requested on review, and if the answers confirm no condition is met adjudication continues. State reads 'foreign government employee' to include locally hired embassy or consulate staff who are nationals of the sending country, and generally to exclude, case by case, third-country nationals, contractors, state-owned-enterprise employees and personal employees of officials. Trump v. Barbara is unchanged: a child born in the United States is a citizen at birth. USCIS, SSA and DOJ had published nothing as of September 5. Updated: the birthright case page, know-your-rights on U.S.-citizen children, and the 12 register-your-U.S.-born-child consulate pages (EN + ES).

Primary source: <https://travel.state.gov/content/travel/en/News/passports/executive-order-14418--continuing-to-protect-the-meaning-and-val.html>

### 2026-09-01 · CORRECTION

**Correction: EOIR pending caseload is 3,469,569 (FY 2026 Q3), not "3.7 million as of FY 2024"**

All 104 immigration-court-by-state pages (EN + ES) stated that EOIR had approximately 3.7 million pending cases as of FY 2024 and an average wait of 1,200-1,500 days from the Notice to Appear to the first hearing. EOIR's own adjudication statistics (Pending Cases, New Cases, and Total Completions, data generated July 24, 2026) show 3,924,993 pending at the end of FY 2024 and 3,469,569 at the end of the third quarter of FY 2026; EOIR publishes no per-court NTA-to-hearing wait. The paragraph now renders from a dataset built from that PDF.

Primary source: <https://www.justice.gov/eoir/media/1344791/dl?inline>

### 2026-09-01 · CORRECTION

**Correction: Form I-131 advance parole takes months longer than the "5-8 months" we stated, and a CBP parole fee applies at the port of entry**

The 66 traveling-to-your-country pages (EN + ES) gave a 5-8 month processing time for Form I-131. USCIS's own processing-times system shows 23 months for advance parole and 16 months for re-entry permits (80% of cases adjudicated in the past six months); the pages now embed that live table. The same pages omitted that the USCIS fee schedule (Form G-1055, edition 05/29/26) attaches the Pub. L. 119-21 immigration parole fee, collected by CBP each time the holder seeks parole at a port of entry unless an exception applies.

Primary source: <https://egov.uscis.gov/processing-times/>

### 2026-09-01 · CORRECTION

**Correction: the OpenSky Secured Visa requires US citizenship or permanent residence, so it is not an option for most ITIN-only applicants**

Our 104 ITIN-banking-by-state pages listed the OpenSky Secured Visa as available to all ITIN holders. The card's own disclosure (Capital Bank, N.A.) requires the applicant to be a United States citizen or permanent resident and carries a $35 annual fee. The pages and the credit-building guide now say so; the Capital One Quicksilver Secured, which Capital One lists as ITIN-eligible, remains.

Primary source: <https://app.openskycc.com/files/tc-sky1-073.pdf>

### 2026-09-01 · COURTS

**The government asks the Supreme Court to decide the interior-arrest bond split — a petition, not a grant (Rhoney v. Barbosa da Cunha, No. 26-104)**

On July 23, 2026 the federal government filed a petition for a writ of certiorari asking the U.S. Supreme Court to review the Second Circuit's decision that immigrants arrested in the interior are detained under 8 U.S.C. § 1226(a) — where an immigration judge can set bond — rather than under § 1225(b)(2)(A) mandatory detention. It is docketed as Rhoney v. Barbosa da Cunha, No. 26-104, from Second Circuit No. 25-3141 (decided April 28, 2026), and the respondent's response was filed August 21, 2026. The Court has NOT granted certiorari: a petition is not a grant, the docket shows no conference date, and until the Court acts the detention rule in each circuit is unchanged. Three other things moved the split since our last review: the Eighth Circuit denied rehearing en banc and panel rehearing in Herrera Avila on June 17, 2026 and issued its mandate on June 25; the Tenth Circuit sided with the immigrants in Santillan Quiroz v. Mullin on June 30, 2026; and the Ninth Circuit did the same in Rodriguez Vazquez v. Bostock on July 30, 2026. The count is now five circuits for a bond hearing (2nd, 6th, 9th, 10th, 11th) against two for mandatory detention (5th, 8th), with the Seventh Circuit's decision failing to command a majority. One caveat on that count: the Eleventh Circuit withheld its mandate on May 13, 2026 and the government's petition for rehearing en banc, filed June 22, 2026, was still pending as of that docket's August 28, 2026 update — so its ruling is not final. Separately, the Supreme Court has set Genalo v. Black, No. 25-886, for oral argument on Tuesday, October 13, 2026 — that case is about prolonged detention under § 1226(c) and will not by itself resolve this split.

Primary source: <https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/26-104.html>

### 2026-08-28 · COURTS

**Second court blocks the USCIS asylum/benefits hold memos — N.D. California enjoins PM 602-0192 and PM 602-0194, certifies a class (Red Eagle Law v. Edlow)**

A second court has now blocked the same policy memos. On August 24, 2026, the U.S. District Court for the Northern District of California issued an order in Red Eagle Law, L.C. v. Edlow, No. 26-cv-04850-CRB, enjoining PM 602-0192 and PM 602-0194 and ordering USCIS to adjudicate applications in the normal course. The court also certified a class: citizens or natives of the 39 countries listed in Proclamations 10949 or 10998 (or the Palestinian Authority) who have a pending asylum application (Form I-589) or another pending USCIS benefit application that was subject to the hold memos and had not received a final decision as of the certification date. USCIS updated its 'Court Order on Hold Policies' alert on August 28, 2026: it says it strongly disagrees with the order but will follow its terms pending possible further judicial review, and will issue updated instructions. USCIS has not said how this injunction interacts with the First Circuit's August 14 order reviving the Comprehensive Re-Review in the Dorcas appeal.

Primary source: <https://www.uscis.gov/newsroom/alerts/recent-court-order-on-hold-policies>

### 2026-08-25 · ENFORCEMENT

**CBP establishes four Customs-Enforcement Areas at sea — South Florida, Gulf Coast of Texas, Central/Southern California and Puerto Rico**

Effective August 25, 2026, the CBP Commissioner declared four Customs-Enforcement Areas under the Anti-Smuggling Act of 1935 (19 U.S.C. 1701), published as CBP Dec. No. 26-17 at 91 FR 54800. Each area sits on the high seas adjacent to but OUTSIDE US customs waters and runs out to 24 nautical miles from the baseline — it covers water further offshore, not more land, and does not change what agents may do at an inland checkpoint, on a bus, or at a home. Inside a CEA, customs officers may board any vessel, examine the vessel and any merchandise or person on board, bring them into port, and pursue, seize or arrest, and may enforce 18 U.S.C. 2237 against a master who fails to heave to or obstructs a boarding. The four areas cover the South Florida coast including the Florida Keys, the Texas Gulf Coast from the Sabine River to the Mexican maritime boundary, the California coast from Ano Nuevo Lighthouse south to the Mexican maritime boundary including eight offshore islands, and the waters encircling Puerto Rico including Mona, Desecheo, Vieques and Culebra. CBP wrote the areas to operate independently, so enjoining one leaves the others in force.

Primary source: <https://www.federalregister.gov/documents/2026/08/25/2026-17354/establishment-of-four-customs-enforcement-areas>

### 2026-08-24 · BENEFITS

**Correction: community health center pages no longer claim patient information is never shared with immigration authorities**

All 52 state community-health-center (FQHC) pages carried the blanket reassurance that patient information is not shared with immigration authorities. That is an overclaim after the 2025 HHS/CMS–ICE Medicaid data-sharing agreement, which a federal court only partially blocked on December 29, 2025. The pages now explain the HIPAA protection, the Medicaid-enrollment caveat, and that sliding-fee payment creates no Medicaid record.

Primary source: <https://clearinghouse.net/case/46754/>

### 2026-08-21 · FEES

**H.R.1 fees appeal: emergency stay motion withdrawn — First Circuit sets merits briefing, opening brief due September 30, 2026**

In the H.R.1 immigration-fees appeal (Venezuelan Ass'n of Mass. v. USCIS, 1st Cir. No. 26-1893), the plaintiffs withdrew their renewed emergency stay motion on August 20, 2026, and on August 21 the court granted the withdrawal and set a merits briefing schedule with the appellants' opening brief due September 30, 2026. No emergency ruling will issue, so the one-year cap on TPS-based work permits keeps operating while the appeal is briefed.

Primary source: <https://www.courtlistener.com/docket/73728632/venezuelan-association-of-massachusetts-v-united-states-citizenship-and/>

### 2026-08-20 · TAXES

**Treasury/IRS propose restricting the refunded portion of the CTC, EITC, AOTC, and adoption credit to citizens and PRWORA qualified aliens**

Proposed regulations published Aug. 20, 2026 (REG-119882-25, 91 FR 53812) would treat the refunded portion of the Child Tax Credit, Earned Income Tax Credit, American Opportunity Credit, and adoption credit as a federal public benefit under PRWORA. Only U.S. citizens, U.S. nationals, and PRWORA qualified aliens (lawful permanent residents, asylees, refugees, and certain other groups) could receive the refunded portion; on a joint return one qualifying spouse suffices, and the non-refundable portion that offsets tax owed is unaffected. This is a proposal, not current law — it would apply to tax years ending on or after the date final regulations publish. Comments are open through Oct. 5, 2026.

Primary source: <https://www.federalregister.gov/documents/2026/08/20/2026-16985/application-of-the-personal-responsibility-and-work-opportunity-reconciliation-act-of-1996-to-the>

### 2026-08-20 · TAXES

**IRS launches a digitally authenticated Tax Compliance Report in Individual Online Account**

On Aug. 20, 2026 the IRS announced a downloadable Tax Compliance Report (IR-2026-97), available through IRS Individual Online Account, for use when applying for a job, a loan, a government benefit, or another service that requires tax-compliance information. Each report carries an IRS-issued digital certificate so receiving organizations can verify its authenticity. It complements, not replaces, the five transcript types.

Primary source: <https://www.irs.gov/newsroom/irs-launches-digitally-authenticated-tax-compliance-report>

### 2026-08-18 · PROCEDURES

**USCIS publishes the public-charge framework that replaces the 2022 rule on September 18**

On Aug. 18, 2026 USCIS published Policy Manual guidance, effective Sept. 18, 2026, that supersedes the 1999 Interim Field Guidance and governs public-charge determinations for I-485s filed on or after that date. Officers weigh five statutory factors case-by-case. Means-tested benefits received before Sept. 18, 2026 are considered only if they were cash assistance or long-term institutionalization (the 2022-rule limits); benefits the applicant receives on or after that date can all be considered — USCIS names cash assistance, housing assistance, food stamps, and college financial aid. Public-charge bonds (Form I-945) return, by USCIS invitation in a Notice of Intent to Deny only.

Primary source: <https://www.uscis.gov/newsroom/alerts/uscis-issues-guidance-on-making-public-charge-inadmissibility-determination>

### 2026-08-18 · TPS

**Ethiopia TPS terminated — the last court stay is lifted**

On Aug. 18, 2026 Judge Brian E. Murphy of the District of Massachusetts lifted the administrative stay in African Communities Together v. Noem (No. 1:26-cv-10278, ECF 103), dismissing Counts I-IV and VI-VIII, denying dismissal of Count V, denying the postponement motion as moot, and ordering a joint discovery and briefing schedule by Aug. 25, 2026. USCIS archived the Ethiopia TPS page the same day and E-Verify guidance issued Aug. 18 (superseding Aug. 6) states the designation is terminated, effective Aug. 18, 2026 — A12/C19 EADs are no longer valid and employers must reverify. Ethiopia's promised Form I-9 date was Aug. 19, so it was cut one day short. No TPS designation is court-stayed any more.

Primary source: <https://www.e-verify.gov/about-e-verify/whats-new/termination-of-temporary-protected-status-for-ethiopia-release-aug-18-2026>

### 2026-08-17 · PROCEDURES

**Overtime corrected for daily-overtime states: California, Alaska, Nevada, Colorado**

Our state wage pages stated overtime as the federal 1.5x-over-40h/week rule everywhere. Four states guarantee more: California (1.5x after 8h/day or 40h/week; 2x after 12h/day — Labor Code §510), Alaska (1.5x after 8h/day or 40h/week — Alaska Stat. §23.10.060), Nevada (1.5x after 8h in a 24-hour period for workers earning under 1.5x the state minimum wage — NRS 608.018), and Colorado (1.5x after 40h/week, 12h/workday, or 12 consecutive hours — COMPS Order Rule 4.1.1). Those four pages now state the state rule.

Primary source: <https://www.dir.ca.gov/dlse/faq_overtime.htm>

### 2026-08-16 · PROCEDURES

**El Salvador TPS: pending EAD renewals extended by USCIS notice to Sept. 9, 2026**

USCIS's El Salvador TPS page confirms that beneficiaries whose A12/C19 EAD renewal is still pending receive a notice (mail + myUSCIS) extending the expired card to September 9, 2026; qualifying card front dates go back to March 9, 2018. Nothing is announced beyond Sept. 9, 2026. Our El Salvador TPS pages now carry the mechanism EN+ES.

Primary source: <https://www.uscis.gov/humanitarian/temporary-protected-status/temporary-protected-status-designated-country-el-salvador>

### 2026-08-14 · PROCEDURES

**New I-539 and I-765 form editions Sept. 15 -- older editions rejected, no grace period**

USCIS announced that revised 09/15/26 editions of Form I-539 (extend/change status) and Form I-765 (work permit) publish September 15, 2026, aligned with the fixed-period-of-admission rule. No grace period: older editions postmarked or submitted on or after September 15 are rejected; the new editions are accepted only on or after that date.

Primary source: <https://www.uscis.gov/newsroom/alerts/uscis-to-publish-new-editions-of-form-i-539-and-form-i-765-older-editions-will-be-rejected-starting>

### 2026-08-14 · BENEFITS

**Appeals court lets USCIS resume re-review of approved cases (39-country litigation)**

On August 14, 2026 the First Circuit partially stayed the Rhode Island ruling in Dorcas International v. USCIS: while the appeal proceeds, USCIS may resume re-reviewing already-approved benefit requests of people from the designated countries who entered the U.S. on or after January 20, 2021. The asylum and benefits holds remain vacated.

Primary source: <https://www.ca1.uscourts.gov/sites/ca1/files/opnfiles/26-1703P-01A.pdf>

### 2026-08-14 · TPS

**Somalia TPS terminated effective Aug. 14, 2026 — court lifts the stay and E-Verify says A12/C19 EADs are no longer valid**

On the day Somalia's Aug. 14 Form I-9 date came due, the District of Massachusetts granted the government's motion and lifted the administrative stay in African Communities Together v. Noem (No. 26-cv-11201); the plaintiffs filed a notice of appeal the same day. E-Verify guidance issued Aug. 14, 2026 (superseding Aug. 12) states the Somalia designation is terminated, effective Aug. 14, 2026: Form I-766 EADs with category A12 or C19 are no longer valid and employers must reverify. Ethiopia's stay survived a same-day motion to lift (No. 26-cv-10278) and it is now the only designation still court-stayed, with a Form I-9 date of Aug. 19, 2026. The USCIS Somalia page had not yet been archived as of Aug. 15, 2026.

Primary source: <https://www.e-verify.gov/about-e-verify/whats-new/termination-of-temporary-protected-status-for-somalia-release-aug-14-2026>

### 2026-08-13 · PROCEDURES

**BIA: leaving on advance parole is now a "departure" — Matter of Arrabally overruled**

In Matter of Delcarmen-Lara, 29 I&N Dec. 830 (BIA 2026, decided Aug. 13), the Board of Immigration Appeals overruled Matter of Arrabally and Yerrabelly (2012) and held that a departure under a grant of advance parole is a "departure" under INA §212(a)(9)(B)(i)(II). Advance-parole travel is no longer a safe harbor from the unlawful-presence bars, and the Board applied the rule to a trip already taken. Our I-131 and DACA travel pages now carry the new rule.

Primary source: <https://www.justice.gov/eoir/media/1457741/dl?inline>

### 2026-08-12 · TPS

**E-Verify moves the TPS Somalia Form I-9 date again: Aug. 12 to Aug. 14, 2026**

On the day Somalia's Aug. 12 Form I-9 date came due, E-Verify posted superseding Somalia guidance replacing the Aug. 10 release. The EADs remain extended per court order under African Communities Together v. Noem (No. 26-cv-11201, D. Mass.), and employers now enter Aug. 14, 2026 on Form I-9 and in E-Verify. This is the second consecutive two-day step, and the third release in a row posted on the very day the prior date came due. Somalia remains the earlier of the two designations still court-stayed, ahead of Ethiopia (Aug. 19, 2026). The USCIS Somalia TPS page is still live, not archived (checked Aug. 14, 2026).

Primary source: <https://www.e-verify.gov/about-e-verify/whats-new/update-on-termination-of-temporary-protected-status-for-somalia-release-7>

### 2026-08-11 · CITIZENSHIP

**DOJ has filed 123 civil denaturalization complaints since Jan. 20, 2025 — a record — USCIS announces 25 more**

USCIS announced that the Justice Department filed denaturalization actions against 25 individuals since July 2026 — described as the largest denaturalization effort yet — and that 123 civil denaturalization complaints have been filed since Jan. 20, 2025, the most in recorded history. In June 2026 news outlets had reported a DOJ goal of at least 250 cases by the end of fiscal year 2026. These are individual civil suits under 8 U.S.C. § 1451(a); each is decided on its own record. Denaturalization does not affect people who are U.S. citizens by birth.

Primary source: <https://www.uscis.gov/newsroom/news-releases/justice-department-files-record-25-denaturalization-cases-against-naturalized-criminals-including>

### 2026-08-11 · CITIZENSHIP

**New executive order on citizenship documents — birthright citizenship itself is unchanged**

Executive Order 14418, signed August 6 and published August 11, 2026 (91 FR 51991), does not reopen Trump v. Barbara: a child born in the United States to undocumented parents is still a U.S. citizen at birth. The order directs federal agencies not to issue — or accept state and local documents recognizing — U.S. citizenship for a person when neither parent is a U.S. citizen and one of four categories applies: a parent is a designated Foreign Terrorist Organization member or Specially Designated Global Terrorist; a parent is a foreign government employee (defined to include embassy or consulate employees who are nationals of that country); the parents engaged in a commercial transaction for birth tourism or U.S. surrogacy, or committed citizenship fraud; or the birth occurred in a U.S. territory where citizenship is not conferred by federal statute. The foreign-government-employee category is broader than the long-standing accredited-diplomat exception. Agencies must publish implementation guidance within 30 days, i.e. by September 5, 2026.

Primary source: <https://www.federalregister.gov/documents/2026/08/11/2026-16403/continuing-to-protect-the-meaning-and-value-of-american-citizenship>

### 2026-08-11 · VISAS

**USCIS gains authority to require e-filing — new Form I-936 waiver ($25); nothing is mandated yet**

An interim final rule effective on publication (91 FR 51924, Aug. 11, 2026) lets USCIS mandate electronic filing of a benefit request that has been available for e-filing at least 180 days (8 CFR 103.2(a)(1)(ii)), after publishing notice on uscis.gov with at least 60 days of advance notice. It mandates nothing on its own: DHS states the rule will have no practical effect until Form I-936 is approved by OMB and USCIS issues such a notice. New Form I-936, Request for Waiver of E-Filing Requirement, is filed before a paper filing and costs $25 (8 CFR 106.2(a)(64)), with a fee waiver available on Form I-912 (8 CFR 106.3). The standard is undue hardship at USCIS's discretion, weighing geographic location, socioeconomic conditions and the availability of public technology resources; DHS says lacking home internet is not by itself enough — the requestor must explain why libraries, community centers, friends or family are not an option. Comments close Oct. 13, 2026 (DHS Docket USCIS-2026-0232, RIN 1615-AD19).

Primary source: <https://www.federalregister.gov/documents/2026/08/11/2026-16313/mandatory-electronic-filing-e-filing>

### 2026-08-10 · FEES

**Court declines to pause the TPS work-permit one-year cap during the H.R.1 fees appeal**

On August 10, 2026 Judge Gorton denied the plaintiffs' emergency motion to stay the TPS work-authorization terminations pending appeal in Venezuelan Ass'n of Mass. v. USCIS, so the one-year cap on TPS-based EADs keeps operating. The plaintiffs' emergency stay motion at the First Circuit (No. 26-1893) was fully briefed August 14 and awaits a ruling.

Primary source: <https://www.courtlistener.com/docket/73564609/venezuelan-association-of-massachusetts-v-united-states-citizenship-and/>

### 2026-08-10 · TPS

**E-Verify moves the TPS Somalia Form I-9 date again: Aug. 10 to Aug. 12, 2026**

On the day Somalia's Aug. 10 Form I-9 date came due, E-Verify posted superseding Somalia guidance replacing the Aug. 5 release. The EADs remain extended per court order under African Communities Together v. Noem (No. 26-cv-11201, D. Mass.), and employers now enter Aug. 12, 2026 on Form I-9 and in E-Verify. The two-day step makes Somalia the earlier of the two designations still court-stayed, ahead of Ethiopia (Aug. 19, 2026). The USCIS Somalia TPS page is still live, not archived (checked Aug. 11, 2026). The release title is not the signal: Burma’s Aug. 7 termination was also posted as “Update on Termination” — only the text distinguishes an extension from a cut.

Primary source: <https://www.e-verify.gov/about-e-verify/whats-new/update-on-termination-of-temporary-protected-status-for-somalia-release-6>

### 2026-08-07 · TPS

**Burma (Myanmar) and South Sudan TPS terminated, effective Aug. 7, 2026 — A12/C19 work permits no longer valid**

On Aug. 7, 2026 USCIS archived the Burma (Myanmar) and South Sudan TPS country pages, and E-Verify guidance issued the same day states both designations are terminated, effective Aug. 7, 2026 (Burma: 90 FR 53378; South Sudan: 90 FR 50484). Form I-766 EADs with category A12 or C19 issued under them are no longer valid, and employers must reverify those employees. South Sudan was terminated three days before the Aug. 10 Form I-9 date its Aug. 6 guidance had promised. Two designations remain court-stayed with EADs extended per court order: Somalia (I-9 date Aug. 10, 2026) and Ethiopia (Aug. 19, 2026).

Primary source: <https://www.e-verify.gov/about-e-verify/whats-new/update-on-termination-of-temporary-protected-status-for-burma-release-aug>

### 2026-08-06 · COURTS

**The alien registration rule is now final and the appeal is over — DHS issued a final rule effective June 29, 2026 and the D.C. Circuit dismissed the challenge on August 6, 2026**

Two changes closed out the Form G-325R registration fight. On June 29, 2026 DHS published the final rule “Alien Registration Form and Evidence of Registration” (91 FR 39248, RIN 1615-AC96), effective the same day. It adopts the March 2025 interim final rule as final and, in DHS's words, adopts the amendments to 8 CFR 264.1(a) and (b) “without change” — Form G-325R remains the general registration form and the USCIS Proof of Alien G-325R Registration remains the evidence of registration. The changes it does make are administrative: it updates which documents count as registration or as proof of registration (adding Forms I-94A/I-94W, DSP-150 in place of the old Canadian and Mexican border crossing cards, I-860, I-871, and NEXUS/SENTRI/FAST/Global Entry documents; dropping obsolete Forms I-67, I-691 and I-700), restructures the fingerprinting waivers in 8 CFR 264.1(e) — edits DHS calls “non-substantive and clarifying” — and makes technical corrections to 8 CFR 264.1(g), 264.5(h) and 264.6. DHS decided not to impose a biometric services fee “at this time,” while saying it may impose an application or biometric services fee in the future. Then, on August 6, 2026, the D.C. Circuit (Judges Millett, Katsas and Childs) discharged its July 27 order to show cause — which had asked why the consolidated appeals (Nos. 25-5152, 25-5233, 25-5247) should not be dismissed as moot in light of the new final rule — and ordered the clerk to note that the case is dismissed, stating that no mandate will issue. The court did not rule on whether the registration rule is lawful. The duty to register, the duty of registered noncitizens 18 and over to carry proof, and the criminal penalties for willful noncompliance are statutory (INA sections 262, 264(e) and 266) and did not change. The district court case (D.D.C. 1:25-cv-00943) remains stayed. DHS separately asked for comments on possible future changes to the registration regulations; that comment period closed August 28, 2026.

Primary source: <https://www.federalregister.gov/documents/2026/06/29/2026-13057/alien-registration-form-and-evidence-of-registration>

### 2026-08-06 · TPS

**E-Verify moves two more TPS Form I-9 dates: Ethiopia to Aug. 19, South Sudan to Aug. 10, 2026**

E-Verify posted superseding guidance for Ethiopia and South Sudan on Aug. 6, 2026 — the day their shared Form I-9 date came due — each replacing a July 30, 2026 release. Employment Authorization Documents under both designations remain extended per court order — African Communities Together v. Noem (Ethiopia: No. 26-cv-10278-BEM; South Sudan: No. 25-cv-13939-PBS, both D. Mass.) — and the guidance still describes the extension as limited relief until the lower courts align with Mullin v. Doe. South Sudan's Section 2 date moves from Aug. 6 to Aug. 10, 2026, the same day as Somalia; Ethiopia's moves from Aug. 6 to Aug. 19, 2026, a 13-day step that makes it the furthest out of the four court-stayed designations. Section 1 still reads 'as per court order'. Neither USCIS country page has been moved to the archive, the step that put the Haiti, Syria and Yemen terminations into force on July 27, 2026.

Primary source: <https://www.e-verify.gov/about-e-verify/whats-new>

### 2026-08-05 · ASYLUM

**Court splits the H.R.1 ruling: asylum-fee rejection and removal stay blocked; the TPS work-permit cap stands**

On Aug. 5, 2026, the federal court in Venezuelan Ass’n of Mass. v. USCIS (No. 26-cv-13038, D. Mass.) replaced its July 21 administrative stay with a longer-term ruling. Stayed nationwide while the case proceeds: the rule provisions letting USCIS reject a pending Form I-589 or initiate removal solely for non-payment of the Annual Asylum Fee. Denied: the challenge to H.R.1’s one-year cap on TPS-based work permits — previously-extended TPS EADs no longer keep their prior expiration dates. The fee itself remains payable, and published summaries of the order do not list work-authorization termination among the stayed provisions — verify current USCIS guidance on that point. The plaintiffs appealed to the First Circuit on Aug. 6, 2026.

Primary source: <https://www.courtlistener.com/docket/73564609/venezuelan-association-of-massachusetts-v-united-states-citizenship-and/>

### 2026-08-05 · TPS

**E-Verify moves the TPS Somalia Form I-9 date again: Aug. 5 to Aug. 10, 2026**

E-Verify posted superseding Somalia guidance on Aug. 5, 2026, replacing its Aug. 3, 2026 release. Employment Authorization Documents issued under the Somalia designation remain extended per court order -- African Communities Together v. Noem, No. 26-cv-11201 (D. Mass.) -- and the guidance still describes the extension as limited relief until the lower courts align with Mullin v. Doe. The Form I-9 Section 2 date employers enter moves from Aug. 5, 2026 to Aug. 10, 2026; Section 1 still reads 'as per court order'. The five-day step makes Somalia the last of the four court-stayed designations to come due rather than the first -- Ethiopia and South Sudan (Aug. 6, 2026) and Burma (Aug. 7, 2026) now fall before it. The USCIS Somalia country page remains live; it has not been moved to the archive, the step that put the Haiti, Syria and Yemen terminations into force on July 27, 2026.

Primary source: <https://www.e-verify.gov/about-e-verify/whats-new/update-on-termination-of-temporary-protected-status-for-somalia-release-5>

### 2026-08-05 · PROCEDURES

**USCIS restores full discretion to deny without first sending an RFE or NOID**

USCIS Policy Alert PA-2026-05, issued Aug. 5, 2026 and effective immediately, updates Policy Manual Volume 1 so officers have full discretion to deny a benefit request without first issuing a Request for Evidence or a Notice of Intent to Deny when the initial evidence required by the form instructions is missing, or when the record does not establish eligibility. It applies to requests pending or filed on or after Aug. 5, 2026. The previous policy instructed officers to send an RFE or NOID first. The alert also drops the standard 12-week RFE response period: 8 CFR 103.2(b)(8)(iv) sets 12 weeks as the maximum, not the norm, and officers may now give less, so an RFE deadline can be considerably shorter than the 60-87 days previously typical. A NOID response stays capped at 30 days, mailed notices still add 3 days under 8 CFR 103.8(b), extra time cannot be granted, and the additional 14 days USCIS used to give for notices mailed outside the United States has been eliminated. Refugee and asylum applications are governed by separate regulations and are not covered.

Primary source: <https://www.uscis.gov/sites/default/files/document/policy-manual-updates/20260805-EvidentiaryStandards.pdf>

---

## Citing a change

Cite the primary government source for the underlying fact, and this record for
the change history. See [README](README.md#cite-this-dataset) for the citation
formats and DOI.

