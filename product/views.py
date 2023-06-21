import json
from product.models import Comment, CommentForm, Images, Product
from django.http.response import HttpResponse, HttpResponseRedirect ,JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from user.models import UserProfile

# Create your views here.

def index(request):
    return HttpResponse("<h1>Product anasayfa</h1>")


def Get_product_detail(request):
    # body : b'product_id=1'
    body = request.body.decode('utf-8').split('=')[1]
    product_id = int(body)
    product = Product.objects.get(pk=product_id)
    images = Images.objects.filter(product_id=product_id)
    
    return JsonResponse({
        'name': product.title,
        'price': product.price,
        'description': product.description[:500], # ilk 100 karakter alınacak ,
        'image': product.image.url,
        'images' : [image.image.url for image in images],
        'id': product.id,
        'category': product.category.title,
        'category_id': product.category.id,
        'slug': product.slug,
        

    })


    
    

@login_required(login_url='/login')
def addcomment(request,id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            customer_id = UserProfile.objects.get(user_id = request.user.id).id
            print(customer_id)
            data = Comment()
            data.customer_id = customer_id
            data.product_id = id
            data.subject = form.cleaned_data['subject']
            data.comment= form.cleaned_data['comment']
            data.rate= form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,'Yorumunuz için teşekkürler')

            return HttpResponseRedirect(url)
    messages.warning(request,'Yorumunuz Gönderilmedi')
    return HttpResponseRedirect(url)
    
