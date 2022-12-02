from django.urls import path, include
from .views import ViewRecipes, ViewRecipe
from recipe import views

urlpatterns = [
    path('recipe/<int:id>/', views.ViewRecipe.as_view()), #! zwraca przepis
    path('recipes/', views.ViewRecipes.as_view()), #! zwraca wszystkie przepisy (recipes)
]