from django.db import models
from smart_note_diploma.core.models import (TimeStampedModel, Hashtags, )


class Note(TimeStampedModel):
    name = models.CharField(max_length=250)
    hash_tags = models.ManyToManyField(Hashtags, blank=True)


class NoteBooks(TimeStampedModel):
    name = models.CharField(max_length=250)
    notes = models.ManyToManyField(Note, blank=True)
