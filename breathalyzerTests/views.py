from rest_framework import generics
from .models import BreathalyzerTest
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import BreathalyzerTestSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrProfessional
from django.shortcuts import get_object_or_404
from users.models import User
from patients.models import Patient
from breathalyzerBatchs.models import BreathalyzerBatch
class BreathalyzerTestsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrProfessional]
    queryset = BreathalyzerTest.objects.all().order_by('result_breathalyzer_test')
    serializer_class = BreathalyzerTestSerializer

    def perform_create(self, serializer):
        breathalyzerBatch_id = self.request.data["breathalyzerBatch_id"]
        breathalyzerBatch = get_object_or_404(BreathalyzerBatch, pk=breathalyzerBatch_id)
        user_id = self.request.data["user_id"]
        user = get_object_or_404(User, pk=user_id)
        patient_id = self.request.data["patient_id"]
        patient = get_object_or_404(Patient, pk=patient_id)
        serializer.save(breathalyzerBatch=breathalyzerBatch,user=user, patient=patient)

class BreathalyzerTestsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrProfessional]
    queryset = BreathalyzerTest.objects.all()
    serializer_class = BreathalyzerTestSerializer

    lookup_url_kwarg = "breathalyzerTest_id"