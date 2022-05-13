"""Township Models."""

# Django
from django.db import models

# Utiliate
from metro.utils.models import MetroModel

class Township(MetroModel):
    """Township Model."""
    name = models.CharField(max_length=60)

    def __str__(self):
        """return the name of Township"""
        return self.name