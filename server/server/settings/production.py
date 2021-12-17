import os

# Dotenv
from dotenv import load_dotenv

# Base settings
from .base import *

load_dotenv()

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
