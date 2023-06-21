from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('addcomment/<int:id>', views.addcomment, name='addcomment'),
    path('Get_product_detail/', views.Get_product_detail, name='Get_product_detail')
]