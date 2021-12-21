# Rest framework
from rest_framework import serializers

# Models
from apps.client.models import ShoppingCart, ShoppingHistory

class ShoppingCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingCart
        fields = '__all__'

    def to_representation(self, instance):
        return {
            "color": instance.color,
            "waist": instance.waist,
            "user": instance.user.id,
            "quantity":instance.quantity,
            "product": {
                'title':instance.product.title,
                'price':instance.product.price,
                'image':str(instance.product.image) if instance.product.image is not None else ""
            } if instance.product is not None else ""
        }

class ShoppingHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingHistory
        fields = '__all__'
 
    def to_representation(self, instance):
        return {

            "product": {
                'title':instance.product.title,
                'price':instance.product.price,
                'image':str(instance.product.image) if instance.product.image is not None else ""
            } if instance.product is not None else "",
            "color": instance.color,
            "waist": instance.waist,
            "quantity":instance.quantity,
            "status":instance.status.status_name,
            "date_purchase":instance.date_purchase
        }

