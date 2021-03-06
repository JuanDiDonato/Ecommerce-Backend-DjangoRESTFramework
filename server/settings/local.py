import os

# Dotenv
from dotenv import load_dotenv

# Base settings
from .base import *

load_dotenv()

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost'
]

STATIC_ROOT = BASE_DIR / 'media'

# Database MySQL
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': '',
        'HOST' : os.getenv('DATABASE_HOST'),
    }
}
"""


# Database SQLite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


