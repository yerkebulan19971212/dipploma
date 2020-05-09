from rest_framework import serializers
from smart_note_diploma.notes.models import Note, NoteBooks, Image, Text, CheckBox
from smart_note_diploma.core.api.serializers import HashTagsSerializers


class CreateNoteSerializer(serializers.ModelSerializer):
    """ This serializer Create a new Note   """
    class Meta:
        model = Note
        fields = ('id', 'name',)


class GetImageSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField('get_type')

    class Meta:
        model = Image
        fields = ('path', 'order', 'type', )

    def get_type(self, obj):
        return 2


class TextSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField('get_type')

    class Meta:
        model = Text
        fields = ('text', 'order', 'type', )

    def get_type(self, obj):
        return 0


class CheckBoxSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField('get_type')

    class Meta:
        model = CheckBox
        fields = ('text', 'is_done', 'order', 'type', )

    def get_type(self, obj):
        return 1


class GetNoteSerializer(serializers.ModelSerializer):
    """ This serializer Retrieve Note """
    hash_tags_list = serializers.SerializerMethodField('get_hash_tags')
    content = serializers.SerializerMethodField('get_content')

    class Meta:
        model = Note
        fields = ('id', 'name', 'favorite', 'color', 'hash_tags_list','content')

    def get_hash_tags(self, obj):
        serializer = HashTagsSerializers(obj.hash_tags, read_only=True, many=True)
        hash_tags = [i['title'] for i in serializer.data]
        return hash_tags

    def get_image(self, obj):
        image = Image.objects.filter(note=obj)
        image_serialzier = GetImageSerializer(image, many=True)
        return image_serialzier.data

    def get_text(self, obj):
        text = Text.objects.filter(note=obj)
        text_serializer = TextSerializer(text, many=True)
        return text_serializer.data

    def get_check_box(self, obj):
        check_box = CheckBox.objects.filter(note=obj)
        check_box_serializer = CheckBoxSerializer(check_box, many=True)
        return check_box_serializer.data

    def get_content(self, obj):
        content_result = []

        images = self.get_image(obj)
        if images:
            content_result += images

        texts = self.get_text(obj)
        if texts:
            content_result += texts

        check_boxes = self.get_check_box(obj)
        if check_boxes:
            content_result += check_boxes

        return sorted(content_result, key=lambda i: int(i['order']))


class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class ImageSerializer(serializers.ModelSerializer):
    path = Base64ImageField(
        max_length=None, use_url=True,
    )

    class Meta:
        model = Image
        fields = ('path', )


class FavoriteNoteSerializer(serializers.ModelSerializer):
    """
    This serializer return list of Note
    use it to return Note-list
    """
    class Meta:
        model = Note
        fields = ('id', 'favorite', )


class NoteSerializer(serializers.ModelSerializer):
    """
    This serializer return list of Note
    use it to return Note-list
    """
    class Meta:
        model = Note
        fields = ('id', 'name', 'modified', )


class CreateNoteBookSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = NoteBooks
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
