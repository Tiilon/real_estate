"""real_estate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from advert import urls as ad_urls
from estate.views import home_page
from user import urls as user_urls
from estate import urls as estate_urls
from land import urls as land_urls
from land.views import *
from estate.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='homepage'),
    path('house/', include(estate_urls, namespace='estate')),
    path('user/', include(user_urls, namespace='user')),
    path('land/', include(land_urls, namespace='land')),
    path('advert/', include(ad_urls, namespace='adverts')),
    path('houses/', website_houses, name='houses'),
    path('lands/', website_lands, name='lands'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
