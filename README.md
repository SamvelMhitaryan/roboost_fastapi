# 📁 Roboost

## 📖 Кратко о проекте

Переписанный в целях обучения с Django на FastAPI проект кофейни "Робуст".
Является первым проектом на FastApi. Цель: освоение таких технологий как 
FastApi, alembic, SQLAlchemy, uvicorn, pydantic. 
---

## 🧾 TODO список (основные положения)

- [x] Настроить инициализацию проекта FastAPI с использованием Uvicorn для асинхронки.
- [x] Создать модели SQLAlchemy для основных сущностей приложения.
- [x] Использовать Alembic для управления миграциями базы данных.
- [x] Реализовать CRUD операции для основных сущностей приложения.

---


## 💻 Запуск проекта

1. Загрузка проекта и переход в директорию 

```bash
git clone git@github.com:SamvelMhitaryan/roboost_fastapi.git
```

2. Создание виртуального окружения (venv): 

```bash
python3 -m venv venv
```

3. Активация виртуального окружения (venv): 

Linux / Mac
```bash
. venv/bin/activate
```

Windows
```bash
. venv\scripts\activate
```

4. Установка зависимостей: 

```bash
pip install -r requirements.txt
```

5. Запуск: 

```bash
python3 main.py
```
