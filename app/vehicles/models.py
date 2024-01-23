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
    dealer_zip = models.CharField(max_length=5)
    listing_price = models.CharField(max_length=255)
    listing_mileage = models.CharField(max_length=50)
    used = models.BooleanField(default=True)
    certified = models.BooleanField(default=False)
    style = models.CharField(max_length=255)
    driven_wheels = models.CharField(max_length=20)
    engine = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)
    exterior_color = models.CharField(max_length=50)
    interior_color = models.CharField(max_length=50)
    seller_website = models.CharField(max_length=255)
    first_seen_date = models.CharField(max_length=255)
    last_seen_date = models.DateField(null=True)
    first_seen_date = models.DateField(null=True)
    dealer_vdp_last_seen_date = models.DateField(null=True)
    listing_status = models.CharField(max_length=50)


# Sample Object
# {
#     "vin": "KNAFK4A61F5428652",
#     "year": "2015",
#     "make": "Kia",
#     "model": "FORTE",
#     "trim": "LX",
#     "dealer_name": "X Nation Auto Group",
#     "dealer_street": "6003 Bandera Rd",
#     "dealer_city": "San Antonio",
#     "dealer_state": "TX",
#     "dealer_zip": "78238",
#     "listing_price": "",
#     "listing_mileage": "53960",
#     "used": "TRUE",
#     "certified": "FALSE",
#     "style": "4D Sedan",
#     "driven_wheels": "FWD",
#     "engine": "1.8L",
#     "fuel_type": "",
#     "exterior_color": "Silver",
#     "interior_color": "Gray",
#     "seller_website": "https://xnationautogroup.com",
#     "first_seen_date": "2021-11-24",
#     "last_seen_date": "2022-08-17",
#     "dealer_vdp_last_seen_date": "2022-08-17",
#     "listing_status": "",
# }
