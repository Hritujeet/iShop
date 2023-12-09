from django.db import models
from shop.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Cart Item of User {self.user}"
    
class Order(models.Model):
    item = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=10000)
    contactNum = models.IntegerField()
    status = models.CharField(max_length=1000,choices=[('Ordered','Ordered'), ('Shipped','Shipped'), ('Out for Delivery','Out for Delivery'), ('Delivered','Delivered')])

    def __str__(self) -> str:
        return f"Order of User {self.user}"