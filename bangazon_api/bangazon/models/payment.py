"""Module for for Payment"""
from django.db import models
from .customer import Customer

class Payment(models.Model):
    """Model class for Payment"""
    merchant_name = models.CharField(max_length=25)
    account_number = models.CharField(max_length=25)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    creation_date =  models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateField(null=True, blank=True, default=None)

    class Meta:
        verbose_name = ("payment")
        verbose_name_plural = ("payments")