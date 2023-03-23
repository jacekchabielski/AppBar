from django.db.models import fields
from rest_framework import serializers
from .models import Order
from recipe.serializers import RecipeSerializer


class OrderSerializer(serializers.ModelSerializer):
    recipe_list = RecipeSerializer(
        source='recipe', read_only=True, many=True)

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
            'recipe_list'
        )
