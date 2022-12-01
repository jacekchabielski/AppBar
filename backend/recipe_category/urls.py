from django.urls import path, include
from .views import GetRecipeCategories
from recipe_category import views


urlpatterns = [
    path('recipeCategory/', views.GetRecipeCategories.as_view()), #! zwraca produkt
]