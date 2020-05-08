from django.urls import path
from .api.views import (
    note_book_list_view, note_list_by_note_book, favorite_note_list_view,
    all_note_list_view, create_note_view,
)


app_name = "notes"
urlpatterns = [
    path('create/', create_note_view),
    path('all-notes/', all_note_list_view),
    path('notebooks/', note_book_list_view),
    path('notebooks/<int:pk>/notes/', note_list_by_note_book),
    path("favorites/", favorite_note_list_view),
]
