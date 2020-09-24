from rest_framework import serializers, status
from rest_framework.exceptions import NotFound

from endpoint.equipment.models import Equipment
from endpoint.sensor.models import Sensor


from bson.objectid import ObjectId


class EquipmentSerializer(serializers.ModelSerializer):
    sensors = serializers.ListField(required=True)

    class Meta:
        model = Equipment
        fields = ("__all__")

    def create(self, validated_data):
        _sensors = validated_data['sensors']
        for index in range(len(_sensors)):
            try:
                sensor = Sensor.objects.get(_id=ObjectId(_sensors[index]))
            except:
                raise NotFound(
                    detail=f"A sensor with _id:{_sensors[index]} was not found.")
        return super().create(validated_data)
