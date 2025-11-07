# ⚠️ WIP

# Django Study Project

A study project to learn Python and Django through Udemy courses.

## Description

This project was created to practice and consolidate web development knowledge with Python and the Django framework.

## Requirements

- Python 3.8+
- pip (Python package manager)
- Virtualenv (optional, but recommended)

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd first-app-django
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Configuration

### 1. Environment Variables

Create a `.env` file in the project root with the necessary variables:

```bash
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 2. Apply Migrations

```bash
python manage.py migrate
```

### 3. Create Superuser (optional)

```bash
python manage.py createsuperuser
```

## Running the Project

To start the development server:

```bash
python manage.py runserver
```

The project will be available at `http://127.0.0.1:8000/`

## Project Structure

```
first-app-django/
├── manage.py
├── README.md
├── .gitignore
├── requirements.txt
└── [Django apps]
```

## Testing

To run the tests:

```bash
python manage.py test
```

## Technologies Used

- **Framework**: Django
- **Language**: Python
- **Database**: SQLite (development)

## Contributing

This is a personal study project. Feel free to fork and experiment!

## License

This project is provided as learning material.

## Author

Vinic - Studying Python and Django through Udemy courses

## Notes

- This is a project in development
- Intended exclusively for educational purposes
- Passwords and secret keys should never be committed to the repository
