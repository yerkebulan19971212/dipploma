from rest_framework import serializers
from smart_note_diploma.notes.models import Note, NoteBooks, Favorite


class NoteSeriallizer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('name', )


class NoteBookSeriallizer(serializers.ModelSerializer):
    notes = serializers.SerializerMethodField('get_count_of_notes')

    class Meta:
        model = NoteBooks
        fields = ('name', 'notes')

    def get_count_of_notes(self, obj):
        return obj.notes.all().count()


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = ('note', )
