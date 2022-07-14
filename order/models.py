from django.db import models
from django.contrib.auth.models import User
from sqlalchemy import false
from product.models import Product
from user.models import UserProfile

# Create your models here.

class ShopCart(models.Model):
    customer = models.ForeignKey(UserProfile,on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product,on_delete= models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0,null=True)

    def __str__(self):
        return '"user" : {}, "product" : {} , "quantity" : {}'.format(self.customer, self.product,self.quantity)
    
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
    customer = models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null =True)
    code = models.CharField(max_length=5,editable=False)
    status = models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True,max_length=20,null=True)
    adminnote = models.CharField(blank=True,max_length=150,null=True)

    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now=True)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    def __str__(self):
        return self.customer.user.username

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    order = models.ForeignKey(Order,on_delete = models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now=True)


    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return self.product.title

class ShippingAddress(models.Model):
    customer = models.ForeignKey(UserProfile,on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    address = models.CharField(max_length=300,null=False)
    phone = models.CharField(max_length=15, null=True)
    city = models.CharField(max_length=200,null=False)
    country = models.CharField(max_length = 100, null =True)
    state = models.CharField(max_length=200,null=False)
    zipcode = models.CharField(max_length=200,null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
