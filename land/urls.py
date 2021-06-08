from django.urls import path
from .views import *

app_name = 'land'

urlpatterns = [
    path('list-land/', list_land, name='list-land'),
    path('', lands, name='lands'),
    path('land-details/<uuid>/', land_details, name='land-details'),
    path('web-land/<uuid>/', website_land_details, name='website_land_details')
]