from rest_framework import serializers
from .models import DrugTest

class DrugTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugTest
        fields = [
            "id",
            "result_drug_test",
            "local_drug_test",
            "created_at",
            "updated_at",
            "patient_id",
            "user_id",
            "drugTestBatch_id",
            "active",      
        ]
       