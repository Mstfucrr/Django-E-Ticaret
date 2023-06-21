from order.models import ShopCart, Wishlist
from product.models import Category, Comment, Images, Product
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from home.models import ContactForm, Setting
import json

from user.models import UserProfile

# Create your views here.
def SettingsFunc(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    
    context = {
        'setting' : setting,
        'category':category
    }
    items,total = CookieCart(request)

    context['cart'] = items
    context['total'] = total
    context['CartItemCount'] = len(context['cart'])
    wishList = None
    if request.user.is_authenticated:
        customer = UserProfile.objects.get(user_id=request.user.id)
        wishList = Wishlist.objects.filter(customer_id=customer.id)
        context['wishList'] = [x.product for x in wishList]

    
    return context

def CookieCart(request): 
    items = []
    total = 0
    if request.user.is_authenticated:
        customer = UserProfile.objects.get(user_id=request.user.id)
        items = ShopCart.objects.filter(customer_id= customer.id)
        total = sum([x.amount for x in items])
    else: 
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        
        for i in cart:
            product = Product.objects.get(id=i)
            total += product.price * cart[i]["quantity"]
            item = {
                'product' : product,
                'quantity' : cart[i]['quantity'], 
            }
            items.append(item)
    return items, total


def index(request):
    context = SettingsFunc(request)
    manCategory = Category.objects.get(title = "Erkek")
    womenCategory = Category.objects.get(title = "Kadın")
    sportsCategory = Category.objects.get(title = "Spor")
    electronicCategory = Category.objects.get(title = "Elektronik")
    images = Images.objects.all()

    context['images'] = images
    context['manCategory'] = manCategory
    context['womenCategory'] = womenCategory
    context['sportsProducts'] = PullProducts(sportsCategory)[:4]
    context['sportsCategory'] = sportsCategory
    context['electronicCategory'] = electronicCategory
    context['electronicProducts'] = PullProducts(electronicCategory)[:4]
    context['manProducts'] = PullProducts(manCategory)[:4]
    context['womenProducts'] = PullProducts(womenCategory)[:4]
    context['slideritems'] = Product.objects.order_by('?')[:4]

    return render(request,'index.html',context)

def category_product(request,id,slug):

    context = SettingsFunc(request)
    categories = Category.objects.filter(id=id) #treequeryset
    category = Category.objects.get(id=id)

    category_children = category.get_children()

    images = Images.objects.all()
    context['categories'] = categories
    context['images'] = images
    context['category_children'] = category_children

    products = PullProducts(category)
    context['products'] = products
    

    return render(request,'products.html',context)

def search_product(request):
    context = SettingsFunc(request)
    key = request.GET.get('searchArea')
    if request.method == 'GET' and key:
        # önce kategoriye bak eğer yoksa ürünlere bak
        categories = Category.objects.filter(title__contains=key)
        products = Product.objects.filter(title__contains=key)
        # kategorilerin içindeki ürünleri çek
        for category in categories:
            products = products | Product.objects.filter(category_id=category.id) # | = union operatorü 
            # union operatorü ile iki queryseti birleştiriyoruz
            # union = birleşim

        # productsın içindeki aynı ürünleri sil
        products = list(dict.fromkeys(products))
        context['products'] = products
        images = Images.objects.all()
        context['images'] = images
        context['key'] = key
    return render(request,'products_search.html',context)


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def search_auto(request):
    if is_ajax(request):
        q = request.GET.get('term', '')
        categorys = Category.objects.filter(title__contains=q)
        results = []
        for category in categorys:
            categorys_json = {}
            categorys_json = category.title
            results.append(categorys_json)

        if len(results) == 0:
            products = Product.objects.filter(title__contains=q)
            for product in products:
                product_json = {}
                product_json = product.title
                results.append(product_json)

        data = json.dumps(results)

    else:
      data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)



def PullProducts(category):
    Mycategor = [cate for cate in Category.objects.all() if str(category) in str(cate)]
    productslist = []
    for idm in Mycategor:
        try:
            for index in Product.objects.filter(category_id = idm.id):
                productslist.append(index)
        except Exception as e:
            print(e)
    return productslist


def product_detail(request,id,slug):
    context = SettingsFunc(request)
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id = id)
    comments = Comment.objects.filter(product_id = id)
    context['product'] = product
    context['images'] = images
    context['comments'] = comments

    return render(request,"product_detail.html",context)


def contactUs(request):
    context = SettingsFunc(request)
    
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


def about(request):
    context = SettingsFunc(request)
    return render(request,'about.html',context)

def references(request):
    context = SettingsFunc(request)
    return render(request,'references.html',context)

