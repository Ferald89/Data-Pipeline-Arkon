"""District Models."""

# Django
from django.db import models

# Utiliate
from metro.utils.models import MetroModel

class District(MetroModel):
    """District Model."""
    name = models.CharField(max_length=60)

    def __str__(self):
        """return the name of District"""
        return self.name