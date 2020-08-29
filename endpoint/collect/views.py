from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins

from endpoint.collect.serializers import CollectSerializer
from endpoint.collect.models import Collect

from django_filters.rest_framework import DjangoFilterBackend


class CollectViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Collect.objects.all()
    serializer_class = CollectSerializer
    filter_backends = [DjangoFilterBackend]

    def update(self, request, *args, **kwargs):
        kwargs['_id'] = kwargs['pk']
        del kwargs['pk']

        return super().update(request, *args, **kwargs)
