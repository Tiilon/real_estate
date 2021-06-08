from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from estate.models import Town, PropertyImage
from land.models import Land


@login_required(login_url='user:login-register')
def list_land(request):
    towns = [t.text for t in Town.objects.all()]
    context = {
        'towns': towns
    }

    if request.method == 'POST':
        acquisition_type = request.POST.get('acquisition_type')
        description = request.POST.get('description')
        land_type = request.POST.get('land_type')
        region = request.POST.get('region')
        town = request.POST.get('town')
        close_landmark = request.POST.get("close_landmark")
        land_size = request.POST.get('size')
        units = request.POST.get('unit')
        amount = request.POST.get('amount')
        rent_duration = request.POST.get('rent_duration')
        lister = request.POST.get('lister')

        file1 = request.FILES.get('file1')
        file2 = request.FILES.get('file2')
        file3 = request.FILES.get('file3')
        file4 = request.FILES.get('file4')

        try:
            town_object = Town.objects.get(text__iexact=town)
        except Town.DoesNotExist:
            town_object = Town(
                text=town,
                region=region,
                created_by=request.user
            )
            town_object.save()

        new_land = Land(
            acquisition_type=acquisition_type,
            description=description,
            land_type=land_type,
            region=region,
            town=town,
            size=land_size,
            unit=units,
            amount=amount,
            rent_duration=rent_duration,
            lister=lister,
            status=1,
            close_landmark=close_landmark,
            created_by=request.user,
        )
        new_land.save()

        if file1:
            image1 = PropertyImage(
                file = file1,
                created_by = request.user
            )
            image1.save()
            new_land.images.add(image1)

        if file2:
            image2= PropertyImage(
                file = file2,
                created_by = request.user
            )
            image2.save()
            new_land.images.add(image2)

        if file3:
            image3= PropertyImage(
                file = file3,
                created_by = request.user
            )
            image3.save()
            new_land.images.add(image3)

        if file4:
            image4= PropertyImage(
                file = file4,
                created_by = request.user
            )
            image4.save()
            new_land.images.add(image4)

        new_land.save()

        return redirect('user:my_properties')
    return render(request, 'website/listing/land.html',context)


@login_required(login_url='user:admin-login')
def lands(request):
    landss = Land.objects.all().order_by('-created_at')
    sort = request.GET.get('sort')

    if sort == 'newest':
        landss = Land.objects.all().order_by('-created_at')
    elif sort == 'oldest':
        landss = Land.objects.all().order_by('created_at')
    elif sort == 'amount_high':
        landss = Land.objects.all().order_by('-amount')
    elif sort == 'amount_low':
        landss = Land.objects.all().order_by('amount')
    else:
        landss = Land.objects.all().order_by('-created_at')

    paginator = Paginator(landss, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'obj': landss.count(),
        'sort':sort,
    }

    return render(request, 'land/lands.html', context)


@login_required(login_url='user:admin-login')
def land_details(request, uuid):
    land = Land.objects.get(uuid=uuid)
    lister_profile = request.FILES.get('lister_profile')
    docs = request.FILES.get('docs')
    form = request.POST.get('form')

    context = {
        'land': land
    }

    if request.method == 'POST':
        if form == 'activate':
            land.lister_profile = lister_profile
            land.documents = docs
            land.is_active = True
            land.save()
            return redirect(reverse('land:land-details', kwargs={'uuid': land.uuid}))
        elif form == 'deactivate':
            land.is_active = False
            land.save()
            return redirect(reverse('land:land-details', kwargs={'uuid': land.uuid}))
    return render(request, 'land/land_details.html', context)


def website_lands(request):
    object_list = Land.objects.filter(is_active=True, status=1).order_by('created_by__is_star', '-created_at')

    context = {
        'object_list': object_list
    }
    return render(request, 'website/lands.html', context)


def website_land_details(request, uuid):
    land = Land.objects.get(uuid=uuid)
    similar_lands = Land.objects.filter(acquisition_type=land.acquisition_type).exclude(uuid=land.uuid)[:2]

    context = {
        'land': land,
        'similar_lands':  similar_lands
    }

    return render(request, 'website/land_details.html', context)