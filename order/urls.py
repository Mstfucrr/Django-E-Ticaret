from django.urls import path
from . import views

urlpatterns = [
    path('', views.order, name='order'),
    path('UpdateItem/',views.UpdateItem, name='UpdateItem'),
    path('checkout/', views.Checkout, name='Checkout'),
]

