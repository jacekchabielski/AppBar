from django.urls import path, include
from .views import ViewProduct, ViewProducts
from product import views

urlpatterns = [
    path('product/<int:id>/', views.ViewProduct.as_view()), #! zwraca produkt
    path('products/', views.ViewProducts.as_view()), #! zwraca wszystkie produkty
]
