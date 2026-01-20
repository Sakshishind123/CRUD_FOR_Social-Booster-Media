CRUD App with Django + REST API + Dashboard + Third-Party API
Table of Contents

Project Overview

Local Setup

Environment Variables

Database & Migrations

Running the Project

Deployment Notes

Testing

Project Structure

Technologies Used

Project Overview

This project is a full-stack Django application with the following features:

CRUD operations for Students (UI + REST API)

 Data Visualization (e.g., total students, status breakdown, trends over time)

Third-party API integration (fetches weather data for “Random Student” feature)

REST API endpoints for all CRUD operations

Live deployment using the same database as the UI

The project demonstrates full-stack development skills, API integration, and real-world reporting dashboards.

Local Setup

Clone the repository:

git clone https://github.com/your-username/crud_project.git
cd crud_project


Create and activate a virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate


Install Python dependencies:

pip install -r requirements.txt

Environment Variables

Copy .env.example to .env:

cp .env.example .env


Set the following variables:

SECRET_KEY=your-django-secret-key
DEBUG=True
DATABASE_URL=postgres://user:password@host:port/dbname
THIRD_PARTY_API_KEY=your_api_key_here

Database & Migrations

Make migrations:

python manage.py makemigrations


Apply migrations:

python manage.py migrate


Create a superuser (optional, for admin access):

python manage.py createsuperuser

Running the Project Locally

Start the server:

python manage.py runserver


Access the app in your browser:

Frontend UI: http://127.0.0.1:8000/

API endpoints: http://127.0.0.1:8000/api/students/

Deployment Notes

Deployed on Render / Heroku / any live server

Example live URL: https://crud_app.onrender.com/

UI and API use the same database, so CRUD operations are synced

How to Test
1. Test CRUD via UI

Navigate to http://127.0.0.1:8000/students/

Create: Click “Add Student”, fill the form, submit

Read: Students list displays all records

Update: Click “Edit”, update fields, submit

Delete: Click “Delete”, confirm deletion

2. Test CRUD via REST API

List Students (GET):

GET /api/students/


Retrieve Student (GET):

GET /api/students/<id>/


Create Student (POST):

POST /api/students/
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "1234567890",
  "status": "active"
}


Update Student (PUT/PATCH):

PUT /api/students/<id>/
PATCH /api/students/<id>/


Delete Student (DELETE):

DELETE /api/students/<id>/


Tip: Use Postman / Thunder Client / Curl for testing API requests.

3. Test Dashboard / Reporting

Open: http://127.0.0.1:8000/dashboard/

Check:

Total students

Active / Inactive status breakdown

Students added over time (trend chart)

CRUD operations update the dashboard dynamically

4. Test Third-Party API Feature

Open: http://127.0.0.1:8000/random-students/

Verify weather data from external API (Open-Meteo) is displayed

Project Structure
crud_project/
├── crud_app/                  # Django app
│   ├── migrations/            # DB migrations
│   ├── templates/             # HTML templates
│   ├── views.py               # Views (UI + API)
│   ├── models.py              # Models (Student)
│   ├── serializers.py         # DRF serializers
│   ├── forms.py               # Forms for CRUD
│   └── urls.py                # App-level URLs
├── crud_project/              # Django project folder
│   ├── settings.py            # Settings (DB, installed apps, etc.)
│   ├── urls.py                # Root URLs
│   └── wsgi.py / asgi.py      # Deployment entry points
├── manage.py                  # Django CLI
├── requirements.txt           # Python dependencies
└── README.md                  # This file

Technologies Used

Python 3.12

Django 6.x

Django REST Framework

SQLite / PostgreSQL / Supabase

HTML + CSS + Bootstrap (frontend)

Chart.js (dashboard charts)

Requests (third-party API integration)

Gunicorn + Whitenoise (for deployment)
