from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductCardsViewSet

router = DefaultRouter()
router.register(r'', ProductCardsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]