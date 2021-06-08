import django_filters as df
from estate.models import *


class EstateFilter(df.FilterSet):
    min_price = df.NumberFilter(field_name='amount', lookup_expr='gte')
    max_price = df.NumberFilter(field_name='amount', lookup_expr='lte')
    town = df.ChoiceFilter(choices=Town.objects.all().values_list('text', 'text'), field_name='town')

    class Meta:
        model = House
        fields = ['region', 'acquisition_type', 'category', 'listed_by', 'min_price', 'max_price', 'number_of_bedrooms', 'number_of_washrooms', 'number_of_kitchen' ]

    def __init__(self, *args, **kwargs):
        super(EstateFilter, self).__init__(*args, **kwargs)

        self.form.fields['min_price'].label = 'Min Price'
        self.form.fields['max_price'].label = 'Max Price'