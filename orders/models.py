from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2) 
    status = models.CharField(max_length=50, default="Pending")  
    payment_status = models.CharField(max_length=50, default="Unpaid")
    payment_id = models.CharField(max_length=50, null=True)
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

# class Meta:
#     verbose_name_plural = 'Orders Items'

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')  # Associate with an Order
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # The product ordered
    quantity = models.PositiveIntegerField()  # Number of products ordered
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product at the time of order

    def __str__(self):
        return f"{self.quantity} of {self.product.name} for Order {self.order.id}"