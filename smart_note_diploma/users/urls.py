from django.urls import path

from smart_note_diploma.users.views import (
    user_redirect_view,
    user_update_view,
    user_detail_view,
)
from smart_note_diploma.users.api.views import CreateUserAPIView, authenticate_user

app_name = "users"
urlpatterns = [
    path("create/", CreateUserAPIView.as_view()),
    path("login/", authenticate_user),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
