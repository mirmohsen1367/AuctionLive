# 🏷️ AuctionLive

A live auction platform built with Django and Django Channels.

---

## 🚀 Clone the Repository

```bash
git clone https://github.com/mirmohsen1367/AuctionLive.git
cd AuctionLive
```

---

## ⚙️ Create Environment File

Copy the example environment file and edit it as needed:

```bash
cp .env.example .env.dev
```

Then open `.env.dev` in a text editor and update the values (e.g., `SECRET_KEY`, `DATABASE`, etc.).

> 💡 Use `.env.dev` for local development and `.env.prod` for production.

---

## 🐍 Create and Activate Virtual Environment

### 🐧 Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 🪟 Windows (PowerShell)

```powershell
python -m venv venv
venv\Scripts\activate
```

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Apply Migrations

```bash
python manage.py migrate
```

---

## ▶️ Run the Development Server

```bash
python manage.py runserver
```

Access the app at:
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🐳 Run with Docker Compose (Local)

```bash
docker compose up
```

This will build and start the containers.
Once running:

* Web app → **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**
* Create a superuser →

  ```bash
  docker compose exec web python manage.py createsuperuser
  ```

---

## 🐳 Run with Docker Compose (Production)

```bash
docker compose -f docker-compose.prod.yml up --build
```

Then:

```bash
docker compose exec web python manage.py collectstatic
docker compose exec web python manage.py createsuperuser
```

---

## 🧪 Test API Routes

Visit the API documentation at:
👉 **[http://example.com/api/swagger](http://example.com/api/swagger)**

---

## 📝 Notes

* Make sure Docker and Docker Compose are installed.
* Configure your `.env` files before running Docker or Django commands.
* Default database: PostgreSQL (configured via Docker).

---
