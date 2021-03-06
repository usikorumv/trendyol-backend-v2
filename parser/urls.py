from django.urls import path, include
from .views import *


urlpatterns = [
    # path('parse_colors/', ParseColor.as_view()),
    # path('parse_brands/', ParseBrand.as_view()),
    # path('parse_sizes/', ParseSize.as_view()),
    path('parse_categories/', ParseCategory.as_view()),
    path('parse_product_cards/', ParseProductCards.as_view()),
    # TODO: MOVE TO ANOTHER APP
    path('brand-list/', BrandsView.as_view()),
    path('color-list/', ColorsView.as_view()),
    path('size-list/', SizesView.as_view()),
]
