from django.shortcuts import render
from .models import Recipe, RecipeProduct
from .serializers import RecipeSerializer, RecipeProductSerializer
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from recipe_category.models import Recipe_category
from django.shortcuts import render, get_object_or_404
from product.models import Product
from django.http import HttpResponse

class ViewAllRecipes(APIView):
    def get(self, request): #! pobieranie wszystkiego
        recipes = Recipe.objects.filter(Q(deleted = False))                                       #? ktore nie sa usuniete (deleted=False)
        recipes = Recipe.objects.filter(Q(deleted = False)) #! ktore nie sa usuniete (deleted=False)
        serializer = RecipeSerializer(recipes, many = True)
        data = {}
        data['recipes'] = serializer.data
        return Response(data)
    

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
        
    def put(self, request, id):
        data = self.request.data                #! nowe dane produktu
        #id = self.request.data.get('id')        #* dane produktu
        recipe = self.get_object(id)           #? Wywołanie metody pobrania produktu ze wskazaniem id (cały obiekt)
        print(data, 'przed')
        _mutable = data._mutable                                                                                         #* zezwolenie na modyfikowanie data
        data._mutable = True
        data._mutable = _mutable
        print(data, 'po')
        serializer = RecipeSerializer(recipe, data = data, partial=True ) #! serializer wstawia nowe dane
        if serializer.is_valid():
            recipe = serializer.save()
            if 'image' in data:
                recipe.image = data['image']
                recipe.thumbnail = None
                recipe.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, id):
        #data = self.request.data
        #id = self.request.data.get('id')  
        data = {}
        data['deleted'] = True
        recipe = self.get_object(id)
        #print(product.deleted)
        serializer = RecipeSerializer(recipe, data = data, partial=True ) #! serializer wstawia nowe dane
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        

#!######################################################
class ViewRecipeProducts(APIView):
    def get(self, request, id):
        products = RecipeProduct.objects.filter(Q(recipe_id = id))
        print(products, 'RECIPE PRODUCTS')
        serializer = RecipeProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#!#####################################################


class AddRecipe(APIView):

    def post(self, request):
        data = self.request.data
        category_name = data.get('recipe_category')
        recipeCategory = Recipe_category.objects.get( name = category_name).id
        _mutable = data._mutable  # * zezwolenie na modyfikowanie data
        data._mutable = True
        data['Recipe_category'] = recipeCategory
        data._mutable = _mutable
        serializer = RecipeSerializer(data=data)
        if serializer.is_valid():
            recipe = serializer.save()
            if 'image' in data:
                recipe.image = data['image']
                recipe.thumbnail = None
                recipe.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    #post i tutaj to co recipe + add_produkt * ile produktów
class AddProduct_to_Recipe(APIView):
    def post(self, request):
        data = self.request.data
        product_id = data.get('id')
        quantity = data.get('quantity')
        recipe_id = Recipe.objects.latest('id').id
        #print(recipe_id, 'ID_PRZEPISU')
        recipe = get_object_or_404(Recipe, id=recipe_id)
        product = Product.objects.get(id = product_id)
        #print(product, "PRODUKT")
        recipe.add_product(product, quantity)
        return HttpResponse('')
