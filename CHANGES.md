# What changed in US immigration data

A dated record of changes to US government immigration data, each verified
against its primary source. Government agencies publish the *current* value and
overwrite it; this file keeps the change itself.

**This page is generated** from [`data/change_log.json`](data/change_log.json)
(machine-readable, with the Spanish text and the affected dataset paths) by
[`scripts/refresh.py`](scripts/refresh.py). Canonical human-readable version, with
full context on each entry: <https://migrantusa.com/updates/>

Showing the 40 most recent of 183 recorded changes. Source data as of 2026-09-17.

---

### 2026-09-22 · ENFORCEMENT

**Folkston Annex and South Texas ICE Processing Center pages now carry the visiting schedules, legal-visit rules and contacts ICE publishes**

The pages for the Folkston ICE Processing Center Annex (Georgia) and the South Texas ICE Processing Center (Pearsall, Texas) were deepened on September 22, 2026 with specifics verified the same day at their own ice.gov facility pages (last updated 08/20/2026 and 08/06/2026) and EOIR's July 2026 List of Pro Bono Legal Service Providers. Newly published: the family, attorney, video-call, consular and clergy visiting periods ICE lists for each facility; visitor rules (ID, arrival time, minors, what visitors may bring); the ERO eFile rules for booking legal visits and the facility contacts for urgent legal requests; legal-document fax and email routes; mail and money-deposit rules, including ICE's own contradiction at the Folkston Annex between a mail-in address for money orders and a statement that all money arriving by mail is returned to the sender; complaint channels (ICE OPR, DHS OIG); and, for South Texas, the free legal providers EOIR lists for Pearsall, Texas. Several earlier statements were corrected, including that letters to a Folkston Annex detainee need the last four digits of the A-number.

Primary source: <https://www.ice.gov/detain/detention-facilities/south-texas-ice-processing-center>

### 2026-09-17 · ENFORCEMENT

**Two ICE facility pages now carry the visiting hours, money-deposit routes, bond rules and named free legal providers ICE and EOIR publish**

The pages for ERO El Paso Camp East Montana and the Karnes County Immigration Processing Center were deepened on September 17, 2026 with specifics verified the same day at their own ice.gov facility pages (last updated 08/10/2026 and 08/06/2026), ICE's CeBONDS page and EOIR's July 2026 List of Pro Bono Legal Service Providers. Newly published: the actual visiting periods (Camp East Montana is by appointment only, weekends and holidays 8 a.m.-1 p.m. and 2 p.m.-6 p.m. MT; Karnes runs 8 a.m.-6 p.m. on days assigned by housing unit, effective July 27, 2026); the mailing and money-deposit routes, including ICE's own contradiction at Karnes between a mail-in address for money orders and a statement that all money arriving by mail is returned to the sender; bond rules (CeBONDS only, Monday-Friday 9 a.m.-3 p.m. in the detainee's time zone, Fedwire or ACH only, obligor must be a citizen, LPR, law firm or non-profit); the ERO eFile requirement for legal visits; the deportation-officer and case-information contacts; the named free legal providers for each facility's court, with the RAICES Karnes hotline and the ABA detention hotline's in-facility speed dial 2150#; and the ICE Detention Reporting and Information Line, 1-888-351-4024.

Primary source: <https://www.ice.gov/detain/detention-facilities/camp-east-montana>

### 2026-09-17 · DATA

**Visa wait times refreshed from the State Department page updated September 17, 2026**

The Global Visa Wait Times table (243 posts) was re-read in a real browser on September 17, 2026, from the State Department page stamped 'Last updated: 17-SEP-2026', replacing the August 17 figures. Among the twelve countries this site tracks, the biggest moves were Mexico City's next B1/B2 appointment (4 to 5 months), Bogota's average B1/B2 wait (11 to 8.5 months), Tegucigalpa (7 to 5 months), Lima (7 to 8.5 months) and Guatemala City (1 to 1.5 months). The State Department blocks automated fetches, so this dataset is refreshed by hand from the rendered page.

Primary source: <https://travel.state.gov/content/travel/en/us-visas/visa-information-resources/global-visa-wait-times.html>

### 2026-09-17 · CORRECTION

**Correction: 16 immigration-court hearing links that no longer worked now point to EOIR's own list**

On September 17, 2026, all 786 Webex hearing-room links published on the immigration-court pages were re-tested against eoir.webex.com. Seventeen returned Webex's 'room not found' page; sixteen were replaced in both languages with a link to EOIR's 'Find an immigration court and access internet-based hearings' page (the judge's name and telephone access code were kept, because a dead room does not mean the judge has left), and one was a misspelling of a room that still works and now points to it. The remaining 769 links answered normally. Room links rot as judges move; they are re-tested monthly.

Primary source: <https://www.justice.gov/eoir/find-immigration-court-and-access-internet-based-hearings>

### 2026-09-17 · CORRECTION

**Correction: the DACA renewal-delays lawsuit is a records (FOIA) case, not a case that can order faster renewals**

The Form I-821D renewal page described East Bay Sanctuary Covenant v. USCIS (N.D. Cal. 3:26-cv-06367) as a suit 'over severe DACA renewal delays' without saying what it asks for. The docket lists its cause as 5 U.S.C. § 552 (Freedom of Information Act): it asks the court to force USCIS and ICE to release their internal records about the delays, and cannot order USCIS to adjudicate renewals faster. The page now says so, notes the stipulated scheduling order entered September 15, 2026, and rolls its 'no ruling has changed the procedure' date forward from August 17 to September 17, 2026. The practical advice is unchanged: file at day 150.

Primary source: <https://www.courtlistener.com/docket/73535388/east-bay-sanctuary-covenant-v-united-states-citizenship-and-immigration-services/>

### 2026-09-17 · CORRECTION

**Correction: the immigration-judge, Webex and dial-in tables on every state and city court page were re-pulled from EOIR — and the Spanish pages, which had been left four months behind English, now match**

Each immigration-court page carries a table of the judges sitting at that court with the judge's Webex hearing link and telephonic access code. Those tables were hand-maintained and had drifted: the English state pages were stamped "EOIR-verified" while the Spanish twins still carried the 2026-05-26 matrix, so a Spanish-speaking reader was being handed judges who had transferred months earlier. All 122 pages — 31 state pages and 30 individual court pages, in both languages — were rebuilt on September 17, 2026 from EOIR's own listing at justice.gov/eoir/eoir-immigration-court-listing: 75 courts and 792 judge rows, parsed once and written to English and Spanish in the same run, taking the state tables from 815 rows to 756. Examples of what was wrong: the Denver table listed André Carman, Jack D. Patten III, Jeremy Sibert and Jennifer C. Whitko, none of whom EOIR lists at Denver (Carman is on the Concord, California list), while Andrew Hurd and Tyler Wood, who are there, were missing; Salt Lake City listed Stephanie Arrache and James K. Glober, both now at Concord, and Joseph Q. Andelin, who is on no court's list, while Grant Pattison was missing; Honolulu listed Demetrius Cheeks, who is not there, and omitted Howard Hom, who is; Charlotte listed Ellen Karesh, who is not on EOIR's Charlotte list; the Annandale, Virginia table had 43 judges where EOIR lists 23, and the El Paso Service Processing Center table had 22 where EOIR lists 5. EOIR also no longer lists a San Francisco Immigration Court: its three judges — ACIJ Julie Nelson, Steven Kirchner and Frank Seminerio — all appear on the Concord list, and the California pages now say that instead of printing a court that no longer exists. The closed Batavia, New York court keeps its explanatory note. Thirteen judges whose EOIR-published Webex rooms no longer open keep pointing at EOIR's hearing-access page rather than at a dead room, and that decision is now carried across both languages and both page families automatically. Both languages are now rebuilt from EOIR's list in a single automated pass, so the Spanish tables can no longer fall behind the English ones.

Primary source: <https://www.justice.gov/eoir/eoir-immigration-court-listing>

### 2026-09-17 · CORRECTION

**Correction: H.R.1 is the 2025 reconciliation law, not the 2026 one**

Ten passages across five English pages and their Spanish twins — the asylum annual fee, the TPS-by-country hub, the ITIN application guide and the ITIN tax-credit guide — introduced H.R.1 as "the 2026 reconciliation law". The law was signed on July 4, 2025: the Department of Homeland Security's own Federal Register notice on the fees it created opens "On July 4, 2025, the President signed into law the One Big Beautiful Bill Act, Public Law 119-21, 139 Stat. 72 (HR-1)", and the site's own hr1_fees.json says the same. What happened in 2026 was the fiscal-year inflation adjustment of the fees, not the law. Every passage now names the law by its year, its public-law number and its signing date. On the ITIN tax-credit page the error also contradicted the next sentence, which already said "the 2025 law".

Primary source: <https://www.federalregister.gov/documents/2025/09/08/2025-17221/certain-dhs-immigration-enforcement-related-fees-required-by-hr-1-reconciliation-bill>

### 2026-09-17 · CORRECTION

**Correction: the USCIS processing time is the 80%-of-cases figure, not a median**

The USCIS processing-times movement page and the datasets index, in both languages, described the numbers we publish as "median processing times". They are not medians. USCIS publishes the time within which it says 80% of recent cases were completed, and our own dataset records that: uscis_processing_times.json states "USCIS publishes '80% of cases are completed within X'". The difference matters to a reader planning around a filing — half of cases finishing inside a window is a very different promise from four in five. Four pages now say what the figure actually is, matching the wording the main processing-times page already used.

Primary source: <https://egov.uscis.gov/processing-times/>

### 2026-09-17 · DATA

**ICE 287(g) dataset refreshed: 2,510 agreements as of ICE's September 15, 2026 workbook**

Our 287(g) file was built from ICE's September 8, 2026 workbook. ICE has since published a September 15, 2026 edition, and the pages that read the file were quoting the older totals. The dataset has been re-scraped from ICE's own participating-agencies workbook and the prose re-anchored to it: 2,510 agreements (was 2,466) held by 2,155 distinct agencies, across 40 jurisdictions — 38 states plus Guam and the Northern Mariana Islands, which the pages had been calling "40 states". By model: 179 Jail Enforcement, 1,778 Task Force, 553 Warrant Service Officer. The growth finding is unchanged in shape — 130 of the 2,510 active agreements predate February 2025, so 2,380 (95%) were signed since — and Texas (528) with Florida (353) still hold about 35% of the national total. Twelve states still have none.

Primary source: <https://www.ice.gov/identify-and-arrest/287g>

### 2026-09-17 · CORRECTION

**Correction: the state DMV pages did not tell you a federal rule now limits non-domiciled CDLs**

The commercial-driver's-licence row on all 53 state DMV pages, in both languages, said only that a CDL needs a Social Security number and lawful status. It did not mention that the Federal Motor Carrier Safety Administration has since narrowed who may hold one. FMCSA's final rule, published February 13, 2026 and effective March 16, 2026, reaffirms its September 29, 2025 interim final rule and limits eligibility for non-domiciled Commercial Learner's Permits and CDLs, for foreign-domiciled individuals, to those holding a specific, verifiable employment-based nonimmigrant status. A separate FMCSA exemption granted May 14, 2026 lets any state issue one to a citizen of the Marshall Islands, Micronesia or Palau with a valid Freely Associated State passport and a Form I-94. Both now appear on every state page, with links to the Federal Register. Someone on a work permit was being told to budget for CDL training that a federal rule may have already closed to them.

Primary source: <https://www.federalregister.gov/documents/2026/02/13/2026-02965/restoring-integrity-to-the-issuance-of-non-domiciled-commercial-drivers-licenses-cdl>

### 2026-09-17 · CORRECTION

**Correction: the internet-setup guides no longer advertise the Affordable Connectivity Program in their page summary, and the cross-border tax FAQ now names the Form 8938 threshold that actually applies to you**

Two leftovers from the September 10 correction wave. The internet-without-SSN guides (EN + ES) had already been corrected in the body to say the Affordable Connectivity Program ended, but their meta description and page summary still listed "low-income programs (ACP)" — the FCC states the ACP "ended on June 1, 2024, due to a lack of additional funding from Congress" (fcc.gov/acp), so the summary now names Lifeline, the program that is still running. Separately, the cross-border tax calculator FAQ (EN + ES) gave the FATCA Form 8938 thresholds as ">$50K (single) or >$100K (MFJ)" with no indication of who they apply to. Per the IRS, those are the thresholds for taxpayers living in the United States — and even there the test is more than $50,000 on the last day of the tax year OR more than $75,000 at any time during the year ($100,000 / $150,000 married filing jointly). Taxpayers living abroad file only above $200,000 / $300,000 (unmarried) or $400,000 / $600,000 (joint). The FAQ now states both sets and says which is which, and the IRS FATCA summary was added to the page's source list. 4 pages touched (2 EN + 2 ES).

Primary source: <https://www.irs.gov/businesses/corporations/summary-of-fatca-reporting-for-us-taxpayers>

### 2026-09-17 · PROCEDURES

**Our Nicaraguan consulate pages said “this office serves you” about offices that closed in January 2024 — the body text now matches the closure notice**

Nicaragua closed its Los Angeles and Houston consulates on January 19, 2024 and New Orleans on January 20, 2024, and the San Francisco office stopped serving the public; Voice of America reported on February 29, 2024 that “en Estados Unidos, por ejemplo, solo funcionan ahora los consulados de Nueva York, Washington y Miami.” Those four pages already carried a closure banner, but the paragraph underneath still read “serves the Nicaraguan community residing in [state]”, the service list was written in the present tense, and the first FAQ — which Google can show as a rich result — answered “Yes” to “Do I need an appointment?” All eight pages (English and Spanish) now state that the office is closed, name Miami, New York and Washington, D.C. as the three that remain, and say plainly that none of the listed services can be obtained at the old address. We also removed an untranslated English fragment from six Spanish pages, repaired a mis-numbered how-to-verify list, and hedged the two “register a US-born child” pages: Nicaragua's appointment portal (citas.cancilleria.gob.ni) rejected our requests on September 17, 2026, so readers are told to phone the consulate or the Embassy in Washington, D.C. at (202) 939-6570 if it will not load. Nicaragua's foreign-ministry site remains unreachable — www.cancilleria.gob.ni returns NXDOMAIN and cancilleria.gob.ni has no address record.

Primary source: <https://www.vozdeamerica.com/a/cierre-de-varios-consulados-de-nicaragua-en-eeuu-mexico-y-guatemala-impacta-a-la-diaspora-del-pais-centroamericano/7485761.html>

### 2026-09-17 · PROCEDURES

**Honduras's own appointment system lists 11 consulates in the US — we publish 19, so eight pages now warn that the office is unconfirmed**

Honduras publishes no consulate directory: sreci.gob.hn/consulados/ renders a page of navigation with no listings at all (checked in a real browser on September 17, 2026 — 1,827 characters, zero mentions of any US city). The one official surface that does name offices is the appointment system, citaconsular.sreci.gob.hn. Choosing “Estados Unidos” there on September 17, 2026 returned exactly eleven: Atlanta, Boston, Charlotte, Chicago, McAllen, Miami, New Orleans, New York, San Francisco, Seattle and Washington, D.C. We publish nineteen Honduran consulate pages. The eight the appointment system does not name — Aurora (CO), Dallas, Glendale (CA), Houston, Irving, Phoenix, Pittsburgh and Tampa (FL) — now carry a warning in both languages saying so. We are deliberately not calling those offices closed: a post that takes no online appointments would not appear in that menu either, and with no directory to check against we cannot tell the two cases apart. What the warning does say is that the address and phone printed on the page are unconfirmed, and that readers should call first or use the Embassy of Honduras in Washington, D.C. at (+1) 202-966-7702. Separately, the Phoenix and Irving pages used to credit their address to the “Honduran Ministry of Foreign Affairs” while citing an OpenStreetMap node that sits in Washington, D.C. and carries no address tag at all; that attribution was corrected on September 10, 2026.

Primary source: <https://citaconsular.sreci.gob.hn/>

### 2026-09-17 · PROCEDURES

**Dominican consulate pages: MIREX's Santo Domingo line corrected, and the new e-passport reaches consulates in August 2026, not February**

Two corrections across the 13 Dominican consulate pages in the United States (12 English pages plus the Spanish Los Angeles page), together with the script that generates the cluster. First, the phone number: the pages told readers that (809) 987-7001 was MIREX's fax line while simultaneously telling them to call it. The Ministry of Foreign Affairs' own website footer reads 'Tel.: (809) 987-7001' and 'Fax: (809) 535-6280' — 987-7001 is the phone, 535-6280 is the fax, and the generator script had been hardcoding the fax number as the number to call. Second, the passport date: the pages said the Dominican Republic's new electronic passport had been available 'since February 2026'. Issuing began inside the Dominican Republic in January 2026 (applications opened 15 January, biometric capture from 19 February), but delivery to Dominicans abroad — including at the US consulates these pages are about — was scheduled to begin in August 2026 (Diario Libre, 5 February 2026). A reader standing at a US consulate in February would have been told to expect a document that was not yet being issued there. The 10-year adult / 5-year minor validity was correct and is unchanged.

Primary source: <https://www.mirex.gob.do/>

### 2026-09-17 · CORRECTION

**Correction: the ITIN bank pages for every state carried a stale FDIC date, fourteen wrong Bank of America branch counts, and told readers in 24 states that their state had "limited coverage" when its own table showed hundreds of branches**

Three defects were fixed across all 104 ITIN-banking state pages (52 jurisdictions, English and Spanish). First, every page's FAQ attributed its Bank of America branch figure to "FDIC data (June 2026)" while the FDIC table directly above it was captioned with the real vintage of the feed that produced it (2026-09-08, api.fdic.gov/banks/locations). The date was written into the page text once and never moved again when the feed refreshed. The FAQ now says "per the FDIC branch data shown on this page" and carries no date at all, so the table's caption is the single place the vintage lives. Second, fourteen states carried a branch count in that FAQ that no longer matched the feed rendering the table on the same page — Ohio's FAQ said 51 next to a table saying 52, South Carolina said 62 next to 61, California 687 next to 685, and Kentucky and Minnesota were low rather than high (7 vs 8, 22 vs 23). Every count in the cohort was recomputed from the FDIC feed; these were wrong numbers inside FAQPage structured data, which is what an AI assistant or a rich result is most likely to quote. Third, 24 pages said "<State> has limited coverage of traditional banks for ITIN clients. The best options are digital neobanks." That sentence came from a hand-typed list of states, not from the data, and it contradicted the page's own table: South Carolina got it with all three national banks present and 1,194 branches from 76 banks; North Dakota with 411 branches from 71 banks; Rhode Island and Oklahoma while the same page's FAQ was telling the reader to walk into a Bank of America branch. It is replaced by a sentence computed from the FDIC feed, naming which of the three national banks with a documented ITIN path have branches in that state and which do not, and pointing at the table for the counts. No branch count, institution total or date is written into the page text any more: the data date is rendered from the feed at build time, and the counts that remain in the FAQ are re-synced from the feed by the maintenance script each time it runs, so a data refresh no longer leaves the words and the table in contradiction.

Primary source: <https://api.fdic.gov/banks/locations>

### 2026-09-17 · CORRECTION

**Correction: the Puerto Rico ITIN banking page called Puerto Rico a state, cited a census release one year behind its siblings, and counted only NCUA credit unions while the island's real co-op sector is supervised by COSSEC**

Three fixes on the Puerto Rico page, English and Spanish. Puerto Rico is an unincorporated US territory, not a state, and the demographics line said "the state's 3,254,885 people"; it now says the territory's. The same line cited the American Community Survey 2023 5-year estimates while all fifty sibling pages cite 2024. We queried the Census Bureau API directly for Puerto Rico (2024 ACS 5-year, the Puerto Rico Community Survey): 3,234,309 residents, 87,466 born outside the United States, and 3,200,873 of Hispanic or Latino origin — 2.7% and 99.0%. The page and its meta description now carry those figures. Third, the credit-union block showed only NCUA-insured institutions — eight of them, largely mainland-affiliated federal credit unions — while telling the reader credit unions are "often the most ITIN-flexible option." Puerto Rico's own cooperativas de ahorro y crédito are not NCUA institutions and so appear nowhere in that count: they are supervised and insured, share and deposit insurance up to $250,000 per member, by COSSEC, the Corporación Pública para la Supervisión y Seguro de Cooperativas de Puerto Rico, created by Ley Núm. 114-2001. A sourced sentence now points readers there. No cooperativa counts were invented — COSSEC publishes its own industry statistics and we cite the agency, not a number we could not verify. The page also no longer says Puerto Rico has "limited coverage of traditional banks": none of Bank of America, Wells Fargo or Chase has a branch on the island, but the FDIC table on the page shows 260 insured branches led by Banco Popular de Puerto Rico with 156, and the text now says that instead.

Primary source: <https://www.cossec.pr.gov/>

### 2026-09-17 · LITIGATION

**A judge set aside the rule ending automatic EAD extensions — but only for the seven people who sued**

On September 10, 2026 (order filed September 11, Dkt. 46), Judge David O. Carter of the U.S. District Court for the Central District of California granted a preliminary injunction in Jane Doe 1 et al. v. DHS, No. 8:26-cv-00060, finding that DHS had not justified bypassing notice-and-comment rulemaking when it issued the October 30, 2025 interim final rule that removed the automatic extension of Employment Authorization Documents (90 Fed. Reg. 48799). The relief is narrow: the court set the rule aside only as to the seven named plaintiffs, expressly declined to issue a nationwide injunction, and certified the order for immediate appeal under 28 U.S.C. § 1292(b), saying it would entertain a nationwide request if the government chooses not to appeal. For everyone else nothing changes yet: EAD renewals (Form I-765) filed on or after October 30, 2025 still receive no automatic extension, and as of September 17, 2026 USCIS had announced no change. What to watch: a government appeal to the Ninth Circuit, or a renewed nationwide-injunction request.

Primary source: <https://storage.courtlistener.com/recap/gov.uscourts.cacd.1001937/gov.uscourts.cacd.1001937.46.0.pdf>

### 2026-09-14 · PROCEDURES

**A court postponed the end of "duration of status" one day before it was due to start — and the new I-539 and I-765 editions are not being accepted**

On September 14, 2026 the U.S. District Court for the District of Massachusetts postponed the effective date of DHS's final rule replacing "duration of status" with a fixed admission period for F, J and I nonimmigrants (91 Fed. Reg. 44976, July 17, 2026), and preliminarily enjoined DHS from taking any further action to implement it, pending further order or resolution on the merits (Presidents' Alliance on Higher Education and Immigration, et al. v. DHS, 26-cv-13799, D. Mass.). The rule had been due to take effect September 15. Two things follow for filers. First, duration of status still applies — USCIS says it "will proceed under the previous regulatory provisions." Second, the form-edition change that USCIS announced on August 14 did not happen: USCIS "continues to accept the 08/28/24 edition of Form I-539 and 08/21/25 edition of Form I-765 and is not accepting the 09/15/26 edition of Forms I-539 and I-765." That reverses the warning we and others published, and it matters most to anyone filing an I-765 — DACA, TPS, asylum and adjustment applicants included — who was told to switch to the new edition. DHS says it disagrees with the order and will implement the rule if the order is lifted, so this is a postponement, not a cancellation: check the edition date on uscis.gov the day you file. Separately and unaffected by this order, Form I-485 does get a 09/18/26 edition on September 18, 2026 with no grace period.

Primary source: <https://www.uscis.gov/i-539>

### 2026-09-10 · CORRECTION

**Correction: the Affidavit of Support income table was two years stale, the U visa's sibling rule was wrong, and two official State Department pages disagree on whether entering the visa lottery costs $1.00 or nothing**

Fourteen verified defects across the procedures, datasets and tools trees, fixed in English and Spanish together. The most consequential: the Affidavit of Support pages published the 2024 Form I-864P income table — a sponsor for a household of four was told $38,750 when USCIS's chart, "effective beginning Mar. 1, 2026," requires $41,250 at 125% of the poverty guidelines; the table now renders live from our own HHS dataset with both the 125% and the active-duty 100% columns. The same pages said the sponsor's promise "lasts 10 years": 8 U.S.C. 1183a(a)(2)-(3) sets no term at all — the affidavit is enforceable until naturalization or 40 qualifying quarters, and the page's own list of ending events already said so. On the U visa, the site listed derivative siblings as "unmarried siblings under 21"; the statute says unmarried siblings under 18 on the date the principal applied, and only when the principal is under 21 — a principal 21 or older can include only a spouse and children. On the Diversity Visa pages, NACARA was described as adding 5,000 visas to a 60,000 cap: 8 U.S.C. 1151(e) sets the level at 55,000 and Pub. L. 105-100 subtracts up to 5,000 from it, so about 50,000 are available and no 60,000 cap exists. Those pages also called any pre-selection charge a scam. State's own fee table now lists a "Diversity Visa Registration Fee (paid at time of registration only by the principal applicant) $1.00" while State's DV entry page still says "There is no cost to register for the DV Program" — both are quoted and neither is declared the winner. The DV pages also promised a DV-2027 registration window in October-November 2025; State has published no DV-2027 instructions at all, and its instructions page still reads "The processing requirements below are for the DV-2026 program." On tax pages: an ITIN filer was told the American Opportunity and Lifetime Learning credits were available, but P.L. 119-21 § 70606 rewrote 26 U.S.C. 25A(g)(1) to require the taxpayer's own Social Security number "to taxable years beginning after December 31, 2025," so both close from tax year 2026 (a 2025 return is unaffected); the non-resident page said a 30% rate applies to US-source income generally, when the IRS says effectively connected income — wages included — is taxed "at graduated rates … the same rates that apply to U.S. citizens and residents" and the flat 30% reaches only unconnected FDAP income; the treaty page dated Hungary's termination for non-withholding taxes to January 1, 2025 when Treasury's own notice says January 1, 2024, and counted 68 treaties in force when the IRS flags Hungary "Treaty Terminated" (Belarus and Russia are flagged "Partially Suspended"). Also fixed: the naturalization pages said an absence of more than a year "automatically" breaks continuous residence without noting that 6-to-12-month absences are presumed to break it too (8 CFR 316.5(c)(1)), and described the 65/20 civics exception as a 20-question test needing 6 correct when the officer asks 10 from a designated bank of 20; the border-wait dataset claimed 82 land ports when the file holds 85 crossings at 53 ports; the TPS work-permit dataset headline said "seven terminations" when its own data shows 11 of 15 designations terminated; the asylum annual-fee pages still said the rule was "open for public comment" 73 days after comments closed on June 29, 2026; and Self was listed as an ITIN-friendly bank on six pages when it sells a Credit Builder Loan and a secured credit card, not a deposit account with a debit card.

Primary source: <https://www.uscis.gov/i-864p>

### 2026-09-10 · CORRECTION

**Correction: every state DMV page carried invented teen-driver ages, and told readers a driving-privilege card counts as an I-9 identity document**

A single template row was repeated across 52 English and 52 Spanish state DMV pages: "Learner's permit — typically 15-15.5 years old", "Provisional/junior license — typically 16-17 years old", and "Auto-converts to full license at 18." None of those figures came from any state. Delaware, the page that exposed it, sets the Level One Learner's Permit at "at least 16 years old and less than 18 years old" and its full-licence minimum at 17 — the page's own key-facts table already said 17, so the row contradicted the page it sat on. Every row now renders the value our own dataset holds for that state (website/data/dmv/state_general.json), and the generator reads the dataset instead of a guess. A second bullet on 53 English and 53 Spanish pages told readers a "standard or undocumented license" counts as an I-9 List B identity document; Delaware's DMV says its Driving Privilege Card "will NOT be considered a valid form of identification" and the card is printed "Not Valid for Identification" on its face, so the bullet was split and the caveat added. Delaware's own card row also said the card requires "DE residency for 6+ months + payment of DE income tax for 2+ years" — the DMV requires a Certification of Filing Compliance showing Delaware taxes were FILED for the previous two years, and publishes no months-of-residency test.

Primary source: <https://services.dmv.de.gov/DriverServices/drivers_license/DPC/index.shtml>

### 2026-09-10 · CORRECTION

**Correction: state DMV pages hinted a matrícula consular "may" be accepted — in the states whose own rules require US-agency proof of lawful presence**

"Depends on the state. [State] may accept matrícula consular under certain circumstances" appeared on the English and Spanish page of every jurisdiction that does NOT issue a licence or ID without regard to immigration status — precisely the states where a consular ID cannot carry an applicant. Texas puts the requirement in statute: an applicant who is not a US citizen "must present to the department documentation issued by the appropriate United States agency that authorizes the applicant to be in the United States" (Tex. Transp. Code § 521.142(a)). Kentucky tells non-US citizens they "must provide proof of identity and lawful status"; North Dakota requires "proof of identity, date of birth, and legal presence in the United States" from every applicant; Tennessee requires "Citizenship or Legal Presence"; Michigan accepts only "a Canadian driver's license or a valid foreign passport" among foreign identity documents. Each page now says a matrícula consular, issued by a foreign consulate rather than a US agency, cannot meet that requirement, and points at the agency's own current document list. Puerto Rico was written separately: it issues a provisional licence under Ley 97-2013, so its page distinguishes the two credentials instead of asserting a flat no.

Primary source: <https://statutes.capitol.texas.gov/Docs/TN/htm/TN.521.htm>

### 2026-09-10 · CORRECTION

**Correction: the SNAP gross-income limit had no elderly or disability exception, and benefit pages promised a child's benefits "never count against you"**

Fifty English and fifty Spanish SNAP state pages answered "how much do I get" with a flat "Max gross income: 130% FPL." Under 7 CFR 273.9(a) a household containing a member age 60 or older or with a disability "shall meet the net income eligibility standards" only — it is exempt from the gross-income test entirely — and categorically eligible households meet neither test. A household that would have read itself out of SNAP now sees the exception. Separately, across the Medicaid and SNAP state pages, the hubs and the public-charge guide, the site told readers that benefits used by their US-citizen children "never count against you." USCIS policy alert PA-2026-09, effective 18 September 2026, does say USCIS "does not attribute to the alien the receipt of means-tested public benefits if the benefit is received by the applicant's relatives, including children" — but it adds that where a relative the applicant is legally obliged to support qualifies "based on the alien's income or assets falling below a certain level, then officers should consider the alien's income or assets falling below the threshold as part of the assets, resources, and financial status factor." That caveat is now on every page that made the promise. The Spanish SNAP hub also still answered the public-charge question with a bare "No" eight days before the 2022 rule's rescission takes effect (91 FR 45324); it now carries the date.

Primary source: <https://www.ecfr.gov/current/title-7/section-273.9>

### 2026-09-10 · CORRECTION

**Correction: three know-your-rights errors — a regulation that never says "judicial", ICE's first courthouse directive described as a narrowing, and one E-Verify clock where there are two**

On the page whose whole thesis is the difference between a judge's warrant and an administrative one, we attributed the judicial qualifier to the regulation itself: "federal regulation instructs that immigration officers may not enter non-public areas without consent or a judicial warrant (8 CFR 287.8(f)(2))." The regulation says "either a warrant or the consent of the owner or other person in control of the site to be inspected" — the judge-signed requirement for a home comes from the Fourth Amendment, not from that text. The sensitive-locations timeline listed "2018 — internal narrowing — reduced courthouse limitations", preceded by a 2013 courthouse guidance we cannot source; ICE Directive 11072.1 (issued and effective 10 January 2018) records "Superseded: None" on its own header, which makes it ICE's first courthouse directive rather than a narrowing of anything. And the workplace page gave a single deadline after an E-Verify mismatch: "contest within 8 federal working days." E-Verify runs two clocks — 10 federal government working days from issuance of the mismatch to tell your employer you will act, then eight federal government working days from receiving the Referral Date Confirmation to contact DHS or SSA. A worker counting eight days from the mismatch was counting the wrong clock.

Primary source: <https://www.ecfr.gov/current/title-8/chapter-I/subchapter-B/part-287>

### 2026-09-10 · CORRECTION

**Correction: childcare pages sent parents to a "[State] Department of Human Services" that most states do not have**

The childcare-by-state generator ended its "immigrant-friendly states" section with "Verify with [State] Department of Human Services" on all 52 English and 52 Spanish state pages. Most states have no agency by that name — North Carolina runs SNAP and childcare through the Department of Health and Human Services, Arizona through the Department of Economic Security, and so on — so the sentence sent a reader searching for an office that does not exist, on a page that already renders the state's real portal, its CCDF programme name and its application methods a few lines above. Each page now points at those official contacts and at the state's childcare.gov page, which names the agency; the generator was corrected so a rebuild cannot restore the invented name.

Primary source: <https://childcare.gov/state-resources>

### 2026-09-10 · CORRECTION

**Correction: our Cuba and Nicaragua “voting from the US” pages described a procedure that does not exist — neither country lets citizens abroad vote**

Four pages (Cuba and Nicaragua, English and Spanish) told readers their country had “established consular voting… and/or postal voting” for citizens abroad, listed presidential, legislative and referendum ballots as available, and gave a registration deadline of “30-90 days before election day.” None of that is true for either country. Cuba's Ley No. 127, “Ley Electoral” (Gaceta Oficial No. 60 Ordinaria, 19 August 2019), art. 7 c) requires “residencia efectiva en el país por un período no menor de dos (2) años antes de las elecciones”, and art. 8 c) withholds the vote from anyone who does not meet that residence requirement — living in the US removes the right itself, and Cuba's President is elected by the deputies of the National Assembly (arts. 220-224), not by voters. Nicaragua's Ley No. 331 (reforms incorporated, La Gaceta – Diario Oficial No. 92, 20 May 2022), art. 109 makes an overseas vote conditional on the Consejo Supremo Electoral deciding, six months before the electoral process begins, that four operating conditions can be met, including an overseas voter registry it has never built; the decision has never been taken. The four pages were rewritten to quote the statutes, explain why no procedure exists, and say what a citizen can actually do; the same fabricated “30-90 day” deadline was removed from the other 20 voting-from-abroad pages, Mexico's real window was published (LGIPE art. 334: 1 September to 15 December of the year before the election) along with the internet-voting channel that 67.86% of the 2024 overseas roll used, and the generator template was corrected so a rebuild cannot restore the falsehoods.

Primary source: <https://www.gacetaoficial.gob.cu/sites/default/files/goc-2019-o60_0.pdf>

### 2026-09-10 · CORRECTION

**Correction: closed Nicaraguan consulates listed as open, two moved Mexican consulates, and a UN mission published as a consulate**

A sweep of the consulate directory found addresses that would send a reader to the wrong building or to no building at all. Nicaragua closed its consulates in Los Angeles and Houston on 19 January 2024 and in New Orleans on 20 January 2024 — in Los Angeles by a notice on the door reading “el Consulado de la Ciudad de Los Ángeles cesa funciones a partir de hoy 19 de enero de 2024” — and the San Francisco office stopped serving the public; only Miami, New York and Washington, D.C. still operate, yet our hub said “7 consular offices” and every city page read as open. Mexico's consulates in Oklahoma City and Fresno have moved: SRE's directory (last updated 6 August 2026) gives 1131 W Sheridan Ave., Oklahoma City, OK 73106, tel. (405) 753-5622 — our page had the old 401 Northwest 16th Street and a number that no longer reaches the office — and 7435 N Ingram Ave., Fresno, CA 93711 in place of 2409 Merced Street. The Honduras and Ecuador New York pages printed 866 United Nations Plaza with a green “verified” badge: that is each country's Permanent Mission to the United Nations, which issues no passports or civil-registry documents, and the actual consulate address sat further down the same page. The Argentine consulate in Atlanta is at 53 Perimeter Center East, Suite #500, Atlanta, GA 30346 (its own site, contact page updated 19/03/2025), not 245 Peachtree Center Avenue, its email is catla@mrecic.gov.ar, and its jurisdiction is Alabama, Georgia, Kentucky, Mississippi, South Carolina and Tennessee — North Carolina belongs to the Embassy in Washington and Florida to Miami, and Argentine consulates are fixed-jurisdiction, so the old list cost readers the appointment.

Primary source: <https://www.vozdeamerica.com/a/cierre-de-varios-consulados-de-nicaragua-en-eeuu-mexico-y-guatemala-impacta-a-la-diaspora-del-pais-centroamericano/7485761.html>

### 2026-09-10 · CORRECTION

**Correction: a geocoding bug pinned 104 consulates to the wrong city, and our sourcing lines claimed verifications that never happened**

Three sourcing defects, all fixed. First, the script that enriched our consulate dataset from OpenStreetMap matched a POI to a city with a containment test; when an OSM node carries no addr:city tag its city normalizes to the empty string, and an empty string is a substring of every city name, so the first tagless diplomatic POI in a country matched every city in it. That put 47 Mexican consulates on a node in Brownsville, Texas, 29 Guatemalan on a Miami node, 17 Honduran and 15 Dominican on Washington, D.C. nodes — published as each page's geographic source and used as its map pin. The false enrichment was stripped from 104 records and the matcher now requires a real city. Second, 32 Mexican consulate pages said their addresses were “cross-referenced against the U.S. State Department's foreign consular office directory”; that check was never run, and the Department no longer publishes such a directory — its page now renders one link and no list (read 2026-09-10) — so the sentence and the 52 pages that linked the directory were corrected. Third, 149 pages credited “datos del Ministerio de Relaciones Exteriores” for data whose own source field is the English Wikipedia list of that country's diplomatic missions; those lines now say what the data is. Separately, the by-state pages sent readers in a consulate-less state to neighbouring states chosen by geography rather than by whether they host a consulate — South Dakota's page named Iowa, Wyoming, Montana and North Dakota, all of which our own pages say host none, and the lists were circular — so all of them are now built from the consulate data and name the actual offices.

Primary source: <https://api.openstreetmap.org/api/0.6/node/9384986783.json>

### 2026-09-10 · CORRECTION

**Correction: our green-card-to-citizenship pages still described the 2008 civics test — USCIS has given the 2025 test since October 20, 2025**

108 pages (54 English + 54 Spanish) told readers the naturalization civics test is 10 questions drawn from a 100-question list with 6 correct to pass, and pointed them at the 100-question study list. USCIS's own Study for the Test page says: "We will administer the 2025 naturalization civics test to aliens who file Form N-400, Application for Naturalization on or after Oct. 20, 2025. The 2025 naturalization civics test is an oral test consisting of 20 questions from the list of 128 civics test questions. You must answer 12 questions correctly to pass the 2025 test." Applicants who filed before October 20, 2025 still take the 2008 test, and applicants 65 or older with 20+ years as a permanent resident answer 10 questions from a specially selected bank of 20. Every page now states which test applies by filing date, and the generator templates that produced them were corrected too.

Primary source: <https://www.uscis.gov/citizenship/find-study-materials-and-resources/study-for-the-test>

### 2026-09-10 · CORRECTION

**Correction: the U visa costs $0, not $440 — 16 pages quoted a fee USCIS does not charge**

A cost FAQ repeated across 16 path-to-status pages said "U-visa: $440 (fee waiver available)" — and on the two U-visa pages themselves the body repeated the $440 a second time, contradicting the same page's own "Fee: FREE" heading. Form G-1055 (edition 09/09/26), the fee schedule USCIS publishes, lists Form I-918 Petition for U Nonimmigrant Status at $0 for general filing, and $0 for Supplement A and Supplement B; Form I-192 is also $0 for U petitioners. There is no fee and nothing to waive. Because those FAQ answers render as FAQPage structured data, the wrong figure was also being fed to search engines.

Primary source: <https://www.uscis.gov/g-1055>

### 2026-09-10 · CORRECTION

**Correction: our Selective Service table said everyone must register — five categories that Selective Service exempts were printed as "YES"**

The who-must-register table on both language versions marked every row "YES," including lawful non-immigrants on current non-immigrant visas, H-2A seasonal agricultural workers, people confined for medical reasons, people continually confined by disability, and members of the Armed Forces on active duty. Selective Service's own Who Needs to Register chart marks all of those "No" or "No*", and Form N-400 agrees for non-immigrants ("Do not select 'Yes' if you were a lawful nonimmigrant for all of that time period"). The cause was a rendering bug, not bad data: our parsed dataset had the correct "no" values, but the page generator truth-tested a string, and the non-empty string "no" is true in Python, so every row printed YES. The generator and the pages are both fixed. The same pages also said the registration deadline is 30 days BEFORE the 26th birthday (it attaches within 30 days AFTER the 18th birthday, with late registration accepted until the day you turn 26), cited the wrong N-400 item (it is Part 9, Items 22.a.-22.c. on the 01/20/25 edition, not Part 11 Question 38), and described a 5-to-8-year naturalization bar that does not exist.

Primary source: <https://www.sss.gov/wp-content/uploads/2026/07/WhoNeedstoRegister.Final.pdf>

### 2026-09-10 · CORRECTION

**Correction: the expanded expedited-removal designation became operative July 17, 2026 — not June 23**

Four pages headlined June 23, 2026 as the date the January 2025 nationwide expansion came back into force. On June 23 a D.C. Circuit panel did vacate the district court's stay in Make the Road New York v. Mullin, No. 25-5320 — but the Clerk withheld issuance of the mandate the same day, so the policy remained blocked. The government moved on June 26 for a stay pending appeal, and the court granted it on July 17, 2026 while denying early issuance of the mandate. AILA's summary of that order (AILA Doc. No. 26062463) reads: "The expansion designation is now unblocked and in effect." The window matters: an interior expedited-removal order issued between June 23 and July 17, 2026 was issued while the expansion was still blocked.

Primary source: <https://www.aila.org/library/d-c-circuit-allows-expansion-of-expedited-removal>

### 2026-09-10 · CORRECTION

**Correction: EB-5 filing fee is $4,675, not $11,160 — and the capital lock-up is 2 years, not 5**

Both EB-5 pages quoted an $11,160 filing fee, a "12-24 month" I-526E wait, an at-risk rule broken by "returning funds before 5+ years," a total USCIS-fee line of "~$13,000-$15,000," a Regional Center Program "currently SUSPENDED periodically," and in-state tuition as a benefit derivatives receive. Form G-1055 (ed. 09/09/26) prices Form I-526E at $3,675 plus the separate $1,000 EB-5 Reform and Integrity Act fee on an initial filing — $4,675 — and the three-form total (I-526E + $1,000 + I-485 $1,440 + I-829 $3,750) is $9,865. USCIS Policy Manual 6 USCIS-PM G.2 says: "For petitions filed on or after March 15, 2022, the capital must be expected to remain invested for not less than 2 years." The 2022 Act reauthorized the Regional Center Program, ending the lapse-and-reauthorize cycle. USCIS's live 80th-percentile figure for I-526E at the Immigrant Investor Program Office is about 35 months. A green card makes a person eligible to establish state residency for tuition; it does not itself confer in-state rates.

Primary source: <https://www.uscis.gov/policy-manual/volume-6-part-g-chapter-2>

### 2026-09-10 · CORRECTION

**Correction: 14 utility pages sent readers to apply for the Affordable Connectivity Program, which ended June 1, 2024**

A body bullet on 14 pages offered "ACP (Affordable Connectivity): $30/month for internet, $75 on tribal lands," and a FAQ answer on 7 of them named the ACP as a live low-income discount — while one of the same pages already said elsewhere that the program had ended. USAC, which administered the program for the FCC, states: "The ACP ended on June 1, 2024, due to a lack of additional funding from Congress." There is no successor. Every one of those pages now points to Lifeline instead, which is live: up to $9.25 a month off phone or internet, and up to $34.25 a month on qualifying Tribal lands. Note for the record: the FCC's own ACP fact sheet returns HTTP 403 to automated requests, so this was verified at USAC, the FCC's administrator, and at lifelinesupport.org.

Primary source: <https://www.usac.org/about/affordable-connectivity-program/>

### 2026-09-10 · CORRECTION

**Correction: HPV is not a required immigration vaccine — 30 vaccination pages listed it as one**

A context block repeated on 30 pages (15 English + 15 Spanish) listed "HPV (age 9-26 catch-up)" among the vaccinations CDC's Technical Instructions for Civil Surgeons require, and dated those instructions to a "most recent major update 2023." CDC's vaccination page for civil surgeons lists exactly these required vaccines: diphtheria, tetanus, pertussis, polio, measles, mumps, rubella, rotavirus, Haemophilus influenzae type b, hepatitis A, hepatitis B, meningococcal disease, varicella, pneumococcal disease and influenza. HPV does not appear anywhere on it, and neither does zoster; the page's own last-updated date is March 11, 2025. A reader who believed the old text could have paid for a three-dose HPV series USCIS never asks for.

Primary source: <https://www.cdc.gov/immigrant-refugee-health/hcp/civil-surgeons/vaccination.html>

### 2026-09-10 · CORRECTION

**Correction: a Form I-693 signed on or after November 1, 2023 has no 2-year expiry — it lasts as long as the application it was filed with**

The immigration medical exam hub said the I-693 is "valid for 2 years from the date the civil surgeon signs," contradicting its own child pages. USCIS Policy Manual 8 USCIS-PM B.4 says a properly completed Form I-693 signed on or after November 1, 2023 "can only be used as evidence to show that the applicant is not inadmissible under the health-related grounds for the entire period the immigration benefit application with which the Form I-693 is submitted is pending," while one signed before that date "retains evidentiary value for 2 years from the date of the civil surgeon's signature." The same pages also linked to my.uscis.gov/findadoctor for finding a civil surgeon, which now returns HTTP 404; the working page is uscis.gov/tools/find-a-civil-surgeon, and that link was replaced on all four pages that carried it.

Primary source: <https://www.uscis.gov/policy-manual/volume-8-part-b-chapter-4>

### 2026-09-10 · CORRECTION

**Correction: a federal-document apostille costs $20, not $8 — and China and Canada now accept apostilles**

Both apostille pages priced the State Department's Office of Authentications service at about $8 per document and listed China and Canada as non-Hague countries needing full embassy legalization. The Schedule of Fees for Consular Services, 22 CFR 22.1, item 46, reads: "Authentications (by the Office of Authentications domestically): (a) Each basic authentication service $20." The HCCH status table for the 1961 Apostille Convention shows China acceded on 8 March 2023 with entry into force 7 November 2023, and Canada on 12 May 2023 with entry into force 11 January 2024. Both now accept an apostille.

Primary source: <https://www.ecfr.gov/current/title-22/chapter-I/subchapter-J/part-22/section-22.1>

### 2026-09-10 · CORRECTION

**Correction: our own methodology page advertised four automated monitors that do not exist, and a 90-day re-verification guarantee we do not meet**

The methodology page (both languages) listed an EOIR statistics scraper, a state DMV contact verifier, a per-country consulate verifier and a daily TPS designation tracker, and described the USCIS processing-times pull as weekly. None of those four exists in our scheduled workflows, and the processing-times pull is monthly and currently run by hand because USCIS renders the data behind Cloudflare. The page also promised that "every 90 days minimum, every page is re-verified" — a promise a reader can falsify from our own Last Verified dates. The monitor table now lists only what actually runs (Federal Register, CBP border waits, State Department visa waits and litigation dockets daily; FX rates weekly; Visa Bulletin plus fee-change watcher monthly on the 16th; HRSA health-center data quarterly; a weekly source-link health check; and the hand-run monthly USCIS processing-times pull), says in plain terms which monitors do not exist, and replaces the 90-day guarantee with the honest version: each page prints the date it was last checked. The same 90-day promise was corrected on the editorial-standards pages, and the meta description's "6,000+ pages" was corrected to 4,500+ — our live sitemaps carry 2,268 English and 2,268 Spanish URLs.

Primary source: <https://migrantusa.com/en/sitemap.xml>

### 2026-09-10 · CORRECTION

**Correction: at least eight federal Circuits protect recording the police, not six — and Riley bars searching your phone, not seizing it**

Both recording-rights pages counted six Circuits and told readers in the remaining Circuits the question was unsettled. Irizarry v. Yehia, 38 F.4th 1282 (10th Cir. 2022) says: "We recognize that the right exists and was clearly established when the incident occurred" — which is what defeats qualified immunity in Colorado, Kansas, New Mexico, Oklahoma, Utah and Wyoming. Sharpe v. Winterville Police Department, 59 F.4th 674 (4th Cir. 2023) holds "that livestreaming a police traffic stop is speech protected by the First Amendment" (the officer there still received qualified immunity because the right was not yet clearly established in that circuit). Both pages also said officers "cannot lawfully seize your phone, search it, or delete recordings without a warrant." Riley v. California, 573 U.S. 373 (2014) is narrower: its holding "is not that the information on a cell phone is immune from search; it is that a warrant is generally required before a search," and officers "remain free to examine the physical aspects of a phone" and may secure it while seeking that warrant. Telling readers a seizure is unlawful invites the confrontation the page warns against. The Spanish page separately named 42 U.S.C. 1983 as the remedy on a page about filming ICE; Section 1983 reaches only state actors, so both pages now say that a claim against a federal officer would be a Bivens action, sharply narrowed by Egbert v. Boule, 596 U.S. 482 (2022).

Primary source: <https://www.ca10.uscourts.gov/sites/ca10/files/opinions/010110708555.pdf>

### 2026-09-10 · CORRECTION

**Correction: an ICE detainer's 48 hours exclude Saturdays, Sundays and holidays — across a holiday weekend that is four or five days**

Four pages said a detainer asks a jail to hold someone "up to 48 hours" past their release. The regulation, 8 CFR 287.7(d), says the agency "shall maintain custody of the alien for a period not to exceed 48 hours, excluding Saturdays, Sundays, and holidays." That exclusion is the number a family actually plans a pickup around, so all four pages now carry it.

Primary source: <https://www.ecfr.gov/current/title-8/chapter-I/subchapter-B/part-287/section-287.7>

### 2026-09-10 · CORRECTION

**Correction: Sudan and Ukraine TPS run THROUGH October 19, 2026 under extensions — neither is terminated**

Our I-821 pages said Sudan and Ukraine "terminate October 19, 2026." USCIS's Sudan country page reads: "TPS Continues Through: Oct. 19, 2026, under the extension of Sudan's TPS designation announced in the Jan. 17, 2025, FRN (90 FR 5944)"; the Ukraine page reads "TPS Designated Through: Oct. 19, 2026" (90 FR 5936). Neither has a published termination notice, and DHS can extend either again — October 19 ends an extension period, it does not terminate a designation. Both pages now also carry the separate, earlier date that the country pages publish: the EAD auto-extension by Federal Register notice ended April 19, 2026, which is proof of status rather than status itself.

Primary source: <https://www.uscis.gov/humanitarian/temporary-protected-status/temporary-protected-status-designated-country-sudan>

---

## Citing a change

Cite the primary government source for the underlying fact, and this record for
the change history. See [README](README.md#cite-this-dataset) for the citation
formats and DOI.

