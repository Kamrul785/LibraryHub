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

## 📚 API Endpoints

### Base URL: `http://127.0.0.1:8000/api/`

| Endpoint | Methods | Description |
|----------|---------|-------------|
| `/authors/` | GET, POST, PUT, DELETE | Manage authors |
| `/books/` | GET, POST, PUT, DELETE | Manage books |
| `/members/` | GET, POST, PUT, DELETE | Manage library members |
| `/borrow-records/` | GET, POST, PUT, DELETE | Manage borrow records |

### 🔍 Search & Filter Examples

```bash
# Search books by title or author
GET /api/books/?search=python

# Filter books by category
GET /api/books/?category=Technology

# Filter books by availability
GET /api/books/?availability_status=true

# Filter borrow records by status
GET /api/borrow-records/?status=BORROWED

# Search members by name or email
GET /api/members/?search=john
```

## 📊 Data Models

### Author
- `name` - Author's full name
- `biography` - Author's biography (optional)
- `books_count` - Number of books by this author

### Book
- `title` - Book title
- `isbn` - Unique ISBN number
- `category` - Book category
- `availability_status` - Current availability
- `publication_date` - Publication date
- `total_copies` - Total number of copies
- `available_copies` - Currently available copies
- `author` - Foreign key to Author

### Member
- `name` - Member's full name
- `email` - Unique email address
- `membership_date` - Date of membership
- `status` - ACTIVE or INACTIVE
- `borrowed_books_count` - Current borrowed books count

### Borrow Record
- `book` - Foreign key to Book
- `member` - Foreign key to Member
- `borrow_date` - Date when book was borrowed
- `due_date` - Due date for return
- `return_date` - Actual return date (if returned)
- `status` - BORROWED, RETURNED, or OVERDUE
- `is_overdue` - Boolean indicating if the book is overdue

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:

```ini
# Django Settings
SECRET_KEY=your-super-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (for production)
DATABASE_URL=postgresql://username:password@localhost:5432/libraryhub

# Email Settings (for notifications)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_USE_TLS=True
```

### Settings for Production
```python
# In settings.py for production
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Use PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'libraryhub',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 📖 API Documentation

The API provides a browsable interface powered by Django REST Framework:

- **Browsable API**: `http://127.0.0.1:8000/api/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/`

### Example API Usage

```python
import requests

# Get all books
response = requests.get('http://127.0.0.1:8000/api/books/')
books = response.json()

# Create a new book
new_book = {
    "title": "Python Programming",
    "isbn": "978-0123456789",
    "category": "Technology",
    "publication_date": "2024-01-01",
    "author": 1,
    "total_copies": 5
}
response = requests.post('http://127.0.0.1:8000/api/books/', json=new_book)
```

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

## 📦 Deployment

### Using Docker (Recommended)
```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### Using Heroku
1. Install Heroku CLI
2. Create `Procfile`:
   ```
   web: python manage.py runserver 0.0.0.0:$PORT
   ```
3. Deploy:
   ```bash
   heroku create your-app-name
   git push heroku main
   heroku run python manage.py migrate
   ```

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** and add tests
4. **Commit your changes**: `git commit -m 'Add amazing feature'`
5. **Push to the branch**: `git push origin feature/amazing-feature`
6. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Write tests for new features
- Update documentation as needed
- Use meaningful commit messages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Known Issues & Roadmap

### Current Limitations
- No email notifications for overdue books
- Basic authentication system (no JWT implemented yet)
- No file upload for book covers

### Future Enhancements
- [ ] JWT Authentication integration
- [ ] Email notifications for due dates
- [ ] Book cover image uploads
- [ ] Advanced reporting and analytics
- [ ] Mobile app API endpoints
- [ ] Integration with external book APIs
- [ ] Multi-library support

## 📞 Support

If you encounter any issues or have questions:

- 📧 **Email**: [kamrul785@example.com](mailto:kamrul785@example.com)
- 🐛 **Issues**: [GitHub Issues](https://github.com/kamrul785/LibraryHub/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/kamrul785/LibraryHub/discussions)

## 🙏 Acknowledgments

- Django team for the amazing framework
- Django REST Framework team for the powerful API toolkit
- All contributors who help improve this project

---

**Built with ❤️ by [Kamrul Hasan](https://github.com/kamrul785)**

⭐ **Star this repository if you found it helpful!**