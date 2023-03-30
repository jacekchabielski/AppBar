from django.shortcuts import render
from .models import Order, OrderRecipe
from .serializers import OrderSerializer, OrderRecipeSerializer
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from recipe.models import Recipe
from django.http import HttpResponse
# Create your views here.
                                            #? pojedynczy order
class ViewOrder(APIView):
    
    #! pobranie obiektu (potrzebne do edycji)
    def get_object(self, order_id):
        try:
            return Order.objects.get(id = order_id)
        except Order.DoesNotExist:
            raise Http404

    #!edycja order
    def put(self, request, id):
        data = self.request.data                #! nowe dane produktu
        #id = self.request.data.get('id')        #* dane produktu
        order = self.get_object(id)           #? Wywołanie metody pobrania produktu ze wskazaniem id (cały obiekt)
        
        print(data, 'przed')
        _mutable = data._mutable                                                                                         #* zezwolenie na modyfikowanie data
        data._mutable = True
        data._mutable = _mutable
        print(data, 'po')
        serializer = OrderSerializer(order, data = data, partial=True ) #! serializer wstawia nowe dane
        if serializer.is_valid():
            order = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

class ViewAllOrders(APIView):
    def get(self, request): #! pobieranie wszystkiego
        orders = Order.objects.filter(Q(deleted = False))                                       #? ktore nie sa usuniete (deleted=False)
        serializer = OrderSerializer(orders, many = True)
        data = {}
        data['orders'] = serializer.data
        return Response(data)


class AddOrder(APIView):
    def post(self, request):
        data = self.request.data
        order_id = Order.objects.latest('id').id
        print(order_id,"orderid")
        print(data,"zawartosc data")
        
        _mutable = data._mutable  # * zezwolenie na modyfikowanie data
        data._mutable = True
        #data._mutable = _mutable
        data['name'] = 'Zamówienie#'+str(order_id)
        data._mutable = _mutable
        print(data, 'po zmianie nazwy')
        serializer = OrderSerializer(data=data, partial=True)
        if serializer.is_valid():
            order = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    #post i tutaj to co recipe + add_produkt * ile produktów
    

class AddRecipe_to_Order(APIView):
    def post(self, request):
        data = self.request.data
        recipe_id = data.get('id')
        quantity = data.get('quantity')
        order_id = Order.objects.latest('id').id
        #print(recipe_id, 'ID_PRZEPISU')
        order = get_object_or_404(Order, id=order_id)
        recipe = Recipe.objects.get(id = recipe_id)
        #print(product, "PRODUKT")
        order.add_recipe(recipe, quantity)
        return HttpResponse('')
    
######################################################
class ViewOrderRecipes(APIView):
    def get(self, request, id):
        recipes = OrderRecipe.objects.filter(Q(order_id = id))
        print(recipes, 'ORDER RECIPES')
        serializer = OrderRecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

######################################################
