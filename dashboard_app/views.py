from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "dashboard_app/home.html")


from rest_framework import generics
from .models import DashboardData
from .serializers import DashboardDataSerializer

class DashboardDataList(generics.ListCreateAPIView):
    queryset = DashboardData.objects.all()
    serializer_class = DashboardDataSerializer
  
  
  
  
  
    
from django.http import JsonResponse
from .models import DashboardData

def get_dashboard_data(request):
    data = DashboardData.objects.all().values()
    return JsonResponse(list(data), safe=False)