# Django Exam Project: Recipe Management System

## Setup Instructions
1. Clone the repository.
2. Create and activate a virtual environment:
   - `python -m venv venv`
   - `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
3. Install dependencies: `pip install -r requirements.txt`
4. Set your database in setting.py in project folder
5. Run migrations: `python manage.py makemigrations` -> `python manage.py migrate`
6. Run the server: `python manage.py runserver`

## Structure Overview
- `chefs/` - Manages chef profiles, personal details, and related views.
- `recipes/` - Manages recipes, instructions, search functionality, and ingredient and chef relationships.
- `ingredients/` - Manages ingredient items and nutritional values (calories, macros).
- `common/` - Shared utilities and custom form mixins (`DisableFormMixin`).