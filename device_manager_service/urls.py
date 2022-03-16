
from django.urls import path, include


urlpatterns = [
    path('', include('device_manager_service_api.urls')),
]
