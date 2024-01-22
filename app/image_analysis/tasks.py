import json

from celery import shared_task
from decouple import config
from google.cloud import vision
from image_analysis.models import ImageUpload


@shared_task
def submit_image_analysis(filename, md5_hash, content):
    """
    Parameters:
        - filename (str): The name of the uploaded image file.
        - md5_hash (str): The MD5 hash of the image file.
        - content (str): The base64-encoded content of the image.

    Returns:
        - ImageUpload: The ImageUpload instance representing the analyzed image.
    """

    image = ImageUpload.objects.create(filename=filename, md5_hash=md5_hash)

    # Initialize the Google Cloud Vision API client
    client = vision.ImageAnnotatorClient(
        client_options={
            "api_key": config("GOOGLE_API_KEY"),
        }
    )

    # Define the request object for analysis
    request = {
        "image": {"content": content},
        "features": [{"type_": vision.Feature.Type.LABEL_DETECTION}],
    }

    # Automatic logs upon various failure types
    response = client.annotate_image(request)
    response_json = vision.AnnotateImageResponse.to_json(response)

    image.analysis = json.dumps(response_json)
    image.save()

    return image
