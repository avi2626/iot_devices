
from django.contrib import admin
from django.urls import path
from device_manager_service_api.views import DeviceList, DeviceHandler

urlpatterns = [
    path('devices', DeviceList.as_view()),
    path('devices/<str:pk>', DeviceHandler.as_view()),
]
