# -*- coding: utf-8 -*-
"""All copy for olimann.com, EN and DE. Edit here, then run build.py."""

SITE = {"domain": "https://olimann.com", "name": "Olimann", "year": "2026"}

# key, lang, path
PAGES = [
    ("home", "en", "/"),                      ("home", "de", "/de/"),
    ("method", "en", "/method/"),             ("method", "de", "/de/methode/"),
    ("departments", "en", "/departments/"),   ("departments", "de", "/de/bereiche/"),
    ("who", "en", "/who-its-for/"),           ("who", "de", "/de/fuer-wen/"),
    ("about", "en", "/about/"),               ("about", "de", "/de/ueber-uns/"),
    ("audit", "en", "/constraint-audit/"),    ("audit", "de", "/de/engpass-analyse/"),
    ("thanks", "en", "/constraint-audit/thanks/"), ("thanks", "de", "/de/engpass-analyse/danke/"),
    ("imprint", "en", "/imprint/"),           ("imprint", "de", "/de/impressum/"),
    ("privacy", "en", "/privacy/"),           ("privacy", "de", "/de/datenschutz/"),
]
NOINDEX = {"thanks"}
SITEMAP_EXCLUDE = {"thanks"}

RING = {
    "en": ["Marketing", "Sales", "Quoting", "Onboarding", "Delivery", "Support", "Renewal", "HR", "Finance", "Data & IT"],
    "de": ["Marketing", "Vertrieb", "Angebot", "Onboarding", "Umsetzung", "Kundenservice", "Verlängerung", "Personal", "Finanzen", "Daten & IT"],
}
SIDES = ["dem", "dem", "dem", "cap", "cap", "cap", "cap", "sup", "sup", "sup"]

T = {}

# ----------------------------------------------------------------------------- EN
T["en"] = dict(
    ui=dict(skip="Skip to content", menu="Menu", nav_method="Method", nav_departments="Departments", nav_who="Who it's for",
            nav_about="About", nav_audit="Constraint Audit", lang_toggle="DE", lang_title="Deutsche Version",
            footer_tagline="Business automation, one constraint at a time. For engineering-led companies that would rather grow than hire in step.",
            footer_pages="Pages", footer_legal="Legal", imprint="Legal notice", privacy="Privacy",
            footer_note="No cookies. No tracking. Fonts served from this domain.", copyright="© 2026 Olimann"),
    meta=dict(
        home=("Olimann — Automate the bottleneck. Then the next one.", "End-to-end business automation for engineering-led companies. We find whether demand or capacity is your constraint, automate that side first, and move to the next."),
        method=("The Flywheel — Olimann", "A company has one constraint at a time. How we find it, what we automate, how we measure it, and why the constraint moves."),
        departments=("Departments — Olimann", "Marketing, sales, onboarding, delivery, support, HR, finance, data. What we have built on both sides of the business."),
        who=("Who it's for — Olimann", "Built for companies where expert hours are the bottleneck: engineering and simulation firms, technical consultancies, specialised manufacturers."),
        about=("About — Olimann", "Business developers who have carried a number and engineers who have shipped to production."),
        audit=("Constraint Audit — Olimann", "Find your constraint before you spend a euro automating the wrong side. Six questions, one conversation, a written readout."),
        thanks=("Received — Olimann", "Your audit request has been received."),
        imprint=("Legal notice — Olimann", "Legal notice (Impressum) for olimann.com."),
        privacy=("Privacy — Olimann", "Privacy policy for olimann.com."),
    ),
    home=dict(
        hero=dict(eyebrow="Business automation · from first contact to final invoice",
                  h1="Automate the bottleneck.<br>Then the next one.",
                  lede="Every company is held back by one constraint at a time: too little demand, or too little capacity to serve it. Olimann finds out which one it is, automates that side of the business first, and moves on to the next. That is how a company grows without its headcount growing at the same pace.",
                  cta1="Start with a Constraint Audit", cta2="How the flywheel works"),
        lifecycle=dict(eyebrow="The whole company, in the order a customer experiences it",
                       groups=[dict(cls="demand", label="Demand side", chips=["Marketing", "Sales", "Quoting"]),
                               dict(cls="capacity", label="Capacity side", chips=["Onboarding", "Delivery", "Support", "Renewal"]),
                               dict(cls="under", label="Underneath everything", chips=["HR", "Finance", "Data & IT"])],
                       text="We work across all of it. Not because every department needs automating — most don't, yet — but because the constraint can sit anywhere, and it moves."),
        problem=dict(h2="Most automation starts in the wrong place.",
                     p1="Companies automate what is fashionable or what shouts loudest — a chatbot, a CRM, a reporting tool. They rarely start with the question that decides whether any of it pays off: where is this business actually stuck right now?",
                     p2="Get the order wrong and automation makes things worse.",
                     panels=[dict(h="Demand side first, with a full order book", p="Lead times stretch. Quality slips. Your best people spend their days firefighting. The customers you just won leave."),
                             dict(h="Capacity side first, with an empty pipeline", p="Expensive specialists wait for work. Fixed costs stay fixed. There is no revenue to show for the investment.")],
                     line="The order is not a preference. It is a diagnosis."),
        flywheel=dict(eyebrow="The method", h2="One constraint at a time. That is the whole method.",
                      steps=[dict(h="Diagnose", p="We map where hours and margin are lost across the customer lifecycle and name the constraint: demand, or capacity."),
                             dict(h="Automate that side", p="We build the systems that remove it — workflows, knowledge, decisions. Not a tool your team has to learn. A system that runs."),
                             dict(h="Measure", p="One number tracks it: what it costs you to serve one customer, project or order, from signature to paid invoice. It should fall."),
                             dict(h="The constraint moves", p="Free capacity gets filled with demand. Filled capacity becomes the new constraint. We go again — on the other side.")],
                      close="Each turn of the wheel is a company that can take on more without hiring in step. That is what scaling actually is.",
                      metric="Cost-to-serve", metric_lo="falling", metric_hi="per customer"),
        caps=dict(eyebrow="What we've built", h2="We have built systems on both sides of the business.",
                  p="Not products. Systems, built into the way your company already works — your tools, your permissions, your data."),
        engagement=dict(eyebrow="How an engagement works", h2="Weeks, not quarters.",
                        stages=[dict(h="Constraint Audit", p="A structured look at your company end to end. You get a written readout: where the constraint is, what we would automate first, and what capacity that frees."),
                                dict(h="First system", p="We build the first system on the constrained side and bring it into daily use with your team."),
                                dict(h="Measure and move", p="We track cost-to-serve, confirm the constraint has moved, and start on the next one.")],
                        line="Built into your stack, documented, and handed over — or run by us, if you prefer."),
        who=dict(eyebrow="Who it's for", h2="Built for companies where expert hours are the bottleneck.",
                 p="Engineering and simulation firms. Technical consultancies. Specialised manufacturers. Software companies with a services arm. Typically €5–50M in revenue, with a delivery team of specialists that took years to build and cannot be hired in a hurry.",
                 notfor="We are not the right partner if you want a chatbot, a single off-the-shelf tool, or automation for a company well below €2M in revenue. We will tell you that in the audit, and point you somewhere better.",
                 cta="Who it's for, in detail"),
        about=dict(eyebrow="About", h2="Business developers and engineers.",
                   p="Olimann is a team of business developers who have been responsible for growth inside operating companies, and engineers who build the systems that let those companies grow.",
                   cta="About Olimann"),
        faq=dict(eyebrow="Questions", h2="The questions a CEO actually asks.",
                 items=[dict(q="Do you replace people?", a="No. We remove the work that keeps skilled people from doing skilled work. What you do with the freed capacity is the point of the exercise: more customers, faster delivery, or both."),
                        dict(q="Is this AI?", a="Where it helps. Much of what removes a constraint is plain workflow and data plumbing. We use language models where the work involves reading, writing or answering, and conventional automation everywhere else. We don't sell AI. We sell the removed constraint."),
                        dict(q="We already have an IT team.", a="Good. We work with them, not around them. Our systems run inside your stack and your permission model, and your team gets the documentation to own them."),
                        dict(q="What about data protection?", a="Your data stays under your control. Systems respect existing access rights, run where you require, and come with processor agreements under the GDPR. We work within the EU AI Act's documentation requirements from the first day."),
                        dict(q="How is this different from a consultancy or an agency?", a="A consultancy gives you a report. An agency gives you leads. We give you the diagnosis and then build the system that acts on it — and we come back for the next constraint."),
                        dict(q="What does it cost?", a="The Constraint Audit is free of charge. Systems are scoped from the audit and quoted at a fixed price each. You know the number before we start.")]),
        close=dict(h2="Find out which side of your business is holding the other back.",
                   p="The Constraint Audit takes one conversation and a short questionnaire. You get a written readout of where your constraint is and what we would do about it — whether or not you go on to work with us.",
                   cta="Start the Constraint Audit"),
    ),
    departments=dict(
        eyebrow="Departments", h1="Everywhere a customer touches your company. And everywhere they don't see.",
        p="We don't specialise in a department. We specialise in finding the one that is holding the others back. But when we get there, this is what we have built before.",
        items=[dict(h="Marketing", before="Output depends on whoever has time this week.", p="Content production pipelines, campaign operations, lead qualification and routing."),
               dict(h="Sales", before="Every quote is built from scratch — by someone who should be selling.", p="Proposals and quotes drawn from past work, estimation support, follow-up, handover to delivery."),
               dict(h="Onboarding", before="The same questions, asked again, in a different order, by a different person.", p="Kickoff and data collection, requirements capture, account and project setup."),
               dict(h="Delivery &amp; Operations", before="Status lives in people's heads. The answer to most questions is in a folder from 2019.", p="Project knowledge you can ask questions of, respecting who may see what. Status tracking and reporting, effort estimation, test and QA support."),
               dict(h="Customer Service", before="Simple questions and urgent ones arrive in the same queue.", p="Triage and escalation, self-service answers, an AI receptionist on the phone."),
               dict(h="Data &amp; Decisions", before="Routine questions wait for the one person who can write the query.", p="Ask your data in plain language, automated reporting, data pipeline operations."),
               dict(h="HR", before="Onboarding a new hire takes a dozen people, and nobody owns the checklist.", p="Staff onboarding and offboarding, knowledge transfer, internal answers on policies and procedures."),
               dict(h="Finance &amp; Admin", before="Invoices and reports are assembled by hand at the end of every month.", p="Invoicing workflows, document processing, management reporting.")],
        cta="Start with a Constraint Audit"),
    method=dict(
        eyebrow="The method", h1="A company has one constraint at a time.",
        lede="At any given moment, one thing limits how much a company can sell and deliver. Not five things. One. Improve anything other than that one thing and the improvement is absorbed by the constraint: the extra leads queue, the extra capacity idles.",
        p="This is not our idea. It is the Theory of Constraints, and it has run factories for forty years. We apply it to the whole company — to its ability to win a customer and to serve one — and we use automation as the lever.",
        blocks=[
            dict(h2="Every company has a demand side and a capacity side.",
                 html="<p><strong>The demand side</strong> is everything that turns a stranger into a signed customer: marketing, sales, quoting.</p><p><strong>The capacity side</strong> is everything that turns a signed customer into a delivered, paid and retained one: onboarding, delivery, support, renewal — and the HR, finance and data functions that hold it all up.</p><p>The constraint is always on one side or the other. The whole question is which.</p>"),
            dict(h2="Three questions find the constraint in most companies.",
                 html="<ul><li><b>Where is the queue?</b> Inquiries waiting for a reply, or signed projects waiting to start?</li><li><b>Where do the most expensive hours go?</b> Are your best people quoting, delivering — or answering questions whose answer already exists somewhere in the company?</li><li><b>What happens when you add?</b> After a strong month in sales, does delivery strain? After a quiet week in delivery, does sales fill it?</li></ul><p>The Constraint Audit asks these questions properly, with your numbers, across every department. The answer is usually clear within a fortnight — and usually not what the management team expected.</p>"),
            dict(h2="Automation here means three things. None of them is a chatbot bolted on.",
                 html="<ul><li><b>Workflows</b> — things that should happen without a person pushing them: a project set up the moment a contract is signed, a status report assembled before anyone asks.</li><li><b>Knowledge</b> — answers that exist in your company but not where they are needed: the specification from a past project, the policy nobody can find, the customer's history at the moment they call.</li><li><b>Decisions</b> — routine judgments made consistently: which inquiry is worth a senior's time, which ticket is urgent, what a project of this shape usually costs.</li></ul><p>People stay where judgment is the product. Everything around that judgment is what we remove.</p>"),
            dict(h2="One number tells you whether it is working.",
                 html="<p><strong>Cost-to-serve:</strong> everything it costs to take one customer, project or order from signature to paid invoice, divided by how many you served.</p><p>We use this one number because it is honest about order. Add demand to a jammed capacity side and cost-to-serve rises — overtime, rework, churn. Add capacity to an empty demand side and it rises too — the same fixed costs spread over fewer customers. It only falls when the right side was automated first. That makes it the scoreboard for the whole method, not just for one project.</p>"),
            dict(h2="The constraint moves. That is the flywheel.",
                 html="<p>Remove a capacity constraint and demand becomes the constraint: you can now serve more customers than you are winning. Remove a demand constraint and capacity becomes the constraint: you are winning more than you can serve. Each system we build moves the constraint to the other side, and each turn leaves the company larger than the one before.</p><p>This is the mechanism by which every well-run company grows. Most do it by instinct, late, and by hiring. We do it deliberately, early, and mostly without.</p>"),
            dict(h2="Inside your stack. Inside your permissions.",
                 html="<ul><li>Systems are built into the tools you already run, not beside them.</li><li>Access rights are inherited, not re-invented: a system can only see what the person using it could see.</li><li>Data is processed where you require it, with a processor agreement in place before anything is connected.</li><li>Every system ships with documentation and a handover session. Your team can own it; nothing depends on us staying.</li><li>Fixed price per system, scoped from the audit.</li></ul>"),
        ],
        cta="Start with a Constraint Audit"),
    who=dict(
        eyebrow="Who it's for", h1="Companies where the most expensive hour in the building is the one that limits growth.",
        p="Engineering and simulation firms. Technical consultancies. Specialised manufacturers. Software companies with a services arm. What they share: a delivery team of specialists that took years to build, a sales process those same specialists are pulled into, and a management team that can feel the ceiling but cannot see which wall it is.",
        yes_h="You are probably in the right place if",
        yes=["Your best people spend hours each week on quoting, reporting, or answering questions whose answer is already written down somewhere.",
             "Sales could close more if delivery could start sooner — or delivery could do more if sales brought it in.",
             "You have bought tools that nobody fully uses.",
             "Hiring another specialist takes months, and you would rather not.",
             "You want one partner who can work on either side of the business, because you do not yet know which side is the problem."],
        no_h="You are probably not, if",
        no=["You want a chatbot, or one specific tool implemented.",
            "Revenue is well below €2M — the systems we build need a certain volume to pay back.",
            "You need a report, not a change."],
        line="We say so in the audit, and we point you somewhere better.", cta="Start with a Constraint Audit"),
    about=dict(
        eyebrow="About Olimann", h1="Business developers who have carried a number. Engineers who have shipped to production.",
        paras=["Olimann started with an observation that repeated itself in company after company: automation gets bought where it is easiest to sell, not where the business is actually stuck. A chatbot for a company whose real problem is quoting. A CRM for a company whose real problem is delivery. We set out to do it in the right order.",
               "The team combines people who have owned revenue and operations targets inside companies with engineers who build production systems — data, workflows and language models — for enterprise clients. We work from Germany with an engineering team in India."],
        how_h="How we work",
        how=["Small, senior teams. The people in the audit are the people who build.",
             "Fixed price per system. No day rates, no open-ended retainers.",
             "Documentation and handover are part of the deliverable, not an extra.",
             "We say no in the audit when we are not the right fit."],
        cta="Start with a Constraint Audit"),
    audit=dict(
        eyebrow="Constraint Audit", h1="Find your constraint before you spend a euro automating the wrong side.",
        lede="Answer five questions. We get back to you as soon as possible with proposed times for a conversation with the member of the team who would run your audit. After it, you receive a written readout: where your constraint is, what we would automate first, what capacity that frees, and a fixed price for the first system — if we think there should be one.",
        get_h="What you get",
        get=["A clear answer to \"demand or capacity?\" — with the reasoning.", "The first system we would build, and why that one.", "A fixed price. Or an honest \"not yet\"."],
        free="The audit is free of charge and commits you to nothing.",
        f=dict(error1="Please fill in your name, company and a valid email address.", error2="The request could not be sent from the server. Please email us directly at <a href=\"mailto:info@olimann.com\">info@olimann.com</a>.",
               q1="You", name="Name", company="Company", role="Role", email="Email", website="Website (optional)",
               q2="Where does work pile up right now?", q2hint="Pick everything that applies.",
               pile=["Inquiries wait for a reply", "Quotes and proposals take too long", "Signed projects wait to start", "Projects run late", "The support queue keeps growing", "Reporting takes too long", "Hiring cannot keep up"],
               pile_other="Somewhere else",
               q3="Roughly how large is the company?", revenue="Revenue", rev_opts=["under €2M", "€2–5M", "€5–20M", "€20–50M", "over €50M"], rev_pick="Select",
               hc="Headcount, roughly (optional)", hc_labels=["Sales & marketing", "Delivery & operations", "Support", "Admin"],
               q4="If you had double the customers tomorrow, would your revenue double, or would something break?",
               q5="Which tools run sales, delivery and support today?",
               consent="I have read the <a href=\"/privacy/\">privacy policy</a>. My answers are used only to prepare the audit.",
               submit="Request the audit")),
    thanks=dict(eyebrow="Received", h1="Thank you. We will get back to you as soon as possible.",
                p="You will receive proposed times for the conversation from a person, not an autoresponder. If it is urgent, write to <a href=\"mailto:info@olimann.com\">info@olimann.com</a>.",
                cta="Back to the start"),
    imprint=dict(title="Legal notice", intro="Information pursuant to § 5 DDG (German Digital Services Act). The German version at <a href=\"/de/impressum/\">/de/impressum/</a> is authoritative.",
                 html="""<h2>Provider</h2>
<address><mark class="todo">[Company legal name and form]</mark><br><mark class="todo">[Street and number]</mark><br><mark class="todo">[Postcode, City]</mark>, Germany</address>
<h3>Represented by</h3><p><mark class="todo">[Managing director(s)]</mark></p>
<h3>Contact</h3><p>Email: <a href="mailto:info@olimann.com">info@olimann.com</a><br>Phone: <mark class="todo">[+49 …]</mark></p>
<h3>Register entry</h3><p><mark class="todo">[Register court, HRB number]</mark></p>
<h3>VAT ID</h3><p>VAT identification number pursuant to § 27a UStG: <mark class="todo">[DE …]</mark></p>
<h3>Responsible for content pursuant to § 18 (2) MStV</h3><p><mark class="todo">[Name, address]</mark></p>
<h2>Dispute resolution</h2><p>We are neither willing nor obliged to participate in dispute resolution proceedings before a consumer arbitration board.</p>
<h2>Liability for content</h2><p>As a service provider we are responsible for our own content on these pages under general law. We are not obliged to monitor transmitted or stored third-party information or to investigate circumstances indicating unlawful activity. Obligations to remove or block the use of information under general law remain unaffected.</p>
<h2>Liability for links</h2><p>Our pages may contain links to external websites over whose content we have no influence. The respective provider is responsible for the content of linked pages. Linked pages were checked for possible legal violations at the time of linking; permanent monitoring is not reasonable without concrete indications of a violation. Upon becoming aware of violations we will remove such links immediately.</p>
<h2>Copyright</h2><p>Content and works on these pages created by the provider are subject to German copyright law. Reproduction, editing, distribution and any kind of use beyond the limits of copyright require the written consent of the respective author.</p>"""),
    privacy=dict(title="Privacy policy", intro="Last updated: September 2026. The German version at <a href=\"/de/datenschutz/\">/de/datenschutz/</a> is authoritative.",
                 html="""<h2>1. Controller</h2>
<address><mark class="todo">[Company legal name]</mark><br><mark class="todo">[Street and number]</mark><br><mark class="todo">[Postcode, City]</mark>, Germany<br>Email: <a href="mailto:info@olimann.com">info@olimann.com</a></address>
<h2>2. What this site does not do</h2><p>This website sets no cookies and uses no analytics or tracking services. Fonts and all other assets are served from our own domain; no third-party requests are made when you view a page.</p>
<h2>3. Hosting and server logs</h2><p>This site is hosted by Hostinger International Ltd., 61 Lordou Vironos Street, 6023 Larnaca, Cyprus, in a data centre in the European Union (<mark class="todo">[location, e.g. Netherlands]</mark>). When you access the site, the web server automatically processes the IP address of the requesting device, date and time, the requested URL, the referring URL, browser type and version, and the operating system. This is necessary to deliver the site and to ensure its security and stability. Legal basis: Art. 6 (1) (f) GDPR. Server logs are deleted after <mark class="todo">[14]</mark> days at the latest. A data processing agreement pursuant to Art. 28 GDPR is in place with the hosting provider.</p>
<h2>4. Constraint Audit form</h2><p>If you request an audit via the form, we process the information you enter: name, company, role, email address, website (optional), your answers to the questions about your company, and the time of submission. The data is stored on our web server (see section 3) and may additionally be forwarded to our mailbox; it is used exclusively to prepare and conduct the audit and to contact you about it. Legal basis: Art. 6 (1) (b) GDPR (pre-contractual measures) and Art. 6 (1) (f) GDPR (our legitimate interest in responding to inquiries). We retain the data for as long as necessary to handle your request; if no business relationship follows, it is deleted after <mark class="todo">[12]</mark> months. Statutory retention obligations remain unaffected. The form contains a hidden field that is used solely to detect automated submissions; no data is stored for this purpose.</p>
<h2>5. Email contact</h2><p>If you contact us by email, we process your email address and the content of your message to handle your request. Legal basis: Art. 6 (1) (b) or (f) GDPR.</p>
<h2>6. Recipients</h2><p>We do not sell or share your data. Recipients are only our hosting provider (see section 3) and our email provider, each bound by a data processing agreement. No data is transferred to countries outside the EU/EEA unless you have been informed otherwise.</p>
<h2>7. Your rights</h2><p>You have the right to access (Art. 15 GDPR), rectification (Art. 16), erasure (Art. 17), restriction of processing (Art. 18), data portability (Art. 20) and to object to processing based on Art. 6 (1) (f) GDPR (Art. 21). You also have the right to lodge a complaint with a supervisory authority (Art. 77 GDPR), for example the data protection authority of the German federal state in which we are based. To exercise your rights, write to <a href="mailto:info@olimann.com">info@olimann.com</a>.</p>
<h2>8. Changes</h2><p>We will update this policy when the site or the law changes. The current version is always available on this page.</p>"""),
    notfound=dict(eyebrow="404", h1="This page isn't here.", p="The rest of the site is.", cta="Back to the start"),
)

# ----------------------------------------------------------------------------- DE
T["de"] = dict(
    ui=dict(skip="Zum Inhalt springen", menu="Menü", nav_method="Methode", nav_departments="Bereiche", nav_who="Für wen",
            nav_about="Über uns", nav_audit="Engpass-Analyse", lang_toggle="EN", lang_title="English version",
            footer_tagline="Unternehmensautomatisierung, ein Engpass nach dem anderen. Für technisch geprägte Unternehmen, die lieber wachsen, als im Gleichschritt einzustellen.",
            footer_pages="Seiten", footer_legal="Rechtliches", imprint="Impressum", privacy="Datenschutz",
            footer_note="Keine Cookies. Kein Tracking. Schriften von dieser Domain.", copyright="© 2026 Olimann"),
    meta=dict(
        home=("Olimann – Erst der Engpass. Dann der nächste.", "Unternehmensautomatisierung für technisch geprägte Unternehmen. Wir finden heraus, ob Nachfrage oder Kapazität Ihr Engpass ist, automatisieren zuerst diese Seite – und dann die nächste."),
        method=("Das Schwungrad – Olimann", "Ein Unternehmen hat zu jedem Zeitpunkt genau einen Engpass. Wie wir ihn finden, was wir automatisieren, wie wir messen und warum der Engpass wandert."),
        departments=("Bereiche – Olimann", "Marketing, Vertrieb, Onboarding, Umsetzung, Kundenservice, Personal, Finanzen, Daten. Was wir auf beiden Seiten des Unternehmens gebaut haben."),
        who=("Für wen – Olimann", "Für Unternehmen, in denen Expertenstunden der Engpass sind: Ingenieur- und Simulationsdienstleister, technische Beratungen, spezialisierte Fertiger."),
        about=("Über uns – Olimann", "Business Developer, die eine Zahl verantwortet haben, und Ingenieure, die in Produktion geliefert haben."),
        audit=("Engpass-Analyse – Olimann", "Finden Sie Ihren Engpass, bevor Sie einen Euro in die Automatisierung der falschen Seite stecken. Sechs Fragen, ein Gespräch, eine schriftliche Auswertung."),
        thanks=("Angekommen – Olimann", "Ihre Anfrage zur Engpass-Analyse ist eingegangen."),
        imprint=("Impressum – Olimann", "Impressum von olimann.com."),
        privacy=("Datenschutz – Olimann", "Datenschutzerklärung von olimann.com."),
    ),
    home=dict(
        hero=dict(eyebrow="Unternehmensautomatisierung · vom ersten Kontakt bis zur letzten Rechnung",
                  h1="Erst der Engpass.<br>Dann der nächste.",
                  lede="Jedes Unternehmen wird zu jedem Zeitpunkt von genau einem Engpass gebremst: zu wenig Nachfrage – oder zu wenig Kapazität, um sie zu bedienen. Olimann findet heraus, welcher es ist, automatisiert zuerst diese Seite des Unternehmens und geht dann zum nächsten Engpass über. So wächst ein Unternehmen, ohne dass die Belegschaft im gleichen Tempo mitwachsen muss.",
                  cta1="Engpass-Analyse starten", cta2="So funktioniert das Schwungrad"),
        lifecycle=dict(eyebrow="Das ganze Unternehmen – in der Reihenfolge, in der ein Kunde es erlebt",
                       groups=[dict(cls="demand", label="Nachfrageseite", chips=["Marketing", "Vertrieb", "Angebot"]),
                               dict(cls="capacity", label="Kapazitätsseite", chips=["Onboarding", "Umsetzung", "Kundenservice", "Verlängerung"]),
                               dict(cls="under", label="Darunter", chips=["Personal", "Finanzen", "Daten & IT"])],
                       text="Wir arbeiten über alle Bereiche hinweg. Nicht, weil jede Abteilung automatisiert werden müsste – die meisten müssen es noch nicht –, sondern weil der Engpass überall sitzen kann. Und er wandert."),
        problem=dict(h2="Die meisten Automatisierungen beginnen an der falschen Stelle.",
                     p1="Unternehmen automatisieren, was gerade in Mode ist oder am lautesten ruft – einen Chatbot, ein CRM, ein Reporting-Tool. Selten beginnen sie mit der Frage, von der abhängt, ob sich davon irgendetwas rechnet: Wo steckt dieses Unternehmen gerade wirklich fest?",
                     p2="Stimmt die Reihenfolge nicht, macht Automatisierung die Lage schlimmer.",
                     panels=[dict(h="Zuerst die Nachfrageseite – bei vollem Auftragsbuch", p="Durchlaufzeiten werden länger. Die Qualität leidet. Ihre besten Leute löschen den ganzen Tag Brände. Die gerade gewonnenen Kunden gehen wieder."),
                             dict(h="Zuerst die Kapazitätsseite – bei leerer Pipeline", p="Teure Fachkräfte warten auf Arbeit. Fixkosten bleiben fix. Es gibt keinen Umsatz, der die Investition rechtfertigt.")],
                     line="Die Reihenfolge ist keine Geschmacksfrage. Sie ist eine Diagnose."),
        flywheel=dict(eyebrow="Die Methode", h2="Ein Engpass nach dem anderen. Das ist die ganze Methode.",
                      steps=[dict(h="Diagnose", p="Wir erfassen, wo entlang des Kundenlebenszyklus Stunden und Marge verloren gehen, und benennen den Engpass: Nachfrage oder Kapazität."),
                             dict(h="Diese Seite automatisieren", p="Wir bauen die Systeme, die ihn beseitigen – Abläufe, Wissen, Entscheidungen. Kein Tool, das Ihr Team erst lernen muss. Ein System, das läuft."),
                             dict(h="Messen", p="Eine Kennzahl zeigt es: was es Sie kostet, einen Kunden, ein Projekt oder einen Auftrag zu bedienen – vom Vertragsabschluss bis zur bezahlten Rechnung. Sie muss sinken."),
                             dict(h="Der Engpass wandert", p="Freie Kapazität wird mit Nachfrage gefüllt. Gefüllte Kapazität wird zum neuen Engpass. Wir fangen wieder an – auf der anderen Seite.")],
                      close="Jede Umdrehung des Rads ist ein Unternehmen, das mehr annehmen kann, ohne im Gleichschritt einzustellen. Genau das ist Skalierung.",
                      metric="Kosten pro bedientem Kunden", metric_lo="sinkend", metric_hi="je Kunde"),
        caps=dict(eyebrow="Was wir gebaut haben", h2="Wir haben Systeme auf beiden Seiten des Unternehmens gebaut.",
                  p="Keine Produkte. Systeme, eingebaut in die Art, wie Ihr Unternehmen bereits arbeitet – Ihre Tools, Ihre Berechtigungen, Ihre Daten."),
        engagement=dict(eyebrow="So läuft eine Zusammenarbeit", h2="Wochen, nicht Quartale.",
                        stages=[dict(h="Engpass-Analyse", p="Ein strukturierter Blick auf Ihr Unternehmen von vorne bis hinten. Sie erhalten eine schriftliche Auswertung: wo der Engpass sitzt, was wir zuerst automatisieren würden und welche Kapazität das freisetzt."),
                                dict(h="Erstes System", p="Wir bauen das erste System auf der Engpass-Seite und bringen es mit Ihrem Team in den täglichen Einsatz."),
                                dict(h="Messen und weiter", p="Wir verfolgen die Kosten pro bedientem Kunden, prüfen, ob der Engpass gewandert ist, und beginnen mit dem nächsten.")],
                        line="In Ihre Systemlandschaft gebaut, dokumentiert und übergeben – oder von uns betrieben, wenn Sie das bevorzugen."),
        who=dict(eyebrow="Für wen", h2="Für Unternehmen, in denen Expertenstunden der Engpass sind.",
                 p="Ingenieur- und Simulationsdienstleister. Technische Beratungen. Spezialisierte Fertiger. Softwareunternehmen mit Dienstleistungsgeschäft. Typischerweise 5 bis 50 Mio. € Umsatz – mit einem Team aus Spezialisten, das über Jahre aufgebaut wurde und sich nicht auf die Schnelle nachbesetzen lässt.",
                 notfor="Wir sind nicht der richtige Partner, wenn Sie einen Chatbot, ein einzelnes Standardtool oder eine Automatisierung für ein Unternehmen deutlich unter 2 Mio. € Umsatz suchen. Das sagen wir Ihnen in der Analyse offen – und nennen Ihnen eine bessere Adresse.",
                 cta="Für wen, im Detail"),
        about=dict(eyebrow="Über uns", h2="Business Developer und Ingenieure.",
                   p="Olimann ist ein Team aus Business Developern, die in Unternehmen selbst für Wachstum verantwortlich waren, und Ingenieuren, die die Systeme dafür bauen.",
                   cta="Über Olimann"),
        faq=dict(eyebrow="Fragen", h2="Die Fragen, die ein Geschäftsführer wirklich stellt.",
                 items=[dict(q="Ersetzen Sie Mitarbeiter?", a="Nein. Wir entfernen die Arbeit, die qualifizierte Menschen davon abhält, qualifizierte Arbeit zu machen. Was Sie mit der freien Kapazität tun, ist der Sinn der Übung: mehr Kunden, schnellere Umsetzung oder beides."),
                        dict(q="Ist das KI?", a="Wo sie hilft. Vieles, was einen Engpass beseitigt, ist schlichte Prozess- und Datenarbeit. Sprachmodelle setzen wir ein, wo gelesen, geschrieben oder geantwortet wird – und klassische Automatisierung überall sonst. Wir verkaufen keine KI. Wir verkaufen den beseitigten Engpass."),
                        dict(q="Wir haben bereits eine IT-Abteilung.", a="Gut. Wir arbeiten mit ihr, nicht an ihr vorbei. Unsere Systeme laufen in Ihrer Systemlandschaft und Ihrem Berechtigungsmodell, und Ihr Team bekommt die Dokumentation, um sie zu übernehmen."),
                        dict(q="Wie steht es um den Datenschutz?", a="Ihre Daten bleiben unter Ihrer Kontrolle. Die Systeme respektieren bestehende Zugriffsrechte, laufen dort, wo Sie es vorgeben, und kommen mit Auftragsverarbeitungsverträgen nach DSGVO. Die Dokumentationspflichten des EU AI Act berücksichtigen wir vom ersten Tag an."),
                        dict(q="Was unterscheidet Sie von einer Beratung oder einer Agentur?", a="Eine Beratung liefert Ihnen einen Bericht. Eine Agentur liefert Ihnen Anfragen. Wir liefern die Diagnose und bauen dann das System, das daraus folgt – und kommen für den nächsten Engpass wieder."),
                        dict(q="Was kostet das?", a="Die Engpass-Analyse ist kostenlos. Systeme werden auf Basis der Analyse einzeln zum Festpreis angeboten. Sie kennen die Zahl, bevor wir anfangen.")]),
        close=dict(h2="Finden Sie heraus, welche Seite Ihres Unternehmens die andere bremst.",
                   p="Die Engpass-Analyse braucht ein Gespräch und einen kurzen Fragebogen. Sie erhalten eine schriftliche Auswertung, wo Ihr Engpass sitzt und was wir dagegen tun würden – ob Sie anschließend mit uns arbeiten oder nicht.",
                   cta="Engpass-Analyse starten"),
    ),
    departments=dict(
        eyebrow="Bereiche", h1="Überall, wo ein Kunde Ihr Unternehmen berührt. Und überall, wo er es nicht sieht.",
        p="Wir sind nicht auf eine Abteilung spezialisiert. Wir sind darauf spezialisiert, die zu finden, die die anderen bremst. Aber wenn wir dort ankommen, haben wir das hier schon einmal gebaut.",
        items=[dict(h="Marketing", before="Der Output hängt davon ab, wer diese Woche gerade Zeit hat.", p="Content-Produktionsstrecken, Kampagnenbetrieb, Qualifizierung und Verteilung von Anfragen."),
               dict(h="Vertrieb", before="Jedes Angebot entsteht von Grund auf neu – bei jemandem, der eigentlich verkaufen sollte.", p="Angebote und Kalkulationen auf Basis vergangener Projekte, Aufwandsschätzung, Nachfassen, Übergabe an die Umsetzung."),
               dict(h="Onboarding", before="Dieselben Fragen, noch einmal gestellt, in anderer Reihenfolge, von einer anderen Person.", p="Kick-off und Datenerfassung, Anforderungsaufnahme, Einrichtung von Konten und Projekten."),
               dict(h="Umsetzung &amp; Betrieb", before="Der Status steckt in Köpfen. Die Antwort auf die meisten Fragen liegt in einem Ordner von 2019.", p="Projektwissen, das man befragen kann, unter Beachtung, wer was sehen darf. Statusverfolgung und Reporting, Aufwandsschätzung, Test- und QS-Unterstützung."),
               dict(h="Kundenservice", before="Einfache und dringende Anliegen landen in derselben Warteschlange.", p="Triage und Eskalation, Self-Service-Antworten, ein KI-Empfang am Telefon."),
               dict(h="Daten &amp; Entscheidungen", before="Routinefragen warten auf die eine Person, die die Abfrage schreiben kann.", p="Daten in normaler Sprache befragen, automatisiertes Reporting, Betrieb von Datenpipelines."),
               dict(h="Personal", before="Ein Onboarding braucht ein Dutzend Beteiligte – und niemandem gehört die Checkliste.", p="On- und Offboarding von Mitarbeitenden, Wissenstransfer, interne Auskunft zu Richtlinien und Abläufen."),
               dict(h="Finanzen &amp; Verwaltung", before="Rechnungen und Berichte werden am Monatsende von Hand zusammengebaut.", p="Rechnungsabläufe, Dokumentenverarbeitung, Management-Reporting.")],
        cta="Engpass-Analyse starten"),
    method=dict(
        eyebrow="Die Methode", h1="Ein Unternehmen hat zu jedem Zeitpunkt genau einen Engpass.",
        lede="In jedem Moment begrenzt eine Sache, wie viel ein Unternehmen verkaufen und leisten kann. Nicht fünf Dinge. Eine. Verbessern Sie irgendetwas anderes als diese eine Sache, verpufft die Verbesserung am Engpass: Die zusätzlichen Anfragen stauen sich, die zusätzliche Kapazität steht still.",
        p="Das ist nicht unsere Erfindung. Es ist die Theory of Constraints, und sie steuert seit vierzig Jahren Fabriken. Wir wenden sie auf das ganze Unternehmen an – auf seine Fähigkeit, einen Kunden zu gewinnen und ihn zu bedienen – und nutzen Automatisierung als Hebel.",
        blocks=[
            dict(h2="Jedes Unternehmen hat eine Nachfrageseite und eine Kapazitätsseite.",
                 html="<p><strong>Die Nachfrageseite</strong> ist alles, was aus einem Fremden einen Kunden mit Unterschrift macht: Marketing, Vertrieb, Angebotserstellung.</p><p><strong>Die Kapazitätsseite</strong> ist alles, was aus einem Kunden mit Unterschrift einen belieferten, zahlenden und bleibenden Kunden macht: Onboarding, Umsetzung, Kundenservice, Verlängerung – und die Bereiche Personal, Finanzen und Daten, die das alles tragen.</p><p>Der Engpass sitzt immer auf einer der beiden Seiten. Die ganze Frage ist: auf welcher.</p>"),
            dict(h2="Drei Fragen finden den Engpass in den meisten Unternehmen.",
                 html="<ul><li><b>Wo ist die Warteschlange?</b> Anfragen, die auf Antwort warten – oder unterschriebene Projekte, die auf den Start warten?</li><li><b>Wohin gehen die teuersten Stunden?</b> Kalkulieren Ihre besten Leute, setzen sie um – oder beantworten sie Fragen, deren Antwort im Unternehmen längst irgendwo steht?</li><li><b>Was passiert, wenn Sie draufsatteln?</b> Nach einem starken Vertriebsmonat: Ächzt die Umsetzung? Nach einer ruhigen Woche in der Umsetzung: Füllt der Vertrieb sie?</li></ul><p>Die Engpass-Analyse stellt diese Fragen sauber, mit Ihren Zahlen, über alle Bereiche hinweg. Die Antwort ist meist innerhalb von zwei Wochen klar – und meist nicht die, die die Geschäftsführung erwartet hat.</p>"),
            dict(h2="Automatisierung heißt hier dreierlei. Nichts davon ist ein angeschraubter Chatbot.",
                 html="<ul><li><b>Abläufe</b> – Dinge, die passieren sollten, ohne dass jemand sie anstößt: ein Projekt, das in dem Moment angelegt wird, in dem der Vertrag unterschrieben ist; ein Statusbericht, der fertig ist, bevor jemand fragt.</li><li><b>Wissen</b> – Antworten, die es im Unternehmen gibt, aber nicht dort, wo sie gebraucht werden: die Spezifikation aus einem früheren Projekt, die Richtlinie, die niemand findet, die Kundenhistorie in dem Moment, in dem er anruft.</li><li><b>Entscheidungen</b> – Routineurteile, die konsequent gefällt werden: welche Anfrage die Zeit eines erfahrenen Kollegen wert ist, welches Ticket dringend ist, was ein Projekt dieser Art üblicherweise kostet.</li></ul><p>Menschen bleiben dort, wo Urteilsvermögen das Produkt ist. Alles um dieses Urteil herum ist das, was wir entfernen.</p>"),
            dict(h2="Eine Kennzahl zeigt, ob es funktioniert.",
                 html="<p><strong>Kosten pro bedientem Kunden:</strong> alles, was es kostet, einen Kunden, ein Projekt oder einen Auftrag vom Vertragsabschluss bis zur bezahlten Rechnung zu bringen – geteilt durch die Anzahl, die Sie bedient haben.</p><p>Wir nutzen genau diese Kennzahl, weil sie ehrlich zur Reihenfolge ist. Geben Sie Nachfrage auf eine verstopfte Kapazitätsseite, steigt sie – Überstunden, Nacharbeit, Abwanderung. Geben Sie Kapazität auf eine leere Nachfrageseite, steigt sie ebenfalls – dieselben Fixkosten, verteilt auf weniger Kunden. Sie sinkt nur, wenn zuerst die richtige Seite automatisiert wurde. Das macht sie zur Anzeigetafel für die ganze Methode, nicht nur für ein einzelnes Projekt.</p>"),
            dict(h2="Der Engpass wandert. Das ist das Schwungrad.",
                 html="<p>Beseitigen Sie einen Kapazitätsengpass, wird die Nachfrage zum Engpass: Sie können jetzt mehr Kunden bedienen, als Sie gewinnen. Beseitigen Sie einen Nachfrageengpass, wird die Kapazität zum Engpass: Sie gewinnen mehr, als Sie bedienen können. Jedes System, das wir bauen, verschiebt den Engpass auf die andere Seite – und jede Umdrehung hinterlässt ein größeres Unternehmen als zuvor.</p><p>Das ist der Mechanismus, nach dem jedes gut geführte Unternehmen wächst. Die meisten tun es aus dem Bauch heraus, zu spät und durch Einstellungen. Wir tun es bewusst, früh und größtenteils ohne.</p>"),
            dict(h2="In Ihrer Systemlandschaft. In Ihren Berechtigungen.",
                 html="<ul><li>Systeme werden in die Tools eingebaut, die Sie bereits betreiben – nicht daneben.</li><li>Zugriffsrechte werden übernommen, nicht neu erfunden: Ein System sieht nur, was die Person, die es nutzt, auch sehen dürfte.</li><li>Daten werden dort verarbeitet, wo Sie es vorgeben – mit Auftragsverarbeitungsvertrag, bevor irgendetwas angebunden wird.</li><li>Jedes System kommt mit Dokumentation und Übergabetermin. Ihr Team kann es übernehmen; nichts hängt davon ab, dass wir bleiben.</li><li>Festpreis pro System, auf Basis der Analyse.</li></ul>"),
        ],
        cta="Engpass-Analyse starten"),
    who=dict(
        eyebrow="Für wen", h1="Unternehmen, in denen die teuerste Stunde im Haus die ist, die das Wachstum begrenzt.",
        p="Ingenieur- und Simulationsdienstleister. Technische Beratungen. Spezialisierte Fertiger. Softwareunternehmen mit Dienstleistungsgeschäft. Was sie gemeinsam haben: ein über Jahre aufgebautes Team aus Spezialisten, einen Vertriebsprozess, in den genau diese Spezialisten hineingezogen werden, und eine Geschäftsführung, die die Decke spürt, aber nicht sieht, welche Wand es ist.",
        yes_h="Sie sind vermutlich richtig hier, wenn",
        yes=["Ihre besten Leute jede Woche Stunden mit Kalkulationen, Reporting oder Fragen verbringen, deren Antwort irgendwo bereits steht.",
             "der Vertrieb mehr abschließen könnte, wenn die Umsetzung früher starten könnte – oder die Umsetzung mehr leisten könnte, wenn der Vertrieb es hereinholte.",
             "Sie Tools gekauft haben, die niemand vollständig nutzt.",
             "eine weitere Fachkraft einzustellen Monate dauert – und Sie es lieber vermeiden würden.",
             "Sie einen Partner wollen, der auf beiden Seiten des Unternehmens arbeiten kann, weil Sie noch nicht wissen, welche Seite das Problem ist."],
        no_h="Vermutlich nicht, wenn",
        no=["Sie einen Chatbot oder die Einführung eines bestimmten Tools suchen.",
            "der Umsatz deutlich unter 2 Mio. € liegt – die Systeme, die wir bauen, brauchen ein gewisses Volumen, um sich zu rechnen.",
            "Sie einen Bericht brauchen, keine Veränderung."],
        line="Das sagen wir Ihnen in der Analyse – und nennen Ihnen eine bessere Adresse.", cta="Engpass-Analyse starten"),
    about=dict(
        eyebrow="Über Olimann", h1="Business Developer, die eine Zahl verantwortet haben. Ingenieure, die in Produktion geliefert haben.",
        paras=["Olimann begann mit einer Beobachtung, die sich in Unternehmen um Unternehmen wiederholte: Automatisierung wird dort gekauft, wo sie am leichtesten zu verkaufen ist – nicht dort, wo das Unternehmen tatsächlich feststeckt. Ein Chatbot für ein Unternehmen, dessen eigentliches Problem die Angebotserstellung ist. Ein CRM für ein Unternehmen, dessen eigentliches Problem die Umsetzung ist. Wir haben uns vorgenommen, es in der richtigen Reihenfolge zu tun.",
               "Das Team verbindet Menschen, die in Unternehmen Umsatz- und Betriebsziele verantwortet haben, mit Ingenieuren, die Produktivsysteme – Daten, Abläufe und Sprachmodelle – für Unternehmenskunden bauen. Wir arbeiten von Deutschland aus, mit einem Entwicklungsteam in Indien."],
        how_h="Wie wir arbeiten",
        how=["Kleine, erfahrene Teams. Die Menschen in der Analyse sind die Menschen, die bauen.",
             "Festpreis pro System. Keine Tagessätze, keine offenen Retainer.",
             "Dokumentation und Übergabe gehören zur Lieferung – sie sind kein Extra.",
             "Wir sagen in der Analyse Nein, wenn wir nicht die Richtigen sind."],
        cta="Engpass-Analyse starten"),
    audit=dict(
        eyebrow="Engpass-Analyse", h1="Finden Sie Ihren Engpass, bevor Sie einen Euro in die Automatisierung der falschen Seite stecken.",
        lede="Beantworten Sie fünf Fragen. Wir melden uns so schnell wie möglich mit Terminvorschlägen für ein Gespräch mit dem Teammitglied, das Ihre Analyse durchführen würde. Danach erhalten Sie eine schriftliche Auswertung: wo Ihr Engpass sitzt, was wir zuerst automatisieren würden, welche Kapazität das freisetzt – und einen Festpreis für das erste System, sofern wir meinen, dass es eines geben sollte.",
        get_h="Was Sie bekommen",
        get=["Eine klare Antwort auf „Nachfrage oder Kapazität?“ – mit Begründung.", "Das erste System, das wir bauen würden – und warum genau dieses.", "Einen Festpreis. Oder ein ehrliches „Noch nicht“."],
        free="Die Analyse ist kostenlos und unverbindlich.",
        f=dict(error1="Bitte geben Sie Name, Unternehmen und eine gültige E-Mail-Adresse an.", error2="Die Anfrage konnte vom Server nicht versendet werden. Bitte schreiben Sie uns direkt an <a href=\"mailto:info@olimann.com\">info@olimann.com</a>.",
               q1="Sie", name="Name", company="Unternehmen", role="Rolle", email="E-Mail", website="Website (optional)",
               q2="Wo staut sich gerade die Arbeit?", q2hint="Wählen Sie alles aus, was zutrifft.",
               pile=["Anfragen warten auf Antwort", "Angebote und Kalkulationen dauern zu lange", "Unterschriebene Projekte warten auf den Start", "Projekte laufen aus dem Zeitplan", "Die Support-Warteschlange wächst", "Reporting dauert zu lange", "Einstellungen kommen nicht hinterher"],
               pile_other="Woanders",
               q3="Wie groß ist das Unternehmen ungefähr?", revenue="Umsatz", rev_opts=["unter 2 Mio. €", "2–5 Mio. €", "5–20 Mio. €", "20–50 Mio. €", "über 50 Mio. €"], rev_pick="Bitte wählen",
               hc="Mitarbeitende, grob (optional)", hc_labels=["Vertrieb & Marketing", "Umsetzung & Betrieb", "Support", "Verwaltung"],
               q4="Wenn Sie morgen doppelt so viele Kunden hätten: Verdoppelt sich Ihr Umsatz – oder bricht etwas?",
               q5="Welche Tools laufen heute in Vertrieb, Umsetzung und Support?",
               consent="Ich habe die <a href=\"/de/datenschutz/\">Datenschutzerklärung</a> gelesen. Meine Angaben werden ausschließlich zur Vorbereitung der Analyse verwendet.",
               submit="Analyse anfragen")),
    thanks=dict(eyebrow="Angekommen", h1="Vielen Dank. Wir melden uns so schnell wie möglich bei Ihnen.",
                p="Sie erhalten Terminvorschläge für das Gespräch – von einem Menschen, nicht von einem Autoresponder. Wenn es eilt, schreiben Sie an <a href=\"mailto:info@olimann.com\">info@olimann.com</a>.",
                cta="Zur Startseite"),
    imprint=dict(title="Impressum", intro="Angaben gemäß § 5 DDG.",
                 html="""<h2>Anbieter</h2>
<address><mark class="todo">[Firma und Rechtsform]</mark><br><mark class="todo">[Straße und Hausnummer]</mark><br><mark class="todo">[PLZ Ort]</mark></address>
<h3>Vertreten durch</h3><p><mark class="todo">[Geschäftsführer/in]</mark></p>
<h3>Kontakt</h3><p>E-Mail: <a href="mailto:info@olimann.com">info@olimann.com</a><br>Telefon: <mark class="todo">[+49 …]</mark></p>
<h3>Registereintrag</h3><p><mark class="todo">[Registergericht, HRB-Nummer]</mark></p>
<h3>Umsatzsteuer-ID</h3><p>Umsatzsteuer-Identifikationsnummer gemäß § 27a UStG: <mark class="todo">[DE …]</mark></p>
<h3>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h3><p><mark class="todo">[Name, Anschrift]</mark></p>
<h2>Verbraucherstreitbeilegung</h2><p>Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
<h2>Haftung für Inhalte</h2><p>Als Diensteanbieter sind wir für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Wir sind jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen. Verpflichtungen zur Entfernung oder Sperrung der Nutzung von Informationen nach den allgemeinen Gesetzen bleiben hiervon unberührt.</p>
<h2>Haftung für Links</h2><p>Unser Angebot kann Links zu externen Websites Dritter enthalten, auf deren Inhalte wir keinen Einfluss haben. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter verantwortlich. Die verlinkten Seiten wurden zum Zeitpunkt der Verlinkung auf mögliche Rechtsverstöße überprüft; eine permanente inhaltliche Kontrolle ist ohne konkrete Anhaltspunkte einer Rechtsverletzung nicht zumutbar. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige Links umgehend entfernen.</p>
<h2>Urheberrecht</h2><p>Die durch den Anbieter erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht. Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der Grenzen des Urheberrechts bedürfen der schriftlichen Zustimmung des jeweiligen Autors bzw. Erstellers.</p>"""),
    privacy=dict(title="Datenschutzerklärung", intro="Stand: September 2026.",
                 html="""<h2>1. Verantwortlicher</h2>
<address><mark class="todo">[Firma]</mark><br><mark class="todo">[Straße und Hausnummer]</mark><br><mark class="todo">[PLZ Ort]</mark><br>E-Mail: <a href="mailto:info@olimann.com">info@olimann.com</a></address>
<h2>2. Was diese Website nicht tut</h2><p>Diese Website setzt keine Cookies und verwendet keine Analyse- oder Tracking-Dienste. Schriften und alle weiteren Ressourcen werden von unserer eigenen Domain ausgeliefert; beim Aufruf einer Seite werden keine Anfragen an Dritte gestellt.</p>
<h2>3. Hosting und Server-Logfiles</h2><p>Diese Website wird bei Hostinger International Ltd., 61 Lordou Vironos Street, 6023 Larnaca, Zypern, in einem Rechenzentrum in der Europäischen Union (<mark class="todo">[Standort, z. B. Niederlande]</mark>) gehostet. Beim Aufruf der Website verarbeitet der Webserver automatisch die IP-Adresse des anfragenden Geräts, Datum und Uhrzeit, die aufgerufene URL, die zuvor besuchte Seite (Referrer), Browsertyp und -version sowie das Betriebssystem. Dies ist zur Auslieferung der Website und zur Gewährleistung ihrer Sicherheit und Stabilität erforderlich. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO. Die Logfiles werden spätestens nach <mark class="todo">[14]</mark> Tagen gelöscht. Mit dem Hosting-Anbieter besteht ein Auftragsverarbeitungsvertrag nach Art. 28 DSGVO.</p>
<h2>4. Formular „Engpass-Analyse“</h2><p>Wenn Sie über das Formular eine Analyse anfragen, verarbeiten wir die von Ihnen eingegebenen Angaben: Name, Unternehmen, Rolle, E-Mail-Adresse, Website (optional), Ihre Antworten auf die Fragen zu Ihrem Unternehmen sowie den Zeitpunkt der Übermittlung. Die Daten werden auf unserem Webserver gespeichert (siehe Ziffer 3) und gegebenenfalls zusätzlich an unser Postfach weitergeleitet; sie werden ausschließlich zur Vorbereitung und Durchführung der Analyse sowie zur Kontaktaufnahme in dieser Sache verwendet. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO (vorvertragliche Maßnahmen) sowie Art. 6 Abs. 1 lit. f DSGVO (unser berechtigtes Interesse an der Beantwortung von Anfragen). Wir speichern die Daten, solange es zur Bearbeitung Ihrer Anfrage erforderlich ist; kommt keine Geschäftsbeziehung zustande, werden sie nach <mark class="todo">[12]</mark> Monaten gelöscht. Gesetzliche Aufbewahrungspflichten bleiben unberührt. Das Formular enthält ein verborgenes Feld, das ausschließlich der Erkennung automatisierter Eingaben dient; hierfür werden keine Daten gespeichert.</p>
<h2>5. Kontakt per E-Mail</h2><p>Wenn Sie uns per E-Mail kontaktieren, verarbeiten wir Ihre E-Mail-Adresse und den Inhalt Ihrer Nachricht zur Bearbeitung Ihres Anliegens. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b bzw. lit. f DSGVO.</p>
<h2>6. Empfänger</h2><p>Wir verkaufen oder teilen Ihre Daten nicht. Empfänger sind ausschließlich unser Hosting-Anbieter (siehe Ziffer 3) und unser E-Mail-Anbieter, jeweils auf Grundlage eines Auftragsverarbeitungsvertrags. Eine Übermittlung in Länder außerhalb der EU/des EWR findet nicht statt, sofern Sie nicht anderweitig informiert wurden.</p>
<h2>7. Ihre Rechte</h2><p>Sie haben das Recht auf Auskunft (Art. 15 DSGVO), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung der Verarbeitung (Art. 18), Datenübertragbarkeit (Art. 20) sowie das Recht, einer Verarbeitung auf Grundlage von Art. 6 Abs. 1 lit. f DSGVO zu widersprechen (Art. 21). Außerdem haben Sie das Recht, sich bei einer Aufsichtsbehörde zu beschweren (Art. 77 DSGVO), etwa bei der Datenschutzbehörde des Bundeslandes, in dem wir unseren Sitz haben. Zur Ausübung Ihrer Rechte wenden Sie sich an <a href="mailto:info@olimann.com">info@olimann.com</a>.</p>
<h2>8. Änderungen</h2><p>Wir passen diese Erklärung an, wenn sich die Website oder die Rechtslage ändert. Die jeweils aktuelle Fassung finden Sie auf dieser Seite.</p>"""),
    notfound=dict(eyebrow="404", h1="Diese Seite gibt es hier nicht.", p="Den Rest der Website schon.", cta="Zur Startseite"),
)
