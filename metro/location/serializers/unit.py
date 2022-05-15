"""Units Serializer"""

# Django REST Frameworks
from rest_framework import serializers

# Model
from metro.location.models import Unit

class UnitModelSerializer(serializers.ModelSerializer):
    """Units Model Serializer."""

    class Meta:
        """Meta class"""
        model = Unit
        fields = '__all__'
