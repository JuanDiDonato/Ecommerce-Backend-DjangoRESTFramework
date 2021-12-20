# Rest framework serializers
from django.db.models import fields
from rest_framework import serializers

# Models
from apps.products.models import Product, Event, Category, Colors, Waist, Images

# Colors serializer
class ColorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Colors
        fields= '__all__'

# Waist serializer
class WaistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Waist
        fields= '__all__'

# Category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_name',)

# Event serializer
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

# Images serializers
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

# Product serialzier
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


    def get_images(self,instance):
        image_list = []
        images = ImageSerializer.Meta.model.objects.filter(product=instance.id)
        for image in images:
            image_list.append(f'media/{str(image)}')
        return image_list

    def get_stock_for_colors(self,attribute):
        dict = {}
        dict['color'] = str(attribute)
        dict['stock_s'] = attribute.id_talle.stock_s
        dict['stock_m'] = attribute.id_talle.stock_m
        dict['stock_l'] = attribute.id_talle.stock_l
        dict['stock_xl'] = attribute.id_talle.stock_xl
        dict['stock_xxl'] = attribute.id_talle.stock_xxl
        dict['stock_xxxl'] = attribute.id_talle.stock_xxxl
        return dict


    def to_representation(self, instance):

        fields = self._readable_fields
        list = []
        for field in fields:
            if field.field_name == 'ids_colors':
                attributes = field.get_attribute(instance)
                for attribute in attributes:
                    dict_colors = self.get_stock_for_colors(attribute)
                    list.append(dict_colors)
        return {
            'id':instance.id,
            'title':instance.title,
            'description':instance.description,
            'price':instance.price,
            'images': self.get_images(instance),
            'category':instance.category.category_name if instance.category is not None else "",
            'disable':instance.disable,
            'created_ad':instance.created_at,
            'event': {
                'name':instance.event.name if instance.event is not None else "",
                'discount':instance.event.discount if instance.event is not None else "",
                'from_date':instance.event.from_date if instance.event is not None else "",
                'to_date':instance.event.to_date if instance.event is not None else "",
            } if instance.event else "",
            'colors':list
        }