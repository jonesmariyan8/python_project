# Airbnb Backend Project

This is a full-stack backend application for an Airbnb-like platform built using Django, Django REST Framework, and MySQL. The application provides functionalities for user management, property listings, bookings, reviews, and payments.

## Table of Contents

- [Technologies](#technologies)
- [Setup Instructions](#setup-instructions)
- [Environment Variables](#environment-variables)
- [Database Initialization](#database-initialization)
- [API Overview](#api-overview)
- [Running the Application](#running-the-application)
- [Testing](#testing)

## Technologies

- Django
- Django REST Framework
- MySQL
- Docker
- Docker Compose

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd airbnb-backend
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   Copy the `.env.example` file to `.env` and fill in the required values:
   ```bash
   cp .env.example .env
   ```

5. **Configure MySQL Database**
   Ensure that MySQL is installed and running. Create a database for the application and update the database settings in the `.env` file.

## Database Initialization

To initialize the database, run the SQL script provided in the `scripts/init_db.sql` file. This script creates the necessary tables and inserts initial data.

```sql
-- Example SQL commands
CREATE TABLE users (...);
CREATE TABLE listings (...);
-- Add other necessary tables
```

## API Overview

The application exposes several RESTful API endpoints for managing users, listings, bookings, reviews, and payments. Refer to the `docs/api_openapi.yml` file for detailed API specifications.

## Running the Application

To run the application, use the following command:

```bash
python manage.py runserver
```

Alternatively, you can use Docker to run the application:

1. Build the Docker image:
   ```bash
   docker-compose build
   ```

2. Start the application:
   ```bash
   docker-compose up
   ```

## Testing

Unit and integration tests are located in the `tests/unit` and `tests/integration` directories, respectively. To run the tests, use the following command:

```bash
python manage.py test
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.