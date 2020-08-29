from rest_framework import serializers


class SensorSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
