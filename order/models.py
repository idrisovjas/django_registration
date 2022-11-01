from django.db import models
from account.models import CustomUser

# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True)
    order_date = models.DateTimeField(auto_now_add=True)
