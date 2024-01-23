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


{
    "vin": "3C6TRVAG4LE105493",
    "year": "2020",
    "make": "Ram",
    "model": "ProMaster Cargo Van",
    "trim": "1500 Low Roof",
    "dealer_name": "Cars For Sale  One Stop Auto Mall",
    "dealer_street": "22028 N 19th Ave",
    "dealer_city": "Phoenix",
    "dealer_state": "AZ",
    "dealer_zip": "85027",
    "listing_price": "35500",
    "listing_mileage": "63323",
    "used": True,
    "certified": False,
    "style": '1500 Low Roof 3dr Van w/136\\" WB (3.6L 6cyl 6A)',
    "driven_wheels": "front wheel drive",
    "engine": "gas",
    "fuel_type": "Gasoline",
    "exterior_color": "Bright White Clear Coat",
    "interior_color": "Black Vinyl",
    "seller_website": "https://www.1stopautomall.com",
    "first_seen_date": "2022-03-19",
    "last_seen_date": "2022-08-17",
    "dealer_vdp_last_seen_date": "2022-08-17",
    "listing_status": "",
}
