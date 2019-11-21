from django.contrib import admin
from django.urls import path
import django.views.defaults
from django.conf.urls import include, url
from django.conf import settings
from django.urls import reverse
from django.contrib import admin
from django.contrib.auth.models import User, Group, Permission
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User

from master import views as master

from django.conf.urls.static import static

router = routers.DefaultRouter()

router.register(r'mastertypeaccount', master.TypeAccountViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include(router.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth-jwt/', obtain_jwt_token),
    url(r'^auth-jwt-refresh/', refresh_jwt_token),
    url(r'^auth-jwt-verify/', verify_jwt_token),
    url(r'^treewidget/', include('treewidget.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)