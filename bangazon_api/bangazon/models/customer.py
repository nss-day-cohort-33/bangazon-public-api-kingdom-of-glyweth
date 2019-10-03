from django.db import models

class Customer(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_lengt=100)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    signup_date = models.DateField(null=True)
    is_activate = models.BooleanField()

    class Meta:
        verbose_name = ("customer")
        verbose_name_plural = ("customers")