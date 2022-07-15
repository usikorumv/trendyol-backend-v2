from django.urls import path, include

from .views import ProductCardDetail, ProductCardList

urlpatterns = [
    path("", ProductCardList.as_view()),
    path('<int:pk>/', ProductCardDetail.as_view()),
]