# 📝 Django To-Do API (Demo Project)

A simple and beginner-friendly **To-Do API** built using **Django** and **Django REST Framework (DRF)**.  
This project demonstrates how to create RESTful endpoints for managing to-do tasks — perfect for learning API development with Django.

---

## 🚀 Features

- Create, Read, Update, and Delete (CRUD) To-Do tasks  
- Built with Django REST Framework  
- Lightweight, modular, and easy to extend  
- JSON-based responses  
- Ready for deployment or further development  

---

## 🧱 Tech Stack

- **Python 3.10+**
- **Django 5+**
- **Django REST Framework**
- **SQLite** (default database)

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/DemoAPIProject.git
cd DemoAPIProject
```

### 2️⃣ Create and Activate a Virtual Environment
**Windows (Git Bash):**
```bash
python -m venv venv
source venv/Scripts/activate
```

**Command Prompt:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install django djangorestframework
```

---

## 🛠️ Usage

### Run Database Migrations
```bash
python manage.py migrate
```

### Start the Development Server
```bash
python manage.py runserver
```

Server will start at:  
👉 http://127.0.0.1:8000/

---

## 📡 API Endpoints (Demo)

| Method | Endpoint | Description | Example Response |
|--------|-----------|-------------|------------------|
| **GET** | `/api/` | Root endpoint | `{ "message": "Welcome to the API root!" }` |
| **GET** | `/api/hello/` | Example To-Do message endpoint | `{ "message": "Hello from Django API!" }` |

You can extend this project to include actual CRUD operations for tasks (e.g., `/api/todos/`, `/api/todos/<id>/`).

---

## 🧩 Project Structure

```
manage.py
myproject/
└── settings.py
api/
   ├── views.py
   ├── urls.py
   └── __init__.py
```

---

## 💡 Future Enhancements

- Add models for To-Do items  
- Implement full CRUD operations  
- Add authentication (JWT or Session)  
- Add filtering and pagination  

---

## 🧾 License

This project is licensed under the MIT License — feel free to use and modify it for learning or development.

---
