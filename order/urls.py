from django.urls import path
from . import views

urlpatterns = [
    path('', views.Cart, name='order'),
    path('UpdateItem/',views.UpdateItem, name='UpdateItem'),
    path('checkout/', views.Checkout, name='Checkout'),
    path('wishlist/', views.WishlistView, name='Wishlist'),
    path('wishListUpdateItem/',views.wishListUpdateItem, name='wishListUpdateItem')
]

