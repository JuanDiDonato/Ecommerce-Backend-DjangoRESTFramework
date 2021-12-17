from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import F
from django.db.models.fields import AutoField, CharField, DateField, IntegerField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey, ManyToManyField

# Models
from apps.products.models import Product
from apps.users.models import User
from apps.mod.models import Status

class ShoppingCart(models.Model):
    id_cart = AutoField(primary_key=True)
    user = ForeignKey(User,on_delete=CASCADE,null=True,blank=True)  # One user have one cart
    color = CharField(max_length=255,null=False,blank=False)
    waist = CharField(max_length=255,null=False,blank=False)
    quantity = IntegerField(null=False,blank=False,default=1)
    product = ForeignKey(Product,on_delete=CASCADE,null=False,blank=False)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return f'Carrito de {str(self.user)}'

class ShoppingHistory(models.Model):
    id_history = AutoField(primary_key=True)
    date_purchase = DateField(auto_now=False,auto_now_add=True)
    color = CharField(max_length=255,null=False,blank=False)
    waist = CharField(max_length=255,null=False,blank=False)
    user = ForeignKey(User,on_delete=CASCADE,null=True,blank=True)
    quantity = IntegerField(null=False,blank=False,default=1)
    product = ForeignKey(Product,on_delete=CASCADE,null=False,blank=False)
    status = ForeignKey(Status,on_delete=SET_NULL,null=True)

    class Meta:
        verbose_name = 'History'
        verbose_name_plural = 'Purchases'

    def __str__(self):
        return f'Historial de {str(self.user)}'
