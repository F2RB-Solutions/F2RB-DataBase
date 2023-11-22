from rest_framework import serializers
from .models import DrugTestBatch
from drugTests.serializers import DrugTestSerializer
class DrugTestBatchSerializer(serializers.ModelSerializer):
    drugTests = DrugTestSerializer(many=True, read_only=True)
    class Meta:
        model = DrugTestBatch
        fields = [
            "id",
            "surname_drug_test_batch",
            "register_drug_test_batch",
            "validity_drug_test_batch",
            "method_drug_test_batch",
            "created_at",
            "updated_at",
            "active",   
            "drugTests",    
        ]
       