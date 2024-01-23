import csv

from django.core.management.base import BaseCommand, CommandError
from vehicles.models import Vehicle

csv.register_dialect("piper", delimiter="|", quoting=csv.QUOTE_NONE)


class Command(BaseCommand):
    help = "Load the inventory data in vehicles"

    def add_arguments(self, parser):
        parser.add_argument("file", nargs="+", type=str)

    """
    Handle loading inventory data into relational database
    """

    def handle(self, *args, **options):
        for file_path in options["file"]:
            with open(file_path) as csvfile:
                # Batch create for faster procesing of data
                i = 1
                batch = []
                batch_size = 10000

                for row in csv.DictReader(csvfile, dialect="piper"):
                    # Sanitize data
                    row["used"] = True if row["used"] == "TRUE" else False
                    row["certified"] = True if row["certified"] == "TRUE" else False
                    if row["dealer_vdp_last_seen_date"] == "":
                        row["dealer_vdp_last_seen_date"] = None

                    batch.append(Vehicle(**row))

                    try:
                        if i % batch_size == 0:
                            Vehicle.objects.bulk_create(batch)
                            batch = []
                            print(f"{i} records created")
                    except Exception as e:
                        print(Exception, e)
                        print(f"{i} Failed with validation {e}")
                        exit()
                    i += 1

                if len(batch) > 0:
                    Vehicle.objects.bulk_create(batch)
                    print(f"{i} last batch created")
