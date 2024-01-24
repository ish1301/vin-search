from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer


class VehicleList(ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    @extend_schema(
        operation_id="List vehicles",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class VehicleView(APIView):
    @extend_schema(
        operation_id="Get vehicle",
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


class VehicleSearch(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="year",
                description="Year of Vehicle",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="make",
                description="Make of Vehicle",
                required=True,
                type=str,
            ),
            OpenApiParameter(
                name="model",
                description="Model of Vehicle",
                required=True,
                type=str,
            ),
            OpenApiParameter(
                name="mileage",
                description="Mileage of Vehicle",
                required=False,
                type=str,
            ),
        ],
        responses={200: VehicleSerializer},
    )
    def post(self, request):
        vehicle = Vehicle.objects.first()
        serializer = VehicleSerializer(vehicle)

        if vehicle:
            return Response(
                serializer.data,
                status=HTTP_200_OK,
            )
        else:
            return Response("Not found", status=HTTP_404_NOT_FOUND)
