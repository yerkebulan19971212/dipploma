from django.contrib import admin
from .models import NoteBooks, Note, Favorite


admin.site.register([NoteBooks, Note, Favorite])


class NoteAdmin(admin.ModelAdmin):
    fields = ['name']

