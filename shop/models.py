from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Shops(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=100)
    store_cover = models.ImageField(upload_to='shop')
    location = models.CharField(max_length=100)
    rating = models.DecimalField(default=0.0,max_digits=2,decimal_places=1)
    is_open = models.BooleanField(default=True)
    approved = models.BooleanField(default=False)


class ShopImages(models.Model):
    shop = models.ForeignKey(Shops,on_delete=models.CASCADE,related_name='shop_images')
    img = models.ImageField(upload_to='shop_images')



class Products(models.Model):
    shop = models.ForeignKey(Shops,on_delete=models.CASCADE,related_name='product_shop')
    item_name = models.CharField(max_length=100)
    product_img = models.ImageField(upload_to='product_images')
    price = models.FloatField()
    tags = models.TextField(null=True,blank=True)
    in_stock = models.BooleanField(default=True)


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='cart_user')
    item = models.ForeignKey(Products,on_delete=models.CASCADE,related_name='cart_item')
    quantity = models.IntegerField(default=1)
    total_price = models.FloatField(default=0.0)


class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='review_user')
    shop = models.ForeignKey(Shops,on_delete=models.CASCADE,related_name='review_shop')
    rating = models.DecimalField(default=0.0,max_digits=2,decimal_places=1)
    review = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
