STUDENTS MANAGEMENT SYSTEM
==========================

A backend Students Management System built with FastAPI and PostgreSQL.
This project provides RESTful APIs for managing student records and
demonstrates database integration using SQLAlchemy.

TECHNOLOGIES USED
-----------------
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn

FEATURES
--------
- Add new students
- View all students
- View student by ID
- Update student information
- Delete students
- Data validation using Pydantic
- PostgreSQL database integration
- SQLAlchemy ORM
- RESTful API architecture
- Interactive API documentation

PROJECT STRUCTURE
-----------------
Students-Management-System/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── routers/
│   └── students.py
├── .env
├── requirements.txt
└── README.txt

INSTALLATION
------------

1. Clone the repository:

   git clone <your-github-repository-url>

2. Create a virtual environment:

   python -m venv env

3. Activate the virtual environment:

   Windows:
   env\Scripts\activate

4. Install dependencies:

   pip install -r requirements.txt

5. Configure your PostgreSQL database and create a .env file.

6. Run the application:

   uvicorn main:app --reload

API DOCUMENTATION
-----------------
After starting the server, open:

Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc

DATABASE
--------
This project uses PostgreSQL as the database and SQLAlchemy as the ORM
for performing database operations.

LEARNING OUTCOMES
-----------------
Through this project, I practiced:

- FastAPI backend development
- REST API design
- CRUD operations
- SQLAlchemy ORM
- PostgreSQL database integration
- Pydantic data validation
- API documentation
- Backend project structure

PROJECT STATUS
--------------
Completed

AUTHOR
------
Tariq Ahmed

Backend Developer | FastAPI Enthusiast
Building APIs | Learning Cloud & AI
