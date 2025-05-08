# E-Commerce Platform

A fully functional e-commerce system for selling and tracking products, built with **Django** and **PostgreSQL**.

## Overview
This project provides a robust platform for managing an online store, including product listings, inventory tracking, and user management. It’s developed using Django (Python web framework) and PostgreSQL (database).

## Prerequisites
Before running the project, ensure you have the following installed:
- **Python 3.8+** (recommended: 3.10)
- **PostgreSQL 12+**
- **Git**

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/ecommerce-project.git
cd ecommerce-project

2. Set Up a Virtual Environment
Create and activate a virtual environment to manage dependencies:

python -m venv .venv
# On Windows
.\.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

3. Install Dependencies
Install the required Python packages using the provided commands:

pip install altair
pip install django-import-export
python -m pip install Pillow
pip install django
pip install psycopg2


4. Configure PostgreSQL Database
Ensure PostgreSQL is running on your machine.
Create a database for the project:

psql -U postgres
CREATE DATABASE ecommerce_db;
\q

from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

5. Apply Migrations
Run Django migrations to set up the database schema:



python manage.py makemigrations
python manage.py migrate
6. Create a Superuser (Optional)
Create an admin user to access the Django admin panel:




python manage.py createsuperuser
Follow the prompts to set up your username, email, and password.

7. Run the Development Server
Start the Django development server:


python manage.py runserver

Open your browser and go to http://127.0.0.1:8000/ to see the application.
Access the admin panel at http://127.0.0.1:8000/admin/ using the superuser credentials.

Contributing
Feel free to fork this repository, make improvements, and submit pull requests. For major changes, please open an issue to discuss.

Contact
For questions or feedback, reach out via LinkedIn: https://www.linkedin.com/in/fady-ibrahim-629ab8277/
Or via Emial: fadymagdy159@gmail.com

Developed by Fady Magdy | AI Enthusiast | Developer with ML & DL