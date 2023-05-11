from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(_('username'), max_length=50, unique=True)
    email = models.EmailField(_('Email'), unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']
