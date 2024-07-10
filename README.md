# Student Management System

A web application for managing student information, including Create, Read, Update, and Delete (CRUD) operations, built with Flask and SQLite.

## Table of Contents

- [Setup](#setup)
- [Run](#run)
- [Test](#test)
- [Project Structure](#project-structure)

## Setup

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- Flask
- SQLite

1. **Create and activate a virtual environment:**
2.**Install the required packages:**
3.**Set up the database:**

## Run
The application will be accessible at http://127.0.0.1:5000/.

## Test
1. Ensure the server is running
2. Use the web browser to access the application:

Add a student by filling out the form on the home page.
View the list of students at http://127.0.0.1:5000/StuList.
Update or delete student details by using the respective buttons on the student list page.
Retrieve student details by entering their ID on the detail page.


## Project Structure
yourrepository/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   ├── parent.html
│   │   ├── index.html
│   │   ├── Stu_list.html
│   │   ├── detail.html
│   │   └── update.html
│   ├── static/
│   │   ├── css/
│   │   └── images/
│   └── ...
├── venv/
├── .gitignore
├── requirements.txt
└── README.md
## Technologies Used
Flask
SQLAlchemy
SQLite
Bootstrap (for styling)
