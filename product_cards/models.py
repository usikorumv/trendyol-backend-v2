from django.db import models

from products.models import Product, Category, Color, Size, Brand


class ProductCard(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="productcard"
    )
    description = models.TextField()
    show_color = models.ForeignKey(
        Color, on_delete=models.CASCADE, related_name="productcard"
    )
    discounted_price = models.PositiveIntegerField(blank=True, null=True)
    selling_price = models.PositiveIntegerField()
    original_price = models.PositiveIntegerField()
    show_size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="productcard")
    campaign = models.CharField(max_length=255)
    currency = models.CharField(max_length=55)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="productcard")

    colors = models.ManyToManyField(Product, related_name='productcard',)

    def __str__(self):
        return self.name




