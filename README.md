# Secure Task API

A backend REST API for task management with JWT authentication and user-isolated data access. Built with FastAPI, SQLAlchemy, and SQLite, focusing on secure authentication, clean service-layer design, and predictable API behavior.

---

## Features

- User registration and login with hashed passwords
- JWT-based authentication (Bearer tokens)
- Protected CRUD endpoints for tasks
- User isolation: each user can access only their own tasks
- Automatic API docs via FastAPI (`/docs`)

---

## Tech Stack

- Python, FastAPI
- SQLite, SQLAlchemy
- JWT auth (python-jose)
- Password hashing (bcrypt via passlib)

---

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
