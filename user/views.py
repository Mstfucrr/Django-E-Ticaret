from home.views import SettingsFunc
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
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
        # username = request.POST['username']

        new_user = User(username=email, first_name=firstname, last_name=lastname, email=email)
        new_user.set_password(password)
        new_user.save()

        login(request, new_user)

        return HttpResponseRedirect('/')


