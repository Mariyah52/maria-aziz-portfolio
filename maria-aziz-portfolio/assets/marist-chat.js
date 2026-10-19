/**
 * Marist chat box for the portfolio.
 *
 * Paste your Marist server's address below (the Render URL of marist-ai, e.g.
 * "https://marist-ai.onrender.com"). While it's empty, the "Ask Marist" button
 * simply opens WhatsApp, exactly as before.
 *
 * Marist's server must list this website in ALLOWED_ORIGINS (see its .env.example).
 */
window.MARIST_API_URL = "https://marist-ai.onrender.com";

(function () {
    var API = (window.MARIST_API_URL || '').trim().replace(/\/+$/, '');
    var fab = document.querySelector('.wa-fab');
    if (!API || !fab || !window.fetch) return;

    var WA = fab.getAttribute('href');
    var GREETING = "Hi! I'm Marist, Maria's AI assistant. What does your business do, and where are you getting stuck?";

    function sessionId() {
        var id = null;
        try { id = localStorage.getItem('marist_web_session'); } catch (e) {}
        if (!id || !/^[A-Za-z0-9_-]{8,64}$/.test(id)) {
            id = 'w_' + Math.random().toString(36).slice(2, 12) + Date.now().toString(36);
            try { localStorage.setItem('marist_web_session', id); } catch (e) {}
        }
        return id;
    }

    // The button now opens the chat box instead of WhatsApp.
    fab.setAttribute('href', '#marist-chat');
    fab.removeAttribute('target');
    fab.setAttribute('aria-haspopup', 'dialog');
    fab.setAttribute('aria-label', 'Chat with Marist, my AI assistant');
    var label = fab.querySelector('.wa-fab-text');
    if (label) label.innerHTML = '<strong>Ask Marist</strong><small>AI assistant · chat</small>';

    var box = document.createElement('section');
    box.className = 'mchat';
    box.id = 'marist-chat';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-label', 'Chat with Marist');
    box.hidden = true;
    box.innerHTML =
        '<header class="mchat-head">' +
            '<div><strong>Marist</strong><small>Maria\'s AI assistant · replies in a few seconds</small></div>' +
            '<button type="button" class="mchat-x" aria-label="Close chat">×</button>' +
        '</header>' +
        '<div class="mchat-log" aria-live="polite"></div>' +
        '<form class="mchat-form">' +
            '<input type="text" maxlength="1000" placeholder="Type your question…" aria-label="Your message" autocomplete="off">' +
            '<button type="submit">Send</button>' +
        '</form>' +
        '<p class="mchat-foot">AI can make mistakes. Prefer WhatsApp? <a href="' + WA + '" target="_blank" rel="noopener">Open WhatsApp</a></p>';
    document.body.appendChild(box);

    var log = box.querySelector('.mchat-log');
    var form = box.querySelector('.mchat-form');
    var input = form.querySelector('input');
    var send = form.querySelector('button');
    var busy = false;

    function bubble(text, who) {
        var b = document.createElement('div');
        b.className = 'mchat-msg ' + who;
        b.textContent = text;
        log.appendChild(b);
        log.scrollTop = log.scrollHeight;
        return b;
    }

    function open() {
        box.hidden = false;
        fab.classList.add('is-open');
        if (!log.children.length) bubble(GREETING, 'bot');
        setTimeout(function () { input.focus(); }, 30);
    }
    function close() {
        box.hidden = true;
        fab.classList.remove('is-open');
        fab.focus();
    }

    fab.addEventListener('click', function (e) { e.preventDefault(); box.hidden ? open() : close(); });
    box.querySelector('.mchat-x').addEventListener('click', close);
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !box.hidden) close(); });

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        var text = input.value.trim();
        if (!text || busy) return;
        busy = true; send.disabled = true;
        bubble(text, 'me');
        input.value = '';
        var wait = bubble('Marist is typing…', 'bot typing');
        fetch(API + '/api/chat/turn', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ session_id: sessionId(), message: text })
        })
            .then(function (r) {
                return r.json().catch(function () { return {}; }).then(function (d) {
                    if (r.status === 429) throw new Error(d.detail || 'Please wait a few minutes and try again.');
                    if (!r.ok || !d.reply) throw new Error('Marist is not available right now.');
                    return d.reply;
                });
            })
            .then(function (reply) { wait.className = 'mchat-msg bot'; wait.textContent = reply; })
            .catch(function (err) {
                wait.className = 'mchat-msg bot err';
                wait.textContent = (err && err.message && /wait|available/.test(err.message) ? err.message : 'Marist is not available right now.') + ' You can also reach Maria on WhatsApp.';
            })
            .then(function () { busy = false; send.disabled = false; log.scrollTop = log.scrollHeight; input.focus(); });
    });
})();
