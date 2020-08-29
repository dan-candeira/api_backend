from djongo import models
from django.utils import timezone
from django.core.validators import EmailValidator


class Patient(models.Model):
    _id = models.CharField(null=False, unique=True,
                           primary_key=True, max_length=11)
    birth_date = models.DateField(null=True)
    first_name = models.CharField(null=False, max_length=255)
    last_name = models.CharField(null=False, max_length=255)
    email = models.EmailField(blank=True,
                              null=True, validators=[EmailValidator, ])
    phone = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    lat = models.CharField(max_length=255, null=True)
    long = models.CharField(max_length=255, null=True)
    collects = models.JSONField(
        null=True, blank=True, editable=False, default=[])
    registration_date = models.DateTimeField(default=timezone.now)
    registered_by = models.EmailField(blank=True,
                                      null=True, validators=[EmailValidator, ])
