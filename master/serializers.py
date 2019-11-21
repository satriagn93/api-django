from master.models import *
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

class TypeAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = TypeAccount
		fields = '__all__'