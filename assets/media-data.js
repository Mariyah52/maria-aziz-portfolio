/**
 * Demo videos and work pictures shown on the Demos page (/media/).
 *
 * 1. Copy your files into assets/media/ (e.g. assets/media/alico-demo.mp4).
 * 2. Add one entry per file below, then commit and push to GitHub.
 *
 * Videos: src can be a file path (.mp4 / .webm) or a YouTube, Vimeo or Loom link.
 * Tip: open /media/?edit=1 on your site to pick files, preview them, and copy
 * ready-made entries for this file.
 */
/*
 * EASIEST WAY: Google Sheet (no code, no push)
 * Paste your sheet's "Publish to web" CSV link below once. After that, every
 * row you add in the sheet shows up on the site automatically.
 * Columns: type | title | project | link | caption | show
 */
window.MEDIA_SHEET_URL = "";

// Your Google Form link. Opening /media/?edit=1 shows an "Add a demo" button that opens it.
window.MEDIA_FORM_URL = "";

window.MEDIA = {
  videos: [
    { title: "HerCommerce: set up a store, add products, get the link", project: "hercommerce", caption: "Seller side · dummy data", src: "/assets/media/hercommerce-seller.mp4", webm: "/assets/media/hercommerce-seller.webm", poster: "/assets/media/hercommerce-seller-poster.jpg" },
    { title: "HerCommerce: a customer shops and orders on WhatsApp", project: "hercommerce", caption: "Customer side · dummy data", src: "/assets/media/hercommerce-customer.mp4", webm: "/assets/media/hercommerce-customer.webm", poster: "/assets/media/hercommerce-customer-poster.jpg" },
    { title: "Child-Friendly City Index: score any area for children", project: "child-friendly-city-index", caption: "Open source, free to use · AI reply generated offline for this demo", src: "/assets/media/cfci-demo.mp4", webm: "/assets/media/cfci-demo.webm", poster: "/assets/media/cfci-demo-poster.jpg" },
    { title: "Claims bot: filing a damage claim on WhatsApp", project: "uk-logistics-whatsapp", caption: "Real bot replies · dummy data", src: "/assets/media/claims-bot.mp4", webm: "/assets/media/claims-bot.webm", poster: "/assets/media/claims-bot-poster.jpg" },
    { title: "Claims dashboard: raise, approve or reject", project: "uk-logistics-whatsapp", caption: "Photos, invoice and details in one place · dummy data", src: "/assets/media/claims-dashboard.mp4", webm: "/assets/media/claims-dashboard.webm", poster: "/assets/media/claims-dashboard-poster.jpg" },
    { title: "Company Monitor: branch WhatsApp leads, visible to management", project: "company-monitor", caption: "Dummy data · simulated WhatsApp connection", src: "/assets/media/cm-demo.mp4", webm: "/assets/media/cm-demo.webm", poster: "/assets/media/cm-demo-poster.jpg" },
    { title: "UK ERP: invoice with VAT, email and credit note", project: "uk-logistics-erp", caption: "Dummy data · client address and bank details blurred", src: "/assets/media/erp-demo.mp4", webm: "/assets/media/erp-demo.webm", poster: "/assets/media/erp-demo-poster.jpg" },
    { title: "ReNaz: booking a pickup on WhatsApp", project: "renaz", caption: "Real bot replies · dummy data", src: "/assets/media/renaz-bot.mp4", webm: "/assets/media/renaz-bot.webm", poster: "/assets/media/renaz-bot-poster.jpg" },
    { title: "ReNaz: the request lands on the dashboard", project: "renaz", caption: "New request, details and collector assignment · dummy data", src: "/assets/media/renaz-dashboard.mp4", webm: "/assets/media/renaz-dashboard.webm", poster: "/assets/media/renaz-dashboard-poster.jpg" },
    { title: "ALICO: invoice to WhatsApp in 15 seconds", project: "alico", caption: "Every module, a new invoice, and WhatsApp sharing · dummy data", src: "/assets/media/alico-demo.mp4", webm: "/assets/media/alico-demo.webm", poster: "/assets/media/alico-demo-poster.jpg" },
    // { title: "ALICO Business Suite demo", project: "ALICO Enterprises", src: "/assets/media/alico-demo.mp4" },
    // { title: "Marist walkthrough", project: "Marist", src: "https://www.youtube.com/watch?v=VIDEO_ID" },
  ],
  photos: [
    { title: "Claims bot: the customer hears back on WhatsApp", project: "uk-logistics-whatsapp", caption: "Approved and rejected replies · dummy data", src: "/assets/media/claims-reply.jpg" },
    { title: "Company Monitor conversations", project: "company-monitor", caption: "Dummy data for demo · no client details shown", src: "/assets/media/cm-demo.jpg" },
    { title: "UK ERP invoice with credit note", project: "uk-logistics-erp", caption: "Dummy data for demo · client details blurred", src: "/assets/media/erp-demo.jpg" },
    { title: "ReNaz dashboard and WhatsApp bot", project: "renaz", caption: "Laptop and mobile view · dummy data for demo", src: "/assets/media/renaz-demo.jpg" },
    { title: "ALICO Business Suite dashboard", project: "alico", caption: "Laptop and mobile view · dummy data for demo", src: "/assets/media/alico-demo.jpg" },
    { title: "SHAH Enterprise Business Suite dashboard", project: "shah", caption: "Laptop and mobile view · dummy data for demo", src: "/assets/media/shah-demo.jpg" },
    // { title: "ALICO dashboard", caption: "Sales and stock overview", src: "/assets/media/alico-dashboard.jpg" },
  ]
};
