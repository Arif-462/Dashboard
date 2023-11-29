import json
from django.core.management.base import BaseCommand
from dashboard_app.models import DashboardData
import os

class Command(BaseCommand):
    help = 'Load data from jsondata.json into the database'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'jsondata.json')
        
        with open(file_path) as file:
            data = json.load(file)

        DashboardData.objects.bulk_create([
            DashboardData(**entry) for entry in data
        ])