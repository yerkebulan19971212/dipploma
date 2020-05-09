from django.urls import path
from .api.view import get_all_countries_view

app_name = "core"
urlpatterns = [
    path('all-countries', get_all_countries_view)
]
