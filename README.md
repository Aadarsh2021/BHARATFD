📖 FAQ API - Multilingual Support 🌍
🚀 A REST API built using Django to manage FAQs with multi-language support and optimized performance.

🎯 Objective
This project was developed as part of a backend developer hiring test, focusing on:
✔ Django models with WYSIWYG editor support
✔ Multi-language translations for FAQs
✔ PEP8 compliance and best practices
✔ Detailed README and proper Git commit messages

✅ Features
✔ Dynamic FAQ Management – Create, update, delete FAQs.
✔ Multi-Language Support – Supports Hindi, Bengali, Urdu, and more.
✔ WYSIWYG Editor – Uses django-ckeditor-5 for rich text formatting.
✔ Optimized Performance – Cached translations using Redis.
✔ Google Translate API – Automates translations at object creation.
✔ Admin Panel – Manage FAQs via Django Admin Interface.
✔ Fully Tested – Unit tests for API & models using pytest.
✔ Docker Support – Includes a Dockerfile for easy containerization.

📌 Installation Guide
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/Aadarsh2021/faq-api.git
cd faq-api
2️⃣ Set Up a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up Environment Variables
Create a .env file and add:

ini
Copy
Edit
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
REDIS_URL=redis://127.0.0.1:6379/1
5️⃣ Apply Database Migrations
bash
Copy
Edit
python manage.py migrate
python manage.py createsuperuser  # Create an admin user
6️⃣ Run the Server
bash
Copy
Edit
python manage.py runserver
✅ Now, your API is live at http://127.0.0.1:8000/.

📌 API Endpoints
🔹 Fetch All FAQs
bash
Copy
Edit
GET /api/faqs/
📌 Example Response:

json
Copy
Edit
[
    {
        "question": "What is Django?",
        "answer": "Django is a Python web framework."
    },
    {
        "question": "How does this API work?",
        "answer": "It provides FAQs via a REST API."
    }
]
🔹 Fetch FAQs in Hindi
bash
Copy
Edit
GET /api/faqs/?lang=hi
📌 Example Response:

json
Copy
Edit
[
    {
        "question": "Django क्या है?",
        "answer": "Django एक पायथन वेब फ्रेमवर्क है।"
    }
]
🔹 Fetch FAQs in Bengali
bash
Copy
Edit
GET /api/faqs/?lang=bn
🔹 Fetch FAQs in Urdu
bash
Copy
Edit
GET /api/faqs/?lang=ur
📌 Admin Panel
URL: http://127.0.0.1:8000/admin/
Login using the superuser credentials.
📌 Caching Mechanism
Uses Redis for optimized caching.
Speeds up API response times by storing translations in Redis.
Can be configured via REDIS_URL in .env.
📌 Unit Testing
To ensure everything is working correctly:

bash
Copy
Edit
pytest
✅ This ensures all models and APIs work correctly.

📌 Git & Version Control
Used Git for version control.
Followed conventional commit messages:
bash
Copy
Edit
feat: Add multilingual FAQ model
fix: Improve translation caching
docs: Update README with API examples
Used atomic commits to maintain clarity.
Pushing Changes
bash
Copy
Edit
git add .
git commit -m "docs: Updated README with full API details"
git push origin main
📌 Docker Support
✅ This project includes Docker support for easy containerization.

Running with Docker
bash
Copy
Edit
docker build -t faq-api .
docker run -d -p 8000:8000 faq-api
📌 Contributing
🔹 Want to improve this project?
Fork the repo, make your changes, and submit a pull request (PR).

bash
Copy
Edit
git checkout -b feature-new
git commit -m "feat: Added new language support"
git push origin feature-new
📌 Contact & Support
🔹 Author: Aadarsh Thakur
🔹 Email: thakuraadarsh1@gmail.com
🔹 GitHub: Aadarsh2021

📌 ✅ Now push this updated README to GitHub:

bash
Copy
Edit
git add README.md
git commit -m "docs: Updated README with full API details"
git push origin main
