from django.urls import path
from . import views

urlpatterns = [
    path('', views.order, name='order'),
    path('addToCart/', views.addToCart, name='addToCart'),
    path('UpdateItem/',views.UpdateItem, name='UpdateItem'),
]

