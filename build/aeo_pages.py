#!/usr/bin/env python3
"""Answer-engine pages for imadi.tech, built by pages.py.

These pages are written for the way Google answer boxes, voice search and AI
assistants (ChatGPT, Perplexity, Claude) quote a source: a question as the
heading, then a direct, self-contained answer of roughly 40-60 words as the
very first sentence, with no build-up before it.

Facts follow the same rule as the rest of the site: industry facts that can be
checked against Meta's own documentation, and claims about IMADI Tech only
where they are already true elsewhere on the site. No invented numbers.
"""
import html

from generate import page, write, SITE_URL, ORG_ID, PERSON_ID
from seo_pages import WA_MARIA, breadcrumb

e = html.escape

GLOSSARY_PATH = "/what-is-whatsapp-automation/"

# (term, question, answer). The answer must stand on its own when quoted
# without the question or the rest of the page.
TERMS = [
    ("WhatsApp automation",
     "What is WhatsApp automation?",
     "WhatsApp automation is software connected to a business's WhatsApp number that handles messages without a person typing each reply. It answers common questions, collects what a customer needs, sends quotations and follows up with people who go quiet, and passes the conversation to a salesperson when it matters."),
    ("WhatsApp chatbot",
     "What is a WhatsApp chatbot?",
     "A WhatsApp chatbot is an assistant that replies inside WhatsApp on a business's own number. It recognises what the customer is asking, answers from the business's own products, prices and policies, and keeps the conversation moving at any hour, including nights and weekends when nobody is at the shop."),
    ("WhatsApp Business Platform",
     "What is the WhatsApp Business Platform?",
     "The WhatsApp Business Platform is Meta's official way to connect software to a business WhatsApp number, through what Meta calls the Cloud API. It is what makes automation, dashboards and multiple agents possible, and it is separate from the free WhatsApp Business app a shop installs on a phone."),
    ("WhatsApp Business app",
     "What is the difference between the WhatsApp Business app and a WhatsApp chatbot?",
     "The free WhatsApp Business app gives a business profile, a greeting message and saved replies, all typed and sent by a person. A chatbot on the WhatsApp Business Platform replies on its own, qualifies leads, sends quotations, follows up automatically and records every lead in one dashboard."),
    ("Message template",
     "What is a WhatsApp message template?",
     "A message template is wording a business registers with Meta in advance so it can start a conversation with a customer, rather than only replying to one. Templates are used for things like quotation follow-ups and order updates, and Meta reviews each one before it can be sent."),
    ("Lead qualification",
     "What is lead qualification in a WhatsApp chatbot?",
     "Lead qualification is the set of questions the assistant asks before a salesperson gets involved: what the customer wants, in what size or quantity, for when, and where. It means your team opens a conversation that already has the details in it, instead of starting from a bare enquiry."),
    ("Automated follow-up",
     "What is an automated follow-up?",
     "An automated follow-up is a message sent on a schedule to a customer who asked about something and then went quiet. It goes out a day or a few days later without anyone remembering to send it, and stops as soon as the customer replies, so nobody is chased after they answer."),
    ("Lead dashboard",
     "What is a lead dashboard?",
     "A lead dashboard is one screen showing every enquiry a business received, where it came from, what stage it is at and who is handling it. Without one, leads live inside chats on individual phones, so an owner cannot see how many arrived or how many turned into orders."),
    ("Human handover",
     "What is handover in a WhatsApp chatbot?",
     "Handover is the moment the assistant stops replying and a person takes over the chat. A well-built assistant hands over as soon as the customer asks for a human, starts negotiating, or raises something unusual, so automation handles the repetitive part and your team handles the sale."),
    ("Per-message pricing",
     "How does Meta charge for WhatsApp Business Platform messages?",
     "Meta charges per delivered message. It moved from conversation-based pricing to per-message pricing on 1 July 2025, and the rate depends on the message category and the country the customer is in. Meta bills a business directly for these charges, separately from what a developer charges to build the system."),
]


def glossary_body():
    blocks = "".join(f'''
            <article class="card" id="{e(t.lower().replace(' ', '-'))}" style="margin-bottom:18px;">
                <h2 style="margin-top:0;">{e(q)}</h2>
                <p style="margin-bottom:0;">{e(a)}</p>
            </article>''' for t, q, a in TERMS)
    return f'''
        <section class="wrap page-hero">
            <div class="eyebrow">IMADI Tech · Plain-language guide</div>
            <h1>WhatsApp automation explained, in plain language</h1>
            <p>WhatsApp automation is software connected to a business's WhatsApp number that replies to every enquiry on its own, qualifies the lead, sends quotations and follows up with customers who go quiet. This page defines each term a business owner meets when setting one up.</p>
            <div class="hero-actions" style="margin-top:22px;">
                <a class="btn primary" href="{WA_MARIA}" target="_blank" rel="noopener" data-track="glossary_whatsapp">Book a free 10-minute demo on WhatsApp</a>
                <a class="btn" href="/whatsapp-automation/">See how the system works</a>
            </div>
        </section>

        <section class="wrap section" style="padding-top:8px;">
            {blocks}
        </section>

        <section class="wrap section">
            <div class="card feature center" style="padding:40px;text-align:center;">
                <h2>Still deciding whether you need one?</h2>
                <p style="max-width:540px;margin:0 auto 22px;">Read <a href="/blog/whatsapp-business-app-vs-chatbot/">WhatsApp Business app or a WhatsApp chatbot</a>, or see the <a href="/faq/">full FAQ</a>.</p>
                <a class="btn primary" href="{WA_MARIA}" target="_blank" rel="noopener">Ask Maria on WhatsApp</a>
            </div>
        </section>
'''


GLOSSARY_LD = [
    {"@type": "DefinedTermSet", "@id": SITE_URL + GLOSSARY_PATH + "#terms",
     "name": "WhatsApp automation terms",
     "description": "Plain-language definitions of the terms a business owner meets when setting up WhatsApp automation.",
     "publisher": {"@id": ORG_ID},
     "hasDefinedTerm": [
         {"@type": "DefinedTerm", "@id": SITE_URL + GLOSSARY_PATH + "#" + t.lower().replace(" ", "-"),
          "name": t, "description": a, "inDefinedTermSet": {"@id": SITE_URL + GLOSSARY_PATH + "#terms"}}
         for t, q, a in TERMS]},
    {"@type": "FAQPage", "@id": SITE_URL + GLOSSARY_PATH + "#faq",
     "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                    for t, q, a in TERMS]},
    {"@type": "WebPage", "@id": SITE_URL + GLOSSARY_PATH + "#webpage",
     "url": SITE_URL + GLOSSARY_PATH, "name": "WhatsApp automation explained",
     "about": {"@id": ORG_ID}, "author": {"@id": PERSON_ID}, "inLanguage": "en"},
    breadcrumb([("Home", "/"), ("WhatsApp Automation", "/whatsapp-automation/"),
                ("What is WhatsApp automation?", GLOSSARY_PATH)]),
]


# FAQ shown on the main WhatsApp automation service page. Kept distinct from
# the site-wide FAQ so the two pages do not answer the same questions.
SERVICE_FAQ = [
    ("What does a WhatsApp lead system actually do?",
     "It replies to every enquiry on your WhatsApp number within seconds, asks the questions a salesperson would ask, shares your designs and price ranges, sends quotations, follows up with customers who go quiet, and lists every lead in one dashboard with its status."),
    ("Do I need a new WhatsApp number?",
     "Usually not. Before setup, IMADI Tech checks whether your existing business number can move to the WhatsApp Business Platform or whether a second number suits you better, so you know exactly what happens to your current chats before anything changes."),
    ("What do you need from me to set it up?",
     "Your product or service list, your prices or price ranges, the questions customers ask most often, and access to your WhatsApp Business number. The conversation is then written around your business and shown to you before it goes live."),
    ("How long does it take before it is answering customers?",
     "Setup is usually a matter of days rather than months, depending on how many products and flows are involved and how quickly your price list and answers are ready. You get a timeline in writing before work starts."),
    ("What does it cost?",
     "A one-time setup fee plus a monthly fee for hosting and support, quoted as a fixed figure after a free 10-minute demo. Meta's own per-message charges are billed by Meta directly to your business, separately from what IMADI Tech charges."),
]


def service_faq_section():
    """Visible FAQ appended to /whatsapp-automation/."""
    items = "".join(f'''
                <details class="faq-item"{' open' if i == 0 else ''}>
                    <summary><h3 class="faq-q">{e(q)}</h3></summary>
                    <p>{e(a)}</p>
                </details>''' for i, (q, a) in enumerate(SERVICE_FAQ))
    return f'''
        <section class="wrap section" id="faq">
            <div class="section-head"><div class="eyebrow">FAQ</div><h2>Common questions about WhatsApp automation</h2></div>
            <div class="faq-list">{items}
            </div>
            <p style="margin-top:16px;">New to the terms? Read <a href="{GLOSSARY_PATH}">WhatsApp automation explained</a>, or see the <a href="/faq/">full FAQ</a>.</p>
        </section>
'''


SERVICE_FAQ_LD = {
    "@type": "FAQPage", "@id": SITE_URL + "/whatsapp-automation/#faq",
    "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                   for q, a in SERVICE_FAQ]}


def build():
    write(GLOSSARY_PATH + "index.html", page(
        "What Is WhatsApp Automation? A Plain Guide | IMADI Tech",
        "What WhatsApp automation, chatbots, the WhatsApp Business Platform, message templates and automated follow-ups actually mean, in plain language.",
        GLOSSARY_PATH, glossary_body(), ld=GLOSSARY_LD))
    return [GLOSSARY_PATH]
