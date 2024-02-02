from django.contrib import admin

from app.vehicles.models import Vehicle, VehicleAdmin

admin.site.register(Vehicle, VehicleAdmin)
