from django.contrib import admin
from .models import NoteBooks, Note, Favorite, Text, Image, CheckBox


admin.site.register([NoteBooks, Note, Favorite, Text, Image, CheckBox])


class NoteAdmin(admin.ModelAdmin):
    fields = ['name']

