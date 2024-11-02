from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(null = False)
    seller = models.ForeignKey(User, related_name="products_for_sale", on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, related_name="purchased_products", null=True, blank=True, on_delete=models.SET_NULL)
    is_seller_anonymous = models.BooleanField(default=False)
    is_buyer_anonymous = models.BooleanField(default=True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {'Sold' if self.is_sold else 'Available'}"
