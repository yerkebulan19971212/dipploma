from rest_framework import serializers
from smart_note_diploma.notes.models import Note, NoteBooks, Favorite


class NoteSeriallizer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('name', )


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

    class Meta:
        model = Favorite
        fields = ('note', )
