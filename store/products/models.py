from django.db import models

class Product(models.Model):
    
    name = models.CharField(max_length=50)
    amount_in_stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name