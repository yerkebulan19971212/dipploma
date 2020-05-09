# third-party imports
from difflib import SequenceMatcher

# rest-framework imports
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# django imports
from django.shortcuts import get_object_or_404

# local imports
from smart_note_diploma.notes.api.serializers import (
    NoteBookSerializer, NoteSerializer, CreateNoteSerializer,
    CreateNoteBookSerializer, FavoriteNoteSerializer, ImageSerializer,
    GetNoteSerializer,
)
from smart_note_diploma.notes.models import (
    Note, NoteBooks,
    Text, CheckBox,
)
from smart_note_diploma.core.models import (HashTag)


class CreateNoteAPIView(APIView):
    """
    This View creates a new Note
    """
    def post(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        note_serilizer = CreateNoteSerializer(data=data)
        contents = data.get('content')
        if note_serilizer.is_valid():
            hash_tags = data.get('hash_tags')
            hash_tags_arr = []
            if hash_tags:
                for i in hash_tags:
                    obj, created = HashTag.objects.get_or_create(title=i)
                    hash_tags_arr.append(obj)
            note = note_serilizer.save(user=user, hash_tags=hash_tags_arr)
        if contents:
            for i in range(len(contents)):
                value = contents[i].get('value')
                if contents[i].get('type') == 0:
                    text = Text.objects.create(
                        note=note,
                        text=value.get("text"),
                        order=i
                    )
                    text.save()
                elif contents[i].get('type') == 1:
                    check_box = CheckBox.objects.create(
                        note=note,
                        text=value.get("text"),
                        order=i,
                        is_done=value.get("isDone")
                    )
                    check_box.save()
                elif contents[i].get('type') == 2:
                    serializer = ImageSerializer(data=value)
                    if serializer.is_valid():
                        serializer.save(note=note, order=i, )
                    return Response({"11111": "shykpady"}, status.HTTP_201_CREATED)

        return Response(note_serilizer.data, status.HTTP_201_CREATED)


create_note_view = CreateNoteAPIView.as_view()


class GetNoteView(RetrieveAPIView):
    serializer_class = GetNoteSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Note.objects.all()
    lookup_field = 'pk'


get_note_page_view = GetNoteView.as_view()


class FilterNotesView(APIView):
    """
    This view filters Notes by hashtag and by name
    and return Note-list
    """
    def get(self, request, ):
        user = request.user
        word = request.GET['word']

        notes_get_hash = Note.objects.filter(user=user)

        similar_list_hashtags = []
        for i in notes_get_hash:
            for j in i.hash_tags.values():
                similar_percent = SequenceMatcher(None, word, j['title']).ratio()
                if similar_percent > 0.7:
                    similar_list_hashtags.append(j['title'])
        hash_tags = HashTag.objects.filter(title__in=similar_list_hashtags)

        note_name = []
        for note in notes_get_hash:
            similar_percent = SequenceMatcher(None, word, note.name).ratio()
            if similar_percent > 0.5:
                note_name.append(note.name)

        notes = Note.objects.filter(hash_tags__in=hash_tags).distinct()
        notes_by_name = Note.objects.filter(name__in=note_name).distinct()
        # notes_by_word = Note.objects.filter(Q())
        note_serializer = NoteSerializer((notes | notes_by_name).distinct(), many=True)

        return Response(note_serializer.data, status.HTTP_200_OK)


filter_notes_by_hash_tags_view = FilterNotesView.as_view()


class AllNoteListView(ListAPIView):
    """
    This view return list of All Notes
    for authentication user
    """
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        queryset = Note.objects.filter(user=user)\
            .order_by('modified')
        return queryset


all_note_list_view = AllNoteListView.as_view()


class CreateNoteBookView(CreateAPIView):
    """
    This View Creates a new NoteBook
    """
    serializer_class = CreateNoteBookSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


create_note_book_view = CreateNoteBookView.as_view()


class NoteBookListView(ListAPIView):
    """
    This view returns list of all NoteBooks
    for authentication user
    """
    serializer_class = NoteBookSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        queryset = NoteBooks.objects.filter(user=user)\
            .distinct()\
            .order_by('name')
        return queryset


note_book_list_view = NoteBookListView.as_view()


class NoteListByNoteBookListView(ListAPIView):
    """
    This View returns list of Notes by Notebook
    """
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = get_object_or_404(NoteBooks, pk=pk)
        notes = queryset.notes.order_by('name')

        return notes


note_list_by_note_book = NoteListByNoteBookListView.as_view()


class AddNoteToNoteBookView(APIView):

    def post(self, request, pk):
        note_pk = request.data['pk']
        note_book = get_object_or_404(NoteBooks, pk=pk)
        note = get_object_or_404(Note, pk=note_pk)
        note_book.notes.add(note)

        return Response({'status': "successfull"})


add_note_to_the_note_book_view = AddNoteToNoteBookView.as_view()


class AddToFavoriteView(UpdateAPIView):
    """
    This view adds a note to favorites and removes from favorites
    """
    serializer_class = FavoriteNoteSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Note.objects.all()
    lookup_field = 'pk'


add_to_favorite_view = AddToFavoriteView.as_view()


class GetFavoriteView(ListAPIView):
    """
    This view return all Favorite-list
    """
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        queryset = Note.objects.filter(user=user, favorite=True)
        return queryset


favorite_note_list_view = GetFavoriteView.as_view()
