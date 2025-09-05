# 📚 LibraryHub - Library Management API

[![Django](https://img.shields.io/badge/Django-5.2.5-green.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-Latest-orange.svg)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

LibraryHub is a comprehensive RESTful Library Management System API built with Django REST Framework. It provides a complete solution for managing library operations including book cataloging, member management, and borrowing workflows with advanced filtering and search capabilities.

## ✨ Features

### Core Functionality
- 📖 **Book Management** - Complete CRUD operations for books with ISBN tracking
- 👤 **Author Management** - Author profiles with biography and book counting
- 🏷️ **Member Management** - Library member registration and status tracking
- 📋 **Borrow Records** - Comprehensive borrowing and return tracking system

### Advanced Features
- 🔍 **Advanced Search** - Search across books, authors, and members
- 📊 **Smart Filtering** - Filter by category, availability, status, and more
- ⏰ **Overdue Tracking** - Automatic overdue detection for borrowed books
- 📈 **Analytics** - Book counts, borrowed books tracking, and member statistics
- 🔄 **Real-time Status** - Dynamic availability updates

## 🛠️ Technologies Used

- **Backend Framework**: Django 5.2.5
- **API Framework**: Django REST Framework
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Filtering**: django-filter
- **Authentication**: Django's built-in authentication system
- **Documentation**: Browsable API (DRF)

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/kamrul785/LibraryHub.git
cd LibraryHub
```

### 2. Set Up Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
# Apply migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Load sample data (optional)
python manage.py loaddata sample_data.json  # if you have sample data
```

### 5. Run Development Server
```bash
python manage.py runserver
```

🎉 **Your API is now running at:** `http://127.0.0.1:8000/`



## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:

```ini
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
ALLOWED_HOSTS=*
EMAIL_HOST=your_email_host
```

## API Documentation
Swagger documentation is available at:
```
http://127.0.0.1:8000/swagger/
```

ReDoc documentation is available at:
```
http://127.0.0.1:8000/redoc/
```

## License
This project is licensed under the MIT License.

---
### Author
[Kamrul Hasan](https://github.com/kamrul785)