import datetime
from dateutil.relativedelta import relativedelta
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from land.models import Advert
from user.models import Activity
from utils.decorators import admin_required


@login_required(login_url='user:admin-login')
@admin_required(redirect_url='user:user-permission')
def advert(request):

    today = timezone.now().date()

    all_object = Advert.objects.all()
    runnings = Advert.objects.filter(start_date__lte=today, end_date__gte=today)
    expires = Advert.objects.exclude(start_date__lte=today, end_date__gte=today)

    context = {
        'all_objects': all_object,
        'runnings': runnings,
        'expires': expires

    }
    if request.method == 'POST':

        company = request.POST.get('company')
        image = request.FILES.get('image')
        website = request.POST.get('website')
        page = request.POST.get('page')
        duration = request.POST.get('duration')
        start_date = request.POST.get('start_date')
        amount = request.POST.get('amount')

        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = None

        if duration == '1':
            end_delta = relativedelta(weeks=1)
            end_date = start_date + end_delta

        elif duration == '2':
            end_delta = relativedelta(weeks=2)
            end_date = start_date + end_delta

        elif duration == '3':
            end_delta = relativedelta(months=1)
            end_date = start_date + end_delta

        print(start_date)
        print(end_date)

        runnings = Advert.objects.filter(start_date__lte=start_date, end_date__gte=end_date, page=page).count()

        if runnings == 2:
            messages.error(request, 'There are two ads already running on this page')
            return redirect('advert:adverts')

        new_ad = Advert.objects.create(
            company=company,
            page=page,
            image=image if image else None,
            website=website,
            duration=duration,
            start_date = start_date,
            end_date=end_date,
            amount=amount if amount else 0.00,
            created_by=request.user,
            is_active=True,
        )

        Activity.objects.create(
            actor=request.user,
            action="Added Advert",
            description=f"Added advert from {new_ad.company}"
        )

        return redirect('advert:adverts')
    return render(request, 'advert/index.html', context)