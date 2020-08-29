from djongo import models
from django.utils import timezone

from endpoint.equipment.models import Equipment
from endpoint.patient.models import Patient


class LoanHistory(models.Model):
    _id = models.ObjectIdField()
    equipment = models.ForeignKey(
        to=Equipment, to_field='_id', on_delete=models.CASCADE)
    patient = models.ForeignKey(
        to=Patient, to_field='_id', on_delete=models.CASCADE)
    loan_date = models.DateTimeField(default=timezone.now)
    devolution_date = models.DateTimeField(null=True)
