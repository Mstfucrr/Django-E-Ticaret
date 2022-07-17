from os import name
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string
from home.views import SettingsFunc
import json

from order.models import Order, OrderItem, ShippingAddress, ShopCart
from product.models import Product
from user.models import UserProfile

# Create your views here.

def GetCustomer(request):
    if request.user.is_authenticated:
        return UserProfile.objects.get(user_id=request.user.id)
    return None



def Cart(request):
    context = SettingsFunc(request)     
     
    return render(request,"cart.html",context)

def Checkout(request):
    context = SettingsFunc(request)
    customer = GetCustomer(request)
    context['customer'] = customer

    if request.method == 'POST':
        
        cart = context['cart']
        data = json.loads(request.body)
        addressInfo = data['addressInfo']

        newOrder = Order(
        code = get_random_string(6).upper(),
        adminnote = addressInfo['specialnote'],
        )
        if customer is not None:
            newOrder.customer = customer
            newOrder.ip = 123123
        else: 
            customer, created = UserProfile.objects.get_or_create(
                name = addressInfo['firtname'] + " " + addressInfo['lastname'],
                email = addressInfo['email']
            )
            newOrder.customer = customer
            newOrder.ip = 123123
        print(customer)

        newOrder.save()
        for c in cart:
            orderitem = OrderItem(
                order=newOrder,
                product= c['product'] if c.product is None else c.product,
                quantity= c['quantity'] if c.product is None else c.quantity,

            )
            orderitem.save()
        shippingaddress = ShippingAddress()
            

        shippingaddress.customer = customer
        shippingaddress.order = newOrder
        isMyAddress = json.loads(request.body)['isMyAddress']
        if isMyAddress:
            shippingaddress.address = customer.address
            shippingaddress.phone = customer.phone
            shippingaddress.city = customer.city
            shippingaddress.country = customer.country
            shippingaddress.zipcode = customer.zipcode
        else:
            
            shippingaddress.address = addressInfo['address']
            shippingaddress.phone = addressInfo['phone']
            shippingaddress.city = addressInfo['city']
            shippingaddress.country = addressInfo['country']
            shippingaddress.state = addressInfo['state']
            shippingaddress.zipcode = addressInfo['zipcode']
        shippingaddress.save()
        return redirect("Checkout")


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
