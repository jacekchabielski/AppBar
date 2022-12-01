from django.urls import path, include
from .views import ViewRecipes
from recipe import views

urlpatterns = [
    path('recipes/', views.ViewRecipes.as_view()), #! zwraca wszystkie przepisy (recipes)
]