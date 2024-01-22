from django.db import models

MAX_IMAGE_SIZE = 4 * 1024 * 1024  # 4MB, Max file size for Google VISION API


class ImageUpload(models.Model):
    filename = models.CharField(max_length=255, null=True)
    md5_hash = models.CharField(max_length=32, null=True)
    analysis = models.TextField(null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
