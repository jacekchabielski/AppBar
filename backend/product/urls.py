from django.urls import path, include
from .views import ViewProduct, ViewProducts, ViewProductsByCategory
from product import views
urlpatterns = [
    path('product/<int:id>/', views.ViewProduct.as_view()), #! zwraca produkt
    path('products/', views.ViewProducts.as_view()), #! zwraca wszystkie produkty
    path('products/<str:category>/', views.ViewProductsByCategory.as_view()), #! zwraca pofiltrowane po category
]
