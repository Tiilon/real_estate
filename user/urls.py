from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('admin/login/', admin_login, name='admin-login'),
    path('admin/dashboard/', admin_dashboard, name='admin-dashboard'),
    path('admin/insight/', admin_insight, name='admin-insight'),
    path('admin/new/', new_admin, name='admin-new'),
    path('login-register/', login_register, name='login_register'),
    path('logout/', user_logout, name='logout'),
    path('my-properties/', my_properties, name='my_properties'),
    path('site/visitors/', site_visitors, name='site-visitors'),
    path('admin/user/<id>/', admin_user_details, name='admin_user_details'),
    path('web/user/<uuid>/', web_user_details, name="web_user_details"),
    path('site/visitor/<slug>/', site_visitor_details, name="site-visitor"),
    path('error403/', user_permission, name="user-permission"),
]