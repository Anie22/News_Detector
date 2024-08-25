from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from account.managers import UserManager

# Create your models here.

class UserModel(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(verbose_name='Full Name', max_length=1075, unique=False)
    user_name = models.CharField(verbose_name='User Nmae', max_length=50, unique=True)
    email = models.EmailField(verbose_name='Email', max_length=200, unique=True)
    date_joined = models.DateTimeField(verbose_name='Jonied on', auto_created=True, auto_now=True)
    last_seen = models.DateTimeField(verbose_name='Onlined on', auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ('full_name', 'user_name')

    objects = UserManager()

    def __str__(self):
        return self.full_name

class UserProfile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    user_image = models.ImageField()

    def __str__(self):
        return f'{self.user}.profile'