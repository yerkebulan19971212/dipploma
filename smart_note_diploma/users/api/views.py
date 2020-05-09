# rest_framework imports
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# django imports
from django.contrib.auth import get_user_model

#  local imports
from .serializers import CreateUserSerializer, UserSerializers

# get User model
User = get_user_model()


class CreateUserView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = CreateUserSerializer


create_user_view = CreateUserView.as_view()


class GetUserView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = request.user
        me_serializer = UserSerializers([user], many=True)
        return Response(me_serializer.data, status=status.HTTP_200_OK)


get_me = GetUserView.as_view()


class MeUpdateView(UpdateAPIView):
    serializer_class = UserSerializers
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()


edit_profile_view = MeUpdateView.as_view()
