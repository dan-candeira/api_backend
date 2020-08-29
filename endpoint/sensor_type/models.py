from djongo import models


class SensorType(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    mesuaring_dimentions = models.JSONField(
        blank=False, null=False, default=[])
