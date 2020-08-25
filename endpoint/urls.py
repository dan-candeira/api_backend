from rest_framework.routers import DefaultRouter
from django.urls import path, include

from endpoint.patient.views import PatientViewSet


app_name = 'api'
router = DefaultRouter()

router.register('patient', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
