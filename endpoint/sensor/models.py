from djongo import models

from endpoint.sensor_type.models import SensorType


class Sensor(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    types = models.JSONField(null=False)
    _model = models.CharField(max_length=255)
