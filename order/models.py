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