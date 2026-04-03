# Finance Data Processing and Access Control Backend

A robust, lightweight RESTful API built to manage financial records, generate dashboard analytics, and enforce Role-Based Access Control (RBAC). 

This project was developed as a backend assessment, focusing on clean architecture, data validation, separation of concerns, and maintainability.

## 🚀 Tech Stack

* **Language:** Python 3.x
* **Framework:** FastAPI (Chosen for automatic OpenAPI documentation, speed, and built-in validation)
* **Database:** SQLite (Chosen for simplicity and zero-config local setup)
* **ORM:** SQLAlchemy
* **Data Validation:** Pydantic

## 📂 Project Structure

The project follows a standard layered architecture to ensure separation of concerns:

```text
finance-backend/
├── app/
│   ├── main.py            # Application entry point & setup
│   ├── database.py        # SQLite connection and session management
│   ├── models.py          # SQLAlchemy database schemas (Tables)
│   ├── schemas.py         # Pydantic models for request/response validation
│   ├── dependencies.py    # Middleware/Guards (Role-Based Access Control)
│   └── routers/           # API Endpoints
│       ├── records.py     # CRUD operations for financial records
│       └── dashboard.py   # Aggregated analytics for the dashboard
├── requirements.txt       # Project dependencies
└── README.md              # Documentation

Local Setup Instructions
Clone or unzip the repository and navigate to the root folder:

Bash
cd finance-backend
Create a virtual environment:

Bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
Install the dependencies:

Bash
pip install -r requirements.txt
Run the application:

Bash
uvicorn app.main:app --reload

## 📖 API Documentation (Swagger UI)

Because this project is built with FastAPI, **interactive API documentation is generated automatically.** Once the server is running, open your browser and navigate to:
👉 **http://127.0.0.1:8000/docs**

From the Swagger UI, you can directly test all endpoints (`POST`, `GET`, `PUT`, `DELETE`). 

## 🔐 Access Control & Authentication (Mock)

As per the assignment guidelines allowing for mock authentication, this API uses header-based Role-Based Access Control (RBAC).

To test the permission logic in Swagger UI or Postman, add the following Header to your requests:
* **Key:** `X-User-Role`
* **Value:** `admin`, `analyst`, or `viewer` (Defaults to `viewer` if omitted)

**Enforced Rules:**
* `Viewer`: Can view records and dashboard summaries, but cannot create, edit, or delete records.
* `Analyst`: Can view records, view summaries, and create records. Cannot delete.
* `Admin`: Full access. Only the Admin can delete records.

*(If a user attempts an unauthorized action, the API gracefully returns a `403 Forbidden` error).*

## 🤔 Assumptions & Trade-offs

1.  **Mock Authentication over JWT:** To keep the focus on backend design and logic rather than boilerplate auth setup, a custom dependency (`dependencies.py`) intercepts the `X-User-Role` header to simulate a decoded token's role claim.
2.  **Database Choice:** SQLite was utilized to ensure the evaluators can run the project instantly without needing to configure a PostgreSQL instance or Docker containers. SQLAlchemy makes it trivial to swap this out for Postgres in a production environment.
3.  **User Entity Mapping:** Since a full registration/login flow was out of scope, a mock `user_id = 1` is hardcoded into the `POST /records` route to satisfy the database foreign key constraint. 
4.  **Soft Deletion vs Hard Deletion:** For simplicity in this assessment, records are hard-deleted. In a production financial system, a `is_deleted` boolean flag (soft delete) would be preferred for auditing purposes.