import os

# Dotenv
from dotenv import load_dotenv

# Base settings
from .base import *

load_dotenv()

DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost'
]

STATIC_ROOT = BASE_DIR / 'media'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST' : os.getenv('DATABASE_HOST'),
    }
}

# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)