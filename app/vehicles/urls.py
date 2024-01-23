from django.urls import path
from vehicles.views import VehicleList, VehicleView

urlpatterns = [
    path("list/", VehicleList.as_view(), name="vehicle_list"),
    path(
        "view/<str:vin>",
        VehicleView.as_view(),
        name="vehicle_get",
    ),
]
