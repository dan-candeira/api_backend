from rest_framework import serializers
from rest_framework.exceptions import NotFound, ValidationError

from django.utils.translation import gettext_lazy as _

from endpoint.loan_history.models import LoanHistory
from endpoint.equipment.models import Equipment


class LoanHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = LoanHistory
        fields = ("__all__")

    def create(self, validated_data):

        recieved_data = validated_data
        equipment = recieved_data['equipment']

        if (equipment.available):
            equipment.available = False
            equipment.save()
            return super().create(recieved_data)

        msg = _("this equipment is alredy being used.")
        raise ValidationError(msg)
