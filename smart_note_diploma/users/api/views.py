# python library imports
import jwt

# rest_framework imports
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_jwt.utils import jwt_payload_handler

# django imports
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.signals import user_logged_in

#  local imports
from .serializers import CreateUserSerializer
from config.settings import local as settings

# get User model
User = get_user_model()


class CreateUser(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CreateUserSerializer


@api_view(['POST'])
@permission_classes((AllowAny, ))
def authenticate_user(request):
    try:
        email = request.data['email']
        password = request.data['password']
        print(email )
        #
        user = get_object_or_404(User, email=email)
        user.check_password(password)
        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)
                user_details = dict()
                user_details['token'] = token
                user_logged_in.send(sender=user.__class__,
                                    request=request, user=user)
                return Response(user_details, status=status.HTTP_200_OK)

            except Exception as e:
                raise e
        else:
            res = {
                'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {'error': password}
        return Response(res)
