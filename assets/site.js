// Shared behavior for every page: footer year, theme toggle, cursor spotlight.
(function () {
    var yearEl = document.getElementById('year');
    if (yearEl) yearEl.textContent = new Date().getFullYear();

    var root = document.documentElement;
    var toggle = document.getElementById('themeToggle');
    if (toggle) {
        toggle.addEventListener('click', function () {
            var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
            root.setAttribute('data-theme', next);
            try { localStorage.setItem('theme', next); } catch (e) { }
        });
    }



    // Analytics-ready events: connect a real Google Tag Manager / Google Ads ID before launch.
    window.dataLayer = window.dataLayer || [];
    function trackPortfolioEvent(name, detail) {
        var event = Object.assign({ event: name, page_path: location.pathname }, detail || {});
        window.dataLayer.push(event);
        window.dispatchEvent(new CustomEvent('imadi:conversion-event', { detail: event }));
    }
    document.querySelectorAll('[data-track]').forEach(function (el) {
        el.addEventListener('click', function () {
            trackPortfolioEvent('portfolio_cta_click', { cta_name: el.getAttribute('data-track'), destination: el.getAttribute('href') || '' });
        });
    });

    // Project enquiry form: "Send Enquiry" emails the details to Maria (via FormSubmit,
    // no server of our own needed); "Send on WhatsApp" opens WhatsApp with the same text.
    // FormSubmit sends a one-time "Activate" email to ENQUIRY_EMAIL on the first enquiry.
    var ENQUIRY_EMAIL = 'maria@imadi.tech';
    var ENQUIRY_WHATSAPP = '923153205484';
    var enquiryForm = document.getElementById('projectEnquiryForm');
    if (enquiryForm) {
        var status = document.getElementById('enquiryStatus');
        var sendBtn = document.getElementById('enquirySend');
        var waBtn = document.getElementById('enquiryWhatsApp');
        var sending = false;

        function readEnquiry() {
            var values = new FormData(enquiryForm);
            var get = function (k, d) { return String(values.get(k) || d || '').trim(); };
            return {
                name: get('name'), email: get('email'), service: get('service'),
                budget: get('budget', 'Not specified'), message: get('message'), honey: get('_honey')
            };
        }
        function enquiryText(v) {
            return [
                'Name: ' + v.name,
                'Email: ' + v.email,
                'Service: ' + v.service,
                'Budget: ' + v.budget,
                '',
                'Project details:', v.message,
                '',
                'Sent from the imadi.tech project enquiry form.'
            ].join('\n');
        }
        function say(text, ok) {
            if (!status) return;
            status.textContent = text;
            status.style.color = ok === false ? 'var(--red, #c0392b)' : '';
        }

        enquiryForm.addEventListener('submit', function (event) {
            event.preventDefault();
            if (sending || !enquiryForm.reportValidity()) return;
            var v = readEnquiry();
            if (v.honey) return; // filled only by spam bots
            sending = true;
            if (sendBtn) sendBtn.disabled = true;
            say('Sending your enquiry…');
            fetch('https://formsubmit.co/ajax/' + ENQUIRY_EMAIL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
                body: JSON.stringify({
                    name: v.name,
                    email: v.email,
                    service: v.service,
                    budget: v.budget,
                    message: v.message,
                    _subject: 'Project enquiry from ' + v.name + ' — ' + v.service,
                    _replyto: v.email,
                    _template: 'table'
                })
            })
                .then(function (r) { return r.json().catch(function () { return {}; }).then(function (d) { return { ok: r.ok, d: d }; }); })
                .then(function (res) {
                    if (!res.ok || String(res.d.success) !== 'true') throw new Error(res.d.message || 'not sent');
                    say('Thank you, ' + v.name + '. Your enquiry has been sent and I will get back to you soon.');
                    trackPortfolioEvent('project_enquiry_sent', { service: v.service });
                    enquiryForm.reset();
                })
                .catch(function () {
                    say('Sorry, the form could not send right now. Please use "Send on WhatsApp" or email ' + ENQUIRY_EMAIL + '.', false);
                })
                .then(function () { sending = false; if (sendBtn) sendBtn.disabled = false; });
        });

        if (waBtn) {
            waBtn.addEventListener('click', function () {
                if (!enquiryForm.reportValidity()) return;
                var v = readEnquiry();
                trackPortfolioEvent('project_enquiry_whatsapp', { service: v.service });
                window.open('https://wa.me/' + ENQUIRY_WHATSAPP + '?text=' + encodeURIComponent('Hi Maria, I have a project enquiry.\n\n' + enquiryText(v)), '_blank', 'noopener');
            });
        }
    }

    var spot = document.getElementById('spotlight');
    var fine = window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches;
    var calm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (spot && fine && !calm) {
        var raf = null, x = 0, y = 0;
        window.addEventListener('mousemove', function (e) {
            x = e.clientX; y = e.clientY;
            if (raf) return;
            raf = requestAnimationFrame(function () {
                spot.style.setProperty('--mx', x + 'px');
                spot.style.setProperty('--my', y + 'px');
                spot.classList.add('on');
                raf = null;
            });
        });
        document.addEventListener('mouseleave', function () { spot.classList.remove('on'); });
    }
})();
