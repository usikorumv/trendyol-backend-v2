from django.db import models


class Category(models.Model):
    title = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, primary_key=True)
    parent = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="children"
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        if not self.parent:
            return self.slug
        else:
            return f"{self.parent} --> {self.slug}"


class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        max_length=100, unique=True, primary_key=True
    )

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, primary_key=True)

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        max_length=100, unique=True, primary_key=True
    )

    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"

    def __str__(self):
        return self.name


class BaseProduct(models.Model):
    campaign = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    rating = models.PositiveIntegerField(
        null=False,
        blank=False)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    show_color = models.ForeignKey(
        Color, on_delete=models.CASCADE, related_name="products"
    )
    show_size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="products")
    discounted_price = models.PositiveIntegerField(blank=True, null=True)
    selling_price = models.PositiveIntegerField()
    original_price = models.PositiveIntegerField()
    currency = models.CharField(max_length=3)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.campaign} {self.name}"


class Image(models.Model):
    url = models.CharField(max_length=1000)
    product = models.ForeignKey(BaseProduct, on_delete=models.CASCADE, related_name="images")

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.link


class ProductSize(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="sizes")
    in_stock = models.BooleanField()
    product = models.ForeignKey(BaseProduct, on_delete=models.CASCADE, related_name="sizes")
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Product Size'
        verbose_name_plural = 'Product Sizes'

    def __str__(self):
        return f"{self.size} {self.product.name}"
