# Django
from django.contrib import admin

# Models
from .models import User, Role

admin.site.register(User)
admin.site.register(Role)
