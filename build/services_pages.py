#!/usr/bin/env python3
"""Service pages beyond WhatsApp, plus the /services/ hub. Built by pages.py via seo_pages.build().

Same rule as the rest of the site: only claims IMADI Tech can stand behind.
"""
import html

from generate import page, write, SITE_URL, ORG_ID
from seo_pages import WA_MARIA, breadcrumb
from growth_pages import _card_grid, _faq, DEV_PATH

e = html.escape

SERVICES = [
    {
        "slug": "marketing-automation",
        "nav": "Instagram & Facebook marketing automation",
        "short": "Marketing automation",
        "title": "Instagram & Facebook Marketing Automation in Pakistan | IMADI Tech",
        "description": "Marketing bots that design branded posts, carousels and voiced reels and publish them to Instagram and Facebook on schedule, with a WhatsApp button on every post.",
        "eyebrow": "Services · Marketing automation",
        "h1": "Instagram and Facebook marketing automation",
        "intro": ("Posting every day takes hours most business owners don't have. IMADI Tech builds marketing bots that design your posts, carousels and reels "
                  "in your brand colors, write the captions, record a natural voiceover, and publish to Instagram and Facebook on a fixed schedule. "
                  "Every post carries your WhatsApp number, so people who see it can message you straight away."),
        "problems": [
            ("No time to post", "Posting stops when the business gets busy, and the page goes quiet for weeks."),
            ("Posts that don't look like your brand", "Different templates and apps make the page look inconsistent."),
            ("Followers but no messages", "Posts get likes but don't tell people how to reach you on WhatsApp."),
        ],
        "features": [
            "Posts, carousels and reels designed in your brand colors, in light and dark styles",
            "Reels with a natural English voiceover, and screen recordings of your product or work",
            "Captions and hashtags written for each post",
            "Published to Instagram and Facebook on a schedule you choose, through Meta's official API",
            "Your WhatsApp number and a click-to-chat link on every post",
            "Runs on its own once set up; you add new topics when you want",
        ],
        "steps": [
            ("Plan", "We agree your posting days, times, topics and the look of your posts."),
            ("Build", "We build the bot with your logo, colors, content and voice."),
            ("Connect", "We connect your Instagram business account and Facebook Page through Meta's official API."),
            ("Run", "The bot posts on schedule. You see every post on your pages and can pause it any time."),
        ],
        "proof": [
            ("case", "hercommerce", "HerCommerce runs its own automated Instagram and Facebook marketing bot, built by IMADI Tech."),
            ("link", "https://www.instagram.com/imadi.tech/", "IMADI Tech on Instagram", "IMADI Tech's own pages are posted by the same kind of bot, every day except Sunday."),
            ("link", "https://github.com/Mariyah52/imadi-marketing", "The bot's code on GitHub", "The marketing bot behind IMADI Tech's pages, open for anyone to read."),
        ],
        "faq": [
            ("Does the bot post by itself?", "Yes. Once it's set up, it designs and publishes posts, carousels and reels to Instagram and Facebook on your schedule without anyone logging in."),
            ("Is it safe for my Instagram account?", "Yes. It publishes through Meta's official Graph API using your own business account, not through unofficial apps or shared logins."),
            ("Can it make reels with voice?", "Yes. Reels can include a natural English voiceover, text scenes in your brand style, and screen recordings of your product or work."),
            ("Can it post to WhatsApp Status?", "No. WhatsApp doesn't allow automatic Status posting for business numbers, so the bot focuses on Instagram and Facebook and adds your WhatsApp link to every post."),
        ],
    },
    {
        "slug": "email-follow-up-automation",
        "nav": "Email follow-up automation",
        "short": "Email follow-up",
        "title": "Email Follow-up & Enquiry Automation for Businesses | IMADI Tech",
        "description": "Automation that replies to email enquiries, sends quotations, follows up with customers who go silent, and tracks every lead in one dashboard, alongside WhatsApp.",
        "eyebrow": "Services · Email automation",
        "h1": "Email follow-up automation for sales enquiries",
        "intro": ("Many B2B buyers send an enquiry by email, receive a quotation, and then go quiet. IMADI Tech builds automation that answers email enquiries quickly, "
                  "sends quotations, follows up at the right times until the customer replies, and puts every lead, from email and WhatsApp, in one dashboard."),
        "problems": [
            ("Quotations that go silent", "A quotation goes out and nobody checks back, so the order goes to a competitor."),
            ("Leads buried in the inbox", "Enquiries sit between other emails and get answered late, or not at all."),
            ("No view of the pipeline", "Without one list, it's hard to see which enquiries are new, quoted, won or lost."),
        ],
        "features": [
            "Reads new enquiries from your business inbox and logs them as leads",
            "Sends a first reply, or a quotation, in your company's name",
            "Follows up on a schedule you set, and stops as soon as the customer replies",
            "Hands warm leads to your sales team with the full email history",
            "Shows every lead from email and WhatsApp in one dashboard",
            "Works with Gmail, Google Workspace and Outlook mailboxes",
        ],
        "steps": [
            ("Map", "We look at how enquiries arrive today and what your team sends back."),
            ("Write", "We write the replies and follow-up emails with you, in your tone."),
            ("Connect", "We connect your mailbox and set the follow-up timing."),
            ("Track", "Your team works from one dashboard, and the system follows up for them."),
        ],
        "proof": [
            ("case", "company-monitor", "Company Monitor: one dashboard for every lead and conversation across branches."),
            ("page", "/whatsapp-automation/", "WhatsApp lead automation", "The same follow-up and dashboard approach, on WhatsApp."),
        ],
        "faq": [
            ("Will customers know the emails are automated?", "The emails are written with you, in your company's tone, and sent from your own address. They read like a normal follow-up from your team."),
            ("Does it stop when the customer replies?", "Yes. As soon as a customer replies, follow-ups stop and the lead goes to your team."),
            ("Can it work together with WhatsApp?", "Yes. Leads from email and WhatsApp can go into the same dashboard, so your team sees everything in one place."),
        ],
    },
    {
        "slug": "erp-business-software",
        "nav": "Custom ERP & business software",
        "short": "ERP & business software",
        "title": "Custom ERP & Business Management Software in Pakistan | IMADI Tech",
        "description": "Custom ERP and business management software for small and mid-sized businesses: quotations, invoices, stock, ledgers, payments and accounting, built around your workflow.",
        "eyebrow": "Services · ERP & business software",
        "h1": "Custom ERP and business management software",
        "intro": ("Off-the-shelf software rarely fits how a growing business actually works. IMADI Tech builds business management systems around your own workflow: "
                  "quotations, delivery challans, invoices, stock, customer ledgers, payments and accounts, with the documents your customers expect and access for each team member."),
        "problems": [
            ("Spreadsheets and paper", "Quotations, invoices and stock live in separate files, and totals don't match."),
            ("Software that doesn't fit", "Generic apps force your team to change how it works, or leave half the job outside the system."),
            ("No clear numbers", "It's hard to see who owes what, what's in stock, and what was sold this month."),
        ],
        "features": [
            "Quotations, delivery challans and invoices with your branding",
            "Stock, purchases and expenses",
            "Customer and supplier ledgers, payments and balances",
            "Roles and permissions for each team member",
            "Works on phone and computer, with offline mode where needed",
            "Accounting features such as VAT, credit notes and reports for larger systems",
        ],
        "steps": [
            ("Map", "We sit with your team and map every document and step you use today."),
            ("Build", "We build in stages and show you working screens as we go."),
            ("Move in", "We bring in your existing customers, products and balances."),
            ("Support", "We fix issues and add features as your business grows."),
        ],
        "proof": [
            ("case", "alico", "ALICO Business Suite: quotations, invoices, stock and payments for a Karachi supply company."),
            ("case", "shah", "SHAH Enterprise Business Suite, adapted for a second business."),
            ("case", "uk-logistics-erp", "ERP and accounting platform with UK VAT for a logistics company in the UK."),
        ],
        "faq": [
            ("Why custom software instead of an off-the-shelf app?", "Custom software follows your own documents and workflow, so your team doesn't have to work around the system, and you only pay for what you use."),
            ("Can it work on mobile?", "Yes. IMADI Tech builds web apps that work on phones and computers, and can work offline and sync when the connection returns."),
            ("Can you connect it to WhatsApp?", "Yes. Quotations and invoices can be shared on WhatsApp, and a WhatsApp assistant can feed leads straight into the system."),
        ],
    },
]


def _steps(steps):
    return "".join(f'<div class="card"><div class="eyebrow">Step {i}</div><h3>{e(t)}</h3><p>{e(d)}</p></div>'
                   for i, (t, d) in enumerate(steps, 1))


def _proof(items, by_slug):
    out = []
    for item in items:
        if item[0] == "case" and item[1] in by_slug:
            name = by_slug[item[1]]["name"].split(":")[0]
            out.append(f'<a class="card project-card" href="/case-study/{item[1]}/"><h3>{e(name)}</h3><p>{e(item[2])}</p>'
                       f'<span class="arrow">Read the {e(name)} case study →</span></a>')
        elif item[0] == "link":
            out.append(f'<a class="card project-card" href="{item[1]}" target="_blank" rel="noopener"><h3>{e(item[2])}</h3>'
                       f'<p>{e(item[3])}</p><span class="arrow">Open →</span></a>')
        elif item[0] == "page":
            out.append(f'<a class="card project-card" href="{item[1]}"><h3>{e(item[2])}</h3><p>{e(item[3])}</p>'
                       f'<span class="arrow">See {e(item[2].lower())} →</span></a>')
    return "".join(out)


def service_page(s, by_slug):
    path = f"/{s['slug']}/"
    body = f'''
        <section class="wrap page-hero">
            <div class="eyebrow">{e(s["eyebrow"])}</div>
            <h1>{e(s["h1"])}</h1>
            <p>{e(s["intro"])}</p>
            <div class="hero-actions" style="margin-top:22px;">
                <a class="btn primary" href="{WA_MARIA}" target="_blank" rel="noopener" data-track="service_whatsapp">Book a free 10-minute demo on WhatsApp</a>
                <a class="btn" href="/services/">All services</a>
            </div>
        </section>

        <section class="wrap section">
            <div class="section-head"><div class="eyebrow">The problem</div><h2>What it fixes</h2></div>
            <div class="grid three">{_card_grid(s["problems"])}</div>
        </section>

        <section class="wrap section">
            <div class="section-head"><div class="eyebrow">What you get</div><h2>What it does</h2></div>
            <ul class="feature-list">{"".join(f"<li>{e(f)}</li>" for f in s["features"])}</ul>
        </section>

        <section class="wrap section">
            <div class="section-head"><div class="eyebrow">How it works</div><h2>From first call to running system</h2></div>
            <div class="grid two">{_steps(s["steps"])}</div>
        </section>

        <section class="wrap section">
            <div class="section-head"><div class="eyebrow">Proof</div><h2>Work by IMADI Tech</h2></div>
            <div class="grid two">{_proof(s["proof"], by_slug)}</div>
        </section>

        <section class="wrap section">
            <div class="section-head"><div class="eyebrow">FAQ</div><h2>Common questions</h2></div>
            <div class="faq-list">{_faq(s["faq"])}</div>
        </section>

        <section class="wrap section">
            <div class="card feature center" style="padding:44px;text-align:center;">
                <h2>See it working for your business</h2>
                <p style="max-width:520px;margin:0 auto 24px;">A free 10-minute demo, set up around a business like yours.</p>
                <a class="btn primary" href="{WA_MARIA}" target="_blank" rel="noopener">Book a demo on WhatsApp</a>
                <p style="margin:18px 0 0;"><a href="/services/">See all IMADI Tech services</a></p>
            </div>
        </section>
'''
    ld = [
        {"@type": "Service", "@id": SITE_URL + path + "#service", "name": s["h1"], "serviceType": s["nav"],
         "description": s["description"], "provider": {"@id": ORG_ID}, "url": SITE_URL + path,
         "areaServed": ["Pakistan", "United Arab Emirates", "United Kingdom"]},
        {"@type": "FAQPage", "@id": SITE_URL + path + "#faq",
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faq"]]},
        breadcrumb([("Home", "/"), ("Services", "/services/"), (s["short"], path)]),
    ]
    write(path + "index.html", page(s["title"], s["description"], path, body, ld=ld))
    return path


HUB = [
    ("/whatsapp-automation/", "WhatsApp chatbots & lead automation",
     "An AI assistant on your WhatsApp Business number that replies instantly, sends quotations, follows up and tracks every lead."),
] + [(f"/{s['slug']}/", s["nav"], s["description"]) for s in SERVICES] + [
    (DEV_PATH, "Development for agencies & companies",
     "Maria Aziz as your developer: WhatsApp bots, dashboards and automations built in Python, FastAPI, React and Meta's APIs."),
]


def services_hub():
    cards = "".join(f'<a class="card project-card" href="{u}"><h3>{e(t)}</h3><p>{e(d)}</p><span class="arrow">Learn more →</span></a>'
                    for u, t, d in HUB)
    body = f'''
        <section class="wrap page-hero">
            <div class="eyebrow">IMADI Tech · Services</div>
            <h1>AI automation and software for growing businesses</h1>
            <p>IMADI Tech, founded by Maria Aziz in Karachi, builds automation that saves your team hours every week: WhatsApp chatbots,
            Instagram and Facebook marketing bots, email follow-ups, and custom ERP and business software. Our systems are live for businesses
            in Pakistan, the UK and Kenya.</p>
            <div class="hero-actions" style="margin-top:22px;">
                <a class="btn primary" href="{WA_MARIA}" target="_blank" rel="noopener" data-track="services_whatsapp">Tell us what you want to automate</a>
                <a class="btn" href="/work/">See our work</a>
            </div>
        </section>
        <section class="wrap section" style="padding-top:8px;"><div class="grid two">{cards}</div></section>
        <section class="wrap section">
            <div class="section-head"><div class="eyebrow">By industry</div><h2>WhatsApp automation for your industry</h2></div>
            <p><a href="/whatsapp-automation/furniture/">Furniture & interiors</a> · <a href="/whatsapp-automation/kitchens-wardrobes/">Kitchens & wardrobes</a> ·
            <a href="/whatsapp-automation/logistics/">Logistics & delivery</a> · <a href="/whatsapp-automation/dubai-uae/">Dubai & UAE</a></p>
        </section>
'''
    ld = [
        {"@type": "ItemList", "@id": SITE_URL + "/services/#list", "name": "IMADI Tech services",
         "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": t, "url": SITE_URL + u} for i, (u, t, _) in enumerate(HUB)]},
        breadcrumb([("Home", "/"), ("Services", "/services/")]),
    ]
    write("/services/index.html", page("Services: WhatsApp, Marketing & Business Automation | IMADI Tech",
                                       "IMADI Tech services: WhatsApp chatbots, Instagram and Facebook marketing automation, email follow-up automation, and custom ERP and business software, from Karachi.",
                                       "/services/", body, ld=ld))
    return "/services/"


def build(projects):
    by_slug = {p["slug"]: p for p in projects}
    return [services_hub()] + [service_page(s, by_slug) for s in SERVICES]
