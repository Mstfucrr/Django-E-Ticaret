from product.models import Category, Product
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from home.models import Contact, ContactForm, Setting


# Create your views here.
def SettingsFunc():
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {
        'setting' : setting,
        'category':category
    }

    return context



def index(request):
    context = SettingsFunc()
    
    manProducts = ManProducts()
    womenProducts = WomenProducts()
    manCategory = Category.objects.get(title = "Erkek")
    womenCategory = Category.objects.get(title = "Kadın")
    slideritems = Product.objects.all()[:4]
    
    context['manCategory'] = manCategory
    context['womenCategory'] = womenCategory
    context['manProducts'] = manProducts
    context['womenProducts'] = womenProducts
    context['slideritems'] = slideritems

    return render(request,'index.html',context)

def ManProducts():
    manCategoryChild = Category.objects.get(title = "Erkek").get_children()
    # for ids in manCategoryChild:
    listem = []
    for idm in manCategoryChild:
        try:
            manProducts = Product.objects.filter(category_id = idm.id)
            listem.append(manProducts)             
        except:
            listem = []

    return listem


def WomenProducts():
    womenCategoryChild = Category.objects.get(title = "Kadın").get_children()
    listem = []
    for ids in womenCategoryChild:
        womenProducts = []
        try:
            womenProducts = Product.objects.filter(category_id = ids.id)
            listem.append(womenProducts)
        except:
            listem = []

    return listem









def about(request):
    context = SettingsFunc()
    return render(request,'about.html',context)

def references(request):
    context = SettingsFunc()
    return render(request,'references.html',context)


def category_product(request,id,slug):
    context = SettingsFunc()
    categories = Category.objects.filter(id=id)            
    products = Product.objects.filter(category_id = id)

    current_category = Category.objects.get(pk=id)
    category_children = current_category.get_children()
    
    context['categories'] = categories
    context['category_children'] = category_children

    context['products'] = products
    context['slug'] = slug
    

    return render(request,'products.html',context)


def contactUs(request):
    context = SettingsFunc()
    
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

    context['form'] = form
    request.methot = 'GET'
    return render(request,'contactUs.html',context)

