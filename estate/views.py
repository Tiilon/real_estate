from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from land.models import Advert, Land
from utils.decorators import admin_required
from .forms import EstateFilter
from estate.models import House, PageVisit, PropertyImage, Town


def home_page(request):
    houses = House.objects.filter(is_active=True, status=1).order_by('created_by__is_star')[:4]
    apartments = House.objects.filter(is_active=True, status=1, category='Apartment')
    flats = House.objects.filter(is_active=True, status=1, category='Flat')
    self_contain = House.objects.filter(is_active=True, status=1, category='Self-Contained')
    hostels = House.objects.filter(is_active=True, status=1, category='Hostel')
    lands = Land.objects.filter(is_active=True, status=1).order_by('created_by__is_star')[:4]
    today = timezone.now()
    ads = Advert.objects.filter(page='HP', start_date__lte=today, end_date__gte=today)

    first_ad = ads[0]
    second_ad = ads[1]

    most_visited = House.objects.filter(is_active=True, status=1).order_by('-number_of_page_visits')[:5]

    context = {
        'houses': houses,
        'apartments': apartments,
        'flats':flats,
        'self_contain':self_contain,
        'hostels': hostels,
        'most_visited' : most_visited,
        'first_ad':first_ad,
        'second_ad':second_ad,
        'lands':lands,
    }

    # PageVisit.objects.create(
    #     page='Home Page',
    #     url='http://' + request.get_host() + reverse_lazy('homepage'),
    #     created_by = request.user if request.user.is_authenticated else None
    # )
    return render(request, 'website/homepage.html', context)


@login_required(login_url='user:login_register')
def list_house(request):
    towns = [t.text for t in Town.objects.all()]
    context = {
        'towns': towns
    }

    if request.method == 'POST':
        acquisition_type = request.POST.get('acquisition_type')
        # property_type = request.POST.get('property_type')
        description = request.POST.get('description')
        category = request.POST.get('category')
        region = request.POST.get('region')
        town = request.POST.get('town')
        number_of_bedrooms = request.POST.get('nob')
        number_of_washrooms = request.POST.get('now')
        number_of_kitchens = request.POST.get('nok')
        is_furnished = request.POST.get('is_furnished')
        has_compound = request.POST.get('has_compound')
        rent_duration = request.POST.get('rent_duration')
        lister = request.POST.get('lister')
        amount = request.POST.get('amount')
        has_garage = request.POST.get('has_garage')
        close_landmark = request.POST.get("close_landmark")
        file1 = request.FILES.get('file1')
        file2 = request.FILES.get('file2')
        file3 = request.FILES.get('file3')
        file4 = request.FILES.get('file4')

        print(request.POST)
        print(request.FILES)

        try:
            town_object = Town.objects.get(text__iexact=town)
        except Town.DoesNotExist:
            town_object = Town(
                text=town,
                region=region,
                created_by=request.user
            )
            town_object.save()

        new_house = House(
            acquisition_type=acquisition_type,
            description=description,
            category=category,
            region=region,
            town=town,
            number_of_bedrooms=number_of_bedrooms,
            number_of_washrooms=number_of_washrooms,
            number_of_kitchen=number_of_kitchens,
            is_furnished = True if is_furnished == 'on' else False,
            has_compound= True if has_compound == 'on' else False,
            has_garage= True if has_garage == 'on' else False,
            amount=amount,
            rent_duration=rent_duration,
            listed_by=lister,
            status=1,
            close_landmark=close_landmark,
            created_by=request.user,
        )
        new_house.save()

        if file1:
            image1= PropertyImage(
                file = file1,
                created_by = request.user
            )
            image1.save()
            new_house.images.add(image1)

        if file2:
            image2= PropertyImage(
                file = file2,
                created_by = request.user
            )
            image2.save()
            new_house.images.add(image2)

        if file3:
            image3= PropertyImage(
                file = file3,
                created_by = request.user
            )
            image3.save()
            new_house.images.add(image3)

        if file4:
            image4= PropertyImage(
                file = file4,
                created_by = request.user
            )
            image4.save()
            new_house.images.add(image4)

        new_house.save()

        return redirect('user:my_properties')
    return render(request, 'website/listing/house.html', context)


@login_required(login_url='user:admin-login')
@admin_required(redirect_url='user:user-permission')
def houses(request):
    object_list = House.objects.all().order_by('-created_at')
    sort = request.GET.get('sort')

    if sort == 'newest':
        object_list = House.objects.all().order_by('-created_at')
    elif sort == 'oldest':
        object_list = House.objects.all().order_by('created_at')
    elif sort == 'amount_high':
        object_list = House.objects.all().order_by('-amount')
    elif sort == 'amount_low':
        object_list = House.objects.all().order_by('amount')
    else:
        object_list = House.objects.all().order_by('-created_at')

    paginator = Paginator(object_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'obj': object_list.count(),
        'sort':sort,
    }
    return render(request, 'estate/houses.html', context)


@login_required(login_url='user:admin-login')
@admin_required(redirect_url='user:user-permission')
def house_details(request, uuid):
    house = House.objects.get(uuid=uuid)
    lister_profile = request.FILES.get('lister_profile')
    form = request.POST.get('form')

    context = {
        'house': house
    }

    if request.method == 'POST':
        if form == 'activate':
            house.lister_profile = lister_profile
            house.is_active = True
            house.save()
            return redirect(reverse('estate:house-details', kwargs={'uuid': house.uuid}))
        elif form == 'deactivate':
            house.is_active = False
            house.save()
            return redirect(reverse('estate:house-details', kwargs={'uuid': house.uuid}))

    return render(request, 'estate/house_details.html', context)


def filter_property(request):
    filter_query = EstateFilter(request.GET, queryset=House.objects.filter(is_active=True, status=1))

    print(filter_query.qs)

    context = {
        'filter': filter_query
    }

    return render(request, 'website/house_filter.html', context)


def website_house_details(request, uuid):
    house = None

    try:
        house = House.objects.get(uuid=uuid)
    except:
        return redirect('homepage')

    if not house.created_by == request.user:
        pv = PageVisit(
            url='http//' + reverse_lazy('estate:website_house_details', kwargs={'uuid':uuid}),
            page=house.category + ' for ' + house.acquisition_type + ' at ' + house.town + ', ' + house.region,
            created_by=request.user if request.user.is_authenticated else None
        )
        pv.save()
        house.page_views.add(pv)
        house.save()

    page_visit = PageVisit.objects.filter(url__icontains=uuid).count()
    house.number_of_page_visits = page_visit
    house.save()

    similar_houses = House.objects.filter(acquisition_type=house.acquisition_type, category=house.category).exclude(uuid=house.uuid)[:2]
    agent_houses = House.objects.filter(created_by=house.created_by)
    agent_hse_count = agent_houses.count()

    context = {
        'house':house,
        'similars':similar_houses,
        'ahc':agent_hse_count,
        'page_visit':page_visit,
    }

    return render(request, 'website/house_details.html', context)


def website_houses(request):
    today = timezone.now().date()
    object_list = House.objects.filter(is_active=True, status=1).order_by('created_by__is_star', '-created_at')
    ads = Advert.objects.filter(start_date__lte=today, end_date__gte=today, page='EP')
    filter = EstateFilter(request.GET, queryset=object_list)
    paginator = Paginator(object_list, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    first_ad,second_ad = None, None

    try:
        first_ad = ads[0]
        second_ad = ads[1]
    except:pass

    context = {
        'filter':filter,
        'page_obj': page_obj,
        'obj': object_list.count(),
        'first_ad':first_ad,
        'second_ad':second_ad,
    }
    return render(request, 'website/houses.html', context)

