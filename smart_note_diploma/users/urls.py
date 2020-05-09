from rest_framework_simplejwt import views as jwt_views

# django imports
from django.urls import path

# local imports
from smart_note_diploma.users.api.views import (
    create_user_view, get_me, edit_profile_view,
)
app_name = "users"
urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path("create/", create_user_view, name="create_user"),
    path('me/', get_me),
    path("<int:pk>/edit/", edit_profile_view)
]
