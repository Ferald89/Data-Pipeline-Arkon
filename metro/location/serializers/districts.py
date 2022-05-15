"""Districts Serializer"""

# Django REST Frameworks
from rest_framework import serializers

# Model
from metro.location.models import District

class DistrictsModelSerializer(serializers.ModelSerializer):
    """Districts Model Serializer."""

    class Meta:
        """Meta class"""
        model = District
        fields = '__all__'
