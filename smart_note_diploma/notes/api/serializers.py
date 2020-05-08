from rest_framework import serializers
from smart_note_diploma.notes.models import Note, NoteBooks, Favorite


class CreateNoteSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = Note
        fields = ('id', 'name', 'color',)


class NoteSerializer(serializers.ModelSerializer):
    """
    This serializer return list of Note
    use it to return Note-list
    """
    class Meta:
        model = Note
        fields = ('id', 'name', 'modified', )


class NoteBookSerializer(serializers.ModelSerializer):
    """
    This Serializer return properties of Notebook
    use it to return Notebooks-list
    """
    number_of_notes = serializers.SerializerMethodField('get_count_of_notes')

    class Meta:
        model = NoteBooks
        fields = ('id', 'name', 'number_of_notes', 'created', )

    def get_count_of_notes(self, obj):
        """ This function counts how many notes """
        return obj.notes.all().count()


class FavoriteSerializer(serializers.ModelSerializer):
    note = NoteSerializer(read_only=True)

    class Meta:
        model = Favorite
        fields = ('note', )
