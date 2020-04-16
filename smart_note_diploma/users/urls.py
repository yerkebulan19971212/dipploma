# django imports
from django.urls import path

# local imports
from smart_note_diploma.users.api.views import CreateUser, authenticate_user

app_name = "users"
urlpatterns = [
    path("create/", CreateUser.as_view()),
    path("login/", authenticate_user)
]
