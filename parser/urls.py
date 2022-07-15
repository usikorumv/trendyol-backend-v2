from django.urls import path, include
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'review', ReviewViewset)
router.register(r'image', ImageView)

urlpatterns = [
    path('parse_color/', ParseColor.as_view()),
    path('parse_brand/', ParseBrand.as_view()),
    path('parse_size/', ParseSize.as_view()),
    path('parse_product/', ParseProduct.as_view()),
]