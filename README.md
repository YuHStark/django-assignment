# Django Product Assignment

A Django web application that allows users to search products by description, category, and tags.

## Data populations

The database (db.sqlite3) is included in this repository and already have 5 categories, 10 tags, and 20 products as sample data.

## Prerequisites

- Python version: 3.x
- pip

## Installation

1. Clone the repository
   - `git clone`
   - `cd ./DjangoAssignment/productInfo`
2. Create and activate a virtual environment (optional)
   - `python -m venv venv`
   - `source venv/bin/activate` (Mac/Linux)
   - `venv\Scripts\activate` (Windows)
3. Install dependencies
   - `pip install django`
4. Run migrations
   `python manage.py migrate`
5. Start the development server
6. `python manage.py runserver`
7. Open your browser and go to http://127.0.0.1:8000

## AI usage:

Used Claude to assist with reviewing code and identifying bugs in views.py and product_list.html