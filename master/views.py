from master.models import *
from rest_framework import viewsets
from .serializers import * 

class TypeAccountViewSet(viewsets.ModelViewSet):
	queryset =  TypeAccount.objects.all()
	serializer_class = TypeAccountSerializer