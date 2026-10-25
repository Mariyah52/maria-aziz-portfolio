#!/usr/bin/env python3
"""Industry landing pages and the blog for imadi.tech, built by pages.py.

Each industry page targets the searches a business owner in that industry makes
("WhatsApp chatbot for furniture business"), with its own FAQ and structured data.
Facts follow the same rule as the rest of the site: only what IMADI Tech has
actually built or can stand behind. No invented statistics or prices.
"""
import html

from generate import page, write, SITE_URL, ORG_ID, PERSON_ID, WEBSITE_ID
from seo_pages import WA_MARIA, breadcrumb

e = html.escape

INDUSTRIES = [
    {
        "slug": "furniture",
        "nav": "Furniture & interiors",
        "title": "WhatsApp Chatbot for Furniture & Interior Businesses | IMADI Tech",
        "description": "WhatsApp automation for furniture showrooms and interior firms in Karachi: instant replies with designs and prices, size questions, PDF quotes and automatic follow-ups.",
        "eyebrow": "WhatsApp automation · Furniture & interiors",
        "h1": "A WhatsApp assistant for furniture and interior businesses",
        "intro": ("Furniture buyers message several showrooms at once, usually in the evening, asking for photos, sizes and prices. "
                  "IMADI Tech sets up an AI assistant on your WhatsApp Business number that answers them instantly with your designs and price ranges, "
                  "asks for room size and city, sends a quotation, and follows up if they go quiet."),
        "problems": [
            ("Price questions at night", "Most \"price?\" and \"do you have this in walnut?\" messages arrive after the showroom closes and wait until the next day."),
            ("Quotes that go quiet", "Custom sofas, beds and wardrobes need a quote, and many buyers disappear after receiving one without a follow-up."),
            ("Leads on salespeople's phones", "When each salesperson handles their own chats, the owner can't see which leads were answered, quoted or lost."),
        ],
        "features": [
            "Shares your catalog photos and price ranges for sofas, beds, dining sets and wardrobes",
            "Asks the questions your team needs: product, size, fabric or wood, city and budget",
            "Sends a PDF quotation on WhatsApp with your logo",
            "Follows up the next day, and again a few days later, with buyers who stopped replying",
            "Hands serious buyers to your salesperson with the full chat attached",
            "Shows every lead, its status and its salesperson in one dashboard",
        ],
        "chat": [("in", "Assalam o Alaikum, what's the price of this L-shaped sofa? 👇"),
                 ("out", "Walaikum Assalam! It starts from the range on our price list. Which size do you need: 5, 6 or 7 seater?"),
                 ("in", "7 seater, in grey"),
                 ("out", "Great choice. Which city should we deliver to? I'll send your quotation right away.")],
        "proof": [("alico", "One business app for quotations, invoices, stock and payments."),
                  ("company-monitor", "See every WhatsApp lead and conversation across branches and salespeople.")],
        "faq": [
            ("Can the assistant show my furniture designs?", "Yes. It shares photos and price ranges from a catalog and price sheet that you update yourself, so new designs and price changes go live without calling a developer."),
            ("Can it handle custom sizes and fabrics?", "Yes. It collects the size, fabric or wood, color and city, then either sends a quotation from your price list or hands the chat to your team for a custom quote."),
            ("Will my salespeople still talk to customers?", "Yes. The assistant handles first replies and common questions, then passes buyers who are ready to your salespeople, with the full conversation attached."),
        ],
    },
    {
        "slug": "kitchens-wardrobes",
        "nav": "Kitchens & wardrobes",
        "title": "WhatsApp Chatbot for Kitchen & Wardrobe Companies | IMADI Tech",
        "description": "WhatsApp automation for kitchen, cabinet and wardrobe makers: collect measurements and photos, book site visits, send quotations and follow up automatically.",
        "eyebrow": "WhatsApp automation · Kitchens & wardrobes",
        "h1": "A WhatsApp assistant for kitchen and wardrobe companies",
        "intro": ("Kitchen and wardrobe projects start with questions about layouts, materials and measurements, and end with a quotation. "
                  "IMADI Tech's WhatsApp assistant collects those details and photos from the customer, books site visits, sends quotes, "
                  "and keeps following up, so your team spends its time measuring and building."),
        "problems": [
            ("The gap after measurement", "Customers wait days between the site visit and the estimate, and some sign with someone else in that time."),
            ("Scattered photos and sizes", "Kitchen photos, wall sizes and preferences arrive across several chats and are hard to find later."),
            ("Overseas clients in other time zones", "Pakistanis abroad furnishing a home here message while your team is asleep."),
        ],
        "features": [
            "Asks for kitchen layout (L-shape, U-shape, straight), wall sizes and photos",
            "Shares material and finish options with price ranges",
            "Books a site visit and confirms it on WhatsApp",
            "Sends the quotation as a PDF and reminds the customer before it expires",
            "Answers overseas clients instantly, at any hour",
            "Keeps every project's photos, sizes and messages together in one dashboard",
        ],
        "chat": [("in", "I want a new kitchen in my DHA flat. Can you send a quote?"),
                 ("out", "Of course! What layout is it: L-shape, U-shape or straight? Please share a photo and the wall lengths."),
                 ("in", "L-shape, 10 ft and 7 ft. Photo attached 📷"),
                 ("out", "Thank you! Would Saturday or Monday suit you for a free site visit?")],
        "proof": [("alico", "Quotations, challans and invoices generated in one app and shared on WhatsApp."),
                  ("renaz", "Customers book, share location and pick a time slot entirely on WhatsApp.")],
        "faq": [
            ("Can the assistant book site visits?", "Yes. It offers available days, confirms the visit on WhatsApp and adds it to your team's list, so nobody has to coordinate by phone."),
            ("Can it send quotations?", "Yes. It can send a quotation as a PDF from your price list, or hand the chat to your team when a project needs a custom estimate."),
            ("Does it work for overseas clients?", "Yes. It replies instantly at any hour, which helps with clients in the UAE, the UK and elsewhere who message while your team is offline."),
        ],
    },
    {
        "slug": "logistics",
        "nav": "Logistics & delivery",
        "title": "WhatsApp Bot for Logistics & Courier Companies | IMADI Tech",
        "description": "WhatsApp bots for logistics companies: rate questions, order inquiries, damage claims with photos and documents, and a dashboard to approve or reject them.",
        "eyebrow": "WhatsApp automation · Logistics",
        "h1": "WhatsApp bots for logistics and delivery companies",
        "intro": ("Logistics teams answer the same questions all day: rates, order status, and what to do when something arrives damaged. "
                  "IMADI Tech builds WhatsApp bots that handle those conversations step by step, collect the right details and documents, "
                  "and send everything to a dashboard where your team takes action."),
        "problems": [
            ("Claims buried in email", "Damage claims arrive as long email threads with photos and invoices scattered across messages."),
            ("Repeated rate questions", "Staff spend hours answering the same rate and coverage questions from customers."),
            ("No single view", "Without one dashboard, it's hard to see which claims or inquiries are open, approved or rejected."),
        ],
        "features": [
            "Guided claim filing on WhatsApp: claim type, shipment details, photos and invoice PDF",
            "Rate and coverage answers from a rate card you maintain",
            "Order and shipment inquiries routed to the right team",
            "A dashboard to review, raise, approve or reject each claim",
            "Customers kept updated on WhatsApp at every step",
        ],
        "chat": [("in", "NEW"),
                 ("out", "Hello! What would you like to report? 1. Damaged goods 2. Lost parcel"),
                 ("in", "1"),
                 ("out", "Sorry to hear that. Please send the tracking number, then photos of the label and the damage.")],
        "proof": [("uk-logistics-whatsapp", "A WhatsApp bot that runs a UK logistics company's damage-claims process."),
                  ("uk-logistics-erp", "A custom ERP and accounting platform with UK VAT and credit notes.")],
        "faq": [
            ("Can customers file claims on WhatsApp?", "Yes. The bot asks for the claim type, shipment details, labeled photos and the invoice, then submits a complete claim to your dashboard."),
            ("Can it answer rate questions?", "Yes. It answers from a rate card your team maintains, so prices stay correct without changing the bot."),
            ("Have you built this before?", "Yes. IMADI Tech built a WhatsApp claims bot and dashboard for a logistics company in the United Kingdom, where staff raise, approve or reject claims from one place."),
        ],
    },
    {
        "slug": "dubai-uae",
        "nav": "Dubai & UAE",
        "title": "WhatsApp Automation for Businesses in Dubai & the UAE | IMADI Tech",
        "description": "WhatsApp chatbots and lead follow-up automation for UAE businesses: instant replies to ad inquiries, quotations, follow-ups and a lead dashboard, built remotely by IMADI Tech.",
        "eyebrow": "WhatsApp automation · Dubai & UAE",
        "h1": "WhatsApp automation for businesses in Dubai and the UAE",
        "intro": ("In the UAE, customers expect a fast reply on WhatsApp, often in English, sometimes in Arabic or Urdu. "
                  "IMADI Tech builds AI assistants and follow-up automation that answer every inquiry from your ads instantly, "
                  "qualify the lead, send a quotation, and keep following up, with every lead visible in one dashboard."),
        "problems": [
            ("Inquiries that go silent", "Many customers ask for a price or quotation and then stop replying, and nobody follows up in time."),
            ("Ads without a fast response", "Meta and Google ads bring inquiries at all hours, but replies wait for office time."),
            ("No view of the pipeline", "Leads arriving by WhatsApp and email are hard to track from first message to sale."),
        ],
        "features": [
            "Instant WhatsApp replies in English, with Arabic or Urdu where needed",
            "Lead qualification: product, quantity, emirate and timeline",
            "Quotations sent on WhatsApp or email",
            "Automatic follow-ups for inquiries that go quiet",
            "One dashboard for WhatsApp and email leads",
            "Built and supported remotely, working in your time zone",
        ],
        "chat": [("in", "Hi, do you supply 500 units to Abu Dhabi? Need a quote."),
                 ("out", "Hi! Yes, we deliver across the UAE. Which product and size do you need?"),
                 ("in", "The 60cm model"),
                 ("out", "Thanks! I'm preparing your quotation now and will send it here in a moment.")],
        "proof": [("company-monitor", "Every WhatsApp lead and conversation across branches, in one dashboard."),
                  ("uk-logistics-whatsapp", "A WhatsApp bot running a full claims process for an international client.")],
        "faq": [
            ("Do you work with clients in the UAE?", "Yes. IMADI Tech works remotely with clients outside Pakistan and has delivered projects for businesses in the UK and Kenya."),
            ("Can the assistant reply in Arabic?", "The assistant can be set up for English, Arabic and Urdu replies, depending on your customers."),
            ("Can it follow up on email inquiries too?", "Yes. Follow-up automation can cover both WhatsApp and email inquiries, with every lead tracked in one dashboard."),
        ],
    },
]


def _card_grid(items):
    return "".join(f'<div class="card"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in items)


def _chat(msgs):
    rows = "".join(f'<div class="chat-msg chat-{side}">{e(t)}</div>' for side, t in msgs)
    return f'<div class="chat-demo" aria-label="Example WhatsApp conversation">{rows}<p class="chat-note">Example conversation</p></div>'


def _faq(items):
    return "".join(f'''
                <details class="faq-item">
                    <summary><h3 class="faq-q">{e(q)}</h3></summary>
                    <p>{e(a)}</p>
                </details>''' for q, a in items)


def industry_page(ind, projects_by_slug):
    path = f"/whatsapp-automation/{ind['slug']}/"
    proof = "".join(
        f'<a class="card project-card" href="/case-study/{s}/"><h3>{e(projects_by_slug[s]["name"].split(":")[0])}</h3>'
        f'<p>{e(text)}</p><span class="arrow">Read the {e(projects_by_slug[s]["name"].split(":")[0])} case study →</span></a>'
        for s, text in ind["proof"] if s in projects_by_slug)
    others = " · ".join(f'<a href="/whatsapp-automation/{o["slug"]}/">{e(o["nav"])}</a>' for o in INDUSTRIES if o is not ind)
    body = f'''
        <section class="wrap page-hero">
            <div class="eyebrow">{e(ind["eyebrow"])}</div>
            <h1>{e(ind["h1"])}</h1>
            <p>{e(ind["intro"])}</p>
            <div class="hero-actions" style="margin-top:22px;">
                <a class="btn primary" href="{WA_MARIA}" target="_blank" rel="noopener" data-track="industry_whatsapp">Book a free 10-minute demo on WhatsApp</a>
                <a class="btn" href="/whatsapp-automation/">How it works</a>
            </div>
        </section>

        <section class="wrap section">
            <div class="section-head"><div class="eyebrow">The problem</div><h2>Where leads get lost</h2></div>
            <div class="grid three">{_card_grid(ind["problems"])}</div>
        </section>

        <section class="wrap section">
            <div class="grid two industry-split">
                <div>
                    <div class="section-head"><div class="eyebrow">What it does</div><h2>What your WhatsApp assistant handles</h2></div>
                    <ul class="feature-list">{"".join(f"<li>{e(f)}</li>" for f in ind["features"])}</ul>
                </div>
                {_chat(ind["chat"])}
            </div>
        </section>

        <section class="wrap section">
            <div class="section-head"><div class="eyebrow">Proof</div><h2>Related work by IMADI Tech</h2></div>
            <div class="grid two">{proof}</div>
        </section>

        <section class="wrap section">
            <div class="section-head"><div class="eyebrow">FAQ</div><h2>Common questions</h2></div>
            <div class="faq-list">{_faq(ind["faq"])}</div>
            <p style="margin-top:16px;">More answers in the <a href="/faq/">full FAQ</a>.</p>
        </section>

        <section class="wrap section">
            <div class="card feature center" style="padding:44px;text-align:center;">
                <h2>See it working for your business</h2>
                <p style="max-width:520px;margin:0 auto 24px;">A free 10-minute demo, set up around a business like yours.</p>
                <a class="btn primary" href="{WA_MARIA}" target="_blank" rel="noopener">Book a demo on WhatsApp</a>
                <p style="margin:18px 0 0;">Other industries: {others}</p>
            </div>
        </section>
'''
    ld = [
        {"@type": "Service", "@id": SITE_URL + path + "#service", "name": ind["h1"],
         "serviceType": "WhatsApp chatbot and lead automation", "description": ind["description"],
         "provider": {"@id": ORG_ID}, "url": SITE_URL + path,
         "audience": {"@type": "BusinessAudience", "audienceType": ind["nav"]}},
        {"@type": "FAQPage", "@id": SITE_URL + path + "#faq",
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in ind["faq"]]},
        breadcrumb([("Home", "/"), ("WhatsApp Automation", "/whatsapp-automation/"), (ind["nav"], path)]),
    ]
    write(path + "index.html", page(ind["title"], ind["description"], path, body, ld=ld))
    return path


# ------------------------------------------------------------------- BLOG ---
# Each post: slug, title, description, date (ISO), and body HTML.
POSTS = [
    {
        "slug": "whatsapp-chatbot-cost-pakistan",
        "title": "How much does a WhatsApp chatbot cost in Pakistan?",
        "description": "What you actually pay for when you set up a WhatsApp chatbot in Pakistan: the build, monthly support, and Meta's own per-message charges, explained simply.",
        "date": "2026-10-25",
        "body": f'''
            <p class="post-lead"><strong>Short answer:</strong> a WhatsApp chatbot has three costs. A one-time setup fee to build it, a monthly fee for hosting and support, and Meta's own WhatsApp charges, which Meta bills to your business directly. How much each one comes to depends mostly on how many conversations you have and how much the bot needs to do.</p>

            <h2>1. The setup (one time)</h2>
            <p>This is the work of building the assistant around your business. It usually covers:</p>
            <ul>
                <li>Mapping your products, price list and the questions customers ask every day</li>
                <li>Writing the conversation: greetings, qualifying questions, hand-off to your team</li>
                <li>Connecting your number to Meta's official WhatsApp Business Platform and completing Meta's verification</li>
                <li>Extras such as PDF quotations, automatic follow-ups or a lead dashboard</li>
            </ul>
            <p>A simple bot that answers common questions costs far less than one that sends quotations, follows up and feeds a dashboard. That's why any honest quote comes after a short call about your workflow.</p>

            <h2>2. Hosting and support (monthly)</h2>
            <p>The bot runs on a server around the clock. The monthly fee covers keeping it online, updating answers and prices, fixing anything that breaks, and adjusting the flows as you learn what customers ask.</p>

            <h2>3. Meta's WhatsApp charges (paid to Meta)</h2>
            <p>Meta charges per <em>delivered message</em>, depending on the message category and the customer's country. Pakistan has its own rate on Meta's rate card. In broad terms, as of October 2026:</p>
            <ul>
                <li><strong>Messages from customers are free.</strong> You're never charged for what customers send you.</li>
                <li><strong>Service replies:</strong> each business number gets 1,000 free service messages a month, then they're charged.</li>
                <li><strong>Marketing, utility and authentication templates</strong> (for example, a follow-up sent after 24 hours, or an order update) are charged per message at Meta's published rates.</li>
                <li><strong>Click-to-WhatsApp ads:</strong> when someone messages you from one of these ads and you reply within 24 hours, Meta opens a free entry point window (up to 7 days) for your messages to that customer.</li>
            </ul>
            <p>Meta updates these rules regularly, so check <a href="https://developers.facebook.com/docs/whatsapp/pricing" target="_blank" rel="noopener">Meta's WhatsApp pricing page</a> for the latest rates. For most small businesses, Meta's charges are small next to the value of the sales a fast reply wins back.</p>

            <h2>WhatsApp Business app vs a chatbot</h2>
            <p>The free WhatsApp Business app is fine for a handful of chats a day, with quick replies and an away message. Once you get many inquiries from ads, or need quotations, follow-ups and more than one person answering, a chatbot on the WhatsApp Business Platform starts to pay for itself.</p>

            <h2>How to keep the cost down</h2>
            <ul>
                <li>Start with the one flow that loses you the most sales, usually first replies and follow-ups</li>
                <li>Keep prices in a sheet you update yourself, so changes don't need a developer</li>
                <li>Answer inside the 24-hour window, where replies to customers cost less</li>
                <li>Add quotations and a dashboard once the basics are working</li>
            </ul>

            <div class="card" style="margin-top:28px;">
                <h3 style="margin-top:0;">Want an exact figure for your business?</h3>
                <p>IMADI Tech gives you a fixed quote after a free 10-minute demo. <a href="{WA_MARIA}" target="_blank" rel="noopener">Message us on WhatsApp</a> or read <a href="/whatsapp-automation/">how the WhatsApp lead system works</a>.</p>
            </div>
''',
    },
]


def blog_post(post):
    path = f"/blog/{post['slug']}/"
    body = f'''
        <article class="wrap page-hero post">
            <div class="eyebrow"><a href="/blog/">Blog</a> · {e(post["date"])}</div>
            <h1>{e(post["title"])}</h1>
            <p class="post-byline">By <a href="/about/">Maria Aziz</a>, founder of IMADI Tech</p>
            <div class="post-body">{post["body"]}</div>
        </article>
'''
    ld = [
        {"@type": "BlogPosting", "@id": SITE_URL + path + "#post", "headline": post["title"], "description": post["description"],
         "datePublished": post["date"], "dateModified": post["date"], "url": SITE_URL + path, "inLanguage": "en",
         "author": {"@id": PERSON_ID}, "publisher": {"@id": ORG_ID}, "isPartOf": {"@id": WEBSITE_ID},
         "mainEntityOfPage": SITE_URL + path},
        breadcrumb([("Home", "/"), ("Blog", "/blog/"), (post["title"], path)]),
    ]
    write(path + "index.html", page(f"{post['title']} | IMADI Tech", post["description"], path, body, ld=ld))
    return path


def blog_index():
    items = "".join(
        f'<a class="card project-card" href="/blog/{p["slug"]}/"><div class="eyebrow">{e(p["date"])}</div>'
        f'<h3>{e(p["title"])}</h3><p>{e(p["description"])}</p><span class="arrow">Read the article →</span></a>'
        for p in sorted(POSTS, key=lambda p: p["date"], reverse=True))
    body = f'''
        <section class="wrap page-hero">
            <div class="eyebrow">IMADI Tech · Blog</div>
            <h1>WhatsApp automation, explained</h1>
            <p>Practical answers for business owners about WhatsApp chatbots, lead follow-up and automation.</p>
        </section>
        <section class="wrap section" style="padding-top:8px;"><div class="grid two">{items}</div></section>
'''
    write("/blog/index.html", page("Blog | IMADI Tech", "Practical articles on WhatsApp chatbots, lead follow-up and business automation from IMADI Tech in Karachi.", "/blog/", body,
                                   ld=[breadcrumb([("Home", "/"), ("Blog", "/blog/")])]))
    return "/blog/"


def build(projects):
    by_slug = {p["slug"]: p for p in projects}
    paths = [industry_page(i, by_slug) for i in INDUSTRIES]
    paths.append(blog_index())
    paths += [blog_post(p) for p in POSTS]
    return paths


def industry_links():
    """Section appended to the main service page, linking each industry page."""
    cards = "".join(
        f'<a class="card project-card" href="/whatsapp-automation/{i["slug"]}/"><h3>{e(i["nav"])}</h3>'
        f'<p>{e(i["description"])}</p><span class="arrow">WhatsApp automation for {e(i["nav"].lower())} →</span></a>'
        for i in INDUSTRIES)
    return f'''
        <section class="wrap section">
            <div class="section-head"><div class="eyebrow">By industry</div><h2>Built for your kind of business</h2></div>
            <div class="grid two">{cards}</div>
        </section>
'''
