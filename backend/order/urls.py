from django.urls import path, include
from .views import ViewOrder, AddOrder, AddRecipe_to_Order, ViewOrderRecipes, OrderOrderRecipes
from order import views

urlpatterns = [
    path('orders/all/', views.ViewAllOrders.as_view()), #? zwwraca wszystkie zamowienia
    path('add_order/', views.AddOrder.as_view()), #! dodawanie zamówienia
    path('order/<int:id>/', views.ViewOrder.as_view()),                     #! zwraca order
    path('add_recipe_to_order/', views.AddRecipe_to_Order.as_view()),
    path('order_recipes/<int:id>/', views.ViewOrderRecipes.as_view()),
    path('order/<int:id>/order_recipes/', views.OrderOrderRecipes.as_view()),
]