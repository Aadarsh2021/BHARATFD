# 🚀 FAQ API - Multilingual Support 🌍

A powerful REST API for managing FAQs with multilingual support! Designed using Django, Django REST Framework, Redis caching, and Google Translate API.

## ✅ Features
✔ **Dynamic FAQ Management**: Create, update, and delete FAQs via API.  
✔ **Multilingual Support**: Hindi (hi), Bengali (bn), Urdu (ur), and more.  
✔ **WYSIWYG Editor**: Rich text formatting via django-ckeditor-5.  
✔ **High Performance**: Redis caching for optimized speed.  
✔ **Secure & Tested**: CI/CD pipeline with pytest for reliability.  
✔ **Docker Support**: Easily deploy anywhere using Docker.  
✔ **Live Demo (If Deployed)**: [Live API Link](https://faq-api.onrender.com/api/faqs/)  

---

## 📌 API Usage Examples

### **🔍 Fetch FAQs (Default: English)**
```bash
curl http://localhost:8000/api/faqs/
```

### **📝 Fetch FAQs in Hindi**
```bash
curl http://localhost:8000/api/faqs/?lang=hi
```

### **🌍 Fetch FAQs in Bengali**
```bash
curl http://localhost:8000/api/faqs/?lang=bn
```

### **🛠 Create a New FAQ**
```bash
curl -X POST http://localhost:8000/api/faqs/ \  
     -H "Content-Type: application/json" \  
     -d '{"question": "What is Django?", "answer": "Django is a Python web framework."}'
```

---

## 🏗 Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Aadarsh2021/faq-api.git
cd faq-api
```

### **2️⃣ Create Virtual Environment & Install Dependencies**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### **3️⃣ Set Up Environment Variables**
Create a `.env` file in the project root:
```ini
SECRET_KEY=your-secret-key
DEBUG=True
REDIS_URL=redis://127.0.0.1:6379/1
```

### **4️⃣ Run Migrations & Start the Server**
```bash
python manage.py migrate
python manage.py runserver
```
Now visit: `http://127.0.0.1:8000/api/faqs/`

---

## 🚀 Deployment (Render/Heroku/Docker)

### **🔹 Deploy with Docker**
```bash
docker build -t faq-api .
docker run -d -p 8000:8000 faq-api
```

### **🔹 Deploy on Render** (Recommended for Free Hosting)
1. **Create an account on** [Render](https://render.com/)
2. **Connect GitHub Repo & Deploy a Web Service**
3. **Set `DATABASE_URL` & `REDIS_URL` in Environment Variables**
4. **Start the Service & Get Live API URL!**

---

## 🔒 Security & Performance Enhancements

✅ **Rate Limiting (Prevents Abuse)**
```python
REST_FRAMEWORK['DEFAULT_THROTTLE_CLASSES'] = ['rest_framework.throttling.UserRateThrottle']
REST_FRAMEWORK['DEFAULT_THROTTLE_RATES'] = {'user': '1000/day'}
```

✅ **Redis Caching for Faster API Responses**
```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

✅ **CI/CD with GitHub Actions** *(Automated Testing Before Merge)*
```yaml
name: Django Tests
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v2
      - name: Install Dependencies
        run: pip install -r requirements.txt
      - name: Run Tests
        run: pytest
```

---

## 🔗 Contributing
1️⃣ **Fork the Repository**  
2️⃣ **Create a Feature Branch** (`git checkout -b feature-new`)  
3️⃣ **Commit Your Changes** (`git commit -m "feat: Added feature"`)  
4️⃣ **Push to GitHub** (`git push origin feature-new`)  
5️⃣ **Create a Pull Request** 🚀

---

## 🤝 Contact & Support
📩 **Email**: aadarsh.dev@example.com  
🐦 **Twitter**: [@Aadarsh2021](https://twitter.com/Aadarsh2021)  
💼 **LinkedIn**: [Aadarsh Profile](https://linkedin.com/in/aadarsh)

