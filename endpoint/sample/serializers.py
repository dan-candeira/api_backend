from rest_framework import serializers
from rest_framework.exceptions import NotFound
import time

from django.utils import timezone
from datetime import datetime

from endpoint.sample.models import Sample
from endpoint.collect.models import Collect
from django.utils.translation import ugettext_lazy as _

from bson.objectid import ObjectId


class SampleSerializer(serializers.ModelSerializer):
    captured_data = serializers.ListField(required=True)
    header = serializers.ListField(required=True)
    collect = serializers.CharField(required=True)

    class Meta:

        model = Sample
        fields = ("__all__")
        extra_kwargs = {
            '_id': {'read_only': True},
            'header': {
                'required': True
            },
        }

    def create(self, validated_data):
        data = validated_data
        header = data['header']
        collect_id = data['collect']
        size_error = False

        if len(data['captured_data']) != len(header):
            size_error = True

        if size_error:
            msg = _(
                "the size of your header did not match the size of values per 'line' in your sample.")
            raise serializers.ValidationError(msg, code='parse_error')

        try:
            collect = Collect.objects.get(_id=ObjectId(collect_id))
        except Exception:
            raise NotFound(
                detail=f"A collect with _id:{collect_id} was not found.")

        data['collect'] = collect

        # add timesleep to verify if it will be reflected on the script
        # time_stamp_ini = datetime.now()
        # time.sleep(25)
        # time_stamp_final = datetime.now()
        # print(time_stamp_final - time_stamp_ini)

        return super().create(data)
