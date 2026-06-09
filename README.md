# 🚀 Health Check Task Manager API — Huawei Cloud CodeArts Demo Project

A simple Python/Flask REST API designed specifically for demonstrating
Huawei Cloud CodeArts end-to-end DevSecOps capabilities.

---

## 📁 Project Structure

```
codearts-demo/
├── app/
│   └── main.py          # Flask REST API
├── tests/
│   └── test_main.py     # Pytest unit tests
├── Dockerfile           # Container image definition
├── requirements.txt     # Python dependencies
└── README.md
```

---

## 🔌 API Endpoints

| Method | Endpoint        | Description            |
|--------|-----------------|------------------------|
| GET    | /               | Service info           |
| GET    | /health         | Health check           |
| GET    | /tasks          | List all tasks         |
| GET    | /tasks/<id>     | Get single task        |
| POST   | /tasks          | Create new task        |
| PUT    | /tasks/<id>     | Update task            |

---

## 🛠️ Local Run

```bash
pip install -r requirements.txt
python app/main.py
# → http://localhost:5000
```

## 🧪 Run Tests

```bash
pytest tests/ -v --cov=app
```

## 🐳 Docker

```bash
docker build -t task-manager:1.0.0 .
docker run -p 5000:5000 task-manager:1.0.0
```

---

## ☁️ CodeArts CI/CD Pipeline Flow

```
CodeArts Req  →  CodeArts Repo  →  CodeArts Check
     ↓                                    ↓
 (Work Items)     (Git Hosting)     (Code Quality)
                                          ↓
                              CodeArts Build (Docker Image)
                                          ↓
                              CodeArts Pipeline (Orchestrate)
                                          ↓
                              CodeArts Deploy (ECS/CCE)
```
