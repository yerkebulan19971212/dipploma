from django.contrib import admin
from .models import NoteBooks, Note


admin.site.register([NoteBooks, Note])


class NoteAdmin(admin.ModelAdmin):
    fields = ['name']

