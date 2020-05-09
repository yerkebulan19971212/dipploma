from rest_framework import serializers
from ..models import HashTag, Country


class HashTagsSerializers(serializers.ModelSerializer):

    class Meta:
        model = HashTag
        fields = ('title', )


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'
