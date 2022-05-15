"""Location URLs."""

# Django
from django.db import router
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# View
from .views import districts as districts_view
from .views import units as units_view

router = DefaultRouter()
router.register(r'district', districts_view.DistrictsViewSet, basename='district')
router.register(r'unit', units_view.UnitViewSet, basename='unit')

urlpatterns = [
    path('', include(router.urls))
]
