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

This is a full-stack Django application that demonstrates:

CRUD operations for Students via UI and REST API

Dashboard / Data Visualization (total students, status breakdown, trends over time)

Third-party API integration (fetches weather data for the “Random Student” feature)

REST API endpoints for all CRUD operations

Live deployment with UI and API synced to the same database

The project showcases full-stack development skills, API integration, and reporting dashboards.

Local Setup

Clone the repository:

git clone https://github.com/your-username/crud_project.git
cd crud_project


Create and activate a virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
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


These variables allow safe configuration of your project for local and production environments.

Database & Migrations

Make migrations:

python manage.py makemigrations


Apply migrations:

python manage.py migrate


Create a superuser (optional, for admin access):

python manage.py createsuperuser

Running the Project

Start the development server:

python manage.py runserver


Frontend UI: http://127.0.0.1:8000/

API Endpoints: http://127.0.0.1:8000/api/students/

⚠️ The development server is for local testing only. Use Gunicorn / Whitenoise for production.

Deployment Notes

Deployed on Render / Heroku (or similar cloud service)

Example live URL: https://crud_app.onrender.com/

UI and API share the same database, so CRUD operations are synchronized.

Production uses DEBUG=False and environment variables for sensitive data.

Testing
1. Test CRUD via UI

Navigate: /students/

Create: Click “Add Student”, fill the form, submit

Read: Student list displays all records

Update: Click “Edit”, modify fields, submit

Delete: Click “Delete”, confirm deletion

2. Test CRUD via REST API

Use Postman / Thunder Client / Curl:

List Students (GET): /api/students/

Retrieve Student (GET): /api/students/<id>/

Create Student (POST):

{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "1234567890",
  "status": "active"
}


Update Student (PUT / PATCH): /api/students/<id>/

Delete Student (DELETE): /api/students/<id>/

3. Test Dashboard / Reporting

Navigate: /dashboard/

Check:

Total students

Active / Inactive breakdown

Students added over time (trend chart)

CRUD operations update the dashboard dynamically.

4. Test Third-Party API Feature

Navigate: /random-students/

Check: Weather data from Open-Meteo API is displayed

Project Structure
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

Technologies Used

Python 3.12

Django 6.x

Django REST Framework

SQLite / PostgreSQL / Supabase

HTML + CSS + Bootstrap

Chart.js (dashboard charts)

Requests (third-party API integration)

Gunicorn + Whitenoise (for production deployment)
