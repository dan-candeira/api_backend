from djongo import models
from django.utils import timezone

from endpoint.equipment.models import Equipment


class Collect(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    timestamp_init = models.DateTimeField(editable=False)
    timestamp_fin = models.DateTimeField(editable=False)
    samples = models.JSONField(null=True, blank=True, default=[])
    equipment = models.ForeignKey(
        to=Equipment, to_field='_id', on_delete=models.CASCADE)
    patient_id = models.CharField(max_length=11, editable=False, null=False)
