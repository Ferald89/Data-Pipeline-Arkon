"""Celery django"""

# Celery
import imp
from celery.decorators import task, periodic_task

# Utils
from datetime import timedelta

# Models
from metro.location.models import Unit
