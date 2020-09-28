import django_filters

from django_filters import DateFilter, CharFilter
from .models import *

class OrderFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="date_created", lookup_expr="gt")
    # end_date = DateFilter(field_name="date_created", lookup_expr="lt")
    note = CharFilter(field_name="note", lookup_expr="icontains") # ignore case sensitive "icontains"
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer' , 'date_created']