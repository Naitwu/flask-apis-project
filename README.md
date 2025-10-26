# Flask API Project with Docker

## Overview
This project is a Flask-based API application designed to be containerized using Docker. It includes features such as user authentication, database migrations, and a modular structure for scalability.

## Features
- **Flask Framework**: Lightweight and flexible web framework.
- **SQLAlchemy**: ORM for database interactions.
- **Flask-Migrate**: Database migrations using Alembic.
- **JWT Authentication**: Secure user authentication with JSON Web Tokens.
- **Dockerized**: Easily deployable using Docker and Docker Compose.

## Project Structure
```
app.py                # Main application entry point
blocklist.py          # JWT blocklist for token revocation
db.py                 # Database initialization
Dockerfile            # Docker image configuration
docker-compose.yml    # Docker Compose configuration
requirements.txt      # Python dependencies
schemas.py            # Marshmallow schemas
migrations/           # Database migration scripts
models/               # Database models
resources/            # API resource endpoints
```

## Prerequisites
- Docker and Docker Compose installed
- Python 3.13 or higher (if running locally)

## Installation

### Using Docker
1. Build the Docker image:
   ```bash
   docker-compose build
   ```
2. Start the application:
   ```bash
   docker-compose up
   ```
3. The API will be available at `http://localhost:5000`.

### Running Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/Naitwu/flask-apis-project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd flask-docker
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the application:
   ```bash
   flask run
   ```

## Environment Variables
The following environment variables can be configured:
- `FLASK_APP`: Entry point for the Flask application (default: `app`)
- `FLASK_ENV`: Environment mode (`development` or `production`)
- `DATABASE_URL`: Database connection string

## Database Migrations
To manage database migrations:
1. Initialize migrations:
   ```bash
   flask db init
   ```
2. Generate a migration script:
   ```bash
   flask db migrate -m "Migration message"
   ```
3. Apply migrations:
   ```bash
   flask db upgrade
   ```

## API Endpoints
The application includes the following endpoints:
- `/items`: Manage items
- `/stores`: Manage stores
- `/tags`: Manage tags
- `/users`: Manage users

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Created by Naitwu.