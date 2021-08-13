from product.models import Product
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from home.models import Contact, ContactForm, Setting


# Create your views here.
def SettingsFunc():
    setting = Setting.objects.get(pk=1)
    context = {'setting' : setting}
    return context



def index(request):
    context = SettingsFunc()
    slideritems = Product.objects.all()[:4]
    context['slideritems'] = slideritems
    return render(request,'index.html',context)

def about(request):
    context = SettingsFunc()
    return render(request,'about.html',context)

def references(request):
    context = SettingsFunc()
    return render(request,'references.html',context)


def contactUs(request):
    setting = Setting.objects.get(pk=1)
    

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.ip = request.META.get('REMOTE_ADDR')
            form.save()
            form = ContactForm()
            return HttpResponseRedirect('/contactUs')
    else:
        form = ContactForm()
    
    context = {
        'setting' : setting,
        'form':form,
        }
    request.methot = 'GET'
    return render(request,'contactUs.html',context)

