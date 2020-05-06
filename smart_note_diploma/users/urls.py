from rest_framework_simplejwt import views as jwt_views

# django imports
from django.urls import path

# local imports
from smart_note_diploma.users.api.views import CreateUser, authenticate_user

app_name = "users"
urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path("create/", CreateUser.as_view(), name="create_user"),
    # path("login/", authenticate_user, name="authenticate_user"),
]
