from django.db import models
from django.contrib.auth.models import User

from shop.models import Products,Shops

# Create your models here.
class Order(models.Model):
    PAY_OPTION_CHOICES = (
        ('CASH','CASH'),
        ('ONLINE','ONLINE'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='order_user')
    shop = models.ForeignKey(Shops,on_delete=models.CASCADE,related_name='order_shop')
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    address_1 = models.CharField(max_length=250,null=True,blank=True)
    address_2 = models.CharField(max_length=250,null=True,blank=True)
    pincode = models.CharField(max_length=6,null=True,blank=True)
    total_price = models.FloatField(default=0.0)
    pay_option = models.CharField(max_length=10,default='CASH')
    order_created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_item')
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    total_price = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

