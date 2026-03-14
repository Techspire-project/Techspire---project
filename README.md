<<<<<<< HEAD
# ⚡ TechSpire - Digital Services Platform

## 🚀 Setup Instructions

### Requirements
- Python 3.8+
- pip

### Installation

```bash
cd techspire
pip install flask
python app.py
```

Open browser: http://localhost:5000

---

## 🔐 Admin Panel

URL: http://localhost:5000/admin/login

```
Username: admin
Password: techspire@2024
```

⚠️ Change password in app.py → ADMIN_PASSWORD before going live!

---

## 📱 Mobile App (PWA)

1. Open website on mobile browser (Chrome recommended)
2. Tap the "Install App" button OR browser menu → "Add to Home Screen"
3. App installs like a native mobile app!

---

## 📂 File Structure

```
techspire/
├── app.py              ← Main Flask app
├── database.db         ← Auto-created SQLite database
├── templates/
│   ├── base.html
│   ├── index.html      ← Homepage
│   ├── project_form.html
│   ├── flex_form.html
│   ├── invitation_form.html
│   ├── ppt_form.html
│   ├── paper_form.html
│   ├── report_form.html
│   ├── article_form.html
│   ├── website_form.html
│   ├── success.html
│   ├── admin_login.html
│   ├── admin_dashboard.html
│   └── admin_orders.html
└── static/
    ├── css/style.css
    ├── js/main.js
    ├── manifest.json   ← PWA config
    ├── sw.js           ← Service Worker
    └── images/
        ├── logo.png
        └── qrcode.jpg
```

---

## 🌐 Deploy Online (Free)

### Option 1 - PythonAnywhere (Recommended)
1. Sign up at pythonanywhere.com
2. Upload all files
3. Set up a Flask web app
4. Your site goes live!

### Option 2 - Render.com
1. Push to GitHub
2. Connect repo to render.com
3. Deploy as Python web service

---

## 💳 Payment Setup
- Replace `917010XXXXXX` in templates with your WhatsApp number
- QR code image is already in static/images/qrcode.jpg

## 📞 WhatsApp Number
Search for `917010XXXXXX` in all HTML files and replace with your number.
=======
# Techspire---project
 Tech_Spire Digital Services - Projects, Designs, PPT, Reports, Websites for Students
>>>>>>> bca0f642f13fe1986f3de8611cadc33c9fb0f586
