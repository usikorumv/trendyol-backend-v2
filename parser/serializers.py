from rest_framework import serializers
from base_product.models import *
from products.models import Product


# TODO: MOVE TO ANOTHER CLASS
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_title(self, title):
        if Category.objects.filter(slug=title.lower()).exists():
            raise serializers.ValidationError('Такое название уже существует')
        return title

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if not instance.parent:
            representation.pop('parent')
        return representation


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

# class ReviewSerializers(serializers.ModelSerializer):
#
#     class Meta:
#         model = Review
#         fields = ('rating', )
#
#
# class ReviewSerializer(serializers.ModelSerializer):
#     """
#     Сериализатор отзывов
#     """
#     user = serializers.ReadOnlyField(source='user.email')
#
#     class Meta:
#         model = Review
#         fields = '__all__'
#
#
# class RetriveReviewSerializer(serializers.ModelSerializer):
#     """
#     Сериализатор для детального отзыва
#     """
#     class Meta:
#         model = Product
#         fields = '__all__'
#
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         rating_result = 0
#         representation['likes'] = instance.like.filter(like=True).count()
#         representation['sizes'] = ProductAllSizesSerializer(instance.all_sizes.all(), many=True).data
#         for i in instance.rating.all():
#             rating_result += int(i.rating)
#         if instance.rating.all().count() == 0:
#             representation['rating'] = rating_result
#         else:
#             representation['rating'] = rating_result / instance.rating.all().count()
#         representation["images"] = ImageSerializer(instance.images.all(), many=True).data
#         representation['reviews'] = ReviewSerializer(instance.comment.all(), many=True).data
#         representation['colors'] = ProductSerializer(instance.children.all(), many=True).data
#         return representation
