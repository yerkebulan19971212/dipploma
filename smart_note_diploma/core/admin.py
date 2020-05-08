from django.contrib import admin
from .models import Country, HashTag


admin.site.register([Country, HashTag, ])
