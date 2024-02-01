import statistics

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

    @property
    def name(self):
        return f"{self.year} {self.make} {self.model}"

    @property
    def location(self):
        return f"{self.dealer_city}, {self.dealer_state}"

    @property
    def price(self):
        return f"${int(self.listing_price):,}" if len(self.listing_price) > 0 else "-"

    @property
    def mileage(self):
        return (
            f"{int(self.listing_mileage):,}" if len(self.listing_mileage) > 0 else "-"
        )

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
    def market_value(self, vehicles, mileage):
        if mileage is None or len(mileage) == 0 or len(vehicles) == 0:
            return None

        # Filter out data with missing price or mileage
        car_inventory = [
            (int(i.listing_mileage), int(i.listing_price))
            for i in vehicles
            if len(i.listing_price) > 0 and len(i.listing_mileage) > 0
        ]

        # Sort the car inventory based on mileage asc order
        car_inventory = sorted(car_inventory, key=lambda item: item[0])

        # Initial price at mileage
        initial_price = sum(i[1] for i in car_inventory[:10]) / len(car_inventory[:10])
        initial_mileage = sum(i[0] for i in car_inventory[:10]) / len(
            car_inventory[:10]
        )

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

        depreciation = depreciation_rate(car_inventory)

        market_price = max(
            0, initial_price + ((int(mileage) - initial_mileage) * depreciation)
        )

        # Round to nearest hundered
        return f"${round(int(market_price / 100) * 100):,}"
