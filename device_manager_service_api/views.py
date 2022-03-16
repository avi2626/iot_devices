from rest_framework.views import APIView
from device_manager_service_api.models import Device, Airplane
from rest_framework.response import Response
from device_manager_service_api.serializer import DeviceSerializer
from rest_framework import status


def validate_airplane_id(request):
    """Checks if the airplane id is a valid airplane id in the airplanes collection

    Args:
        request : the incoming request

    Returns:
         A boolean that indicates if the airplane id is valid.
    """
    airplane_id = request.data.get('airplane')
    return Airplane.objects.filter(id=airplane_id).exists()


def validate_unique_fields(request):
    """Checks if the unique fields in the device record are unique

    Args:
        request : the incoming http data dictionary


    Returns:
        A boolean that indicates if the request is not introducing duplicate objects.
    """
    device_serial_number = request.data.get('serial_number')
    device_id = request.data.get('id')
    serial_exists_on_other = Device.objects.filter(
        serial_number=device_serial_number, deleted=False).exclude(id=device_id).exists()
    id_number_exists = Device.objects.filter(
        id=device_id, deleted=False).exists()
    serial_exists = Device.objects.filter(
        serial_number=device_serial_number, deleted=False).exists()

    if(request.method == 'PATCH'):
        if(device_serial_number and serial_exists_on_other):
            return False
        return True
    if(id_number_exists or serial_exists):
        return False
    return True


def record_exists_and_not_deleted(pk):
    """Function that checks that a record exists and is not marked as deleted.

    Args:
        request: the incoming data request.

    Returns:
        Boolean indicating if the record is exists and not marked as deleted.
    """
    return Device.objects.filter(id=pk, deleted=False).exists()


def record_exists(pk):
    """Function that checks that a record exist even if deleted.

    Args:
        pk: the primary key from the incoming request.

    Returns:
        Boolean indicating if the record is exists even if deleted.
    """
    return Device.objects.filter(id=pk).exists()


class DeviceList(APIView):
    """APIView for listing and creating IOT devices."""

    def get(self, request):
        """List IOT devices."""
        devices = Device.objects.all().filter(deleted=False)
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Create an IOT devices if it does not already exist."""
        if not validate_airplane_id(request):
            return Response('airplane id not found',
                            status=status.HTTP_400_BAD_REQUEST)
        if not validate_unique_fields(request):
            return Response('id and serial_number needs to be unique',
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceHandler(APIView):
    """APIView for retrieving, updating and deleting IOT devices."""

    def get(self, request, pk):
        if not record_exists_and_not_deleted(pk):
            return Response(status=status.HTTP_404_NOT_FOUND)
        device = Device.objects.get(pk=pk)
        serializer = DeviceSerializer(device)
        return Response(serializer.data)

    def patch(self, request, pk):
        """Updating a fields of a device."""
        if not (record_exists_and_not_deleted(pk)):
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.data.get('airplane'):
            if not (validate_airplane_id(request)):
                return Response('airplane_id not found',
                                status=status.HTTP_400_BAD_REQUEST)
        if not validate_unique_fields(request):
            return Response('id and serial_number needs to be unique',
                            status=status.HTTP_400_BAD_REQUEST)
        device = Device.objects.get(pk=pk)
        serializer = DeviceSerializer(
            device, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return serializer.errors

    def delete(self, request, pk):
        """Marking a device as deleted."""
        if not (record_exists(pk)):
            return Response(status=status.HTTP_404_NOT_FOUND)
        if(record_exists_and_not_deleted(pk)):
            device = Device.objects.get(pk=pk)
            device.deleted = True
            device.save()
        return Response('Success', status=status.HTTP_200_OK)
