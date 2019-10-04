from django.db import models
from .product_category import Product_Category
from .customer import Customer

class Product(models.Model):

    name = models.CharField(max_length = 50)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    price = models.DecimalField(max_digits = 100, decimal_places = 2)
    description = models.CharField(max_length = 300)
    product_category = models.ForeignKey(Product_Category, on_delete = models.CASCADE)
    quantity_available = models.IntegerField()
    quantity_sold = models.IntegerField()
    date_created = models.DateField(null=True)
    image = models.ImageField(upload_to = None)

    class Meta:
        verbose_name = ("product")
        verbose_name_plural = ("products")