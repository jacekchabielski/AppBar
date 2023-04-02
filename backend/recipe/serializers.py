from django.db.models import fields
from rest_framework import serializers
from .models import Recipe, RecipeProduct, Product
from product.serializers import ProductSerializer


class RecipeProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecipeProduct
        fields = (
            'id',
            'product_id',
            'recipe_id',
            'quantity',
            
        )

class RecipeSerializer(serializers.ModelSerializer):
   # product_list = RecipeProductSerializer(
       # source='id.recipe_id', read_only=True, many=True)
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
            #'product_list',   
            'get_absolute_url',
            'get_image',
            'get_thumbnail',
            'Recipe_category'
        )


