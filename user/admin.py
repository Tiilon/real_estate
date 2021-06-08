from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import *


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (_('login'), {'fields': ('username', 'email', 'password', 'uuid', 'slug')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'user_type', 'gender', 'profile')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_star', 'groups', 'user_permissions', 'reset_password')}),
        (_('Important Dates'), {'fields': ('last_login', 'date_joined', 'is_logged_in')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')
        }),
    )

    list_display = ('username', 'first_name', 'last_name', 'user_type')

    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('-date_joined',)


admin.site.register(Activity)
admin.site.register(Rating)
