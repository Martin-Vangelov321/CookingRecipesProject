# Django Exam Project: Recipe Management System

## Setup Instructions
1. Clone the repository.
2. Create and activate a virtual environment:
   - `cd (project folder name)`
   - `python -m venv venv`
   - `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
3. PyCharm Virtual Environment & Interpreter Setup (Optional/Troubleshooting):
   - `If you open the project in PyCharm and see a "Invalid Python Interpreter" warning, configure it manually:`
   - `Click on configure python interpreter (or go to File -> Settings -> Python Interpreter).`
   - `Select Add New -> Select existing.`
   - `Browse to your project folder and select the Python executable inside your virtual environment: `venv\Scripts\python.exe` (Windows) or `venv/bin/python` (Mac/Linux).`
4. Install dependencies: `pip install -r requirements.txt`
5. Set your database in setting.py in project folder not necessary
6. Run migrations: `python manage.py makemigrations` -> `python manage.py migrate`
7. Run the server: `python manage.py runserver`

## Structure Overview
- `chefs/` - Manages chef profiles, personal details, and related views.
- `recipes/` - Manages recipes, instructions, search functionality, and ingredient and chef relationships.
- `ingredients/` - Manages ingredient items and nutritional values (calories, macros).
- `common/` - Shared utilities and custom form mixins (`DisableFormMixin`).