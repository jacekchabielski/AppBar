from django.db.models import fields
from rest_framework import serializers
from .models import Recipe
from product.serializers import ProductSerializer

class RecipeSerializer(serializers.ModelSerializer):
    product_list = ProductSerializer(source = 'product', read_only = True, many = True)
    class Meta:
        model = Recipe
        fields = (
            'id',
            'name',
            'description',
            'price',
            'slug',
            'created',
            'deleted',
            'product_list',   
            'get_absolute_url',
            'get_image',
            'get_thumbnail',       
        )
