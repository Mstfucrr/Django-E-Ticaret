from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.utils.safestring import mark_safe

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE, null = True)
    name = models.CharField(max_length=30,blank = True,null = True)
    email = models.EmailField(max_length=50,blank = True, null = True)
    phone = models.CharField(blank=True,max_length=20,null = True)
    address = models.CharField(blank=True,max_length=150,null = True)
    city = models.CharField(blank=True,max_length=30,null=True)
    country = models.CharField(blank=True,max_length=30,null=True)
    zipcode = models.CharField(blank=True,max_length=10,null=True)
    image = models.ImageField(blank=True,upload_to='images/users/',null=True)
    def __str__(self):
        return self.name

    def first_name(self):
        return self.user.first_name

    def Name(self):
        if self.user != None:
            self.name = self.user.first_name + " " + self.user.last_name
        else:
            self.name = ""
        return self.name

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

