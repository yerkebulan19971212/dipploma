# rest_framework imports
from rest_framework import serializers

# django imports
from django.contrib.auth import get_user_model

# get user model
User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    """
    This serializer returns and validates user data
    use it to create new User
    """

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = super(CreateUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializers(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', )
