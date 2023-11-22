from rest_framework import generics
from .models import BreathalyzerBatch
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import BreathalyzerBatchSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrProfessional

class BreathalyzerBatchsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrProfessional]
    queryset = BreathalyzerBatch.objects.all().order_by('surname_breathalyzer')
    serializer_class = BreathalyzerBatchSerializer


class BreathalyzerBatchsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrProfessional]
    queryset = BreathalyzerBatch.objects.all()
    serializer_class = BreathalyzerBatchSerializer

    lookup_url_kwarg = "breathalyzerBatch_id"