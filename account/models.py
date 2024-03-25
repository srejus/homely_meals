from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    USER = "USER"
    SHOP = "SHOP"

    USER_TYPE_CHOICES = (
        (USER,USER),
        (SHOP,SHOP),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    place = models.CharField(max_length=100,null=True,blank=True)
    user_type = models.CharField(max_length=5,default=USER,choices=USER_TYPE_CHOICES)

    def __str__(self):
        return str(self.user.username)