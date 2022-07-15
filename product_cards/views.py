from rest_framework import generics 

from .models import ProductCard
from .serializers import ProductCardSerializer


class ProductCardList(generics.ListCreateAPIView):
    queryset = ProductCard.objects.all()
    serializer_class = ProductCardSerializer


class ProductCardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCard.objects.all()
    serializer_class = ProductCardSerializer
