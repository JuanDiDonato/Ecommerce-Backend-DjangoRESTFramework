from django.db import models
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL
from django.db.models.fields import AutoField, CharField, DateField, FloatField, IntegerField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from apps.products.models import Product
from apps.users.models import User

# Stauts of purchase
class Status(models.Model):
    status_name = CharField(max_length=255,null=False,blank=False)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return self.status_name

# Pending shipments
class PendingShipments(models.Model):
    id = AutoField(primary_key=True)
    product = ForeignKey(Product,on_delete=SET_DEFAULT,null=True,default=str(Product.title))
    quantity = IntegerField(null=False,blank=False)
    waist = CharField(max_length=255,blank=False,null=False)
    color = CharField(max_length=255,blank=False,null=False)
    user = ForeignKey(User,on_delete=CASCADE,null=False,blank=False)
    status = ForeignKey(Status,on_delete=SET_NULL,null=True)

    class Meta:
        verbose_name = 'Pending shipment'
        verbose_name_plural = 'Pendings shipments'

    def __str__(self):
        return f'Envio/s para {str(self.user)}'

# Statistics
class Statistic(models.Model):

    incomes = FloatField(null=True,blank=True)
    sales = IntegerField(null=True,blank=True)
    date = DateField(auto_now=False,auto_now_add=True)

    class Meta :
        verbose_name = 'Statistic'
        verbose_name_plural = 'Statistics'
        
    
    def __str__(self):
        return f'Estadisticas de {str(self.date)}'

# Monthly statistics
class MonthlyStatistic(models.Model):

    incomes = FloatField(null=True,blank=True)
    sales = IntegerField(null=True,blank=True)
    date = DateField(auto_now=False,auto_now_add=True)

    class Meta :
        verbose_name = 'Monthly statistic'
        verbose_name_plural = 'Monthly statistics'
        
    
    def __str__(self):
        return f'Estadisticas de {str(self.date)}'