from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from smart_note_diploma.notes.api.serializers import (NoteBookSeriallizer)
from smart_note_diploma.notes.models import (NoteBooks)


class NoteBookListView(ListAPIView):
    serializer_class = NoteBookSeriallizer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = NoteBooks.objects.filter(notes__user=user).distinct()  #filter(note__user=user)
        return queryset


note_book_list_view = NoteBookListView.as_view()
