"""eTicaret URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('home/',include('home.urls')),
    path('product/',include('product.urls')),
    path('account/',include('user.urls')),
    path('order/',include('order.urls')),
    path('^ckeditor/', include('ckeditor_uploader.urls')),
    path('about/',views.about,name='about'),
    path('references/',views.references,name='references'),
    path('contactUs/',views.contactUs,name='contactUs'),
    path('category/<int:id>/<slug:slug>/',views.category_product,name='category_product'),
    path('product/<int:id>/<slug:slug>/',views.product_detail,name='product_detail'),
    path('search/', views.search_product, name='search_product'),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('filter_product/displayedProductsIds=<str:displayedProductsIds>&minPrice=<str:minPrice>&maxPrice=<str:maxPrice>/',views.filter_product,name='filter_product'),
    path('sorter_product/displayedProductsIds=<str:displayedProductsIds>&sort=<str:sort>/',views.sorter_product,name='sorter_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)