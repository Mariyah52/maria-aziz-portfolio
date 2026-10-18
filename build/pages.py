#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate import page, write

import json as _json, re as _re
_pd = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "projects-data.js"), encoding="utf-8").read()
PLAIN = _json.loads(_re.search(r"window\.PLAIN = (\{.*?\n\});", _pd, _re.S).group(1))
_NAMES = dict(_re.findall(r'slug: "([^"]+)",\s*name: "([^"]+)"', _pd))
_CLIENTS = dict((m[0], m[1]) for m in _re.findall(r'slug: "([^"]+)",[\s\S]*?client: "([^"]+)"', _pd))

def ps_card(slug):
    x = PLAIN[slug]
    return (f'<a class="card ps-card" href="/case-study/?slug={slug}">'
            f'<h3>{_NAMES[slug]}</h3><div class="project-client">{_CLIENTS.get(slug, "")}</div>'
            f'<div class="ps"><p><b class="ps-l ps-p">Problem</b>{x["problem"]}</p>'
            f'<p><b class="ps-l ps-s">Solution</b>{x["solution"]}</p></div>'
            f'<span class="arrow">Read the case study →</span></a>')

HOME_SOLVED = "".join(ps_card(s_) for s_ in ["alico", "uk-logistics-whatsapp", "company-monitor", "renaz", "uk-logistics-erp", "hercommerce"])

# ---------------------------------------------------------------- HOME -----
home_body = """
        <section class="wrap hero-grid reveal">
            <div>
                <div class="eyebrow">Maria Aziz</div>
                <h1 style="font:700 clamp(2.4rem,5.6vw,4.2rem)/1.05 var(--display);letter-spacing:-.03em;margin:8px 0 20px;">AI Product Founder<br>&amp; Technology Entrepreneur</h1>
                <p style="color:var(--muted);font-size:1.12rem;max-width:560px;margin:0 0 18px;">Full-Stack AI Engineer &amp; SaaS Builder with a proven track record of architecting, building, and deploying 6 production-ready client platforms across the UK, Kenya, and Pakistan in under a year. Expert in Python, React, LLM integration, and enterprise-grade automation.</p>
                <p style="color:var(--body);max-width:580px;margin:0 0 30px;">My work begins with understanding the problem. I analyse workflows, users and operational challenges, then design practical technology solutions that can be built, tested and improved.</p>
                <div class="hero-actions">
                    <a class="btn primary" href="/contact/?source=homepage" data-track="primary_cta">Discuss Your Project <span aria-hidden="true">↗</span></a>
                    <a class="btn" href="/work/">Explore Case Studies</a>
                    <a class="btn" href="https://wa.me/923421393991?text=Hi%20Marist!" target="_blank" rel="noopener">Say Hi to Marist</a>
                </div>
                <p class="hero-note">From workflow discovery to a tested, practical solution.</p>
            </div>
        </section>

        <section class="wrap section reveal">
            <a class="card marist-card" href="https://wa.me/923421393991?text=Hi%20Marist!" target="_blank" rel="noopener" style="text-decoration:none;">
                <div class="marist-icon"><svg viewBox="0 0 24 24" aria-hidden="true" width="20" height="20"><path fill="currentColor" d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48-.89-.79-1.49-1.77-1.66-2.07-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.21 3.08c.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.69.63.71.23 1.36.2 1.87.12.57-.09 1.76-.72 2.01-1.41.25-.69.25-1.29.17-1.41-.07-.12-.27-.2-.57-.35M12.05 21.5h-.01a9.4 9.4 0 0 1-4.8-1.31l-.34-.2-3.57.94.95-3.48-.22-.36A9.4 9.4 0 0 1 2.6 12C2.6 6.8 6.84 2.56 12.06 2.56c2.52 0 4.9.99 6.68 2.77A9.38 9.38 0 0 1 21.5 12c0 5.2-4.24 9.44-9.45 9.44M20.1 3.9A11.3 11.3 0 0 0 12.05.6C5.78.6.67 5.71.67 12c0 2 .52 3.97 1.52 5.7L.57 23.4l5.83-1.53A11.4 11.4 0 0 0 12.04 23.4h.01c6.27 0 11.38-5.11 11.38-11.4 0-3.04-1.18-5.9-3.33-8.1"/></svg></div>
                <div>
                    <div class="eyebrow">My AI chat buddy</div>
                    <h3 style="font:700 1.25rem var(--display);margin:0 0 6px;">Say hi to Marist on WhatsApp ↗</h3>
                    <p style="color:var(--muted);margin:0 0 6px;">Marist is an AI chat buddy I built in my free time. It chats in Roman Urdu and loves sharing a little motivation. Say hi any time.</p>
                    <p style="color:var(--body);margin:0;font-weight:600;">+92 342 1393991</p>
                </div>
            </a>
        </section>

        <section class="wrap section reveal" style="padding-top:0;">
            <div class="stat-band">
                <div class="stat"><span class="stat-num">6</span><span class="stat-label">Client platforms built</span></div>
                <div class="stat"><span class="stat-num">5</span><span class="stat-label">Live in daily use</span></div>
                <div class="stat"><span class="stat-num">3</span><span class="stat-label">Countries: Pakistan, UK, Kenya</span></div>
                <div class="stat"><span class="stat-num">358</span><span class="stat-label">Automated tests on one ERP</span><span class="stat-note">Checks that run automatically after every change</span></div>
            </div>
        </section>

        <section class="wrap section reveal">
            <div class="section-head">
                <div class="eyebrow">Problems I've solved</div>
                <h2>The Problem, and What I Built</h2>
                <p class="section-intro">Every project starts with a real business problem. Here is what each client was struggling with, and how the solution changed their day.</p>
            </div>
            <div class="grid two">__HOME_SOLVED__</div>
            <p style="margin-top:18px;"><a class="btn" href="/work/">See all projects →</a></p>
        </section>

        <section class="wrap section reveal">
            <div class="section-head">
                <div class="eyebrow">What I do</div>
                <h2>From Problems to Technology Solutions</h2>
            </div>
            <div class="grid three">
                <div class="card project-card"><div class="project-icon">✦</div><h3>AI-Powered Products</h3><p>Products designed so intelligence solves a real workflow problem, not just a demo.</p></div>
                <div class="card project-card"><div class="project-icon">↻</div><h3>Intelligent Automation</h3><p>Removing repetitive, manual steps so teams spend time on judgement, not data entry.</p></div>
                <div class="card project-card"><div class="project-icon">◇</div><h3>Chatbots &amp; Conversational Systems</h3><p>Conversational interfaces that meet people where they already are, like WhatsApp.</p></div>
                <div class="card project-card"><div class="project-icon">◌</div><h3>Machine Learning &amp; NLP</h3><p>Applying ML and NLP where it genuinely improves a decision or an understanding of language.</p></div>
                <div class="card project-card"><div class="project-icon">▣</div><h3>Scalable SaaS Platforms</h3><p>Multi-tenant products built for a team's real workflow, not a single user's.</p></div>
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
"""

home_extra = """    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Person",
      "name": "Maria Aziz",
      "jobTitle": "AI Product Founder & Technology Entrepreneur",
      "sameAs": ["https://www.linkedin.com/in/maria-aziz-ai/", "https://github.com/Mariyah52"]
    }
    </script>
"""

home_body = home_body.replace("__HOME_SOLVED__", HOME_SOLVED)
write("/index.html", page(
    "Maria Aziz | AI Product Founder & Technology Entrepreneur",
    "Maria Aziz builds AI-powered products, intelligent automation, conversational systems and scalable SaaS solutions for real-world problems.",
    "/",
    home_body,
    extra_head=home_extra,
))

# ---------------------------------------------------------------- ABOUT ----
about_body = """
        <section class="wrap page-hero reveal">
            <div class="eyebrow">About</div>
            <h1>Maria Aziz</h1>
            <p style="font-weight:700;color:var(--ink);font-size:1.15rem;margin:-6px 0 20px;">AI Product Founder &amp; Technology Entrepreneur</p>
            <p>I build practical technology solutions around real-world problems, working across AI-powered products, machine learning, natural language processing, automation, conversational systems and SaaS.</p>
            <p>My approach begins with understanding the people, processes and challenges behind a problem before selecting the technology. Since May 2026, I have built six client platforms for businesses in Pakistan, the United Kingdom and Kenya, five of them live in daily use, alongside my own SaaS products.</p>
            <div style="display:flex;flex-wrap:wrap;gap:14px;color:var(--muted);font-size:.86rem;margin-top:22px;">
                <span>📍 Karachi, Sindh, Pakistan</span>
                <span>🏢 Founder &amp; AI Specialist</span>
                <span>🌍 Clients in Pakistan, UK &amp; Kenya</span>
                <span>🎓 AI/ML/DL Specialisation, IBA Karachi</span>
            </div>
        </section>

        <section class="wrap section reveal">
            <div class="section-head"><div class="eyebrow">Experience</div><h2>Founder &amp; AI Specialist</h2></div>
            <p class="section-intro">May 2026 – Present · Karachi, Pakistan. I build AI-powered business software, WhatsApp automation and SaaS products for SMEs. I gather requirements directly from business owners, then design, build and deploy each system end to end.</p>
            <p style="margin-top:8px;"><a class="btn" href="/work/">See all projects →</a></p>
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
                        <span class="chip">Sentiment Analysis</span><span class="chip">Predictive Modelling</span><span class="chip">Regression &amp; Logistic Regression</span>
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
                        <span class="chip">Data Visualisation</span><span class="chip">Dashboard Building</span><span class="chip">Microsoft Power BI</span>
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
                        <h3 style="font:700 1.1rem var(--display);margin:0 0 4px;">Specialisation Certificate: Artificial Intelligence / Machine Learning / Deep Learning</h3>
                        <p style="color:var(--muted);font-size:.86rem;margin:0 0 10px;">Institute of Business Administration (IBA), Karachi · February 2026 – May 2026</p>
                        <p style="color:var(--body);font-size:.94rem;margin:0 0 12px;">Fully funded under the Prime Minister's Hunarmand Pakistan Program (NAVTTC). Machine learning, deep learning and NLP pipelines with scikit-learn, TensorFlow, PyTorch and Keras.</p>
                    </div>
                </div>
                <div class="card exp-card">
                    <div class="exp-logo">KU</div>
                    <div>
                        <h3 style="font:700 1.1rem var(--display);margin:0 0 4px;">Bachelor of Public Administration (BSPA, BS 4-year)</h3>
                        <p style="color:var(--muted);font-size:.86rem;margin:0 0 10px;">University of Karachi · January 2024 – December 2025 · CGPA 3.37 / 4.00</p>
                        <p style="color:var(--body);font-size:.94rem;margin:0 0 12px;">16 years of education. Statistics, research methodology, Power BI, logistics and supply chain management, and public policy.</p>
                    </div>
                </div>
                <div class="card exp-card">
                    <div class="exp-logo">KU</div>
                    <div>
                        <h3 style="font:700 1.1rem var(--display);margin:0 0 4px;">Bachelor of Arts (Psychology)</h3>
                        <p style="color:var(--muted);font-size:.86rem;margin:0 0 10px;">University of Karachi · November 2009 – December 2011 · 69.32%</p>
                        <p style="color:var(--body);font-size:.94rem;margin:0 0 12px;">14 years of education.</p>
                    </div>
                </div>
            </div>
            <div class="card" style="margin-top:24px;">
                <p style="color:var(--body);margin:0;">A background in public administration and psychology alongside a technical AI specialisation gives me a working understanding of how organisations, operations and people actually function, which shapes how I design technology for real-world use, not just the technology in isolation.</p>
            </div>
        </section>

        <section class="wrap section reveal">
            <div class="section-head"><div class="eyebrow">Certifications</div><h2>Selected Certifications</h2></div>
            <div class="grid three">
                <div class="card">
                    <h3 style="font:700 1.02rem var(--display);margin:0 0 12px;">AI &amp; Data</h3>
                    <ul style="margin:0;padding-left:18px;color:var(--body);font-size:.88rem;display:grid;gap:5px;">
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
                    <ul style="margin:0;padding-left:18px;color:var(--body);font-size:.88rem;display:grid;gap:5px;">
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
                    <ul style="margin:0;padding-left:18px;color:var(--body);font-size:.88rem;display:grid;gap:5px;">
                        <li>Search Engine Optimization (SEO) with Squarespace — Coursera</li>
                        <li>Use Canva to Design Digital Course Collateral — Coursera</li>
                        <li>Start Writing Prompts like a Pro — Google</li>
                    </ul>
                </div>
            </div>
            <p style="color:var(--muted);font-size:.84rem;margin-top:16px;">A full list of licences and certifications (21 total) is available on LinkedIn.</p>
        </section>

        <section class="wrap section reveal">
            <div class="section-head"><div class="eyebrow">Conference Paper · 2024</div><h2>Exploring the Psychological Puzzle of Travelling: A Journey Through Your Thoughts</h2></div>
            <div class="card">
                <div class="grid two" style="margin-bottom:18px;">
                    <div><p style="color:var(--muted);font-size:.78rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 4px;">Author</p><p style="color:var(--body);margin:0;">Maria Aziz</p></div>
                    <div><p style="color:var(--muted);font-size:.78rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 4px;">Role</p><p style="color:var(--body);margin:0;">Research Scholar, Department of Public Administration, University of Karachi</p></div>
                    <div><p style="color:var(--muted);font-size:.78rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 4px;">Conference</p><p style="color:var(--body);margin:0;">National Conference on Managing Mega Cities (NCMC), Department of Public Administration, University of Karachi</p></div>
                    <div><p style="color:var(--muted);font-size:.78rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 4px;">Date</p><p style="color:var(--body);margin:0;">14–15 May 2024</p></div>
                </div>
                <p style="color:var(--muted);font-size:.78rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 4px;">Summary</p>
                <p style="color:var(--body);margin:0 0 12px;">Explores the psychological dimensions of daily commuting and travel behaviour: how routine journeys by walking, cycling, driving or public transport affect mood, stress, attention and reflective thinking.</p>
                <ul style="margin:0;padding-left:18px;color:var(--body);display:grid;gap:5px;">
                    <li>The interplay between the mind and daily travel routines</li>
                    <li>How traffic jams, delays and crowded transport drive stress and annoyance</li>
                    <li>Moments of calm and self-reflection on familiar routes</li>
                    <li>Implications for urban mobility and well-being in mega cities</li>
                </ul>
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
            <h1>Problems I've Solved</h1>
            <p>For every project: the problem in one line, and what I built to solve it.</p>
        </section>

        <div id="work-groups" aria-live="polite">
            <section class="wrap section"><div class="card"><h2>Loading selected projects…</h2><p>If projects do not appear, check that JavaScript is enabled and reload this page.</p></div></section>
        </div>
"""
work_scripts = """    <script src="/assets/projects-data.js"></script>
    <script>
        (function () {
            var root = document.getElementById('work-groups');
            if (!root || !window.PROJECTS) return;
            var fallback = root.querySelector('.card'); if (fallback) fallback.remove();

            var GROUPS = [
                { title: 'Client Work', intro: 'Real businesses, real problems, systems in daily use.', slugs: ['alico', 'uk-logistics-erp', 'uk-logistics-whatsapp', 'renaz', 'company-monitor', 'shah'] },
                { title: 'My Own Products', intro: 'Products I built for problems I saw around me.', slugs: ['hercommerce', 'child-friendly-city-index'] },
                { title: 'Hobby Projects', intro: 'What I build, write and try out in my free time, to learn, to experiment and sometimes just for fun.', slugs: ['marist-bot', 'overthinking-journal', 'smart-meal-planner', 'ml-pipeline', 'nlp-sentiment-analysis'], compact: true }
            ];

            GROUPS.forEach(function (g) {
                var section = document.createElement('section');
                section.className = 'wrap section';
                var head = document.createElement('div');
                head.className = 'section-head';
                head.innerHTML = '<h2></h2><p class="section-intro"></p>';
                head.firstChild.textContent = g.title;
                head.lastChild.textContent = g.intro || '';
                var grid = document.createElement('div');
                grid.className = 'grid two';

                g.slugs.forEach(function (slug) {
                    var p = window.getProjectBySlug(slug);
                    if (!p) return;
                    var a = document.createElement('a');
                    a.href = '/case-study/?slug=' + encodeURIComponent(p.slug);
                    a.className = 'card project-card';
                    var prob = p.plainProblem || p.problem || '', sol = p.plainSolution || p.solution || '';
                    if (g.compact) {
                        a.className = 'card project-card hobby-card';
                        a.innerHTML =
                            '<div class="project-status" data-status="' + p.status + '">' + p.status + '</div>' +
                            '<h3>' + p.name + '</h3>' +
                            '<p>' + (p.hobby || sol) + '</p>' +
                            '<span class="arrow">More →</span>';
                        grid.appendChild(a);
                        return;
                    }
                    a.className = 'card project-card ps-card';
                    a.innerHTML =
                        '<div class="project-status" data-status="' + p.status + '">' + p.status + '</div>' +
                        '<h3>' + p.name + '</h3>' + (p.client ? '<div class="project-client">' + p.client + '</div>' : '') +
                        '<div class="ps">' + (prob ? '<p><b class="ps-l ps-p">Problem</b>' + prob + '</p>' : '') +
                        (sol ? '<p><b class="ps-l ps-s">Solution</b>' + sol + '</p>' : '') + '</div>' +
                        (p.letter ? '<span class="letter-badge">\u2713 Client letter</span>' : '') +
                        '<span class="arrow">Read the case study →</span>';
                    grid.appendChild(a);
                });

                section.appendChild(head);
                section.appendChild(grid);
                root.appendChild(section);
            });
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

# ---------------------------------------------------------------- CONTACT -
contact_body = """
        <section class="wrap page-hero reveal">
            <div class="eyebrow">Contact</div>
            <h1>Tell Me Your Problem.</h1>
            <p>You don't need to know which technology fits. Describe the challenge and we'll work out the right approach together.</p>
            <div class="hero-actions"><a class="btn primary" href="#project-enquiry" data-track="contact_cta">Start a Project Enquiry</a><a class="btn" href="mailto:maria@imadi.tech">Email Directly</a></div>
        </section>

        <section class="wrap section reveal">
            <a class="card marist-card" href="https://wa.me/923421393991?text=Hi%20Marist!" target="_blank" rel="noopener" style="text-decoration:none;">
                <div class="marist-icon"><svg viewBox="0 0 24 24" aria-hidden="true" width="20" height="20"><path fill="currentColor" d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48-.89-.79-1.49-1.77-1.66-2.07-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.21 3.08c.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.69.63.71.23 1.36.2 1.87.12.57-.09 1.76-.72 2.01-1.41.25-.69.25-1.29.17-1.41-.07-.12-.27-.2-.57-.35M12.05 21.5h-.01a9.4 9.4 0 0 1-4.8-1.31l-.34-.2-3.57.94.95-3.48-.22-.36A9.4 9.4 0 0 1 2.6 12C2.6 6.8 6.84 2.56 12.06 2.56c2.52 0 4.9.99 6.68 2.77A9.38 9.38 0 0 1 21.5 12c0 5.2-4.24 9.44-9.45 9.44M20.1 3.9A11.3 11.3 0 0 0 12.05.6C5.78.6.67 5.71.67 12c0 2 .52 3.97 1.52 5.7L.57 23.4l5.83-1.53A11.4 11.4 0 0 0 12.04 23.4h.01c6.27 0 11.38-5.11 11.38-11.4 0-3.04-1.18-5.9-3.33-8.1"/></svg></div>
                <div>
                    <div class="eyebrow">My AI chat buddy</div>
                    <h3 style="font:700 1.25rem var(--display);margin:0 0 6px;">Say hi to Marist on WhatsApp ↗</h3>
                    <p style="color:var(--muted);margin:0 0 6px;">Marist is an AI chat buddy I built in my free time. It chats in Roman Urdu and loves sharing a little motivation. Say hi any time.</p>
                    <p style="color:var(--body);margin:0;font-weight:600;">+92 342 1393991</p>
                </div>
            </a>
        </section>

        <section class="wrap section reveal" id="project-enquiry">
            <div class="card enquiry-card">
                <div class="eyebrow">Project enquiry</div>
                <h2>What would you like to improve?</h2>
                <p class="section-intro">Share a little context. This form prepares an email in your email app; it does not send information to a server.</p>
                <form id="projectEnquiryForm" class="enquiry-form">
                    <div class="form-grid">
                        <label>Your name <span aria-hidden="true">*</span><input name="name" autocomplete="name" required maxlength="100" /></label>
                        <label>Business email <span aria-hidden="true">*</span><input name="email" type="email" autocomplete="email" required maxlength="180" /></label>
                        <label>What do you need help with? <span aria-hidden="true">*</span>
                            <select name="service" required>
                                <option value="" selected disabled>Select a service</option>
                                <option>Business process automation</option><option>WhatsApp / conversational systems</option><option>ERP or custom business software</option><option>AI product or assistant</option><option>SaaS / web application</option><option>Data analytics / machine learning</option><option>Not sure yet</option>
                            </select>
                        </label>
                        <label>Project budget (optional)
                            <select name="budget"><option value="Not specified" selected>Prefer to discuss</option><option>Under $1,000</option><option>$1,000–$5,000</option><option>$5,000–$15,000</option><option>$15,000+</option></select>
                        </label>
                        <label class="form-wide">Tell me about the problem <span aria-hidden="true">*</span><textarea name="message" rows="5" required maxlength="3000" placeholder="What is happening today, and what would a better outcome look like?"></textarea></label>
                    </div>
                    <label class="consent-line"><input type="checkbox" name="consent" required /> I agree that the details I enter can be included in an email to respond to this enquiry.</label>
                    <button class="btn primary" type="submit">Prepare My Enquiry Email <span aria-hidden="true">↗</span></button>
                    <p id="enquiryStatus" class="form-status" role="status" aria-live="polite">Your email app will open with your enquiry filled in. Review and send it there.</p>
                </form>
            </div>
        </section>

        <section class="wrap section reveal">
            <div class="grid two">
                <a class="card" href="mailto:maria@imadi.tech" style="text-decoration:none;">
                    <div class="eyebrow">Email</div>
                    <h3 style="font:700 1.15rem var(--display);margin:0 0 6px;">maria@imadi.tech</h3>
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
            </div>
        </section>

        <section class="wrap section reveal">
            <div class="section-head"><div class="eyebrow">Solutions</div><h2>Where I Can Help</h2><p class="section-intro">Start from the problem, not the technology. Here are the kinds of challenges I work on most often.</p></div>
            <div class="grid two">
                <div class="card"><div class="eyebrow">Business Operations</div>
                    <p style="color:var(--muted);font-size:.82rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 6px;">Problem</p>
                    <p style="color:var(--body);margin:0 0 16px;">Manual workflows and repetitive processes.</p>
                    <p style="color:var(--muted);font-size:.82rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 6px;">Potential solutions</p>
                    <p style="color:var(--body);margin:0;">Automation, dashboards and integrated systems.</p>
                </div>
                <div class="card"><div class="eyebrow">Customer Communication</div>
                    <p style="color:var(--muted);font-size:.82rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 6px;">Problem</p>
                    <p style="color:var(--body);margin:0 0 16px;">Teams spend time responding to repetitive enquiries.</p>
                    <p style="color:var(--muted);font-size:.82rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 6px;">Potential solutions</p>
                    <p style="color:var(--body);margin:0;">Chatbots and conversational automation.</p>
                </div>
                <div class="card"><div class="eyebrow">Data &amp; Decision Making</div>
                    <p style="color:var(--muted);font-size:.82rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 6px;">Problem</p>
                    <p style="color:var(--body);margin:0 0 16px;">Organisations have data but lack useful insights.</p>
                    <p style="color:var(--muted);font-size:.82rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 6px;">Potential solutions</p>
                    <p style="color:var(--body);margin:0;">Analytics, dashboards and machine learning.</p>
                </div>
                <div class="card"><div class="eyebrow">Education Technology</div>
                    <p style="color:var(--muted);font-size:.82rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 6px;">Problem</p>
                    <p style="color:var(--body);margin:0 0 16px;">Learning and progress tracking can be fragmented.</p>
                    <p style="color:var(--muted);font-size:.82rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 6px;">Potential solutions</p>
                    <p style="color:var(--body);margin:0;">AI-powered learning platforms and SaaS.</p>
                </div>
                <div class="card"><div class="eyebrow">Logistics &amp; Operations</div>
                    <p style="color:var(--muted);font-size:.82rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 6px;">Problem</p>
                    <p style="color:var(--body);margin:0 0 16px;">Disconnected and manual operational workflows.</p>
                    <p style="color:var(--muted);font-size:.82rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 6px;">Potential solutions</p>
                    <p style="color:var(--body);margin:0;">Digital workflows, automation and intelligent systems.</p>
                </div>
                <div class="card"><div class="eyebrow">Community &amp; Social Impact</div>
                    <p style="color:var(--muted);font-size:.82rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 6px;">Problem</p>
                    <p style="color:var(--body);margin:0 0 16px;">Complex public and community challenges need better digital tools.</p>
                    <p style="color:var(--muted);font-size:.82rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin:0 0 6px;">Potential solutions</p>
                    <p style="color:var(--body);margin:0;">Research-driven platforms, data systems and technology solutions.</p>
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
            <h1 id="case-title">Loading project details…</h1>
            <p id="case-loading-help" class="case-loading-help">Project details are taking longer than expected. <a href="/work/">Return to all projects</a> or <a href="/contact/">contact Maria directly</a>.</p>
            <div class="case-hero-meta">
                <span class="project-status" id="case-status" data-status="">Status</span>
                <span class="case-meta" id="case-client"></span>
                <span class="case-meta" id="case-period"></span>
            </div>
        </section>
        <section class="wrap" id="case-short" hidden style="padding:16px 0 0;">
            <div class="card ps-card ps-short">
                <div class="eyebrow">In short</div>
                <div class="ps"><p><b class="ps-l ps-p">Problem</b><span id="short-problem"></span></p><p><b class="ps-l ps-s">Solution</b><span id="short-solution"></span></p></div>
            </div>
        </section>
        <section class="wrap section" id="case-letter" hidden style="padding-bottom:0;">
            <div class="section-head"><div class="eyebrow">Client letter</div><h2>In the client's words</h2></div>
            <div class="card letter-card">
                <a class="letter-thumb" id="letter-link" href="#" target="_blank" rel="noopener"><img id="letter-img" alt="Letter from the client confirming delivery" loading="lazy"></a>
                <div>
                    <blockquote id="letter-quote"></blockquote>
                    <p class="letter-by"><strong id="letter-name"></strong><span id="letter-role"></span></p>
                    <p class="letter-note">Signed and stamped letter confirming the software was developed and delivered<span id="letter-date"></span>. Commercial terms are withheld.</p>
                    <a class="btn small" id="letter-open" href="#" target="_blank" rel="noopener">View full letter ↗</a>
                </div>
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
    <script src="/assets/media-data.js"></script>
    <script src="/assets/media-loader.js"></script>
    <script>
        (function () {
            var slug = new URLSearchParams(location.search).get('slug');
            var project = slug ? window.getProjectBySlug(slug) : null;
            if (!project) {
                document.getElementById('case-title').textContent = 'Case study not found';
                var missing = document.getElementById('case-loading-help'); if (missing) missing.hidden = false;
                return;
            }
            document.title = project.name + ' | Maria Aziz';
            document.getElementById('case-title').textContent = project.name;
            var loadingHelp = document.getElementById('case-loading-help'); if (loadingHelp) loadingHelp.hidden = true;
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
            if (project.plainProblem) {
                document.getElementById('short-problem').textContent = project.plainProblem;
                document.getElementById('short-solution').textContent = project.plainSolution || '';
                document.getElementById('case-short').hidden = false;
            }
            if (project.letter) {
                var L = project.letter;
                document.getElementById('letter-img').src = L.image;
                document.getElementById('letter-link').href = L.image;
                document.getElementById('letter-open').href = L.image;
                document.getElementById('letter-quote').textContent = '\u201C' + L.quote + '\u201D';
                document.getElementById('letter-name').textContent = L.name;
                document.getElementById('letter-role').textContent = L.role ? ' \u00B7 ' + L.role : '';
                document.getElementById('letter-date').textContent = L.date ? ', dated ' + L.date : '';
                document.getElementById('case-letter').hidden = false;
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
            if (window.loadMedia) window.loadMedia().then(function (m) {
                var vids = (m.videos || []).filter(function (v) { return window.mediaMatchesProject(v, project); });
                var pics = (m.photos || []).filter(function (v) { return window.mediaMatchesProject(v, project); });
                if (!vids.length && !pics.length) return;
                var sec = document.createElement('section');
                sec.className = 'wrap section reveal in';
                sec.innerHTML = '<div class="section-head"><div class="eyebrow">Demo</div><h2>See it in action</h2></div><div class="media-grid"></div>';
                var grid = sec.querySelector('.media-grid');
                vids.forEach(function (v) { grid.appendChild(window.mediaVideoCard({ title: v.title, caption: v.caption, src: v.src, webm: v.webm, poster: v.poster })); });
                pics.forEach(function (v) {
                    var card = document.createElement('a');
                    card.className = 'media-card media-pic'; card.href = window.mediaImageUrl(v.src); card.target = '_blank'; card.rel = 'noopener';
                    var img = document.createElement('img'); img.src = window.mediaImageUrl(v.src); img.alt = v.title || 'Demo picture'; img.loading = 'lazy';
                    var c = document.createElement('div'); c.className = 'cap';
                    var t = document.createElement('strong'); t.textContent = v.title || ''; c.appendChild(t);
                    if (v.caption) { var sp = document.createElement('span'); sp.textContent = v.caption; c.appendChild(sp); }
                    card.appendChild(img); card.appendChild(c); grid.appendChild(card);
                });
                if (pics.length && !vids.length) sec.querySelector('.media-grid').classList.add('single');
                var main = document.getElementById('main');
                var letterBox = document.getElementById('case-letter');
                var anchor = (letterBox && !letterBox.hidden) ? letterBox : document.getElementById('case-short');
                main.insertBefore(sec, anchor ? anchor.nextSibling : null);
            });
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


# ---------------------------------------------------------------- MEDIA ----
media_body = """
        <section class="wrap page-hero">
            <div class="eyebrow">Demos</div>
            <h1>Demos &amp; Work in Pictures</h1>
            <p>Short walkthroughs of the products I build, and pictures of the work in use.</p>
        </section>

        <section class="wrap section" style="padding-top:12px;">
            <div class="section-head"><h2>Demo videos</h2></div>
            <div class="add-demo" data-edit hidden>
                <a class="btn primary" id="add-demo-link" href="#" target="_blank" rel="noopener">+ Add a demo link</a>
                <span style="color:var(--muted);font-size:.86rem;">Opens your form. Paste a YouTube, LinkedIn, Loom, Vimeo or Google Drive link, submit, and refresh this page in a few minutes.</span>
            </div>
            <div class="media-grid" id="video-grid"></div>
        </section>

        <section class="wrap section">
            <div class="section-head"><h2>Work in pictures</h2></div>
            <div class="media-grid" id="photo-grid"></div>
        </section>

        <dialog class="lightbox" id="lightbox"><img alt=""><p></p></dialog>
"""
media_scripts = """    <script src="/assets/projects-data.js"></script>
    <script src="/assets/media-data.js"></script>
    <script src="/assets/media-loader.js"></script>
    <script>
        window.loadMedia().then(function (data) {
            var edit = new URLSearchParams(location.search).get('edit') === '1';
            var vGrid = document.getElementById('video-grid');
            var pGrid = document.getElementById('photo-grid');
            var box = document.getElementById('lightbox');

            if (edit) document.querySelectorAll('[data-edit]').forEach(function (el) { el.hidden = false; });
            var formBtn = document.getElementById('add-demo-link');
            if (formBtn) {
                if (window.MEDIA_FORM_URL) formBtn.href = window.MEDIA_FORM_URL;
                else { formBtn.removeAttribute('target'); formBtn.addEventListener('click', function (e) { e.preventDefault(); formBtn.textContent = 'Form link not set yet (MEDIA_FORM_URL in assets/media-data.js)'; }); }
            }

            function cap(item) {
                var c = document.createElement('div');
                c.className = 'cap';
                var t = document.createElement('strong');
                t.textContent = item.title || '';
                c.appendChild(t);
                var sub = item.caption || projectLabel(item);
                if (sub) { var s = document.createElement('span'); s.textContent = sub; c.appendChild(s); }
                return c;
            }
            function embedUrl(src) {
                var m;
                if ((m = src.match(/youtu\\.be\\/([\\w-]{6,})/)) || (m = src.match(/[?&]v=([\\w-]{6,})/)) || (m = src.match(/youtube\\.com\\/embed\\/([\\w-]{6,})/)))
                    return 'https://www.youtube-nocookie.com/embed/' + m[1];
                if ((m = src.match(/vimeo\\.com\\/(\\d+)/))) return 'https://player.vimeo.com/video/' + m[1];
                if ((m = src.match(/loom\\.com\\/(?:share|embed)\\/(\\w+)/))) return 'https://www.loom.com/embed/' + m[1];
                return null;
            }
            function projectLabel(item) {
                var p = item.project && window.getProjectBySlug ? window.getProjectBySlug(item.project.trim().toLowerCase()) : null;
                return p ? p.name : item.project;
            }
            function addVideo(item) {
                vGrid.appendChild(window.mediaVideoCard({ title: item.title, caption: item.caption, project: projectLabel(item), src: item.src, webm: item.webm, poster: item.poster }));
            }
            function addPhoto(item) {
                var card = document.createElement('div');
                card.className = 'media-card';
                var img = document.createElement('img');
                img.className = 'ph'; img.src = window.mediaImageUrl(item.src); img.alt = item.title || 'Work picture'; img.loading = 'lazy';
                img.addEventListener('click', function () {
                    box.querySelector('img').src = window.mediaImageUrl(item.src);
                    box.querySelector('img').alt = img.alt;
                    box.querySelector('p').textContent = [item.title, item.caption].filter(Boolean).join(' — ');
                    box.showModal();
                });
                card.appendChild(img);
                card.appendChild(cap(item));
                pGrid.appendChild(card);
            }
            box.addEventListener('click', function () { box.close(); });

            function empty(grid, text) {
                if (grid.children.length) return;
                var d = document.createElement('div');
                d.className = 'media-empty'; d.textContent = text;
                grid.parentNode.insertBefore(d, grid);
                grid.dataset.empty = '1';
            }
            (data.videos || []).forEach(addVideo);
            (data.photos || []).forEach(addPhoto);
            if (!edit) {
                empty(vGrid, 'Demo videos are coming soon.');
                empty(pGrid, 'Project pictures are coming soon.');
            }

        });
    </script>
"""
write("/media/index.html", page(
    "Demos | Maria Aziz",
    "Demo videos and pictures of the AI products, automation and SaaS platforms built by Maria Aziz.",
    "/media/",
    media_body,
    extra_scripts=media_scripts,
))

# ------------------------------------------------------------------ 404 ----
# Old or mistyped addresses go straight to Home instead of showing an error.
write("/404.html", page(
    "Maria Aziz",
    "Maria Aziz builds AI-powered products, intelligent automation, conversational systems and scalable SaaS solutions.",
    "/",
    """
        <section class="wrap page-hero">
            <h1>Taking you to the home page</h1>
            <p><a class="btn primary" href="/">Go to Home</a></p>
        </section>
""",
    extra_head='    <meta http-equiv="refresh" content="0; url=/">\n    <meta name="robots" content="noindex">\n',
))

# ------------------------------------------------------------ SEO FILES --
# No live domain is confirmed yet for this site. Rather than guess one, the
# sitemap uses an obvious placeholder token — find-and-replace it with the
# real domain once this site is actually hosted somewhere.
SITE_URL_PLACEHOLDER = "https://www.imadi.tech"
sitemap_paths = ["/", "/about/", "/work/", "/media/", "/contact/"]
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
