from django.db import models


class Vehicle(models.Model):
    vin = models.CharField(max_length=17)
    year = models.CharField(max_length=4)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    trim = models.CharField(max_length=255)
    dealer_name = models.CharField(max_length=255)
    dealer_street = models.CharField(max_length=255)
    dealer_city = models.CharField(max_length=255)
    dealer_state = models.CharField(max_length=255)
    dealer_zip = models.CharField(max_length=10)
    listing_price = models.CharField(max_length=255)
    listing_mileage = models.CharField(max_length=50)
    used = models.BooleanField(default=True)
    certified = models.BooleanField(default=False)
    style = models.CharField(max_length=255)
    driven_wheels = models.CharField(max_length=255)
    engine = models.CharField(max_length=255)
    fuel_type = models.CharField(max_length=255)
    exterior_color = models.CharField(max_length=255)
    interior_color = models.CharField(max_length=255)
    seller_website = models.CharField(max_length=255)
    first_seen_date = models.CharField(max_length=255)
    last_seen_date = models.DateField(null=True)
    first_seen_date = models.DateField(null=True)
    dealer_vdp_last_seen_date = models.DateField(null=True, blank=True)
    listing_status = models.CharField(max_length=50)

    class Meta:
        indexes = [
            models.Index(fields=["vin"], name="vin_idx"),
            models.Index(fields=["year"], name="year_idx"),
            models.Index(fields=["make"], name="make_idx"),
            models.Index(fields=["model"], name="model_idx"),
        ]

    def calc_price(self, year, make, model):
        return 13100
