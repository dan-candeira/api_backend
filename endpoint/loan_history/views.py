from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins

from endpoint.loan_history.serializers import LoanHistorySerializer
from endpoint.loan_history.models import LoanHistory

from django_filters.rest_framework import DjangoFilterBackend


class LoanHistoryViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin):

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = LoanHistory.objects.all()
    serializer_class = LoanHistorySerializer
    filter_backends = [DjangoFilterBackend]
