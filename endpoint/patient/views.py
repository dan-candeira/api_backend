from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.exceptions import NotFound

from endpoint.patient.serializers import PatientSerializer
from endpoint.patient.models import Patient

from django_filters.rest_framework import DjangoFilterBackend

from json import loads


class PatientViewSet(viewsets.ModelViewSet):

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [DjangoFilterBackend]

    def retrieve(self, request, *args, **kwargs):
        try:
            patient = Patient.objects.get(_id=kwargs['pk'])
        except Exception:
            raise NotFound(
                detail=f"A patient with _id:{kwargs['pk']} was not found.", code=status.HTTP_404_NOT_FOUND)
        serializer = PatientSerializer(patient)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        try:
            patient = Patient.object.get(_id=kwargs['pk'])
        except Exception:
            raise NotFound(
                detail=f"A patient with _id:{kwargs['pk']} was not found.", code=status.HTTP_404_NOT_FOUND)

        data = loads(request.body)

        for (key, value) in data.items():
            setattr(patient, key, value)
        patient.save()

        serializer = PatientSerializer(patient)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        try:
            patient = Patient.objects.get(_id=kwargs['pk'])
        except Exception:
            raise NotFound(
                detail=f"A patient with _id:{kwargs['pk']} was not found.", code=status.HTTP_404_NOT_FOUND)

        patient.delete()
        return JsonResponse({'data': f'{patient}'}, status=status.HTTP_204_NO_CONTENT)
