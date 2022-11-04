from itertools import product
from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404




#! pobieranie wszystkiego
class ViewProducts(APIView):
    def get(self, request):
        products = Product.objects.filter(Q(deleted=False)) #! ktore nie sa usuniete (deleted=False)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
#! dodawanie nowego
    def post(self, request):
        data = self.request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            product = serializer.save()
            if 'image' in data:
                product.image = data['image']
                product.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

#! Edycja
#******************* POBRANIE OBIEKTU (PRODUKTU) **************
    def get_object(self, product_id):
        try:
            return Product.objects.filter(id = product_id).get()
        except Product.DoesNotExist:
            raise Http404
#**********************************************************

    def put(self, request):
        data = self.request.data                #! nowe dane produktu
        id = self.request.data.get('id')        #* dane produktu
        product = self.get_object(id)           #? Wywołanie metody pobrania produktu ze wskazaniem id (cały obiekt)
        serializer = ProductSerializer(product, data = data, partial=True ) #! serializer wstawia nowe dane
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        

