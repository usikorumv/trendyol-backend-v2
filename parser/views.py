from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from base_product.models import *
from .parser import Scraper
from .serializers import *


scraper = Scraper()


class ParseColor(APIView):
    # permission_classes = [IsAdminUser,]

    def get(self, request, format=None):
        response = scraper.parse_colors()
        return Response(response)


class ParseBrand(APIView):
    # permission_classes = [IsAdminUser,]

    def get(self, request, format=None):
        response = scraper.parse_brands()
        return Response(response)


class ParseSize(APIView):
    # permission_classes = [IsAdminUser,]

    def get(self, request, format=None):
        response = scraper.parse_sizes()
        return Response(response)


class ParseCategory(APIView):
    # permission_classes = [IsAdminUser,]

    def get(self, request, format=None):
        response = scraper.parse_categories()
        return Response(response)


class ParseProductCards(APIView):
    # permission_classes = [IsAdminUser,]

    def get(self, request, format=None):
        response = scraper.parse_product_cards()
        return Response(response)


class CategoriesView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class BrandsView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ColorsView(ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class SizesView(ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
