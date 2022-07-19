from rest_framework import serializers

from .models import *
from base_product.serializers import *


class ProductColorsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='color.name', read_only=True)
    slug = serializers.CharField(source='color.slug', read_only=True)

    class Meta:
        model = ProductColor
        fields = ('name', 'slug', 'product')


class ProductCardsSerializer(serializers.ModelSerializer):
    images = ImagesSerializers(many=True)
    sizes = ProductSizesSerializer(many=True)
    colors = ProductColorsSerializer(many=True)

    class Meta:
        model = ProductCard
        fields = (
            'id', 'images', 'campaign', 'name', 'rating', 'description', 'category', 'show_color', 'show_size', 'sizes',
            'colors', 'discounted_price', 'selling_price', 'original_price', 'currency', 'brand',)
