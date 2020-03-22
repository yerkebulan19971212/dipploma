from django.db import models
from smart_note_diploma.core.models import TimeStampedModel


class Note(TimeStampedModel):
    name = models.CharField(max_length=250)
    hastags
