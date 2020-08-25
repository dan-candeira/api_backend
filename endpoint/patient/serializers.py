from rest_framework import serializers, status
from rest_framework.views import exception_handler
from endpoint.patient.models import Patient
from django.utils.translation import gettext_lazy as _

# from user.models import User


class PatientSerializer(serializers.ModelSerializer):

    _id = serializers.RegexField(
        regex=r'^[\d]{11}', required=True, max_length=11)
    collects = serializers.ListField(required=False)

    class Meta:

        model = Patient
        fields = ("__all__")

    def create(self, validated_data):

        data = validated_data

        try:
            currentUser = patient = None

            currentUser = self.context['request'].user
            patient = Patient.objects.get(_id=data['_id'])

        except Exception:

            if patient:

                msg = _("a user with that id was alredy registered.")
                raise serializers.ValidationError(
                    msg, code='duplicated_key')

            # verify if a user was authenticated and add his information to the database
            if (str(currentUser) != "AnonymousUser"):

                data["registered_by"] = currentUser

                return super().create(data)

            return super().create(data)
