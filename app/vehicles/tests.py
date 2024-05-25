from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer


class VehicleListTests(APITestCase):
    def setUp(self):
        self.vehicle1 = Vehicle.objects.create(
            vin="1HGCM82633A123456", year=2020, make="Honda", model="Accord", listing_price=20000, listing_mileage=15000
        )
        self.vehicle2 = Vehicle.objects.create(
            vin="1HGCM82633A654321", year=2019, make="Toyota", model="Camry", listing_price=18000, listing_mileage=20000
        )

    def test_list_vehicles(self):
        url = reverse("vehicle_list")
        response = self.client.get(url)
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"], serializer.data)


class VehicleViewTests(APITestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(
            vin="1HGCM82633A123456", year=2020, make="Honda", model="Accord", listing_price=20000, listing_mileage=15000
        )

    def test_get_vehicle(self):
        url = reverse("vehicle_get", kwargs={"vin": self.vehicle.vin})
        response = self.client.get(url)
        serializer = VehicleSerializer(self.vehicle)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_vehicle_not_found(self):
        url = reverse("vehicle_get", kwargs={"vin": "INVALIDVIN"})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, "Not found")


class VehicleSearchTests(APITestCase):
    def setUp(self):
        self.vehicle1 = Vehicle.objects.create(
            vin="1HGCM82633A123456", year=2020, make="Honda", model="Accord", listing_price=20000, listing_mileage=15000
        )
        self.vehicle2 = Vehicle.objects.create(
            vin="1HGCM82633A654321", year=2020, make="Honda", model="Accord", listing_price=21000, listing_mileage=14000
        )
        self.vehicle3 = Vehicle.objects.create(
            vin="1HGCM82633A111111", year=2019, make="Toyota", model="Camry", listing_price=18000, listing_mileage=20000
        )

    def test_search_vehicle(self):
        url = reverse("vehicle_search")
        data = {"year": 2020, "make": "Honda", "model": "Accord"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)
        self.assertIn("market_value", response.data)
        self.assertEqual(len(response.data["results"]), 2)

    def test_search_vehicle_with_mileage(self):
        url = reverse("vehicle_search")
        data = {
            "year": 2020,
            "make": "Honda",
            "model": "Accord",
            "mileage": "25000",
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["market_value"], "$10,000")
        self.assertEqual(len(response.data["results"]), 2)

    def test_search_vehicle_invalid(self):
        url = reverse("vehicle_search")
        data = {"year": "INVALID_YEAR", "make": "Honda", "model": "Accord"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
