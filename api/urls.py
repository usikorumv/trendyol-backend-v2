from django.urls import path, include

urlpatterns = [
    path("products/", include("products.urls")),
    path("product_cards/", include("product_cards.urls")),
    path("parser/", include("parser.urls")),
]