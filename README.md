# Jobapplicationapp
A web application built with **Django** that helps users organize and track their job applications. Users can log company details, job title, application date, status, and notes — all in one centralized dashboard.

---

## 🚀 Features

- 👤 **User Authentication** (Sign up, Login, Logout)
- 📂 **Job Application Management**
  - Add a new job application
  - View all applications
  - Edit or update an application
  - Delete an application
- 📊 **Dashboard Overview** (Number of applications by status: applied, interviewing, rejected, etc.)

---

## 🛠️ Tech Stack

- **Backend**: Django, Django Rest Framework
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Frontend**: Django Templates (can extend to React or Vue later)
- **Authentication**: Django’s built-in auth system

---

## 📁 Project Structure

job-application-tracker/
├── manage.py
├── my_job_tracker_project/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── apps/
│ ├── users/
│ │ ├── models.py
│ │ ├── views.py
│ │ └── urls.py
│ └── applications/
│ ├── models.py
│ ├── views.py
│ └── urls.py
├── templates/ # HTML templates
├── static/ # CSS, JS, Images
├── requirements.txt
└── README.md

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/job-application-tracker.git
   cd job-application-tracker

python -m venv venv
venv\Scripts\activate   

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate


python manage.py runserver

http://127.0.0.1:8000/
🔑 API Endpoints
User Endpoints
POST /api/users/signup/ → Register a new user

POST /api/users/login/ → Login user

POST /api/users/logout/ → Logout user

Job Application Endpoints
GET /api/applications/ → List all job applications

POST /api/applications/ → Create a new job application

GET /api/applications/<id>/ → Retrieve a job application

PUT /api/applications/<id>/ → Update a job application

DELETE /api/applications/<id>/ → Delete a job application
