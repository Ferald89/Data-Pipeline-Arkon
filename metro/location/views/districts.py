"""Districts view."""

# Django REST Framework
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from metro.location.models import District, Unit

# Serialier
from metro.location.serializers import DistrictsModelSerializer, UnitModelSerializer

class DistrictsViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    """Town view Set."""
    queryset = District.objects.all()
    serializer_class = DistrictsModelSerializer

    @action(detail=True, methods=['get'])
    def unit_list(self, request, *args, **kwargs):
        """Retrieve a list containing all 
        units availables into the district"""
        district = self.get_object()
        units = Unit.objects.filter(district=district)
        data = UnitModelSerializer(units, many=True).data
        return Response(data)
