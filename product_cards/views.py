from collections import OrderedDict

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .filters import ProductCardFilter
from .models import ProductCard
from .serializers import ProductCardsSerializer


class ProductCardsPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 100
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))


class ProductCardsViewSet(ModelViewSet):
    queryset = ProductCard.objects.all()
    serializer_class = ProductCardsSerializer
    pagination_class = ProductCardsPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductCardFilter
    search_fields = ['name']

    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # search_fields = ['name']

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer =
    #     return Response(serializer.data)

    # @action(methods=['GET'], detail=True)
    # def recomendation(self, request, pk):
    #     product_id = ProductCard.objects.get(id=pk)
    #     category_of_product = product_id.category
    #     recomendation_product = Product.objects.filter(category=category_of_product)
    #     serializer = ProductSerializer(recomendation_product, many=True)
    #
    #     return Response(serializer.data)
    #
    # @action(methods=['POST'], detail=True)
    # def rating(self, request, pk):
    #     serializer = ReviewSerializers(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     try:
    #         obj = Review.objects.get(product=self.get_object(), user=request.user)
    #         obj.rating = request.data['rating']
    #     except Review.DoesNotExist:
    #         obj = Review(user=request.user, product=self.get_object(), rating=request.data['rating'])
    #
    #     obj.save()
    #     return Response(request.data, status=status.HTTP_201_CREATED)

    # @action(methods=['POST'], detail=True)
    # def like(self, request, pk):
    #     product = self.get_object()
    #     like_obj, _ = Like.objects.get_or_create(product=product, user=request.user)
    #     print(like_obj)
    #     like_obj.like = not like_obj.like
    #     like_obj.save()
    #     status = 'liked'
    #     if not like_obj.like:
    #         status = 'unliked'
    #     return Response({'status': status})


# class ReviewViewset(ModelViewSet):
#     """
#     Представление отзывов
#     """
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class FavouriteDeleteUpdateRetriveView(RetrieveDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
