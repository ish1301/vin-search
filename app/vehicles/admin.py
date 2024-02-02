from django.contrib import admin
from vehicles.models import Vehicle, VehicleAdmin

admin.site.register(Vehicle, VehicleAdmin)
