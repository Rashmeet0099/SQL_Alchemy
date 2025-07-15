# SQL_Alchemy


SQLAlchemy ORM Project with PostgreSQL
======================================

This is a simple SQLAlchemy 2.0 ORM project using **PostgreSQL** that demonstrates how to:

- Declare ORM models
- Create and connect to a PostgreSQL database
- Create tables
- Insert and query data
- Use relationships (One-to-Many)


Project Structure
-----------------
sqlalchemy_project/
├── models.py         # ORM classes (User, Address)
├── database.py       # PostgreSQL engine & session setup
├── main.py           # Script to create tables and perform operations
├── requirements.txt  # Required Python packages
└── README.txt         # Project documentation


PostgreSQL Setup
----------------
Make sure you have PostgreSQL installed and a database created.

    sudo service postgresql start
    createdb your_database

Update your PostgreSQL credentials in `database.py`:

    DATABASE_URL = "postgresql+psycopg2://username:password@localhost:5432/your_database"


Installation
------------
1. Clone the repository:

    git clone https://github.com/yourusername/sqlalchemy-project.git
    cd sqlalchemy-project

2. (Optional) Create a virtual environment:

    python -m venv venv
    source venv/bin/activate

3. Install dependencies:

    pip install -r requirements.txt


How to Run
----------
    python main.py

- Creates tables in your PostgreSQL database
- Adds users and their email addresses
- Performs simple SELECT queries


Dependencies
------------
- SQLAlchemy 2.0.41
- psycopg2-binary 2.9.9 (for PostgreSQL)

Install via:

    pip install sqlalchemy psycopg2-binary


License
-------
MIT License


Author
------
Rashmeet Singh
