import statistics

from django.contrib import admin
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
    listing_price = models.IntegerField(blank=True, null=True, default=None)
    listing_mileage = models.IntegerField(blank=True, null=True, default=None)
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

    @property
    def name(self):
        return f"{self.year} {self.make} {self.model}"

    @property
    def location(self):
        return f"{self.dealer_city}, {self.dealer_state}"

    @property
    def price(self):
        return f"${int(self.listing_price):,}" if self.listing_price > 0 else "-"

    @property
    def mileage(self):
        return f"{int(self.listing_mileage):,}" if self.listing_mileage > 0 else "-"

    class Meta:
        indexes = [
            models.Index(fields=["vin"], name="vin_idx"),
            models.Index(fields=["year"], name="year_idx"),
            models.Index(fields=["make"], name="make_idx"),
            models.Index(fields=["model"], name="model_idx"),
        ]

    def __str__(self):
        return self.name

    """
    Evaluate market value based on close matches to mileage
    """

    @classmethod
    def market_value(self, year, make, model, mileage):
        # When comparing closet mileage, use 20% delta
        mileage_delta = 0.2

        # Limit vehicles data in response
        limit_vehicles = 100

        def round_by_100(price):
            return f"${round(int(price / 100) * 100):,}" if price > 0 else ""

        def depreciation_rate(vehicles):
            # Initialize variables to track changes in mileage and price
            total_mileage_change = 0
            total_price_change = 0

            # Calculate the total change in mileage and price between consecutive data points
            for i in range(1, len(vehicles)):
                mileage_prev, price_prev = vehicles[i - 1]
                mileage_curr, price_curr = vehicles[i]
                mileage_change = mileage_curr - mileage_prev
                price_change = price_curr - price_prev
                total_mileage_change += mileage_change
                total_price_change += price_change

            # Calculate the rate of depreciation
            depreciation_rate = total_price_change / total_mileage_change
            return depreciation_rate

        vehicles = (
            Vehicle.objects.exclude(listing_price=None)
            .exclude(listing_mileage=None)
            .filter(year=year)
            .filter(make=make)
            .filter(model=model)
        )

        # Filter out data which is too far from the dataset
        if mileage:
            mileage = int(mileage)
            vehicles = vehicles.filter(listing_mileage__gte=mileage * (1 - mileage_delta)).filter(
                listing_mileage__lte=mileage * (1 + mileage_delta)
            )

        # No matching vehicles
        if len(vehicles) == 0:
            return [], ""

        # Filter out data with missing price or mileage
        car_inventory = [
            (int(i.listing_mileage), int(i.listing_price))
            for i in vehicles
            if i.listing_price > 0 and i.listing_mileage > 0
        ]

        # Sort the car inventory based on mileage asc order
        car_inventory = sorted(car_inventory, key=lambda item: item[0])

        # Initial price at mileage
        median_price = statistics.median([i[1] for i in car_inventory])
        median_mileage = statistics.median([i[0] for i in car_inventory])

        # If mileage is unknown return median
        if mileage is None or mileage == 0:
            return vehicles[:limit_vehicles], round_by_100(median_price)

        depreciation = depreciation_rate(car_inventory)
        market_price = max(0, median_price + ((int(mileage) - median_mileage) * depreciation))

        return vehicles[:limit_vehicles], round_by_100(market_price)


class VehicleAdmin(admin.ModelAdmin):
    list_display = ["id", "year", "make", "model", "listing_price", "listing_mileage"]
