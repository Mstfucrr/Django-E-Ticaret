from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from home.views import SettingsFunc
import json

from order.models import ShopCart
from product.models import Product
from user.models import UserProfile

# Create your views here.

def GetCustomer(request):
    if request.user.is_authenticated:
        return UserProfile.objects.get(user_id=request.user.id)
    return None

def order(request):
    context = SettingsFunc(request)
    if request.user.is_authenticated:
        cart = ShopCart.objects.filter(customer_id= GetCustomer(request).id)
        context['cart'] = cart
        context['total'] = sum([x.amount for x in cart])
    return render(request,"cart.html",context)

    
def Checkout(request):
    context = SettingsFunc(request)
    context['customer'] = GetCustomer(request)

    return render(request,"checkout.html",context)

        
@login_required(redirect_field_name=None, login_url='/account/')
def UpdateItem(request):
    data = json.loads(request.body)
    productId = data['productid']
    action = data['action']
    cart = ShopCart.objects.get_or_create(customer_id=GetCustomer(request).id, product_id = productId)[0]
    if action == 'add':
        cart.quantity += 1
    elif action == 'remove':
        cart.quantity -= 1
    cart.save()
    if action == 'AllRemove' or cart.quantity <= 0:
        cart.delete()   
    return JsonResponse('Item was update',safe=False)
