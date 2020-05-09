from rest_framework import serializers
from ..models import HashTag


class HashTagsSerializers(serializers.ModelSerializer):

    class Meta:
        model = HashTag
        fields = ('title', )
