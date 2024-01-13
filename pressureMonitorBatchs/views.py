from rest_framework import generics
from .models import PressureMonitorBatch
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import PressureMonitorBatchSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrProfessional

class PressureMonitorBatchsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrProfessional]
    queryset = PressureMonitorBatch.objects.all().order_by('surname_pressure_monitor')
    serializer_class = PressureMonitorBatchSerializer


class PressureMonitorBatchsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrProfessional]
    queryset = PressureMonitorBatch.objects.all()
    serializer_class = PressureMonitorBatchSerializer

    lookup_url_kwarg = "pressureMonitorBatch_id"