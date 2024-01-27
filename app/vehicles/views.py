from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from vehicles.models import Vehicle
from vehicles.serializers import (
    VehicleReportSerializer,
    VehicleSearchSerializer,
    VehicleSerializer,
)


class VehicleList(ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    @extend_schema(
        operation_id="List Vehicles",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class VehicleView(APIView):
    @extend_schema(
        operation_id="Get Vehicle",
        responses={200: VehicleSerializer},
    )
    def get(self, request, vin):
        vehicle = Vehicle.objects.filter(vin=vin).first()
        serializer = VehicleSerializer(vehicle)

        if vehicle:
            return Response(
                serializer.data,
                status=HTTP_200_OK,
            )
        else:
            return Response("Not found", status=HTTP_404_NOT_FOUND)


class VehicleSearch(APIView, LimitOffsetPagination):
    @extend_schema(
        operation_id="Search Vehicle",
        request=VehicleSearchSerializer,
        responses={200: VehicleReportSerializer},
    )
    def post(self, request):
        serializer = VehicleSearchSerializer(data=request.data)
        if serializer.is_valid():
            year = request.data.get("year")
            make = request.data.get("make")
            model = request.data.get("model")
            mileage = request.data.get("mileage", None)
            vehicles = (
                Vehicle.objects.filter(year=year)
                .filter(make=make)
                .filter(model=model)[:100]
            )
            market_value = Vehicle.market_value(vehicles, mileage)

            serializer = VehicleReportSerializer(
                {"results": vehicles, "market_value": market_value}
            )

            return Response(
                serializer.data,
                status=HTTP_200_OK,
            )
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
