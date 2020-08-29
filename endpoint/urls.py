from rest_framework.routers import DefaultRouter
from django.urls import path, include

from endpoint.patient.views import PatientViewSet
from endpoint.equipment.views import EquipmentViewSet
from endpoint.collect.views import CollectViewSet
from endpoint.loan_history.views import LoanHistoryViewSet


app_name = 'api'
router = DefaultRouter()

router.register('patient', PatientViewSet)
router.register('equipment', EquipmentViewSet)
router.register('collect', CollectViewSet)
router.register('loan-history', LoanHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
