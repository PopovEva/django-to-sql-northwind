# Django Project with REST API and MySQL Integration

This repository contains a simple Django project setup with Django Rest Framework, connected to a MySQL database. The project uses the Northwind database and demonstrates basic API functionality.

## Repository

[GitHub Repository](https://github.com/PopovEva/django-to-sql-northwind.git)

## Features

- **Django Framework**: Utilizes Django 5.0.7 for backend development.
- **REST API**: Implements Django Rest Framework for creating RESTful APIs.
- **MySQL Integration**: Connects to a MySQL database, specifically using the Northwind sample database.
- **Basic API Endpoint**: Demonstrates a basic API endpoint that returns a JSON response.
- **Admin Interface**: Includes Django's default admin interface for managing models and data.

## Technologies Used

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django Rest Framework (DRF)**: A powerful and flexible toolkit for building Web APIs.
- **MySQL**: An open-source relational database management system.
- **Python**: The programming language used for developing this project.

## Installation

### Prerequisites

- Python 3.x
- MySQL server
- MySQL client for Python

### Steps to Set Up the Project

1. **Clone the repository:**

    ```bash
    git clone https://github.com/PopovEva/django-to-sql-northwind.git
    cd django-to-sql-northwind
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the MySQL database:**

    Ensure that you have a MySQL server running and create a database named `northwind`. Update the `DATABASES` setting in `myproj/settings.py` if necessary.

    ```sql
    CREATE DATABASE northwind;
    CREATE USER 'root'@'localhost' IDENTIFIED BY 'yourpassword';
    GRANT ALL PRIVILEGES ON northwind.* TO 'root'@'localhost';
    FLUSH PRIVILEGES;
    ```

5. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

### Running the Project

    After setting up the project and database, run the development server using:

    ```bash
    python manage.py runserver  
    ```
You can access the Django administration site at http://127.0.0.1:8000/admin/ and the API endpoint at http://127.0.0.1:8000/.      

API Endpoints  

GET /: Returns a simple JSON response.
CRUD Endpoints: Endpoints to create, read, update, and delete resources.
Contributing  

Feel free to fork this repository and submit pull requests. Any contributions are welcome!

License
This project is licensed under the MIT License.  



