# handles authentication and authorization
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# create a viewset
from rest_framework import viewsets

# handles responses rest framework
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed
from django.http.response import JsonResponse
from rest_framework import status
from django.http import Http404

# handles id conversion from database
from bson.objectid import ObjectId
from bson.json_util import loads


from endpoint.collect.serializers import CollectSerializer
from endpoint.collect.models import Collect

from django_filters.rest_framework import DjangoFilterBackend


class CollectViewSet(viewsets.ModelViewSet):

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Collect.objects.all()
    serializer_class = CollectSerializer
    filter_backends = [DjangoFilterBackend]

    def retrieve(self, request, *args, **kwargs):

        try:
            collect = Collect.objects.get(_id=ObjectId(kwargs['pk']))
        except Exception:
            raise Http404

        serializer = CollectSerializer(collect)

        return Response(serializer.data)

    # verify if this method with profº
    def update(self, request, *args, **kwargs):

        raise MethodNotAllowed('update')

    def destroy(self, request, *args, **kwargs):
        try:
            collect = Collect.objects.get(_id=ObjectId(kwargs['pk']))
        except Exception:
            raise Http404
        collect_id = collect._id
        collect.delete()

        return JsonResponse({'data': f'{collect}'}, status=status.HTTP_204_NO_CONTENT)
