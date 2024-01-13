from rest_framework import serializers
from .models import PressureMonitorBatch
from pressureMonitor.serializers import PressureMonitorSerializer
class PressureMonitorBatchSerializer(serializers.ModelSerializer):
    pressureMonitors = PressureMonitorSerializer(many=True, read_only=True)
    class Meta:
        model = PressureMonitorBatch
        fields = [
            "id",
            "surname_pressure_monitor",
            "serial_number_pressure_monitor",
            "lote_number_pressure_monitor",
            "certificate_number_pressure_monitor",
            "model_pressure_monitor",
            "brand_pressure_monitor",
            "created_at",
            "updated_at",
            "active",   
            "pressureMonitors",    
        ]
       