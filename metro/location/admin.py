"""Location model admin."""

# Django
from django.contrib import admin

# Models
from metro.location.models import District, Unit

class DistrictAdmin(admin.ModelAdmin):
    """District model admin."""
    list_display = ('id', 'name')

class UnitAdmin(admin.ModelAdmin):
    """Unit model admin."""
    list_display = ('id', 'latitude', 'longitude', 'district')

admin.site.register(District, DistrictAdmin)
admin.site.register(Unit, UnitAdmin)