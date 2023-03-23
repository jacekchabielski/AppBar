from django.urls import path, include
from .views import AddOrder, AddRecipe_to_Order
from order import views

urlpatterns = [
    path('add_order/', views.AddOrder.as_view()), #! dodawanie zamówienia
    path('add_recipe_to_order/', views.AddRecipe_to_Order.as_view()),

]