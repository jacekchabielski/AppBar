from django.db import models
from django.utils.text import slugify
from product.models import Product
from django.db.models.deletion import CASCADE
from recipe_category.models import Recipe_category
from io import BytesIO
from PIL import Image
from django.core.files import File

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank = True)
    product = models.ManyToManyField(Product, related_name='product', blank=True)
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