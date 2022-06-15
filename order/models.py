from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.

class ShopCart(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product,on_delete= models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0,null=True)

    def __str__(self):
        return '"user" : {}, "product" : {} , "quantity" : {}'.format(self.user, self.product,self.quantity)
    
    @property
    def amount(self):
        return (self.quantity * self.product.price)

    @property
    def price(self):
        return self.product.price


class Order(models.Model):
    STATUS = (
        ('New','New'),
        ('Accepted','Accepted'),
        ('Preaparing','Preaparing'),
        ('OnShipping','OnShipping'),
        ('Completed','Completed'),
        ('Cancelled','Cancelled'),
    )
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null =True)
    code = models.CharField(max_length=5,editable=False)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length= 20)
    phone = models.CharField(blank=True,max_length=20)
    address = models.CharField(blank=True,max_length=200)
    city = models.CharField(blank=True,max_length=30)
    country = models.CharField(blank =True,choices=STATUS,max_length = 20)
    total = models.FloatField()
    status = models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True,max_length=20)
    adminnote = models.CharField(blank=True,max_length=150)
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now=True)

class OrderProduct(models.Model):
    STATUS = (
        ('New','New'),
        ('Accepted','Accepted'),
        ('Cancelled','Cancelled'),
    )
    order = models.ForeignKey(Order,on_delete = models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.IntegerField()
    # price= models.FloatField()
    # amount = models.FloatField()
    status = models.CharField(max_length=10,choices= STATUS, default='New')
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now=True)

    @property
    def amount(self):
        return (self.quantity * self.product.price)

    @property
    def price(self):
        return self.product.price
