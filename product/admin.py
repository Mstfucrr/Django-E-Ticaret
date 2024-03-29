from product.models import Category, Comment, Images, Product
from django.contrib import admin
from mptt.admin import MPTTModelAdmin,DraggableMPTTAdmin
from django.utils.html import format_html

# Register your models here.

class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


class ImageAdmin(admin.ModelAdmin):
    list_display = ['title','product','image_tag']
    readonly_fields = ('image_tag',)


class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category','price','amount','image_tag','status','slug']
    readonly_fields = ('image_tag',)
    list_filter = ['status','category']
    inlines = [ProductImageInline]


def make_status_True(modeladmin, request, queryset):
    queryset.update(status='True')
make_status_True.short_description = "Mark selected comments as True"

def make_status_False(modeladmin, request, queryset):
    queryset.update(status='False')
make_status_False.short_description = "Mark selected comments as False"

class CommentAdmin(admin.ModelAdmin):
    list_display = ['customer','rate','product','status']
    list_filter = ['status']
    actions = [make_status_True,make_status_False]





admin.site.register(Comment,CommentAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin) 
admin.site.register(Images,ImageAdmin)

   

