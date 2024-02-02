from django.contrib import admin
from .models import *

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','phone','email','total_price']

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
