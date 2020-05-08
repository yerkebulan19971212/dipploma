from django.contrib import admin
from .models import NoteBooks, Note,  Text, Image, CheckBox


admin.site.register([NoteBooks, Note,  Text, Image, CheckBox])


class NoteAdmin(admin.ModelAdmin):
    fields = ['name']

