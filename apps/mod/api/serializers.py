# Rest framework
from rest_framework import serializers

# Models
from apps.mod.models import Statistic, MonthlyStatistic, PendingShipments, Status

# Statistics serializer
class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = '__all__'

# Monthly statistics serializer
class MonthlyStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyStatistic
        fields = '__all__'

# Pending shipments serializer
class PendingShipmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PendingShipments
        fields = '__all__'

    
    def to_representation(self, instance):
        return {
            'id':instance.id,
            'product': {
                'title':instance.product.title,
                'price':instance.product.price
            },
            'color':instance.color,
            'waist':instance.waist,
            'quantity':instance.quantity,
            'user':instance.user.username,
            'status':instance.status.status_name,
        }

# Status serializer
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
    