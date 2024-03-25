from django.contrib import admin
from .models import *

# Register your models here.
class ShopAdmin(admin.ModelAdmin):
    list_display = ['shop_name','location']

admin.site.register(Shops,ShopAdmin)
admin.site.register(ShopImages)
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(Review)