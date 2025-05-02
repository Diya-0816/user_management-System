# 🧑‍💼 User Management System (FastAPI-Based)

An open-source **User Management System** developed by **Professor Keith Williams** for NJIT students. This modular and scalable backend provides a robust foundation for an event-driven platform connecting students and professionals through company tours, mock interviews, and guest lectures.

---

## 🚀 Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL + SQLAlchemy
- **Authentication**: OAuth2 with Password Flow
- **Email**: Mailtrap + FastMail
- **Deployment**: Docker, Docker Compose
- **Testing**: Pytest, GitHub Actions (CI/CD)

---

## 📁 Project Structure

```
user_management_system/
│
├── app/                    # Main application package
│   ├── api/                # API routes (FastAPI Routers)
│   ├── core/               # Configuration & Security
│   ├── db/                 # DB session, base class
│   ├── models/             # SQLAlchemy models
│   ├── schemas/            # Pydantic schemas
│   ├── services/           # Business logic
│   ├── templates/          # Email templates (HTML)
│   └── utils/              # Utilities (e.g., username generator)
│
├── scripts/                # CLI scripts (e.g., admin creation)
├── tests/                  # Unit and integration tests
├── Dockerfile              # Docker image configuration
├── docker-compose.yml      # Multi-container setup
├── requirements.txt        # Python dependencies
└── main.py                 # FastAPI entry point
```

---

## ✅ Features

### 👤 User Management
- Register, login, and update profiles
- Role-based access: `Admin`, `Manager`, `Authenticated`, `Anonymous`
- Email verification with templates
- Unique username generation (noun_verb_number)
- Pro status request (upon completing profile)

### 🔐 Authentication
- OAuth2 (Password Flow)
- Token-based security
- Role and permission checks

### 📬 Email Service
- Integrated with Mailtrap for dev/testing
- Templated HTML verification emails

### 🧪 Testing & CI/CD
- Pytest test suite
- Fixtures and mocks for isolated tests
- GitHub Actions (optional setup)

### 🐳 Dockerized
- Full app runs via `docker-compose up`
- PostgreSQL included in container setup

---

## 🛠️ Getting Started

### 🚧 Prerequisites

- Python 3.9+
- Docker + Docker Compose

### 🔧 Setup

```bash
git clone https://github.com/yourusername/user-management-system.git
cd user-management-system
cp .env.example .env  # Update your secrets
docker-compose up --build
```

---

## 🧑‍💻 Development Notes

- First registered user is assigned admin by default (override with CLI script).
- Username is editable but must remain unique and URL-safe.
- Mailtrap integration is used in dev — replace SMTP in production.

---

## 📝 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
