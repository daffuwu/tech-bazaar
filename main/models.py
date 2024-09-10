from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()

    @property
    def is_expensive(self):
        return self.price>2000
    
    @property
    def is_available(self):
        return self.stock>0
