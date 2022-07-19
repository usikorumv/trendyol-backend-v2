from django_filters import rest_framework as filters

from product_cards.models import ProductCard


class ProductCardFilter(filters.FilterSet):
    # filter_f = filters.CharFilter(field_name='category__filter_f', lookup_expr='icontains')
    price_from = filters.NumberFilter(field_name='selling_price', lookup_expr='gte')
    price_to = filters.NumberFilter(field_name='selling_price', lookup_expr='lte')
    category = filters.CharFilter(field_name='category__slug', lookup_expr='iexact')
    brand = filters.CharFilter(field_name='brand__slug', lookup_expr='iexact')
    size = filters.CharFilter(field_name='show_size')
    color = filters.CharFilter(field_name='show_color')

    class Meta:
        model = ProductCard
        fields = ('price_from', 'price_to', 'category', 'brand', 'size', 'color',)
