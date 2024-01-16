from rest_framework import serializers
from .models import Patient
from rest_framework.validators import UniqueValidator
from quizs.serializers import QuizSerializer
from drugTests.serializers import DrugTestSerializer
from breathalyzerTests.serializers import BreathalyzerTestSerializer
class PatientSerializer(serializers.ModelSerializer):
    quizs = QuizSerializer(many=True, read_only=True)
    drugTests = DrugTestSerializer(many=True, read_only=True)
    breathalyzerTests = BreathalyzerTestSerializer(many=True, read_only=True)
    
    class Meta:
        model = Patient
        fields = [
            "id",
            "username",
            "cpf",
            "role",
            "date_birth",
            "email",
            "tel",
            "created_at",
            "updated_at",
            "active",
            "client_id",
            "quizs",
            "drugTests",
            "breathalyzerTests",           
        ]
        extra_kwargs = {
            'role': {'allow_blank': True},
            'date_birth': {'allow_blank': True},
            'email': {'allow_blank': True},
            'tel': {'allow_blank': True},
            "client": {"read_only": False},
            # "email": {
            #     "validators": [
            #         UniqueValidator(
            #             queryset=Patient.objects.all(),
            #             message="A user with that email already exists.",
            #         )
            #     ]
            # },
        }