from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product_category
from rest_framework.response import Response
from rest_framework import status

class GetProductCategories(APIView):
    def get(self, request, format = None):
        product_categories = Product_category.objects.values_list('name', flat=True) #! pobieramy wszystkie nazwy
        product_categories = list(dict.fromkeys(product_categories))    #? pozbywamy się powtórzeń
        return Response(product_categories,status=status.HTTP_200_OK)

