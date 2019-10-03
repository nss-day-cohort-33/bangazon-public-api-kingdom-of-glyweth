from django.db import models

class Order(models.Model):

    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    order_placed_date = models.DateField(null=True, blank=True, default=None)

    class Meta:
        verbose_name = ("order")
        verbose_name_plural = ("orders")