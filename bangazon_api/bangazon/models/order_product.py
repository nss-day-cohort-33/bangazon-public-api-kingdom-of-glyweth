"""Module for the Order_Product"""
from django.db import models
from .order import Order
from .product import Product

class Order_Products(models.Model):
    """Model class for Order_Products"""
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.CharField(max_length=300)
    
    class Meta:
        verbose_name = ("order_product")
        verbose_name_plural = ("order_products")