import json
from home.views import SettingsFunc
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from user.models import UserProfile
# Create your views here.

def account(request):
    context = SettingsFunc()
    customer = UserProfile.objects.get(user_id=request.user.id)
    context['customer'] = customer
    return render(request,'account.html',context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # username none değeri olmadığı için değeri email'e eiştlendi
        user = authenticate(request, username=email, email=email, password=password)
        if user is None:
            messages.warning(request,'E-posta adresiniz veya paralonız hatalı!')
            return redirect('account')
        
        login(request, user)
        

        return HttpResponseRedirect('/')

def UserUpdate(request):
    if request.method == 'POST':
    
        data = json.loads(request.body)
        print(data)
        action = data['action']
        customer_id = data['customer']
        user = get_object_or_404(User, id=customer_id)
        customer = get_object_or_404(UserProfile, user_id = customer_id)

        if ( action == "info"):
            user.first_name = data['infoUpdate']['name']
            user.last_name = data['infoUpdate']['lastname']
        elif (action == "contact"):
            customer.email = data['infoUpdate']['email']
            customer.phone = data['infoUpdate']['phone']
        elif (action == 'address'):
            customer.address = data['infoUpdate']['address']
            customer.country = data['infoUpdate']['country']
            customer.city = data['infoUpdate']['city']

        # user.save()
        # customer.save()
        messages.success(request,"Bilgileriniz başarıyla güncellendi !")
        request.method = "GET"
        return redirect("account")
    return HttpResponseRedirect('/')

def register_view(request): 
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        country = request.POST['country']
        profileImage = request.POST['profileImage']
        # username = request.POST['username']

        new_user = User(username=email, first_name=firstname, last_name=lastname, email=email)
        new_user.set_password(password)
        new_user.save()
        customer = UserProfile(user=new_user,phone = phone, address=address, city=city, country=country,image=profileImage)
        customer.save()

        login(request, new_user)

        return HttpResponseRedirect('/')


