from rest_framework import generics
from .models import DrugTestBatch
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import DrugTestBatchSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrProfessional

class DrugTestBatchsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrProfessional]
    queryset = DrugTestBatch.objects.all().order_by('surname_drug_test_batch')
    serializer_class = DrugTestBatchSerializer


class DrugTestBatchsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrProfessional]
    queryset = DrugTestBatch.objects.all()
    serializer_class = DrugTestBatchSerializer

    lookup_url_kwarg = "drugTestBatch_id"