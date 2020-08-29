from djongo import models

from endpoint.sensor_type.models import SensorType


class Sensor(models.Model):
    _id = models.AutoField(primary_key=True)
    types = models.ArrayReferenceField(
        to=SensorType, to_field='_id', null=False)
    model = models.CharField(max_length=255)
