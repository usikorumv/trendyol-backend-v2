from rest_framework import serializers
from .models import *


class ImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('url',)


class ProductSizesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='size.name', read_only=True)
    slug = serializers.CharField(source='size.slug', read_only=True)

    class Meta:
        model = ProductSize
        fields = ('name', 'slug', 'price', 'in_stock',)
