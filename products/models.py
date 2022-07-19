from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from base_product.models import BaseProduct


class Product(BaseProduct):
    pass

# TODO: ADD REVIEW, LIKE
# TODO: REFACTOR

#
# class Review(models.Model):
#     product = models.ForeignKey(
#         Product, on_delete=models.CASCADE
#     )
#     user = models.CharField(max_length=100)
#     comment = models.TextField(blank=True, null=True)
#     rating = models.SmallIntegerField(
#         validators=[
#             MinValueValidator(1),
#             MaxValueValidator(5),
#         ]
#     )
#
#     class Meta:
#         verbose_name = "Rating"
#         verbose_name_plural = "Ratings"
#
#     def __str__(self):
#         return f"{self.user} {self.rating} {self.comment}"
#
#
# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     like = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f"{self.user} - {self.like}"
#
#     class Meta:
#         verbose_name = "Лайк"
#         verbose_name_plural = "Лайки"
#
#         verbose_name = "Like"
#         verbose_name_plural = "Likes"


# class Review(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
#     product = models.ForeignKey(
#         Product, on_delete=models.CASCADE, related_name="comment"
#     )
#     comment = models.TextField()
#
#     def __str__(self):
#         return f"{self.user} - {self.comment}"
#
#     class Meta:
#         verbose_name = "Review"
#         verbose_name_plural = "Reviews"


# class FavouriteProduct(models.Model):
#     user = models.ForeignKey(User, related_name='favourite', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, related_name='favourite', on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name = 'Favourite'
#         verbose_name_plural = 'Favourites'
