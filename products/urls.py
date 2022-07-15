from django.urls import path, include

from .views import ProductDetail, ProductList

urlpatterns = [
    path("", ProductList.as_view()),
    path('<int:pk>/', ProductDetail.as_view()),
]
