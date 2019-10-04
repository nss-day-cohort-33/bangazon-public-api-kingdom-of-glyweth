"""Model for order"""
from django.db import models
from .customer import Customer
from .payment import Payment

class Order(models.Model):
    """Model for order"""
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    payment = models.ForeignKey(Payment, on_delete=models.DO_NOTHING)
    order_placed_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("order")
        verbose_name_plural = ("orders")