# AuctionLive

Clone the project repository:

```bash
git clone https://github.com/mirmohsen1367/AuctionLive.git
cd AuctionLive
```

## Create and Activate Virtual Environment

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

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Apply Migrations

```bash
python manage.py migrate
```

## Run the Development Server

```bash
python manage.py runserver
```

You can now access the application at:
**[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**


### 🐳 Run with Docker Compose for local
    docker compose up
    Build and start the containers
    Web app: http://127.0.0.1:8000/
    docker compose exec web python manage.py createsuperuser 

### 🐳 Run with Docker Compose for product
    docker compose -f docker-compose.prod.yml up --build
    docker compose exec web python manage.py collectstatic
    docker compose exec web python manage.py createsuperuser     