from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from order.models import ShopCart

# Create your views here.
@login_required(login_url='/login')
def addToCart(request,id):
    if request.method == 'POST': 
        cart = ShopCart()
        cart.user = request.user.id
        cart.product = id
        