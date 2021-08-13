from django import forms
from django.db import models
from django.db.models.fields import CharField, DateTimeField
from django.db.models.fields.files import ImageField
from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.
class Setting(models.Model):
    STATUS = (
        ('True','Evet'),
        ('False','Hayır'),
    )

    title = CharField(max_length=200)
    keywords = CharField(max_length=255)
    description = CharField(max_length=255)

    company = CharField(max_length=50)
    address = CharField(blank=True,max_length=200)
    phone = CharField(blank=True,max_length=15)
    fax = CharField(blank=True,max_length=15)
    email = CharField(blank=True,max_length=50)

    smtpserver = CharField(max_length=15)
    smtpemail = CharField(max_length=15)
    smtppassword = CharField(max_length=15)
    smtpport = CharField(blank=True,max_length=5)

    icon = ImageField(blank=True,upload_to='images/')

    facebook = CharField(max_length=15)
    twitter = CharField(max_length=15)

    abouts = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    
    status = CharField(max_length=10,choices=STATUS)

    created_at = DateTimeField(auto_now_add=True)
    update_at = DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


class Contact(models.Model):
    STATUS = (
        ('New','New'),
        ('Read','Read'),
    )
    name = CharField(blank=True, max_length=25)
    email = CharField(blank=True,max_length=50)
    subject = CharField(blank=True,max_length=50)
    message = CharField(blank=True,max_length=260)
    status = CharField(max_length=10,choices=STATUS,default='New')
    ip = CharField(blank=True,max_length=20)
    note = CharField(blank=True,max_length=100)
    created_at = DateTimeField(auto_now_add=True)
    update_at = DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name','email','subject','message')
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder':'İsim*','required':''}),
            'email' : forms.TextInput(attrs={'placeholder':'Email Adresi*','required':''}),
            'subject' : forms.TextInput(attrs={'placeholder':'Konu*','required':''}),
            'message' : forms.Textarea(attrs={'placeholder':'Mesajınız..*','style':"resize: none;",'required':''}),
            
        }
        


