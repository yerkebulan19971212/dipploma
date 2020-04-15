# rest_framework imports
from rest_framework import serializers

# django imports
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')

        extra_kwargs = {
            'password': {'write_only': True}
        }

