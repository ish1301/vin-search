from django.urls import path
from image_analysis.views import ImageAnalysisView, ImageUploadView

urlpatterns = [
    path("analyze-image/", ImageUploadView.as_view(), name="analyze_image"),
    path(
        "analyze-image/<md5_hash>/",
        ImageAnalysisView.as_view(),
        name="analyze_image_get",
    ),
]
