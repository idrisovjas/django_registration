from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 45)
    price = models.FloatField(max_length = 45)
    image = models.ImageField(null=True,blank=True)


    def __str(self):
        return self.name



