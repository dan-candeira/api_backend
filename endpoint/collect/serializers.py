from rest_framework import serializers
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework import status

from django.utils import timezone
import datetime

from django.utils.translation import gettext_lazy as _

from endpoint.collect.models import Collect
from endpoint.patient.models import Patient
from endpoint.equipment.models import Equipment
from endpoint.loan_history.models import LoanHistory


class CollectSerializer(serializers.ModelSerializer):
    samples = serializers.ListField()
    timestamp_init = serializers.DateTimeField()
    timestamp_fin = serializers.DateTimeField()

    class Meta:
        model = Collect
        fields = ("__all__")
        extra_kwargs = {'_id': {'read_only': True}}

    def create(self, validated_data):
        recieved_data = validated_data
        equipment = recieved_data['equipment']

        last_collect = Collect.objects.filter(
            equipment_id=equipment._id).latest('timestamp_init')

        if last_collect.timestamp_init.date() == timezone.now().date():
            return last_collect

        # the rest of this code only will be executed
        # if the conditional above is false

        recieved_data['timestamp_init'] = timezone.now()

        if (equipment.available):
            msg = _("the equipment with id provided is not being used.")
            raise ValidationError(
                detail=msg)

        loan = LoanHistory.objects.get(equipment_id=equipment._id)

        recieved_data['patient_id'] = loan.patient_id
        recieved_data['timestamp_fin'] = timezone.now()

        return super().create(recieved_data)
