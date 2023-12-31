from rest_framework import generics
from .models import Client
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ClientSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrProfessional

class ClientsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrProfessional]
    
    queryset = Client.objects.all().order_by('client_name')
    serializer_class = ClientSerializer


class ClientsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrProfessional]

    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    lookup_url_kwarg = "client_id"