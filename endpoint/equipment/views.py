from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from django.http.response import JsonResponse

from rest_framework.exceptions import NotFound

from endpoint.equipment.serializers import EquipmentSerializer
from endpoint.equipment.models import Equipment

from django_filters.rest_framework import DjangoFilterBackend
from json import loads


class EquipmentViewSet(viewsets.ModelViewSet):

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    filter_backends = [DjangoFilterBackend]

    def retrieve(self, request, *args, **kwargs):
        try:
            equipment = Equipment.objects.get(_id=kwargs['pk'])
        except Exception:
            raise NotFound(
                detail=f"equipment with _id:{kwargs['pk']} was not found.", code=status.HTTP_404_NOT_FOUND)
        serializer = EquipmentSerializer(equipment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        try:
            equipment = Equipment.objects.get(_id=kwargs['pk'])
        except Exception:
            raise NotFound(
                detail=f"equipment with _id:{kwargs['pk']} was not found.", code=status.HTTP_404_NOT_FOUND)

        data = loads(request.body)

        for (key, value) in data.items():
            setattr(equipment, key, value)
        equipment.save()

        serializer = EquipmentSerializer(equipment)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        try:
            equipment = Equipment.objects.get(_id=kwargs['pk'])
        except Exception:
            raise NotFound(
                detail=f"equipment with _id:{kwargs['pk']} was not found.", code=status.HTTP_404_NOT_FOUND)
        equipment.delete()
        return JsonResponse({'data': f'{equipment}'}, status=status.HTTP_204_NO_CONTENT)
