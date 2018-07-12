import django_filters
from rest_framework import filters

from commodity.models import sweaters

class SweatersFilter(filters.FilterSet):

    name = django_filters.CharFilter('sws_name', lookup_expr='icontains')
    # tel = django_filters.CharFilter('s_tel')
    # status = django_filters.CharFilter('s_status')
    # operate_time_min = django_filters.DateTimeFilter('s_operate_time', lookup_expr='gte')
    # operate_time_max = django_filters.DateTimeFilter('s_operate_time', lookup_expr='lte')
    # yuwen_min = django_filters.NumberFilter('s_yunwen', lookup_expr='gte')
    # yuwen_max = django_filters.NumberFilter('s_yunwen', lookup_expr='lte')

    class Meta:
        model=sweaters
        fields = []
