from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    place = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return str(self.user.username)