# rest-framework imports
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

# django imports
from django.shortcuts import get_object_or_404

# local imports
from smart_note_diploma.notes.api.serializers import (
    NoteBookSerializer, FavoriteSerializer, NoteSerializer
)
from smart_note_diploma.notes.models import (Note, NoteBooks, Favorite)


class AllNoteListView(ListAPIView):
    """
    This view return list of All Notes
    for authentication user
    """
    serializer_class = NoteSerializer
    # permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        queryset = Note.objects.filter(user=user)\
            .order_by('modified')
        return queryset


all_note_list_view = AllNoteListView.as_view()


class NoteBookListView(ListAPIView):
    """
    This view return list of all NoteBooks
    for authentication user
    """
    serializer_class = NoteBookSerializer
    # permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        queryset = NoteBooks.objects.filter(notes__user=user)\
            .distinct()\
            .order_by('name')
        return queryset


note_book_list_view = NoteBookListView.as_view()


class NoteListByNoteBookListView(ListAPIView):
    serializer_class = NoteSerializer
    # permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = get_object_or_404(NoteBooks, pk=pk)
        notes = queryset.notes.order_by('name')

        return notes


note_list_by_note_book = NoteListByNoteBookListView.as_view()


class GetFavoriteView(ListAPIView):
    serializer_class = NoteSerializer
    # permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        faivorite = Favorite.objects.filter(user=user)
        faivorite_arr = [i.note.pk for i in faivorite]
        queryset = Note.objects.filter(pk__in=faivorite_arr)
        return queryset


favorite_note_list_view = GetFavoriteView.as_view()
