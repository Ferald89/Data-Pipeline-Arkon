"""Location model admin."""

# Django
from django.contrib import admin

# Models
from metro.location.models import Township, Unit

class TownshipAdmin(admin.ModelAdmin):
    """Township model admin."""
    list_display = ('id', 'name')

class UnitAdmin(admin.ModelAdmin):
    """Unit model admin."""
    list_display = ('id', 'latitude', 'longitude', 'township')

admin.site.register(Township, TownshipAdmin)
admin.site.register(Unit, UnitAdmin)