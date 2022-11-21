from django.urls import path, include
from .views import GetProductCategories
from product_category import views


urlpatterns = [
    path('productCategory/', views.GetProductCategories.as_view()), #! zwraca produkt
]