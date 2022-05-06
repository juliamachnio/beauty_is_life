import django_filters
from .models import *
from django_filters import DateFilter

class RequestFilter(django_filters.FilterSet):

    #start_date = DateFilter(field_name="service_date", lookup_expr='gte')
    #end_date = DateFilter(field_name="service_date", lookup_expr='lte')

    class Meta:
        model = RequestsRegister
        fields = '__all__'
        #exclude = ['image']
