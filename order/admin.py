from django.contrib import admin

from order.models import Order, OrderItem, ShippingAddress, ShopCart, Wishlist

# Register your models here.

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['customer','product','quantity','amount']

class WishlistAdmin(admin.ModelAdmin):
    list_display = ['customer','product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['created_at','customer','status','get_cart_total','get_cart_items']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'product','quantity','get_total']
    
class ShippingAdmin(admin.ModelAdmin):
    list_display = ['customer','city','address','country','state','date_added']

admin.site.register(ShopCart,ShopCartAdmin)
admin.site.register(Wishlist,WishlistAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(ShippingAddress,ShippingAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
