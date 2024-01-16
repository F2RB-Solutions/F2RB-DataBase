from rest_framework import generics
from .models import Patient
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import PatientSerializer
from rest_framework.permissions import IsAuthenticated
from clients.models import Client
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class PatientsView(generics.ListCreateAPIView):
    # authentication_classes = [JWTAuthentication]
    queryset = Patient.objects.all().order_by('username')
    serializer_class = PatientSerializer

    def perform_create(self, serializer):
        client_id = self.request.data["client_id"]
        client = get_object_or_404(Client, pk=client_id)
        serializer.save(client=client)

class PatientsDetailView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    lookup_url_kwarg = "patient_id"
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        client_id = request.data.get("client_id")
        if client_id:
            client = get_object_or_404(Client, pk=client_id)
            instance.client = client

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)