from rest_framework import generics, serializers
from .models import Quiz
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import QuizSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrProfessional
from django.shortcuts import get_object_or_404
from users.models import User
from patients.models import Patient
from django.utils import timezone
class QuizsView(generics.ListCreateAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAdminOrProfessional]
    queryset = Quiz.objects.all().order_by('select_corresponding_unit')
    serializer_class = QuizSerializer

    def perform_create(self, serializer):
        user_id = self.request.data["user_id"]
        user = get_object_or_404(User, pk=user_id)
        patient_id = self.request.data["patient_id"]
        patient = get_object_or_404(Patient, pk=patient_id)

        
        if Quiz.objects.filter(
            patient=patient,
            created_at__gte=timezone.now() - timezone.timedelta(hours=16),
        ).exists():
        
            raise serializers.ValidationError("Usuário já fez um questionário nas últimas 16 horas.")

        serializer.save(user=user, patient=patient)

class QuizsDetailView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated, IsAdminOrProfessional]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    lookup_url_kwarg = "quiz_id"