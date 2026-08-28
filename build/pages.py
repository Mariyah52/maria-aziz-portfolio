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
                    <div class="eyebrow">Research</div>
                    <h3 style="font:700 1.2rem var(--display);margin:0 0 10px;">Research, Publications &amp; Recognition</h3>
                    <p style="color:var(--muted);font-size:.92rem;margin:0 0 18px;">A 2024 conference proceeding at the National Conference on Managing Mega Cities, plus recognition and media coverage as it's confirmed.</p>
                    <a class="btn small" href="/research/">View research →</a>
                </div>
                <div class="card">
                    <div class="eyebrow">Recognition</div>
                    <h3 style="font:700 1.2rem var(--display);margin:0 0 10px;">Media &amp; Recognition</h3>
                    <p style="color:var(--muted);font-size:.92rem;margin:0 0 18px;">Including an IBA success story currently in preparation.</p>
                    <a class="btn small" href="/recognition/">View recognition →</a>
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
      "sameAs": ["https://www.linkedin.com/in/maria-aziz-ai/"]
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
                var problem = p.problem || 'Problem statement to be added.';
                a.innerHTML =
                    '<div class="project-tag">' + p.tagline + '</div>' +
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
            <p>My approach begins with understanding the people, processes and challenges behind a problem before selecting the technology.</p>
            <div style="display:flex;flex-wrap:wrap;gap:14px;color:var(--muted);font-size:.86rem;margin-top:22px;">
                <span>📍 Karachi, Sindh, Pakistan</span>
                <span>🎓 NAVTTC Fellow @ IBA Karachi</span>
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
            <div class="section-head"><div class="eyebrow">Experience</div><h2>Where I've Worked</h2></div>
            <div class="stack">
                <div class="card exp-card">
                    <div class="exp-logo">AE</div>
                    <div>
                        <h3 style="font:700 1.2rem var(--display);margin:0 0 4px;">AI / ML and Automation Consultant</h3>
                        <p style="color:var(--muted);font-size:.86rem;margin:0 0 12px;">ALICO Enterprises · Contract · Jun 2026 – Present · Karachi, Sindh, Pakistan · Remote</p>
                        <p style="color:#cdd9ec;font-size:.96rem;margin:0 0 14px;">Designed and deployed the ALICO Business Suite, a web ERP for invoicing, stock, expense and banking with role-based access control and audit logging.</p>
                        <div class="chip-row"><span class="chip">Firebase</span><span class="chip">Artificial Intelligence (AI)</span></div>
                    </div>
                </div>
                <div class="card exp-card">
                    <div class="exp-logo">SM</div>
                    <div>
                        <h3 style="font:700 1.2rem var(--display);margin:0 0 4px;">AI Product Developer — SmartPlan Meals</h3>
                        <p style="color:var(--muted);font-size:.86rem;margin:0 0 12px;">Self Employed · Freelance · May 2026 – Present · Karachi Division, Sindh, Pakistan · Remote</p>
                        <p style="color:#cdd9ec;font-size:.96rem;margin:0 0 14px;">Developed AI-powered products and automation solutions. SmartPlan Meals is an AI-based meal planning system with personalized nutrition.</p>
                        <div class="chip-row"><span class="chip">Natural Language Processing (NLP)</span><span class="chip">Artificial Intelligence (AI)</span></div>
                    </div>
                </div>
                <div class="card exp-card">
                    <div class="exp-logo">CI</div>
                    <div>
                        <h3 style="font:700 1.2rem var(--display);margin:0 0 4px;">Creator — Child-Friendly City Index</h3>
                        <p style="color:var(--muted);font-size:.86rem;margin:0 0 12px;">Independent Project Development · Self-employed · May 2026 – Present · Remote</p>
                        <p style="color:#cdd9ec;font-size:.96rem;margin:0 0 14px;">Building an open-source tool to score neighborhoods for children — from vision deck to working prototype. Vision: "If Children Designed Our Cities: Reimagining Karachi."</p>
                        <div class="chip-row"><span class="chip">Python</span><span class="chip">Artificial Intelligence (AI)</span></div>
                    </div>
                </div>
            </div>
        </section>

        <section class="wrap section reveal">
            <div class="section-head"><div class="eyebrow">Background</div><h2>My Background</h2></div>
            <div class="stack">
                <div class="card exp-card">
                    <div class="exp-logo">IBA</div>
                    <div>
                        <h3 style="font:700 1.2rem var(--display);margin:0 0 4px;">Institute of Business Administration (IBA)</h3>
                        <p style="color:var(--muted);font-size:.86rem;margin:0 0 12px;">Specialization Certificate, Artificial Intelligence · February 2026 – May 2026</p>
                        <p style="color:#cdd9ec;font-size:.96rem;margin:0;">Selected for the competitive, fully funded Prime Minister's Hunarmand Pakistan Program scholarship.</p>
                    </div>
                </div>
                <div class="card exp-card">
                    <div class="exp-logo">KU</div>
                    <div>
                        <h3 style="font:700 1.2rem var(--display);margin:0 0 4px;">Karachi University</h3>
                        <p style="color:var(--muted);font-size:.86rem;margin:0 0 12px;">Public Administration &amp; Supply Chain Management · January 2024 – December 2025</p>
                        <p class="placeholder" style="font-size:.86rem;margin:0;">Exact official qualification title to be confirmed and added here.</p>
                    </div>
                </div>
                <div class="card exp-card">
                    <div class="exp-logo">KU</div>
                    <div>
                        <h3 style="font:700 1.2rem var(--display);margin:0 0 4px;">Karachi University</h3>
                        <p style="color:var(--muted);font-size:.86rem;margin:0 0 12px;">Bachelor's Degree, Psychology · January 2009 – December 2011 · Grade: A</p>
                        <p style="color:#cdd9ec;font-size:.96rem;margin:0;">Activities: Psychology Seminar Series, Consumer Behavior Workshop, research seminars.</p>
                    </div>
                </div>
            </div>
            <div class="card" style="margin-top:24px;">
                <p style="color:#cdd9ec;margin:0;">Studying public administration and supply chain management alongside a technical AI specialization gives me a working understanding of how organisations, operations, public systems and supply chains actually function — which shapes how I approach real-world implementation, not just the technology in isolation.</p>
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
                    var problem = p.problem || 'Problem statement to be added.';
                    a.innerHTML =
                        '<div class="project-tag">' + p.tagline + '</div>' +
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
research_body = """
        <section class="wrap page-hero reveal">
            <div class="eyebrow">Research</div>
            <h1>Research &amp; Publications</h1>
            <p>Verified academic and conference work. Details are added here only once confirmed — nothing is published as complete until it genuinely is.</p>
        </section>

        <section class="wrap section reveal">
            <div class="section-head"><div class="eyebrow">2024 Publications</div><h2>National Conference on Managing Mega Cities (NCMC)</h2></div>
            <div class="card">
                <div class="grid two" style="margin-bottom:18px;">
                    <div>
                        <p style="color:var(--muted);font-size:.78rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 4px;">Title</p>
                        <p class="placeholder" style="margin:0;">Exact verified publication title to be added.</p>
                    </div>
                    <div>
                        <p style="color:var(--muted);font-size:.78rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 4px;">Authors</p>
                        <p class="placeholder" style="margin:0;">To be confirmed.</p>
                    </div>
                    <div>
                        <p style="color:var(--muted);font-size:.78rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 4px;">Conference</p>
                        <p style="color:#cdd9ec;margin:0;">National Conference on Managing Mega Cities (NCMC)</p>
                    </div>
                    <div>
                        <p style="color:var(--muted);font-size:.78rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 4px;">Date</p>
                        <p style="color:#cdd9ec;margin:0;">May 14–15, 2024</p>
                    </div>
                    <div>
                        <p style="color:var(--muted);font-size:.78rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 4px;">Research area</p>
                        <p class="placeholder" style="margin:0;">To be confirmed.</p>
                    </div>
                    <div>
                        <p style="color:var(--muted);font-size:.78rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 4px;">DOI / official link</p>
                        <p class="placeholder" style="margin:0;">To be added once available.</p>
                    </div>
                </div>
                <p style="color:var(--muted);font-size:.78rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 4px;">Abstract</p>
                <p class="placeholder" style="margin:0;">Abstract to be added once the verified publication details are confirmed.</p>
                <p style="margin-top:18px"><span class="placeholder-tag">Awaiting verified details</span></p>
            </div>
        </section>

        <section class="wrap section reveal">
            <div class="section-head"><div class="eyebrow">Related work</div><h2>NLP Sentiment Analysis of Travel Blogs</h2></div>
            <p class="section-intro">A separate, independent research project comparing BERT and LSTM models on nuanced emotional sentiment in travel writing.</p>
            <a class="btn" href="/case-study/?slug=nlp-sentiment-analysis">View the case study →</a>
        </section>
"""
write("/research/index.html", page(
    "Research | Maria Aziz",
    "Research and publications by Maria Aziz, including a 2024 National Conference on Managing Mega Cities (NCMC) proceeding.",
    "/research/",
    research_body,
))

# -------------------------------------------------------------- WRITING ----
articles = [
    "We Stopped Prompting AI. We Started Onboarding It.",
    "From Problem to Product: How I Approach Technology Solutions",
    "Building Technology for Real-World Problems",
    "BERT vs LSTM: Lessons from My NLP Sentiment Analysis Project",
    "Why Automation Should Start With Understanding the Workflow",
    "WhatsApp as a Gateway to Digital Services",
]
article_cards = "\n                ".join(
    f'<div class="card project-card"><span class="placeholder-tag" style="margin-bottom:14px;align-self:flex-start;">Planned</span><h3>{title}</h3><p class="placeholder">Article coming soon.</p></div>'
    for title in articles
)
writing_body = f"""
        <section class="wrap page-hero reveal">
            <div class="eyebrow">Writing</div>
            <h1>Writing &amp; Insights</h1>
            <p>Planned articles on building AI products, automation and technology for real-world problems. None of these are published yet — this is the upcoming list.</p>
        </section>

        <section class="wrap section reveal">
            <div class="grid three">
                {article_cards}
            </div>
        </section>
"""
write("/writing/index.html", page(
    "Writing | Maria Aziz",
    "Planned articles and insights from Maria Aziz on AI products, automation and building technology for real-world problems.",
    "/writing/",
    writing_body,
))

# ----------------------------------------------------------- RECOGNITION --
recognition_body = """
        <section class="wrap page-hero reveal">
            <div class="eyebrow">Recognition</div>
            <h1>Recognition &amp; Media</h1>
            <p>Verified recognition only — anything still in progress is marked clearly rather than implied.</p>
        </section>

        <section class="wrap section reveal">
            <div class="grid two">
                <div class="card">
                    <div class="eyebrow">IBA</div>
                    <h3 style="font:700 1.2rem var(--display);margin:0 0 10px;">IBA Success Story</h3>
                    <p style="color:var(--muted);margin:0 0 16px;">A success story with the Institute of Business Administration (IBA) is currently being prepared.</p>
                    <span class="placeholder-tag">Success Story — Coming Soon</span>
                </div>
                <div class="card">
                    <div class="eyebrow">Research</div>
                    <h3 style="font:700 1.2rem var(--display);margin:0 0 10px;">Conference Appearance</h3>
                    <p style="color:var(--muted);margin:0 0 16px;">National Conference on Managing Mega Cities (NCMC), May 14–15, 2024.</p>
                    <a class="btn small" href="/research/">View research →</a>
                </div>
            </div>
        </section>

        <section class="wrap section reveal">
            <div class="section-head"><div class="eyebrow">Media &amp; appearances</div><h2>Coverage, Interviews &amp; Podcasts</h2></div>
            <div class="card">
                <p class="placeholder" style="margin:0;">No media coverage, interviews, podcast appearances or awards are confirmed yet. This section will be updated as soon as any are.</p>
            </div>
        </section>
"""
write("/recognition/index.html", page(
    "Recognition | Maria Aziz",
    "Recognition and media coverage for Maria Aziz, including the IBA success story (coming soon) and conference appearances.",
    "/recognition/",
    recognition_body,
))

# -------------------------------------------------------------------- NOW -
now_body = """
        <section class="wrap page-hero reveal">
            <div class="eyebrow">Now</div>
            <h1>What I'm Building Now</h1>
            <p>Only projects that are genuinely active right now — everything else lives on the <a href="/work/" style="color:var(--cyan);font-weight:700;">Work</a> page.</p>
        </section>

        <section class="wrap section reveal">
            <div class="stack">
                <div class="card exp-card">
                    <div class="exp-logo">AE</div>
                    <div>
                        <h3 style="font:700 1.2rem var(--display);margin:0 0 4px;">ALICO Business Suite</h3>
                        <p style="color:var(--muted);font-size:.86rem;margin:0 0 10px;">AI/ML and Automation Consultant, ALICO Enterprises · Jun 2026 – Present</p>
                        <a class="btn small" href="/case-study/?slug=alico">View case study →</a>
                    </div>
                </div>
                <div class="card exp-card">
                    <div class="exp-logo">SM</div>
                    <div>
                        <h3 style="font:700 1.2rem var(--display);margin:0 0 4px;">Smart Meal Planner</h3>
                        <p style="color:var(--muted);font-size:.86rem;margin:0 0 10px;">AI Product Developer, self-employed · May 2026 – Present</p>
                        <a class="btn small" href="/case-study/?slug=smart-meal-planner">View case study →</a>
                    </div>
                </div>
                <div class="card exp-card">
                    <div class="exp-logo">CI</div>
                    <div>
                        <h3 style="font:700 1.2rem var(--display);margin:0 0 4px;">Child Friendly City Index</h3>
                        <p style="color:var(--muted);font-size:.86rem;margin:0 0 10px;">Independent project development · May 2026 – Present</p>
                        <a class="btn small" href="/case-study/?slug=child-friendly-city-index">View case study →</a>
                    </div>
                </div>
            </div>
            <p class="placeholder" style="margin-top:24px;">Activity status for HifzAI, ReNaz and other Imadi Technologies products is being confirmed before listing here.</p>
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
            <p>You don't need to know which technology fits — describe the challenge and we'll work out the right approach together.</p>
        </section>

        <section class="wrap section reveal">
            <div class="card feature center" style="padding:56px 40px;text-align:center;">
                <p style="color:var(--muted);max-width:520px;margin:0 auto 28px;">Best way to reach me is on LinkedIn, or through Imadi Technologies.</p>
                <div style="display:flex;justify-content:center;gap:14px;flex-wrap:wrap;">
                    <a class="btn primary" href="https://www.linkedin.com/in/maria-aziz-ai/" target="_blank" rel="noopener">LinkedIn ↗</a>
                    <a class="btn" href="https://imadi-technologies.com" target="_blank" rel="noopener">Imadi Technologies ↗</a>
                </div>
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
            </div>
        </section>
        <section class="wrap" style="padding:20px 0 60px;">
            <div class="card" style="padding:8px 40px;">
                <div class="case-section"><h2>01. The Problem</h2><p id="case-problem"></p></div>
                <div class="case-section" id="case-challenge-section" hidden><h2>02. The Challenge</h2><p id="case-challenge"></p></div>
                <div class="case-section"><h2>03. The Solution</h2><p id="case-solution"></p></div>
                <div class="case-section"><h2>04. My Role</h2><p id="case-role"></p></div>
                <div class="case-section" id="case-tech-section" hidden><h2>05. Technology</h2><div class="chip-row" id="case-technology"></div></div>
                <div class="case-section" id="case-architecture-section" hidden><h2>06. Architecture</h2><div class="workflow-steps" id="case-architecture"></div><p class="placeholder" id="case-architecture-note" style="margin-top:12px;" hidden></p></div>
                <div class="case-section" id="case-innovation-section" hidden><h2>07. Innovation</h2><p id="case-innovation"></p></div>
                <div class="case-section"><h2>08. Results</h2><p id="case-results"></p></div>
                <div class="case-section" id="case-evidence-section" hidden><h2>09. Evidence</h2><div class="evidence-list" id="case-evidence"></div></div>
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
            var placeholder = function (text) {
                var span = document.createElement('span');
                span.className = 'placeholder';
                span.textContent = text;
                return span;
            };
            var setText = function (id, value, fallback) {
                var el = document.getElementById(id);
                if (!el) return;
                if (value) { el.textContent = value; }
                else { el.innerHTML = ''; el.appendChild(placeholder(fallback)); }
            };

            if (!project) {
                document.getElementById('case-title').textContent = 'Case study not found';
                document.getElementById('case-tagline').textContent = 'Case study';
                return;
            }

            document.title = project.name + ' | Maria Aziz';
            document.getElementById('case-title').textContent = project.name;
            document.getElementById('case-tagline').textContent = project.tagline;
            var statusEl = document.getElementById('case-status');
            statusEl.textContent = project.status;
            statusEl.setAttribute('data-status', project.status);

            setText('case-problem', project.problem, 'Problem statement to be added.');
            if (project.challenge) {
                document.getElementById('case-challenge-section').hidden = false;
                setText('case-challenge', project.challenge, '');
            }
            setText('case-solution', project.solution, 'Solution summary to be added.');
            setText('case-role', project.myRole, 'To be confirmed.');
            setText('case-results', project.resultsNote || project.results, 'No measurable results are published yet for this project. This section will be updated once real, verified figures are available — nothing here is estimated.');

            if (project.technology && project.technology.length) {
                document.getElementById('case-tech-section').hidden = false;
                var techRow = document.getElementById('case-technology');
                project.technology.forEach(function (t) {
                    var chip = document.createElement('span');
                    chip.className = 'chip';
                    chip.textContent = t;
                    techRow.appendChild(chip);
                });
            }

            if (project.architecture && project.architecture.length) {
                document.getElementById('case-architecture-section').hidden = false;
                var archRow = document.getElementById('case-architecture');
                project.architecture.forEach(function (step) {
                    var box = document.createElement('span');
                    box.className = 'workflow-step';
                    box.textContent = step;
                    archRow.appendChild(box);
                });
                if (project.architectureNote) {
                    var note = document.getElementById('case-architecture-note');
                    note.hidden = false;
                    note.textContent = project.architectureNote;
                }
            }

            if (project.innovation) {
                document.getElementById('case-innovation-section').hidden = false;
                setText('case-innovation', project.innovation, '');
            }

            if (project.evidence && project.evidence.length) {
                document.getElementById('case-evidence-section').hidden = false;
                var evRow = document.getElementById('case-evidence');
                project.evidence.forEach(function (ev) {
                    var a = document.createElement('a');
                    a.href = ev.href;
                    a.target = '_blank';
                    a.rel = 'noopener';
                    a.textContent = ev.label + ' ↗';
                    evRow.appendChild(a);
                });
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
SITE_URL_PLACEHOLDER = "https://REPLACE-WITH-YOUR-DOMAIN"
sitemap_paths = ["/", "/about/", "/work/", "/solutions/", "/research/", "/writing/", "/recognition/", "/now/", "/contact/"]
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
print("NOTE: sitemap.xml and robots.txt use a placeholder domain (" + SITE_URL_PLACEHOLDER + ") — update once this site has real hosting.")
