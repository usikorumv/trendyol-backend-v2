from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from base_product.models import *
from .parser import Client
from .serializers import *


client = Client()


class ParseCategory(APIView):
    # permission_classes = [IsAdminUser,]

    def get(self, request, format=None):
        response = client.parse_categories()
        return Response(response)


class ParseProductCards(APIView):
    # permission_classes = [IsAdminUser,]

    def get(self, request, format=None):
        response = client.parse_product_cards()
        return Response(response)


class CategoriesView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandsView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ColorsView(ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class SizesView(ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
