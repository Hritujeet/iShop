from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.TextField()
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    publish_date = models.DateTimeField()
    img = models.ImageField(upload_to='shop/images', default="")

    def __str__(self) -> str:
        return f"Product {self.name} - {self.price}"
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=now)

    def __str__(self) -> str:
        return f"Review of {self.user} for {self.product}"    
