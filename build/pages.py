#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate import page, write

# ---------------------------------------------------------------- HOME -----
home_body = """
        <section class="wrap hero-grid reveal">
            <div>
                <div class="eyebrow">Maria Aziz</div>
                <h1 style="font:700 clamp(2.4rem,5.6vw,4.2rem)/1.05 var(--display);letter-spacing:-.03em;margin:8px 0 20px;">AI Product Founder<br>&amp; Technology Entrepreneur</h1>
                <p style="color:var(--muted);font-size:1.12rem;max-width:560px;margin:0 0 18px;">Building AI-powered products, intelligent automation, conversational systems and scalable SaaS solutions for real-world problems.</p>
                <p style="color:#cdd9ec;max-width:580px;margin:0 0 30px;">My work begins with understanding the problem. I analyse workflows, users and operational challenges, then design practical technology solutions that can be built, tested and improved.</p>
                <div style="display:flex;flex-wrap:wrap;gap:12px;">
                    <a class="btn primary" href="/work/">Explore My Work</a>
                    <a class="btn" href="/contact/">Tell Me Your Problem</a>
                </div>
            </div>
            <div class="card reveal" style="padding:32px;">
                <div class="eyebrow">How the work moves</div>
                <div class="timeline-numbered" style="margin-top:8px;">
                    <div class="step"><div class="num">1</div><div><h3 style="margin:0;font-size:.95rem;">Problem</h3></div></div>
                    <div class="step"><div class="num">2</div><div><h3 style="margin:0;font-size:.95rem;">Research</h3></div></div>
                    <div class="step"><div class="num">3</div><div><h3 style="margin:0;font-size:.95rem;">Solution design</h3></div></div>
                    <div class="step"><div class="num">4</div><div><h3 style="margin:0;font-size:.95rem;">Technology &amp; build</h3></div></div>
                    <div class="step"><div class="num">5</div><div><h3 style="margin:0;font-size:.95rem;">Automation</h3></div></div>
                    <div class="step"><div class="num">6</div><div><h3 style="margin:0;font-size:.95rem;">Measurable impact</h3></div></div>
                </div>
            </div>
        </section>


        <section class="wrap section reveal" style="padding-top:0;">
            <div class="stat-band">
                <div class="stat"><span class="stat-num">6</span><span class="stat-label">Client platforms built</span></div>
                <div class="stat"><span class="stat-num">5</span><span class="stat-label">Live in daily use</span></div>
                <div class="stat"><span class="stat-num">3</span><span class="stat-label">Countries: Pakistan, UK, Kenya</span></div>
                <div class="stat"><span class="stat-num">358</span><span class="stat-label">Automated tests on one ERP</span></div>
            </div>
        </section>

        <section class="wrap section reveal">
            <div class="section-head">
                <div class="eyebrow">What I do</div>
                <h2>From Problems to Technology Solutions</h2>
            </div>
            <div class="grid three">
                <div class="card project-card"><div class="project-icon">✦</div><h3>AI-Powered Products</h3><p>Products designed so intelligence solves a real workflow problem, not just a demo.</p></div>
                <div class="card project-card"><div class="project-icon">↻</div><h3>Intelligent Automation</h3><p>Removing repetitive, manual steps so teams spend time on judgment, not data entry.</p></div>
                <div class="card project-card"><div class="project-icon">◇</div><h3>Chatbots &amp; Conversational Systems</h3><p>Conversational interfaces that meet people where they already are, like WhatsApp.</p></div>
                <div class="card project-card"><div class="project-icon">◌</div><h3>Machine Learning &amp; NLP</h3><p>Applying ML and NLP where it genuinely improves a decision or an understanding of language.</p></div>
                <div class="card project-card"><div class="project-icon">▣</div><h3>Scalable SaaS Platforms</h3><p>Multi-tenant products built for a team's real workflow, not a single user's.</p></div>
            </div>
        </section>

        <section class="wrap section reveal">
            <div class="section-head">
                <div class="eyebrow">Selected work</div>
                <h2>Selected Technology Projects</h2>
                <p class="section-intro">A closer look at the projects behind the categories above — problem, solution, and current status for each.</p>
            </div>
            <div class="grid three" id="featured-work-grid"></div>
            <p style="margin-top:28px"><a class="btn" href="/work/">See all projects →</a></p>
        </section>

        <section class="wrap section reveal">
            <div class="card feature" style="padding:44px;">
                <div class="eyebrow">Not sure what you need?</div>
                <h2>Have a Problem? Let's Find the Right Solution.</h2>
                <p style="max-width:640px;margin-bottom:28px;">You do not need to know which technology to use. Start by explaining the challenge you are facing. I can help analyse workflows, identify opportunities and explore practical digital solutions — from automation and chatbots to AI-powered products and SaaS platforms.</p>
                <div class="timeline-numbered" style="margin-bottom:28px;">
                    <div class="step"><div class="num">01</div><div><h3>Tell Me the Problem</h3></div></div>
                    <div class="step"><div class="num">02</div><div><h3>Understand the Process</h3></div></div>
                    <div class="step"><div class="num">03</div><div><h3>Identify Opportunities</h3></div></div>
                    <div class="step"><div class="num">04</div><div><h3>Design the Solution</h3></div></div>
                    <div class="step"><div class="num">05</div><div><h3>Build &amp; Automate</h3></div></div>
                    <div class="step"><div class="num">06</div><div><h3>Test &amp; Improve</h3></div></div>
                </div>
                <a class="btn primary" href="/contact/">Discuss Your Problem</a>
            </div>
        </section>

        <section class="wrap section reveal">
            <div class="section-head">
                <div class="eyebrow">How I work</div>
                <h2>How I Build Solutions</h2>
            </div>
            <div class="grid three">
                <div class="card"><h3 style="font:700 1.05rem var(--display);margin:0 0 8px;">Understand</h3><p style="color:var(--muted);margin:0;font-size:.92rem;">Learn the people, workflow and constraints behind the problem before proposing anything.</p></div>
                <div class="card"><h3 style="font:700 1.05rem var(--display);margin:0 0 8px;">Research</h3><p style="color:var(--muted);margin:0;font-size:.92rem;">Look at what already exists, what data is available, and what's genuinely feasible.</p></div>
                <div class="card"><h3 style="font:700 1.05rem var(--display);margin:0 0 8px;">Design</h3><p style="color:var(--muted);margin:0;font-size:.92rem;">Shape a solution around the real workflow, not a generic template.</p></div>
                <div class="card"><h3 style="font:700 1.05rem var(--display);margin:0 0 8px;">Build</h3><p style="color:var(--muted);margin:0;font-size:.92rem;">Develop the product or automation, choosing technology to fit the problem.</p></div>
                <div class="card"><h3 style="font:700 1.05rem var(--display);margin:0 0 8px;">Test</h3><p style="color:var(--muted);margin:0;font-size:.92rem;">Check the solution against real use, not just an ideal case.</p></div>
                <div class="card"><h3 style="font:700 1.05rem var(--display);margin:0 0 8px;">Measure</h3><p style="color:var(--muted);margin:0;font-size:.92rem;">Track what actually changed, and improve based on evidence.</p></div>
            </div>
        </section>

        <section class="wrap section reveal">
            <div class="section-head">
                <div class="eyebrow">Technology &amp; expertise</div>
                <h2>Where I Work</h2>
                <p class="section-intro">Organised by area rather than a generic skill-percentage bar — only technologies and skills genuinely demonstrated in the work on this site.</p>
            </div>
            <div class="grid two">
                <div class="card"><h3 style="font:700 .95rem var(--display);margin:0 0 14px;color:var(--muted);text-transform:uppercase;letter-spacing:.06em">Artificial Intelligence &amp; Machine Learning</h3>
                    <div class="chip-row">
                        <span class="chip">Machine Learning</span><span class="chip">Generative AI</span><span class="chip">Natural Language Processing</span>
                        <span class="chip">Sentiment Analysis</span><span class="chip">Predictive Modeling</span><span class="chip">Regression &amp; Logistic Regression</span>
                        <span class="chip">TensorFlow</span><span class="chip">PyTorch</span><span class="chip">Scikit-Learn</span><span class="chip">Chatbots &amp; Conversational AI</span>
                    </div>
                </div>
                <div class="card"><h3 style="font:700 .95rem var(--display);margin:0 0 14px;color:var(--muted);text-transform:uppercase;letter-spacing:.06em">Intelligent Automation &amp; Conversational Systems</h3>
                    <div class="chip-row">
                        <span class="chip">WhatsApp Business API</span><span class="chip">Workflow Automation</span><span class="chip">Firebase</span>
                    </div>
                </div>
                <div class="card"><h3 style="font:700 .95rem var(--display);margin:0 0 14px;color:var(--muted);text-transform:uppercase;letter-spacing:.06em">SaaS &amp; Product Engineering</h3>
                    <div class="chip-row">
                        <span class="chip">JavaScript</span><span class="chip">Product Design &amp; Prototyping</span><span class="chip">Product Strategy</span>
                    </div>
                </div>
                <div class="card"><h3 style="font:700 .95rem var(--display);margin:0 0 14px;color:var(--muted);text-transform:uppercase;letter-spacing:.06em">Data &amp; Analytics</h3>
                    <div class="chip-row">
                        <span class="chip">Python</span><span class="chip">SQL</span><span class="chip">Pandas</span><span class="chip">Data Analytics</span>
                        <span class="chip">Data Visualization</span><span class="chip">Dashboard Building</span><span class="chip">Microsoft Power BI</span>
                    </div>
                </div>
            </div>
        </section>

        <section class="wrap section reveal">
            <div class="grid two">
                <div class="card">
                    <div class="eyebrow">Research &amp; Publications</div>
                    <h3 style="font:700 1.2rem var(--display);margin:0 0 10px;">Published Work</h3>
                    <p style="color:var(--muted);font-size:.92rem;margin:0 0 18px;">A conference paper at the National Conference on Managing Mega Cities (2024) and a guided journal published on Amazon.</p>
                    <a class="btn small" href="/research/">View research →</a>
                </div>
                <div class="card">
                    <div class="eyebrow">IMADI Technologies</div>
                    <h3 style="font:700 1.2rem var(--display);margin:0 0 10px;">Founder &amp; AI Specialist</h3>
                    <p style="color:var(--muted);font-size:.92rem;margin:0 0 18px;">Building AI-powered business software, WhatsApp automation and SaaS products for clients in Pakistan, the United Kingdom and Kenya.</p>
                    <a class="btn small" href="/about/">About my experience →</a>
                </div>
            </div>
        </section>
"""

home_extra = """    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Person",
      "name": "Maria Aziz",
      "jobTitle": "AI Product Founder & Technology Entrepreneur",
      "worksFor": { "@type": "Organization", "name": "Imadi Technologies", "url": "https://imadi-technologies.com" },
      "sameAs": ["https://www.linkedin.com/in/maria-aziz-ai/", "https://github.com/Mariyah52"]
    }
    </script>
    <script src="/assets/projects-data.js"></script>
"""
home_scripts = """    <script>
        (function () {
            var grid = document.getElementById('featured-work-grid');
            if (!grid || !window.PROJECTS) return;
            var featured = window.PROJECTS.filter(function (p) { return p.featured; }).slice(0, 6);
            featured.forEach(function (p) {
                var a = document.createElement('a');
                a.href = '/case-study/?slug=' + encodeURIComponent(p.slug);
                a.className = 'card project-card reveal in';
                var problem = p.problem || p.solution || '';
                a.innerHTML =
                    '<div class="project-tag">' + p.tagline + '</div>' + (p.client ? '<div class="project-client">' + p.client + '</div>' : '') +
                    '<div class="project-status" data-status="' + p.status + '">' + p.status + '</div>' +
                    '<h3>' + p.name + '</h3>' +
                    '<p>' + problem + '</p>' +
                    '<span class="arrow">View case study →</span>';
                grid.appendChild(a);
            });
        })();
    </script>
"""

write("/index.html", page(
    "Maria Aziz | AI Product Founder & Technology Entrepreneur",
    "Maria Aziz builds AI-powered products, intelligent automation, conversational systems and scalable SaaS solutions for real-world problems.",
    "/",
    home_body,
    extra_head=home_extra,
    extra_scripts=home_scripts,
))

# ---------------------------------------------------------------- ABOUT ----
about_body = """
        <section class="wrap page-hero reveal">
            <div class="eyebrow">About</div>
            <h1>Maria Aziz</h1>
            <p style="font-weight:700;color:var(--ink);font-size:1.15rem;margin:-6px 0 20px;">AI Product Founder &amp; Technology Entrepreneur</p>
            <p>I build practical technology solutions around real-world problems, working across AI-powered products, machine learning, natural language processing, automation, conversational systems and SaaS.</p>
            <p>My approach begins with understanding the people, processes and challenges behind a problem before selecting the technology. Since founding IMADI Technologies, I have built six client platforms for businesses in Pakistan, the United Kingdom and Kenya, five of them live in daily use, alongside my own SaaS products.</p>
            <div style="display:flex;flex-wrap:wrap;gap:14px;color:var(--muted);font-size:.86rem;margin-top:22px;">
                <span>📍 Karachi, Sindh, Pakistan</span>
                <span>🏢 Founder &amp; AI Specialist, IMADI Technologies</span>
                <span>🌍 Clients in Pakistan, UK &amp; Kenya</span>
                <span>🎓 AI/ML/DL Specialization, IBA Karachi</span>
            </div>
        </section>

        <section class="wrap section reveal">
            <div class="section-head"><div class="eyebrow">What I do</div><h2>Capabilities</h2></div>
            <div class="chip-row">
                <span class="chip">AI Product Development</span><span class="chip">Machine Learning</span><span class="chip">Natural Language Processing</span>
                <span class="chip">Intelligent Automation</span><span class="chip">Conversational Systems</span><span class="chip">SaaS</span><span class="chip">Product Strategy</span>
            </div>
        </section>

        <section class="wrap section reveal">
            <div class="section-head"><div class="eyebrow">Experience</div><h2>Founder &amp; AI Specialist, IMADI Technologies</h2></div>
            <p class="section-intro">May 2025 – Present · Karachi, Pakistan. I founded IMADI Technologies to build AI-powered business software, WhatsApp automation and SaaS products for SMEs. I gather requirements directly from business owners, then design, build and deploy each system end to end.</p>
            <div class="stack">
                <div class="card exp-card">
                    <div class="exp-logo">AE</div>
                    <div>
                        <h3 style="font:700 1.1rem var(--display);margin:0 0 4px;">ALICO Business Suite</h3>
                        <p style="color:var(--muted);font-size:.86rem;margin:0 0 10px;">Client: ALICO Enterprises, Pakistan · May 2026 – Present · Live</p>
                        <p style="color:#cdd9ec;font-size:.94rem;margin:0 0 12px;">Complete business management PWA: quotations, challans, GST invoices, purchase orders, stock, ledgers and banking, offline-first with real-time sync.</p>
                        <a class="btn small" href="/case-study/?slug=alico">View case study →</a>
                    </div>
                </div>
                <div class="card exp-card">
                    <div class="exp-logo">UK</div>
                    <div>
                        <h3 style="font:700 1.1rem var(--display);margin:0 0 4px;">ERP &amp; Accounting Platform</h3>
                        <p style="color:var(--muted);font-size:.86rem;margin:0 0 10px;">Client: logistics company, United Kingdom · Jun 2026 – Present · Live</p>
                        <p style="color:#cdd9ec;font-size:.94rem;margin:0 0 12px;">13-module ERP and double-entry accounting backend with UK VAT, logistics and OCR, verified by 358 end-to-end tests.</p>
                        <a class="btn small" href="/case-study/?slug=uk-logistics-erp">View case study →</a>
                    </div>
                </div>
                <div class="card exp-card">
                    <div class="exp-logo">SE</div>
                    <div>
                        <h3 style="font:700 1.1rem var(--display);margin:0 0 4px;">SHAH Enterprise Business Suite</h3>
                        <p style="color:var(--muted);font-size:.86rem;margin:0 0 10px;">Client: SHAH Enterprise, Pakistan · Jul 2026 – Present · Live</p>
                        <p style="color:#cdd9ec;font-size:.94rem;margin:0 0 12px;">Adapted the ALICO platform for a petrochemicals trader, with linked document conversion and automatic stock updates.</p>
                        <a class="btn small" href="/case-study/?slug=shah">View case study →</a>
                    </div>
                </div>
                <div class="card exp-card">
                    <div class="exp-logo">RN</div>
                    <div>
                        <h3 style="font:700 1.1rem var(--display);margin:0 0 4px;">ReNaz: WhatsApp Scrap Collection Platform</h3>
                        <p style="color:var(--muted);font-size:.86rem;margin:0 0 10px;">Client: scrap collection business, Pakistan · Aug 2026 – Present · Live</p>
                        <p style="color:#cdd9ec;font-size:.94rem;margin:0 0 12px;">WhatsApp-first pickup booking for customers and collectors, with 23+ pickups completed and 1–2 new requests daily.</p>
                        <a class="btn small" href="/case-study/?slug=renaz">View case study →</a>
                    </div>
                </div>
                <div class="card exp-card">
                    <div class="exp-logo">UK</div>
                    <div>
                        <h3 style="font:700 1.1rem var(--display);margin:0 0 4px;">WhatsApp Automation &amp; Operations Platform</h3>
                        <p style="color:var(--muted);font-size:.86rem;margin:0 0 10px;">Client: logistics company, United Kingdom (repeat client) · Sep 2026 – Present · Live</p>
                        <p style="color:#cdd9ec;font-size:.94rem;margin:0 0 12px;">Instant rate quotes, order enquiries and a full damage-claims workflow on WhatsApp, with an operations dashboard.</p>
                        <a class="btn small" href="/case-study/?slug=uk-logistics-whatsapp">View case study →</a>
                    </div>
                </div>
                <div class="card exp-card">
                    <div class="exp-logo">KE</div>
                    <div>
                        <h3 style="font:700 1.1rem var(--display);margin:0 0 4px;">Company Monitor</h3>
                        <p style="color:var(--muted);font-size:.86rem;margin:0 0 10px;">Client: multi-branch business, Nairobi, Kenya · Sep 2026 – Present · In build</p>
                        <p style="color:#cdd9ec;font-size:.94rem;margin:0 0 12px;">Secure platform giving management branch-level visibility of messages on company-authorised WhatsApp Business numbers.</p>
                        <a class="btn small" href="/case-study/?slug=company-monitor">View case study →</a>
                    </div>
                </div>
            </div>
        </section>

        <section class="wrap section reveal">
            <div class="section-head"><div class="eyebrow">Education</div><h2>My Background</h2></div>
            <div class="stack">
                <div class="card exp-card">
                    <div class="exp-logo">IBA</div>
                    <div>
                        <h3 style="font:700 1.1rem var(--display);margin:0 0 4px;">Specialization Certificate: Artificial Intelligence / Machine Learning / Deep Learning</h3>
                        <p style="color:var(--muted);font-size:.86rem;margin:0 0 10px;">Institute of Business Administration (IBA), Karachi · February 2026 – May 2026</p>
                        <p style="color:#cdd9ec;font-size:.94rem;margin:0 0 12px;">Fully funded under the Prime Minister's Hunarmand Pakistan Program (NAVTTC). Machine learning, deep learning and NLP pipelines with scikit-learn, TensorFlow, PyTorch and Keras.</p>
                    </div>
                </div>
                <div class="card exp-card">
                    <div class="exp-logo">KU</div>
                    <div>
                        <h3 style="font:700 1.1rem var(--display);margin:0 0 4px;">Bachelor of Public Administration (BSPA, BS 4-year)</h3>
                        <p style="color:var(--muted);font-size:.86rem;margin:0 0 10px;">University of Karachi · January 2024 – December 2025 · CGPA 3.37 / 4.00</p>
                        <p style="color:#cdd9ec;font-size:.94rem;margin:0 0 12px;">16 years of education. Statistics, research methodology, Power BI, logistics and supply chain management, and public policy.</p>
                    </div>
                </div>
                <div class="card exp-card">
                    <div class="exp-logo">KU</div>
                    <div>
                        <h3 style="font:700 1.1rem var(--display);margin:0 0 4px;">Bachelor of Arts (Psychology)</h3>
                        <p style="color:var(--muted);font-size:.86rem;margin:0 0 10px;">University of Karachi · November 2009 – December 2011 · 69.32%</p>
                        <p style="color:#cdd9ec;font-size:.94rem;margin:0 0 12px;">14 years of education.</p>
                    </div>
                </div>
            </div>
            <div class="card" style="margin-top:24px;">
                <p style="color:#cdd9ec;margin:0;">A background in public administration and psychology alongside a technical AI specialisation gives me a working understanding of how organisations, operations and people actually function, which shapes how I design technology for real-world use, not just the technology in isolation.</p>
            </div>
        </section>

        <section class="wrap section reveal">
            <div class="section-head"><div class="eyebrow">Certifications</div><h2>Selected Certifications</h2></div>
            <div class="grid three">
                <div class="card">
                    <h3 style="font:700 1.02rem var(--display);margin:0 0 12px;">AI &amp; Data</h3>
                    <ul style="margin:0;padding-left:18px;color:#cdd9ec;font-size:.88rem;display:grid;gap:5px;">
                        <li>Google AI Professional Certificate — Coursera</li>
                        <li>AI Fundamentals — Google</li>
                        <li>AI for Data Analysis — Google</li>
                        <li>AI for Content Creation — Google</li>
                        <li>AI for App Building — Google</li>
                        <li>AI for Research and Insights — Google</li>
                        <li>AI for Writing and Communicating — Google</li>
                        <li>AI for Brainstorming and Planning — Google</li>
                        <li>Foundations: Data, Data, Everywhere — Google</li>
                    </ul>
                </div>
                <div class="card">
                    <h3 style="font:700 1.02rem var(--display);margin:0 0 12px;">Project &amp; People Management</h3>
                    <ul style="margin:0;padding-left:18px;color:#cdd9ec;font-size:.88rem;display:grid;gap:5px;">
                        <li>Foundations of Agile Project Management — Google</li>
                        <li>Organize Projects and Measure Productivity with Scrum — Google</li>
                        <li>Google People Management Essentials — Google</li>
                        <li>Grow as a Manager — Google</li>
                        <li>Create a High-Performing Team — Google</li>
                        <li>Set and Achieve Team Goals — Google</li>
                        <li>Support Individual Growth and Development — Google</li>
                    </ul>
                </div>
                <div class="card">
                    <h3 style="font:700 1.02rem var(--display);margin:0 0 12px;">Marketing &amp; Design</h3>
                    <ul style="margin:0;padding-left:18px;color:#cdd9ec;font-size:.88rem;display:grid;gap:5px;">
                        <li>Search Engine Optimization (SEO) with Squarespace — Coursera</li>
                        <li>Use Canva to Design Digital Course Collateral — Coursera</li>
                        <li>Start Writing Prompts like a Pro — Google</li>
                    </ul>
                </div>
            </div>
            <p style="color:var(--muted);font-size:.84rem;margin-top:16px;">A full list of licenses and certifications (21 total) is available on LinkedIn.</p>
        </section>

        <section class="wrap section reveal">
            <div class="card feature center" style="padding:44px;text-align:center;">
                <h2>See the work behind this background</h2>
                <p style="max-width:520px;margin:0 auto 24px;">Projects, case studies and research that put this approach into practice.</p>
                <a class="btn primary" href="/work/">Explore my work</a>
            </div>
        </section>
"""
write("/about/index.html", page(
    "About | Maria Aziz",
    "Maria Aziz is an AI Product Founder and Technology Entrepreneur building practical technology around real-world problems.",
    "/about/",
    about_body,
))

# ----------------------------------------------------------------- WORK ----
work_body = """
        <section class="wrap page-hero reveal">
            <div class="eyebrow">Work</div>
            <h1>Selected Technology Projects</h1>
            <p>Problem, solution and current status for each project — filter by category to explore.</p>
        </section>

        <section class="wrap section reveal">
            <div class="filter-bar" id="filter-bar"></div>
            <div class="grid three" id="work-grid"></div>
        </section>
"""
work_scripts = """    <script src="/assets/projects-data.js"></script>
    <script>
        (function () {
            var grid = document.getElementById('work-grid');
            var bar = document.getElementById('filter-bar');
            if (!grid || !bar || !window.PROJECTS) return;

            var categoriesPresent = ['featured'];
            window.PROJECTS.forEach(function (p) {
                p.categories.forEach(function (c) { if (categoriesPresent.indexOf(c) === -1) categoriesPresent.push(c); });
            });

            var active = 'featured';

            function render() {
                grid.innerHTML = '';
                var list = active === 'featured'
                    ? window.PROJECTS.filter(function (p) { return p.featured; })
                    : window.PROJECTS.filter(function (p) { return p.categories.indexOf(active) !== -1; });
                list.forEach(function (p) {
                    var a = document.createElement('a');
                    a.href = '/case-study/?slug=' + encodeURIComponent(p.slug);
                    a.className = 'card project-card';
                    var problem = p.problem || p.solution || '';
                    a.innerHTML =
                        '<div class="project-tag">' + p.tagline + '</div>' + (p.client ? '<div class="project-client">' + p.client + '</div>' : '') +
                        '<div class="project-status" data-status="' + p.status + '">' + p.status + '</div>' +
                        '<h3>' + p.name + '</h3>' +
                        '<p>' + problem + '</p>' +
                        '<span class="arrow">View case study →</span>';
                    grid.appendChild(a);
                });
            }

            categoriesPresent.forEach(function (cat) {
                var btn = document.createElement('button');
                btn.className = 'btn small';
                btn.textContent = window.CATEGORY_LABELS[cat] || cat;
                btn.setAttribute('aria-pressed', cat === active ? 'true' : 'false');
                btn.addEventListener('click', function () {
                    active = cat;
                    bar.querySelectorAll('button').forEach(function (b) { b.setAttribute('aria-pressed', 'false'); });
                    btn.setAttribute('aria-pressed', 'true');
                    render();
                });
                bar.appendChild(btn);
            });

            render();
        })();
    </script>
"""
write("/work/index.html", page(
    "Work | Maria Aziz",
    "Selected AI, automation, chatbot, SaaS, machine learning and social-impact technology projects by Maria Aziz.",
    "/work/",
    work_body,
    extra_scripts=work_scripts,
))

# ------------------------------------------------------------ SOLUTIONS ----
def solution_card(eyebrow, problem, solutions):
    return f"""<div class="card"><div class="eyebrow">{eyebrow}</div>
                    <p style="color:var(--muted);font-size:.82rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 6px;">Problem</p>
                    <p style="color:#cdd9ec;margin:0 0 16px;">{problem}</p>
                    <p style="color:var(--muted);font-size:.82rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 6px;">Potential solutions</p>
                    <p style="color:#cdd9ec;margin:0;">{solutions}</p>
                </div>"""

solutions_body = f"""
        <section class="wrap page-hero reveal">
            <div class="eyebrow">Solutions</div>
            <h1>Tell Me Your Problem. Let's Explore the Solution.</h1>
            <p>Start from the problem, not the technology. Here are the kinds of challenges I work on most often.</p>
        </section>

        <section class="wrap section reveal">
            <div class="grid two">
                {solution_card("Business Operations", "Manual workflows and repetitive processes.", "Automation, dashboards and integrated systems.")}
                {solution_card("Customer Communication", "Teams spend time responding to repetitive inquiries.", "Chatbots and conversational automation.")}
                {solution_card("Data &amp; Decision Making", "Organisations have data but lack useful insights.", "Analytics, dashboards and machine learning.")}
                {solution_card("Education Technology", "Learning and progress tracking can be fragmented.", "AI-powered learning platforms and SaaS.")}
                {solution_card("Logistics &amp; Operations", "Disconnected and manual operational workflows.", "Digital workflows, automation and intelligent systems.")}
                {solution_card("Community &amp; Social Impact", "Complex public and community challenges need better digital tools.", "Research-driven platforms, data systems and technology solutions.")}
            </div>
        </section>

        <section class="wrap section reveal">
            <div class="card feature center" style="padding:44px;text-align:center;">
                <h2>Tell Me About Your Challenge</h2>
                <p style="max-width:520px;margin:0 auto 24px;">You don't need the technical answer yet — just describe what's happening.</p>
                <a class="btn primary" href="/contact/">Get in touch</a>
            </div>
        </section>
"""
write("/solutions/index.html", page(
    "Solutions | Maria Aziz",
    "Tell Maria Aziz your problem — business operations, customer communication, data, education technology, logistics or social impact — and explore the right technology solution.",
    "/solutions/",
    solutions_body,
))

# ------------------------------------------------------------- RESEARCH ----
def field(label, value):
    return f'<div><p style="color:var(--muted);font-size:.78rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 4px;">{label}</p><p style="color:#cdd9ec;margin:0;">{value}</p></div>'

research_body = f"""
        <section class="wrap page-hero reveal">
            <div class="eyebrow">Research</div>
            <h1>Research &amp; Publications</h1>
            <p>Published academic and written work, alongside the machine learning research behind my projects.</p>
        </section>

        <section class="wrap section reveal">
            <div class="section-head"><div class="eyebrow">Conference Paper · 2024</div><h2>Exploring the Psychological Puzzle of Travelling: A Journey Through Your Thoughts</h2></div>
            <div class="card">
                <div class="grid two" style="margin-bottom:18px;">
                    {field("Author", "Maria Aziz")}
                    {field("Role", "Research Scholar, Department of Public Administration, University of Karachi")}
                    {field("Conference", "National Conference on Managing Mega Cities (NCMC), Department of Public Administration, University of Karachi")}
                    {field("Date", "14–15 May 2024")}
                </div>
                <p style="color:var(--muted);font-size:.78rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 4px;">Summary</p>
                <p style="color:#cdd9ec;margin:0 0 12px;">Explores the psychological dimensions of daily commuting and travel behaviour: how routine journeys by walking, cycling, driving or public transport affect mood, stress, attention and reflective thinking.</p>
                <ul style="margin:0;padding-left:18px;color:#cdd9ec;display:grid;gap:5px;">
                    <li>The interplay between the mind and daily travel routines</li>
                    <li>How traffic jams, delays and crowded transport drive stress and annoyance</li>
                    <li>Moments of calm and self-reflection on familiar routes</li>
                    <li>Implications for urban mobility and well-being in mega cities</li>
                </ul>
            </div>
        </section>

        <section class="wrap section reveal">
            <div class="section-head"><div class="eyebrow">Book · Amazon KDP</div><h2>Overthinking Journal for Women 25–40: A Guided Emotional Reset System</h2></div>
            <div class="card">
                <div class="grid two" style="margin-bottom:18px;">
                    {field("Author", "Mariyah Aziz")}
                    {field("Format", "Paperback, self-published on Amazon KDP (ASIN B0GZBRLHDD)")}
                </div>
                <p style="color:#cdd9ec;margin:0 0 18px;">A guided, structured journal that helps women manage racing thoughts, emotional overwhelm and mental spirals. Targeted prompts and a guided emotional-reset framework help readers slow down, process their thoughts and regain calm and clarity in daily life: a practical, non-clinical tool for everyday emotional regulation.</p>
                <a class="btn primary small" href="https://www.amazon.com/dp/B0GZBRLHDD" target="_blank" rel="noopener">View on Amazon ↗</a>
            </div>
        </section>

        <section class="wrap section reveal">
            <div class="section-head"><div class="eyebrow">Machine learning research</div><h2>AI / ML Projects</h2></div>
            <div class="grid two">
                <a class="card project-card" href="/case-study/?slug=nlp-sentiment-analysis"><div class="project-tag">NLP · Research</div><h3>NLP Sentiment Analysis of Travel Blogs</h3><p>Comparing BERT and LSTM models on nuanced emotional sentiment in long-form travel writing.</p><span class="arrow">View case study →</span></a>
                <a class="card project-card" href="/case-study/?slug=ml-pipeline"><div class="project-tag">ML · IBA Karachi</div><h3>End-to-End Machine Learning Pipeline</h3><p>21 Decision Tree and SVM models trained, tuned and evaluated on accuracy, sensitivity and specificity.</p><span class="arrow">View case study →</span></a>
            </div>
        </section>
"""
write("/research/index.html", page(
    "Research | Maria Aziz",
    "Research and publications by Maria Aziz: a 2024 National Conference on Managing Mega Cities paper, a book on Amazon, and machine learning research.",
    "/research/",
    research_body,
))

# -------------------------------------------------------------------- NOW -
def now_card(logo, title, meta, slug):
    return f"""                <div class="card exp-card">
                    <div class="exp-logo">{logo}</div>
                    <div>
                        <h3 style="font:700 1.1rem var(--display);margin:0 0 4px;">{title}</h3>
                        <p style="color:var(--muted);font-size:.86rem;margin:0 0 10px;">{meta}</p>
                        <a class="btn small" href="/case-study/?slug={slug}">View case study →</a>
                    </div>
                </div>
"""
now_body = f"""
        <section class="wrap page-hero reveal">
            <div class="eyebrow">Now · September 2026</div>
            <h1>What I'm Building Now</h1>
            <p>Work actively in progress right now. Everything already delivered lives on the <a href="/work/" style="color:var(--cyan);font-weight:700;">Work</a> page.</p>
        </section>

        <section class="wrap section reveal">
            <div class="stack">
{now_card("KE", "Company Monitor", "Client project, Nairobi, Kenya · In build · QR-login pilot in testing", "company-monitor")}
{now_card("AI", "IMADI AI Sales Engine", "Co-founded venture · Launching October 2026", "imadi-sales-engine")}
{now_card("MB", "Marist Bot", "Own product · Conversational AI assistant · ~80% built", "marist-bot")}
{now_card("HA", "HifzAI", "Own product · Completed · Pilot stage ahead of launch", "hifzai")}
{now_card("RN", "ReNaz", "Client project, Pakistan · Live · Expanding to commercial bulk scrap", "renaz")}
            </div>
        </section>
"""
write("/now/index.html", page(
    "Now | Maria Aziz",
    "What Maria Aziz is actively building right now.",
    "/now/",
    now_body,
))

# ---------------------------------------------------------------- CONTACT -
contact_body = """
        <section class="wrap page-hero reveal">
            <div class="eyebrow">Contact</div>
            <h1>Tell Me Your Problem.</h1>
            <p>You don't need to know which technology fits. Describe the challenge and we'll work out the right approach together.</p>
        </section>

        <section class="wrap section reveal">
            <div class="grid two">
                <a class="card" href="mailto:mariyahheal92@gmail.com" style="text-decoration:none;">
                    <div class="eyebrow">Email</div>
                    <h3 style="font:700 1.15rem var(--display);margin:0 0 6px;">mariyahheal92@gmail.com</h3>
                    <p style="color:var(--muted);margin:0;">The best way to describe a project or problem in detail.</p>
                </a>
                <a class="card" href="https://www.linkedin.com/in/maria-aziz-ai/" target="_blank" rel="noopener" style="text-decoration:none;">
                    <div class="eyebrow">LinkedIn</div>
                    <h3 style="font:700 1.15rem var(--display);margin:0 0 6px;">linkedin.com/in/maria-aziz-ai ↗</h3>
                    <p style="color:var(--muted);margin:0;">Connect or send a message.</p>
                </a>
                <a class="card" href="https://github.com/Mariyah52" target="_blank" rel="noopener" style="text-decoration:none;">
                    <div class="eyebrow">GitHub</div>
                    <h3 style="font:700 1.15rem var(--display);margin:0 0 6px;">github.com/Mariyah52 ↗</h3>
                    <p style="color:var(--muted);margin:0;">Public code and open-source projects.</p>
                </a>
                <a class="card" href="/assets/Maria_Aziz_CV.pdf" target="_blank" rel="noopener" style="text-decoration:none;">
                    <div class="eyebrow">CV</div>
                    <h3 style="font:700 1.15rem var(--display);margin:0 0 6px;">Download my CV (PDF) ↓</h3>
                    <p style="color:var(--muted);margin:0;">Two pages: experience, products, education and publications.</p>
                </a>
            </div>
        </section>
"""
write("/contact/index.html", page(
    "Contact | Maria Aziz",
    "Get in touch with Maria Aziz to discuss an AI product, automation or SaaS problem.",
    "/contact/",
    contact_body,
))

# ------------------------------------------------------------ CASE STUDY --
case_study_body = """
        <section class="wrap page-hero reveal">
            <div class="eyebrow" id="case-tagline">Case study</div>
            <h1 id="case-title">Loading…</h1>
            <div class="case-hero-meta">
                <span class="project-status" id="case-status" data-status="">Status</span>
                <span class="case-meta" id="case-client"></span>
                <span class="case-meta" id="case-period"></span>
            </div>
        </section>
        <section class="wrap" style="padding:20px 0 60px;">
            <div class="card" style="padding:8px 40px;">
                <div class="case-section" data-field="problem" hidden><h2>The Problem</h2><p id="case-problem"></p></div>
                <div class="case-section" data-field="challenge" hidden><h2>The Challenge</h2><p id="case-challenge"></p></div>
                <div class="case-section" data-field="solution" hidden><h2>The Solution</h2><p id="case-solution"></p></div>
                <div class="case-section" data-field="features" hidden><h2>Key Features</h2><ul class="feature-list" id="case-features"></ul></div>
                <div class="case-section" data-field="myRole" hidden><h2>My Role</h2><p id="case-myRole"></p></div>
                <div class="case-section" data-field="technology" hidden><h2>Technology</h2><div class="chip-row" id="case-technology"></div></div>
                <div class="case-section" data-field="architecture" hidden><h2>Architecture</h2><div class="workflow-steps" id="case-architecture"></div></div>
                <div class="case-section" data-field="innovation" hidden><h2>What's Different</h2><p id="case-innovation"></p></div>
                <div class="case-section" data-field="results" hidden><h2>Results</h2><ul class="feature-list" id="case-results"></ul></div>
                <div class="case-section" data-field="evidence" hidden><h2>Links</h2><div class="evidence-list" id="case-evidence"></div></div>
            </div>
        </section>
        <section class="wrap section reveal">
            <div class="card feature center" style="padding:44px;text-align:center;">
                <h2>Have a similar problem?</h2>
                <p style="max-width:480px;margin:0 auto 24px;">Let's talk through what you're trying to solve.</p>
                <a class="btn primary" href="/contact/">Discuss your problem</a>
            </div>
        </section>
"""
case_study_scripts = """    <script src="/assets/projects-data.js"></script>
    <script>
        (function () {
            var slug = new URLSearchParams(location.search).get('slug');
            var project = slug ? window.getProjectBySlug(slug) : null;
            if (!project) {
                document.getElementById('case-title').textContent = 'Case study not found';
                return;
            }
            document.title = project.name + ' | Maria Aziz';
            document.getElementById('case-title').textContent = project.name;
            document.getElementById('case-tagline').textContent = project.tagline;
            var statusEl = document.getElementById('case-status');
            statusEl.textContent = project.status;
            statusEl.setAttribute('data-status', project.status);
            document.getElementById('case-client').textContent = project.client || '';
            document.getElementById('case-period').textContent = project.period || '';

            function show(field) { document.querySelector('[data-field="' + field + '"]').hidden = false; }
            function text(field) {
                if (!project[field]) return;
                document.getElementById('case-' + field).textContent = project[field];
                show(field);
            }
            function list(field, id, cls) {
                var items = project[field];
                if (!items || !items.length) return;
                var el = document.getElementById(id);
                items.forEach(function (item) {
                    var node = document.createElement(cls === 'li' ? 'li' : 'span');
                    if (cls !== 'li') node.className = cls;
                    node.textContent = item;
                    el.appendChild(node);
                });
                show(field);
            }
            ['problem', 'challenge', 'solution', 'myRole', 'innovation'].forEach(text);
            list('features', 'case-features', 'li');
            list('results', 'case-results', 'li');
            list('technology', 'case-technology', 'chip');
            list('architecture', 'case-architecture', 'workflow-step');
            if (project.evidence && project.evidence.length) {
                var ev = document.getElementById('case-evidence');
                project.evidence.forEach(function (e) {
                    var a = document.createElement('a');
                    a.href = e.href; a.target = '_blank'; a.rel = 'noopener';
                    a.textContent = e.label + ' ↗';
                    ev.appendChild(a);
                });
                show('evidence');
            }
        })();
    </script>
"""
write("/case-study/index.html", page(
    "Case Study | Maria Aziz",
    "A detailed case study: problem, solution, technology, and results.",
    "/case-study/",
    case_study_body,
    extra_scripts=case_study_scripts,
))

# ------------------------------------------------------------ SEO FILES --
# No live domain is confirmed yet for this site. Rather than guess one, the
# sitemap uses an obvious placeholder token — find-and-replace it with the
# real domain once this site is actually hosted somewhere.
SITE_URL_PLACEHOLDER = "https://maria-aziz-portfolio.onrender.com"
sitemap_paths = ["/", "/about/", "/work/", "/solutions/", "/research/", "/now/", "/contact/"]
sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for p in sitemap_paths:
    sitemap_xml += f"  <url><loc>{SITE_URL_PLACEHOLDER}{p}</loc></url>\n"
sitemap_xml += "</urlset>\n"
write("/sitemap.xml", sitemap_xml)

robots_txt = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL_PLACEHOLDER}/sitemap.xml
"""
write("/robots.txt", robots_txt)

print("\\nAll pages generated.")
