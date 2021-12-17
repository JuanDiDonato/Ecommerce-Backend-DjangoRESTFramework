from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import AutoField, BooleanField, CharField, FloatField, IntegerField, TextField, DateField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey, ManyToManyField


# Events model
class Event(models.Model):

    id = AutoField(primary_key=True)
    name = CharField(max_length=255,unique=True,null=False,blank=False)
    discount = IntegerField(null=True,blank=False)
    from_date = DateField(auto_now_add=False,auto_now=False)
    to_date = DateField(auto_now_add=False,auto_now=False)

    class Meta :
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return f'Evento: {self.name}'

# Categories of products
class Category(models.Model):
    id = AutoField(primary_key=True)
    category_name = CharField(max_length=255,null=False,blank=False,unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return f'Categoria: {self.category_name}'

# Product 
class Product(models.Model):

    id = AutoField(primary_key=True)
    title = CharField(max_length=255,unique=True,null=False,blank=False)
    description = TextField(null=True,blank=False)
    price = FloatField(max_length=255,null=True,blank=False,default=0)
    image = ImageField(upload_to='assets/img/',null=True,blank=True)
    disable = BooleanField(default=False)
    category = ForeignKey(Category,on_delete=SET_NULL,null=True)
    event = ForeignKey(Event,on_delete=SET_NULL,null=True)
    ids_colors = ManyToManyField('Colors',blank=True)

    class Meta :
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title

# Colors 
class Colors(models.Model):

    id_color = AutoField(primary_key=True)
    color = CharField(max_length=255,null=True,blank=False)
    id_talle = ForeignKey('Waist',on_delete=CASCADE,null=True,blank=True)
    
    class Meta:
        verbose_name = 'Waist and color'
        verbose_name_plural = 'Waists and colors'

    def __str__(self):
        return f'{self.color}'

# Waist
class Waist(models.Model):
    id_waist = AutoField(primary_key=True)
    stock_s = IntegerField(null=True,blank=True)
    stock_m = IntegerField(null=True,blank=True)
    stock_l = IntegerField(null=True,blank=True)
    stock_xl = IntegerField(null=True,blank=True)
    stock_xxl = IntegerField(null=True,blank=True)
    stock_xxxl = IntegerField(null=True,blank=True)

    class Meta:
        verbose_name = 'waist'
        verbose_name_plural = 'waists'

    def __str__(self):
        return str(self.id_waist)
