from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
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

def order(request):
    context = SettingsFunc(request)
    if request.user.is_authenticated:
        cart = ShopCart.objects.filter(customer_id= GetCustomer(request).id)
        context['cart'] = cart
        context['total'] = sum([x.amount for x in cart])
    return render(request,"cart.html",context)

    
def Checkout(request):
    context = SettingsFunc(request)
    customer = GetCustomer(request)
    context['customer'] = customer
    if request.method == 'POST':
        
        cart = ShopCart.objects.filter(customer_id= customer.id)

        newOrder = Order(
        code = get_random_string(6).upper(),
        adminnote = request.POST.get('specialnote'),
        )
        if customer is not None:
            newOrder.customer = customer
            newOrder.ip = 123123
        else: 
            # yeni customer
            pass

        print(newOrder.adminnote)
        newOrder.save()
        for c in cart:
            orderitem = OrderItem(
                order=newOrder,
                product=c.product,
                quantity= c.quantity,

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
            shippingaddress.address = request.POST['address']
            shippingaddress.phone = request.POST['phone']
            shippingaddress.city = request.POST['city']
            shippingaddress.country = request.POST['country']
            shippingaddress.state = request.POST['state']
            shippingaddress.zipcode = request.POST['zipcode']
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
