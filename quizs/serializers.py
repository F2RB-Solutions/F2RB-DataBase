from rest_framework import serializers
from .models import Quiz


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = [
            "id",
            "regular_medication",
            "description_regular_medication",
            "consumed_alcoholic",
            "description_consumed_alcoholic",
            "consumed_drugs",
            "description_consumed_drugs",
            "result",
            "created_at",
            "updated_at",
            "user_id",
            "patient_id",
            "active",
        ]
        extra_kwargs = {
            'description_regular_medication': {'allow_blank': True},
            'description_consumed_alcoholic': {'allow_blank': True},
            'description_consumed_drugs': {'allow_blank': True},
        }