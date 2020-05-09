# rest framework import
from rest_framework.generics import ListAPIView

# local import
from .serializers import CountrySerializer
from ..models import Country


class AllCountryView(ListAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


get_all_countries_view = AllCountryView.as_view()
