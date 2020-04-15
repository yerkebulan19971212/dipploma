from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)

from smart_note_diploma.users.manager import UserManager
from smart_note_diploma.core.models import (TimeStampedModel, Country)


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    """
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30,)
    last_name = models.CharField(max_length=30,)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self
