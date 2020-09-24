from rest_framework import serializers

from endpoint.sensor_type.models import SensorType


class SensorTypeSerializer(serializers.ModelSerializer):
    mesuaring_dimentions = serializers.ListField(required=True)

    class Meta:
        model = SensorType
        fields = ("__all__")
        read_only = ('_id',)
