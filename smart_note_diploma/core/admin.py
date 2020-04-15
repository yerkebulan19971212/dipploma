from django.contrib import admin
from .models import Country, Hashtag


admin.site.register([Country, Hashtag, ])
