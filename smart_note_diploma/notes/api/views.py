# rest-framework imports
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

# django imports
from django.shortcuts import get_object_or_404

# local imports
from smart_note_diploma.notes.api.serializers import (
    NoteBookSerializer, FavoriteSerializer, NoteSerializer
)
from smart_note_diploma.notes.models import (NoteBooks, Favorite)


class NoteBookListView(ListAPIView):
    """
    This view return list of all NoteBooks
    for authentication user
    """
    serializer_class = NoteBookSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        queryset = NoteBooks.objects.filter(notes__user=user)\
            .distinct()\
            .order_by('name')
        return queryset


note_book_list_view = NoteBookListView.as_view()


class NoteListByNoteBookListView(ListAPIView):
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = get_object_or_404(NoteBooks, pk=pk)
        notes = queryset.notes.order_by('name')

        return notes


note_list_by_note_book = NoteListByNoteBookListView.as_view()


class GetFavoriteView(ListAPIView):
    serializer_class = FavoriteSerializer
    # permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)


favorite_note_list_view = GetFavoriteView.as_view()
