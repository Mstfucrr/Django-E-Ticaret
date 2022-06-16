from django.contrib import admin

from order.models import Order, OrderProduct, ShopCart

# Register your models here.

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['user','product','quantity','amount']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','code','city','country','status']

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user','product','quantity','price','amount','status']
    

admin.site.register(ShopCart,ShopCartAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)