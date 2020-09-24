from rest_framework import serializers
from rest_framework.exceptions import NotFound, ValidationError

from django.utils.translation import gettext_lazy as _

from endpoint.loan_history.models import LoanHistory
from endpoint.equipment.models import Equipment
from endpoint.patient.models import Patient
from bson.objectid import ObjectId


class LoanHistorySerializer(serializers.ModelSerializer):
    devolution_date = serializers.DateTimeField(required=False)
    patient = serializers.CharField(required=True)

    class Meta:
        model = LoanHistory
        fields = ("__all__")

    def create(self, validated_data):

        recieved_data = validated_data
        equipment = recieved_data['equipment']
        patient_id = recieved_data['patient']

        try:
            patient = Patient.objects.get(_id=patient_id)
        except Exception:
            raise NotFound(
                detail=f"A patient with _id:{patient_id} does not exists.")

        recieved_data['patient'] = patient

        if (equipment.available):
            equipment.available = False
            equipment.save()
            return super().create(recieved_data)

        msg = _("this equipment is alredy being used.")
        raise ValidationError(msg)
