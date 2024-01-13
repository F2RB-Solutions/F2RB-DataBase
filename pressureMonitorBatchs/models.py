from django.db import models
import uuid


class PressureMonitorBatch(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    surname_pressure_monitor = models.CharField(max_length=150, unique=True)
    serial_number_pressure_monitor = models.CharField(max_length=150)
    lote_number_pressure_monitor = models.CharField(max_length=150)
    certificate_number_pressure_monitor = models.CharField(max_length=150)
    model_pressure_monitor = models.CharField(max_length=150)
    brand_pressure_monitor = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
   
    def __repr__(self) -> str:
        return f"<DrugTestBatch ({self.id}) - {self.surname_pressure_monitor}>"
