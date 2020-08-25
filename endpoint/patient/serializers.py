from rest_framework import serializers
from endpoint.patient.models import Patient
from django.utils.translation import gettext_lazy as _

# from user.models import User


class PatientSerializer(serializers.ModelSerializer):

    _id = serializers.RegexField(
        regex=r'^[\d]{11}', required=True, max_length=11)
    collects = serializers.ListField()

    class Meta:

        model = Patient
        fields = ("__all__")
        extra_kwargs = {'_id': {'error_messages': {
            'invalid': _("A user with that email already exists.")}}}
