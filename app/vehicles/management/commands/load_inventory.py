import csv

from django.core.management.base import BaseCommand, CommandError
from vehicles.models import Vehicle

csv.register_dialect("piper", delimiter="|", quoting=csv.QUOTE_NONE)


class Command(BaseCommand):
    help = "Load the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("file", nargs="+", type=str)

    def handle(self, *args, **options):
        for file_path in options["file"]:
            with open(file_path) as csvfile:
                for row in csv.DictReader(csvfile, dialect="piper"):
                    print(row)
                    exit()
