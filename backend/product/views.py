from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status

class ViewProducts(APIView):
    def get(self, request):
        products = Product.objects.filter(Q(deleted = False))
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)

    def post(self, request):
        data = self.request.data
        serializer = ProductSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_422_UNPROCESSABLE_ENTITY)
        

        
