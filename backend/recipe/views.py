from django.shortcuts import render
from django.shortcuts import render
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.core.paginator import Paginator
from rest_framework.decorators import api_view

class ViewRecipes(APIView):
    def get(self, request): #! pobieranie wszystkiego
        page_number = self.request.query_params.get('page_number', 1)                               #? numer aktualnej strony (aktualnie pierwsza)
        page_size = self.request.query_params.get('page_size', 5)                                   #? ilość elementów na stronie (aktualnie 5)
        recipes = Recipe.objects.filter(Q(deleted = False))                                       #? ktore nie sa usuniete (deleted=False)
        category = self.request.query_params.get('category', '')
            #? ilość elementów na stronie (aktualnie 5)
        if category != '' and category != 'Wszystkie kategorie':
            recipes = Recipe.objects.filter(Q(Recipe_category__name__icontains = category) & Q(deleted = False)) #? ktore nie sa usuniete (deleted=False)
        else:
            recipes = Recipe.objects.filter(Q(deleted = False)) #! ktore nie sa usuniete (deleted=False)
        paginator = Paginator(recipes, page_size)
        serializer = RecipeSerializer(paginator.page(page_number), many = True)
        data = {}
        data['recipes'] = serializer.data
        data['page_numbers'] = paginator.num_pages                                                  #? ile bedzie razem podstron
        data['next_page'] = False if int(page_number) >= paginator.num_pages else True              #? czy istnieje kolejna podstrona
        return Response(data)

@api_view(['POST'])                             #! wyszukiwanie przepisow
def search(request):
    query = request.data.get('query', '')
    if query:
        recipes = Recipe.objects.filter(Q(name__icontains = query) | Q(description__icontains = query) ).all()
        recipes_list = list(recipes)
        page_number = request.query_params.get('page_number', 1)                               #? numer aktualnej strony (aktualnie pierwsza)
        page_size = request.query_params.get('page_size', 5)  
        paginator = Paginator(recipes_list, page_size)
        serializer = RecipeSerializer(paginator.page(page_number), many = True)
        data = {}
        data['recipes'] = serializer.data
        data['page_numbers'] = paginator.num_pages                                                  #? ile bedzie razem podstron
        data['next_page'] = False if int(page_number) >= paginator.num_pages else True              #? czy istnieje kolejna podstrona
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response({'recipes':[]})

class ViewRecipe(APIView):
    def get(self,request, id):
        recipe = self.get_object(id)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def get_object(self, recipe_id):
        try:
            return Recipe.objects.get(id = recipe_id)
        except Recipe.DoesNotExist:
            raise Http404