from django.db.models import fields
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    Product_category_name = serializers.ReadOnlyField(source='Product_category.name')
    class Meta:
        model = Product
        fields = (
            'id',
            'created',
            'deleted',
            'name',
            'description',
            'product_quantity',
            'get_absolute_url',
            'get_image',
            'get_thumbnail',
            'slug',
            'Product_category',
            'Product_category_name'
        )
