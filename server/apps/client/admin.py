# DJango
from django.contrib import admin

# Models
from .models import ShoppingHistory, ShoppingCart

admin.site.register(ShoppingCart),
admin.site.register(ShoppingHistory)