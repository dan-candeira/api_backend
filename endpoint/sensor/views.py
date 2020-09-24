from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.exceptions import NotFound

from endpoint.sensor.models import Sensor
from endpoint.sensor.serializers import SensorSerializer

from django_filters.rest_framework import DjangoFilterBackend

from bson.objectid import ObjectId


class SensorViewSet(viewsets.ModelViewSet):

    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filter_backends = [DjangoFilterBackend]

    def retrieve(self, request, *args, **kwargs):
        try:
            sensor = Sensor.objects.get(_id=ObjectId(kwargs['pk']))
        except Exception:
            raise NotFound(
                detail='A sensor type with this _id was not found.', code=status.HTTP_404_NOT_FOUND)

        serializer = SensorSerializer(sensor)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        try:
            sensor = Sensor.objects.get(_id=ObjectId(kwargs['pk']))
        except Exception:
            raise NotFound(
                detail='A sensor type with this _id was not found.', code=status.HTTP_404_NOT_FOUND)

        sensor.delete()

        return JsonResponse({'data': f'{sensor}'}, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        try:
            sensor = Sensor.objects.get(_id=ObjectId(kwargs['pk']))
        except Exception:
            raise NotFound(
                detail='A sensor type with this _id was not found.', code=status.HTTP_404_NOT_FOUND)

        for (key, value) in sensor.items():
            if (key != '_id'):
                sensor[key] = value

        sensor.save()
        serializer = SensorSerializer(sensor)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
