"""Module for the Order_Product"""
from django.db import models
from .order import Order
from .product import Product

class Order_Products(models.Model):
    """Model class for Order_Products"""
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, related_name="cart")
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name="cart")
    review = models.CharField(max_length=300)

    class Meta:
        verbose_name = ("line_item")
        verbose_name_plural = ("line_items")