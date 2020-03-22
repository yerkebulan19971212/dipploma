from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Country(models.Model):
    name = models.CharField(max_length=128)
    short_name = models.CharField(max_length=12)


class Hashtags(models.Model):
    hash_tag = models.CharField(max_length=16)
