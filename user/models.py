from django.db import models
import uuid
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, password=None, **extra_fields):
        if not username:
            raise ValueError('username is required')

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, first_name, last_name, password):
        user = self.create_user(username=username, first_name=first_name, last_name=last_name, password=password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.user_type = 'AD'
        user.save(using=self.db)
        return user


USER_TYPES = {
    ('AD', 'Admins'),
    ('NU', 'Normal User')
}

GENDER = {
    ('Male', 'Male'),
    ('Female', 'Female')
}


class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, blank=True, null=True)
    slug = models.SlugField(max_length=200, blank=True, null=True, unique=True)
    user_type = models.CharField(max_length=200, choices=USER_TYPES, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True, unique=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_staff = models.BooleanField(default=True, blank=True, null=True)
    is_superuser = models.BooleanField(default=False, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True, unique=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    is_star = models.BooleanField(default=False, blank=True, null=True)
    profile = models.FileField(upload_to='profile/', blank=True,  null=True)
    gender = models.CharField(max_length=100, blank=True, null=True, choices=GENDER)
    reset_password = models.BooleanField(blank=True, null=True)
    is_logged_in = models.BooleanField(blank=True, null=True)
    login_at = models.DateTimeField(blank=True, null=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'user'
        ordering = ['-date_joined']

    def __str__(self):
        return f"{self.get_full_name()}"


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='rating_user', blank=True, null=True)
    rate = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=10)
    feedback = models.CharField(max_length=200, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='ratings', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'rating'

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.rate}"


class Activity(models.Model):
    actor = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='activity_actor', blank=True, null=True)
    action = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'activity'

    def __str__(self):
        return f"{self.actor.get_full_name()} {self.action} {self.description}"