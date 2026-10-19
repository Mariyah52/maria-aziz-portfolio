# Imadi.tech — pre-ad launch checklist

This update preserves your existing portfolio project data, media data, CV, portrait, and the dates/content stored in the project data file.

## What is implemented
- Conversion-focused homepage CTA and clearer enquiry CTA.
- Accessible project enquiry form that prepares a message in the visitor's email app. It does **not** submit to a server; the visitor must press Send in their mail app.
- `dataLayer` events: `portfolio_cta_click` and `project_enquiry_email_prepared`. These events are only instrumentation hooks until a real Google Tag Manager / Google Ads tag is configured.
- Responsive form styles, focus states, and reduced-motion handling.
- Canonical production host in generated page metadata and sitemap: `https://www.imadi.tech`. Ensure apex `https://imadi.tech` redirects to the www host.
- Work-page loading fallback and a helpful case-study loading/not-found message.

## Required before paid ads
1. **Use a server-backed form for reliable lead capture.** The current form opens the visitor's email app. For direct website submissions, connect Formspree, your own API, or another form provider. Add its endpoint only after creating the account and configuring spam protection and privacy terms.
2. **Configure tracking IDs.** Create/choose a Google Tag Manager container or Google tag, add the real ID in the site's head, configure a Google Ads conversion action for a confirmed successful enquiry, and test with Tag Assistant. No tracking ID was invented or inserted in this project.
3. **Do not mark CTA clicks as leads.** Treat CTA events as micro-conversions; count a lead only after a server-confirmed form submission or a clearly measured contact action. The email-compose fallback cannot confirm that an email was actually sent.
4. **Add real project screenshots.** `assets/media-data.js` currently contains example comments, not confirmed screenshot assets. Add authentic, client-approved screenshots/videos in `assets/media/` and entries in `assets/media-data.js`; no mock client evidence was fabricated.
5. **Check canonical domain and redirects.** Confirm `https://imadi.tech/*` redirects to `https://www.imadi.tech/*`, all pages load over HTTPS, and Google Search Console has the correct property and sitemap.
6. **Performance/accessibility testing.** Run PageSpeed Insights on `/`, `/work/`, `/contact/`, and a case-study URL; test keyboard-only navigation, mobile viewport, form validation, theme toggle, and case-study links in Chrome.
7. **Validate contact delivery.** Submit a test enquiry, confirm the email draft contains the expected fields, and separately verify the recipient address.

## Useful pages
- Homepage: https://www.imadi.tech/
- Work: https://www.imadi.tech/work/
- Demos: https://www.imadi.tech/media/
- Contact: https://www.imadi.tech/contact/

## Deployment note
The site is a static HTML/CSS/JavaScript project. Deploy the contents of this folder using the same static hosting workflow as before. Keep a backup of the current live deployment so you can roll back.
