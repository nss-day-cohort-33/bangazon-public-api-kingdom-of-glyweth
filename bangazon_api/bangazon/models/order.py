from django.db import models
from .customer import Customer
from .payment import Payment

class Order(models.Model):
    """Model for order"""

    customer_id = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    payment_id = models.ForeignKey(Payment, on_delete=models.DO_NOTHING)
    order_placed_date = models.DateField(null=True, blank=True, default=None)

    class Meta:
        verbose_name = ("order")
        verbose_name_plural = ("orders")