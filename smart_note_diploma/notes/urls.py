from django.urls import path
from .api.views import (
    note_book_list_view, note_list_by_note_book, favorite_note_list_view,
    all_note_list_view, create_note_view, create_note_book_view, add_to_favorite_view,
    get_note_page_view, add_note_to_the_note_book_view, filter_notes_by_hash_tags_view
)


app_name = "notes"
urlpatterns = [
    path('create/', create_note_view),
    path('<int:pk>/', get_note_page_view),
    path('notebooks/create/', create_note_book_view),
    path('all-notes/', all_note_list_view),
    path('notebooks/', note_book_list_view),
    path('notebooks/<int:pk>/notes/', note_list_by_note_book),
    path('notebooks/<int:pk>/add-notes/', add_note_to_the_note_book_view),
    path("favorites/", favorite_note_list_view),
    path("add/favorite/<int:pk>/", add_to_favorite_view),
    path('filter', filter_notes_by_hash_tags_view)
]
