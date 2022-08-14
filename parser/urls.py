from django.urls import path, include
from .views import *


urlpatterns = [
    path('parse_categories/', ParseCategory.as_view()),
    path('parse_product_cards/', ParseProductCards.as_view()),
    # TODO: MOVE TO ANOTHER APP
    path('categories-list/', CategoriesView.as_view()),
    path('brand-list/', BrandsView.as_view()),
    path('color-list/', ColorsView.as_view()),
    path('size-list/', SizesView.as_view()),
]
