Ah! I understand now — you don’t want the extra `**` that Markdown automatically adds for bold when you copy-paste. You want a **clean, ready-to-paste README** without any extra formatting added by me. I’ll rewrite it **plain Markdown**, fully structured, with headings, code blocks, and lists, but **no extra bolding added outside your text**.

Here’s the clean version:

````markdown
# CRUD App with Django + REST API + Dashboard + Third-Party API

## Table of Contents
1. Project Overview
2. Local Setup
3. Environment Variables
4. Database & Migrations
5. Running the Project
6. Deployment Notes
7. Testing
8. Project Structure
9. Technologies Used

---

## Project Overview

This is a full-stack Django application that demonstrates:

- CRUD operations for Students via UI and REST API
- Dashboard / Data Visualization (total students, status breakdown, trends over time)
- Third-party API integration (fetches weather data for the “Random Student” feature)
- REST API endpoints for all CRUD operations
- Live deployment with UI and API synced to the same database

The project showcases full-stack development skills, API integration, and reporting dashboards.

---

## Local Setup

Clone the repository:

```bash
git clone https://github.com/your-username/crud_project.git
cd crud_project
````

Create and activate a virtual environment:

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Copy the example environment file:

```bash
cp .env.example .env
```

Set the following variables in `.env`:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
DATABASE_URL=postgres://user:password@host:port/dbname
THIRD_PARTY_API_KEY=[your_open_meteo_api_key](https://api.open-meteo.com/v1/forecast)
```

These variables allow safe configuration of your project for local and production environments.

---

## Database & Migrations

Make migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Create a superuser (optional, for admin access):

```bash
python manage.py createsuperuser
```

---

## Running the Project

Start the development server:

```bash
python manage.py runserver
```

Access the app in your browser:

* Frontend UI: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* API Endpoints: [http://127.0.0.1:8000/api/students/](http://127.0.0.1:8000/api/students/)

Note: The development server is for local testing only. Use Gunicorn + Whitenoise for production.

---

## Deployment Notes

* Deployed on Render 
* live URL:https://crud-for-social-booster-media-4.onrender.com/
* UI and API share the same database, so CRUD operations are synchronized
* Production uses DEBUG=False and environment variables for sensitive data

---

## Testing

### 1. Test CRUD via UI

Navigate to: `/students/`

* Create: Click “Add Student”, fill the form, submit
* Read: Student list displays all records
* Update: Click “Edit”, modify fields, submit
* Delete: Click “Delete”, confirm deletion

### 2. Test CRUD via REST API

Use Postman / Thunder Client / Curl:

* List Students (GET):

```
GET /api/students/
```

* Retrieve Student (GET):

```
GET /api/students/<id>/
```

* Create Student (POST):

```json
POST /api/students/
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "1234567890",
  "status": "active"
}
```

* Update Student (PUT / PATCH):

```
PUT /api/students/<id>/
PATCH /api/students/<id>/
```

* Delete Student (DELETE):

```
DELETE /api/students/<id>/
```

### 3. Test Dashboard / Reporting

Navigate to: `/dashboard/`

* Total students
* Active / Inactive breakdown
* Students added over time (trend chart)

CRUD operations update the dashboard dynamically.

### 4. Test Third-Party API Feature

Navigate to: `/random-students/`

* Verify weather data from Open-Meteo API is displayed

---

## Project Structure

```
crud_project/
├── crud_app/                  # Django app
│   ├── migrations/            # Database migrations
│   ├── templates/             # HTML templates (UI)
│   ├── views.py               # Views (UI + API)
│   ├── models.py              # Student model
│   ├── serializers.py         # DRF serializers
│   ├── forms.py               # Forms for CRUD
│   └── urls.py                # App-level URLs
├── crud_project/              # Django project folder
│   ├── settings.py            # Settings (DB, installed apps, etc.)
│   ├── urls.py                # Root URLs
│   └── wsgi.py / asgi.py      # Deployment entry points
├── manage.py                  # Django CLI
├── requirements.txt           # Python dependencies
├── .env.example               # Example environment variables
└── README.md                  # Project documentation
```

---

## Technologies Used

* Python 3.12
* Django 6.x
* Django REST Framework
*PostgreSQL / Supabase
* HTML + CSS
* Dashboard chart
* Requests (third-party API integration)
* Gunicorn + Whitenoise (for production deployment)

```


