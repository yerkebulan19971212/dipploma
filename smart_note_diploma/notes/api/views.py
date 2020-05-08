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
    CreateImage, CreateNoteBookSerializer, FavoriteNoteSerializer
)
from smart_note_diploma.notes.models import (
    Note, NoteBooks,
    Text, CheckBox, Image
)
from smart_note_diploma.core.models import (HashTag)


class CreateNoteAPIView(APIView):
    # parser_classes = (FileUploadParser, )
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
                    serializer = CreateImage(data=value)
                    if serializer.is_valid():
                        return Response({"SSS": "SS"}, status.HTTP_201_CREATED)
                    return Response({"11111": "SS"}, status.HTTP_201_CREATED)

                    # serializer.save(note=note)
                    # iamge = Image.objects.create(
                    #     note=note,
                    #     path=value.get('image')
                    # )
                    # iamge.save()
        return Response(note_serilizer.data, status.HTTP_201_CREATED)


create_note_view = CreateNoteAPIView.as_view()


class GetNoteView(RetrieveAPIView):
    pass
    # serializer_class =
    # def get(self, request, pk):
    #     note = get_object_or_404(Note, pk=pk)
    #     check_box = CheckBox.objects.filter()


get_note_page_view = GetNoteView.as_view()


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
    serializer_class = CreateNoteBookSerializer
    permission_classes = (IsAuthenticated, )


create_note_book_view = CreateNoteBookView.as_view()


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


class AddToFavoriteView(UpdateAPIView):
    serializer_class = FavoriteNoteSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Note.objects.all()

    def perform_update(self, serializer):
        pk = self.kwargs['pk']
        queryset = Note.objects.filter(pk=pk)
        queryset.update(favorite=True)
        serializer.save()


add_to_favorite_view = AddToFavoriteView.as_view()


class GetFavoriteView(ListAPIView):
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        queryset = Note.objects.filter(user=user, favorite=True)
        return queryset


favorite_note_list_view = GetFavoriteView.as_view()
