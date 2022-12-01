from django.db import models
from django.utils.text import slugify


class Recipe_category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length = 255, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    deleted = models.BooleanField(default = False)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = "Recipe_categories"
        

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name) #!przy zapisie tworzy slug z nazwa
        super(Recipe_category, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return f'/{self.id}/'
    
