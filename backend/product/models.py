from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db.models.deletion import CASCADE
from django.utils.text import slugify

class Product(models.Model):
    created = models.DateField(auto_now_add = True)
    deleted = models.BooleanField(default = False)
    name = models.CharField(max_length = 255)
    description = models.TextField(blank = True)
    product_quantity = models.IntegerField(blank = True, null = True, default = 0)
    image = models.ImageField(upload_to = 'uploads/', blank = True, null = True)
    thumbnail = models.ImageField(upload_to = 'uploads/', blank = True, null = True)
    slug = models.SlugField(max_length = 255, blank = True)

    class Meta:
        ordering = ('-created',) #! odwrocenie segregacji po dacie utworzenia

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name) #!przy zapisie tworzy slug z nazwa
        super(Product, self).save(*args, **kwargs)


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

    



