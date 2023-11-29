from django.urls import path
from .views import get_dashboard_data

urlpatterns = [
    path('api/', get_dashboard_data, name='get_dashboard_data'),
]