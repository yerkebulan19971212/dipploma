from django.db import models
from smart_note_diploma.core.models import (TimeStampedModel, Hashtag, )
from smart_note_diploma.users.models import User


class Note(TimeStampedModel):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hash_tags = models.ManyToManyField(Hashtag, blank=True)


class NoteBooks(TimeStampedModel):
    name = models.CharField(max_length=250)
    notes = models.ManyToManyField(Note, blank=True)


class Favorite(TimeStampedModel):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
