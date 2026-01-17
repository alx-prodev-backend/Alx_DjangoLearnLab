ALX_DJANGOLEARNLAB
==================

Project: Deep Dive into Django Models and Views
Track: ALX Backend / Django
Author: Hamad

--------------------------------------------------

PROJECT OVERVIEW
----------------
Alx_DjangoLearnLab is a Django learning repository designed to strengthen
backend development skills using Django. The main project in this repository,
"Deep Dive into Django Models and Views", focuses on mastering Django ORM,
views, authentication, role-based access control, and custom permissions.

This project follows real-world backend engineering practices and is structured
to simulate production-ready Django applications.

--------------------------------------------------

LEARNING OBJECTIVES
-------------------
By completing this project, you will be able to:

- Implement advanced Django ORM relationships
  (ForeignKey, ManyToMany, OneToOne)
- Build function-based and class-based views
- Configure URL routing effectively
- Implement user authentication (login, logout, registration)
- Apply role-based access control (RBAC)
- Create and enforce custom Django permissions
- Structure Django projects professionally for scalability

--------------------------------------------------

PROJECT STRUCTURE
-----------------
Alx_DjangoLearnLab/
|
|-- django-models/
|   |-- manage.py
|   |-- django_models/
|   |   |-- settings.py
|   |   |-- urls.py
|   |   |-- asgi.py
|   |   |-- wsgi.py
|   |
|   |-- relationship_app/
|   |   |-- models.py
|   |   |-- views.py
|   |   |-- urls.py
|   |   |-- signals.py
|   |   |-- query_samples.py
|   |   |-- templates/
|   |       |-- relationship_app/
|   |           |-- list_books.html
|   |           |-- library_detail.html
|   |           |-- login.html
|   |           |-- logout.html
|   |           |-- register.html
|   |           |-- admin_view.html
|   |           |-- librarian_view.html
|   |           |-- member_view.html
|
|-- scripts/
|   |-- setup_project.sh
|
|-- .github/
|   |-- ISSUE_TEMPLATE/
|   |-- PULL_REQUEST_TEMPLATE.md
|
|-- README.txt
|-- LICENSE

--------------------------------------------------

TECH STACK
----------
- Python 3.8+
- Django 4+
- SQLite (development)
- HTML (Django Templates)
- Git & GitHub

--------------------------------------------------

SETUP INSTRUCTIONS
------------------
1. Clone the repository:
   git clone https://github.com/<your-username>/Alx_DjangoLearnLab.git

2. Navigate to the project:
   cd Alx_DjangoLearnLab

3. Run setup script:
   bash scripts/setup_project.sh

4. Apply migrations:
   python manage.py migrate

5. Run development server:
   python manage.py runserver

--------------------------------------------------

USER ROLES
----------
Admin:
- Full access
- Manage users and books

Librarian:
- Add and edit books
- View libraries

Member:
- View books and libraries only

--------------------------------------------------

FEATURES
--------
- Advanced Django ORM relationships
- Function-based and class-based views
- Authentication system
- Role-Based Access Control (RBAC)
- Custom permissions for book management

--------------------------------------------------

BDD (GHERKIN OVERVIEW)
---------------------
Feature: Library and Book Management

Scenario: View books
- Given books exist
- When user visits book list
- Then books are displayed

Scenario: Role-restricted actions
- Given user role
- When user performs action
- Then access is allowed or denied

--------------------------------------------------

LICENSE
-------
MIT License

--------------------------------------------------

AUTHOR
------
Hamad
ALX Backend / Django Developer
