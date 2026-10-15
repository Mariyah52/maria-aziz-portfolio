/**
 * Loads demo videos and pictures for the Demos page and the case studies.
 *
 * Two sources are merged:
 *   1. assets/media-data.js (window.MEDIA) — entries written into the code.
 *   2. A Google Sheet published as CSV (window.MEDIA_SHEET_URL) — add a row
 *      there and it appears on the site on the next page load, no code or push.
 *
 * Sheet columns (first row is the header, order does not matter):
 *   type     video | photo            (blank = video)
 *   title    Shown under the video
 *   project  Project slug or name, e.g. alico or "ALICO Business Suite"
 *            (puts the video on that project's case study page too)
 *   link     YouTube / Vimeo / Loom / Google Drive link, or a direct .mp4/.jpg URL
 *   caption  Optional short description
 *   show     Optional. Write "no" to hide a row without deleting it.
 */
(function () {
    function parseCSV(text) {
        var rows = [], row = [], cell = '', q = false;
        for (var i = 0; i < text.length; i++) {
            var c = text[i];
            if (q) {
                if (c === '"') { if (text[i + 1] === '"') { cell += '"'; i++; } else q = false; }
                else cell += c;
            } else if (c === '"') q = true;
            else if (c === ',') { row.push(cell); cell = ''; }
            else if (c === '\n' || c === '\r') {
                if (c === '\r' && text[i + 1] === '\n') i++;
                row.push(cell); rows.push(row); row = []; cell = '';
            } else cell += c;
        }
        if (cell !== '' || row.length) { row.push(cell); rows.push(row); }
        return rows;
    }

    function fromSheet(url) {
        return fetch(url, { cache: 'no-store' })
            .then(function (r) { if (!r.ok) throw new Error(r.status); return r.text(); })
            .then(function (text) {
                var rows = parseCSV(text).filter(function (r) { return r.join('').trim(); });
                if (!rows.length) return { videos: [], photos: [] };
                // Header names are matched loosely so a Google Form's response sheet works as-is
                // ("Demo link", "Video URL", "Project name", "Short caption", ...).
                var head = rows.shift().map(function (h) {
                    h = h.trim().toLowerCase();
                    if (/link|url/.test(h)) return 'link';
                    if (/project/.test(h)) return 'project';
                    if (/title|name/.test(h)) return 'title';
                    if (/caption|description|about/.test(h)) return 'caption';
                    if (/^type|kind/.test(h)) return 'type';
                    if (/show|visible|publish/.test(h)) return 'show';
                    return h;
                });
                var out = { videos: [], photos: [] };
                rows.forEach(function (r) {
                    var o = {};
                    head.forEach(function (h, i) { if (!o[h]) o[h] = (r[i] || '').trim(); });
                    var src = o.link || o.src || o.url;
                    if (!src || /^(no|hide|false)$/i.test(o.show || '')) return;
                    var item = { title: o.title || '', project: o.project || '', caption: o.caption || '', src: src };
                    (/^(photo|picture|image)/i.test(o.type || '') ? out.photos : out.videos).push(item);
                });
                return out;
            });
    }

    window.loadMedia = function () {
        var base = window.MEDIA || {};
        var merged = { videos: (base.videos || []).slice(), photos: (base.photos || []).slice() };
        var url = (window.MEDIA_SHEET_URL || '').trim();
        if (!url || !window.fetch) return Promise.resolve(merged);
        return fromSheet(url).then(function (s) {
            merged.videos = merged.videos.concat(s.videos);
            merged.photos = merged.photos.concat(s.photos);
            return merged;
        }).catch(function () { return merged; });
    };

    function driveId(src) {
        var m = src.match(/drive\.google\.com\/(?:file\/d\/|open\?id=|uc\?(?:export=\w+&)?id=)([\w-]{10,})/);
        return m ? m[1] : null;
    }

    window.mediaEmbedUrl = function (src) {
        var m;
        if ((m = src.match(/youtu\.be\/([\w-]{6,})/)) || (m = src.match(/[?&]v=([\w-]{6,})/)) || (m = src.match(/youtube\.com\/(?:embed|shorts|live)\/([\w-]{6,})/)))
            return 'https://www.youtube-nocookie.com/embed/' + m[1];
        if ((m = src.match(/vimeo\.com\/(?:video\/)?(\d+)/))) return 'https://player.vimeo.com/video/' + m[1];
        if ((m = src.match(/loom\.com\/(?:share|embed)\/(\w+)/))) return 'https://www.loom.com/embed/' + m[1];
        var d = driveId(src);
        if (d) return 'https://drive.google.com/file/d/' + d + '/preview';
        var li = linkedinEmbed(src);
        if (li) return li;
        return null;
    };

    // LinkedIn post links: /posts/...-activity-123..., /feed/update/urn:li:activity:123..., or an embed link.
    function linkedinEmbed(src) {
        if (!/linkedin\.com/.test(src)) return null;
        if (/linkedin\.com\/embed\//.test(src)) return src.split('?')[0];
        var m = src.match(/urn(?::|%3A)li(?::|%3A)(activity|ugcPost|share)(?::|%3A)(\d{10,})/i)
            || src.match(/-(activity|ugcPost|share)-(\d{10,})/i);
        return m ? 'https://www.linkedin.com/embed/feed/update/urn:li:' + m[1] + ':' + m[2] : null;
    }

    window.mediaImageUrl = function (src) {
        var d = driveId(src);
        return d ? 'https://drive.google.com/thumbnail?id=' + d + '&sz=w1600' : src;
    };

    function norm(t) { return (t || '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim(); }
    window.mediaMatchesProject = function (item, project) {
        var p = norm(item.project);
        if (!p || !project) return false;
        var slug = norm(project.slug), name = norm(project.name);
        return p === slug || p === name || name.indexOf(p) === 0 || p.indexOf(name) === 0;
    };

    window.mediaVideoCard = function (item) {
        var card = document.createElement('div');
        card.className = 'media-card';
        var emb = window.mediaEmbedUrl(item.src), el;
        if (emb) {
            el = document.createElement('iframe');
            el.src = emb; el.title = item.title || 'Demo video'; el.loading = 'lazy';
            el.allow = 'autoplay; fullscreen; picture-in-picture'; el.allowFullscreen = true;
            if (/linkedin\.com/.test(emb)) el.className = 'li-embed';
        } else if (!/\.(mp4|webm|ogg|mov|m4v)(\?|#|$)/i.test(item.src)) {
            // Any other link: show a clean "watch" card instead of a broken player.
            el = document.createElement('a');
            el.href = item.src; el.target = '_blank'; el.rel = 'noopener';
            el.className = 'media-link';
            var host = ''; try { host = new URL(item.src).hostname.replace(/^www\./, ''); } catch (e) {}
            el.innerHTML = '<span class="play" aria-hidden="true">▶</span><span>Watch demo</span><small></small>';
            el.querySelector('small').textContent = host;
        } else {
            el = document.createElement('video');
            el.controls = true; el.preload = 'metadata'; el.playsInline = true;
            // Optional WebM copy next to an MP4, for browsers without H.264.
            [[item.src, /\.webm(\?|#|$)/i.test(item.src) ? 'video/webm' : 'video/mp4'], [item.webm, 'video/webm']].forEach(function (s) {
                if (!s[0]) return; var so = document.createElement('source'); so.src = s[0]; so.type = s[1]; el.appendChild(so);
            });
            if (item.poster) el.poster = item.poster;
        }
        card.appendChild(el);
        var c = document.createElement('div');
        c.className = 'cap';
        var t = document.createElement('strong'); t.textContent = item.title || '';
        c.appendChild(t);
        var sub = item.caption || item.project;
        if (sub) { var s = document.createElement('span'); s.textContent = sub; c.appendChild(s); }
        card.appendChild(c);
        return card;
    };
})();
