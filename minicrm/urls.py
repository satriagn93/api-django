import django.views.defaults
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url('', admin.site.urls),
]
