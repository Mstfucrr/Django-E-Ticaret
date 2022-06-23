from django.contrib import admin

from order.models import Order, OrderItem, ShippingAddress, ShopCart

# Register your models here.

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['customer','product','quantity','amount']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer','status','get_cart_total','get_cart_items']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product','quantity','get_total']
    
class ShippingAdmin(admin.ModelAdmin):
    list_display = ['customer','city']

admin.site.register(ShopCart,ShopCartAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(ShippingAddress,ShippingAdmin)
admin.site.register(OrderItem,OrderItemAdmin)