from django.db import models
from django.db.models.fields import CharField, DateTimeField, FloatField, IntegerField, SlugField, TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from django_extensions.db.fields import AutoSlugField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
import unidecode
from unidecode import unidecode
# Create your models here.

class Category(MPTTModel):
    STATUS = (
        ('True','Evet'),
        ('False','Hayır'),
    )
    parent = TreeForeignKey('self',blank=True,null=True,related_name="children",on_delete=models.CASCADE)
    
    title = CharField(max_length=200)
    keywords = CharField(blank = True,max_length=255)
    description = CharField(blank = True,max_length=255)
    
    image = ImageField(blank = True,upload_to = "images/")
    status = CharField(max_length=10,choices=STATUS)
    
    slug = AutoSlugField(populate_from='title')

    
    
    created_at = DateTimeField(auto_now_add=True)
    update_at = DateTimeField(auto_now=True)

    def slugify_function(self, content):
        if self.parent:
            return (str(self.parent.slug)+"-"+unidecode(str(content.replace(' ', '-')).lower()))
        return str(unidecode(str(content.replace(' ', '-')).lower()))

    
    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by=['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '  --> '.join(full_path[::-1])
    
    def image_tag(self):
        try:
            return mark_safe(f'<img src="{self.image.url}" alt="image"  height = "50"')
        except Exception:
            return mark_safe(f'<img alt="image field is blank"')
    image_tag.short_description = "Image"

class Product(models.Model):
    STATUS = (
        ('True','Evet'),
        ('False','Hayır'),
    )

    category = ForeignKey(Category,on_delete=models.CASCADE)

    title = CharField(max_length=200)
    keywords = CharField(blank = True,max_length=255)
    description = CharField(blank = True,max_length=255)

    image = ImageField(blank = True,upload_to = "images/")
    price = FloatField()
    amount = IntegerField()
    detail = RichTextUploadingField()
    status = CharField(max_length=10,choices=STATUS)

    slug = AutoSlugField(populate_from='title')

    def slugify_function(self, content):
        return str(unidecode(str(content.replace(' ', '-')).lower()))
    
    created_at = DateTimeField(auto_now_add=True)
    update_at = DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def image_tag(self):
        try:
            return mark_safe(f'<img src="{self.image.url}" alt="image"  height = "50"')
        except Exception:
            return mark_safe(f'<img alt="image field is blank"')
    image_tag.short_description = "Image"


class Images(models.Model):
    product = ForeignKey(Product,on_delete=models.CASCADE)
    title = CharField(max_length=50,blank=True)
    image = ImageField(blank = True,upload_to = "images/")
    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe(f'<img src="{self.image.url}" height = "50"')
    image_tag.short_description = "Image"
