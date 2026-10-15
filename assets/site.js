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

    var enquiryForm = document.getElementById('projectEnquiryForm');
    if (enquiryForm) {
        enquiryForm.addEventListener('submit', function (event) {
            event.preventDefault();
            if (!enquiryForm.reportValidity()) return;
            var values = new FormData(enquiryForm);
            var name = String(values.get('name') || '').trim();
            var email = String(values.get('email') || '').trim();
            var service = String(values.get('service') || '').trim();
            var budget = String(values.get('budget') || 'Not specified').trim();
            var message = String(values.get('message') || '').trim();
            var subject = 'Project enquiry from ' + name + ' — ' + service;
            var body = [
                'Name: ' + name,
                'Email: ' + email,
                'Service: ' + service,
                'Budget: ' + budget,
                '',
                'Project details:', message,
                '',
                'Sent from imadi.tech project enquiry form.'
            ].join('\n');
            var mailto = 'mailto:mariyahheal92@gmail.com?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
            var status = document.getElementById('enquiryStatus');
            if (status) status.textContent = 'Your email app should open now. Review the message and press Send to submit your enquiry. If it does not open, email mariyahheal92@gmail.com directly.';
            trackPortfolioEvent('project_enquiry_email_prepared', { service: service });
            window.location.href = mailto;
        });
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
