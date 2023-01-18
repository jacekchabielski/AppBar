
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('product.urls')),
    path('api/v1/', include('product_category.urls')),
    path('api/v1/', include('recipe.urls')),
    path('api/v1/', include('recipe_category.urls')),
    path('api/v1/', include('user_profile.urls')),
] +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

