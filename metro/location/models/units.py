"""Township Models."""

# Django
from django.db import models

# Utiliate
from metro.utils.models import MetroModel

class Unit(MetroModel):
    """Unit Model."""
    id = models.IntegerField(primary_key=True)

    # Position
    latitude = models.FloatField()
    longitude  = models.FloatField()

    # Township use a Foreign Key from township model
    township = models.ForeignKey('location.Township', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """Return the id"""
        return self.id