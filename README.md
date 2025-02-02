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