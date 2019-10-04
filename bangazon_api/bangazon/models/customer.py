from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    """Model for the Customer - BP"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("customer")
        verbose_name_plural = ("customers")