from django.urls import path
from .views import *

app_name = 'estate'

urlpatterns = [
    path('list-house/', list_house, name='list-house'),
    path('', houses, name="houses"),
    path('house-details/<uuid>', house_details, name="house-details"),
    path('house/filter', filter_property, name='filter-property'),
    path('details/<uuid>/', website_house_details, name='website_house_details'),
]