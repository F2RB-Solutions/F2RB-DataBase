from rest_framework import serializers
from .models import BreathalyzerTest

class BreathalyzerTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BreathalyzerTest
        fields = [
            "id",
            "result_breathalyzer_test",
            "local_breathalyzer_test",
            "created_at",
            "updated_at",
            "breathalyzerBatch_id",
            "user_id",
            "patient_id",
            "active",      
        ]
       