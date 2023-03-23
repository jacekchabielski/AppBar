from django.shortcuts import render
from .models import Order
from .serializers import OrderSerializer
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


class AddOrder(APIView):
  #name table price status
    def post(self, request):
        data = self.request.data
        _mutable = data._mutable  # * zezwolenie na modyfikowanie data
        order_id =Order.objects.latest('id').id
        
        data._mutable = True
        data['name'] = 'Zamówienie#'+str(order_id)
        data._mutable = _mutable
        serializer = OrderSerializer(data=data)
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