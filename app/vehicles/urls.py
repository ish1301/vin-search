from django.urls import path
from vehicles.views import VehicleList, VehicleView

urlpatterns = [
    path("/", VehicleList.as_view(), name="vehicle_list"),
    path(
        "<vin>/",
        VehicleView.as_view(),
        name="vehicle_get",
    ),
]
