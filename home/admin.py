from django.contrib import admin
from home.models import Contact, Setting
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','subject','status']
    list_filter = ['status']


admin.site.register(Setting)
admin.site.register(Contact,ContactAdmin)