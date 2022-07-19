from django.db import models

from base_product.models import *
from products.models import Product


class ProductCard(BaseProduct):
    pass


class ProductColor(models.Model):
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name="colors")
    product_card = models.ForeignKey(ProductCard, on_delete=models.CASCADE, related_name="colors")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="colors")

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"

    def __str__(self):
        return f"{self.color.name} {self.product.name}"
