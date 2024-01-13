from rest_framework import serializers
from .models import PressureMonitor

class PressureMonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PressureMonitor
        fields = [
            "id",
            "local_pressure_monitor_test",
            "measuring_blood_repressure_test",
            "result_pressure_monitor_test",
            "created_at",
            "updated_at",
            "patient_id",
            "user_id",
            "pressureMonitorBatch_id",
            "active",      
        ]
       