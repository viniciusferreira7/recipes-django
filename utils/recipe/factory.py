from random import randint
from typing import TypedDict
from datetime import datetime

from faker import Faker

fake = Faker('pt_BR')


def rand_ratio():
    return randint(840, 900), randint(473, 573)


class Author(TypedDict):
    first_name: str
    last_name: str


class Category(TypedDict):
    name: str


class Cover(TypedDict):
    url: str


class Recipe(TypedDict):
    id: int
    title: str
    description: str
    preparation_time: int
    preparation_time_unit: str
    servings: int
    servings_unit: str
    preparation_steps: str
    created_at: datetime
    author: Author
    category: Category
    cover: Cover


FOOD_TAGS = [
    "food", "pizza", "burger", "pasta", "cake", "salad",
    "steak", "sushi", "sandwich", "dessert", "chocolate",
    "ramen", "tacos", "soup", "bread", "fruits"
]


def random_food_tag():
    return fake.random_element(FOOD_TAGS)


def make_recipe() -> Recipe:
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutes',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porção',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
           'url': f"https://loremflickr.com/{rand_ratio()[0]}/{rand_ratio()[1]}/{random_food_tag()}"
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())
