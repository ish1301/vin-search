from django.test import TestCase
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.test import APIClient


class ImageUploadViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.data_files = "app/tests/data/"

    def test_image_upload_valid(self):
        """
        Test the image upload view with a valid image.
        """
        file_path = f"{self.data_files}valid-image.jpg"
        with open(file_path, "rb") as image:
            response = self.client.post(
                reverse("analyze_image"),
                data={"image": image},
                format="multipart",
            )

        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_image_upload_invalid(self):
        """
        Test the image upload view with an invalid image.
        """
        invalid_image_path = f"{self.data_files}invalid-image.txt"
        with open(invalid_image_path, "rb") as invalid_image_file:
            response = self.client.post(
                reverse("analyze_image"),
                data={"image": invalid_image_file},
                format="multipart",
            )

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertIn(
            "Not An Image Or A Corrupted Image",
            response.data["image"][0].title(),
        )

    def test_image_upload_invalid_size(self):
        """
        Test the image upload view with an over size image.
        """
        invalid_image_path = f"{self.data_files}image_5mb.jpg"
        with open(invalid_image_path, "rb") as invalid_image_file:
            response = self.client.post(
                reverse("analyze_image"),
                data={"image": invalid_image_file},
                format="multipart",
            )

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertIn(
            "File Size Exceeds The Allowed Limit",
            response.data["image"][0].title(),
        )

    def test_image_upload_with_no_files(self):
        """
        Test the image upload view with empty request.
        """
        response = self.client.post(
            reverse("analyze_image"),
            format="multipart",
        )

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertIn(
            "No File Was Submitted",
            response.data["image"][0].title(),
        )
