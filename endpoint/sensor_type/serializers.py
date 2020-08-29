from rest_framework import serializers


class SensorTypeSerializer(serializers.ModelSerializer):
    mesuaring_dimentions = serializers.ListField(required=True)

    def create(self, validated_data):
        return super().create(validated_data)
