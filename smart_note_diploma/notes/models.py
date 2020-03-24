from django.db import models
from smart_note_diploma.core.models import (TimeStampedModel, Hashtag, )


class Note(TimeStampedModel):
    name = models.CharField(max_length=250)
    hash_tags = models.ManyToManyField(Hashtag, blank=True)


class NoteBooks(TimeStampedModel):
    name = models.CharField(max_length=250)
    notes = models.ManyToManyField(Note, blank=True)
