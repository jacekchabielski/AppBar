from django.db.models import fields
from rest_framework import serializers
from .models import Order, OrderRecipe, Recipe
from recipe.serializers import RecipeSerializer


class OrderRecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderRecipe
        fields = (
            'id',
            'recipe_id',
            'order_id',
            'quantity',
            
        )

class OrderSerializer(serializers.ModelSerializer):
# recipe_list = RecipeSerializer(source='recipe', read_only=True, many=True)
    created = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Order
        fields = (
            'id',
            'name',
            'table',
            'price',
            'status',
            'slug',
            'deleted',
            'created',
        )
