# 📖 FAQ API - Multilingual Support 🌍

🚀 A REST API built using Django to manage FAQs with multi-language support and optimized performance.

## 🎯 Objective
This project was developed as part of a backend developer hiring test, focusing on:
- ✔ Django models with WYSIWYG editor support
- ✔ Multi-language translations for FAQs
- ✔ PEP8 compliance and best practices
- ✔ Detailed README and proper Git commit messages

## ✅ Features
- ✔ Dynamic FAQ Management – Create, update, delete FAQs
- ✔ Multi-Language Support – Supports Hindi, Bengali, Urdu, and more
- ✔ WYSIWYG Editor – Uses django-ckeditor-5 for rich text formatting
- ✔ Optimized Performance – Cached translations using Redis
- ✔ Google Translate API – Automates translations at object creation
- ✔ Admin Panel – Manage FAQs via Django Admin Interface
- ✔ Fully Tested – Unit tests for API & models using pytest
- ✔ Docker Support – Includes Dockerfile for easy containerization

## 📌 Installation Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Aadarsh2021/faq-api.git
cd faq-api


2️⃣ Set Up Virtual Environment
bash
Copy
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy
pip install -r requirements.txt
4️⃣ Environment Variables
Create .env file:

ini
Copy
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
REDIS_URL=redis://127.0.0.1:6379/1
5️⃣ Database Setup
bash
Copy
python manage.py migrate
python manage.py createsuperuser
6️⃣ Run Server
bash
Copy
python manage.py runserver
API Live at: http://127.0.0.1:8000/

📌 API Endpoints
🔹 Get All FAQs
http
Copy
GET /api/faqs/
Response:

json
Copy
[
    {
        "question": "What is Django?",
        "answer": "Django is a Python web framework."
    }
]
🔹 Get Hindi FAQs
http
Copy
GET /api/faqs/?lang=hi
Response:

json
Copy
[
    {
        "question": "Django क्या है?",
        "answer": "Django एक पायथन वेब फ्रेमवर्क है।"
    }
]
🔹 Get Bengali FAQs
http
Copy
GET /api/faqs/?lang=bn
🔹 Get Urdu FAQs
http
Copy
GET /api/faqs/?lang=ur
📌 Admin Panel
Access: http://localhost:8000/admin/
Use superuser credentials created during setup.

📌 Caching Mechanism
Redis-based caching for translations

Configure via REDIS_URL in .env

Automatic cache invalidation on FAQ updates

📌 Unit Testing
bash
Copy
pytest
📌 Version Control
Commit Convention:

Copy
feat: Add multilingual FAQ model
fix: Improve translation caching
docs: Update README with API examples
Push Changes:

bash
Copy
git add .
git commit -m "docs: Updated README with full API details"
git push origin main
📌 Docker Support
Build & Run:

bash
Copy
docker build -t faq-api .
docker run -d -p 8000:8000 faq-api
📌 Contributing
Fork the repository

Create feature branch:

bash
Copy
git checkout -b feature-new
Commit changes:

bash
Copy
git commit -m "feat: Added new language support"
Push to branch:

bash
Copy
git push origin feature-new
Open a Pull Request

📌 Contact
Author: Aadarsh Thakur

Email: thakuraadarsh1@gmail.com

GitHub: Aadarsh2021

Copy

This version:
1. Uses proper Markdown syntax for GitHub rendering
2. Maintains consistent emoji usage
3. Has proper code block formatting with language identifiers
4. Uses hierarchical headers
5. Includes clear section separation
6. Maintains all original information while improving readability
7. Follows GitHub-Flavored Markdown standards

The preview in VS Code will match GitHub's rendering closely, especially when using the Markdown Preview Enhanced extension.