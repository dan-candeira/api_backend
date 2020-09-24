from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.exceptions import NotFound

from django_filters.rest_framework import DjangoFilterBackend

from endpoint.sensor_type.models import SensorType
from endpoint.sensor_type.serializers import SensorTypeSerializer

from bson.objectid import ObjectId


class SensorTypeViewset(viewsets.ModelViewSet):

    queryset = SensorType.objects.all()
    serializer_class = SensorTypeSerializer
    filter_backends = [DjangoFilterBackend]

    def retrieve(self, request, *args, **kwargs):
        try:
            sensor_type = SensorType.objects.get(_id=ObjectId(kwargs['pk']))
        except Exception:
            raise NotFound(
                detail='A sensor type with this _id was not found.', code=status.HTTP_404_NOT_FOUND)

        serializer = SensorTypeSerializer(sensor_type)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        try:
            sensor_type = SensorType.objects.get(_id=ObjectId(kwargs['pk']))
        except Exception:
            raise NotFound(
                detail='A sensor type with this _id was not found.', code=status.HTTP_404_NOT_FOUND)

        sensor_type.delete()

        return JsonResponse({'data': f'{sensor_type}'}, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        try:
            sensor_type = SensorType.objects.get(_id=ObjectId(kwargs['pk']))
        except Exception:
            raise NotFound(
                detail='A sensor type with this _id was not found.', code=status.HTTP_404_NOT_FOUND)

        for (key, value) in sensor_type.items():
            if (key != '_id'):
                sensor_type[key] = value

        sensor_type.save()
        serializer = SensorTypeSerializer(sensor_type)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
