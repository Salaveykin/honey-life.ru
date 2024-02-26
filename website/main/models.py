from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='png')

    def __str__(self):
        return self.name
    
class Order(models.Model):
    user = models.CharField(max_length=100)
    products = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.user