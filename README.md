# ⚠️ WIP

# Recipes Django

A recipe management web application built with Django as a study project.

## Description

This project is a recipe sharing platform that allows users to browse, view, and organize recipes by categories. Created to practice and consolidate web development knowledge with Python and the Django framework.

## Features

- **Recipe Listing**: Browse all published recipes on the home page
- **Recipe Details**: View complete recipe information including preparation steps, time, and servings
- **Category Organization**: Filter recipes by categories
- **Category Pages**: Dedicated pages for each category showing all related recipes
- **Responsive Design**: Clean, modern UI with CSS styling
- **Admin Panel**: Manage recipes, categories, and users through Django admin

## Requirements

- Python 3.8+
- pip (Python package manager)
- Virtualenv (optional, but recommended)

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd recipes-django
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
recipes-django/
├── manage.py
├── README.md
├── .gitignore
├── requirements.txt
├── recipes/                    # Main app
│   ├── migrations/            # Database migrations
│   ├── static/
│   │   └── recipes/
│   │       └── css/
│   │           └── styles.css # Recipe and category styles
│   ├── templates/
│   │   └── recipes/
│   │       ├── pages/
│   │       │   ├── home.html       # Recipe listing page
│   │       │   ├── recipe-view.html # Recipe detail page
│   │       │   └── category.html   # Category page
│   │       └── partials/
│   │           ├── recipe.html     # Recipe card component
│   │           ├── header.html
│   │           ├── footer.html
│   │           └── search.html
│   ├── models.py              # Recipe and Category models
│   ├── views.py               # View functions
│   ├── urls.py                # App URL routing
│   └── admin.py               # Admin configuration
├── base_static/               # Global static files
│   └── global/
│       └── css/
└── project/                   # Project settings
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## Models

### Category
- `id`: UUID (Primary Key)
- `name`: CharField (max 65 characters)
- `created_at`: DateTimeField (auto-generated)

### Recipe
- `id`: UUID (Primary Key)
- `title`: CharField (max 65 characters)
- `description`: CharField (max 165 characters)
- `slug`: SlugField (unique)
- `preparation_time`: IntegerField
- `preparation_time_unit`: CharField (choices: Minute, Hour, Day)
- `servings`: IntegerField
- `servings_unit`: CharField (choices: Gram, Milliliter, Unit, Slice)
- `preparation_steps`: TextField
- `is_preparation_steps_html`: BooleanField
- `created_at`: DateTimeField (auto-generated)
- `updated_at`: DateTimeField (auto-updated)
- `is_published`: BooleanField
- `cover`: ImageField
- `category`: ForeignKey to Category
- `author`: ForeignKey to User

## Testing

To run the tests:

```bash
python manage.py test
```

## URL Routes

- `/` - Home page (recipe listing)
- `/recipes/<uuid:id>/` - Recipe detail page
- `/recipes/category/<uuid:category_id>/` - Category page with filtered recipes
- `/admin/` - Django admin panel

## Technologies Used

- **Framework**: Django
- **Language**: Python
- **Database**: SQLite (development)
- **Frontend**: HTML5, CSS3, Font Awesome icons

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
