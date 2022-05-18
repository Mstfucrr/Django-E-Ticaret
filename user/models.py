from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.safestring import mark_safe

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    phone = models.CharField(blank=True,max_length=20)
    address = models.CharField(blank=True,max_length=150)
    city = models.CharField(blank=True,max_length=30)
    country = models.CharField(blank=True,max_length=30)
    image = models.ImageField(blank=True,upload_to='images/users/')
    def __str__(self):
        return self.user.username

    def first_name(self):
        return self.user.first_name

    def image_tag(self):
        try:
            return mark_safe(f'<img src="{self.image.url}" alt="image"  height = "50"')
        except Exception:
            return mark_safe(f'<img alt="image field is blank"')
    image_tag.short_description = "Image"

class UserProfileForm(ModelForm):
    class Meta: 
        model = UserProfile
        fields = ['phone', 'address', 'city', 'country','image']

