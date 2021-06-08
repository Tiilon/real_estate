from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid
from estate.models import PropertyImage

ACQUISITION_TYPE = {
    ('Rent', 'Rent'),
    ('Sale', 'Sale')
}
REGION = {
    ('Greater Accra', 'Greater Accra'),
    ('Ashanti', 'Ashanti'),
    ('Northern', 'Northern'),
    ('Western', 'Western'),
    ('Eastern', 'Eastern')
}

UNIT = {
    ('Plot', 'Plot'),
    ('Acres', 'Acres'),
    ('Sqft', 'Sqft')
}

STATUS = {
    (0, 'Unavailable'),
    (1, 'Available')
}

LAND_TYPE = {
    ('Agriculture', 'Agriculture'),
    ('Commercial', 'Commercial'),
    ('Residential', 'Residential')
}

LISTER = {
    ('Agent', 'Agent'),
    ('Agency', 'Agency'),
    ('Owner', 'Owner')
}

DURATION = {
    (1, 'One week'),
    (2, 'Two weeks'),
    (3, 'One Month')
}


class Land(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, blank=True, null=True)
    region = models.CharField(max_length=250, blank=True, null=True, choices=REGION)
    town = models.CharField(max_length=250, blank=True, null=True)
    size = models.CharField(max_length=250, blank=True, null=True)
    unit = models.CharField(max_length=250, blank=True, null=True, choices=UNIT)
    close_landmark = models.CharField(max_length=200, blank=True, null=True)
    images = models.ManyToManyField(PropertyImage, related_name='land_images', blank=True)
    lister = models.CharField(max_length=200, blank=True, null=True, choices=LISTER)
    lister_profile = models.FileField(upload_to='lister_profile/', blank=True, null=True)
    owner_name = models.CharField(max_length=100, blank=True, null=True)
    owner_contact = models.CharField(max_length=100, blank=True, null=True)
    attachments = models.BooleanField(default=False)
    documents = models.FileField(upload_to='land_docs/', blank=True, null=True)
    land_type = models.CharField(max_length=250, blank=True, null=True, choices=LAND_TYPE)
    acquisition_type = models.CharField(max_length=250, blank=True, null=True, choices=ACQUISITION_TYPE)
    amount = models.DecimalField(default=0.00, blank=True, null=True, decimal_places=2, max_digits=10)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True, choices=STATUS)
    is_active = models.BooleanField(default=False)
    rent_duration = models.CharField(max_length=200, blank=True, null=True)
    page_views = models.ManyToManyField('estate.PageVisit', related_name='land_views', blank=True)
    number_of_page_visits = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='lands', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.town + ', ' + self.region

    class Meta:
        db_table = 'land'
        ordering = ['-created_at']
        verbose_name = 'land'
        verbose_name_plural = 'lands'


PAGES = {
    ('HP', 'Home Page'),
    ('LDP', 'Lands Details Page'),
    ('HDP', 'House Details Page'),
    ('EP', 'Estate Page'),
    ('LP', 'Land Page'),
}


class Advert(models.Model):
    company = models.CharField(max_length=250, blank=True, null=True)
    image = models.FileField(upload_to='advert/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    page = models.CharField(max_length=250, blank=True, null=True, choices=PAGES)
    is_active = models.BooleanField(default=True)
    duration = models.IntegerField(default=0, blank=True, null=True, choices=DURATION)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(null=True, blank=True)
    amount = models.DecimalField(default=0.00, blank=True, null=True, decimal_places=2, max_digits=10)
    click_counts = models.IntegerField(default=0, blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='ads', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.company

    class Meta:
        db_table = 'ads'
        ordering = ['-created_at']