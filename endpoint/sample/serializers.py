from rest_framework import serializers

from endpoint.sample.models import Sample


class SampleSerializer(serializers.ModelSerializer):
    data_captured = serializers.ListField(required=True)

    class Meta:

        model = Sample
        fields = ("__all__")
