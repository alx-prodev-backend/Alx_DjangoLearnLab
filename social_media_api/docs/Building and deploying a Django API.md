# 🌐 Social Media API
## Milestone 1 – Project Setup & User Authentication

---

## 📌 Project Overview

This project is part of the ALX Backend Engineering program.

The goal of this milestone is to build the foundation of a production-ready **Social Media API** using:

- Django
- Django REST Framework (DRF)
- Token Authentication

This milestone focuses on:

- Setting up the Django project
- Creating a custom User model
- Implementing secure authentication
- Building registration and login endpoints
- Structuring the project for scalability

---

## 🏗 Project Structure

```
social_media_api/
│
├── accounts/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── social_media_api/
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py / wsgi.py
│
└── manage.py
```

---

## 🚀 Technologies Used

- Python 3.x
- Django
- Django REST Framework
- DRF Token Authentication
- SQLite (development database)

---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository

```
git clone https://github.com/YOUR_USERNAME/Alx_DjangoLearnLab.git
cd social_media_api
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate environment:

**Windows**
```
venv\Scripts\activate
```

**Linux / Mac**
```
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```
pip install django djangorestframework
```

---

### 4️⃣ Apply Migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Create Superuser (Optional)

```
python manage.py createsuperuser
```

---

### 6️⃣ Run Development Server

```
python manage.py runserver
```

Server runs at:
```
http://127.0.0.1:8000/
```

---

## 👤 Custom User Model

The project uses a custom user model extending `AbstractUser`.

### Additional Fields

- `bio` → TextField
- `profile_picture` → ImageField
- `followers` → ManyToManyField (self-reference, symmetrical=False)

### Configuration

In `settings.py`:

```
AUTH_USER_MODEL = 'accounts.User'
```

This ensures scalability and future extensibility.

---

## 🔐 Authentication System

Authentication is handled using:

- DRF Token Authentication
- Token automatically generated upon registration
- Token returned on successful login

Authentication header format:

```
Authorization: Token <your_token_here>
```

---

## 🔌 API Endpoints

---

### 📝 Register User

**POST** `/register/`

#### Request Body

```json
{
  "username": "john",
  "email": "john@example.com",
  "password": "StrongPassword123"
}
```

#### Response

```json
{
  "user": {
    "id": 1,
    "username": "john",
    "email": "john@example.com"
  },
  "token": "abc123xyz"
}
```

---

### 🔑 Login

**POST** `/login/`

#### Request Body

```json
{
  "username": "john",
  "password": "StrongPassword123"
}
```

#### Response

```json
{
  "token": "abc123xyz"
}
```

---

### 👤 Profile

**GET** `/profile/`

#### Headers

```
Authorization: Token abc123xyz
```

#### Response

```json
{
  "id": 1,
  "username": "john",
  "email": "john@example.com",
  "bio": "",
  "followers": []
}
```

---

## 🛡 Permissions

- Registration → Public
- Login → Public
- Profile → Authenticated users only

Unauthorized requests return:

```
401 Unauthorized
```

---

## 🧪 Testing

You can test the API using:

- Postman
- Thunder Client
- curl

Recommended testing flow:

1. Register user
2. Copy token
3. Login
4. Access profile with token
5. Try accessing profile without token (should fail)

---

## 🧱 Architecture Decisions

- Custom User Model implemented from start (best practice)
- Token-based authentication (simple & scalable)
- Modular app structure
- Clean separation of models, serializers, views

---

## 📈 Future Milestones

Upcoming features include:

- Posts & Comments
- Follow System
- Feed Generation
- Likes & Notifications
- Production Deployment

---

## 👨‍💻 Author

ALX Backend Engineering Track  
Social Media API – Django REST Project

---

## 📄 License

This project is for educational purposes.