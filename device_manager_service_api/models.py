from django.db import models


class Airplane(models.Model):
    """The Airplane model that Represents an airplane.
    """
    id = models.CharField(max_length=100, primary_key=True)


class Device(models.Model):
    """Represents an IOT device that is placed in an airplane.

    """
    id = models.CharField(max_length=100, primary_key=True,
                          unique=True)
    serial_number = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100)
    deleted = models.BooleanField(default=False)
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
