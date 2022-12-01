from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recipe_category
from rest_framework.response import Response
from rest_framework import status

class GetRecipeCategories(APIView):
    def get(self, request, format = None):
        recipe_categories = Recipe_category.objects.values_list('name', flat=True) #! pobieramy wszystkie nazwy
        recipe_categories = list(dict.fromkeys(recipe_categories))    #? pozbywamy się powtórzeń
        return Response(recipe_categories,status=status.HTTP_200_OK)

