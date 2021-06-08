from functools import wraps
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import resolve_url,redirect


def user_passes_test(test_func, redirect_url=None):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            path = request.build_absolute_uri()
            resolved_redirect_url = resolve_url(redirect_url or settings.PERMISSION_REDIRECT_URL)

            return redirect(resolved_redirect_url)
        return _wrapped_view
    return decorator


def admin_required(function=None, redirect_url=None):
    actual_decorator = user_passes_test(
        lambda u: u.user_type == 'AD',
        redirect_url=redirect_url
    )

    if function:
        return actual_decorator(function)
    return actual_decorator