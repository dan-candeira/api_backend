from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from django.http.response import JsonResponse

from endpoint.loan_history.serializers import LoanHistorySerializer
from endpoint.loan_history.models import LoanHistory
from endpoint.equipment.models import Equipment

from django_filters.rest_framework import DjangoFilterBackend

from bson.objectid import ObjectId
from bson.json_util import loads


class LoanHistoryViewSet(viewsets.ModelViewSet):

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = LoanHistory.objects.all()
    serializer_class = LoanHistorySerializer
    filter_backends = [DjangoFilterBackend]

    def retrieve(self, request, *args, **kwargs):

        try:
            loan_history = LoanHistory.objects.get(_id=ObjectId(kwargs['pk']))
        except Exception:
            raise NotFound

        serializer = LoanHistorySerializer(loan_history)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):

        try:
            loan_history = LoanHistory.objects.get(_id=ObjectId(kwargs['pk']))
        except Exception:
            raise NotFound

        loan_history.delete()

        return JsonResponse({'data': f'{loan_history}'}, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):

        data = loads(request.body)

        try:
            loan_history = LoanHistory.objects.get(_id=ObjectId(kwargs['pk']))
        except Exception:
            raise NotFound

        for (key, value) in data.items():
            if (key == 'devolution_date'):
                setattr(loan_history, key, value)
        loan_history.save()

        devolution_date = loan_history.devolution_date

        if (devolution_date != None):
            equipment = Equipment.objects.get(
                _id=loan_history.equipment_id)
            setattr(equipment, 'available', True)
            equipment.save()

        serializer = LoanHistorySerializer(loan_history)

        return Response(serializer.data, status=status.HTTP_200_OK)
