"""Districts view."""

# Django REST Framework
from rest_framework import mixins, viewsets

# Models
from metro.location.models import District

# Serialier
from metro.location.serializers import DistrictsModelSerializer

class DistrictsViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    """Town view Set."""
    queryset = District.objects.all()
    serializer_class = DistrictsModelSerializer
