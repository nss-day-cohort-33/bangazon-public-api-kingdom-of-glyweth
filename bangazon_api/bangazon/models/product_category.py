from django.db import models

class Product_Category(models.Model):
    """Model for order"""

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("product_category")
        verbose_name_plural = ("product_categories")