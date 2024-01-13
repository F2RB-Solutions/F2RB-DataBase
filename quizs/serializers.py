from rest_framework import serializers
from .models import Quiz


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = [
            "id",
            "select_corresponding_unit",
            "change_in_health",
            "description_change_in_health",
            "pain_moment",
            "description_pain_moment",
            "noticed_change_concentration",
            "description_noticed_change_concentration",
            "noticing_changes_sleep",
            "description_noticing_changes_sleep",
            "alters_ability_activities",
            "description_alters_ability_activities",
            "currently_locomotor_difficulties",
            "description_currently_locomotor_difficulties",
            "recent_changes_mood",
            "description_recent_changes_mood",
            "regular_medication",
            "description_regular_medication",
            "consumed_alcoholic",
            "consumed_drugs",
            "description_consumed_drugs",
            "created_at",
            "updated_at",
            "user_id",
            "patient_id",
            "active",
        ]
        extra_kwargs = {
            'description_change_in_health': {'allow_blank': True},
            'description_pain_moment': {'allow_blank': True},
            'description_noticed_change_concentration': {'allow_blank': True},
            'description_noticing_changes_sleep': {'allow_blank': True},
            'description_alters_ability_activities': {'allow_blank': True},
            'description_currently_locomotor_difficulties': {'allow_blank': True},
            'description_recent_changes_mood': {'allow_blank': True},
            'description_regular_medication': {'allow_blank': True},
            'description_consumed_drugs': {'allow_blank': True},   
        }