from drf_spectacular.utils import extend_schema
from image_analysis.models import ImageUpload
from image_analysis.serializers import ImageAnalysisSerializer, ImageUploadSerializer
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.views import APIView


class ImageUploadView(APIView):
    parser_classes = [
        MultiPartParser,
    ]

    @extend_schema(
        operation_id="POST image for analysis",
        request=ImageUploadSerializer,
        responses={200: ImageUploadSerializer, 400: ValidationError},
    )
    def post(self, request):
        serializer = ImageUploadSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ImageAnalysisView(APIView):
    @extend_schema(
        operation_id="GET image analysis",
        responses={200: ImageAnalysisSerializer, 404: FileNotFoundError},
    )
    def get(self, request, md5_hash):
        image = ImageUpload.objects.filter(md5_hash=md5_hash).first()
        serializer = ImageAnalysisSerializer(image)

        if image:
            return Response(
                serializer.data,
                status=HTTP_200_OK,
            )
        else:
            return Response("Not found", status=HTTP_404_NOT_FOUND)
