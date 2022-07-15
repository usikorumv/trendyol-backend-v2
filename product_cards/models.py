from django.db import models

from products.models import Product


class ProductCard(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
