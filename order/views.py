from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from home.views import SettingsFunc
import json

from order.models import ShopCart
from product.models import Product

# Create your views here.


def order(request):
    cart = ShopCart.objects.filter(user_id=request.user.id)
    context = SettingsFunc()
    context['cart'] = cart
    print("order created")
    return render(request,"cart.html",context)

@login_required(login_url='/login')
def addToCart(request,id):
    if request.method == 'POST': 
        cart = ShopCart()
        cart.user = request.user.id
        cart.product = id
        cart.save()
    return HttpResponseRedirect('/')
        

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
    if cart.quantity <= 0 :
        cart.delete()
    return JsonResponse('Item was update',safe=False)
