from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins

from endpoint.patient.serializers import PatientSerializer
from endpoint.patient.models import Patient

from django_filters.rest_framework import DjangoFilterBackend


class PatientViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [DjangoFilterBackend]
