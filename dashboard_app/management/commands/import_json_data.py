import json
from django.core.management.base import BaseCommand
from dashboard_app.models import DashboardData

class Command(BaseCommand):
    help = 'Import data from JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        json_file_path = kwargs['json_file']
        with open(json_file_path) as f:
            data = json.load(f)

        for item in data:
            DashboardData.objects.create(**item)

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))