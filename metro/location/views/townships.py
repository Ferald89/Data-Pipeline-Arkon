"""Townships view."""

# Django REST Framework
from rest_framework import mixins, viewsets

# Models
from metro.location.models import Township

# Serialier
from metro.location.serializers import TownshipsModelSerializer

class TownshipsViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    """Town view Set."""
    queryset = Township.objects.all()
    serializer_class = TownshipsModelSerializer
