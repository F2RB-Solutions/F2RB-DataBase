from rest_framework import serializers
from .models import BreathalyzerBatch
from breathalyzerTests.serializers import BreathalyzerTestSerializer
class BreathalyzerBatchSerializer(serializers.ModelSerializer):
    breathalyzerTests = BreathalyzerTestSerializer(many=True, read_only=True)
    class Meta:
        model = BreathalyzerBatch
        fields = [
            "id",
            "surname_breathalyzer",
            "serial_number_breathalyzer",
            "certificate_number_breathalyzer",
            "created_at",
            "updated_at",
            "active",      
            "breathalyzerTests",   
        ]
       