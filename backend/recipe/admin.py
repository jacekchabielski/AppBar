from django.contrib import admin
from .models import Recipe, RecipeProduct

admin.site.register(Recipe)
admin.site.register( RecipeProduct)