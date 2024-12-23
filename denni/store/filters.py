from django_filters import FilterSet
from .models import *


class ShoesFilter(FilterSet):
    class Meta:
        model = Shoes
        fields = {
            'brand': ['exact'],
            'category': ['exact'],
            'price': ['gt', 'lt'],
        }