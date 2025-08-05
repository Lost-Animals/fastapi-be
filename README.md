# 🐾 Lost Animals – FastAPI Backend

Welcome to the **Lost Animals** backend service – a FastAPI-based API that powers the platform helping people find and report lost pets.

---

## 🚀 Features

- 📌 Report lost/found animals
- 🔍 Search with filters (location, type, date)
- 🗺️ Integration with map services
- 🔐 Google SSO authentication
- 🌐 Public API for third-party use
- ⚙️ Admin tools for moderation and management

---

## 🛠️ Getting Started

### 🔧 Requirements

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (or pip)
- Google Firestore (as the database)
- Docker (optional for deployment)

### 📦 Installation

```bash
git clone https://github.com/Lost-Animals/backend.git
cd backend

# Install dependencies using uv
uv sync

# Start the development server
uvicorn app.main:app --reload
```

---

## 🐳 Docker Support

You can build and run the project using Docker:

```bash
docker buildx build -t lost-be .
docker run --name lostbe01 -d -p 8000:8000 lost-be
```

---

## 📡 API Documentation

Once running, visit:
- 🔗 Swagger: `http://localhost:8000/docs`
- 🔗 Redoc: `http://localhost:8000/redoc`

---

## 🔐 Authentication

Google Single Sign-On (SSO) is used for authentication.

---

## 🗃️ Database

Using **Google Firestore** (serverless, NoSQL) to store and retrieve reports and user data.

---

## 🚀 Deployment

Currently deployed on **Google Cloud Run** for serverless, auto-scaled hosting.

---

## 📚 Documentation

- 📖 [Wiki](https://github.com/Lost-Animals/docs/wiki)
- 📄 [Branching Strategy](https://github.com/Lost-Animals/docs/wiki/Branching-strategy)

---

## 🤝 Contributing

We welcome contributions of all kinds!

> Please read the [Branching Strategy](https://github.com/Lost-Animals/docs/wiki/Branching-strategy) before submitting PRs.

---

## 📜 License

MIT – free to use, share, and modify.

---

## ❤️ Thanks

Thanks to all contributors and communities helping build tech for a better cause!