# ☕ Coffee Shop API

A REST API backend for small coffee shop businesses 
who want to manage their operations without expensive 
software licensing fees.

## Features

- Category and drink management
- Order system with multiple items
- Branch management
- Customer reviews and ratings
- Promotions with discounts
- Favorite drinks per user
- Ingredient tracking with allergen info
- Token authentication
- Custom permissions (Admin/ReadOnly)
- Filtering, search and pagination
- pytest test coverage

## Tech Stack

- Python 3.14
- Django 5.x
- Django REST Framework
- SQLite
- pytest

## Installation

git clone https://github.com/ilybueface/first_orm_project
cd first_orm_project
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## Running Tests

pytest

## API Endpoints

| URL | Method | Permission | Description |
|-----|--------|------------|-------------|
| /coffee/drinks/ | GET | All | List drinks |
| /coffee/drinks/ | POST | Admin | Create drink |
| /coffee/category/ | GET/POST | All/Admin | Categories |
| /coffee/order/ | GET/POST | Authenticated | Orders |
| /coffee/review/ | GET/POST | All/Auth | Reviews |
| /coffee/favorite/ | GET/POST | Authenticated | Favorites |
| /coffee/promotion/ | GET/POST | All/Admin | Promotions |
| /coffee/ingredient/ | GET/POST | All/Admin | Ingredients |
| /token/ | POST | All | Get auth token |

## Author

MRX — Junior Backend Developer
GitHub: github.com/ilybueface