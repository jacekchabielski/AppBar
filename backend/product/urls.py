from django.urls import path, include
from .views import ViewProducts
from product import views

urlpatterns = [
    path('products/', views.ViewProducts.as_view()), #! zwraca wszystkie produkty
]
