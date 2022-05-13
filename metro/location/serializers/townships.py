"""Townships Serializer"""

# Django REST Frameworks
from rest_framework import serializers

# Model
from metro.location.models import Township

class TownshipsModelSerializer(serializers.ModelSerializer):
    """Townships Model Serializer."""

    class Meta:
        """Meta class"""
        model = Township
        fields = '__all__'
