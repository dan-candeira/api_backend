from djongo import models

from endpoint.collect.models import Collect


class Sample(models.Model):
    _id = models.AutoField(primary_key=True)
    header = models.JSONField(null=False, editable=False)
    time_start = models.DateTimeField(editable=False)
    time_end = models.DateTimeField(editable=False)
    captured_data = models.JSONField(editable=False, null=False, blank=False)
    collect = models.ForeignKey(
        to=Collect, on_delete=models.CASCADE, to_field="_id")
