from django.urls import path, include
from .views import ViewRecipes, ViewRecipe, AddRecipe, AddProduct_to_Recipe, ViewRecipeProducts
from recipe import views

urlpatterns = [
    path('recipe/<int:id>/', views.ViewRecipe.as_view()), #! zwraca przepis
    path('add_recipe/', views.AddRecipe.as_view()), #! dodawanie przepisu
    path('add_product_to_recipe/', views.AddProduct_to_Recipe.as_view()), #! dodawanie produktu do przepisu
    path('recipes/', views.ViewRecipes.as_view()), #! zwraca wszystkie przepisy (recipes)
    path('recipe_products/<int:id>/', views.ViewRecipeProducts.as_view()),
    path('recipes/search/', views.search),
    
]