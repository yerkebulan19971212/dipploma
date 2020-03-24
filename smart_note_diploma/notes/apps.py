from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NotesConfig(AppConfig):
    name = 'smart_note_diploma.notes'
    verbose_name = _("Notes")
