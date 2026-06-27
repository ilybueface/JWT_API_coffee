import django_filters
from django_filters import FilterSet
from .models import Drink


class DrinkFilter(FilterSet):
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Drink
        fields = [
            'max_price',
            'min_price',
            'name',
        ]
