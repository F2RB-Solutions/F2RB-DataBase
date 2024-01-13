from rest_framework import generics
from .models import PressureMonitor
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import PressureMonitorSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrProfessional
from django.shortcuts import get_object_or_404
from users.models import User
from patients.models import Patient
from pressureMonitorBatchs.models import PressureMonitorBatch
class PressureMonitorsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrProfessional]
    queryset = PressureMonitor.objects.all().order_by('result_pressure_monitor_test')
    serializer_class = PressureMonitorSerializer

    def perform_create(self, serializer):
        pressureMonitorBatch_id = self.request.data["pressureMonitorBatch_id"]
        pressureMonitorBatch = get_object_or_404(PressureMonitorBatch, pk=pressureMonitorBatch_id)
        user_id = self.request.data["user_id"]
        user = get_object_or_404(User, pk=user_id)
        patient_id = self.request.data["patient_id"]
        patient = get_object_or_404(Patient, pk=patient_id)
        
        serializer.save(pressureMonitorBatch=pressureMonitorBatch,user=user, patient=patient)

class PressureMonitorsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrProfessional]
    queryset = PressureMonitor.objects.all()
    serializer_class = PressureMonitorSerializer

    lookup_url_kwarg = "pressureMonitor_id"