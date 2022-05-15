"""Units View."""

# Django REST Framework
from rest_framework import mixins, viewsets

# Models
from metro.location.models import Unit

# Serialier
from metro.location.serializers import UnitModelSerializer

class UnitViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    """Unit View Set."""
    queryset = Unit.objects.all()
    serializer_class = UnitModelSerializer
