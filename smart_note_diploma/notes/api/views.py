from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from smart_note_diploma.notes.api.serializers import (NoteBookSeriallizer, FavoriteSerializer)
from smart_note_diploma.notes.models import (NoteBooks, Favorite)


class NoteBookListView(ListAPIView):
    serializer_class = NoteBookSeriallizer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        queryset = NoteBooks.objects.filter(notes__user=user).distinct()
        return queryset


note_book_list_view = NoteBookListView.as_view()


class GetFavoriteView(ListAPIView):
    serializer_class = FavoriteSerializer
    # permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)


favorite_note_list_view = GetFavoriteView.as_view()
