from django.contrib import admin
from .models import Order, OrderRecipe

admin.site.register(Order)
admin.site.register(OrderRecipe)