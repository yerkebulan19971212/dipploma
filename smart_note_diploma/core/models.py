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

    def __str__(self):
        return " - ".join([self.short_name, self.name])


class HashTag(models.Model):
    title = models.CharField(max_length=16)

    def __str__(self):
        return self.title
