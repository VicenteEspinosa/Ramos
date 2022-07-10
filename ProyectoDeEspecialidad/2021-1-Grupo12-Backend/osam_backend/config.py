import os

from dotenv import load_dotenv

load_dotenv()

# Set a fixed string for development. Not suitable for production!
os.environ.setdefault('B_DJANGO_SECRET_KEY', 'development-key')
os.environ.setdefault('CATEGORY_0_TOKEN', 'category-0-token')
os.environ.setdefault('CATEGORY_1_TOKEN', 'category-1-token')

DJANGO_SECRET_KEY = os.environ['B_DJANGO_SECRET_KEY']
MONGO_URI = os.environ['B_MONGO_URI']
CATEGORY_0_TOKEN = os.environ["CATEGORY_0_TOKEN"]
CATEGORY_1_TOKEN = os.environ["CATEGORY_1_TOKEN"]