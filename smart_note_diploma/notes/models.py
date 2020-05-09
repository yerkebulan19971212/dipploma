from django.db import models
from smart_note_diploma.core.models import (TimeStampedModel, HashTag, )
from smart_note_diploma.users.models import User


class Note(TimeStampedModel):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.IntegerField(default=0)
    favorite = models.BooleanField(default=False)
    hash_tags = models.ManyToManyField(HashTag, blank=True)

    def __str__(self):
        return self.name


class NoteBooks(TimeStampedModel):
    name = models.CharField(max_length=250)
    notes = models.ManyToManyField(Note, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    path = models.ImageField(upload_to='images/', blank=True, null=True)
    order = models.IntegerField()
    note = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
        return self.path.name


class Text(models.Model):
    text = models.TextField(default='')
    order = models.IntegerField()
    note = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
        return  self.text


class CheckBox(models.Model):
    text = models.CharField(max_length=250, null=True)
    is_done = models.BooleanField(default=False)
    order = models.IntegerField()
    note = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

