# Social Media API

A full-featured Social Media API built with **Django** and **Django REST Framework (DRF)**.  
This project supports user authentication, posts, comments, user follows, feeds, likes, notifications, and is ready for production deployment.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Installation](#installation)  
4. [Environment Variables](#environment-variables)  
5. [Usage](#usage)  
6. [API Endpoints](#api-endpoints)  
7. [Deployment](#deployment)  
8. [Testing](#testing)  
9. [Contributing](#contributing)  
10. [License](#license)  

---

## Project Overview

The Social Media API allows users to:

- Register and authenticate accounts.  
- Create, read, update, and delete posts and comments.  
- Follow/unfollow other users.  
- View a personalized feed of posts from followed users.  
- Like posts and receive notifications for interactions.  
- Deploy to a production-ready environment with secure settings.

This project serves as a practice close to real-world backend development.

---

## Features

**Milestone 0: Project Setup & User Authentication**
- Custom User model with `bio`, `profile_picture`, `followers`, `following`.  
- Token-based authentication.  
- Registration, login, and profile management endpoints.

**Milestone 1: Posts & Comments**
- Post model: `author`, `title`, `content`, timestamps.  
- Comment model: references `Post` and `User`.  
- CRUD operations for posts and comments.  
- Pagination and filtering by post title/content.

**Milestone 2: User Follows & Feed**
- Users can follow/unfollow others.  
- Feed endpoint displays posts from followed users in reverse chronological order.

**Milestone 3: Likes & Notifications**
- Users can like/unlike posts.  
- Notifications for likes, comments, and new followers.  
- Endpoint for fetching unread notifications.

**Milestone 4: Deployment**
- Production-ready `settings.py`.  
- Static files served via WhiteNoise.  
- PostgreSQL support for production.  
- Deployment using Gunicorn/Nginx or Heroku.

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api
