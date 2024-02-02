from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Shops)
admin.site.register(ShopImages)
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(Review)