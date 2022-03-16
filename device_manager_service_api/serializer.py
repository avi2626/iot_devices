from rest_framework import serializers
from device_manager_service_api.models import Device
from rest_framework.decorators import api_view


class DeviceSerializer(serializers.ModelSerializer):
    """_summary_ Serializer for the Device model


    """
    class Meta:
        model = Device
        exclude = ['deleted']
