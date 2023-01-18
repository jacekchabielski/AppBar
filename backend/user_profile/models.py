from django.db import models
from PIL import Image
from django.core.files import File
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save, post_delete, pre_delete
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.dispatch import receiver


class User_Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    slug = models.SlugField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    role = models.TextField(blank=True, null=True)
    workplace = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username) #!przy zapisie tworzy slug z nazwa
        super(User_Profile, self).save(*args, **kwargs)


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

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created=User_Profile.objects.get_or_create(user=instance)
post_save.connect(create_user_profile, sender=User)
    
