#!/usr/bin/env python3
"""SEO / AEO / GEO pages for imadi.tech, built by pages.py.

- One static page per case study at /case-study/<slug>/, rendered from
  assets/projects-data.js (needs Node to read that file), so search engines
  and AI crawlers see the full text without running JavaScript.
- /whatsapp-automation/ : the service page for business buyers.
- /faq/ : answer-first questions with FAQPage structured data.
- /llms.txt : a plain summary for AI assistants.

Only facts already stated on the site or by Maria are used here. Prices,
guarantees and security claims are deliberately left out until confirmed.
"""
import html
import json
import os
import subprocess

from generate import page, write, SITE_URL, ORG_ID, PERSON_ID, WEBSITE_ID

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WA_MARIA = "https://wa.me/923153205484?text=Hi%20Maria%2C%20I%20found%20IMADI%20Tech%20on%20imadi.tech%20and%20would%20like%20a%20demo."
e = html.escape


def load_projects():
    js = ("global.window={};require(process.argv[1]);"
          "process.stdout.write(JSON.stringify(window.PROJECTS))")
    out = subprocess.run(["node", "-e", js, os.path.join(ROOT, "assets", "projects-data.js")],
                         check=True, capture_output=True, text=True).stdout
    return json.loads(out)


def breadcrumb(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE_URL + u}
        for i, (n, u) in enumerate(items)]}


def clip(text, n=155):
    text = " ".join((text or "").split())
    return text if len(text) <= n else text[:n - 1].rsplit(" ", 1)[0] + "…"


# ------------------------------------------------------------ CASE STUDIES --
def case_study(p):
    slug, name = p["slug"], p["name"]
    short = name.split(":")[0]
    path = f"/case-study/{slug}/"

    def sec(title, inner):
        return f'<div class="case-section"><h2>{title}</h2>{inner}</div>'

    def para(field, title):
        return sec(title, f'<p>{e(p[field])}</p>') if p.get(field) else ""

    def items(field, title, kind):
        vals = p.get(field) or []
        if not vals:
            return ""
        if kind == "li":
            return sec(title, '<ul class="feature-list">' + "".join(f"<li>{e(v)}</li>" for v in vals) + "</ul>")
        cls, wrap = ("chip", "chip-row") if kind == "chip" else ("workflow-step", "workflow-steps")
        return sec(title, f'<div class="{wrap}">' + "".join(f'<span class="{cls}">{e(v)}</span>' for v in vals) + "</div>")

    evidence = ""
    if p.get("evidence"):
        evidence = sec("Links", '<div class="evidence-list">' + "".join(
            f'<a href="{e(x["href"])}" target="_blank" rel="noopener">{e(x["label"])} ↗</a>' for x in p["evidence"]) + "</div>")

    short_box = ""
    if p.get("plainProblem"):
        short_box = f'''
        <section class="wrap" id="case-short" style="padding:16px 0 0;">
            <div class="card ps-card ps-short">
                <div class="eyebrow">In short</div>
                <div class="ps"><p><b class="ps-l ps-p">Problem</b>{e(p["plainProblem"])}</p><p><b class="ps-l ps-s">Solution</b>{e(p.get("plainSolution") or "")}</p></div>
            </div>
        </section>'''

    letter = ""
    L = p.get("letter")
    if L:
        meta = (" · " + e(L["role"])) if L.get("role") else ""
        dated = (", dated " + e(L["date"])) if L.get("date") else ""
        letter = f'''
        <section class="wrap section" id="case-letter" style="padding-bottom:0;">
            <div class="section-head"><div class="eyebrow">Client letter</div><h2>In the client's words</h2></div>
            <div class="card letter-card">
                <a class="letter-thumb" href="{e(L["image"])}" target="_blank" rel="noopener"><img src="{e(L["image"])}" alt="Letter from the client confirming delivery" loading="lazy"></a>
                <div>
                    <blockquote>“{e(L["quote"])}”</blockquote>
                    <p class="letter-by"><strong>{e(L["name"])}</strong><span>{meta}</span></p>
                    <p class="letter-note">Signed and stamped letter confirming the software was developed and delivered{dated}. Commercial terms are withheld.</p>
                    <a class="btn small" href="{e(L["image"])}" target="_blank" rel="noopener">View full letter ↗</a>
                </div>
            </div>
        </section>'''

    body = f'''
        <section class="wrap page-hero">
            <div class="eyebrow">{e(p.get("tagline") or "Case study")}</div>
            <h1>{e(name)}</h1>
            <div class="case-hero-meta">
                <span class="project-status" data-status="{e(p.get("status") or "")}">{e(p.get("status") or "")}</span>
                <span class="case-meta">{e(p.get("client") or "")}</span>
                <span class="case-meta">{e(p.get("period") or "")}</span>
            </div>
        </section>{short_box}{letter}
        <section class="wrap" style="padding:20px 0 60px;">
            <div class="card" style="padding:8px 40px;">
                {para("problem", "The Problem")}
                {para("challenge", "The Challenge")}
                {para("solution", "The Solution")}
                {items("features", "Key Features", "li")}
                {para("myRole", "My Role")}
                {items("technology", "Technology", "chip")}
                {items("architecture", "Architecture", "step")}
                {para("innovation", "What's Different")}
                {items("results", "Results", "li")}
                {evidence}
            </div>
        </section>
        <section class="wrap section">
            <div class="card feature center" style="padding:44px;text-align:center;">
                <h2>Have a similar problem?</h2>
                <p style="max-width:480px;margin:0 auto 24px;">Let's talk through what you're trying to solve.</p>
                <a class="btn primary" href="/contact/">Discuss your problem</a>
                <p style="margin:18px 0 0;"><a href="/work/">See all case studies</a> · <a href="/whatsapp-automation/">WhatsApp lead automation</a></p>
            </div>
        </section>
'''
    # Demo videos and pictures still load from the media data, as before.
    scripts = f'''    <script src="/assets/projects-data.js"></script>
    <script src="/assets/media-data.js"></script>
    <script src="/assets/media-loader.js"></script>
    <script>
        (function () {{
            var project = window.getProjectBySlug && window.getProjectBySlug({json.dumps(slug)});
            if (!project || !window.loadMedia) return;
            window.loadMedia().then(function (m) {{
                var vids = (m.videos || []).filter(function (v) {{ return window.mediaMatchesProject(v, project); }});
                var pics = (m.photos || []).filter(function (v) {{ return window.mediaMatchesProject(v, project); }});
                if (!vids.length && !pics.length) return;
                var sec = document.createElement('section');
                sec.className = 'wrap section reveal in';
                sec.innerHTML = '<div class="section-head"><div class="eyebrow">Demo</div><h2>See it in action</h2></div><div class="media-grid"></div>';
                var grid = sec.querySelector('.media-grid');
                vids.forEach(function (v) {{ grid.appendChild(window.mediaVideoCard({{ title: v.title, caption: v.caption, src: v.src, webm: v.webm, poster: v.poster }})); }});
                pics.forEach(function (v) {{
                    var card = document.createElement('a');
                    card.className = 'media-card media-pic'; card.href = window.mediaImageUrl(v.src); card.target = '_blank'; card.rel = 'noopener';
                    var img = document.createElement('img'); img.src = window.mediaImageUrl(v.src); img.alt = v.title || 'Demo picture'; img.loading = 'lazy';
                    var c = document.createElement('div'); c.className = 'cap';
                    var t = document.createElement('strong'); t.textContent = v.title || ''; c.appendChild(t);
                    if (v.caption) {{ var sp = document.createElement('span'); sp.textContent = v.caption; c.appendChild(sp); }}
                    card.appendChild(img); card.appendChild(c); grid.appendChild(card);
                }});
                if (pics.length && !vids.length) grid.classList.add('single');
                var main = document.getElementById('main');
                var anchor = document.getElementById('case-letter') || document.getElementById('case-short');
                main.insertBefore(sec, anchor ? anchor.nextSibling : main.children[1] || null);
            }});
        }})();
    </script>
'''
    ld = [
        {"@type": "CreativeWork", "@id": SITE_URL + path + "#case-study", "name": f"{name}: case study",
         "url": SITE_URL + path, "about": p.get("plainProblem") or p.get("problem"),
         "author": {"@id": PERSON_ID}, "publisher": {"@id": ORG_ID}, "isPartOf": {"@id": WEBSITE_ID},
         "keywords": ", ".join(p.get("technology") or [])},
        breadcrumb([("Home", "/"), ("Work", "/work/"), (short, path)]),
    ]
    write(path + "index.html", page(
        f"{short} Case Study | IMADI Tech",
        clip(p.get("plainProblem") or p.get("problem")),
        path, body, extra_scripts=scripts, ld=ld))
    return path


# ------------------------------------------------------- SERVICE PAGE ------
SERVICE_BODY = f'''
        <section class="wrap page-hero">
            <div class="eyebrow">IMADI Tech · WhatsApp &amp; Instagram lead automation · Karachi</div>
            <h1>Reply to every lead from your ads, instantly</h1>
            <p>IMADI Tech sets up an AI assistant on your WhatsApp Business number that answers every enquiry within seconds, day or night. It shares your designs and price ranges, collects details like size and city, sends a quotation, follows up with customers who go quiet, and shows every lead in one dashboard.</p>
            <div class="hero-actions" style="margin-top:22px;">
                <a class="btn primary" href="{WA_MARIA}" target="_blank" rel="noopener" data-track="service_whatsapp">Book a free 10-minute demo on WhatsApp</a>
                <a class="btn" href="/contact/?source=whatsapp-automation">Send an enquiry</a>
            </div>
        </section>

        <section class="wrap section">
            <div class="section-head">
                <div class="eyebrow">The problem</div>
                <h2>Why businesses lose leads they already paid for</h2>
            </div>
            <div class="grid two">
                <div class="card"><h3>Late replies</h3><p>A customer asks for a price at 10pm and gets an answer the next afternoon. By then they have messaged two other shops.</p></div>
                <div class="card"><h3>No follow-up</h3><p>After a quotation, many customers go quiet. Nobody has time to follow up with each one, so the sale slips away.</p></div>
                <div class="card"><h3>Leads spread across phones</h3><p>Enquiries sit on several salespeople's phones, so the owner cannot see which leads were answered, quoted, won or lost.</p></div>
                <div class="card"><h3>More ad spend, same sales</h3><p>When enquiries are not handled well, raising the ad budget brings more messages but not more orders.</p></div>
            </div>
        </section>

        <section class="wrap section">
            <div class="section-head">
                <div class="eyebrow">What's included</div>
                <h2>What the WhatsApp lead system does</h2>
            </div>
            <ul class="feature-list">
                <li>Instant replies on WhatsApp in English or Roman Urdu, set up around your products, prices and questions</li>
                <li>Shares your catalogue, designs and price ranges from a sheet you can update yourself</li>
                <li>Asks qualifying questions such as product, size, city and budget</li>
                <li>Sends quotations as PDF documents on WhatsApp</li>
                <li>Automatic follow-up messages for customers who stop replying</li>
                <li>Hands the chat to your salesperson when a customer asks for a person or is ready to buy</li>
                <li>A dashboard with every lead and its status: new, in process, quoted, won or lost</li>
                <li>Instagram DM and comment replies, connected to the same lead list (add-on)</li>
            </ul>
        </section>

        <section class="wrap section">
            <div class="section-head">
                <div class="eyebrow">Who it's for</div>
                <h2>Built for businesses that sell through enquiries</h2>
                <p class="section-intro">It suits owner-led businesses that run Facebook, Instagram or Google ads and receive many WhatsApp enquiries, especially where each order is high in value and needs a quotation.</p>
            </div>
            <div class="grid three">
                <div class="card"><h3>Furniture &amp; interiors</h3><p>Showrooms, custom furniture makers and interior fit-out firms.</p></div>
                <div class="card"><h3>Kitchens &amp; wardrobes</h3><p>Kitchen, cabinet and wardrobe companies that quote by size and material.</p></div>
                <div class="card"><h3>Suppliers &amp; logistics</h3><p>Building material suppliers, distributors and logistics companies.</p></div>
            </div>
        </section>

        <section class="wrap section">
            <div class="section-head">
                <div class="eyebrow">How it works</div>
                <h2>From first call to live system</h2>
            </div>
            <ol class="feature-list">
                <li><strong>Free 10-minute demo.</strong> See the assistant reply, ask questions and send a quotation, using an example like your own business.</li>
                <li><strong>Workflow call.</strong> We map your products, price list, common questions and who on your team handles which leads.</li>
                <li><strong>WhatsApp Business setup.</strong> We connect your number through Meta's official WhatsApp Business Platform and complete Meta's verification steps with you.</li>
                <li><strong>Build and test.</strong> IMADI Tech builds the conversation, quotation and follow-up flows and tests them with you before customers see them.</li>
                <li><strong>Go live and review.</strong> Your team gets the dashboard, and we review the results with you and adjust the flows.</li>
            </ol>
        </section>

        <section class="wrap section">
            <div class="section-head">
                <div class="eyebrow">Proof</div>
                <h2>WhatsApp systems IMADI Tech has already built</h2>
            </div>
            <div class="grid three">
                <a class="card project-card" href="/case-study/uk-logistics-whatsapp/"><h3>UK logistics claims bot</h3><p>A WhatsApp bot that runs a UK logistics company's damage-claims process, with approvals from one dashboard.</p><span class="arrow">Read the UK logistics case study →</span></a>
                <a class="card project-card" href="/case-study/company-monitor/"><h3>Company Monitor</h3><p>Lets a multi-branch business in Nairobi see every WhatsApp lead and conversation across branches and salespeople.</p><span class="arrow">Read the Company Monitor case study →</span></a>
                <a class="card project-card" href="/case-study/renaz/"><h3>ReNaz scrap collection</h3><p>Customers and collectors in Karachi book and complete pickups entirely through WhatsApp.</p><span class="arrow">Read the ReNaz case study →</span></a>
            </div>
        </section>

        <section class="wrap section">
            <div class="card feature center" style="padding:44px;text-align:center;">
                <h2>See it working for your business</h2>
                <p style="max-width:520px;margin:0 auto 24px;">Book a free 10-minute demo. Setup cost depends on your products and flows, and you get a fixed quote before any work starts.</p>
                <a class="btn primary" href="{WA_MARIA}" target="_blank" rel="noopener">Book a demo on WhatsApp</a>
                <p style="margin:18px 0 0;">Or email <a href="mailto:maria@imadi.tech">maria@imadi.tech</a> · Read the <a href="/faq/">FAQ</a></p>
            </div>
        </section>
'''

SERVICE_LD = [
    {"@type": "Service", "@id": SITE_URL + "/whatsapp-automation/#service",
     "name": "WhatsApp & Instagram lead automation",
     "serviceType": "WhatsApp chatbot and lead follow-up automation",
     "description": ("An AI assistant on a business's WhatsApp number that replies to enquiries instantly, shares designs "
                     "and price ranges, sends PDF quotations, follows up automatically and tracks every lead in a dashboard."),
     "provider": {"@id": ORG_ID},
     "areaServed": [{"@type": "City", "name": "Karachi"}, {"@type": "Country", "name": "Pakistan"},
                    {"@type": "Country", "name": "United Arab Emirates"}],
     "audience": {"@type": "BusinessAudience",
                  "audienceType": "Furniture, kitchen, interior, building supply and logistics businesses"},
     "url": SITE_URL + "/whatsapp-automation/"},
    breadcrumb([("Home", "/"), ("WhatsApp Automation", "/whatsapp-automation/")]),
]


# ------------------------------------------------------------------- FAQ ---
# Each answer starts with a direct one-sentence answer, which is what search
# and AI answer engines quote. Keep answers true to what IMADI Tech delivers.
FAQ = [
    ("What does IMADI Tech do?",
     "IMADI Tech builds AI automation for businesses: WhatsApp chatbots and lead follow-up systems, custom ERP and "
     "business management software, and SaaS products. It was founded in May 2026 by Maria Aziz in Karachi, Pakistan, "
     "and has built platforms for clients in Pakistan, the UK and Kenya."),
    ("Who is IMADI Tech for?",
     "IMADI Tech works with small and mid-sized, owner-led businesses that get many enquiries on WhatsApp, Instagram "
     "or Facebook. It is a strong fit for furniture, kitchen, interior, building supply and logistics businesses, "
     "where each order needs a quotation."),
    ("How does a WhatsApp chatbot help a business get more sales?",
     "A WhatsApp chatbot replies to every enquiry within seconds, so customers get an answer while they are still "
     "interested. It also asks qualifying questions, sends quotations and follows up with people who go quiet, "
     "which are the steps where most leads are usually lost."),
    ("Does the chatbot replace my sales team?",
     "No. The chatbot handles first replies, common questions, quotations and reminders, then hands the conversation "
     "to your salesperson when a customer asks for a person or is ready to buy. Your team spends its time on serious buyers."),
    ("Will I lose my WhatsApp number or my old chats?",
     "You keep your business number, but it is connected to Meta's official WhatsApp Business Platform. Before setup, "
     "IMADI Tech checks with you whether your number can stay on the WhatsApp Business app alongside the platform or "
     "whether a separate number is better, so you know exactly what happens to your existing chats."),
    ("Can the chatbot reply in Roman Urdu?",
     "Yes. The assistant can be set up to reply in English or Roman Urdu, matching how your customers write to you."),
    ("Can it send quotations and price lists?",
     "Yes. The assistant can share your catalogue and price ranges from a sheet you update yourself, and send "
     "quotations as PDF documents on WhatsApp."),
    ("Can IMADI Tech automate Instagram messages too?",
     "Yes, as an add-on. Instagram direct messages and replies to comments can be answered automatically and added "
     "to the same lead list as WhatsApp. This needs an Instagram professional account linked to your Facebook Page."),
    ("How long does setup take?",
     "Setup time depends on how many products and flows you need, and Meta's business verification can add time. "
     "You get a timeline in writing before work starts."),
    ("How much does it cost?",
     "Pricing is a one-time setup fee plus monthly support, quoted after a free 10-minute demo once your products and "
     "flows are clear. Meta bills its WhatsApp messaging charges directly to your business."),
    ("Where is IMADI Tech based, and do you work with clients outside Pakistan?",
     "IMADI Tech is based in Karachi, Pakistan, and works remotely with clients elsewhere. It has delivered projects "
     "for businesses in Pakistan, the United Kingdom and Kenya, and also takes on clients in the UAE."),
    ("Who is Maria Aziz?",
     "Maria Aziz is the founder of IMADI Tech, based in Karachi. She builds AI-powered business software, including "
     "WhatsApp chatbots, ERP systems and SaaS products, and studied at the University of Karachi with an AI "
     "specialization certificate from IBA Karachi."),
    ("How do I book a demo?",
     "Message Maria on WhatsApp from the button on this page, or email maria@imadi.tech. The demo takes about 10 "
     "minutes and shows the assistant replying, qualifying a lead and sending a quotation."),
]


def faq_body():
    items = "".join(
        f'''
                <details class="faq-item"{' open' if i < 3 else ''}>
                    <summary><h2 class="faq-q">{e(q)}</h2></summary>
                    <p>{e(a)}</p>
                </details>''' for i, (q, a) in enumerate(FAQ))
    return f'''
        <section class="wrap page-hero">
            <div class="eyebrow">IMADI Tech · FAQ</div>
            <h1>Frequently asked questions</h1>
            <p>Straight answers about WhatsApp chatbots, lead automation and working with IMADI Tech.</p>
        </section>
        <section class="wrap section" style="padding-top:8px;">
            <div class="faq-list">{items}
            </div>
        </section>
        <section class="wrap section">
            <div class="card feature center" style="padding:40px;text-align:center;">
                <h2>Still have a question?</h2>
                <p style="max-width:480px;margin:0 auto 22px;">Ask Maria directly, or see how the WhatsApp lead system works.</p>
                <a class="btn primary" href="{WA_MARIA}" target="_blank" rel="noopener">Ask on WhatsApp</a>
                <a class="btn" href="/whatsapp-automation/">How it works</a>
            </div>
        </section>
'''


FAQ_LD = [
    {"@type": "FAQPage", "@id": SITE_URL + "/faq/#faq",
     "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]},
    breadcrumb([("Home", "/"), ("FAQ", "/faq/")]),
]


def llms_txt(projects):
    lines = [
        "# IMADI Tech",
        "",
        "> IMADI Tech is an AI automation company in Karachi, Pakistan, founded by Maria Aziz in May 2026. "
        "It builds WhatsApp chatbots and lead follow-up automation, Instagram and Facebook marketing automation, email follow-up automation, custom ERP and business management systems, "
        "and SaaS products for small and mid-sized businesses. It has delivered projects in Pakistan, the UK and Kenya "
        "and also takes on clients in the UAE.",
        "",
        "Contact: maria@imadi.tech · Website: https://www.imadi.tech",
        "",
        "## Services",
        f"- [WhatsApp & Instagram lead automation]({SITE_URL}/whatsapp-automation/): an AI assistant that replies to "
        "every enquiry instantly, shares designs and price ranges, sends PDF quotations, follows up automatically and "
        "tracks every lead in a dashboard. Best fit: furniture, kitchen, interior, building supply and logistics businesses.",
        f"- [FAQ]({SITE_URL}/faq/): pricing model, setup, languages, WhatsApp number questions.",
        "",
        f"- [WhatsApp chatbot and AI automation developer in Pakistan]({SITE_URL}/whatsapp-chatbot-developer-pakistan/): Maria Aziz's developer profile, tech stack (Python, FastAPI, Flask, PostgreSQL, React, TypeScript, Firebase, Meta WhatsApp Cloud API and Graph API) and shipped systems.",
        f"- [All services]({SITE_URL}/services/): overview of every IMADI Tech service.",
    ] + [f"- [{x['nav']}]({SITE_URL}/{x['slug']}/): {x['description']}" for x in __import__('services_pages').SERVICES] + [
        "",
        "## By industry",
    ] + [f"- [{i['h1']}]({SITE_URL}/whatsapp-automation/{i['slug']}/): {i['description']}" for i in __import__('growth_pages').INDUSTRIES] + [
        "",
        "## Blog",
    ] + [f"- [{b['title']}]({SITE_URL}/blog/{b['slug']}/): {b['description']}" for b in __import__('growth_pages').POSTS] + [
        "",
        "## Case studies",
    ]
    for p in projects:
        if "client" in (p.get("categories") or []) or p["slug"] == "hercommerce":
            lines.append(f"- [{p['name']}]({SITE_URL}/case-study/{p['slug']}/): {clip(p.get('solution') or p.get('plainSolution'), 220)}")
    lines += ["", "## About",
              f"- [Maria Aziz, founder]({SITE_URL}/about/)",
              f"- [All work]({SITE_URL}/work/)",
              f"- [Contact]({SITE_URL}/contact/)", ""]
    write("/llms.txt", "\n".join(lines))


def build():
    import growth_pages
    projects = load_projects()
    paths = [case_study(p) for p in projects]
    write("/whatsapp-automation/index.html", page(
        "WhatsApp Chatbot & Lead Automation in Karachi | IMADI Tech",
        "AI WhatsApp and Instagram automation for furniture, kitchen, interior and supply businesses: instant replies, PDF quotations, auto follow-ups and one lead dashboard.",
        "/whatsapp-automation/", SERVICE_BODY + growth_pages.industry_links(), ld=SERVICE_LD))
    write("/faq/index.html", page(
        "WhatsApp Chatbot FAQ | IMADI Tech, Karachi",
        "Answers about WhatsApp chatbots and lead automation from IMADI Tech: cost, setup time, Urdu replies, quotations, Instagram and your WhatsApp number.",
        "/faq/", faq_body(), ld=FAQ_LD))
    llms_txt(projects)
    import services_pages
    return ["/whatsapp-automation/", "/faq/"] + growth_pages.build(projects) + services_pages.build(projects) + paths
