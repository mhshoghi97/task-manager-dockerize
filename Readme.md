# Task Management Simple Service


```
task_manager/
├── app/
│   ├── __init__.py
│   ├── main.py              # Main Entry Point
│   ├── core/                # Main Settings
│   │   ├── config.py
│   │   └── security.py
│   ├── models/              # Database Models
│   │   ├── user.py
│   │   └── task.py
│   ├── schemas/             # Pydantic schemas
│   │   ├── user.py
│   │   └── task.py
│   ├── api/                 # Endpoints
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   └── tasks.py
│   │   └── dependencies.py
│   ├── services/            # Business Logic
│   │   ├── auth_service.py
│   │   └── task_service.py
│   └── database.py          # Database Settings
├── tests/                   # Test Cases
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_tasks.py
│   └── test_integration.py
├── requirements/
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
├── Dockerfile
├── docker-compose.yml
├── .github/workflows/       # CI/CD Files (Github Integration)
│   ├── ci.yml
│   └── cd.yml
├── .gitignore
├── pytest.ini
├── README.md
└── requirements.txt
```