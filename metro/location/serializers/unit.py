"""Units Serializer"""

# Django REST Frameworks
from rest_framework import serializers

# Model
from metro.location.models import Unit

# Serializer
from metro.location.serializers import DistrictsModelSerializer

# GraphQL
from django_restql.mixins import DynamicFieldsMixin

class UnitModelSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    """Units Model Serializer."""

    district = DistrictsModelSerializer(read_only=True)

    class Meta:
        """Meta class"""
        model = Unit
        fields = '__all__'
