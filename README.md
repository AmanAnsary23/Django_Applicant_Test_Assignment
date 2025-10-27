# 🧩 Django Applicant Test Assignment

A simple **Job Application Management API** built using **Django REST Framework**.
This project demonstrates core Django concepts such as models, serializers, API design, validation, and JWT authentication.

---

## 🚀 Features

* Applicant, Job, and Application management
* RESTful API endpoints for CRUD operations
* Validation to prevent duplicate job applications
* Search filtering on applicant name and email
* JWT-based authentication (using SimpleJWT)
* Pagination support for list endpoints
* File upload support for resumes

---

## 🏗️ Tech Stack

* **Backend:** Django 5.2.7, Django REST Framework
* **Authentication:** JWT (SimpleJWT)
* **Database:** SQLite (default, can be replaced with PostgreSQL/MySQL)
* **Filtering & CORS:** `django-filter`, `django-cors-headers`
* **Media Handling:** Pillow

---

## ⚙️ Installation and Setup

### 2. Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate    # For Windows
# OR
source venv/bin/activate  # For Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Server will start at:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔐 Environment Variables

You can create a `.env` file (optional) to store environment variables such as:

```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=*
```

Add a `.env.example` file for reference.

---

## 🧾 API Endpoints

<img width="851" height="262" alt="Screenshot 2025-10-28 011905" src="https://github.com/user-attachments/assets/10f3e6f0-665c-4bbc-ab4d-e72fbc693410" />

## 🧪 Validation Rules

* Prevents duplicate applications (same applicant can’t apply twice for the same job)
* Uses `ModelSerializer` for clean validation and error handling
* Returns proper HTTP status codes and error messages

---

## 🧰 Dependencies

---

pip install asgiref <br>
pip install Django <br>
pip install django-cors-headers <br>
pip install django-filter <br>
pip install djangorestframework <br>
pip install djangorestframework_simplejwt <br>
pip install pillow <br>
pip install PyJWT <br>
pip install sqlparse <br>
pip install tzdata <br>

---

## 🧑‍💻 Bonus Features

* JWT Authentication via `djangorestframework_simplejwt`
* Pagination support on list endpoints
* Basic unit tests for one or more API endpoints

---

## Admin 

<img width="1905" height="594" alt="Screenshot 2025-10-28 011717" src="https://github.com/user-attachments/assets/3e18f874-850f-4633-9a45-d33436f36e2e" />

## Applicants

<img width="1881" height="594" alt="applicants" src="https://github.com/user-attachments/assets/e6251175-571b-4b44-aa85-cdb9470baefd" />

## Applications

<img width="1857" height="679" alt="applications" src="https://github.com/user-attachments/assets/0e324213-00c5-4e91-b4ed-5f2e6da5bfbc" />

## Jobs 

<img width="1894" height="685" alt="job" src="https://github.com/user-attachments/assets/5f2a96e5-6549-418b-bc0c-e889b15f52e6" />


## 📦 Project Structure

<img width="563" height="378" alt="Screenshot 2025-10-28 012301" src="https://github.com/user-attachments/assets/97292841-19aa-416c-9caf-a6a9927802ab" />


