from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils.text import slugify
from estate.models import House
from land.models import Land
from user.models import User, Activity
from utils.decorators import admin_required


@login_required(login_url='user:login-register')
def user_permission(request):
    return render(request, '403.html')


def admin_login(request):

    if request.user.is_authenticated:
        return redirect('user:admin-dashboard')
    context = {
        'email': '',
        'password': '',
        'remember_me': ''
    }
    try:
        if request.session['remember_me'] == 'on':
            email = request.session['email']
            password = request.session['password']
            context['email'] = email
            context['password'] = password
            context['remember_me'] = request.session['remember_me']
    except:
        pass
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        try:
            user = authenticate(request=request, username=email, password=password)
            if user is None:
                messages.error(request, 'Credentials Do Not Match')
                return redirect('user:admin-login')
            elif user and user.user_type != 'AD':
                messages.error(request, 'You Do Not Have Permissions To Login Here')
                return redirect('user:admin-login')
            elif user and not user.is_active:
                messages.error(request, 'Your account has been blocked. Please contact admin to activate')
                return redirect('user:admin-login')
            # elif user and user.reset_password:
            login(request, user)

            user.is_logged_in = True
            user.login_at = timezone.now()
            user.save()

            if remember_me == 'on':
                request.session['email'] = email
                request.session['password'] = password
                request.session['remember_me'] = remember_me
            else:
                request.session['email'] = ''
                request.session['password'] = ''
                request.session['remember_me'] = 'off'
            return redirect('user:admin-dashboard')
        except:
            messages.error(request, 'Something went wrong')
            return redirect('user:admin-login')
    return render(request, 'user/login.html',context)


@login_required(login_url='user:admin-login')
def admin_dashboard(request):
    return render(request, 'user/admin-dashboard.html')


@login_required(login_url='user:admin-login')
@admin_required(redirect_url='user:user-permission')
def admin_insight(request):
    admin_list = User.objects.filter(user_type='AD')
    paginator = Paginator(admin_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }
    return render(request, 'user/admin_insight.html', context)


@login_required(login_url='user:admin-login')
@admin_required(redirect_url='user:user-permission')
def new_admin(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        profile = request.FILES.get('file')
        gender = request.POST.get('gender')
        user_view = request.POST.get('user.view_user')
        user_write = request.POST.get('user.write_user')
        house_view = request.POST.get('estate.view_house')
        house_write= request.POST.get('estate.write_house')

        try:
            User.objects.get(username=email)
            messages.error(request, 'User with this email already exist')
            return redirect('user:admin-new')
        except User.DoesNotExist:
            pass

        new_user = User.objects.create(
            username=email,
            first_name=first_name,
            last_name=last_name,
            profile=profile if profile else None,
            gender=gender,
            slug='-'.join((slugify(first_name), slugify(last_name))),
            user_type='AD',
            reset_password=True
        )
        password = 'password'
        new_user.set_password(password)
        new_user.save()

        try:
            user_view_perm = Permission.objects.get(name='Can view user')
            if user_view == 'on':
                new_user.user_permissions.add(user_view_perm)
            else:
                new_user.user_permissions.remove(user_view_perm)
        except Permission.DoesNotExist:pass

        try:
            user_change_perm = Permission.objects.get(name='Can change user')
            if user_view == 'on':
                new_user.user_permissions.add(user_change_perm)
            else:
                new_user.user_permissions.remove(user_change_perm)
        except Permission.DoesNotExist:
            pass

        try:
            house_view_perm = Permission.objects.get(name='Can view house')
            if user_view == 'on':
                new_user.user_permissions.add(house_view_perm)
            else:
                new_user.user_permissions.remove(house_view_perm)
        except Permission.DoesNotExist:
            pass

        try:
            house_change_perm = Permission.objects.get(name='Can change house')
            if user_view == 'on':
                new_user.user_permissions.add(house_change_perm)
            else:
                new_user.user_permissions.remove(house_change_perm)
        except Permission.DoesNotExist:
            pass
        new_user.save()
        return redirect('user:admin-insight')

    return render(request, "user/new_admin.html")


def login_register(request):
    form = request.POST.get('form')
    context = {
        'login_errors': '',
        'register_errors':'',
    }

    if form == 'login':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            usr = User.objects.get(email=username)
            username = usr.username
        except User.DoesNotExist:pass

        try:
            user = authenticate(request, username=username, password=password)

            if user and user.is_active and user.user_type == 'NU':
                login(request, user)
                user.is_logged_in = True
                user.save()

                redirect_to= request.POST.get('next', request.GET.get('next', ''))

                url_is_safe = url_has_allowed_host_and_scheme(
                    url=redirect_to,
                    allowed_hosts={request.get_host(), *set()},
                    require_https=request.is_secure()
                )

                redirect_url = redirect_to if url_is_safe else ''
                return redirect(redirect_url) if redirect_url else redirect('homepage')

            elif user and not user.is_active:
                context['login_errors'] = 'This account is not active, Contact administrator'
                return render(request, 'website/login_register.html', context)

            else:
                context['login_errors'] = 'Please input a correct username and password. Note that both fields are both case sensitive'
                return render(request, 'website/login_register.html', context)
        except:
            context['login_errors'] = 'Username does not exist'
            return render(request, 'website/login_register.html', context)

    elif form == 'register':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        if password != password2:
            context['register_errors'] = 'Passwords do not match'
            return render(request, 'website/login_register.html', context)

        try:
            User.objects.get(username=username)
            context['register_errors'] = 'User with this username already exist'
            return render((request, 'website/login_register.html', context))
        except User.DoesNotExist:
            pass

        try:
            User.objects.get(email=email)
            context['register_errors'] = 'User with this email already exist'
            return render((request, 'website/login_register.html', context))
        except User.DoesNotExist:pass

        new_user = User.objects.create(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            user_type='NU',
            slug='-'.join((slugify(first_name), slugify(last_name))),
            phone_number=phone_number,
            address=address
        )
        new_user.set_password(password)
        new_user.save()

        messages.success(request, 'Registration was successful. Login to continue')
        return redirect('user:login_register')
    return render(request, 'website/login_register.html', context)


@login_required(login_url='user:login_register')
def user_logout(request):

    request.user.is_logged_in = False
    request.user.save()

    if request.user.user_type == 'NU':
        logout(request)
        return redirect('homepage')
    logout(request)
    return redirect('user:admin-login')


@login_required(login_url='user:login_register')
def my_properties(request):
    houses = House.objects.filter(created_by=request.user)
    lands = Land.objects.filter(created_by=request.user)
    context = {
        'houses': houses,
        'lands': lands,
    }
    return render(request, 'website/my_properties.html', context)


@login_required(login_url='user:login_register')
def site_visitors(request):

    object_list = User.objects.filter(user_type='NU')

    context = {
        'object_list': object_list
    }
    return render(request, 'user/site_visitors.html', context)


@login_required(login_url='user:admin-login')
@admin_required(redirect_url='user:user-permission')
def admin_user_details(request, id):
    admin_user = User.objects.get(id=id)

    context = {
        'admin_user': admin_user
    }
    return render(request, 'user/admin_user_details.html', context)


@login_required(login_url='user:login_register')
def web_user_details(request, uuid):
    web_user = User.objects.get(uuid=uuid)
    houses = House.objects.filter(created_by=web_user).order_by('-created_at')[:3]
    lands = Land.objects.filter(created_by=web_user).order_by('-created_at')[:3]
    total = House.objects.filter(created_by=web_user).count() + Land.objects.filter(created_by=web_user).count()

    context = {
        'web_user': web_user,
        'houses': houses,
        'lands': lands,
        'total': total
    }
    return render(request, 'user/web_user_details.html', context)


@login_required(login_url='user:admin-login')
@admin_required(redirect_url='user:user-permission')
def site_visitor_details(request, slug):

    visitor=None

    try:
        visitor = User.objects.get(slug=slug)
    except:
        pass

    houses = House.objects.filter(created_by=visitor)
    lands = Land.objects.filter(created_by=visitor)
    activities = Activity.objects.filter(actor=visitor).order_by('-created_at')

    context = {
        'object': visitor,
        'houses': houses,
        'lands': lands,
        'activities': activities
    }
    try:
        is_star = request.GET.get('is_star')

        if is_star == 'Yes':
            visitor.is_star = True if visitor.is_star == False else False
            visitor.save()
            return redirect('user:site-visitor', slug)
    except:
        pass

    return render(request, 'user/visitor_detail.html', context)





























