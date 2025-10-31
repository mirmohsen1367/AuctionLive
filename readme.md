# AuctionLive

## 🧩 Clone the Repository

```bash
git clone https://github.com/mirmohsen1367/AuctionLive.git
cd AuctionLive
```

---

## 🐍 Python Version

This project uses **Python 3.12**.
Make sure it’s installed before proceeding.

---

## ⚙️ Environment Setup

Copy the example environment file to create your local configuration:

```bash
cp .env.example .env
cp .env.example .env.dev
```

Then edit the values inside `.env` and `.env.dev` according to your environment.

---

## 🌱 Create and Activate Virtual Environment

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

## 🧱 Apply Migrations

```bash
python manage.py migrate
```

---

## 🚀 Run the Development Server

```bash
python manage.py runserver
```

Access the app at:
**[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🐳 Run with Docker Compose (Development)

```bash
docker compose up
```

* Web app: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🏗️ Run with Docker Compose (Production)

```bash
docker compose -f docker-compose.prod.yml up 
docker compose exec web python manage.py collectstatic
```

---

## 👤 Create Superuser (Stage)

After the containers are running or migrations are applied, create an admin user:

```bash
python manage.py createsuperuser
```

or (for Docker):

```bash
docker compose exec web python manage.py createsuperuser
```

---

## 🧪 Test API Routes

You can view the API documentation at:

```
http://127.0.0.1:8000/api/swagger/
```

---

✅ **You’re all set!** Your AuctionLive Django app should now be running locally or via Docker.
