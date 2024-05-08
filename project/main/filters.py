import django_filters
from .models import *
from django_filters import RangeFilter
class OrderFilter(django_filters.FilterSet):
    prix = RangeFilter(field_name='prix')
    class Meta:
        model = Product
        fields=['gender','title','prix','category','tag']