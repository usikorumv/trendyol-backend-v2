from django_filters import rest_framework as filters

from product_cards.models import ProductCard


class ProductCardFilter(filters.FilterSet):
    price_from = filters.NumberFilter(field_name='selling_price', lookup_expr='gte')
    price_to = filters.NumberFilter(field_name='selling_price', lookup_expr='lte')
    category = filters.CharFilter(field_name='category__chain', lookup_expr='icontains')
    brand = filters.CharFilter(field_name='brand__slug')
    size = filters.CharFilter(field_name='show_size__slug')
    color = filters.CharFilter(field_name='show_color__slug')

    class Meta:
        model = ProductCard
        fields = ('price_from', 'price_to', 'category', 'brand', 'size', 'color',)
