// Shared behavior for every page: mobile menu, reveal-on-scroll, footer year.
(function () {
    var yearEl = document.getElementById('year');
    if (yearEl) yearEl.textContent = new Date().getFullYear();

    var revealEls = document.querySelectorAll('.reveal');
    if ('IntersectionObserver' in window) {
        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('in');
                    io.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12 });
        revealEls.forEach(function (el) { io.observe(el); });
    } else {
        revealEls.forEach(function (el) { el.classList.add('in'); });
    }

    var menuToggle = document.getElementById('menuToggle');
    if (menuToggle) {
        menuToggle.addEventListener('click', function () {
            var navlinks = document.querySelector('.navlinks');
            if (!navlinks) return;
            var isOpen = navlinks.style.display === 'flex';
            navlinks.style.cssText = isOpen
                ? ''
                : 'display:flex;flex-direction:column;position:absolute;top:76px;left:0;right:0;background:rgba(7,17,31,.97);padding:20px 24px;gap:16px;border-bottom:1px solid rgba(211,229,255,.13)';
        });
    }
})();
