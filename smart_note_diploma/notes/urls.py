from django.urls import path
from .api.views import (
    note_book_list_view, note_list_by_note_book, favorite_note_list_view,
    all_note_list_view
)


app_name = "notes"
urlpatterns = [
    path('all-notes/', all_note_list_view),
    path('notebooks/', note_book_list_view),
    path('notebooks/<int:pk>/notes/', note_list_by_note_book),
    path("favorite/", favorite_note_list_view),
]
