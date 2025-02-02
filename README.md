# 🌐 FAQ API - Multilingual Management System

[![Django](https://img.shields.io/badge/Django-4.2-brightgreen)](https://www.djangoproject.com/)
[![Redis](https://img.shields.io/badge/Redis-7.0-red)](https://redis.io/)
[![Docker](https://img.shields.io/badge/Docker-24.0-blue)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A high-performance REST API for managing multilingual FAQs with automated translations and Redis caching.

![System Architecture](docs/architecture-diagram.png) <!-- Add actual diagram in your repo -->

## 📑 Table of Contents
- [Features](#-features)
- [Quick Start](#-quick-start)
- [API Documentation](#-api-documentation)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

| Feature                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| **Multi-language**     | Supports 10+ languages including Hindi, Bengali, Urdu                      |
| **Auto-translation**   | Google Translate API integration                                           |
| **Rich Text Editor**   | WYSIWYG editor with django-ckeditor-5                                       |
| **Caching**            | Redis-backed translation caching                                           |
| **Admin Interface**    | Full CRUD operations through Django Admin                                  |
| **Docker Support**     | Containerized development and production setups                            |
| **CI/CD**              | GitHub Actions for automated testing and deployment                        |

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Redis Server
- Docker (optional)
- Google Cloud Service Account

### Local Development

1. **Clone Repository**
   ```bash
   git clone https://github.com/Aadarsh2021/faq-api.git
   cd faq-api
Setup Environment

bash
Copy
python -m venv .venv && source .venv/bin/activate  # Linux/macOS
# For Windows: .venv\Scripts\activate
Install Dependencies

bash
Copy
pip install -r requirements.txt
Configure Environment
Create .env file:

ini
Copy
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
REDIS_URL=redis://localhost:6379/1
GOOGLE_APPLICATION_CREDENTIALS=./service-account.json
Database Setup

bash
Copy
python manage.py migrate
python manage.py createsuperuser
Run Server

bash
Copy
python manage.py runserver
Access API at: http://localhost:8000/api/faqs/

📚 API Documentation
Endpoints
http
Copy
GET /api/faqs/?lang={language_code}
POST /api/faqs/
PUT /api/faqs/{id}/
DELETE /api/faqs/{id}/
Example Requests
Get English FAQs

bash
Copy
curl http://localhost:8000/api/faqs/?lang=en
Create New FAQ

bash
Copy
curl -X POST -H "Content-Type: application/json" -d '{
  "question": "How to use this API?",
  "answer": "Check the documentation for implementation details."
}' http://localhost:8000/api/faqs/
Response Schema
json
Copy
{
  "id": 1,
  "question": "What is Django?",
  "answer": "A high-level Python web framework...",
  "language": "en",
  "created_at": "2023-08-20T12:34:56Z",
  "updated_at": "2023-08-20T12:34:56Z"
}
🐳 Deployment
Docker Setup
bash
Copy
docker-compose up --build
Production Environment
yaml
Copy
# docker-compose.prod.yml
version: '3.8'

services:
  web:
    image: faq-api:prod
    command: gunicorn faq_api.wsgi:application --bind 0.0.0.0:8000
    env_file:
      - .env.prod
    ports:
      - "8000:8000"
    depends_on:
      - redis
      - postgres

  redis:
    image: redis:alpine

  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: faq_db
      POSTGRES_USER: faq_user
      POSTGRES_PASSWORD: strongpassword
🧪 Testing
Run test suite with coverage:

bash
Copy
pytest --cov=faq_api --cov-report=html
🤝 Contributing
Fork the repository

Create feature branch:

bash
Copy
git checkout -b feat/new-feature
Commit changes:

bash
Copy
git commit -m "feat: Add new awesome feature"
Push to branch:

bash
Copy
git push origin feat/new-feature
Open a Pull Request

Code Standards:

PEP8 compliance enforced with flake8

100% test coverage for new features

Type hints for all public methods

Meaningful commit messages

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

Maintainer: Aadarsh Thakur
Email: thakuraadarsh1@gmail.com
Documentation: API Reference Guide