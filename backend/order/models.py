from django.db import models
from django.utils.text import slugify
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator
from recipe.models import Recipe

class Order(models.Model):
    name = models.CharField(max_length=255)
    table = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255)
    slug = models.SlugField(max_length = 255, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    deleted = models.BooleanField(default = False)
    
    class Meta:
        ordering = ('-created',)
        

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name) #!przy zapisie tworzy slug z nazwa
        super(Order, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/{self.id}/'
    

    def add_recipe(self, recipe, quantity):
        #print(product.id ,"product w add product")
        new_order_recipe = OrderRecipe.objects.get_or_create(recipe_id=recipe, order_id=self, quantity=quantity)
        #new_recipe_product.quantity += quantity
        return new_order_recipe
    
    def update_recipe(self, recipe, quantity):
        order_recipe = OrderRecipe.get(recipe_id= recipe.id, order_id= self.id)
        if not order_recipe: return None 
        order_recipe.quantity = quantity
        return order_recipe
    
    def delete_recipe(self, recipe_id):
        order_recipe = OrderRecipe.get(recipe_id= recipe_id, order_id= self.id)
        if not order_recipe is None: order_recipe.delete()

class OrderRecipe(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=CASCADE, related_name='recipe_idd', blank=False)
    order_id = models.ForeignKey(Order,  on_delete=CASCADE, related_name='order_id', blank=False)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(1)])
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.order_id.name + " - " +  self.recipe_id.name 