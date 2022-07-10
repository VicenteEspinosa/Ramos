from backend_app.db_helpers.form_tree_helpers import get_category_name
from backend_app.db_models.client import Client
import string
import random


def create_token():
    letters = string.ascii_letters
    digits = string.digits
    total = letters + digits
    token = ""
    for _ in range(10):
        token += random.choice(total)
    return token

def create_new_client(category_id):
    client = Client(id=int(category_id),name= get_category_name(category_id),
                    category=category_id, token= create_token())

    client.save()
