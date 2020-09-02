from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed, NotFound
from rest_framework import status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from endpoint.sample.models import Sample
from endpoint.sample.serializers import SampleSerializer
from endpoint.collect.models import Collect

from bson.objectid import ObjectId
from bson.json_util import loads


class SampleViewSet(viewsets.ModelViewSet):

    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    filter_backends = [DjangoFilterBackend]

    def retrieve(self, request, *args, **kwargs):
        try:
            sample = Sample.objects.get(_id=ObjectId(kwargs['pk']))
        except Exception:
            raise NotFound(detail="A smaple with this _id was not found.")

        serializer = SampleSerializer(sample)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed('update')

    def destroy(self, request, *args, **kwargs):
        try:
            sample = Sample.objects.get(_id=ObjectId(kwargs['pk']))
        except Exception:
            raise NotFound(detail="A smaple with this _id was not found.")
        sample.delete()

        serializer = SampleSerializer(sample)

        return Response(data=serializer.data, status=status.HTTP_204_NO_CONTENT)
