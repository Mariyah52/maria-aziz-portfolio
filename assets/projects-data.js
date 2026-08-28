/**
 * Reusable project data for Maria Aziz's portfolio.
 *
 * This is the single source of truth for every project shown on the Home,
 * Work (filtered index), and Case Study pages. To add a new project or
 * update an existing one, edit this file only — every page that lists or
 * links to projects reads from here.
 *
 * Field notes:
 * - `status` must be one of: "Concept", "Prototype", "MVP", "Pilot", "Live",
 *   "Research", or "To be confirmed". Never mark something "Live" unless it
 *   is genuinely deployed and in use — when a project's real status isn't
 *   confirmed, use "To be confirmed" rather than guessing.
 * - Any field that is `null` renders as a clearly-labeled "to be added" /
 *   "to be confirmed" placeholder on the page — it never gets invented text.
 * - `categories` controls which filter pills a project appears under on the
 *   Work page. A project can belong to more than one category.
 */

window.PROJECTS = [
  {
    slug: "hifzai",
    name: "HifzAI",
    tagline: "AI-Powered SaaS",
    categories: ["ai-powered-saas", "ai-automation"],
    featured: true,
    status: "To be confirmed",
    problem: "Structured Quran memorisation support — for students, teachers and parents — is often fragmented across separate tools, notebooks and informal tracking.",
    solution: "An AI-powered learning and Quran memorisation platform designed to support students, teachers and parents through structured learning workflows, progress tracking and intelligent insights.",
    myRole: null,
    technology: null,
    architecture: null,
    innovation: null,
    results: null,
    evidence: []
  },
  {
    slug: "renaz",
    name: "ReNaz",
    tagline: "Conversational Technology & Community Automation",
    categories: ["chatbots", "ai-automation", "social-impact"],
    featured: true,
    status: "MVP",
    problem: "Dry-waste collection in a community setting relies on manual coordination between residents, collectors and administrators, with no shared system to track requests or pickups.",
    challenge: "Coordinating pickups in real time between residents, collectors and administrators is difficult without a shared system — requests, matching, and status all need to stay in sync across everyone involved.",
    solution: "A WhatsApp-first technology solution designed to simplify dry-waste collection workflows and connect residents, collection operations and administrative systems — residents request pickups over WhatsApp, the system matches the nearest available collector, and the full pickup lifecycle is tracked end to end on one operations dashboard.",
    myRole: "Product strategy and project leadership as Founder & CEO of Imadi Technologies, the company building ReNaz.",
    technology: ["WhatsApp Business API"],
    architecture: [
      "WhatsApp",
      "Conversational interface",
      "Backend",
      "Request management",
      "Matching / operations",
      "Admin dashboard"
    ],
    innovation: "Runs entirely over WhatsApp rather than requiring residents to install a separate app, with category-based pricing (PKR per kilogram) and a full pickup lifecycle tracked end to end on one dashboard.",
    results: null,
    evidence: [{ label: "Live product page", href: "https://imadi-technologies.com/products/" }]
  },
  {
    slug: "alico",
    name: "ALICO Business Suite",
    tagline: "AI & Business Automation",
    categories: ["ai-automation"],
    featured: true,
    status: "Live",
    problem: "ALICO Enterprises needed a single system for invoicing, stock, expenses and banking, with role-based access rather than disconnected spreadsheets and manual processes.",
    challenge: "A small business ERP has to stay reliable even with unreliable connectivity, while keeping financial records, stock and access control accurate and auditable.",
    solution: "A web-based ERP — the ALICO Business Suite — covering invoicing, stock, expense tracking and banking in one connected system, with role-based access control and audit logging, built to work offline and sync when back online.",
    myRole: "AI/ML and Automation Consultant, ALICO Enterprises (contract, Jun 2026 – Present) — designed and deployed the ALICO Business Suite.",
    technology: ["Firebase"],
    architecture: null,
    innovation: "Every document lives in one system with admin and viewer roles, stock and ledger that stay in sync, and support for offline use that syncs once back online.",
    results: null,
    evidence: [{ label: "Product overview", href: "https://imadi-technologies.com/products/" }]
  },
  {
    slug: "shah",
    name: "SHAH",
    tagline: "AI & Workflow Automation",
    categories: ["ai-automation"],
    featured: false,
    status: "To be confirmed",
    problem: null,
    solution: null,
    myRole: null,
    technology: null,
    architecture: null,
    innovation: null,
    results: null,
    evidence: []
  },
  {
    slug: "maflow",
    name: "Maflow",
    tagline: "SaaS Platform",
    categories: ["ai-powered-saas"],
    featured: true,
    status: "Live",
    problem: "Teams managing business documents often work across scattered files and tools, with no shared, branded home for company documents and reporting.",
    solution: "A SaaS platform that gives a team one place for every document, with ledger, reports and an audit log — private and branded to the company using it, built for how businesses actually work rather than one person's workflow.",
    myRole: "Product strategy and project leadership as Founder & CEO of Imadi Technologies, the company building Maflow.",
    technology: null,
    architecture: null,
    innovation: "Built for a team rather than a single user, with real help built in rather than a generic ticket queue.",
    results: null,
    evidence: [{ label: "Try the live product", href: "https://imadi-technologies.com/products/" }]
  },
  {
    slug: "imadi-logistics-bot",
    name: "Imadi Logistics Bot",
    tagline: "Chatbots & Conversational Systems",
    categories: ["chatbots"],
    featured: false,
    status: "To be confirmed",
    problem: null,
    solution: null,
    myRole: null,
    technology: null,
    architecture: null,
    innovation: null,
    results: null,
    evidence: []
  },
  {
    slug: "marist-bot",
    name: "Marist Bot",
    tagline: "Chatbots & Conversational Systems",
    categories: ["chatbots"],
    featured: false,
    status: "To be confirmed",
    problem: null,
    solution: null,
    myRole: null,
    technology: null,
    architecture: null,
    innovation: null,
    results: null,
    evidence: []
  },
  {
    slug: "nlp-sentiment-analysis",
    name: "NLP Sentiment Analysis of Travel Blogs",
    tagline: "Machine Learning & NLP · 2024",
    categories: ["ml-nlp", "research"],
    featured: true,
    status: "Research",
    problem: "Understanding how travelers actually express emotion in long-form writing — joy, frustration, nostalgia — is harder than standard positive/negative sentiment scoring, which flattens that nuance.",
    challenge: "Long-form emotional language rarely fits neatly into positive/negative categories, and comparing a transformer model against a sequence model fairly requires careful, consistent evaluation.",
    solution: "An open-source comparison of BERT vs. LSTM models for detecting nuanced emotional sentiment in travel blogs, including full training logs and confusion matrices for both approaches.",
    myRole: "Research design, data preparation, model training and evaluation.",
    technology: ["BERT", "LSTM", "Sentiment Analysis"],
    architecture: null,
    innovation: "Compares a transformer-based approach (BERT) against a sequence-based approach (LSTM) on the same nuanced-emotion task, rather than treating sentiment as simple positive/negative classification.",
    results: null,
    resultsNote: "Full training logs and confusion matrices exist for this project. Specific accuracy, precision, recall and F1 figures will be published here once finalised for public sharing — they are not estimated or published yet.",
    evidence: []
  },
  {
    slug: "ml-pipeline",
    name: "End-to-End Machine Learning Pipeline",
    tagline: "Machine Learning & NLP",
    categories: ["ml-nlp"],
    featured: false,
    status: "To be confirmed",
    problem: null,
    solution: null,
    myRole: null,
    technology: null,
    architecture: [
      "Data ingestion",
      "Data validation",
      "Data transformation",
      "Feature engineering",
      "Model training",
      "Model evaluation",
      "Experiment tracking",
      "Deployment",
      "Monitoring"
    ],
    architectureNote: "This shows the conceptual pipeline stages this project is organised around. The specific tools used at each stage will be added once confirmed.",
    innovation: null,
    results: null,
    evidence: []
  },
  {
    slug: "child-friendly-city-index",
    name: "Child Friendly City Index",
    tagline: "Data & Social Impact Technology",
    categories: ["social-impact"],
    featured: true,
    status: "Prototype",
    problem: "Cities are rarely designed or evaluated from a child's perspective, and there's no simple way to score how child-friendly a given neighbourhood actually is.",
    challenge: "Comparing neighbourhoods fairly requires a real benchmark and sourced data — without that, a scoring tool is just an opinion.",
    solution: "An open-source tool that scores a neighbourhood for children in seconds, benchmarked against the Sweden child-friendly-city model, with around 60 real places pre-scored and concrete, sourced recommendations for improvement.",
    myRole: "Creator — independent project development, from vision deck to working prototype (\"If Children Designed Our Cities: Reimagining Karachi\").",
    technology: ["Python"],
    architecture: null,
    innovation: "Grounded in real coursework and sourced data rather than a generic scoring model, and honest about its own limits rather than overstating what the index can tell you.",
    results: null,
    evidence: []
  },
  {
    slug: "smart-meal-planner",
    name: "Smart Meal Planner",
    tagline: "Intelligent Digital Product",
    categories: ["ai-automation"],
    featured: false,
    status: "To be confirmed",
    problem: null,
    solution: "An AI-based meal planning system with personalised nutrition (known internally as SmartPlan Meals).",
    myRole: "AI Product Developer, self-employed (May 2026 – Present) — developed the product and its automation.",
    technology: null,
    architecture: null,
    innovation: null,
    results: null,
    evidence: []
  }
];

/** Lookup helpers shared by the Work and Case Study pages. */
window.getProjectBySlug = function (slug) {
  return window.PROJECTS.find((p) => p.slug === slug) || null;
};

window.CATEGORY_LABELS = {
  "featured": "Featured",
  "ai-automation": "AI & Automation",
  "chatbots": "Chatbots & Conversational Systems",
  "ai-powered-saas": "SaaS",
  "ml-nlp": "Machine Learning & NLP",
  "social-impact": "Digital & Social Impact",
  "research": "Research"
};
