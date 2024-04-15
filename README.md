This is a Django REST Framework (DRF) project. Below are the steps to get started.

## Setting up Virtual Environment

It's recommended to use a virtual environment to manage dependencies for your project.

1. Create a virtual environment (venv):

```bash
python3 -m venv myenv
```

2. Activate the virtual environment:

#### On Windows
```bash
myenv\Scripts\activate
```

#### On macOS and Linux
```bash
source myenv/bin/activate
```

## Installing Dependencies

Ensure you are inside the activated virtual environment before installing dependencies.

```bash
pip install -r requirements.txt
```

## Migrations

Before running the project, make sure to apply migrations:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

This will create necessary database tables based on your Django models.

## Running the Project

Once dependencies and migrations are installed, you can run the project using the following command:

```bash
python manage.py runserver
```

This will start the development server at `http://127.0.0.1:8000/`.

## Documentation

API documentation is available via Swagger. Once the server is running, you can access the Swagger UI by navigating to:

```
http://127.0.0.1:8000/swagger/
```

This will display the interactive API documentation where you can explore available endpoints and make requests.
