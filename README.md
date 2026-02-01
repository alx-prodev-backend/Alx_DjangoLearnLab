# 🧩 API Project – Django REST Framework

## 📌 Project Name

**API Project – Django REST Framework Fundamentals**

## 📌 GitHub Repository Name

**Alx_DjangoLearnLab**

📂 **Project Directory:** `api_project/`

---

## 🎯 Project Description

This project is a hands-on learning application built using **Django REST Framework (DRF)**. It demonstrates the fundamental concepts required to build RESTful APIs using Django, starting from project setup and ending with secured endpoints using authentication and permissions.

The project is designed as a **learning milestone / lab**, focusing on practical implementation rather than theory. It is structured to be easily extendable in the future (pagination, filtering, JWT authentication, role-based access control, etc.).

---

## 🧠 Learning Objectives

* Understand the structure of a Django project built for APIs
* Integrate and use Django REST Framework correctly
* Create models, serializers, and API views
* Implement CRUD operations using ViewSets
* Use Routers to auto-generate API URLs
* Secure APIs using Token Authentication
* Apply permission classes to control access
* Document a Django REST project professionally on GitHub

---

## 🏗️ Project Structure

```
api_project/
│
├── api/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── api_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
└── README.md
```

---

## 🗂️ Milestones & Tasks Documentation

# 🚩 Milestone 0: Project Setup & DRF Installation

### 🎯 Objective

Set up a new Django project configured specifically for API development using Django REST Framework.

### ✅ Tasks

* Install Django
* Create a new Django project named `api_project`
* Install Django REST Framework
* Create a Django app named `api`
* Define a simple model (`Book`)
* Run database migrations
* Start the development server to verify setup

### 🧩 Book Model

```python
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
```

---

# 🚩 Milestone 1: First API Endpoint (ListAPIView)

### 🎯 Objective

Create the first API endpoint to retrieve a list of books using Django REST Framework.

### ✅ Tasks

* Create `serializers.py`
* Implement `BookSerializer` using `ModelSerializer`
* Create `BookList` view using `ListAPIView`
* Configure URL routing for the API endpoint
* Test the endpoint using browser or API tools

### 🔗 Endpoint

```
GET /api/books/
```

### 📤 Sample Response

```json
[
  {
    "id": 1,
    "title": "Clean Code",
    "author": "Robert C. Martin"
  }
]
```

---

# 🚩 Milestone 2: CRUD Operations using ViewSets & Routers

### 🎯 Objective

Implement full CRUD functionality for the Book model using DRF ViewSets and Routers.

### ✅ Tasks

* Create `BookViewSet` using `ModelViewSet`
* Register the ViewSet using `DefaultRouter`
* Include router URLs in the app routing
* Test Create, Read, Update, and Delete operations

### 🔗 Endpoints

```
GET     /api/books_all/
GET     /api/books_all/<id>/
POST    /api/books_all/
PUT     /api/books_all/<id>/
DELETE  /api/books_all/<id>/
```

---

# 🚩 Milestone 3: Authentication & Permissions

### 🎯 Objective

Secure API endpoints using Token Authentication and permission classes.

### ✅ Tasks

* Add `rest_framework.authtoken` to installed apps
* Run migrations for token tables
* Configure DRF authentication settings
* Enable token-based authentication
* Apply permission classes such as `IsAuthenticated`
* Test API access with and without authentication tokens

### 🔐 Authentication Method

* Token Authentication

### 🔑 Token Endpoint

```
POST /api/token/
```

### 🛡️ Permissions Used

* IsAuthenticated
* IsAdminUser (optional)

---

## 🧪 Testing Tools

* Postman
* curl
* Web Browser (GET requests)

---

## 📄 README.md Template (Ready to Use)

````md
# API Project – Django REST Framework

## Description
A learning-based Django REST Framework project covering API fundamentals, CRUD operations, and authentication.

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite

## Features
- Book API
- Full CRUD operations
- Token Authentication
- Permissions

## Installation
```bash
pip install django djangorestframework
````

## Run Project

```bash
python manage.py migrate
python manage.py runserver
```

## API Endpoints

| Method | Endpoint        | Description          |
| ------ | --------------- | -------------------- |
| GET    | /api/books/     | List books           |
| CRUD   | /api/books_all/ | Full CRUD operations |

## Author

Hammad Ibrahim

```

---

## 🏷️ Suggested GitHub Labels

- milestone-0
- milestone-1
- milestone-2
- milestone-3
- django
- drf
- api
- authentication

---

## 🧩 Suggested GitHub Issues

- Project setup and configuration
- Create Book model
- Implement serializers
- Create API views
- Implement CRUD using ViewSets
- Secure API with token authentication
- Write project documentation

---

## ✅ Project Status

✔ Completed – Ready for review, assessment, and future extension

---

🚀 **Milestone Achieved: Django REST Framework Fundamentals**

```
