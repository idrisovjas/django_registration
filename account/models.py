from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=40,null=True,blank=True)
    username = models.CharField(max_length=30,unique=True)
    image = models.ImageField(null=True,blank=True)
    first_name = models.CharField(max_length=40,null=True,blank=True)
    last_name = models.CharField(max_length=40,null=True,blank=True)
    email = models.EmailField(max_length=45,unique=True)
    password = models.CharField(max_length=200)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return self.first_name


