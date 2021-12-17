from django.contrib import admin
from .models import PendingShipments,Statistic,MonthlyStatistic,Status

admin.site.register(PendingShipments)
admin.site.register(Status)
admin.site.register(Statistic)
admin.site.register(MonthlyStatistic)

