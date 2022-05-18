from email.mime import image
from home.views import SettingsFunc
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from user.models import UserProfile
# Create your views here.

def account(request):
    context = SettingsFunc()
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
        customer = UserProfile(user=new_user,phone = phone, address=address, city=city, country=country,image=profileImage)
        new_user.save()
        customer.save()

        login(request, new_user)

        return HttpResponseRedirect('/')


