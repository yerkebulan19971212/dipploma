from rest_framework import serializers
# from smart_note_diploma.users.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'created', 'password')

        extra_kwargs = {
            'password': {'write_only': True}
        }

