# Multi-Database Django DRF Project and Mutil-Project

## Overview
This project is a Django REST Framework (DRF) application that utilizes multiple databases. Also it runs two projects at same with two admin panels.

## Features
- Uses Django's **database routing** to manage multiple databases.
- Stores LahoreHotel data in the **default** database.
- Stores IslamabadHotel data in the **secondary** database.
- Implements **Django REST Framework (DRF)** for API endpoints.
- One project with different admin panel is running in it.
---

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/husnainhashmi5/multi_db_project.git
cd multi_db_project
```

### 2. Create and Activate a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

---

## Database Configuration

### 1. Configure `settings.py`
In `settings.py`, define multiple databases.

### 2. Setup Database Router (`api/db_router.py`) for the models,apps,project
### 3. Add Router to `settings.py`
```python
DATABASE_ROUTERS = ['api.db_router.MyDatabaseRouter']
```
### 4. Run Migrations according to database name
```sh
python manage.py migrate --database=default
python manage.py migrate --database=secondary
```

---

## Running the Project
### 1. Start the Development Server
```sh
python manage.py runserver
```

## Contributing
Feel free to submit issues and pull requests.

## License
MIT License
