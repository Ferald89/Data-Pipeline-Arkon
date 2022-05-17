"""Districts Serializer"""

# Django REST Frameworks
from rest_framework import serializers

# Model
from metro.location.models import District

# GraphQL
from django_restql.mixins import DynamicFieldsMixin

class DistrictsModelSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    """Districts Model Serializer."""

    class Meta:
        """Meta class"""
        model = District
        fields = '__all__'
