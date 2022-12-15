from django.urls import path, include
from .views import ViewProduct, ViewProducts, ViewAllProducts
from product import views
urlpatterns = [
    path('products/all/', views.ViewAllProducts.as_view()), #? zwwraca wszystkie produkty
    path('product/<int:id>/', views.ViewProduct.as_view()), #! zwraca produkt
    path('products/', views.ViewProducts.as_view()), #! zwraca wszystkie produkty - z paginacją
    # path('products/<str:category>/', views.ViewProductsByCategory.as_view()), #! zwraca pofiltrowane po category
    path('products/search/', views.search),
]
