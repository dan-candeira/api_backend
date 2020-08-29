from rest_framework import serializers

from endpoint.equipment.models import Equipment


class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = ("__all__")
