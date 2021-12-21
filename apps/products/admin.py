# DJango
from django.contrib import admin

# Models
from .models import  Product, Colors, Waist,Category, Event, Images

class ImagesAdmin(admin.TabularInline):
    model = Images
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImagesAdmin
    ]

admin.site.register(Colors)
admin.site.register(Waist)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Event)



