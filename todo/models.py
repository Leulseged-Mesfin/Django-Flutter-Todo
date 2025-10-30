from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders', blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)