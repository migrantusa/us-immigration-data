# What changed in US immigration data

A dated record of changes to US government immigration data, each verified
against its primary source. Government agencies publish the *current* value and
overwrite it; this file keeps the change itself.

**This page is generated** from [`data/change_log.json`](data/change_log.json)
(machine-readable, with the Spanish text and the affected dataset paths) by
[`scripts/refresh.py`](scripts/refresh.py). Canonical human-readable version, with
full context on each entry: <https://migrantusa.com/updates/>

Showing the 40 most recent of 166 recorded changes. Source data as of 2026-09-16.

---

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

### 2026-09-10 · CORRECTION

**Correction: four USCIS wait times on our pages were far shorter than USCIS's own published figures**

Eight pages quoted wait ranges that our own USCIS processing-times dataset contradicts. VAWA self-petitions (Form I-360) were described as "18-36 months" and, in the page metadata, as "about 15.5 months" — 15.5 was the median across four unrelated I-360 categories, not the VAWA figure; USCIS's 80th-percentile figure for VAWA is about 51.5 months. The I-601A provisional unlawful-presence waiver was given as 12-18 months against USCIS's 27.5. The I-526E was given as 12-24 months against 35. Removing conditions on residence (Form I-751) was given as 18-36 months against 33.5 months at service centers and 37.0 across field offices. The two I-360 pages now render the live dataset table instead of a hand-typed one, so the figures cannot drift again, and every other page states the USCIS figure with a pointer to check it live. Understating an I-601A wait by a year is the difference between a planned trip abroad and a family stranded there.

Primary source: <https://egov.uscis.gov/processing-times/>

### 2026-09-10 · CORRECTION

**Correction: replacing a Form I-94 costs $584, not $24 — the $24 is an additional fee sent separately**

A fee-comparison table on six pages showed Form I-94 replacement as "Free for most" before H.R.1 and "$24" after. Form G-1055 (ed. 09/09/26) shows Form I-102 at $560 general filing, with the Pub. L. 119-21 I-94 fee of $24 listed as an "Additional Form I-94 Fee" that "you must submit... separately from the filing fee." So the before figure was never free and the after figure is $584. A reader who budgeted $24 would have had the filing rejected for the wrong fee.

Primary source: <https://www.uscis.gov/g-1055>

### 2026-09-10 · CORRECTION

**Correction: most Advance Parole categories cost $580 filed online, not a flat $630**

Both Form I-131 pages quoted a flat $630 for Advance Parole. Form G-1055 (ed. 09/09/26) lists $630 paper / $580 online for the pending-I-485, pending-initial-I-821, DED, DACA and TPS Travel Authorization categories; only the Re-Entry Permit row is paper-only at $630, and T and U holders pay $0. The pages already carried the separate Pub. L. 119-21 immigration parole fee that CBP collects at the port of entry each time an Advance Parole document is used; that remains unchanged.

Primary source: <https://www.uscis.gov/g-1055>

### 2026-09-10 · CORRECTION

**Correction: if your DACA lapsed more than a year ago, the filing is an initial request — and USCIS is barred from granting those**

The DACA renewal calculator told readers that a DACA expired more than a year ago "may have to be filed as if it were a new request, which is more complex and uncertain." USCIS's DACA page is blunter: "USCIS will continue to accept initial requests but will not process initial DACA requests at this time," and "DHS is prohibited from granting initial DACA requests and related employment authorization under the final rule." There is no path to a grant right now, though the fees would still be charged. The same pages said filing more than 150 days out "can lead to rejection"; USCIS says only that filing earlier than 150 days "will not result in a faster decision," and names no rejection consequence.

Primary source: <https://www.uscis.gov/DACA>

### 2026-09-10 · RULE-CHANGE

**DHS interim final rule: a child born on or after September 4, 2026 to a “foreign government employee” can register as a permanent resident — comments close October 5, and a Maryland injunction limits who it reaches**

The Federal Register printed DHS's interim final rule on September 9, 2026 (FR doc 2026-18345, RIN 1615-AD24, DHS Docket No. USCIS-2026-0496), amending 8 CFR parts 101 and 264. It decides no one's citizenship: Trump v. Barbara still stands, a child born in the United States to undocumented parents is a U.S. citizen at birth, and every Executive Order 14418 category requires that neither parent is a U.S. citizen. What the rule changes is the registration mechanism — it replaces “foreign diplomatic officer” with the broader “foreign government employee,” which includes persons employed by a foreign embassy or consulate who are nationals of that foreign country and excludes third-country nationals, contractors, personal employees of officials and most state-owned-enterprise employees, and it lets those children voluntarily register as lawful permanent residents on Form I-485, with Form G-325R revised for those who do not. In the rule's own words it “is effective on September 4, 2026” and “will apply to children born to foreign government employees on or after September 4, 2026; children born to a foreign government employees prior to that date will be treated consistently with the regulations in place at the time of their birth,” and comments “must be received on or before October 5, 2026.” DHS adds that it will not implement the rule against any member of the certified class in Casa Inc. v. Trump, No. 8:25-cv-00201 (D. Md.), while the preliminary injunction entered there on September 2, 2026 stands; the government moved to dissolve or stay that injunction on September 8, 2026 (ECF 183) and the motion is pending. The State Department published its own implementation plan on September 4; the Social Security Administration and the Justice Department had published nothing as of September 10, 2026, and any family with a child born on or after September 4, 2026 to a parent employed by a foreign government, embassy, consulate or international organization should take the question to a licensed immigration attorney.

Primary source: <https://www.federalregister.gov/documents/2026/09/09/2026-18345/registration-of-lawful-permanent-residence-for-children-born-to-foreign-government-employees-in-the>

### 2026-09-10 · CORRECTION

**Correction: our Section 8 eligibility list invented one immigration category and left out four real ones**

Our housing hub told readers that the eligible statuses for Section 8 and public housing are US citizen, permanent resident, refugee or asylee, Cuban-Haitian entrant and "VAWA self-petitioner". A VAWA self-petition is not on the statutory list at all, and the list omitted four categories that are: people paroled under INA 212(d)(5), people granted withholding of removal under INA 241(b)(3), people with temporary or permanent residence under INA 245A, and Marshall Islands, Micronesia and Palau citizens under the Compacts of Free Association, who also get a local preference under 24 CFR 5.506(c). Rewritten to the categories in 42 U.S.C. 1436a(a) as 24 CFR 5.506(a) applies them, on 2 pages (EN + ES) and in the generator scripts that produce them. VAWA still gives survivors separate housing protections — confidentiality, continued occupancy and emergency transfer — but not voucher eligibility.

Primary source: <https://www.law.cornell.edu/uscode/text/42/1436a>

### 2026-09-10 · CORRECTION

**Correction: our SNAP pages overstated the average benefit, printed a household-of-four figure above the legal maximum, and named an agency that does not exist in most states**

Three template defects were repaired on 102 SNAP pages (51 EN + 51 ES). (1) "Average: $200-$300 per person/month" — USDA FNA reports the actual FY2025 national average monthly benefit per person as $188.30, so the whole quoted range sat above the real figure. (2) "Household of 4: ~$800-$1,200/month" — the FY2026 federal maximum for a four-person household in the 48 states and DC is $994, so the upper bound exceeded the legal maximum by $206, on pages whose own allotment table already printed $994. (3) "Visit the [State] Department of Human Services" appeared on all 50 state pages, but most states have no agency by that name; the step now points at the official contacts block already on each page, built from the USDA FNA state directory. The generator scripts were corrected too.

Primary source: <https://www.fna.usda.gov/sites/default/files/resource-files/snap-annualsummary-8.pdf>

### 2026-09-10 · CORRECTION

**Correction: we told mixed-status families not to include an ineligible member's information — federal rules require the state to count that income**

On 102 SNAP pages (51 EN + 51 ES) the mixed-status advice read "Don't include ineligible members' information" / "NO incluya información sobre miembros inelegibles". Under 7 CFR 273.11(c)(3)(i) the State agency "must count all or, at the discretion of the State agency, all but a pro rata share, of the ineligible alien's income and deductible expenses and all of the ineligible alien's resources", and a SNAP household under 7 CFR 273.1(a) is everyone who lives together and customarily buys and prepares food together. Following our old wording produced an under-reported application and an overpayment the state can bill back. The corrected text separates the two rules that actually apply: the non-applicant's status does not have to be documented (7 CFR 273.4(b)(2)), but their income and resources are counted for the eligible members' allotment.

Primary source: <https://www.ecfr.gov/current/title-7/section-273.11>

### 2026-09-10 · CORRECTION

**Correction: work-authorized non-residents are not categorically shut out of Medicare, and DC's Health Care Alliance no longer takes new adults 26 and older**

Two categorical claims were repaired. Our Medicare page said a work-authorized non-permanent-resident is "generally not eligible for Medicare". 42 U.S.C. 426(a) grants Part A at 65 to anyone entitled to monthly Social Security benefits under section 402 and sets no citizenship or green-card condition; 42 U.S.C. 402(y) pays those benefits to an alien who is lawfully present, which 8 CFR 1.3 defines to include deferred action, TPS and DED. With 40 quarters, that person gets premium-free Part A and can then enroll in Part B under 42 U.S.C. 1395o(1). What is closed is the buy-in, open under 1395o(2) only to citizens and LPRs of five continuous years. Separately, our Medicaid state table said DC's Alliance covers "all adults regardless of status"; DHCF's own published changes for October 1, 2025 are "No new enrollees 26 and older" and an income limit cut "from 215% of the federal poverty level to 138%".

Primary source: <https://www.law.cornell.edu/uscode/text/42/426>

### 2026-09-10 · CORRECTION

**DMV pages: we told readers a non-REAL-ID license means you cannot board a domestic flight, cited the wrong federal rule, and said most states issue a state ID regardless of status**

A source-by-source re-read of the 127-page DMV cluster on Sept. 10, 2026 corrected six template claims and eight state-specific ones. (1) Every state page carried an absolute: without a REAL ID "you cannot board a domestic commercial flight in the US." TSA's own identification page now says the opposite: "Starting February 1, 2026, if you are unable to provide the required acceptable form of ID at a TSA checkpoint, you will have the option to pay a $45 fee to use TSA ConfirmID. TSA will then attempt to verify your identity so you can begin the airport security screening process." TSA puts the check at "an average of 10-15 minutes; however, it could take 30 minutes or more." All 106 English and Spanish pages that carried the sentence now say that, and that you are still refused if TSA cannot verify you; the /dmv/ hub and 13 more state pages carried the same absolute in other words ("cannot be used to board a domestic flight") and now say the card is not accepted as identification, which is what is actually true. (2) The same block cited 49 CFR 1560 as the REAL ID authority on 104 pages. 49 CFR part 1560 is the Secure Flight Program and contains no REAL ID provision; the REAL ID rule is 6 CFR part 37, and the pages now cite 6 CFR 37.5(b) plus 37.5(d)(4), which lets federal agencies phase enforcement in but requires them to "achieve full enforcement of the requirements of paragraphs (b) and (c) of this section no later than May 5, 2027." (3) The non-driving state-ID row on 104 pages said "Status not required in most states for ID-only." NCSL counts "Nineteen states and the District of Columbia" whose laws let unauthorized immigrants obtain a credential - a minority, not most - and not all of those extend it to the ID card. (4) The Florida SB 1718 pages named only Connecticut's "Drive Only" and Delaware's "Driving Privilege Only" classes. FLHSMV publishes a second list on the same page - California, Colorado, DC, Hawaii, Illinois, Maryland, Massachusetts, Minnesota, Nevada, New Jersey, New Mexico, New York, Oregon, Rhode Island, Utah, Vermont, Virginia and Washington - whose non-REAL-ID licenses "may be invalid in the state of Florida if presented by a driver who is not lawfully present in the United States." Our own page then advised readers to consider California, Illinois, New Jersey, New York or Washington. (5) The Colorado CDL row gave no warning that, per the Colorado DMV, "effective Monday, September 29, 2025, the Colorado DMV has paused the issuance and renewals of term-limited (non-domiciled) Commercial Driver Licenses (CDLs) and Commercial Learner Permits (CLPs) to temporarily lawfully present residents until further notice." (6) The FAQ "Do they accept matricula consular?" asserted on 40 pages that the state accepts it "under certain circumstances" with no state source; it now sends readers to each agency's acceptable-document list. State fixes: Colorado's Standard fees had been read off the REAL ID table and were stale ($34 / $21.50 / $13.30 become the current $36 / $23.00 / $14.00); the Colorado credential's banner was quoted truncated, hiding the voting and public-benefit limits, and its 3-year validity and CRS 42-2-501 to 506 basis were missing; "such as providing state tax returns" was NCSL's 2013 description of SB13-251 and appears nowhere in Colorado's current document set; Arizona's "8 years; expires when driver turns 65" contradicted A.R.S. 28-3171(A), which makes the license valid until the 65th birthday and keys five-year renewals to age 60; Hawaii's limited-purpose license was cited to HRS 286-101.5 instead of 286-104.5, whose subsection (c) requires a reverse-side legend broader than "LIMITED PURPOSE"; a scraped Wikipedia sentence was serving as Hawaii's agency NAME in five places on each Hawaii page; New Jersey and New York said lawful status is required for the standard license when NJ MVC issues it "without regard to immigration status" and NY's Green Light Law "allows all New Yorkers age 16 and older to apply for a standard, not-for-federal purpose, non-commercial driver license or learner permit regardless of their citizenship or lawful status in the United States" (New York's non-driver ID card is the exception NY DMV names: "The Green Light Law does not apply to Non-Driver ID cards."); and the Minnesota fee link on four pages, which those pages' own cost FAQ defers to, is a 404 - the whole dps.mn.gov tree returns 404 today - so those cells now point to the fee schedule in Minn. Stat. sec. 171.06 - the same statute that settles two more Minnesota rows, since subd. 3(d) says the application "must not provide for identification of ... the applicant's citizenship, immigration status, or lawful presence in the United States" and bars DVS from asking, while our table said lawful status was required for both the standard license and the ID card.

Primary source: <https://www.tsa.gov/travel/security-screening/identification>

### 2026-09-10 · CORRECTION

**Correction: two of the four immigration hotlines we published on 104 legal-aid pages were numbers that do not exist**

Every state legal-aid page carried a "Specific-case hotlines" block listing "Asylum: RAICES (1-866-RAICES-4)" and "Detention: NIPNLG (1-800-867-2924)". Neither number is published by the organization it was attributed to. RAICES' own contact page publishes "+1 (833) 372-4237" and nothing in the 866 range; 1-866-RAICES-4 dials 1-866-724-2374, a number RAICES does not list anywhere. NIPNLG's contact page publishes exactly two numbers, "Phone: (617) 227-9727" and "Fax: (617) 227-5495", and the string 867-2924 does not appear on the site at all. A person in detention, or a family trying to reach an asylum organization, was being handed a dead or misrouted number at the moment it mattered most. All 104 pages (52 EN + 52 ES) now carry RAICES 1-833-372-4237 and the National Immigration Project (NIPNLG) (617) 227-9727, plus the ICE ERO Detention Reporting and Information Line 1-888-351-4024, which ICE publishes at ice.gov/contact/ero. The two numbers in the same block that were already correct were re-verified at the source and left alone: the National Domestic Violence Hotline publishes "1.800.799.SAFE (7233)" and the National Human Trafficking Hotline publishes "1-888-373-7888". The generator that stamps this block onto every state page was corrected in the same pass.

Primary source: <https://nipnlg.org/contact>

### 2026-09-10 · CORRECTION

**Correction: our USCIS office pages sent readers to "myUSCIS.com", a lookalike domain that redirects to a private medical-exam site, and told them a few walk-in slots exist**

All 104 USCIS field-office pages (52 EN + 52 ES) told readers to schedule an InfoPass appointment "via myUSCIS.com". Checked on 2026-09-10, https://myuscis.com answers HTTP 301 with Location: http://www.uscismedicalexams.com/ — a private commercial site, not a government one. The USCIS account portal is my.uscis.gov, which does brand itself "myUSCIS"; the word was right, the ".com" turned it into exactly the lookalike-domain pattern USCIS's own Avoid Scams program warns about. The pages now point to my.uscis.gov and give the USCIS Contact Center number USCIS publishes, 800-375-5283 (TTY 800-767-1833). The same pages' appointment FAQ said "few walk-in slots available", contradicting a line further down the same page; USCIS states categorically: "USCIS field offices do not allow walk-ins. You must have an appointment to visit an office." That FAQ now says an appointment is required for every purpose. The cluster hub also said "USCIS operates 93 field offices nationwide" and "walk-ins generally not allowed". Two independent sources refute 93: the USCIS Field Operations Directorate page says the directorate includes "88 field offices", and USCIS's own field-office-by-ZIP file dated 2026-07-29 lists 92 domestic field offices. The hub now quotes both figures rather than picking one, and states the no-walk-ins rule as USCIS states it. The two generator scripts that write this block were corrected in the same pass.

Primary source: <https://www.uscis.gov/about-us/find-a-uscis-office/field-offices>

### 2026-09-10 · CORRECTION

**Correction: we called free IRS Taxpayer Assistance Centers fee-based Certifying Acceptance Agents, printed the word "none" where an address should be, and hid "this TAC is currently closed" on 34 offices**

Three defects across the 104 IRS-office pages (52 EN + 52 ES). (1) Every page said "many TACs are designated as Certifying Acceptance Agents" and its FAQ named an "ITIN-Certifying Acceptance Agent" designation. The IRS's own "Compare options to apply in person" table lists them as separate options: "IRS Taxpayer Assistance Center with ITIN services | Free | Reviews W-7: Yes | Helps complete W-7: No | Authenticates most supporting documents: Yes" against "Certifying Acceptance Agent | Fee-based | Yes | Yes | Yes". Calling a free IRS office a CAA implied a charge that does not exist, and implied help completing the W-7 that a TAC does not give. (2) The office tables printed the IRS locator's literal placeholder string "none" into the Address, Phone and Hours cells for 35 offices — a row that promised an office in a city and then showed nothing — while dropping the locator's note for that office. Our own dataset held the missing hours all along: the Cedar Rapids, Iowa row showed no address, no phone and no hours while the data said "This TAC opens 10 a.m. - Noon Tuesday and Thursday ONLY". The same dropped-notes bug hid "*This TAC is currently closed*" on 34 offices, 23 of which rendered a full address, a phone and "8:30am - 4:30pm" hours — the pages were sending readers to closed IRS offices. Empty cells now say so, and the locator's standing note is printed; dated one-off notes are deliberately not surfaced, because a May-dated closure would read as current. (3) The freshness line stamped a September verification over a directory snapshot taken 2026-05-27 (only DC, HI, MT and SC were reconciled later, on 2026-07-22). Each page now says which date the directory was captured and separately when the page was reviewed. The generator was fixed, and so was the CI gate that had been requiring the pages to print "none" — it now imports the renderer's own cell composer, so gate and generator cannot drift again.

Primary source: <https://www.irs.gov/tin/itin/how-to-apply-for-an-itin>

### 2026-09-10 · CORRECTION

**Correction: our BIA-recognized directory listed organizations DOJ does not recognize, ran on a roster four and a half months old, and called a listing count an organization count**

The 104 BIA-recognized-help pages (52 EN + 52 ES) were built from the EOIR Recognition & Accreditation Roster of April 20, 2026. The live roster is stamped "Report Last Updated on: 09/06/26", and re-pulling it changed the tables materially. Two rows were phantoms on a page that opens by telling readers it lists organizations "currently authorized by the U.S. Department of Justice": "Immigrant Legal Aid Foundation" (New York, 1740 Broadway, (917) 647-2023) returns zero hits for its name, its street and its phone in both current rosters, while control searches for sibling New York organizations on the same page do hit; and "Dreamers2gether Inc." was listed with a Houston, Texas office at 5211 Brookglen Dr, (203) 437-7566, when the organization's only office on the roster is "Principal Office / 14 N Main Street / Waterbury, CT 06702 / (202) 313-1951". Presenting an unlisted organization as DOJ-recognized is the exact risk these pages' own notario-fraud warning is about. Three published addresses had also moved: American Organization for Immigrants is at 1800 NE Loop 410, Suite 310, San Antonio, TX 78217 (not 702 Donaldson Avenue); Community Response Coalition of Kentucky at 210 East High Street, #9, Lexington, KY 40507 (not 153 Patchen Drive); Catholic Social Services, Archdiocese of Philadelphia Immigration Legal Services at 4404 N 5th Street, Philadelphia, PA 19140 (not 222 N. 17th Street). Separately, every page said "As of the 2026-04-20 EOIR roster: 1,452 recognized organizations operate 1,564 offices nationwide." 1,452 was our own count of roster LISTINGS — one per organization per city — not organizations; the alphabetical roster's own header prints "Number of Recognized Organizations: 949". The sentence now gives both and says which is which. Every page also claimed the roster "is updated quarterly"; 09/06/26 is not a quarterly step from 04/20/26 and the roster PDF says nothing about cadence, so the pages now tell readers to check the "Report Last Updated" date the file prints at the top. The parser was fixed to read that date out of the PDF instead of carrying a hardcoded one, and the immigration-court legal-deserts join that reads this dataset was rebuilt, which moved Louisiana from 7 recognized nonprofits to 6 and its ratio from 1.8 to 1.5 per court.

Primary source: <https://www.justice.gov/eoir/recognition-accreditation-roster-reports>

### 2026-09-10 · CORRECTION

**Correction: we told parents they must prove their own immigration status to get a Social Security number for their US-born child — SSA asks for identity and relationship, not status**

The 10 Social Security pages (5 EN + 5 ES) listed "Parent's proof of status (USC, LPR, or eligible status)" among the documents needed for a newborn's SSN. SSA's own publication for citizen children, EN-05-10023, says: "No matter where you apply, you will need to: Show us original documents proving your child's: U.S. citizenship. Age. Identity. Show us documents proving your identity and your relationship to your child." Nowhere does SSA ask a parent for immigration status — and the same page's own FAQ already said status is not a factor, so the page contradicted itself. The practical harm is specific: an undocumented parent reading our document list would conclude their US-citizen baby cannot get a number. Four more claims on the same pages were repaired against SSA. The processing table ("Online: 2-3 weeks / By mail: 4-6 weeks / In person: same appointment or 2-3 weeks") is replaced by SSA's single published figure — "Once your application is approved, you'll receive a Social Security card with your number on it by mail in 5 to 10 business days" — and by SSA's statement on the replacement page that "Your local Social Security office cannot print one for you," which kills the same-appointment claim. "Online: ssa.gov/forms" is replaced by how SSA says the online path works: start at ssa.gov/number-card, then finish at a local office; ssa.gov/forms is only where Form SS-5 is printed. "The 2023 Inflation Reduction Act expanded SSA staffing" was deleted: the enacted law, Public Law 117-169, was signed August 16, 2022, not 2023, and a full-text search of it returns zero occurrences of "Social Security Administration". "Approximately 5 million new SSN cards in FY 2024 and approximately 13 million name-change requests" was deleted as untraceable — the page's only cited source was the bare SSA homepage. And the SSA Inspector General fraud number we printed, 1-800-269-0271, appears nowhere on oig.ssa.gov's own reporting or scam-awareness pages, so it was replaced with the OIG's online reporting form. The generator scripts that stamp these blocks were corrected in the same pass.

Primary source: <https://www.ssa.gov/pubs/EN-05-10023.pdf>

### 2026-09-10 · CORRECTION

**Correction: we said the Social Security office that handles your case sits in your own country — for 9 of 12 it is in a third country, and Cuba cannot be paid at all**

All 24 Social Security totalization pages (12 EN + 12 ES) told readers that "if you return to live in <country>" there is a dedicated Federal Benefits Unit at the US consulate there. SSA's own roster (ssa.gov/foreign/foreign.htm, read September 10, 2026) says otherwise for nine of the twelve: Cuba and Colombia are served from the US Embassy in Santo Domingo; Ecuador, El Salvador, Guatemala, Honduras and Nicaragua from San Jose, Costa Rica; Peru and Venezuela from Buenos Aires. Only Argentina, Mexico and the Dominican Republic have an FBU inside the country. Each page now names the office SSA actually lists, with its phone and email. The Cuba page also gained the fact it was silent on: SSA Handbook 1849 makes Cuba a US Treasury restricted country, so a non-citizen who lives there loses every withheld payment permanently. Same pass: the quarter-of-coverage figure moved from a two-year-stale $1,730 (2024) to $1,890, SSA's 2026 amount.

Primary source: <https://www.ssa.gov/foreign/foreign.htm>

### 2026-09-10 · CORRECTION

**Correction: the FATCA threshold had only one half of the IRS test — a balance that peaked mid-year still requires Form 8938**

The 24 country tax pages (12 EN + 12 ES) gave the Form 8938 thresholds as "Single: $50,000 at year-end / Married filing jointly: $100,000 at year-end". The IRS states TWO prongs and either one triggers the form: more than $50,000 on the last day of the year OR more than $75,000 at any time during it (single), and $100,000 / $150,000 married filing jointly. A reader whose foreign balance hit $80,000 in July and $40,000 on December 31 would have concluded nothing was due; IRC 6038D carries a $10,000 penalty. The 28 expat country pages carried the mirror-image error — quoting the in-US thresholds to readers living abroad, where the figures are $200,000/$300,000 and $400,000/$600,000. Both are fixed, along with the generator that produced them. Same pass: the US-Chile tax treaty entered into force December 19, 2023 (US Treasury), not 2016; the un-substituted "if <country> has NO tax treaty" block was deleted from the Mexico and Venezuela pages, which say two paragraphs earlier that both have one; El Salvador's territorial system replaced a claim that it taxes your US wages; and Cuba's 2019 Constitution (art. 36) replaced the pre-2019 rule that naturalising costs you Cuban citizenship.

Primary source: <https://www.irs.gov/businesses/corporations/summary-of-fatca-reporting-for-us-taxpayers>

---

## Citing a change

Cite the primary government source for the underlying fact, and this record for
the change history. See [README](README.md#cite-this-dataset) for the citation
formats and DOI.

