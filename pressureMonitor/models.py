from django.db import models
import uuid

class PressureMonitor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    local_pressure_monitor_test = models.CharField(max_length=150)
    measuring_blood_repressure_test = models.CharField(max_length=150)
    result_pressure_monitor_test = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    pressureMonitorBatch = models.ForeignKey(
        "pressureMonitorBatchs.PressureMonitorBatch",
        related_name="pressureMonitors",
        on_delete=models.CASCADE, null=True
    )
    user = models.ForeignKey(
        "users.User",
        related_name="pressureMonitors",
        on_delete=models.CASCADE, null=True
    )  
    patient = models.ForeignKey(
        "patients.Patient",
        related_name="pressureMonitors",
        on_delete=models.CASCADE, null=True
    )    
   
    def __repr__(self) -> str:
        return f"<PressureMonitors ({self.id}) - {self.result_pressure_monitor_test}>"
