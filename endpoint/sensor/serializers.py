from rest_framework import serializers, status
from rest_framework.exceptions import NotFound

from endpoint.sensor.models import Sensor
from endpoint.sensor_type.models import SensorType
from bson.objectid import ObjectId


class SensorSerializer(serializers.ModelSerializer):
    types = serializers.ListField(required=True)

    class Meta:
        model = Sensor
        fields = ("__all__")

    def create(self, validated_data):
        _types = validated_data['types']
        for index in range(len(_types)):
            try:
                sensor_type = SensorType.objects.get(
                    _id=ObjectId(_types[index]))
            except Exception:
                raise NotFound(
                    detail="A sensor type with this _id was not found.", code=status.HTTP_404_NOT_FOUND)
        validated_data['types'] = _types
        return super().create(validated_data)
