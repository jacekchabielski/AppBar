from django.db.models import fields
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'created',
            'deleted',
            'name',
            'description',
            'product_quantity',
            'get_image',
            'get_thumbnail',
            'slug'
        )
