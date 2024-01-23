from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer


class VehicleList(APIView):
    @extend_schema(
        operation_id="List vehicles",
        responses={200: VehicleSerializer},
    )
    def get(self, request):
        queryset = Vehicle.objects.all()
        serializer = VehicleSerializer(queryset, many=True)
        return Response(serializer.data)


class VehicleView(APIView):
    @extend_schema(
        operation_id="Get vehicle",
        responses={200: VehicleSerializer, 404: FileNotFoundError},
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
