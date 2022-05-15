"""Location URLs."""

# Django
from django.db import router
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# View
from .views import townships as townships_view
from .views import units as units_view

router = DefaultRouter()
router.register(r'township', townships_view.TownshipsViewSet, basename='township')
router.register(r'unit', units_view.UnitViewSet, basename='unit')

urlpatterns = [
    path('', include(router.urls))
]
