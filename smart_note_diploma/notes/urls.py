from django.urls import path
from .api.views import (note_book_list_view, favorite_note_list_view)


app_name = "notes"
urlpatterns = [
    path('notebooks/', note_book_list_view),
    path("favorite/", favorite_note_list_view)
]
