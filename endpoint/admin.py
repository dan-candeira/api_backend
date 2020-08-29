from django.contrib import admin

from endpoint.patient.models import Patient
from endpoint.collect.models import Collect

admin.site.register(Patient)
admin.site.register(Collect)
