from django.urls import path
from .views import *

app_name = 'advert'

urlpatterns = [
    path('', advert, name='adverts')
]