from django.db import models
from django.utils.text import slugify
from product.models import Product
from django.db.models.deletion import CASCADE
from recipe_category.models import Recipe_category
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.core.validators import MaxValueValidator, MinValueValidator


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank = True)
    #product = models.ManyToManyField(Product, related_name='product', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length = 255, blank = True)
    image = models.ImageField(upload_to = 'uploads/recipe/', blank = True, null = True)
    thumbnail = models.ImageField(upload_to = 'uploads/recipe/', blank = True, null = True)
    Recipe_category = models.ForeignKey(Recipe_category, on_delete=CASCADE, related_name='recipe_category', blank=True)
    created = models.DateTimeField(auto_now_add = True)
    deleted = models.BooleanField(default = False)
    class Meta:
        ordering = ('-created',)
        

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name) #!przy zapisie tworzy slug z nazwa
        super(Recipe, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/{self.id}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
        
    def make_thumbnail(self,image,size = (600,500)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'PNG', quality = 85)
        thumbnail = File(thumb_io, name = image.name)
        return thumbnail

    def add_product(self, product, quantity):
        #print(product.id ,"product w add product")
        new_recipe_product = RecipeProduct.objects.get_or_create(product_id=product, recipe_id=self, quantity=quantity)
        #new_recipe_product.quantity += quantity
        return new_recipe_product
    
    def update_product(self, product, quantity):
        recipe_product = RecipeProduct.get(product_id= product.id, recipe_id= self.id)
        if not recipe_product: return None 
        recipe_product.quantity = quantity
        return recipe_product
    
    def delete_product(self, product_id):
        recipe_product = RecipeProduct.get(product_id= product_id, recipe_id= self.id)
        if not recipe_product is None: recipe_product.delete()

class RecipeProduct(models.Model):
    product_id = models.ForeignKey(Product, on_delete=CASCADE, related_name='product_id', blank=False)
    recipe_id = models.ForeignKey(Recipe,  on_delete=CASCADE, related_name='recipe_id', blank=False)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(1)])
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.product_id.name + " of " + self.recipe_id.name
    