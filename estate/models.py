from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid

ACQUISITION_TYPE = {
    ('Rent', 'Rent'),
    ('Sale', 'Sale')
}

CATEGORY = {
    ('Flat', 'Flat'),
    ('Apartment', 'Apartment'),
    ('Self-Contained', 'Self-Contained'),
    ('Hostel', 'Hostel')
}
REGION = {
    ('Greater Accra', 'Greater Accra'),
    ('Ashanti', 'Ashanti'),
    ('Northern', 'Northern'),
    ('Western', 'Western'),
    ('Eastern', 'Eastern')
}
STATUS = {
    (0, 'Unavailable'),
    (1, 'Available')
}

LISTER = {
    ('Agent', 'Agent'),
    ('Agency', 'Agency'),
    ('Owner', 'Owner')
}


class House(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, blank=True, null=True)
    slug = models.SlugField(max_length=200, blank=True, null=True, unique=True)
    acquisition_type = models.CharField(max_length=100, choices=ACQUISITION_TYPE, blank=True, null=True)
    region = models.CharField(max_length=200, blank=True, null=True, choices=REGION)
    town = models.CharField(max_length=200, blank=True, null=True)
    close_landmark = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, blank=True, null=True)
    is_furnished = models.BooleanField(default=False, blank=True, null=True)
    number_of_bedrooms = models.IntegerField(default=0, blank=True, null=True)
    number_of_washrooms = models.IntegerField(default=0, blank=True, null=True)
    number_of_kitchen = models.IntegerField(default=0, blank=True, null=True)
    has_compound = models.IntegerField(default=0, blank=True, null=True)
    amount = models.DecimalField(default=0.00, blank=True, null=True, decimal_places=2, max_digits=10)
    is_active = models.BooleanField(default=False, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True, choices=STATUS)
    rent_duration = models.CharField(max_length=100, blank=True, null=True)
    listed_by = models.CharField(max_length=250, blank=True, null=True, choices=LISTER)
    lister_profile = models.FileField(upload_to='lister_profile/', blank=True, null=True)
    has_garage = models.BooleanField(blank=True, null=True)
    page_views = models.ManyToManyField('PageVisit', related_name='house_views', blank=True)
    number_of_page_visits = models.IntegerField(blank=True, null=True)
    images = models.ManyToManyField('PropertyImage', related_name='house_images', blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='houses', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'house'
        ordering = ['created_by__is_star', 'created_at']

    def __str__(self):
        return f"{self.description}"


class PageVisit(models.Model):
    page = models.CharField(max_length=200, blank=True, null=True)
    url = models.URLField(max_length=2000, blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='page_visits', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'page_visits'
        ordering = ['created_at']

    def __str__(self):
        return f"{self.page}"


class PropertyImage(models.Model):
    file = models.FileField(upload_to='properties/', blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='images', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'property_image'
        ordering = ['created_at']

    def __str__(self):
        return f"{self.file.name}"


class Town(models.Model):
    text = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='towns',blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'town'
        managed = True
        verbose_name = 'Town'
        verbose_name_plural = 'Towns'

    def __str__(self):
        return self.text

































