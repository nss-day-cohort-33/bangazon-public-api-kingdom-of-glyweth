"""
Joe Kennerly
Model for order
"""
from django.db import models
from .customer import Customer
from .payment import Payment

class Order(models.Model):
    """Model for order
    customer - An order is dependent on a customer. If a customer is removed from the db, remove associated orders.
    payment - A payment is required to indicate a completed order. On creation, payment will be nothing.
    order_placed_date - Save the current date value on creation of an order.
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.DO_NOTHING, blank=True, null=True)
    order_placed_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("order")
        verbose_name_plural = ("orders")