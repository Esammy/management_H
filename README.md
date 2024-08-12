# Hospital API

## Overview

The Hospital API is a RESTful API built using Django and MongoDB, with Celery for asynchronous processing. This project aims to manage hospital admissions, patient data, and staff allocations. The API provides endpoints to query various aspects of hospital operations, including patient admissions, staff allocations, and average patient stay durations.

## Project Setup

### Prerequisites

- Docker
- Docker Compose
- Python 3.8 or later

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Esammy/management_H.git
   cd hospital_api
   ```
2. **Build and Start Docker Containers:**

Ensure Docker and Docker Compose are installed on your system. Build and start the containers by running:

```bash
Copy code
docker-compose build
docker-compose up
```
This will set up the Django application, MongoDB, and Celery worker.

3. **Migrate Database:**

The project uses MongoDB, so there are no traditional migrations. Ensure MongoDB is running and connected properly.

4. **Create Superuser:**

To create a Django superuser for admin access, run:

```bash
Copy code
docker-compose exec web python manage.py createsuperuser
```
5. **Run Tests:**

To run the test suite, use:

```bash
Copy code
docker-compose exec web pytest
```
## API Endpoints

### `/patients/staff/<int:id>/`

- **Method:** GET
- **Description:** Retrieve patients seen by a specific staff member.
- **Parameters:**
  - `id` (required): Staff ID.
- **Returns:** 
  - JSON object containing patient details.

### `/patients/discharged/`

- **Method:** GET
- **Description:** List of patients discharged within 3 days of admission.
- **Returns:** 
  - JSON object containing patient details.

### `/admissions/day/`

- **Method:** GET
- **Description:** Identify the day of the week with the most admissions.
- **Returns:** 
  - JSON object with the name of the day.

### `/patients/staff/avg_duration/`

- **Method:** GET
- **Description:** Calculate the average duration of patients seen by a specific staff member.
- **Parameters:**
  - `id` (required): Staff ID.
- **Returns:** 
  - JSON object with average duration.

## API Documentation
Interactive API documentation is available at:

```bash
Copy code
http://localhost:8000/swagger/
```
## Project Structure

- **`hospital_api/`**: Contains the main Django project settings and configuration.
- **`core/`**: Django app containing models, views, and serializers.
- **`Dockerfile`**: Docker configuration for the Django application.
- **`docker-compose.yml`**: Docker Compose configuration for the entire stack.
- **`requirements.txt`**: List of Python dependencies.
- **`pytest.ini`**: Pytest configuration file.

Asynchronous Processing
Celery is used for background task processing. Ensure the Celery worker is running:

```bash
Copy code
docker-compose up celery
```

```bash
Copy code
docker-compose up celery
```
Troubleshooting
- **`Database Connection Issues`**: Ensure MongoDB is up and running. Check docker-compose logs for errors.
- **`Docker Issues`**: Restart Docker and re-run docker-compose up.
