from rest_framework import generics
from .models import DrugTest
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import DrugTestSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrProfessional
from django.shortcuts import get_object_or_404
from users.models import User
from patients.models import Patient
from drugTestBatchs.models import DrugTestBatch
class DrugTestsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrProfessional]
    queryset = DrugTest.objects.all().order_by('result_drug_test')
    serializer_class = DrugTestSerializer

    def perform_create(self, serializer):
        drugTestBatch_id = self.request.data["drugTestBatch_id"]
        drugTestBatch = get_object_or_404(DrugTestBatch, pk=drugTestBatch_id)
        user_id = self.request.data["user_id"]
        user = get_object_or_404(User, pk=user_id)
        patient_id = self.request.data["patient_id"]
        patient = get_object_or_404(Patient, pk=patient_id)
        
        serializer.save(drugTestBatch=drugTestBatch,user=user, patient=patient)

class DrugTestsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrProfessional]
    queryset = DrugTest.objects.all()
    serializer_class = DrugTestSerializer

    lookup_url_kwarg = "drugTest_id"