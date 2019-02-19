from .models import Wine
import django_filters

class WineFilter(django_filters.FilterSet):
    class Meta:
        model = Wine
        fields = {
        	'country': ['icontains',],
        	'province':['icontains',],
        	'region_1': ['icontains',],
        }