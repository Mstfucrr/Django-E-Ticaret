from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from home.views import SettingsFunc
import json

from order.models import ShopCart
from product.models import Product
from user.models import UserProfile

# Create your views here.


def order(request):
    cart = ShopCart.objects.filter(user_id=request.user.id)
    context = SettingsFunc(request)
    context['cart'] = cart
    total = [x.amount for x in cart]
    context['total'] = sum(total)
    return render(request,"cart.html",context)

    
def Checkout(request):
    context = SettingsFunc(request)
    if request.user.is_authenticated:
        context['customer'] = UserProfile.objects.filter(user_id=request.user.id)[0]

    return render(request,"checkout.html",context)

@login_required(login_url='/login')
def addToCart(request,id):
    if request.method == 'POST': 
        cart = ShopCart()
        cart.user = request.user.id
        cart.product = id
        cart.save()
    return HttpResponseRedirect('/')
        
@login_required(redirect_field_name=None, login_url='/account/')
def UpdateItem(request):
    data = json.loads(request.body)
    productId = data['productid']
    action = data['action']
    cart = ShopCart.objects.get_or_create(user_id=request.user.id, product_id = productId)[0]
    print(cart)
    if action == 'add':
        cart.quantity += 1
    elif action == 'remove':
        cart.quantity -= 1
    cart.save()
    if action == 'AllRemove' or cart.quantity <= 0:
        cart.delete()   
    return JsonResponse('Item was update',safe=False)
