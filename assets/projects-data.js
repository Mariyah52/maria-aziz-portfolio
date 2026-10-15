/**
 * Project data for Maria Aziz's portfolio: single source of truth for the
 * Home featured grid, the Work page and every case study.
 *
 * Fields: slug, name, tagline, client, period, categories[], featured,
 * status, problem, challenge, solution, features[], myRole, technology[],
 * architecture[], innovation, results[], evidence[{label, href}].
 * Any field left null/empty is simply hidden on the page.
 *
 * status values used: "Live", "Pilot", "In build", "Launching Oct 2026",
 * "Prototype", "Research", "Academic". Only mark "Live" when genuinely in use.
 */

window.PROJECTS = [
  // ------------------------------------------------------ CLIENT WORK --
  {
    slug: "alico",
    name: "ALICO Business Suite",
    tagline: "Client Work · Business Automation",
    client: "ALICO Enterprises, general order supplier · Karachi, Pakistan",
    period: "May 2026 – Present",
    categories: ["client", "ai-automation"],
    featured: true,
    status: "Live",
    problem: "A Karachi general order supplier was running quotations, delivery challans, tax invoices, stock and payments across paper and spreadsheets, with no single record and no way to keep working when the internet dropped.",
    challenge: "Requirements came directly from the business owner in Roman Urdu, and the system had to follow Pakistani business practice (PKR, NTN/STRN, GST) while staying reliable offline.",
    solution: "A complete business management system for ALICO Enterprises covering the full sales and purchase cycle (quote, challan, invoice, payment), with stock, ledgers and bank accounts in one installable app that works offline and syncs in real time across devices.",
    features: [
      "Quotations: create and send professional quotes",
      "Delivery Challans: description, unit and quantity only, no pricing",
      "Sales Tax Invoices with configurable GST (0–20%)",
      "Commercial Bills",
      "Purchase Orders with supplier management and GRN",
      "Parties: customer and supplier directory with NTN/STRN",
      "Products & Stock with low-stock alerts",
      "Payments received and paid out",
      "Expense tracking",
      "Customer Ledger with full account statements",
      "Multiple bank accounts",
      "Reports: sales, receivables and stock",
      "Audit Log: every action tracked with a timestamp",
      "Role-based access: Admin and Viewer",
      "Backup & Restore (JSON export/import)",
      "WhatsApp sharing of documents",
      "Digital or physical stamp and signature on print-ready documents"
    ],
    myRole: "Founder & AI Specialist. Gathered requirements from the owner in Roman Urdu, then designed, built and deployed the system using an LLM-assisted development workflow.",
    technology: ["HTML5", "CSS3", "JavaScript (PWA)", "Firebase Firestore", "Firebase Authentication", "IndexedDB", "LocalStorage", "Netlify"],
    architecture: ["Installable PWA (iOS & Android)", "IndexedDB offline store", "Firebase Authentication", "Firestore real-time sync", "Print-ready documents", "Netlify hosting"],
    innovation: "Offline-first architecture that keeps working without internet and syncs automatically, custom AL-XXXX-YY document numbering, and a development process that turned Roman Urdu business requirements into production software with AI assistance.",
    results: [
      "Live and in daily use by ALICO Enterprises since May 2026",
      "Became the foundation for a second client deployment (SHAH Enterprise)"
    ],
    evidence: []
  },
  {
    slug: "uk-logistics-erp",
    name: "ERP & Accounting Platform",
    tagline: "Client Work · Enterprise ERP",
    client: "IMADI Fulfilment & Logistics · United Kingdom",
    period: "Jun 2026 – Present",
    categories: ["client", "ai-automation"],
    featured: true,
    status: "Live",
    problem: "A UK logistics business was managing accounts, VAT, stock, deliveries and its fleet across separate tools, with no single source of truth for its finances.",
    challenge: "Accounting software has to be exact: every transaction must stay balanced, closed periods must stay locked, and VAT figures must always be derived from the underlying transactions.",
    solution: "One integrated platform where posting an invoice automatically reduces stock and writes a balanced journal entry, supplier bills post to the ledger on approval, and every report reads live from the same accounting engine.",
    features: [
      "13 integrated modules: authentication, customers, suppliers, inventory, invoicing, purchasing, banking, accounting, UK VAT, logistics, reports, AI assistant and security",
      "Double-entry accounting engine: chart of accounts, journals, trial balance, P&L, balance sheet, cash flow",
      "Financial-year closing with period locks, and recurring journals",
      "Bank reconciliation with CSV statement import and auto-matching",
      "UK VAT reporting on HMRC's 9-box return structure, with VAT-number check-digit validation",
      "Inventory by warehouse and batch, with QR codes and stock transfers",
      "Purchase order and bill approval workflows with goods receipt",
      "Logistics: shipments, proof of delivery, drivers, vehicles, fuel and a public customer tracking portal",
      "Every report exportable to PDF and Excel",
      "AI assistant: invoice and receipt OCR, duplicate-invoice detection, expense categorisation, cash-flow forecast and financial Q&A",
      "Security: 2FA, argon2 password hashing, role permissions, field-level encryption, CSRF protection, rate limiting, audit logs, backup and restore"
    ],
    myRole: "Founder & AI Specialist. Led the architecture, module design and delivery.",
    technology: ["Python", "FastAPI", "PostgreSQL", "SQLAlchemy", "Alembic", "Pydantic", "Tesseract OCR", "ReportLab", "JWT / TOTP 2FA"],
    architecture: ["API routers", "Services (business logic)", "Repositories (data access)", "PostgreSQL", "Shared accounting engine", "Reports & PDF/Excel export"],
    innovation: "A single shared accounting engine enforces double entry and period locks for every module, so no part of the system can post an unbalanced or back-dated entry.",
    results: [
      "Live and in daily use since June 2026",
      "13 modules and 60 database tables, verified by 358 end-to-end tests against a real PostgreSQL database",
      "The client customised it for their operations and returned to commission a WhatsApp automation platform"
    ],
    evidence: []
  },
  {
    slug: "shah",
    name: "SHAH Enterprise Business Suite",
    tagline: "Client Work · Business Automation",
    client: "SHAH Enterprise, petrochemicals, solvents & commodity goods · Karachi, Pakistan",
    period: "Jul 2026 – Present",
    categories: ["client", "ai-automation"],
    featured: false,
    status: "Live",
    problem: "A petrochemical and solvents trader needed the same control over quotes, deliveries, tax invoices and stock, under its own branding and document series.",
    solution: "A dedicated business suite built on the ALICO platform, extended with linked document conversion, automatic stock updates and a guided self-service cloud setup.",
    features: [
      "Convert a quotation or challan into an invoice, sales tax invoice or commercial bill",
      "Automatic stock deduction from sales and restocking from GRNs",
      "Duplicate-safe SE-XXXX-YY numbering that stays correct across devices after sync",
      "Guided Firebase setup wizard and an offline demo mode",
      "Weekly, monthly and yearly sales, receivables and low-stock reports",
      "Customer ledger, bank accounts, expenses, audit log and role-based access"
    ],
    myRole: "Founder & AI Specialist. Adapted and extended the platform for the client and deployed it.",
    technology: ["JavaScript (PWA)", "Firebase Firestore", "Firebase Authentication", "IndexedDB"],
    architecture: null,
    innovation: "Shows the platform is reusable: a second business was onboarded by adapting the product rather than rebuilding it.",
    results: ["Live and in daily use since July 2026"],
    letter: {
      quote: "We appreciate Ms. Maria Aziz's professional services and technical contribution in developing this customized business solution for our organization.",
      name: "Haseeb",
      role: "Owner, SHAH Enterprise",
      date: "3 September 2026",
      image: "/assets/media/shah-letter.jpg"
    },
    evidence: []
  },
  {
    slug: "renaz",
    name: "ReNaz: WhatsApp Scrap Collection Platform",
    tagline: "Client Work · Conversational Systems",
    client: "Scrap collection business · Pakistan",
    period: "Aug 2026 – Present",
    categories: ["client", "chatbots", "social-impact"],
    featured: true,
    status: "Live",
    problem: "Scrap and dry-waste collection relied on informal, manual coordination between customers and collectors, with nothing tracking requests, pricing or pickups.",
    challenge: "Two very different users, customers and collectors, needed to be served through the app they already use, with every pickup kept in sync for the operations team.",
    solution: "Customers book pickups by chatting on WhatsApp, choosing a waste category, date and timeslot with per-kg pricing in PKR. Collectors receive and complete jobs on WhatsApp, and administrators see every pickup from request to completion on one dashboard.",
    features: [
      "Customer WhatsApp flow: category selection, custom categories, date and timeslot booking, cancellation",
      "Collector WhatsApp flow: job reference numbers and completion reporting",
      "Category-based pricing in PKR per kg",
      "React admin dashboard tracking the full pickup lifecycle"
    ],
    myRole: "Founder & AI Specialist. Designed the conversation flows and architecture, built the platform and launched it for the client.",
    technology: ["Python", "FastAPI", "React", "TypeScript", "WhatsApp Business API", "Render"],
    architecture: ["Customer WhatsApp flow", "Collector WhatsApp flow", "FastAPI backend", "Database", "Admin REST API", "React dashboard"],
    innovation: "Runs entirely on WhatsApp, with no app to install, serving two user types through separate flows on one system.",
    results: [
      "Live since August 2026",
      "23+ pickups completed through WhatsApp",
      "1–2 new pickup requests daily",
      "Positive feedback from the business owner, who is now expanding to commercial bulk scrap"
    ],
    evidence: []
  },
  {
    slug: "uk-logistics-whatsapp",
    name: "WhatsApp Automation & Operations Platform",
    tagline: "Client Work · Conversational Systems",
    client: "IMADI Fulfilment & Logistics · United Kingdom (returning client)",
    period: "Sep 2026 – Present",
    categories: ["client", "chatbots", "ai-automation"],
    featured: true,
    status: "Live",
    problem: "Rate quotes, order enquiries and damage claims were handled manually, so claims were hard to track and customers waited for quotes.",
    solution: "A WhatsApp-first system on Meta's Cloud API. Customers get instant pallet-rate quotes and place order enquiries; registered corporate clients file damage claims step by step with photos and invoices, and administrators review and approve them from one dashboard.",
    features: [
      "Intent routing that recognises registered corporate senders",
      "Instant pallet-rate quotes pulled live from a Google Sheets rate card",
      "Order enquiry capture",
      "Multi-step claims flow: shipment details, labelled photo evidence and proof-of-cost invoices",
      "Claims approval workflow with automatic WhatsApp notifications",
      "Operations dashboard: orders, claims review, evidence, company administration and role-based admin access"
    ],
    myRole: "Founder & AI Specialist. Designed the conversation flows and architecture and built the bot and dashboard.",
    technology: ["Python", "Flask", "PostgreSQL", "Meta WhatsApp Cloud API", "Google Sheets API"],
    architecture: ["WhatsApp", "Cloud API webhook", "Intent router (rate / order / claim)", "Flask backend + PostgreSQL", "Google Sheets rate card", "Admin dashboard", "WhatsApp notifications"],
    innovation: "One WhatsApp number serves two audiences: it recognises registered companies automatically, and every claim runs from first message to final decision with its evidence attached. Built for reliability with persistent conversation state, idempotent webhook processing, secure media handling and audit logging.",
    results: [
      "Live since September 2026",
      "Commissioned by the same client after adopting the ERP & Accounting Platform"
    ],
    evidence: []
  },
  {
    slug: "company-monitor",
    name: "Company Monitor",
    tagline: "Client Work · Conversational Systems",
    client: "Multi-branch business · Nairobi, Kenya",
    period: "Sep 2026 – Present",
    categories: ["client", "chatbots"],
    featured: false,
    status: "In build",
    problem: "A multi-branch business had no visibility of customer enquiries reaching branch WhatsApp numbers, so leads could be missed or diverted.",
    solution: "A central platform where company-authorised WhatsApp Business numbers feed one secure inbox, visible by branch and by role.",
    features: [
      "Authorised Cloud API number setup, fixed to one company and branch",
      "HMAC-SHA256 signed webhooks and encrypted access-token storage",
      "Durable PostgreSQL inbox with a separate background worker",
      "Message deduplication, restart-safe processing and quarantine of malformed deliveries",
      "Management sees all company accounts; branch staff see only their assigned branches",
      "Disconnect erases access and hides stored messages until re-authorisation"
    ],
    myRole: "Founder & AI Specialist. Architecture and build.",
    technology: ["Python", "FastAPI", "PostgreSQL", "React", "TypeScript", "Meta WhatsApp Cloud API"],
    architecture: null,
    innovation: "Consent and security built in from the start: numbers connect only with explicit company authorisation, and disconnecting erases access.",
    results: ["Phase 4 (Cloud API receiver) complete; QR-login pilot in testing"],
    evidence: []
  },

  // ---------------------------------------------- PRODUCTS & VENTURES --
  {
    slug: "hercommerce",
    name: "HerCommerce",
    tagline: "Product · SaaS · Women Entrepreneurs",
    client: "Own product",
    period: null,
    categories: ["saas", "social-impact"],
    featured: true,
    status: "Live",
    problem: "Many women entrepreneurs already sell through WhatsApp, but setting up an online store usually needs technical skills and a monthly bill they can't justify.",
    challenge: "The platform had to be simple enough for anyone who can use WhatsApp, and cost nothing to run, with no paid servers and no credit card anywhere in the setup.",
    solution: "A mobile-first, multi-tenant SaaS platform where a woman can create and run an online business: a guided 4-step onboarding, her own storefront, products with variants, WhatsApp ordering, order management, vouchers and gift cards.",
    features: [
      "Multi-tenant accounts with seller onboarding in 4 steps",
      "Store builder: business profile, storefront, products, categories and variants",
      "Cart and WhatsApp ordering with pre-filled order messages",
      "Real-time order management and Mark as Sold / Reactivate",
      "Customer CRM, vouchers and gift cards",
      "Platform admin dashboard: seller management, categories and analytics"
    ],
    myRole: "Founder. Led product and AI.",
    technology: ["React", "TypeScript", "Firebase Firestore", "Firebase Authentication", "Firebase Hosting", "Cloudinary"],
    architecture: ["Mobile-first React app", "Firebase Authentication", "Firestore (multi-tenant)", "Security Rules validation", "Cloudinary images", "WhatsApp order links"],
    innovation: "No backend server at all: every write, including a customer placing an order without an account, goes straight to Firestore inside a transaction and is validated by Security Rules, so the platform runs at zero cost.",
    results: ["Live with 18 active subscriptions", "All 6 build phases complete: foundation, store builder, selling, customer tools, platform admin"],
    evidence: [{ label: "Open HerCommerce", href: "https://hercommerce-299ba.web.app/" }]
  },
  {
    slug: "marist-bot",
    name: "Marist",
    tagline: "Hobby · Conversational AI",
    client: "Hobby project",
    period: null,
    categories: ["chatbots"],
    featured: false,
    status: "Live",
    hobby: "A WhatsApp chat buddy I built for fun. It chats in Roman Urdu and shares a little motivation whenever someone needs it.",
    problem: "Sometimes people just need a kind, upbeat word at the end of a long day.",
    solution: "Marist is a friendly WhatsApp chat buddy I built in my free time. It chats in Roman Urdu, keeps the conversation positive and shares a little motivation. Say hi on WhatsApp: 0342 1393991.",
    myRole: "Built it end to end in my free time.",
    technology: ["Python", "Flask", "WhatsApp Cloud API", "Claude API"],
    architecture: null,
    innovation: null,
    results: ["Live on WhatsApp: 0342 1393991"],
    evidence: [{ label: "Say hi to Marist on WhatsApp", href: "https://wa.me/923421393991?text=Hi%20Marist!" }]
  },
  {
    slug: "child-friendly-city-index",
    name: "Child-Friendly City Index",
    tagline: "Open Source · Data & Social Impact",
    client: "Open-source contribution · free for anyone to use",
    period: "May 2026",
    categories: ["social-impact"],
    featured: false,
    status: "Live",
    problem: "Cities are rarely designed or evaluated from a child's perspective, and there is no simple way to score how child-friendly a neighbourhood is.",
    challenge: "Comparing neighbourhoods fairly needs a real benchmark and sourced data; without that, a scoring tool is just an opinion.",
    solution: "A conversational bot for parents: ask which places are child-friendly (for example, for Asian children in New Zealand) and it gathers data on each area and scores it against the Swedish child-friendly-city model. 1,683 cities and districts, organised country → city → neighbourhood → postal code.",
    myRole: "Creator: from the vision deck (\"If Children Designed Our Cities: Reimagining Karachi\") to the working tool.",
    technology: ["React", "TypeScript", "Node.js / Express", "OpenAI API", "Python (data preparation)"],
    architecture: null,
    innovation: "Grounded in sourced data and a published benchmark, and open about the limits of what the index can tell you.",
    results: ["Live and publicly accessible since May 2026", "Open source: anyone can use it, adapt it or build on it"],
    evidence: [{ label: "Open the live tool", href: "https://child-friendly-city-index-v2.netlify.app/" }, { label: "View source code on GitHub", href: "https://github.com/Mariyah52/child-friendly-city-index-v2" }]
  },
  {
    slug: "smart-meal-planner",
    name: "Smart Meal Planner",
    tagline: "Hobby · AI Application",
    client: "Hobby project",
    period: null,
    categories: ["ai-automation"],
    featured: false,
    status: "Prototype",
    hobby: "An AI app I'm playing with that suggests meal plans based on each person's nutrition needs.",
    problem: "Planning healthy meals that suit each person's nutrition needs takes time.",
    solution: "An AI-based meal planning app with personalised nutrition and meal recommendations.",
    myRole: "Built it in my free time.",
    technology: null,
    architecture: null,
    innovation: null,
    results: null,
    evidence: []
  },
  {
    slug: "overthinking-journal",
    name: "Overthinking Journal for Women",
    tagline: "Hobby · Writing & Digital Product",
    client: "Hobby project · Amazon",
    period: null,
    categories: ["social-impact"],
    featured: false,
    status: "In progress",
    hobby: "A guided journal for women aged 25–40 who overthink. It's on Amazon as a paperback, and I'm now designing a digital version.",
    problem: "Many women aged 25–40 get stuck in loops of overthinking and have no simple, guided way to reset.",
    solution: "\"Overthinking Journal for Women 25–40: A Guided Emotional Reset System\", a guided journal with prompts and exercises, published as a paperback on Amazon under the name Mariyah Aziz. I'm now designing a digital version for Amazon.",
    myRole: "Author and designer.",
    technology: null,
    architecture: null,
    innovation: null,
    results: ["Paperback published on Amazon KDP (as Mariyah Aziz)", "Digital version in design"],
    evidence: []
  },

  // --------------------------------------------------------- AI / ML --
  {
    slug: "ml-pipeline",
    name: "End-to-End Machine Learning Pipeline",
    tagline: "Hobby · Machine Learning",
    client: "Hobby project · started during my IBA AI course",
    period: "May 2026",
    categories: ["ml-nlp"],
    featured: false,
    status: "Hobby",
    hobby: "A practice project from my AI course: I cleaned a dataset, then trained and compared 21 models to find the most accurate one.",
    problem: "Choosing a reliable classifier means comparing many models fairly on data that hasn't been seen during training.",
    solution: "A four-notebook pipeline covering data cleaning, a 3-way train/validation/test split, and training 21 Decision Tree and SVM models with hyperparameter tuning, evaluated on accuracy, sensitivity and specificity to select the top performers.",
    myRole: "Data preparation, modelling and evaluation.",
    technology: ["Python", "scikit-learn", "Pandas", "NumPy", "Jupyter"],
    architecture: ["Data cleaning", "3-way split", "Model training (21 models)", "Hyperparameter tuning", "Evaluation", "Model selection"],
    innovation: null,
    results: null,
    evidence: []
  },
  {
    slug: "nlp-sentiment-analysis",
    name: "NLP Sentiment Analysis of Travel Blogs",
    tagline: "Hobby · NLP",
    client: "Hobby project",
    period: null,
    categories: ["ml-nlp"],
    featured: false,
    status: "Hobby",
    hobby: "Out of curiosity about travel writing, I compared BERT and LSTM models to spot emotions like joy, frustration and nostalgia in travel blogs.",
    problem: "Travellers express emotions like joy, frustration and nostalgia in long-form writing, which standard positive/negative sentiment scoring flattens.",
    challenge: "Comparing a transformer model against a sequence model fairly requires careful, consistent evaluation.",
    solution: "A comparison of BERT and LSTM models for detecting nuanced emotional sentiment in travel blogs, with full training logs and confusion matrices for both.",
    myRole: "Research design, data preparation, model training and evaluation.",
    technology: ["Python", "BERT", "LSTM"],
    architecture: null,
    innovation: "Treats sentiment as nuanced emotion rather than simple positive/negative classification.",
    results: null,
    evidence: []
  }
];

/* Plain-language "problem in one line, solution in two" used on cards, the home page and the top of each case study. */
window.PLAIN = {
  "alico": {
    "problem": "Staff spent about 2 hours every day in Excel making quotations, invoices and bills, and tracking stock, payments and customer accounts.",
    "solution": "I built one app that does all of this, works even without internet and shares print-ready documents on WhatsApp. The same daily work now takes about 20 minutes."
  },
  "uk-logistics-erp": {
    "problem": "The company did its accounting by hand and, when moving to software, wanted a system built around the way it works.",
    "solution": "I built a custom accounting system with the features they asked for: credit notes, UK VAT and emailing invoices straight from the software, plus automatic invoice reading and delivery tracking."
  },
  "shah": {
    "problem": "A second trading business needed the same control over quotes, deliveries, invoices and stock, under its own name.",
    "solution": "I adapted the ALICO system for them, adding one-click conversion from quotation to invoice and automatic stock updates."
  },
  "renaz": {
    "problem": "The client needed data on how much scrap comes from across Karachi, an easy way to collect it, and verified collectors who can enter gated communities.",
    "solution": "Customers and collectors do everything through a WhatsApp conversation, and the data reaches a dashboard automatically. Collectors register with their CNIC. 23+ pickups completed."
  },
  "uk-logistics-whatsapp": {
    "problem": "As a B2B company, staff had to sort through emails to find and handle damage claims.",
    "solution": "A WhatsApp bot now runs the whole claims process, and staff raise, approve or reject claims from one dashboard. It saves time and keeps all data in sync."
  },
  "company-monitor": {
    "problem": "Salesmen were taking leads from WhatsApp, delivering goods from outside the company and keeping the commission.",
    "solution": "Each branch scans a QR code to connect its WhatsApp to a dashboard, so management sees every lead and conversation for every branch and salesman."
  },
  "hercommerce": {
    "problem": "Women who sell on WhatsApp often cannot set up or afford an online store.",
    "solution": "HerCommerce lets them open their own shop and take orders on WhatsApp, at no running cost. 18 active subscriptions."
  },
  "marist-bot": {
    "problem": "Sometimes people just need a kind, upbeat word at the end of a long day.",
    "solution": "Marist is a friendly WhatsApp chat buddy I built for fun. It chats in Roman Urdu and shares a little motivation."
  },
  "child-friendly-city-index": {
    "problem": "Parents have no simple way to know which neighbourhoods are good for children.",
    "solution": "Ask the bot about any area and it scores how child-friendly it is. 1,683 cities and districts. Open source: anyone can use it for free."
  },
  "overthinking-journal": {
    "problem": "Many women aged 25–40 get stuck in loops of overthinking and have no simple, guided way to reset.",
    "solution": "A guided journal with prompts and exercises, on Amazon as a paperback. A digital version is in design."
  },
  "smart-meal-planner": {
    "problem": "Planning healthy meals that suit each person's nutrition needs takes time.",
    "solution": "An AI app that suggests meal plans based on personal nutrition needs."
  },
  "ml-pipeline": {
    "problem": "Picking the right prediction model means comparing many models fairly.",
    "solution": "I built a 4-step pipeline that cleaned the data and tested 21 models to find the most accurate one."
  },
  "nlp-sentiment-analysis": {
    "problem": "Simple positive/negative scoring misses the real emotions in travel writing.",
    "solution": "I compared two AI models (BERT and LSTM) to detect emotions like joy, frustration and nostalgia in travel blogs."
  }
};
(window.PROJECTS || []).forEach(function (p) { var x = window.PLAIN[p.slug]; if (x) { p.plainProblem = x.problem; p.plainSolution = x.solution; } });

window.getProjectBySlug = function (slug) {
  return window.PROJECTS.find(function (p) { return p.slug === slug; }) || null;
};

window.CATEGORY_LABELS = {
  "featured": "Featured",
  "client": "Client Work",
  "saas": "Products & SaaS",
  "chatbots": "Conversational Systems",
  "ai-automation": "AI & Automation",
  "ml-nlp": "Machine Learning & NLP",
  "social-impact": "Social Impact"
};
