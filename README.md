# Welcome to To-DoListo 📝

A RESTful backend API for secure task management, built with Python, FastAPI JWT auth and SQLAlchemy ORM.

---

## Features

- Full CRUD operations
- JWT-based authentication and authorization
- Relational database integration via SQLAlchemy
- Clean, documented REST API
- Database zero-config

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Framework | FastAPI |
| ORM | SQLAlchemy |
| Auth | JSON Web Tokens (JWT) |
| Server | Uvicorn |
| Hashing | bcryipt |

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- `pip` package manager

### Public URL
https://fastapi-task-manager-production-2f54.up.railway.app/

**Use Example**
<img width="718" height="376" alt="example app" src="https://github.com/user-attachments/assets/fa7d74b0-9569-4e27-996b-622e08644708" />


### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/RaAdlDev/fastapi-task-manager.git

   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux / macOS
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the root directory:

   ```env
   SECRET_KEY=your_super_secret_key
   ```

5. **Run the development server**

   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at `http://127.0.0.1:8000`.

---

## API Overview

- Protected routers with Depends
- Each task is associated with a user_id
- The user id is automatically generated with uuid

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/register` | Register a new user |
| `POST` | `/login` | Login and receive a JWT token |


### Tasks

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/tasks` | List all tasks for the current user |
| `POST` | `/tasks` | Create a new task |
| `GET` | `/task/{id}` | Get a task by ID |
| `GET` | `/tasks/stats` | Get tasks stats |
| `DELETE` | `/tasks/{id}` | Delete a task by ID |
| `PATCH` | `/tasks/{id}` | Update a task by ID |

> All task endpoints require a valid JWT token in the `Authorization: Bearer <token>` header.

---

## Interactive API Docs

FastAPI generates interactive documentation automatically. Once the server is running, visit:

- **Swagger UI** → `http://127.0.0.1:8000/docs`
- **ReDoc** → `http://127.0.0.1:8000/redoc`

---

## Project Structure

```
to-dolisto/
├── main.py               # App entry point
├── database/             # Database connection and session, SQLAlchemy models
│   ├── models.py
│   └── connection.py           
├── schemas/              # Pydantic schemas
│   ├── user_schema.py
│   └── task_schema.py
├── routers/              # API route handlers
│   ├── users_auth.py
│   └── tasks.py
├── core/                 # JWT logic and dependencies
│   ├── security.py
│   └── settings.py
├── services/             # Business logic and database operations
│   ├── tasks_services.py
│   └── user_services.py
├── requirements.txt
└── .env
└── .gitignore

```

---

## License

This project is licensed under the MIT License.
