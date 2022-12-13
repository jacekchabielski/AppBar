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
from product_category.models import Product_category
from django.core.paginator import Paginator

class ViewAllProducts(APIView):
    def get(self, request): #! pobieranie wszystkiego
        products = Product.objects.filter(Q(deleted = False))                                       #? ktore nie sa usuniete (deleted=False)
        products = Product.objects.filter(Q(deleted = False)) #! ktore nie sa usuniete (deleted=False)
        serializer = ProductSerializer(products, many = True)
        data = {}
        data['products'] = serializer.data
        return Response(data)

#! WYŚWIETLANIE WSZYSTKICH PRODUKTÓW  Z PAGINACJĄ
class ViewProducts(APIView):
    def get(self, request): #! pobieranie wszystkiego
        page_number = self.request.query_params.get('page_number', 1)                               #? numer aktualnej strony (aktualnie pierwsza)
        page_size = self.request.query_params.get('page_size', 5)                                   #? ilość elementów na stronie (aktualnie 5)
        products = Product.objects.filter(Q(deleted = False))                                       #? ktore nie sa usuniete (deleted=False)
        category = self.request.query_params.get('category', '')
            #? ilość elementów na stronie (aktualnie 5)
        if category != '' and category != 'Wszystkie kategorie':
            products = Product.objects.filter(Q(Product_category__name__icontains = category) & Q(deleted = False)) #? ktore nie sa usuniete (deleted=False)
        else:
            products = Product.objects.filter(Q(deleted = False)) #! ktore nie sa usuniete (deleted=False)
        paginator = Paginator(products, page_size)
        serializer = ProductSerializer(paginator.page(page_number), many = True)
        data = {}
        data['products'] = serializer.data
        data['page_numbers'] = paginator.num_pages                                                  #? ile bedzie razem podstron
        data['next_page'] = False if int(page_number) >= paginator.num_pages else True              #? czy istnieje kolejna podstrona
        return Response(data)



#! WYSWIETLANIE POSZCZEGÓLNEGO PRODUKTU 
class ViewProduct(APIView):
    def get(self,request, id):
        #data = self.request.GET
        #id = self.request.GET.get('id')  

        print(id)
        product = self.get_object(id)
        #print(product)
        serializer = ProductSerializer(product)
        
        return Response(serializer.data)


#! DODAWANIE NOWEGO PRODUKTU
    def post(self, request, id):
        data = self.request.data
        category_name = data.get('Product_category')
        productCategory = Product_category.objects.get( name = category_name ).id
        data['Product_category'] = productCategory
        serializer = ProductSerializer(data = data)
        if serializer.is_valid():
            product = serializer.save()
            if 'image' in data:
                product.image = data['image']
                product.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

#! EDYCJA PRODUKTU
#******************* POBRANIE OBIEKTU (PRODUKTU) **************
    def get_object(self, product_id):
        try:
            return Product.objects.get(id = product_id)
        except Product.DoesNotExist:
            raise Http404
#**********************************************************

    def put(self, request, id):
        data = self.request.data                #! nowe dane produktu
        #id = self.request.data.get('id')        #* dane produktu
        product = self.get_object(id)           #? Wywołanie metody pobrania produktu ze wskazaniem id (cały obiekt)
        category_name = data.get('Product_category')
        productCategory = Product_category.objects.get( name = category_name ).id
        print(data, 'przed')
        _mutable = data._mutable                                                                                         #* zezwolenie na modyfikowanie data
        data._mutable = True
        data['Product_category'] = productCategory
        data._mutable = _mutable
        print(data, 'po')
        serializer = ProductSerializer(product, data = data, partial=True ) #! serializer wstawia nowe dane
        if serializer.is_valid():
            product = serializer.save()
            if 'image' in data:
                product.image = data['image']
                product.thumbnail = None
                product.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, id):
        #data = self.request.data
        #id = self.request.data.get('id')  
        data = {}
        data['deleted'] = True
        product = self.get_object(id)
        #print(product.deleted)
        serializer = ProductSerializer(product, data = data, partial=True ) #! serializer wstawia nowe dane
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    

